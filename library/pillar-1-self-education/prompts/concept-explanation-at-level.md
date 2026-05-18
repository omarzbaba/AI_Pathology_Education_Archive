---
title: Concept explanation at level
pillar: self-education
event_type: n/a
audience: resident
difficulty: intermediate
time_to_use: <2min
visual: text-only
tags: concepts, scaffolding
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Get a pathology concept explained in three layers calibrated to your specific gap — not a textbook dump and not a "for dummies" version. The output meets you at your current level, gives you something more than you came in with, and ends with a check question so you don't move on while you're still confused.

## When to use it

The **first move** in a self-study session. Calibration here sets the model's mental model of you for every prompt that follows in the conversation. Especially useful the night before sign-out on a topic you know you'll need to discuss, or when reviewing a topic you've read multiple times but still can't quite operationalize.

**Not for:** initial encounter with a totally unfamiliar topic (use a textbook chapter first), board-question-style discrete fact retrieval (use the MCQ generator), or quick lookups (use search).

## The prompt

```
You are my pathology study partner for this session, not a textbook. Your job is to meet me at my current level, give me something I didn't already know, and check my understanding before moving on. Calibration matters more than coverage.

## My context

- **PGY level / role:** [e.g., PGY-2 resident]
- **Current rotation or situation:** [e.g., second month of hematopathology, preparing for tomorrow morning's bone marrow sign-out]
- **Adjacent material I already understand:** [e.g., normal lymphoid architecture, basic flow gating, the difference between paratrabecular vs nodular infiltrates]
- **Target concept:** [the specific thing you're trying to understand — be specific]
- **Why I need it:** [the concrete situation in which I'll need to use this — board question, sign-out, teaching a junior, writing an MCQ, etc.]

## What to produce

Explain the target concept in **exactly three layers**, written as connected prose (no bullets within layers):

1. **First-year medical student version (1 sentence).** The simplest true statement. If it requires medical vocabulary, define it inline.

2. **My-level version (1 paragraph, 4-6 sentences).** The mechanistic explanation I should know cold for sign-out and board purposes. Use vocabulary I'd hear from a senior resident on this service. Connect the mechanism to *why* it matters clinically — what changes about the case depending on whether this concept applies.

3. **The "thought hard about this" layer (1 paragraph, 3-5 sentences).** The nuanced detail that distinguishes someone who has internalized the concept from someone who has memorized facts. This layer should surface a *connection*, *implication*, or *counterintuitive consequence* I am unlikely to have noticed yet — not just a more advanced restatement of layer 2.

## Hard rules

- **Source any specific value.** If any layer references a cutoff, drug name, gene, dose, classification edition, or guideline year, mark it inline like `[NCCN v2.2024]`, `[WHO 5th ed.]`, `[BSH 2023]`. If you're uncertain about a specific value, mark it `[VERIFY]` rather than stating it as fact.
- **No repetition across layers.** Layer 3 must add new depth; do not restate layer 2 in more elaborate vocabulary.
- **No padding.** If a layer is shorter than the target length but says everything that needs to be said, leave it shorter.
- **No "in summary" or recap paragraph.** End with the check question.

## After your explanation

Ask me **one** check question that tests the most likely misunderstanding *for my level*. The question must require me to APPLY the concept (predict what would happen, choose between two options, explain a counterintuitive finding) — not restate it. Then **wait for my answer**.

If my answer is wrong, name the specific gap before re-explaining. Do not just give the right answer — that builds dependence, not understanding. If my answer is right, ask one harder follow-up to push the edge of my knowledge.

## What I will NOT accept

- Layers that all sound the same level (calibration failure)
- A bulleted list disguised as a paragraph
- An unsourced number I have to chase down
- Moving on without waiting for my answer to the check question
- "Hope this helps!" or any other filler closer
```

## Expected output

Three labeled layers in connected prose (~50 / ~120 / ~80 words respectively), every specific value sourced inline or flagged `[VERIFY]`, ending with one applied-question check that waits for your response. The "thought hard" layer should make you go *huh, I hadn't thought about it that way*. If it doesn't, the model failed at the highest-value part of the prompt.

## Common failure modes

- **The model defaults to the textbook framing** and gives you what you could read in Robbins. Mitigate by being more specific about what aspect confuses you (the "Adjacent material I already understand" field is the calibration lever).
- **Layers collapse into one level.** Push back: "Layer 1 is at PGY-1 level, not med student level. Re-do layer 1."
- **The nuanced detail in layer 3 is confidently wrong.** This is the most dangerous failure mode for self-study — the model is most likely to hallucinate at the level where you have least ability to catch it.
- **The check question is recall, not application.** Push back: "That question only tests whether I read your explanation. Ask one that makes me predict or choose."
- **Model moves on without waiting for your answer.** Push back: "Stop. I haven't answered yet."

## Required human verification

- **Cross-check layer 3 against an authoritative source** every time. The relevant chapter, a current guideline, or a curated review. The model is most likely to be confidently wrong at the level where you have least ability to catch it.
- **Verify any sourced value.** Just because the model tagged it `[NCCN v2.2024]` doesn't mean the value or the version is right.
- **If the check question's "correct" answer surprises you,** verify it against an authoritative source before incorporating it into your mental model.

## Best model and why

**Claude Sonnet 4.6** — handles layered, calibrated explanations reliably without over-elaborating. Use **Opus 4.7** if the topic is highly specialized (rare entities, subspecialty molecular nuances) and you want maximum depth at layer 3. **Avoid Haiku** — it tends to compress all three layers into the same level, which defeats the entire prompt.
