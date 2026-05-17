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

Get an explanation of a pathology concept calibrated to your current level — neither too elementary nor too advanced. The output is an *adapted* explanation, not a generic textbook paragraph.

## When to use it

When you encounter a concept you half-understand and want a targeted explanation that meets you where you are. Best used as the *first* step in a longer self-quizzing session; the calibration here sets the model's mental model of you for everything that follows.

## The prompt

```
I'm a [PGY level] pathology resident on my [N]th rotation in [subspecialty]. I have a [working / weak / strong] understanding of [adjacent concept]. I'm trying to understand [target concept] well enough to [specific goal — e.g., interpret a case in tomorrow's sign-out, write an MCQ for our didactics, answer a co-resident's question].

Explain [target concept] in three layers:

1. The one-sentence version a first-year medical student would understand.
2. The mechanistic explanation a pathology resident at my level should know cold.
3. The nuanced detail that distinguishes someone who has thought hard about this from someone who has just memorized it.

After your explanation, ask me ONE follow-up question to check my understanding before moving on. Do not move on until I answer.

**Important — refinement:** If any claim in any layer references a specific cutoff, drug name, gene, dose, or guideline year, source it explicitly (e.g., '2024 NCCN, version 2'). If you can't source a specific number, mark it [VERIFY] rather than stating it as fact.
```

## Expected output

Three-layer explanation in plain prose (not bullets) totaling 200-400 words. The third layer should surface a nuance you didn't previously know. The follow-up question at the end should target the most likely misunderstanding for your level.

## Common failure modes

- The model defaults to the textbook framing and gives you back what you could read in Robbins. Mitigate by being specific about *which* aspect confuses you.
- The model skips the level calibration and explains at one undifferentiated level. Mitigate by re-stating the level after the first response.
- The "nuanced detail" turns out to be a half-remembered fact that's actually wrong. This is the failure mode that matters most for self-education — see verification below.

## Required human verification

- Cross-check the nuanced detail (layer 3) against an authoritative source: the relevant chapter in Robbins, a recent guideline, or a curated review article. The model is most likely to be confidently wrong at the level where you have least ability to catch it.
- If a specific numerical threshold or cutoff is given, verify against the current reference range or guideline.

## Best model and why

**Claude Sonnet 4.6** — Sonnet 4.6 handles calibrated, layered explanations reliably without over-elaborating. Use Opus 4.7 if the topic is highly specialized and you want maximum depth at layer 3. Avoid Haiku — it tends to compress all three layers into the same level.
