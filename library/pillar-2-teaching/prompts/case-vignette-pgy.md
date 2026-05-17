---
title: Case vignette at PGY level
pillar: teaching
event_type: n/a
audience: faculty
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: vignette, case-based
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Generate a case vignette calibrated to a specific PGY level — appropriate complexity, age-appropriate red herrings, the right amount of clinical context.

## When to use it

When designing case-based teaching and you need a vignette tuned to a specific level. PGY-1 vignettes should be simpler than PGY-3 vignettes in ways that go beyond word count.

## The prompt

```
Generate a case vignette for a teaching session targeted at [PGY level] residents on [topic / diagnosis being taught].

Calibration guidance by level:

- **PGY-1:** classic presentation, one main differential to resolve, all relevant data given, no significant red herrings.
- **PGY-2:** more typical presentation with a complicating factor (atypical demographic, comorbidity that obscures the picture, a 'positive' test result that's actually a red herring).
- **PGY-3:** atypical presentation, ambiguous lab/imaging data, must integrate multiple discordant findings.
- **PGY-4 / Fellow:** rare entity or atypical presentation of common entity, requires judgment calls under uncertainty.

The vignette should:

1. Be 4-7 sentences long.
2. Include demographic detail relevant to the differential (don't default to a 50-year-old white male).
3. Include the data the resident needs to reason from, no more.
4. End at the point where the resident must commit to an interpretation or next step.

After the vignette, provide:
- The intended diagnosis.
- The 2-3 most likely wrong answers a resident at this level would give, and why.
- One discussion question to use after the resident commits.

**Important — refinement:** Vary patient demographics across cases. Do not default to middle-aged white male unless I specify. The demographic should reflect the actual epidemiology of the condition, not the textbook archetype.
```

## Expected output

The vignette + intended diagnosis + wrong-answer analysis + discussion question. The wrong-answer analysis is the most useful part for teaching.

## Common failure modes

- The vignette is technically 'PGY-3' but the answer is obvious — calibration miss.
- Demographic defaults to standard textbook archetype.
- The 'wrong answers a resident would give' are improbable rather than the real common errors.

## Required human verification

- Pressure-test the vignette against a resident at the target level before using it in a session — is the difficulty actually right?
- Check that the demographic detail is consistent with the diagnosis's actual epidemiology, not a stereotype.
- No PHI, ever — this is fictional or genericized.

## Best model and why

**Claude Opus 4.7** — Calibrating difficulty to PGY level (red herrings, comorbidities, demographic variation) requires depth. Sonnet vignettes tend toward 'classic presentation' regardless of stated level.
