---
title: Photomicrograph description practice
pillar: self-education
event_type: n/a
audience: resident
difficulty: advanced
time_to_use: 2-10min
visual: multimodal
tags: multimodal, morphology
verified_models: TODO
last_updated: 2026-05-17
---

## What this prompt does

Upload a photomicrograph and have the model describe what it sees, then critique your own description against the model's. The drill is your description, not the model's diagnosis.

## When to use it

When you're building morphologic observation skills and want a structured practice partner. Use published teaching cases or public-domain images — never real patient material.

## The prompt

```
I'm uploading a photomicrograph of a [specimen type — e.g., 'H&E-stained kidney biopsy at 40x', 'peripheral blood smear at 100x oil immersion']. This is a published teaching case, not real patient material.

Before I share my own interpretation, please:

1. **Describe what you see** in the image, organized by what's visible at this magnification. Use morphologic descriptors, not diagnostic language ('clusters of cells with hyperchromatic nuclei and high N:C ratio' not 'malignant cells').
2. **Identify the cell type or tissue type** if you can.
3. **Generate a differential** of 3-5 entities based on the visible features.
4. **Name the single most discriminating feature** you'd want to see on additional levels, stains, or higher magnification.

Then ask me ONE question about my interpretation before you reveal what you think the diagnosis is.
```

## Expected output

Structured description → cell/tissue ID → 3-5 entity differential → one discriminating feature → one question to you. The model holds back the diagnosis until you've engaged.

## Common failure modes

- The model jumps to a diagnosis before describing the morphology. Push back: 'describe first, diagnose later.'
- The model uses diagnostic language disguised as description ('atypical cells').
- The model confidently identifies a finding that isn't actually visible in the image. Watch for this — multimodal AI is improving but still routinely confident-wrong.

## Required human verification

- **Never upload real patient images.** Use published teaching cases, public-domain images, or your legitimately-cleared teaching collection.
- The model's morphologic descriptions are fallible — verify against the published answer for the teaching case before incorporating into your mental model.
- See [Guardrails](library.html#/docs/guardrails) for the full multimodal rules.
