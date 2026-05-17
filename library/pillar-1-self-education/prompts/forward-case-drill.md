---
title: Forward case drill — diagnosis to expected findings
pillar: self-education
event_type: n/a
audience: resident
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: case-based, drilling
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Name a diagnosis and have the model generate the constellation of findings you would expect to see, then quiz yourself on which findings are pathognomonic vs supportive vs incidental.

## When to use it

When you're studying a diagnosis you've read about but haven't seen many times. Builds the pattern recognition that comes from case exposure.

## The prompt

```
I'm studying [diagnosis] at a [PGY level] level. Generate the constellation of findings I should expect to see, organized as:

1. **Clinical presentation:** demographics, symptoms, onset, common comorbidities.
2. **Laboratory findings:** what's elevated, what's low, what's normal but tested anyway. Include reference ranges.
3. **Imaging findings:** what's seen on the relevant modality.
4. **Morphologic / histopathologic findings:** organized by what's seen at low power → high power → IHC/molecular.
5. **Findings that rule the diagnosis OUT:** the negative findings that should make you reconsider.

For each finding, label it [Pathognomonic / Highly Supportive / Supportive / Common but non-specific].

Then quiz me: ask me which findings I would prioritize on a sign-out and why.

**Important — refinement:** Be strict about the 'pathognomonic' label. A finding is only pathognomonic if it is unique to this diagnosis. If a finding appears in >1 diagnosis, it's at most 'highly supportive'. Over-labeling pathognomonic findings is the most common error in this kind of teaching summary.
```

## Expected output

A structured constellation with all five sections, every finding labeled by diagnostic weight, and a quiz question at the end about prioritization.

## Common failure modes

- The model labels too many findings as 'pathognomonic' — a finding is only pathognomonic if it's unique to the diagnosis, which is rare.
- The model includes findings that are actually for a similar but different diagnosis.
- Reference ranges given without source.

## Required human verification

- Verify which findings are truly pathognomonic vs merely supportive. The model overuses 'pathognomonic'.
- Cross-reference the morphologic findings against your subspecialty's atlas or reference text — this is where confident-wrong answers are most likely.

## Best model and why

**Claude Opus 4.7** — Distinguishing pathognomonic from supportive findings requires medical-knowledge depth and discipline about labels. Opus is more careful with these distinctions than Sonnet.
