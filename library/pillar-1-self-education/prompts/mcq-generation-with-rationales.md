---
title: MCQ generation with rationales
pillar: self-education
event_type: n/a
audience: resident
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: mcq, board-prep
verified_models: TODO
last_updated: 2026-05-17
---

## What this prompt does

Generate board-style multiple-choice questions with detailed rationales for all answer choices — both correct and incorrect. The rationales for the distractors are where the learning happens.

## When to use it

When you've just finished a study block and want active retrieval practice, or when you're building a personal question bank for board prep. Not a substitute for a real qbank, but useful for filling specific gaps.

## The prompt

```
Generate [N] USMLE/board-style multiple-choice questions on [topic] calibrated to [PGY level / board level — e.g., RISE, AP/CP boards, ABPath in-service].

For each question:

- The stem must include a clinical or laboratory vignette, not just a knowledge prompt.
- Five answer choices (A-E), with exactly one best answer.
- All distractors must be plausible to someone with partial knowledge — no obvious throwaways.
- After all questions, provide an answer key with a 2-3 sentence rationale for **each** answer choice, including why the wrong ones are wrong. The wrong-answer rationales are the most important part.

Topic depth: assume the resident has read the relevant chapter once but has not drilled the material.
```

## Expected output

N questions in the requested format with full vignettes, five plausible choices each, and complete rationales (right and wrong) for each choice. Rationales should explain not just the fact but the reasoning that connects vignette to answer.

## Common failure modes

- Distractors are obvious throwaways (one is clearly wrong without thought). Push back: 'Make the distractors more plausible.'
- Wrong-answer rationales are perfunctory ('this is incorrect because the right answer is A'). Push back for substantive explanations.
- Vignettes are generic 'a 50-year-old male presents with' templates that don't add educational value.

## Required human verification

- **Critical:** verify the correct answer against an authoritative source before using the question for study or sharing. AI-generated MCQs routinely have plausible-looking-but-wrong correct answers, especially for nuanced topics.
- Check that the question is not a near-duplicate of a real published board question (rare but possible).
