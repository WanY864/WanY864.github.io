---
title: "HCI — Homework 3"
summary: "Lectures 7–9: three AR ideas, a caption prototype, and a simple evaluation approach."
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

For this homework, I tried to think of AR as something that helps with small problems in daily life, not just something that looks impressive in a demo.

## Lecture 7 — Three ideas to enhance human abilities

### Idea 1: Spatial Memory Aid

I often put something down and then forget where it is. My first idea is an AR reminder system for small objects, such as keys, glasses or tools.

I imagine pointing to an object and saving its location. Later, when I want to find it, a small arrow could appear in my view. I would not want the glasses to record everything automatically: the user should choose what to remember.

The difficult part is tracking. If the system remembers the wrong place, the arrow might be more annoying than helpful. I would also want a clear way to remove a saved location.

![Early sketch of a spatial memory reminder.](spatial-memory.svg)

### Idea 2: Live Conversation Captions

My second idea is live subtitles for a face-to-face conversation. This could help in a noisy room, when someone speaks too quickly, or when a person has difficulty hearing.

Instead of looking down at a phone, the user sees a short line of text near the speaker. I think the subtitles should be easy to pause, because we do not need them in every part of a conversation.

The challenge is that captions can be wrong or arrive late. Privacy also matters: other people should know when captions are being used, and a private conversation should not be recorded by default.

![Early sketch of an AR conversation caption.](live-captions.svg)

### Idea 3: Assembly Guide

My third idea is AR instructions for assembling something unfamiliar, like a small piece of furniture.

A normal manual gives you pictures on a separate page. With AR, I imagine a simple outline showing which part to pick up and where to place it. The user could move through the steps with **Next** and **Back**.

I think it could reduce confusion for beginners, but alignment is very important. If the arrow points to the wrong part, the instructions could cause mistakes instead of preventing them.

![Early sketch of step-by-step AR assembly help.](assembly-guide.svg)

### Which idea should I prototype?

I chose **Live Conversation Captions**. It has a small number of important actions—start, read, pause and exit—which makes it easier to test as a first prototype.

The other two ideas are also useful, but they depend much more on accurate object or location tracking. For captions, I can first study the interface without pretending that I have already built the speech-recognition system.

## Lecture 8 — Live Captions prototype

I made the interface around one question: **can someone tell immediately whether the glasses are listening or paused?**

The design uses a dark, slightly transparent caption card, a visible state indicator, and short lines. I tried to keep the text away from the centre of the conversation so it would not cover people's faces.

The mockup below lets you move between states using sample dialogue. It simulates the interaction; it does not listen to a microphone.

{{< hci-prototype name="live-captions" title="Live Captions interactive AR interface concept" >}}

### Low-fidelity version for a first user walkthrough

I also kept a simple three-state storyboard: **Ready → Live → Paused**. This version can be printed or shown on a screen while another person follows the task.

![Three-state low-fidelity captions storyboard, showing Ready, Live and Paused.](live-captions-prototype.svg)

For a Wizard-of-Oz test, one person can show prepared subtitle lines while the participant chooses when to start, pause or exit. That way, I can focus on whether the controls make sense without needing working AR glasses.

The key details I want to check are the caption position, the difference between Live and Paused, and how easy it is to stop the interaction quickly.

## Lecture 9 — Evaluation

The next step is to let **at least one other person** try the prototype. I would give them a simple scenario:

> You are talking to a classmate in a noisy café. Start captions, follow two lines of conversation, then pause them when the topic becomes private.

I would let the person try first without explaining which control to press. Then I would watch where they hesitate and ask a few questions:

- Was it obvious when captions were on or off?
- Were the words easy to read without blocking the conversation?
- Did the Pause control feel clear enough?
- What would you change before using this in real life?

I would use their actual comments to decide what to improve. At this stage, the prototype shows the design idea, **not the results of a completed user study**. One participant would be a useful first check, but not enough to prove the design works well for everyone.
