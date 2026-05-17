---
title: End-of-rotation evaluation
pillar: educational-operations
event_type: rotation
audience: program-director
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: evaluation, end-of-rotation
verified_models: TODO
last_updated: 2026-05-17
---

## What this prompt does

Generate an end-of-rotation evaluation form aligned to milestones, with both numeric and narrative sections.

## When to use it

When you're updating an evaluation form or when residents and attendings both complain the current form doesn't capture what matters.

## The prompt

```
Generate an end-of-rotation evaluation form for [rotation name], [PGY level], using the evaluation rubric I've provided (or a new one if I haven't).

The form should include:

1. **Header**: resident name, rotation name, dates, supervising attending(s), number of weeks evaluated.
2. **Numeric ratings**: each dimension from the rubric, rated 1-5 with the anchor text visible.
3. **Narrative comment for each dimension**: prompted with a specific question ('Describe a specific instance where you observed this resident at this level').
4. **Overall narrative**: 1-2 paragraph free text covering the resident's trajectory, strengths, and growth opportunities.
5. **Specific commitment for next rotation**: 1-2 behavioral targets the resident should focus on.
6. **Quality of evaluation gates**: a question to the evaluator about whether they had sufficient observation to evaluate this resident (mitigates the 'I'll just give 4s' default).
7. **Resident sign-off**: a box for the resident to acknowledge they received and discussed the evaluation.

Make the form completable in 20-30 minutes by an attending who knows the resident well.
```

## Expected output

A complete evaluation form ready for use, with numeric and narrative sections and sufficient observation gating.

## Common failure modes

- Narratives become 'no comments' because the prompts are weak.
- Numeric ratings default to all-fours because the anchors don't distinguish levels.
- The form takes so long that attendings rush it.

## Required human verification

- Pilot with one attending on one resident; iterate the form based on what they say is hard.
- Verify milestone alignment.
- Check that the form complies with any institutional or ACGME documentation requirements.
