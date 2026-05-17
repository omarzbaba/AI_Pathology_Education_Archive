---
title: Matched case pair — reactive vs neoplastic
pillar: teaching
event_type: n/a
audience: faculty
difficulty: advanced
time_to_use: 2-10min
visual: text-only
tags: vignette, differential
verified_models: TODO
last_updated: 2026-05-17
---

## What this prompt does

Generate two cases that share a superficial presentation but resolve to different diagnoses, designed to highlight a specific discriminating feature. The pair structure forces residents to notice the discriminator.

## When to use it

When teaching a differential where two entities are commonly confused, especially when the discrimination is taught in a textbook but rarely drilled.

## The prompt

```
Generate a matched case pair for teaching the discrimination between [entity A] and [entity B] at [PGY level].

The pair should:

1. **Share superficial features** that put both entities in the differential (similar demographics, similar chief complaint, similar initial workup results).
2. **Diverge on the discriminating feature(s)** I want to teach — name those features explicitly.
3. **Be roughly equal in length and information density**, so the difficulty isn't in deciphering one but in noticing the discriminator.

For each case, provide:

- The vignette (4-6 sentences).
- The intended diagnosis.
- The discriminating feature(s) that should resolve it.

After both cases:

- A side-by-side comparison showing which features they share and which differ.
- The 'aha' question to use in teaching: when residents see both side by side, what question crystallizes the discrimination?
```

## Expected output

Two paired vignettes + intended diagnoses + named discriminators + side-by-side comparison + 'aha' question.

## Common failure modes

- The two cases differ on a feature other than the intended discriminator (confounded teaching).
- One case is obviously harder than the other and residents notice the structural difference rather than the clinical one.
- The 'aha question' is leading rather than illuminating.

## Required human verification

- Verify the discriminating feature is actually the discriminator in current practice (not an outdated criterion).
- Pressure-test with a resident who hasn't been taught the discrimination — do they notice it, or does the pair just feel like 'two cases'?
