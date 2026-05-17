---
title: Bloom's taxonomy MCQ generation
pillar: teaching
event_type: n/a
audience: faculty
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: mcq, assessment, blooms
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Generate MCQs at a specified Bloom's level (recall vs application vs analysis) with rationales calibrated to the cognitive task. The Bloom's level matters because most resident MCQs default to recall when application is what residents actually need.

## When to use it

When you're building assessment items and want to test reasoning, not just memorization.

## The prompt

```
Generate [N] multiple-choice questions on [topic] for [PGY level] residents. I want the questions distributed across Bloom's taxonomy levels:

- [X]% at **Application** (use knowledge in a new situation — typical clinical vignette)
- [Y]% at **Analysis** (distinguish, compare, organize — requires breaking down a complex case)
- [Z]% at **Evaluation** (justify a decision based on criteria — requires choosing among multiple acceptable approaches)

Avoid Remember/Understand level questions — they don't test what residents actually need.

For each question:

1. Provide the question and 5 answer choices.
2. Label the Bloom's level.
3. Explain *why* this question is at that level (what cognitive task is required to answer it).
4. Provide rationales for all five choices.

The rationales should explain the *reasoning*, not just state which is right.

**Important — refinement:** After each MCQ, justify the Bloom's level by naming the specific cognitive task required to reach the answer. If a question can be answered by retrieving a memorized fact alone — regardless of how clinical-looking the vignette is — it's Remember/Recall, not Application.
```

## Expected output

N questions with Bloom's labels, level justifications, and full rationales. The 'why this level' explanation should make explicit what cognitive task the question tests.

## Common failure modes

- The model mis-labels Bloom's level (calls a recall question 'application' because it includes a clinical vignette).
- All questions end up at the same actual level despite the requested distribution.
- 'Application' questions test the same fact a 'recall' question would, just dressed up.

## Required human verification

- Verify the correct answer against an authoritative source.
- Pressure-test the Bloom's level: would a resident who has only memorized facts be able to answer this question? If yes, it's not actually application or higher.
- Have a colleague who teaches this topic review the questions before using them in formal assessment.

## Best model and why

**Claude Opus 4.7** — Bloom's level calibration is genuinely difficult and Sonnet often mis-labels questions. Opus is more disciplined about identifying when a 'clinical vignette' actually only tests recall.
