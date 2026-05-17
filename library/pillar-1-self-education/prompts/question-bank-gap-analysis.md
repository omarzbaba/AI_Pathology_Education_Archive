---
title: Question bank gap analysis
pillar: self-education
event_type: n/a
audience: resident
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: board-prep, gap-analysis
verified_models: TODO
last_updated: 2026-05-17
---

## What this prompt does

Paste a list of question topics you've missed and have the model identify the underlying concept gaps and suggest a targeted review plan.

## When to use it

After completing a block of qbank questions where you've underperformed. The diagnostic value comes from being honest about which questions you missed and why.

## The prompt

```
I've completed [N] qbank questions on [topic / subspecialty / mixed]. Here are the questions I missed, with a brief note on each about why I missed it:

[paste a list, one question per line: 'topic — why I missed it']

Analyze these misses and identify:

1. **The underlying concept gaps** — group the misses into 2-5 concept clusters. A 'gap' is a missing piece of understanding, not 'I didn't know this fact'.
2. **The priority order to address them**, with rationale (which gap, if filled, would resolve the most other questions?).
3. **A specific review plan** for the top gap: which chapter or paper to read, which targeted qbank topic to drill next, an estimate of hours needed.
4. **A 'don't worry about it' list** — anything in my misses that's low-yield for the exam and not worth fixing.
```

## Expected output

2-5 concept clusters with rationale, a priority order, a specific review plan for the top cluster, and a deliberate low-yield list.

## Common failure modes

- The model treats every miss as equally important. Push back: 'rank the clusters by impact.'
- The 'review plan' is generic ('read more'). Push back: 'name the specific resource and a specific number of hours.'
- The low-yield list is empty. Real qbank performance always includes some questions not worth re-studying — push for an honest list.

## Required human verification

- Cross-check the concept clustering — are these really the right groupings, or is the model finding patterns that don't exist?
- Validate the 'don't worry about it' list against your program's expectations for the exam.
