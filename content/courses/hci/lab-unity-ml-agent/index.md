---
title: "HCI — Lab_Unity_ML_agent"
date: 2026-10-12
summary: "Setting up the Python and Unity sides of ML-Agents and checking that the training tools are available."
tags: ["HCI", "Lab", "Unity", "ML-Agents", "Python"]
categories: ["Human-Computer Interaction"]
draft: false
showTableOfContents: true
showReadingTime: true
showWordCount: false
---

## Goal

The goal of this lab is to prepare a working **Unity ML-Agents** environment before moving on to the official learning-environment examples and my own extension.

I treated the setup as two connected parts:

1. the **Python side**, which provides the training tools such as `mlagents-learn`;
2. the **Unity side**, which provides the ML-Agents package used inside the Unity project.

I found it easier to test these parts separately instead of trying to configure everything at once.

## My Setup Process

### 1. Installing Python 3.10.11

I first installed **Python 3.10.11 (64-bit)** on Windows.

The installer completed successfully, which gave me a clean Python environment for the ML-Agents tools. One Windows-specific detail I noticed at the end of the installation was the **Disable path length limit** option. This is useful to keep in mind because Unity projects and Python packages can create fairly deep folder structures.

At this point, the Python installation itself was ready.

### 2. Checking the ML-Agents Command Line

After installing the required Python-side tools, I checked whether the ML-Agents command-line program could actually be found by the system.

I used:

```text
mlagents-learn --help
```

The command returned the complete help page instead of an error. I could see options such as:

- `--run-id`
- `--resume`
- `--inference`
- `--base-port`
- `--num-envs`

For me, this was an important checkpoint. It showed that the **Python trainer was installed and the `mlagents-learn` command was available** before I started debugging anything inside Unity.

This also made the setup easier to reason about: if a later problem appeared in Unity, I already knew that the Python command-line side was at least responding correctly.

### 3. Installing the ML-Agents Package in Unity

Next, I moved to the Unity side.

In the Unity Package Manager, I installed the ML-Agents package from the local release folder:

```text
D:/MLAgents/ml-agents-release_23/com.unity.ml-agents
```

Unity showed the package installation process in Package Manager. This confirmed that the editor was reading the ML-Agents package directly from my downloaded local release.

I chose to keep the ML-Agents files in a dedicated folder on drive `D:`, which makes it easier for me to see exactly which release and package path the project is using.

## What I Learned from the Setup

The most useful thing I learned from this stage is that **Unity ML-Agents is not a single installation**.

There are two sides that need to communicate:

```text
Unity Environment
        ↕
ML-Agents package
        ↕
Python trainer / mlagents-learn
```

Because of this, I think it is better to verify the setup step by step.

My order was:

```text
Install Python
→ verify Python-side ML-Agents tools
→ check mlagents-learn
→ install the Unity package
→ test a Unity learning environment
```

This is much easier to debug than installing everything first and only checking it when the final training command fails.

## Problems and Things to Pay Attention To

The main thing I had to pay attention to was **version and path consistency**.

ML-Agents includes both Python packages and a Unity package, so it is important to know which release is being used on each side. I also found that keeping the downloaded release in a clear location such as:

```text
D:/MLAgents/ml-agents-release_23/
```

made the Unity package installation easier to understand.

Another useful check is to run `mlagents-learn --help` early. If this command does not work, there is little reason to start debugging the Unity project yet.

## Current Status

At this stage I have:

- installed Python 3.10.11;
- verified that `mlagents-learn` is available from the command line;
- opened Unity Package Manager;
- started installing the ML-Agents package from the local release folder.

The next part of the lab is to run one of the official **Learning Environment Examples**, verify communication between Unity and Python, and then extend the idea to a new situation.

I will continue documenting the actual test and extension here rather than writing the final result before I have run it.
