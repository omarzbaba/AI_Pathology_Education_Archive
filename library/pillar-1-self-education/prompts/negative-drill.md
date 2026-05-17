---
title: Negative drill — what would change the diagnosis
pillar: self-education
event_type: n/a
audience: resident
difficulty: advanced
time_to_use: 2-10min
visual: text-only
tags: case-based, drilling
verified_models: TODO
last_updated: 2026-05-17
---

## What this prompt does

Take a settled diagnosis and ask the model to enumerate the findings or test results that would force you to reconsider, ranked by likelihood. Trains the habit of disconfirmation.

## When to use it

When you have a working diagnosis you're confident in and want to stress-test that confidence. Especially useful for diagnoses you've seen rarely or for cases where the consequences of being wrong are high.

## The prompt

```
I have a working diagnosis of [diagnosis] in a patient with [brief clinical context — no PHI]. I want to stress-test this diagnosis.

Generate a ranked list of findings or test results that would force me to reconsider, organized as:

1. **Findings that would force a complete reconsideration** (rule out this diagnosis).
2. **Findings that would expand the differential** (suggest a different category of disease).
3. **Findings that are inconsistent but don't necessarily change the diagnosis** (worth noting, may indicate complication or atypical presentation).

For each finding, give a one-sentence rationale: why does this finding contradict the diagnosis?

Then identify the **single most likely** alternative diagnosis if I'm wrong, and the one test I should order to discriminate between them.
```

## Expected output

A three-tier list of disconfirming findings with rationales, plus a named alternative diagnosis and a discriminating test.

## Common failure modes

- The list focuses on the rare and exotic alternatives rather than the common ones. Push back: 'what's the most COMMON way I could be wrong?'
- The 'most likely alternative' is something already excluded by basic workup.
- The discriminating test is something with low specificity that won't actually settle the question.

## Required human verification

- This prompt is most useful as a thinking exercise; the model's specific suggestions are starting points, not definitive guidance.
- If a specific test is recommended (e.g., 'order a flow cytometry'), verify the test is the right one for the discrimination you actually need.
