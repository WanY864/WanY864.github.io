---
title: "HCI — Lab: Talking LLM Character in Unity"
date: 2026-11-04
lastmod: 2026-11-04
summary: "Building Douni, a two-character Unity chat prototype, and comparing Typing and Streaming through a four-condition HCI ablation study."
tags: ["HCI", "Lab", "Unity", "Conversational AI", "Typing Indicator", "Streaming", "Ablation Study"]
categories: ["Human-Computer Interaction"]
draft: false
workType: lab
workStatus: completed
workSubtitle: "Unity 6 · Douni AI Chat · DeepSeek · Typing × Streaming"
weight: 50
linkTitle: "HCI — Talking LLM Character"
showDate: false
showTableOfContents: true
showReadingTime: true
showWordCount: false
---

## Goal and choice of HCI exercises

The lab **Building a Talking LLM Character in Unity** is about more than obtaining a response from a language model. It asks how an interface communicates **latency, turn-taking, transparency, anthropomorphism, and readability** while a person talks to an AI character. The teaching example connects **Unity 6, LLMUnity, LLMAgent, a C# controller, and a scrollable chat panel**, then asks each group to explore two HCI exercises and explain its findings.

For my lab, I focused on the two exercises that are closely connected:

1. **Measure latency:** distinguish the delay before the first visible response from the time until the complete response is displayed.
2. **Typing indicator:** investigate how an explicit waiting cue changes the clarity of the interaction while the AI is preparing its reply.

I extended these exercises by making **Typing** and **Streaming** independent switches. This allowed me to study four UI configurations rather than comparing only two screens. The primary evidence is **22 screenshots** from the Douni chat interface; each shows the experimental switches at the bottom.

## What I built: Douni AI Chat Experiment

I built a conversational UI around two illustrated companions, **Red Scarf Douni** and **Blue Scarf Douni**. Both remain visible, while the selected character provides the response. The friendly visual identity makes the interface feel less like a raw text console, but it also raises an HCI question: could an appealing character make an uncertain or slow answer seem more acceptable?

The main interface contains a central conversation panel, distinct user and AI message bubbles, a text field and **Send** button, a scrollable chat history, and a **Jump to latest** action. The navigation also exposes **Memory Manager**, **Experiment Data**, **Experiment Settings**, and **Settings**. The bottom bar is especially important in this lab: it contains the **Typing**, **Streaming**, and **Record data** switches alongside the connection and frame-time labels.

![Douni chat interface showing the red and blue companions, conversation bubbles, and the bottom experiment switches.](screenshots/1.png "Figure 1. Douni interface; the bottom bar in screenshot 1 shows Typing ON and Streaming ON.")

### Implementation and the difference from the teaching example

The supplied teaching slides use **LLMUnity with a locally downloaded GGUF model**. My actual Douni project is a **Unity 6 interface connected to the DeepSeek cloud API through a local Node.js proxy**. I am documenting that substitution explicitly rather than presenting it as the same offline setup.

The project folder includes a Unity scene and C# scripts for the character, UI, network handling, conversation state and trial metrics. The documented Unity baseline is **6000.0.40f1**; the interface has a **mock proxy mode** for UI checks and a **live proxy mode** for actual DeepSeek requests. In the screenshots, the footer says **“DeepSeek verified this session”**, indicating the live connection state shown by the application. This is a UI observation, not proof of an independently measured server response time.

The chat design separates three events that are sometimes treated as one: **request submitted**, **first answer text becomes visible**, and **complete answer is visible**. In the documented implementation, the upstream response can be received incrementally even when the **Streaming** display toggle is OFF; the toggle controls whether those chunks are **shown immediately or buffered**. This helps isolate the HCI effect of **presentation**, although the real network and server still introduce variability.

The project documentation also describes bounded scrolling, separate character histories, and ears that move when answer text is being displayed rather than simply during a silent wait. Those details matter for feedback design: an animation should not accidentally become a second waiting indicator in an otherwise “Typing OFF” condition. The screenshots establish the visible interface, not all of these dynamic behaviors.

## Experimental design: a 2 × 2 ablation

Instead of changing the model or character for each test, I treated the two bottom switches as **independent interface factors**:

| Condition | Typing indicator | Streaming display | Screenshots | Intended user experience |
| --- | :---: | :---: | --- | --- |
| **A — Baseline** | OFF | OFF | **5–10** | No dedicated typing cue; the answer appears as a completed block. |
| **B — Typing only** | ON | OFF | **11–16** | A waiting cue can signal that a reply is being prepared, followed by a complete answer. |
| **C — Streaming only** | OFF | ON | **17–22** | Partial answer text can appear as it arrives, without a separate typing cue. |
| **D — Combined** | ON | ON | **1–4** | A waiting cue can bridge the delay before the first visible text, then the answer appears progressively. |

This is a **2 × 2 factorial ablation of visible UI feedback**, not a comparison of four different LLMs. I checked the bottom controls in each original screenshot rather than assigning conditions based on file order alone.

My research questions were:

- **RQ1 — Latency perception:** Can displaying part of the answer sooner make a conversational AI feel more responsive, even if the whole answer is not finished sooner?
- **RQ2 — Turn-taking clarity:** Can an “AI is typing…” cue make it clearer that the system received a message and is working on a response?
- **RQ3 — Interaction between the two cues:** Is the transition from an explicit waiting state to streaming text clearer than either mechanism alone?

The corresponding expectations are **hypotheses**. Screenshots by themselves cannot establish a measured improvement in perceived wait, satisfaction, or trust.

## Direct answers to the two selected HCI questions

**Question 1 — Does streaming make waiting feel shorter? What is the difference between first-token delay and complete-response delay?**

**Answer:** Streaming can make an AI *appear* more responsive because users can start reading once the first text is available, instead of waiting for the complete answer. With my implementation, **Streaming ON** displays incoming content progressively, while **Streaming OFF** buffers it before display. This affects **time to first visible text**, not necessarily the actual model computation or total network completion time. Screenshots **5–10** (OFF) and **17–22** (ON) confirm the intended modes. In informal hands-on use, the visible response progressed at roughly **30 characters per second**; longer answers therefore took noticeably longer to finish. This is an **approximate observation**, not a logged cross-condition average or a fixed model throughput. Streaming allows reading to begin during that generation/display process, but the screenshots show completed conversations rather than send-to-first-word recordings. I **cannot calculate an exact first-token latency or quantify any reduction in perceived waiting** from these images. That would require the request, first-visible-text and completion timestamps plus user feedback.

**Question 2 — Does showing an “AI is typing…” indicator change satisfaction or understanding of the wait?**

**Answer:** A typing indicator can explain the otherwise silent period after **Send**, helping users understand that the AI has received their message. My comparison isolates this cue using **Typing OFF** in screenshots **5–10** and **17–22**, and **Typing ON** in screenshots **11–16** and **1–4**. Conceptually, the indicator is useful before the first answer fragment appears, even when Streaming is enabled. **My qualitative observation was that turning Typing ON made the interaction feel faster and smoother**, because the UI acknowledged the request while the first answer text was still pending. This is an observation about **perceived responsiveness**, not evidence that the model generated characters faster. Since the images are static end states and include **no recorded participant ratings**, I cannot quantify a satisfaction improvement or make a controlled causal claim.

**What I changed and what I found:** I changed the **two presentation switches**, producing four combinations while retaining the same basic interface. Separate user testing also found that the interface felt gentle and inviting, that the red/blue characters appeared to differ in rational and emotional approaches to decisions, and that low text resolution made the interface harder to use. I verified **22 screenshots** by checking the bottom toggle states. The **observed result** is a complete four-condition UI comparison, an approximate displayed pace of **30 characters per second** during hands-on use, and a qualitative impression of **smoother, faster-feeling interaction with Typing ON**. The **design conclusion** is that typing feedback and streaming cover different stages of waiting and may complement each other. The **unanswered empirical question** is which option people actually prefer—this needs controlled timings and participant responses. Therefore, I do **not** label the combined condition as statistically best.

## Visual comparison of the four conditions

### A. Baseline — Typing OFF, Streaming OFF (screenshots 5–10)

![Baseline red-character conversation, with Typing OFF and Streaming OFF in the footer.](screenshots/5.png "Figure 2. Condition A, screenshot 5: Red Scarf Douni; both interface-feedback switches OFF.")

![Baseline blue-character conversation, with Typing OFF and Streaming OFF in the footer.](screenshots/10.png "Figure 3. Condition A, screenshot 10: Blue Scarf Douni; both switches OFF.")

Condition A removes both explicit waiting feedback and progressive text display. The completed exchanges in screenshots **5** and **10** show that replies can be presented within the same chat layout. However, the period between pressing **Send** and the response appearing would be relatively uninformative if the interface showed no other status. The still images do **not** show that waiting interval, so I treat confusion or impatience here as a risk to evaluate, not an observed user reaction.

### B. Typing only — Typing ON, Streaming OFF (screenshots 11–16)

![Red-character conversation with Typing ON and Streaming OFF in the bottom bar.](screenshots/11.png "Figure 4. Condition B, screenshot 11: Typing ON, Streaming OFF.")

![Blue-character conversation with Typing ON and Streaming OFF in the bottom bar.](screenshots/16.png "Figure 5. Condition B, screenshot 16: Typing ON, Streaming OFF.")

Condition B isolates the **explicit waiting indicator**. Conceptually, a typing cue can reassure a person that the request has been received, even before the system is ready to display its answer. The completed-response screenshots verify the **switch state**, but do not capture the cue itself during the wait. Consequently, I cannot infer how long the indicator stayed visible or how participants reacted to it.

### C. Streaming only — Typing OFF, Streaming ON (screenshots 17–22)

![Red-character conversation with Typing OFF and Streaming ON in the bottom bar.](screenshots/17.png "Figure 6. Condition C, screenshot 17: Typing OFF, Streaming ON.")

![Blue-character conversation with Typing OFF and Streaming ON in the bottom bar.](screenshots/22.png "Figure 7. Condition C, screenshot 22: Typing OFF, Streaming ON.")

Condition C isolates **progressive text presentation**. Once the first fragment is visible, the user gains direct evidence that the answer is arriving. However, **Streaming ON does not eliminate the wait before the first fragment**. If the model or network is slow to produce that first content, there can still be a silent interval in this condition. Screenshots **17** and **22** verify the selected display mode, not its timing.

### D. Combined — Typing ON, Streaming ON (screenshots 1–4)

![Red-character conversation with both Typing and Streaming ON.](screenshots/1.png "Figure 8. Condition D, screenshot 1: both feedback options ON.")

![Blue-character conversation with both Typing and Streaming ON.](screenshots/4.png "Figure 9. Condition D, screenshot 4: both feedback options ON.")

Condition D is designed to provide feedback through both parts of the interaction: **an explicit processing cue while waiting**, followed by **visible incremental content when the response begins**. This seems like a promising design because each cue communicates a different state. It is **not** legitimate to call it the “winner” without users' ratings or comparable measured trials.

## Findings from the screenshots

The clearest result is that **all four UI configurations were demonstrated**. The footer gives an auditable record of the two manipulated switches, and the two characters appear across different conditions. The same broad layout — companions, conversation bubbles, input, Send button and footer — is maintained. This makes the intended UI comparison easy to understand.

A second observation from hands-on use is that **response length is a major driver of complete-response duration**. The reply appeared to progress at approximately **30 characters per second**, so a longer answer naturally takes more time to finish. This is a rough operational estimate, not a stopwatch-based measurement; it should not be treated as an exact model speed or used to compare Typing conditions without matching output length.

A third observation is that **similar questions receive different wording**. Across the captures, Douni's replies are not identical even when the user asks a comparable question. Therefore, differences in reply length or phrasing should **not** be attributed to Typing or Streaming. Those switches change how a response is displayed, not necessarily what advice the model generates.

A fourth observation concerns **information during a delay**. Each mode covers a different portion of the timeline:

| Moment | Typing cue helps? | Streaming helps? |
| --- | --- | --- |
| Immediately after pressing Send, before any text is available | Potentially **yes**: explains the pending state | **Not yet**: no content exists to reveal |
| After the first response fragment arrives | Usually no longer necessary | Potentially **yes**: shows progress in the answer |
| Once the answer is complete | Should disappear | Should stop updating and leave a readable complete reply |

In my qualitative use of the prototype, **Typing ON felt faster and more fluid**, despite there being no evidence that the actual character-generation rate changed. The typing cue helps communicate activity during the otherwise silent period; the feedback changes the experience of waiting rather than necessarily its physical duration.

This is an HCI interpretation supported by an informal hands-on impression, **not a quantitative measurement of participants' behavior**. The distinction matters: users may experience an interface as more responsive without the model actually computing any faster.

The screenshots also reveal an evaluation limitation: the width and scaling of captures **1–4** differ from many of the other images. Line wrapping and visible chat history vary. For a stronger comparison, all four conditions should be recorded at the same Game View resolution with the same prompt and controlled conversation context.

## Exercise 1 — Measuring latency correctly

The course asks us to distinguish **time to first token** from the total completion time. For this UI, I would also distinguish when text arrives over the network from when the user **actually sees** it:

| Timestamp | Definition |
| --- | --- |
| **t_send** | Send is activated. |
| **t_first_delta** | The first nonempty content arrives at the client. |
| **t_first_display** | The first answer text becomes visible in the chat bubble. |
| **t_network_done** | The network response completes. |
| **t_display_done** | The last response character has appeared in the interface. |

Because the observed pace is only an approximate **30 characters per second**, output length would need to be recorded or controlled before comparing total response durations. The approximate rate is not a substitute for timestamped observations.

The useful measures are **first visible delay = t_first_display − t_send** and **full visible delay = t_display_done − t_send**. I would also record **network time = t_network_done − t_send**. In a buffered mode, the first network content may have arrived long before it is shown; streaming separates those events.

The small **“Live frame time”** number printed in the screenshots is a rendering/frame-time indicator measured in milliseconds. **It is not LLM time-to-first-token, total generation latency, or perceived waiting time.** Treating it as a response-latency result would be incorrect.

## Exercise 2 — Evaluating the typing indicator and turn-taking

For the typing-indicator exercise, the useful question is not just whether the cue exists, but **whether a person understands what the system is doing**. A future evaluation should compare the four conditions using the same short prompts and ask users to rate, for example, **“I knew the AI was processing my message”** and **“The waiting time felt acceptable”** on a 1–7 scale. I would also observe repeated attempts to send, uncertainty about whether the application has frozen, and preferences after trying all conditions.

The documented experimental plan proposes a within-participant comparison, counterbalanced order, comparable prompts, and clearing conversation memory between conditions. This is a sensible next step, but I am **not claiming it was carried out with participants** merely because the four switch combinations appear in screenshots. Such short custom ratings are also **not a System Usability Scale (SUS) score**.

## User testing feedback — appeal, character differentiation, and readability

In hands-on user testing, the feedback was **positive about the visual concept but critical of text legibility**:

| Area | What users reported | HCI interpretation |
| --- | --- | --- |
| Visual appeal | The interface feels **gentle and welcoming**, making users **want to try and continue using it**. | A friendly visual style can increase initial motivation and make the AI less intimidating. |
| Two characters | Users could sense a **rational-versus-emotional difference** between the **red-scarf and blue-scarf Douni** when they approached decisions, and considered the two styles suitable for **different kinds of questions**. | Character presentation and conversational style affect expectations; a choice of companions can support different preferences and tasks. |
| Readability and usability | The **interface resolution was too low**; text was **difficult to read**, which made interaction **harder**. | Readability is a core usability requirement. Attractive characters and useful answers cannot compensate for an interface whose text is hard to see. |

This is **reported qualitative user feedback**. I have not recorded a participant count, questionnaire scores, task-completion times, or a controlled evaluation of character personality. In particular, the feedback does **not** establish which scarf color is inherently “rational” or “emotional,” or whether the users consistently preferred one character. It does show that **users noticed a meaningful distinction** between them.

**Design response:** My first visual fix should be to **increase the effective UI resolution and text legibility**, adjust font sizes and contrast, and recheck the conversation at the actual display resolution. I should also verify line wrapping, bubble width, and scaling in the Unity Game View. Then I can retest reading and message entry with users. This issue deserves priority over adding more decorative features.

These comments are also **separate from the Typing/Streaming ablation**. They strengthen the overall usability evaluation, but cannot substitute for timing data or condition-by-condition satisfaction ratings.

## What was measured, and what was not

The screenshot set establishes **22 visible interface states**, with these exact groups: **A = 5–10, B = 11–16, C = 17–22, D = 1–4**. In **every screenshot**, the third switch reads **Record data: OFF**. There is no attached CSV of completed live timing trials, no synchronized recording of the waiting/streaming phase, and no **condition-by-condition participant satisfaction ratings** for the Typing/Streaming comparison. The evidence now includes an **informal observation of roughly 30 visible characters per second**, the **subjective impression that Typing ON felt quicker and smoother**, and **qualitative user-test feedback** about the gentle visual design, perceived rational-versus-emotional differences between the two Douni characters, and a low-resolution readability problem. None of these constitute controlled latency statistics or a scored user study.

For that reason I do **not** report invented averages, milliseconds, percentages, significance tests, participant counts, or a preferred condition. What I have completed here is a **four-condition exploratory UI ablation and evidence-based HCI interpretation**. A controlled latency and usability study remains follow-up work.

The cloud-based DeepSeek implementation also differs from the original course's local-model example: network fluctuations and remote server load can affect times. The documented proxy checks used mocked upstream responses, which is useful for software verification but cannot substitute for real timing observations or Unity Play Mode evaluation.

## Problems, design decisions, and improvements

The major design lesson for me was that **feedback is not the same as performance**. A typing cue can reduce uncertainty without shortening computation. Streaming can reveal content earlier without reducing the time needed to finish the whole answer. Combining them should be evaluated for clarity, not automatically assumed to be faster.

There were also important interface considerations. The chat needs a bounded, scrollable region so long messages do not overlap the input. A **Jump to latest** control is useful when someone has scrolled up to reread an earlier answer. Distinct bubble colors and named avatars support turn-taking. User testing suggests that the two companions are experienced as different in rational versus emotional decision-making; that difference may be useful for different tasks, but should be controlled when evaluating Typing and Streaming. Testers also reported that low interface resolution made the text hard to read, so improving legibility is an immediate usability priority.

For the next iteration, I would:

1. Enable **Record data ON** and export genuine per-request timings for all four conditions, without storing API keys or message content in the trial log.
2. Record a short **screen video** of each condition so that the typing cue, first character, incremental text and completion are visible over time.
3. Fix the model, prompt, output limit, network setting, character and resolution while changing **only** the two experimental switches; clear conversation history between conditions.
4. **Prioritize the user-reported readability problem:** improve effective resolution, font size and contrast, then test reading and input tasks at the actual screen size.
5. Conduct a small counterbalanced within-participant test, keeping qualitative feedback separate from measured timings.
6. Make waiting, response arrival, errors and cancellation distinguishable states, with the typing cue removed as soon as real response text is visible.

## Reflection

This lab changed my focus from **“Can the character reply?”** to **“Can the person tell what is happening while it replies?”** A completed answer is only one part of a conversational interaction. The moments before the first word, during progressive output and at completion all affect how users understand the system.

I successfully organized my prototype into a **2 × 2 comparison of Typing and Streaming**, supported by 22 screenshots with explicit switch states. User testing also gave me two valuable insights: the **gentle design encouraged use**, and the **red- and blue-scarf Douni characters felt distinct in rational-versus-emotional decision-making**, making them seem useful for different questions. At the same time, users found the **low-resolution text difficult to read**, which increased interaction difficulty. I therefore need to improve legibility before treating visual appeal as sufficient usability. The absence of recorded latency trials and condition-specific satisfaction ratings still limits claims about which Typing/Streaming condition performs best. My main takeaway is that an AI companion needs both **clear feedback about its state and readable content**; personality and visual warmth should support, not obstruct, interaction.

## Materials and screenshot index

- [Course lab slide deck — Building a Talking LLM Character in Unity](https://docs.google.com/presentation/d/1jrL7pdQ2JOt8BcIjLqaodLd5q0tsmxWv/edit)
- [Unity/DeepSeek Douni project and implementation notes](https://drive.google.com/drive/folders/1dxMTcIGbLs1m1BeI5S1qi6QgUsyiCVuO)
- [Experiment protocol](https://drive.google.com/file/d/1vn5G3o4xUCNIaYFpgKVtqjcdIW6-k41v/view)
- [Original screenshot folder on Google Drive](https://drive.google.com/drive/folders/1VPT5pNLsNKvsdX5dnIixwUt_LVFkXUAm)
- [LLMUnity repository (the original course approach)](https://github.com/undreamai/LLMUnity)

All **22 original screenshots** are included in this page bundle and can be opened individually. In the list below, the image number is the original filename, not a chronological response-time measurement.

**A — Typing OFF / Streaming OFF:** [5](screenshots/5.png) · [6](screenshots/6.png) · [7](screenshots/7.png) · [8](screenshots/8.png) · [9](screenshots/9.png) · [10](screenshots/10.png).

**B — Typing ON / Streaming OFF:** [11](screenshots/11.png) · [12](screenshots/12.png) · [13](screenshots/13.png) · [14](screenshots/14.png) · [15](screenshots/15.png) · [16](screenshots/16.png).

**C — Typing OFF / Streaming ON:** [17](screenshots/17.png) · [18](screenshots/18.png) · [19](screenshots/19.png) · [20](screenshots/20.png) · [21](screenshots/21.png) · [22](screenshots/22.png).

**D — Typing ON / Streaming ON:** [1](screenshots/1.png) · [2](screenshots/2.png) · [3](screenshots/3.png) · [4](screenshots/4.png).
