---
title: "HCI — Lab_mobile"
date: 2026-10-12
summary: "Adapt an existing Unity application for mobile interaction and deploy it to an Android phone or emulator."
tags: ["HCI", "Lab", "Mobile", "Unity", "Android"]
categories: ["Human-Computer Interaction"]
draft: false
workType: lab
workStatus: in-progress
workSubtitle: "Mobile interaction · Android deployment"
weight: 40
linkTitle: "HCI — Lab_mobile"
showTableOfContents: true
showReadingTime: true
showWordCount: false
---

> **Work status:** The requirements, mobile design choices and test checklist are prepared. The app has **not been shown to run on a phone or emulator** in this page. Screenshots, build output and real observations must be added after testing.

## What the lab requires

The **Lab2_mobile** slides specify two tasks, worth **15 points in total**:

1. **Implement a Mobile Application (10 points).** Adapt the application implemented in the previous week so it works on a mobile phone. Use an appropriate mobile interaction technique; the slides mention the phone gyroscope as an example. A desktop interaction design should not simply be assumed to work on a phone.
2. **Deploy Mobile Application (5 points).** Set up the development environment and deploy an initial build to a real phone **or an Android emulator**. Document the process.

[Lab materials: ML_agent folder, including Lab2_mobile.pptx](https://drive.google.com/drive/folders/1LXSiqex2GMRSVQd_L829p7vAvmkgcxs2)

## Non-hands-on design preparation

A possible candidate is a previous week's ball-control Unity application, **if that is the actual project being adapted**. The final page should name the real source project and identify what changed.

| Interaction | Typical desktop mapping | Proposed mobile equivalent | Reason |
| --- | --- | --- | --- |
| Move the object | Arrow keys / WASD | Tilt device or drag a virtual joystick | No physical keyboard is available |
| Select an action | Mouse click | Large touch button | Direct finger target |
| Pause / restart | Keyboard shortcut | Persistent on-screen action | Discoverable without remembering keys |
| Feedback | UI in a desktop window | Responsive text and touch-friendly layout | Smaller screen and different viewing distance |

**Choice to validate:** tilting the phone can feel natural for steering, but it can also make the screen harder to read. A touch alternative or sensitivity control could support users who find tilt uncomfortable. The best mapping must be judged after an actual trial, not guessed to be successful.

### Interaction proposal

- Decide on the device orientation (portrait or landscape) and keep the play area readable.
- Calibrate neutral tilt on startup or provide a Reset Calibration action.
- Cap input sensitivity to avoid accidental large movements.
- Place Pause and Restart controls away from the area where the finger typically steers.
- Keep score, win/lose feedback and error messages visible at phone size.
- Support a fallback touch control if the hardware sensor is not available in an emulator.

## Implementation and deployment checks

- [ ] Identify the previous Unity app and record its original desktop control scheme.
- [ ] Add phone-appropriate input (gyro/accelerometer, touch, or another justified technique).
- [ ] Confirm controls, UI layout and text size on a mobile aspect ratio.
- [ ] Install the necessary Android Build Support and SDK/NDK tools for the selected Unity version.
- [ ] Set Android as the target platform and resolve build errors.
- [ ] Build the application, recording the actual Unity version and target device or emulator.
- [ ] Launch the build on **a phone or Android emulator**.
- [ ] Test movement, pause/restart, score or task completion, and orientation changes.
- [ ] Compare the experience with desktop interaction and explain specific differences.
- [ ] Add genuine screenshots and a short development log.

Unity's documentation linked by the slides: [Android build process](https://docs.unity3d.com/Manual/android-BuildProcess.html).

## Test record (fill after deployment)

| Question | Result |
| --- | --- |
| Unity version and source project | Not recorded |
| Phone / emulator model and Android version | Not recorded |
| Input mapping actually implemented | Not verified |
| Build success and installation | Not verified |
| Movement, responsiveness and comfort | Not tested |
| Bugs encountered and fixes | Not documented |
| Evidence screenshots / video | Not uploaded |

## Reflection topics

After real testing, discuss whether motion controls offer a better correspondence between hand motion and on-screen movement, whether they introduce fatigue or uncertainty, and whether the interface is readable while the device itself moves. Describe problems, steps taken to solve them, and what a beginner should consider before following the same process.

No build, deployment or gameplay result is claimed in this draft.
