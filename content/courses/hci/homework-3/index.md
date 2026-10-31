---
title: "HCI — Homework 3"
summary: "Lectures 7–9: three AR concepts, a low-fidelity prototype, and a user-evaluation plan."
tags: ["HCI", "Homework", "Augmented Reality", "Ideation", "Prototyping", "Evaluation"]
categories: ["Human-Computer Interaction"]
draft: false
workType: homework
workStatus: in-progress
workSubtitle: "Lectures 7–9 · AR ideas · prototype · evaluation"
weight: 30
showDate: false
showTableOfContents: true
showReadingTime: true
showWordCount: true
---

> **Work status:** Three concepts and their sketches are prepared; a low-fidelity prototype storyboard is also provided. **Lecture 9 is not completed:** at least one real person must interact with the prototype before observations and critical reflection can be reported. The design decisions below are proposals, not measured findings.

## Assignment requirements

The lecture brief describes a common theme: **enhancing human abilities in the age of augmented reality**.

- **Lecture 7 — Ideate (5 points):** create, sketch, and present **at least three ideas**.
- **Lecture 8 — Prototype (5 points):** build a prototype (for example, a paper prototype or Wizard-of-Oz prototype) good enough for first user exposure.
- **Lecture 9 — Evaluate (5 points):** ask **at least one person other than the designer** to interact with the prototype, observe that interaction, discuss their opinion, and reflect critically.

[Source: HW3.pdf](https://drive.google.com/file/d/1sSkRrC8AUAKFVhRXo7JJhEU2xWpl5Oyl/view)

## Lecture 7 — Three ideas for augmenting human abilities

These three concepts address different limitations: remembering places, understanding speech, and carrying out an unfamiliar physical procedure. Each keeps the real world visible and gives the user control over when information appears.

### Idea 1: Spatial Memory Aid

**Ability enhanced:** remembering where an everyday item or useful location was last seen.

**Scenario.** A person puts their keys on a shelf and later forgets where. An AR interface allows them to save a spatial reminder. When they search for the keys, a small directional cue leads them toward the saved location.

**Interaction.** The user selects an object, confirms its location, and chooses whether to save a reminder. Later, a search phrase such as “Find my keys” displays a limited, world-anchored hint rather than covering the whole field of view with labels.

**HCI rationale.** The system shifts some prospective and spatial memory work into the environment. Confirmation is important because an approximate location must not be presented as certain. Information should be available when requested and disappear once it is no longer useful.

**Potential problems.** Incorrect tracking could guide the user to the wrong place. Continuous recording of a room could expose private information. The default should therefore be user-controlled saving, visible uncertainty, and an easy way to delete reminders.

![Sketch of Spatial Memory Aid showing a saved location and directional hint.](spatial-memory.svg)

### Idea 2: Live Conversation Captions

**Ability enhanced:** understanding spoken conversation when speech is difficult to hear, in noisy rooms, or when using an unfamiliar language.

**Scenario.** Two people talk face to face. Instead of looking down at a phone, the user sees a short caption near the current speaker. They can pause captions or hide them whenever the conversation becomes easier to follow.

**Interaction.** Captions begin only when the user activates them. The interface displays brief speaker-labelled text, a clear pause control, language settings, and a private mode that avoids saving a transcript.

**HCI rationale.** A good augmentation should support attention to the speaker, not replace the conversation with a second screen. Position, contrast, timing, and line length matter: long captions or frequent updates may distract from gestures and facial expressions.

**Potential problems.** Speech-recognition errors, incorrect speaker identification, delayed captions, and the consent of other participants are significant risks. The interface must show that captions can be wrong.

![Sketch of Live Conversation Captions with speaker text and privacy controls.](live-captions.svg)

### Idea 3: Assembly Guide

**Ability enhanced:** performing an unfamiliar manual task by combining instructions with the physical object.

**Scenario.** A beginner assembles a small piece of furniture or a mechanical kit. The AR interface identifies the current part, displays one step at a time, and lets the user move forward only after checking the result.

**Interaction.** A highlighted outline indicates where a part should go. The system uses short text, a single arrow, and explicit Next / Back controls. A 2D instruction view remains available if tracking becomes unreliable.

**HCI rationale.** Instructions placed near the relevant object can reduce repeated attention shifts between a separate manual and the work area. Step-by-step presentation also limits cognitive load.

**Potential problems.** Poor alignment could cause mistakes; an overlay could hide safety-critical features. The system should avoid pretending it can verify a connection it has not actually checked.

![Sketch of Assembly Guide with one step and an AR alignment overlay.](assembly-guide.svg)

### Comparison and proposed selection

| Criterion | Spatial Memory Aid | Live Captions | Assembly Guide |
| --- | --- | --- | --- |
| Main ability | Recall / navigation | Communication | Procedural learning |
| Interaction frequency | Occasional | During conversation | During a task |
| Primary failure risk | Wrong location | Wrong transcript | Misaligned guidance |
| First paper-prototype feasibility | Moderate | **High** | Moderate |
| Privacy consideration | Personal location history | Other speakers' consent | Camera view of workspace |

I propose **Live Conversation Captions** for the first prototype. Its main interaction can be simulated with cards and a printed screen without needing to claim that speech recognition or headset tracking already works.

## Lecture 8 — Low-fidelity prototype

**Prototype format:** three printable frames and a Wizard-of-Oz procedure. This is a proposed interface prototype, **not a functioning speech-recognition application**.

![Three-panel low-fidelity caption interface storyboard: ready, live and paused states.](live-captions-prototype.svg)

The storyboard has three states:

1. **Ready.** The participant sees two people and a Start Captions action. Nothing is transcribed automatically.
2. **Live.** A facilitator reveals prewritten lines, one at a time, as the imagined speaker talks. A label identifies the speaker and the user may choose Pause.
3. **Paused / Private.** The caption area visibly changes to Paused. The user can Resume or Exit and should understand that nothing further is displayed.

**Materials:** print the storyboard, prepare a few short example phrases on paper, and place a transparent sheet over a photograph or sketch of a conversation. The facilitator moves the prepared phrases when the participant requests captions. No headset is required for this first exposure.

**Proposed task:** “Imagine you have difficulty hearing a friend in a busy room. Start captions, follow two spoken lines, pause them because a private topic begins, and exit the interface.”

**What this prototype can test:** whether people notice the Start action, recognise the current state, find Pause quickly, understand privacy mode, and consider the captions legible. It **cannot** validate real-world caption accuracy, latency, eye tracking, or headset comfort.

## Lecture 9 — Evaluation plan (real participant required)

This part **cannot be completed from documents alone**. The lecture specifically asks for at least one other person to use the prototype and discuss the experience.

### Procedure

1. Ask an adult volunteer for consent to do a short usability walkthrough. Do not record a real conversation without permission.
2. Explain the scenario but do not demonstrate where the controls are.
3. Present the Ready card. Give the participant the task described in Lecture 8.
4. Show the Live card and reveal two prepared example captions. Observe which information they look at first.
5. Ask the participant to pause, resume, and exit. Note hesitations, mistaken assumptions, and any need for hints.
6. Ask open questions: “What felt clear?”, “What was confusing?”, “Where should the captions appear?”, and “Would you trust these captions?”
7. Compare their comments with the original design expectations; propose changes supported by what was actually observed.

### Record actual observations here

| Observation | Record after the session |
| --- | --- |
| Participant identifier (anonymous) | **Not yet recorded** |
| Task completion without hints | **Not tested** |
| Controls the participant found confusing | **Not observed** |
| Comments about caption placement and legibility | **Not collected** |
| Comments about consent / privacy | **Not collected** |
| Proposed changes based on evidence | **Pending** |

### Critical reflection prompts

The critical reflection must refer to the participant's **actual** behaviour rather than predictions. Consider whether placing captions near a face supports conversation or distracts from eye contact; whether users notice that the system can misrecognise speech; and whether a visible privacy toggle changes their sense of control. Also acknowledge the limits of a single participant and a static paper prototype.

## Remaining submission evidence

- [x] Three distinct concepts described and compared.
- [x] Three concept sketches.
- [x] Low-fidelity storyboard prototype and an exposure procedure.
- [ ] Have **at least one person other than the designer** interact with the prototype.
- [ ] Record what the person actually does and says.
- [ ] Add a critical reflection based on that interaction, including proposed revisions.
- [ ] Add photographs of the printed prototype or an actual exposure session, if available.
