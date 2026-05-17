---
title: Reverse case drill — findings to diagnosis
pillar: self-education
event_type: n/a
audience: resident
difficulty: advanced
time_to_use: 2-10min
visual: text-only
tags: case-based, drilling
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Give the model a set of findings and ask it to walk you through the differential and final diagnosis — then critique your own approach against the model's. The drill is in your interpretation, not in receiving the answer.

## When to use it

When you've just signed out a case and want to test whether you'd reach the same conclusion working in reverse from the findings alone. Especially useful for cases where the diagnosis was non-obvious or the differential was wide.

## The prompt

```
I'm going to give you a set of findings from a case I just worked. Work the case in reverse: starting from the findings alone, walk through your differential, narrow it systematically, and reach a final diagnosis.

Ground rules:

1. **Do not skip steps.** Even if the answer seems obvious, show your reasoning.
2. **Be explicit about pretest probability.** Name the demographic and clinical context that's shifting your differential.
3. **For each step, name the discriminating finding** that moves you from broad → narrower → narrowest.
4. **End with the single piece of evidence you most wanted that you didn't have**, and what it would have ruled in or out.

After your walkthrough, I'll tell you what I actually concluded and we can compare reasoning paths.

Findings:
[paste the findings — labs, imaging summary, morphology description, clinical context. De-identified, no PHI.]

**Important — refinement:** Critical reminder: the findings I paste must be **de-identified** with NO patient identifiers — no name, MRN, accession number, exact date of service, exact age, institutional identifiers, or rare-finding combinations sufficient for re-identification. If you see anything that looks identifiable in what I paste, stop and tell me before proceeding.
```

## Expected output

A step-by-step differential walkthrough ending in a final diagnosis and a named 'missing piece of evidence'. The walkthrough should be longer than the findings — that ratio is the point.

## Common failure modes

- The model jumps to the answer without showing reasoning. Push back: 'walk through the differential explicitly.'
- The model uses information that wasn't in your findings, then claims it was. Watch for this — push back.
- The differential is too narrow because the model anchored on a likely answer. Push back: 'broaden the differential and explain what would shift you to each.'

## Required human verification

- **Never paste identifiable patient information.** Use de-identified findings, published teaching cases, or sufficiently genericized vignettes.
- The model's final diagnosis is fallible. Treat the exercise as a structured comparison of *reasoning paths*, not as a second opinion on the case.

## Best model and why

**Claude Opus 4.7** — Explicit reasoning chains under uncertainty are Opus's strongest use case. Sonnet skips steps; Opus shows the work, which is the point of the drill.
