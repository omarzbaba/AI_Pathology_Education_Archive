---
title: Worked example — Self-quizzing through SPEP interpretation
pillar: self-education
event_type: n/a
audience: resident
difficulty: intermediate
time_to_use: >10min
visual: multimodal
tags: spep, ife, self-quiz, paraprotein, worked-example, multimodal
verified_models: Claude Sonnet 4.5, GPT-4o
best_model: Claude Sonnet 4.6
last_updated: 2026-05-18
---

## What this example shows

A 22-minute self-quizzing session through SPEP and follow-up IFE interpretation. The user is a PGY-2 in their first week of clinical chemistry. **The goal is not to get the diagnosis** — it is to drill the interpretive reflex: see a pattern → generate a differential → narrow systematically → critique the reasoning.

The session uses three prompts in sequence — **calibrate** → **deepen** → **drill** — chained in a single conversation so the model maintains its mental model of the user across turns. Every model exchange is shown verbatim. Annotations in *italics* show what the user did well, what they corrected, and where they had to push back.

This is the most useful structure of any Pillar 1 example because it demonstrates the *chaining* pattern that distinguishes effective AI study from one-shot queries.

## Setup

- **User:** PGY-2 resident, week 1 of CP/clinical chemistry rotation
- **Source material:** A SPEP gel and densitometry trace from a published teaching case (de-identified, public-domain — provenance confirmed before upload)
- **Tools:** Claude Sonnet 4.6 with image attachment; single conversation thread
- **Time invested:** 22 minutes
- **Outcome:** correctly identified IgG-kappa monoclonal gammopathy of undetermined significance vs early myeloma; one model correction caught; one model hedge pushed back on

## Turn 1 — Calibrate

> **User:** I'm a PGY-2 in my first week of clinical chemistry. I've read the chapter on serum protein electrophoresis once. I can identify the five major regions on a normal trace but I have not yet practiced interpreting abnormal patterns.
>
> I'm going to show you a SPEP and I want you to **quiz me before you tell me anything**. Ask me one question at a time, starting from the broadest observation and narrowing. Wait for my answer each time. Do not give me the answer until I tell you I'm stuck.

*Annotation: the calibration is doing three things simultaneously — declaring level (PGY-2, week 1), declaring goal (drill, not lecture), and setting the interaction protocol (one question at a time, wait for answer). Without the explicit protocol declaration, the model defaults to dumping the full interpretation at once. The protocol is the entire point of the chained approach.*

> **Model:** Got it. Looking at the trace you've attached, here's my first question:
>
> Before we get into the diagnostic interpretation, can you describe what you observe in the **gamma region** compared to a normal trace? Just describe the shape, not the diagnosis.

## Turn 2 — User answer + deepen

> **User:** The gamma region has a tall, narrow spike that is much sharper than a normal polyclonal gamma hump. The base of the spike is narrow — it looks like a single column rather than a broad mound.

> **Model:** Good — that's the key observation. The narrow base is what separates this from a polyclonal increase. Next question:
>
> Given that morphology, what are the **two broad categories** of paraprotein you should be thinking about, and how do they differ in clinical implication?

*Annotation: the model correctly named the next layer without skipping ahead. It also reinforced the discriminating feature ("narrow base") — exactly the kind of repetition that builds the interpretive reflex.*

> **User:** The two broad categories are monoclonal gammopathy of undetermined significance (MGUS) and a malignant plasma cell disorder, most commonly multiple myeloma. MGUS has a lower paraprotein level (usually under 3 g/dL), no end-organ damage, and bone marrow plasma cells under 10%. Multiple myeloma has higher paraprotein, end-organ damage (CRAB), and ≥10% plasma cells on marrow.

> **Model:** Correct on the discriminators. One small refinement: you should also be thinking about **smoldering multiple myeloma** as the intermediate category between MGUS and overt myeloma — same higher paraprotein and marrow plasma cells as myeloma but without end-organ damage. Worth knowing because the management is different.
>
> Next question:
>
> What is the next test you would order to characterize this spike, and what specifically would it tell you?

## Turn 3 — Drill

> **User:** I would order an immunofixation electrophoresis (IFE). It would tell me the heavy chain class (IgG, IgA, IgM, IgD, IgE) and the light chain type (kappa or lambda) of the paraprotein.

> **Model:** Right. I'm attaching the IFE result for this same patient now. Tell me what you see — and again, describe before diagnosing.

*Annotation: the user uploaded the IFE; the model's next response described the band positions and asked the user to interpret. The full session continued for another 14 turns through bone marrow biopsy interpretation, free light chain ratio, and a discussion of when to refer to hematology. Truncated here for length — the pattern is the lesson.*

## Two correction moments

### Correction #1 — model overstated MGUS safety

In turn 6 (not shown), the model wrote: "**MGUS is benign**." The user pushed back:

> **User:** MGUS isn't benign — it carries a ~1%/year risk of progression to myeloma. "Benign" is the wrong frame.

> **Model:** You're right, my apologies — that was imprecise. MGUS is **clinically asymptomatic** but is not biologically benign — it carries roughly 1% per year progression risk to overt plasma cell neoplasm, with cumulative risk that becomes meaningful over decades. The phrase I should have used was "asymptomatic" or "premalignant," not benign.

*Annotation: this is the most important moment in the transcript. Self-education with AI requires the user to catch the model's confident errors. The model's correction was graceful; the user's catch was correct. Both matter.*

### Correction #2 — model tried to skip ahead

In turn 10 (not shown), after the user had committed to "IgG kappa monoclonal gammopathy", the model started a paragraph on **treatment** for symptomatic myeloma. The user redirected:

> **User:** I'm not at treatment yet — I want to stay on interpretation. What does the marrow biopsy report add that I haven't already integrated?

> **Model:** Fair pull-back — let me stay on interpretation. Looking at the marrow report you described...

*Annotation: the model's instinct to "complete" the case (move forward to clinical management) competed with the user's drill goal. The user enforced the boundary. This is normal — the model doesn't know the user's specific learning goal unless reminded.*

## What the user did well

1. **Set the interaction protocol up front.** "Ask me one question at a time, wait for my answer" prevents the model from defaulting to a complete answer dump.
2. **Described before diagnosing.** Even when the diagnosis was obvious, forcing morphologic description first mimics the reading rhythm of an experienced pathologist.
3. **Pushed back on model overstatement** ("benign") and on model scope creep (moving to treatment). Both pushes preserved the drill.
4. **Used a single conversation thread** so the model maintained context. Re-starting fresh between turns would have lost the calibration.

## What this example does NOT show

- This is a **study transcript**, not a clinical workflow. The trace was a published teaching case. **No real patient was involved.**
- The model's interpretations were correct in this case — but they could have been wrong, and the user was responsible for verification against the published answer key.
- This pattern (calibrate → deepen → drill) is not the right shape for every learning task. Use it for *interpretive* skill-building; for *recall* tasks, use the MCQ generation or Anki prompts instead.

## How to use this example

If you're a CP resident in your first month, use this transcript as a template:

1. **Find a published SPEP teaching case** (atlas, society teaching set, public-domain case repository).
2. **Open a fresh conversation** with your preferred model (Claude Sonnet 4.6 or comparable).
3. **Paste the calibration prompt** (Turn 1 above), substituting your level and the specific image.
4. **Drill through 5-10 turns**, enforcing the one-at-a-time protocol.
5. **End with a check question** like: "Based on this session, what's the one concept I'm still weakest on?"

If you're a faculty member, this transcript is a useful model for what to encourage residents toward. The transcript can also be used as a teaching artifact in a "how to study with AI" session.

## Related prompts

- [SPEP / IFE trace interpretation walkthrough](library.html#/library/pillar-1-self-education/prompts/multimodal-spep-ife)
- [Self-quiz one at a time](library.html#/library/pillar-1-self-education/prompts/self-quiz-one-at-a-time)
- [Concept explanation at level](library.html#/library/pillar-1-self-education/prompts/concept-explanation-at-level)
- [Guardrails](library.html#/docs/guardrails)
