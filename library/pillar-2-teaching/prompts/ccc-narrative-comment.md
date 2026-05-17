---
title: CCC narrative comment drafting
pillar: teaching
event_type: n/a
audience: faculty
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: ccc, narrative
verified_models: TODO
last_updated: 2026-05-17
---

## What this prompt does

Convert milestone scores and bullet observations into a CCC narrative comment that connects evidence to the assigned milestone level.

## When to use it

When you're writing CCC narratives at the semi-annual review and need to convert your numeric scores into prose that justifies the rating with evidence.

## The prompt

```
Write a CCC narrative comment for [resident initial], PGY-[level], for [milestone sub-competency — e.g., 'PC1.3 Interpretation of Diagnostic Studies'].

My assigned level: [milestone level]
My evidence/observations: [paste bullet observations from this review period that support this level]
Comparison to prior: [stayed the same / progressed / regressed since last review]

Format the narrative:

1. **One sentence stating the level and the trajectory** (progressed, plateaued, etc.).
2. **2-3 sentences of behavioral evidence** for this level — specific behaviors I observed.
3. **One sentence on the next milestone behavior** the resident is approaching or working toward.
4. **One sentence with a forward-looking expectation** for the next 6 months.

Tone: factual, evidence-based, defensible. The narrative should make sense to an external reviewer (PGY-1 ACGME visit) reading the file cold.

Do NOT inflate beyond the evidence I provided. If the evidence supports level 3 but I've inadvertently described level 4 behaviors, flag the inconsistency.
```

## Expected output

A four-sentence narrative tightly mapped to the milestone, with explicit evidence and forward-looking framing.

## Common failure modes

- The narrative inflates the level beyond the evidence.
- 'Evidence' is generic ('resident demonstrates competence') rather than behavioral.
- The forward-looking expectation is unrealistic given the current level.

## Required human verification

- Read against your bullets — every claim in the narrative should be traceable to a bullet.
- Have a colleague on the CCC read for tone consistency with how they'd write a similar narrative.
- Verify the milestone level descriptors against your program's current milestone document — these get revised periodically.
