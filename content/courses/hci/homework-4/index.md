---
title: "HCI — Homework 4"
summary: "Lectures 10–12: how phones changed, Weiser's idea of ubiquitous computing, and three MR app ideas."
tags: ["HCI", "Homework", "Ubiquitous Computing", "Mixed Reality", "Smartphones"]
categories: ["Human-Computer Interaction"]
draft: false
workType: homework
workStatus: completed
workSubtitle: "Lectures 10–12 · Smartphones · Ubiquitous Computing · MR"
weight: 40
showDate: false
showTableOfContents: true
showReadingTime: true
showWordCount: true
---


For this homework, I used one theme to connect the three lectures: **technology should adapt to what people need, instead of making people adapt to the device**.

I first looked at how the physical shape of phones changed, then compared Mark Weiser's idea of ubiquitous computing with the devices around us today. Finally, I used those thoughts to come up with three MR apps. I made an early sketch for each app and then turned the ideas into small clickable interface concepts.

## Lecture 10 — How and why smartphone shapes changed

I started by comparing three stages of phone design: **phones with keypads, touchscreen smartphones, and foldable phones**. What interested me was not just how they looked, but what each shape made easier or harder for the user.

Older phones had small displays and physical keys. This worked well for calls and simple text messages because the controls stayed in the same place. But when people began using their phones for maps, web pages, photos and videos, those fixed keys took up space that could have been used by the screen.

I think the touchscreen was a big change because the controls could change with the task. A keyboard appears when we type, the entire screen becomes a camera viewfinder when we take a photo, and gestures can replace some physical buttons. This made the phone much more flexible.

I then looked at foldable phones. To me, they show a new design problem: we want a large screen, but we do not want a very large object in our pockets. A foldable display is a possible solution, although the hinge, weight, price and software layout also make the interaction more complicated.

| Phone design | What I think it improves | What becomes difficult |
| --- | --- | --- |
| Physical keypad | Familiar buttons and simple actions | Not much room for changing interfaces |
| Touchscreen | One surface can support many tasks | Less tactile feedback; some actions are harder one-handed |
| Foldable display | More screen space without always carrying a tablet-sized device | Thickness, durability, cost and changing layouts |

### What do I think comes next?

My prediction is **more flexible ways of using a phone**, not one strange new shape that everyone must buy.

For example, I can imagine using a normal phone for messages, opening a larger screen when I need to read or work, and using lightweight glasses for short information such as directions. Each device would be useful in a different situation. I also think traditional phones will remain popular because they are simple and reliable.

I reached this idea by thinking about how I use a screen: checking a message takes a few seconds, while reading a long document can take much longer. These tasks do not really need the same screen size. For me, a good design should make the transition between tasks easy without creating more work.

## Lecture 11 — Mark Weiser's vision of ubiquitous computing

In *The Computer for the 21st Century*, Mark Weiser imagined a world where computing becomes part of normal surroundings. I understood his point as **making the computer less noticeable while keeping its help available**.

To connect the paper with what we see now, I looked at his three device scales:

| In Weiser's paper | How I connect it to today |
| --- | --- |
| **Tabs** — small, portable devices | Smart tags, watches and small sensors |
| **Pads** — portable display surfaces | Tablets and shared portable screens |
| **Boards** — large shared displays | Classroom smartboards and meeting-room screens |

When I made these comparisons, I felt that we already have many parts of his idea. We carry several connected devices, and computers are inside objects that do not look like traditional PCs.

However, I do not think that means the full vision is complete. I still notice how often technology demands attention. Notifications interrupt what we are doing, devices do not always share information smoothly, and something as simple as moving between apps can take several extra steps.

Another issue I thought about is privacy. If a room can recognise who is there and automatically show personal information, that could be useful. But I would also want to know **what it knows about me, who can see it, and how to turn it off**.

So my answer is **partly yes**. We are surrounded by computing, but it is not always calm or invisible. I think the next improvement is not simply adding more devices. It is making their behaviour easier to understand, more connected, and more respectful of people's attention.

*Reading:* [Mark Weiser — *The Computer for the 21st Century* (1991)](https://www.lri.fr/~mbl/Stanford/CS477/papers/Weiser-SciAm.pdf)

## Lecture 12 — Three MR apps for everyday life

For the future MR app store, I wanted to imagine apps I might actually use, not just things that look good in a demonstration.

I followed three small rules when designing them: **solve a common problem**, **show only the information that matters**, and **give the user a simple way to hide or change the overlay**.

I came up with **Context Translator**, **Everyday Wayfinding** and **Shared Spatial Notes**. I first drew what the user would see in the real world, then created three different interactive mockups to explain the key actions. These are interface concepts, not real MR applications running on a headset.

### App 1 — Context Translator

**The problem I started with:** reading a menu, sign or label in a language I do not understand. Using a translation app on a phone works, but it means switching attention between the phone and the thing I am trying to read.

My idea is to show a small translation next to the original words. I sketched a menu with a simple text overlay. I then made a mockup where the user can switch between **Show translations** and **View original**. I deliberately kept the original text visible because a translation might be wrong.

{{< hci-prototype name="context-translator" title="Context Translator interactive MR concept" >}}

**Why it could be popular:** people travel, study and move between different languages all the time. I think the value would be immediate: instead of opening another app, the answer could appear beside the object.

The main risk is trust. If the translation is incorrect, especially for something important, the user needs an easy way to check the original.

### App 2 — Everyday Wayfinding

**The problem I started with:** finding a room or destination in a large campus, hospital or station. A normal map can be useful, but it still takes effort to match the map to the corridor in front of me.

I drew a campus route with a few directional hints. For the interactive version, I made a small map and a **Next instruction** control that advances the simulated position. The approximate distances come from the illustrated paths, not GPS measurements. I also added a **step-free route** switch because a path is not equally convenient for everyone.

{{< hci-prototype name="everyday-wayfinding" title="Everyday Wayfinding interactive MR concept" >}}

**Why it could be popular:** navigation is an everyday need. I can imagine this helping students, visitors or anyone looking for the right entrance in an unfamiliar place.

I would keep the arrows small and avoid covering obstacles. I also think the app should always have a regular map as a backup if the position tracking is inaccurate.

### App 3 — Shared Spatial Notes

**The problem I started with:** when a group works on a physical object, a message such as “change this part” does not always explain which part someone means.

I imagined placing virtual sticky notes directly next to an object. I sketched a shared worktable with labels attached to different parts. Then I built a clickable concept that lets the user switch between **Team** and **My notes**, and type a short example note.

{{< hci-prototype name="shared-spatial-notes" title="Shared Spatial Notes interactive MR concept" >}}

**Why it could be popular:** I think it could help students and teams explain changes much more directly than a long text conversation. The note would stay where the idea is relevant.

The part I paid most attention to was **who can see a note**. A shared workspace can become uncomfortable if private notes appear to everyone by accident, so visibility needs to be obvious.

### Which app would I download first?

I would probably use **Context Translator** most often because it solves a small problem with almost no learning time. I can also see Wayfinding being useful for many people, especially in unfamiliar places. Shared Spatial Notes feels a little more specialised, but very helpful for teamwork.

After making these sketches and mockups, I think the strongest MR apps will not necessarily be the ones with the most 3D effects. They will be the ones that make a real task easier **while keeping the real world in focus**.

## What connects the three lectures for me

The way I see it, smartphone shapes, ubiquitous computing and future MR apps are all parts of the same design question: **how much technology does a person really need to notice?**

Phones changed shape to support more kinds of tasks. Weiser imagined computing fitting quietly into everyday spaces. My three MR concepts try to follow that idea by showing a small piece of information at the right moment, with controls that let the user decide when it should disappear.
