---
title: Guideline plain-language translation
pillar: self-education
event_type: n/a
audience: resident
difficulty: quick-win
time_to_use: 2-10min
visual: text-only
tags: guidelines, plain-language
verified_models: TODO
last_updated: 2026-05-17
---

## What this prompt does

Translate a published guideline into plain language at a target reading level, preserving the recommendations and grading.

## When to use it

When you need to brief a non-pathologist colleague (or yourself, after a long day) on a guideline you've read but not yet internalized. Especially useful before tumor board where you'll need to explain a recommendation.

## The prompt

```
Translate the following guideline recommendations into plain language for a [target audience — e.g., 'first-year medical student', 'practicing internist', 'patient at 10th-grade reading level'].

For each recommendation:

1. State the recommendation in one sentence in plain language.
2. Preserve the strength of recommendation (Strong, Conditional, etc.) and the quality of evidence (High, Moderate, Low, Very Low) — these matter and shouldn't be smoothed over.
3. Translate technical terms inline (e.g., 'monoclonal gammopathy of undetermined significance (MGUS) — a small abnormal antibody in the blood that doesn't yet require treatment').
4. Add a one-sentence 'why this matters' line.

Do NOT change the substantive content of the recommendation. If a guideline says 'consider X', do not translate it to 'do X' — preserve the conditional language.

Guideline recommendations: [paste the recommendations]
```

## Expected output

A list of plain-language recommendations, each with grade and evidence quality preserved, with inline term translations and a 'why this matters' line.

## Common failure modes

- The model strengthens or weakens recommendations during translation. Push back: 'preserve the strength of recommendation exactly.'
- Inline term translations are inaccurate (e.g., translating MGUS as 'cancer').
- 'Why this matters' adds editorial content the guideline didn't actually say.

## Required human verification

- Cross-check the translated recommendations against the original guideline, particularly the strength of recommendation and any conditional language.
- Confirm inline term translations are accurate at the target reading level.
