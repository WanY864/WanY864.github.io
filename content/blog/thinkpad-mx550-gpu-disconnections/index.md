---
title: "Diagnosing NVIDIA MX550 GPU Disconnections on a ThinkPad T14 Gen 3"
date: 2026-11-26
draft: false
description: "A collaborative debugging investigation into GPU loss, Windows graphics kernel failures, firmware, power management and a reproducible clock-limiting workaround."
summary: "From recurring Direct3D and CUDA crashes to a practical GPU clock-limiting workaround, using WinDbg and controlled experiments."
tags: ["ThinkPad", "NVIDIA", "Windows", "Debugging", "Hardware"]
---

## The problem

Since buying my ThinkPad, I had experienced recurring crashes whenever an application used the discrete GPU. Games would exit with Direct3D errors, while CUDA training could freeze indefinitely. Even terminating the affected process sometimes failed; restarting Windows was often the only way to recover the GPU.

The problem was particularly noticeable during transitions: loading a new map, returning to a menu, or changing workloads. In Aim Lab, an ongoing training scenario could run normally, yet switching maps could make the graphics device disappear.

On November 26, 2026, I decided to investigate the problem systematically with ChatGPT. I operated the machine, collected logs, changed settings and ran experiments; ChatGPT helped interpret the evidence, propose tests and revise hypotheses. This article documents our joint debugging session, including unsuccessful attempts rather than just the eventual workaround.

**Result:** limiting the MX550 core clock to 1200 MHz produced a successful short test, including near-30 W GPU operation. I subsequently chose a 1350 MHz startup limit and reduced CPU frequency limits for daily use. At the time of writing, the problem appears mitigated, but the underlying hardware or software fault has not been conclusively identified.

## 1. Hardware and software environment

| Component | Configuration |
| --- | --- |
| Laptop | Lenovo ThinkPad T14 Gen 3 Intel (type 21AH) |
| Processor | Intel Core i7-1260P |
| Integrated GPU | Intel Iris Xe |
| Discrete GPU | NVIDIA GeForce MX550, 2 GB |
| Memory | 32 GB |
| Operating system | Windows 11 Home, build 26200 |
| AC adapter | Original Lenovo 65 W USB-C adapter |
| Initial NVIDIA driver | 621.24 |
| Initial BIOS / EC | 1.34 / 1.14 |

The first unexpected discovery was that Windows reported only four CPU cores and four logical processors.

```powershell
Get-CimInstance Win32_Processor |
    Select-Object Name,NumberOfCores,NumberOfLogicalProcessors
```

The i7-1260P should have four performance cores, eight efficiency cores and sixteen logical processors. The boot configuration contained no obvious processor-count restriction. Reading Lenovo's BIOS settings exposed the explanation:

```powershell
Get-CimInstance -Namespace root/wmi -ClassName Lenovo_BiosSetting |
    Select-Object -ExpandProperty CurrentSetting |
    Where-Object { $_ -match 'Core|Thread|CPU|Power|Thermal' }
```

```text
CPUPowerManagement,Disable
HyperThreadingTechnology,Disable
EfficientCores,Disable
```

I enabled these three settings in BIOS and verified that Windows subsequently detected 12 cores and 16 threads. This corrected a separate performance problem, but did not resolve the discrete GPU crashes.

## 2. Looking beyond application errors

Windows Reliability Monitor (`perfmon /rel`) showed repeated hardware-error reports and abnormal shutdowns. Five historical kernel minidumps were available under `C:\Windows\Minidump`.

Using Microsoft's WinDbg, we opened the dumps and ran:

```text
.symfix
.reload
!analyze -v
```

The November 26 dump contained the following diagnostic signature:

```text
VIDEO_DXGKRNL_FATAL_ERROR (113)
Arg1: 0000000000000019
Arg3: 00000000000010de
Arg4: 0000000000001f9f

DirectX.FatalError.Desc: UNEXPECTED_SURPRISE_REMOVAL
IMAGE_NAME: nvlddmkm.sys
FAILURE_BUCKET_ID: 0x113_19_nvlddmkm!unknown_function
```

The stack included `dxgkrnl!DpiFdoHandleDevicePower` and `dxgkrnl!DpiFdoDispatchPower`. However, the power-management stack was not sufficient to identify the initial trigger. Running `!blackboxbsd` showed that a user shutdown was already in progress, and I remembered attempting to restart after the GPU had frozen. The blue screen was therefore likely a secondary failure during recovery.

The November 23 dump was different:

```text
WIN32K_POWER_WATCHDOG_TIMEOUT (19c)
Arg1: 0000000000000050
FAILURE_BUCKET_ID:
0x19C_DRVSETMONITORPOWERSTATE_HANG_dxgkrnl!DxgkPowerOnOffMonitor
```

This was consistent with a monitor power-on request timing out; I recalled that this incident probably occurred while waking the display.

Two additional Reliability Monitor reports carried the following signatures:

```text
LiveKernelEvent 193
LKD_0x193_DxgkrnlLiveDump:815__dxgkrnl!DXGSESSIONMGR::WaitForPnPTransitionDone
LKD_0x193_DxgkrnlLiveDump:810__dxgkrnl!ProcessDeadlockThread
```

Together these reports pointed toward graphics-device availability and state-management failures rather than ordinary application exceptions. They did not establish that a specific physical component was defective.

## 3. Capturing the failure while Windows was still running

The decisive observation came directly from NVIDIA's management utility:

```text
Unable to determine the device handle for GPU0: 0000:03:00.0:
GPU is lost. Reboot the system to recover this GPU

No devices were found
```

Surprisingly, Windows still reported the MX550 as present, with `CM_PROB_NONE`:

```powershell
Get-PnpDevice -Class Display |
    Format-Table Status,FriendlyName,Problem -AutoSize
```

The stored device power state was D0, and PCIe properties still reported a link width of x4. These properties describe Windows' device records and are not proof of live hardware communication.

We attempted a device restart (after saving open work):

```powershell
$gpu = Get-PnpDevice -Class Display |
    Where-Object { $_.FriendlyName -like '*MX550*' }
pnputil /restart-device "$($gpu.InstanceId)"
nvidia-smi
```

The restart operation returned success, but NVIDIA's utility now reported:

```text
Failed to initialize NVML: Not Found
```

Windows subsequently reported `CM_PROB_FAILED_ADD` (Code 31). The underlying problem status was:

```text
0xC0000010 (STATUS_INVALID_DEVICE_REQUEST)
```

This showed that restarting the device did not restore its functionality. No matching WHEA PCIe error or NVIDIA Xid 79 was found in the queried Windows logs. The absence of these events does not rule out a hardware fault.

The logs also contained repeated Kernel-Processor-Power event 37 warnings, indicating firmware-limited CPU performance. That raised questions about platform power management, without proving a connection to the GPU failure.

## 4. Driver, firmware and hardware checks

We tested the Lenovo-provided NVIDIA driver, version 596.52, instead of the newer 621.24 driver. Windows initially continued selecting the newer package even after the Lenovo installer had run. The following command revealed both compatible packages:

```powershell
pnputil /enum-devices /instanceid "$($gpu.InstanceId)" /drivers
```

I manually selected version 32.0.15.9652 in Device Manager and verified 596.52 using `nvidia-smi`. The crashes persisted. Disabling the ToDesk and Oray virtual display adapters also did not prevent recurrence. The major Intel and Lenovo power-management driver versions were checked against the vendor's offerings; no clear missing component was identified.

Lenovo UEFI Diagnostics passed the PCI Express status test, motherboard chipset and PCI/PCIe tests, and fan control test. I could hear the fan accelerate. These tests established basic functionality outside Windows, but the tool did not offer a dedicated MX550 compute or VRAM stress test.

Another discovery was that BIOS 1.34 was paired with EC 1.14, whereas Lenovo's release table lists EC 1.17 alongside that BIOS. The actual versions were confirmed in BIOS. We updated both using the official Lenovo package:

| Firmware | Before | After |
| --- | --- | --- |
| UEFI BIOS | N3BET56W (1.34) | N3BET71W (1.49) |
| Embedded controller | 1.14 | 1.23 |

The release history includes fan-control and power-delivery improvements, making this a worthwhile investigation. Nevertheless, the GPU still disappeared after the update. The previous version pairing was real, but its role in the GPU failure remains unproven.

Firmware flashing is not a routine troubleshooting step on an unstable machine: verify model compatibility, back up important files, check encryption recovery arrangements, ensure stable AC power and a charged battery, and follow Lenovo's instructions. Never interrupt an active firmware update.

## 5. Measuring instead of guessing

We recorded GPU utilization, temperature, power and clocks at approximately one-second intervals:

```powershell
nvidia-smi --query-gpu=timestamp,temperature.gpu,power.draw,pstate,utilization.gpu,clocks.gr,clocks.mem --format=csv -l 1 |
    Tee-Object -FilePath "$env:USERPROFILE\gpu_test.csv"
```

To inspect reported throttling reasons and power limits:

```powershell
nvidia-smi -q -d PERFORMANCE,TEMPERATURE,POWER
```

On battery power, the GPU was limited to 10 W, and the gaming workload reached 100% utilization while the core remained at 300 MHz and memory at 405 MHz. Actual GPU power was around 6.5 W and temperature around 60 degrees Celsius. This was stable during the short observation, but extremely slow.

The driver reported both software power capping and software thermal slowdown. The core temperature was below the listed GPU temperature thresholds, but other platform constraints and unreported sensor values could not be excluded. Battery and AC results must not be interpreted as a controlled firmware comparison.

On AC power, after the firmware update, the GPU returned to its 30 W limit and normal boost behavior. Unfortunately, the fault reappeared. We then switched a customized power plan to Balanced, experimented with NVIDIA power-management modes, and disabled CPU turbo temporarily. The GPU still failed.

### Comparison of the recorded experiments

| Metric | AC, unrestricted, turbo enabled | AC, unrestricted, turbo disabled | AC, core limited to 1200 MHz |
| --- | ---: | ---: | ---: |
| Highest sampled core clock | 1770 MHz | 1800 MHz | 1200 MHz |
| Peak sampled GPU power | 29.90 W | 29.97 W | 29.23 W |
| Peak sampled GPU temperature | 75 C | 67 C | 66 C |
| Memory clock under load | 6000 MHz | 6000 MHz | 6000 MHz |
| Outcome | GPU lost | GPU lost | No loss during recorded test |

The first unrestricted test failed after about 40 seconds of substantial GPU load. Its last valid sample showed 1770 MHz at 16.63 W. The second test failed at 1410 MHz and 29.64 W in the last valid sample, after a similar period of load.

These observations weakened the idea that core overheating alone was responsible. They also showed that the fault did not require a sampled jump to 1770 MHz. The one-second polling interval cannot capture short voltage, current or clock transients, and the tests differed in power settings and workload transitions.

## 6. The workaround that finally helped

Instead of increasing voltage or disabling protections, we reduced the GPU core frequency ceiling using NVIDIA's own management interface.

First we checked available clocks:

```powershell
nvidia-smi -q -d CLOCK,SUPPORTED_CLOCKS
```

The MX550 reported a maximum graphics clock of 2100 MHz and supported clock steps of 15 MHz. In an elevated PowerShell window, with GPU workloads closed, I ran:

```powershell
nvidia-smi -i 0 -lgc 300,1200
```

The command returned:

```text
GPU clocks set to "(gpuClkMin 300, gpuClkMax 1200)" for GPU 00000000:03:00.0
All done.
```

The subsequent Aim Lab test completed without a GPU disconnection, including map changes. I did not notice an obvious loss of playability.

Here are selected samples from that run:

| Time | Temperature | Power | Utilization | Core clock | Memory clock |
| --- | ---: | ---: | ---: | ---: | ---: |
| 21:25:43 | 59 C | 25.37 W | 100% | 1200 MHz | 6000 MHz |
| 21:26:18 | 65 C | 29.09 W | 100% | 1200 MHz | 6000 MHz |
| 21:26:39 | 66 C | 29.23 W | 100% | 1200 MHz | 6000 MHz |
| 21:27:27 | 64 C | 19.63 W | 75% | 1200 MHz | 6000 MHz |

The key observation is that the GPU could approach 30 W while maintaining the reduced core clock, without failing during this short run. Memory frequency remained unchanged.

This supports a hypothesis involving core-clock-dependent stability, voltage/frequency transitions or the transient response of the GPU power supply. It does not prove that the GPU silicon is defective, nor does it rule out driver behavior, VRAM issues or board-level power delivery. The successful log spans less than three minutes, not a formal long-duration reliability test.

I later chose 1350 MHz as a practical daily ceiling. This is a provisional setting, not a proven universal safe frequency. Start with the more conservative 1200 MHz if reproducing the experiment; stop if the machine hangs or the GPU disappears. Clock control may not be supported on other laptop GPUs or drivers.

## 7. Making the GPU limit persistent

The frequency command is a runtime setting, not a VBIOS modification. To reapply it at boot, I created a Windows scheduled task in elevated PowerShell. The following version uses the final 1350 MHz ceiling; substitute 1200 if necessary.

```powershell
$exe = (Get-Command nvidia-smi.exe -ErrorAction Stop).Source

schtasks /create /tn "MX550_ClockLimit" /tr "`"$exe`" -i 0 -lgc 300,1350" /sc onstart /delay 0000:30 /ru SYSTEM /rl HIGHEST /f

$settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -StartWhenAvailable

Set-ScheduledTask -TaskName "MX550_ClockLimit" -Settings $settings
schtasks /run /tn "MX550_ClockLimit"
```

The battery settings matter: the task initially created by schtasks did not allow starting on battery power. I also encountered a Get-ScheduledTask query error despite the task being present, so schtasks was useful as an alternative inspection tool.

```powershell
schtasks /query /tn "MX550_ClockLimit" /v /fo list
Get-ScheduledTaskInfo -TaskName "MX550_ClockLimit"
```

After rebooting, LastRunTime advanced to the new startup time, LastTaskResult was 0 and NumberOfMissedRuns was 0. This verified automatic command execution. Actual clock enforcement should still be checked under normal load using the monitoring command above. Sleep/resume, a driver reset or driver updates may invalidate runtime settings even when the startup task is configured correctly.

To remove the workaround:

```powershell
schtasks /delete /tn "MX550_ClockLimit" /f
nvidia-smi -i 0 -rgc
```

## 8. Reducing CPU power pressure without disabling turbo

The original 65 W adapter has limited headroom when the CPU and discrete GPU are both busy. A higher-capacity compatible USB-C PD adapter is a possible future experiment, but we did not test one.

Rather than using ThrottleStop to write low-level power limits, I opted for Windows' native power plan. I restored CPU turbo and set approximate 80% ceilings relative to the processor's advertised peak clocks: 3.7 GHz for performance cores and 2.7 GHz for efficiency cores.

```powershell
powercfg /setacvalueindex SCHEME_BALANCED SUB_PROCESSOR PERFBOOSTMODE 2
powercfg /setacvalueindex SCHEME_BALANCED SUB_PROCESSOR PROCFREQMAX 2700
powercfg /setacvalueindex SCHEME_BALANCED SUB_PROCESSOR PROCFREQMAX1 3700
powercfg /setactive SCHEME_BALANCED
```

These settings apply to AC power only and persist across reboot. The two processor efficiency classes are intended here for the E-core and P-core ceilings respectively; verify their actual behavior on the machine rather than assuming the mapping or enforcement is universal.

```powershell
powercfg /qh SCHEME_CURRENT SUB_PROCESSOR PROCFREQMAX
powercfg /qh SCHEME_CURRENT SUB_PROCESSOR PROCFREQMAX1
```

Frequency limits are not equivalent to PL1/PL2 wattage limits, and retaining 80% of peak frequency does not guarantee 80% of performance or power. The additional CPU restriction is a precaution, not an independently demonstrated fix.

To remove the added CPU frequency ceilings, set both values back to 0 and reactivate the Balanced plan.

## 9. Where things stand

| Setting | Final configuration |
| --- | --- |
| CPU | 12 cores / 16 threads, turbo enabled |
| CPU AC frequency ceilings | 2700 / 3700 MHz for the two efficiency classes |
| BIOS / EC | 1.49 / 1.23 |
| NVIDIA driver | Lenovo-provided 596.52 |
| Windows power plan | Balanced |
| NVIDIA power-management mode | Prefer consistent performance |
| GPU core clock | 300–1350 MHz via a startup task |
| GPU memory and power limit | Default settings |

At the end of the session, the machine was usable and I considered the immediate problem resolved. The strongest directly logged result remains the 1200 MHz trial; long-term stability at 1350 MHz with CPU turbo restored still needs observation. If it fails again, returning to 1200 MHz is the first step. If failures persist even with conservative settings, professional hardware diagnosis or a separate operating-system test would be more informative than repeatedly forcing crashes.

The lesson from this investigation is that a workaround and a root-cause diagnosis are different things. Firmware updates, driver replacement and lower CPU power demand did not eliminate the failure on their own. Measuring the GPU during real workloads and limiting one of its operating parameters finally provided a useful result without replacing hardware.

This is a case study of one laptop, not evidence of a model-wide defect. No overvolting, firmware modification of the GPU, or disabling of thermal protections was required.

## References and further reading

- [Microsoft: Bug check 0x113 — VIDEO_DXGKRNL_FATAL_ERROR](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/bug-check-0x113---video-dxgkrnl-fatal-error)
- [Microsoft: Bug check 0x19C — WIN32K_POWER_WATCHDOG_TIMEOUT](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/bug-check-0x19c--win32k-power-watchdog-timeout)
- [Microsoft: NVIDIA-independent PnP Code 31 documentation](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/cm-prob-failed-add)
- [NVIDIA System Management Interface documentation](https://docs.nvidia.com/deploy/nvidia-smi/)
- [Lenovo ThinkPad BIOS update utility and release notes](https://support.lenovo.com/us/en/downloads/ds557163)
- [Lenovo ThinkPad T14 Gen 3 Intel specifications](https://psref.lenovo.com/product/ThinkPad/ThinkPad_T14_Gen_3_Intel)

*Acknowledgment: this investigation and article were developed collaboratively with ChatGPT. All physical operations and observations were performed by me; the diagnostic interpretation and write-up were assisted by AI. Identifying device and account information has been removed from the published excerpts.*
