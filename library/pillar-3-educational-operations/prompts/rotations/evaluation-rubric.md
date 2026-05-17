---
title: Rotation evaluation rubric
pillar: educational-operations
event_type: rotation
audience: program-director
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: evaluation, rubric
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Generate a rotation evaluation rubric with milestone-aligned dimensions and behavioral anchors for each level.

## When to use it

When the existing evaluation form is generic or when you're piloting milestone-anchored evaluations. Should be reviewed by the CCC before use.

## The prompt

```
Generate an end-of-rotation evaluation rubric for [rotation name], [PGY level] residents.

The rubric should:

1. Have **5-7 dimensions** mapped to milestone sub-competencies that this rotation is positioned to assess.
2. For each dimension, **5 levels** with behavioral anchors (e.g., level 3 = 'Independently formulates a workup plan for routine cases and seeks supervision appropriately for complex ones').
3. Include both **knowledge/technical dimensions** and **professional/interpersonal dimensions**.
4. Have a **narrative comment field** for each dimension with prompting questions to help raters write meaningful narratives.

Avoid:
- Anchors that describe attitudes ('shows enthusiasm') rather than behaviors.
- Anchors that are mostly about effort ('tries hard') rather than performance.
- A 'meets expectations' middle that nobody can disagree with.

End with:
- Estimated time for an attending to complete the rubric (target: 15 minutes).
- The minimum number of observations required to assign each dimension fairly.

**Important — refinement:** Behavioral anchors must describe observable behaviors, not personality traits. 'Shows enthusiasm' is not a behavior; 'arrives prepared to sign-out with a written preview of complex cases' is.
```

## Expected output

A rubric with 5-7 dimensions, 5 leveled behavioral anchors per dimension, narrative prompts, plus time and observation guidance.

## Common failure modes

- Anchors that all sound positive (no real differentiation between levels 3-5).
- Dimensions overlap and rate the same behavior twice.
- Behavioral anchors aren't actually behaviors.

## Required human verification

- Run the rubric by your CCC chair before use.
- Pilot with two raters scoring the same resident independently. If inter-rater reliability is low, the anchors need refinement.
- Verify milestone mapping against your program's current document.

## Best model and why

**Claude Opus 4.7** — Behavioral anchors that genuinely discriminate between levels are hard. Opus produces more differentiated anchors; Sonnet tends toward all-positive language.
