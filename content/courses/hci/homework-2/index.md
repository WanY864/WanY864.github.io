---
title: "HCI — Homework 2"
date: 2026-10-08
summary: "Lecture 4–6: a current HCI researcher, The Ultimate Display, and the vertical ergonomic mouse."
tags: ["HCI", "Homework", "Human-AI Interaction", "XR", "Input Devices"]
categories: ["Human-Computer Interaction"]
draft: false
showTableOfContents: true
showReadingTime: true
showWordCount: true
---

Homework 2 continues the lecture-based part of the course. For the first three tasks, I looked at a current HCI researcher, revisited an early vision of immersive computing, and examined an alternative input device from an HCI perspective.

## Lecture 4 — Present One HCI Researcher

## Sidong Feng — Human, Software, and AI Interaction

For this task, I chose **Dr. Sidong Feng**, an Assistant Professor at the School of Data Science, The Chinese University of Hong Kong, Shenzhen.

I chose him because his work sits in an area that I find especially interesting: the boundary between **software engineering, HCI, and AI agents**. Instead of treating a GUI only as something used by a human, some of his recent work asks how an AI agent can understand and operate the same interface.

A large part of his recent research focuses on **GUI automation and intelligent software testing**. For example, his current publications include work on replaying software bugs from video reports with vision-language models, using multiple LLM agents to test multi-user features, and using retrieval-based LLMs for UI automation testing.

What I find interesting is that these problems are not only software-engineering problems. An agent has to make many decisions that are normally easy for a human user:

- Which object on the screen is interactive?
- What does an icon probably mean?
- Which action should happen next?
- Did the interface respond in the expected way?
- When should the agent stop and ask the human for help?

This makes the interface a meeting point between the **human user, the software, and the AI agent**.

In a traditional GUI, I usually think about the relationship as:

**Human → Interface → Software**

With GUI agents, it can become:

**Human → AI Agent → Interface → Software**

For me, this creates a new HCI problem. If an agent is going to act for the user, the interface also needs to support trust, feedback, correction, and human control. A system may be technically capable of clicking the correct button, but the user still needs to understand what it is doing and why.

This is the main reason I chose Sidong Feng. His work shows how HCI is expanding as AI becomes more active inside software systems.

**References**

- [Sidong Feng — CUHK-Shenzhen faculty profile](https://sds.cuhk.edu.cn/en/teacher/2381)
- [Sidong Feng — personal research page](https://sidongfeng.github.io/)

## Lecture 5 — The Ultimate Display

## Reading Ivan Sutherland's 1965 Vision Today

When I read Ivan Sutherland's **The Ultimate Display**, the part that surprised me most was how modern the main idea still feels.

The paper was written in 1965, but Sutherland was already thinking beyond a normal flat computer screen. His idea was closer to a computer-generated environment that surrounds the user and responds to the user's body.

Today, several parts of that vision already exist.

Modern VR and MR headsets can track head movement and update a stereoscopic 3D scene in real time. Hand tracking and motion controllers allow us to interact with virtual objects. Eye tracking is also becoming a normal part of high-end XR systems. Spatial audio makes virtual environments react not only visually but also acoustically.

So many parts of the **visual and interaction layer** of Sutherland's idea are already real:

- stereoscopic 3D displays,
- head tracking,
- hand and body tracking,
- eye tracking,
- spatial audio,
- motion controllers,
- basic haptic feedback.

However, the most ambitious part of his vision is still missing.

A virtual object can now look convincing, but it usually does not have the same physical consequences as a real object. I can see a virtual chair in a headset, walk around it, and even touch it with a tracked virtual hand. But I still cannot actually sit on it unless there is a real physical surface in the same place.

This is where I think the biggest gap remains: **physical feedback**.

Current haptics can create vibration or limited force feedback, but they cannot freely create solid objects, weight, resistance, texture, or temperature anywhere in space.

In the future, I think we may get closer to Sutherland's vision by combining several technologies rather than inventing one perfect display. Possible examples are:

- lighter haptic gloves,
- wearable force-feedback devices,
- robotic or shape-changing surfaces,
- room-scale tracking,
- redirected walking,
- AI-generated interactive environments.

In that case, the computer would not literally create matter. Instead, it could coordinate the virtual scene with physical devices so well that the user receives the right physical feedback at the right moment.

For me, the main value of *The Ultimate Display* is not that every prediction became exactly correct. It is that Sutherland treated the display as an **interactive environment**, not just a rectangle showing information. That idea is still one of the central goals of VR and MR today.

**Reading**

- [Ivan Sutherland — *The Ultimate Display*](http://worrydream.com/refs/Sutherland%20-%20The%20Ultimate%20Display.pdf)

## Lecture 6 — Input Devices and Interaction Paradigms

## The Vertical Ergonomic Mouse

![A commercial vertical ergonomic mouse that keeps the hand in a more upright position.](vertical-mouse.webp)

*Figure 9. Example of a vertical ergonomic mouse. The main change is not the cursor mapping, but the posture of the hand and forearm.*

For this task, I chose the **vertical ergonomic mouse**.

I would not describe it as a completely failed product, because vertical mice are still sold and used today. I think it is more interesting to see it as an alternative input device that has existed for years but has **never replaced the conventional flat mouse**.

That leads to a simple HCI question:

> If the ergonomic idea makes sense, why do most people still use a normal mouse?

## Classification

From an interaction point of view, the vertical mouse is still a normal **GUI pointing device**.

I would classify it as:

- **physical input device**,
- **indirect input**,
- **continuous 2D pointing input**,
- mainly used with a **graphical user interface**.

The cursor mapping is basically unchanged. Moving the mouse moves the pointer, while buttons and the scroll wheel provide discrete actions.

The important difference is the **posture of the hand and forearm**.

## The Ergonomic Idea

With a normal flat mouse, the palm faces downward and the forearm is more pronated. A vertical mouse rotates the hand toward a more neutral, handshake-like position.

Research supports at least part of this idea. In one study comparing a standard mouse and a vertical mouse, the vertical design reduced forearm pronation and lowered activity in some wrist extensor muscles. However, participants also needed more time to reach targets.

That trade-off is important to me because it shows that an input device can improve one part of the experience while making another part worse.

A second study comparing flat, angled, and vertical mice found that fully vertical designs reduced pronation, but the fully vertical mouse also produced the poorest pointing performance. Angled designs gave some of the postural benefit without the same performance cost.

## Why Did It Not Replace the Normal Mouse?

I think there are several reasons.

The first is **muscle memory**. Most users have spent many years using a flat mouse. Even if the cursor mapping is identical, changing the orientation of the hand changes the way small movements are produced.

The second is **precision and speed**. For gaming, CAD, image editing, or other tasks that require fast pointing, users may prefer a device they already know very well.

The third is **fit**. A vertical mouse usually depends more strongly on hand size and handedness. A shape that feels natural for one person may be uncomfortable for another.

There is also a more general HCI lesson here: calling something “ergonomic” does not automatically make it the better interface for every user. Comfort, performance, familiarity, learning time, and task type all matter together.

## Will It Succeed in the Future?

I think the vertical mouse will continue to exist, but mainly as an **alternative**, not as a universal replacement.

For office users who spend many hours using a mouse, reduced forearm pronation may be worth a short learning period. For other users, the conventional mouse may still provide the best balance of speed, familiarity, size, and control.

The future may therefore be less about choosing between completely flat and completely vertical designs. A more realistic direction is a range of **slanted and adjustable shapes** that try to balance ergonomics with familiar pointing performance.

This example shows a trade-off that appears often in HCI:

**better physical posture does not automatically mean better overall interaction.**

**References**

- Quemelo, P. R. V. & Vieira, E. R. (2013), *Biomechanics and performance when using a standard and a vertical computer mouse.*
- Odell, D. & Johnson, P. (2015), *Evaluation of flat, angled, and vertical computer mice and their effects on wrist posture, pointing performance, and preference.*
- Gaudez, C. & Cail, F. (2016), *Effects of mouse slant and desktop position on muscular and postural stresses, subject preference and performance.*
