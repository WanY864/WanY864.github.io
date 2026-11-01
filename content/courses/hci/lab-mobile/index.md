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

## Goal

This lab explores how an existing Unity application can be adapted to mobile interaction and run on an Android phone or emulator. Touch and motion input require different interface decisions from desktop interaction.

[Lab reference: Mobile interaction slides](https://drive.google.com/drive/folders/1LXSiqex2GMRSVQd_L829p7vAvmkgcxs2)

## Mobile Interaction Design

A ball-control Unity application offers a useful example for comparing keyboard input with touch and motion input. The following mappings are design options.

| Interaction | Typical desktop mapping | Proposed mobile equivalent | Reason |
| --- | --- | --- | --- |
| Move the object | Arrow keys / WASD | Tilt device or drag a virtual joystick | No physical keyboard is available |
| Select an action | Mouse click | Large touch button | Direct finger target |
| Pause / restart | Keyboard shortcut | Persistent on-screen action | Discoverable without remembering keys |
| Feedback | UI in a desktop window | Responsive text and touch-friendly layout | Smaller screen and different viewing distance |

Tilting the phone might feel natural for steering, but it can make the screen harder to read. A touch alternative and adjustable sensitivity could make the interaction more comfortable.

### Interaction Details

- Decide on the device orientation (portrait or landscape) and keep the play area readable.
- Calibrate neutral tilt on startup or provide a Reset Calibration action.
- Cap input sensitivity to avoid accidental large movements.
- Place Pause and Restart controls away from the area where the finger typically steers.
- Keep score, win/lose feedback and error messages visible at phone size.
- Support a fallback touch control if the hardware sensor is not available in an emulator.
