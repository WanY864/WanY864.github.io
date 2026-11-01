---
title: "HCI — Lab: Talking LLM Character in Unity"
summary: "Unity 6, LLMUnity, a streaming chat interface, and a plan for two HCI interaction exercises."
tags: ["HCI", "Lab", "Unity", "LLMUnity", "LLM", "Usability"]
categories: ["Human-Computer Interaction"]
draft: false
workType: lab
workStatus: in-progress
workSubtitle: "Unity 6 · Local LLM · Chat UI · HCI exercises"
weight: 50
showDate: false
showTableOfContents: true
showReadingTime: true
showWordCount: true
---


## Goal and brief

The lab handout, **Building a Talking LLM Character in Unity**, describes a locally running language model and a chat interface made with **Unity 6**, **LLMUnity** and **TextMeshPro**.

The intended result is an AI character whose answer appears progressively in a conversation window. The HCI focus is not simply whether a model produces text, but how people perceive **latency, turn-taking, trust, transparency, anthropomorphism and readability**.

The slides also specify that **each group chooses two HCI exercises and presents its findings at the next session**.

[Lab materials: LLM_Unity folder](https://drive.google.com/drive/folders/1M9TuVJU10GAa2rJej6nNNlPJspALEBUE)

## Interface Design and Implementation

### 1. Prepare Unity and the local model

- Install and open **Unity 6 (6000.0.x)** and create a **3D (URP)** project.
- In Package Manager, add LLMUnity from the Git URL provided by the slides: https://github.com/undreamai/LLMUnity.git
- Accept the TextMeshPro essentials import.
- Create an empty object, **LLM_GameObject**, with the **LLM** component.
- Select and download a local model through LLMUnity. The slides compare a small Qwen model with a DeepSeek reasoning model; any actual model name and version should be recorded from the real installation.
- Verify the model loads in Play Mode before building the chat interface.

**Why this order?** If model loading does not work, UI debugging cannot establish whether a blank screen is caused by the interface or the model.

### 2. Create the AI character

Create an **AI Character** GameObject with the **LLMAgent** component. Assign the LLM reference and provide a short, neutral System Prompt.

A short response target makes it easier to observe the delay between submitting a message and seeing the first visible token. The lab also points out that some reasoning-style models may output a visible thinking block, raising a transparency question.

### 3. Assemble the conversation UI

The teaching slides specify this basic hierarchy:

~~~text
Canvas
├── InputField_UserMessage  (TextMeshPro input)
├── Button_Send
└── ChatScrollView
    ├── Viewport
    │   └── Content
    │       └── ChatLogText
    └── Scrollbar Vertical
~~~

A practical UI should preserve the following relationships:

| Element | Responsibility |
| --- | --- |
| Input field | Accept a message and allow the next turn only when appropriate |
| Send button | Trigger the same send action as the Enter key |
| Scroll view | Keep the conversation in a bounded, scrollable area |
| Speaker labels | Visually distinguish the user from the model |
| Streaming output | Reveal the reply progressively and keep the latest text visible |

### 4. Wire the interaction script

The slide deck supplies an example called **NPCController.cs**. In the Inspector it connects **LLMAgent**, **TMP_InputField**, **TextMeshProUGUI**, **Button**, and **ScrollRect**.

The expected control flow is:

1. Read and validate a nonempty user message.
2. Append a labelled user turn to the chat log.
3. Clear and temporarily disable input while the model answers.
4. Start generation; update the visible answer as tokens arrive.
5. Scroll to the newest content.
6. Restore input focus and button availability when the response finishes.

**Version check:** LLMUnity callback signatures can vary. The handout warns that an API mismatch may cause a Chat method argument error. Any code copied from the teaching slides must be checked against the installed package version rather than assumed to compile unchanged.

## HCI research questions

**Latency perception.** A response that streams immediately may feel faster than a response displayed in one block, even if the total generation time is similar. The first-token delay and complete-response delay should be measured separately.

**Turn-taking.** Temporarily disabling inputs can avoid overlapping requests, but if the interface has no clear state indicator, the user may think it has frozen. The application should explain what it is currently doing.

**Trust and transparency.** Models can confidently generate incorrect answers. The UI should not encourage users to treat fluency as evidence of correctness. Showing internal-looking reasoning text can also confuse the conversation.

**Anthropomorphism.** Changing a character's name or conversational style may change user expectations even if the model and data are unchanged.

**Readability.** Scroll behaviour, text contrast, font size, response spacing and input placement directly affect whether the conversation is usable.

## HCI Interaction Exercises

Two possible studies focus on response timing and the effect of a typing indicator on turn-taking.

### Exercise A — Measure latency

**Question:** How does time to first visible token differ from total response time, and how do participants perceive this wait?

**Suggested procedure:** Log Unity timestamps when Send is pressed, when the first text arrives, and when the reply finishes. Repeat with a few comparable prompts on the same machine.

For each trial, the relevant measures are send time, time of first visible token, completion time and perceived wait.

Compute first-token delay as **first-token time − send time** and completion delay as **completion time − send time**. Interpret measurements only after running the application.

### Exercise B — Typing indicator

**Question:** Does an explicit “AI is typing…” status change how clear or tolerable the wait feels?

**Suggested comparison:** Use the same interface in two conditions: without an indicator and with an indicator displayed from Send until the first token. Keep the prompt and local model configuration comparable. Ask users whether they know if the system is processing a reply.

**What to observe:** attempts to press Send again, comments about uncertainty, perceived delay, and whether the indicator disappears when the actual reply begins.

No differences in satisfaction or speed are asserted here. Those are **hypotheses to evaluate**, not results.

### Alternative Exercises

The slides additionally suggest a **persona A/B test**, showing versus hiding a reasoning-style model's thinking text, a **five-person think-aloud and SUS usability study**, or a **multimodal speech-input/output comparison**. The handout asks each group to choose two exercises.

## Technical Notes

The teaching materials discuss several technical issues to consider:

- A Unity editor stall during domain reload when memory is heavily used.
- Missing Android SDK build tools in an unrelated Unity configuration.
- UI fields left unassigned, leading to null references.
- A chat log that grows outside the intended Scroll View.
- TextMeshPro not having glyphs for some emoji.
- Game view not receiving keyboard events unless it has focus.
- Different LLMUnity package versions providing different callback signatures.
