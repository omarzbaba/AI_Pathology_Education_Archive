---
title: Worked example — Self-quizzing through SPEP interpretation
pillar: self-education
event_type: n/a
audience: resident
difficulty: intermediate
time_to_use: >10min
visual: multimodal
tags: spep, ife, self-quiz, paraprotein, multimodal
verified_models: Claude Sonnet 4.5, GPT-4o
last_updated: 2026-05-17
---

## What this example shows

A 22-minute self-quizzing session with Claude using a SPEP trace and follow-up IFE. The user is a PGY-2 in their first week of clinical chemistry. The goal is not to *get the diagnosis* — it is to **drill the interpretive reflex**: see a pattern, generate a differential, narrow it down systematically, and then critique the reasoning.

The session uses three prompts in sequence: **calibrate**, **deepen**, **drill**. Each one is shown verbatim with the model's response. Annotations in *italics* show what the user did well, what they edited, and what they had to push back on.

## Setup

The user opened a fresh conversation and attached a single image: a SPEP gel and densitometry trace from a published teaching case (de-identified, public-domain). No patient data, no institutional case.

## Turn 1 — Calibrate

> I'm a PGY-2 in my first week of clinical chemistry. I've read the chapter on serum protein electrophoresis once. I can identify the five major regions on a normal trace but I have not yet practiced interpreting abnormal patterns. I'm going to show you a SPEP and I want you to **quiz me before you tell me anything**. Ask me one question at a time, starting from the broadest observation and narrowing. Wait for my answer each time. Do not give me the answer until I tell you I'm stuck.

*Annotation: the calibration is doing three things at once — declaring level, declaring goal (drill, not lecture), and setting the interaction protocol (one question at a time, wait for me). Without the protocol declaration, the model defaults to dumping everything at once.*

**Model:**

> Got it. Looking at the trace you've attached, here's my first question:
>
> Before we get into the diagnostic interpretation, can you describe what you observe in the **gamma region** compared to a normal trace? Just describe the shape, not the diagnosis.

## Turn 2 — User answer + deepen

> The gamma region has a tall, narrow spike that is much sharper than a normal polyclonal gamma hump. The base of the spike is narrow — it looks like a single column rather than a broad mound.

**Model:**

> Good — that's the key observation. The narrow base is what separates this from a polyclonal increase. Next question:
>
> Given that morphology, what are the **two broad categories** of paraprotein you should be thinking about, and how do they differ in clinical implication?

*Annotation: the model correctly named the next layer without skipping ahead. It also reinforced the discriminating feature ("narrow base") which is exactly the kind of repetition that builds the interpretive reflex.*

> The two broad categories are monoclonal gammopathy of undetermined significance (MGUS) and a malignant plasma cell disorder, most commonly multiple myeloma. MGUS has a lower paraprotein level (usually under 3 g/dL), no end-organ damage, and bone marrow plasma cells under 10%. Multiple myeloma has higher paraprotein, end-organ damage (CRAB), and ≥10% plasma cells on marrow.

**Model:**

> Correct on the discriminators. One small refinement: you should also be thinking about **smoldering multiple myeloma** as the intermediate category between MGUS and overt myeloma — same higher paraprotein and marrow plasma cells as myeloma but without end-organ damage. Worth knowing because the management is different.
>
> Next question:
>
> What is the next test you would order to characterize this spike, and what specifically would it tell you?

## Turn 3 — Drill

> I would order an immunofixation electrophoresis (IFE). It would tell me the heavy chain class (IgG, IgA, IgM, IgD, IgE) and the light chain type (kappa or lambda) of the paraprotein.

**Model:**

> Right. I'm attaching the IFE result for this same patient now. Tell me what you see — and again, describe before diagnosing.

*[The user uploaded the IFE; the model's next response described the band positions and asked the user to interpret. Truncated here for length — the full session continued for another 14 turns through bone marrow biopsy interpretation, free light chain ratio, and a discussion of when to refer to hematology.]*

## What the user did well

- **Set the protocol up front.** "Ask me one question at a time, wait for my answer" prevented the model from doing what it wants to do by default (dump everything).
- **Described before diagnosing.** Forcing morphologic description first, even when the diagnosis was obvious to them, mimics the reading rhythm of an experienced pathologist.
- **Pushed back when the model jumped ahead** (Turn 5, not shown — the model started discussing treatment; the user redirected back to interpretation).

## What the user had to edit

- The model used the phrase "**MGUS is benign**" early in the conversation. The user pushed back: MGUS is *not* benign, it carries a ~1%/year risk of progression. The model corrected itself.
- The model offered to "generate a final diagnosis" before all the evidence was gathered. The user declined and continued the drill.

## What you should not take from this example

This is a **study transcript**, not a clinical workflow. The trace was a published teaching case. No real patient was involved. Do not paste real patient data into any AI tool — that is the most important guardrail in this entire library. See [Guardrails](library.html#/docs/guardrails) for the full list.
