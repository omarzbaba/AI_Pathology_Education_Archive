---
title: Paper methods critique
pillar: self-education
event_type: n/a
audience: resident
difficulty: advanced
time_to_use: 2-10min
visual: text-only
tags: literature, critical-appraisal
verified_models: TODO
last_updated: 2026-05-17
---

## What this prompt does

Critique a paper's methods section against standard reporting guidelines for the study type (CONSORT for trials, STROBE for observational, PRISMA for reviews, etc.), surfacing missing elements and potential biases.

## When to use it

When you're presenting a paper at journal club, writing a critical review, or reviewing for a journal. Generates a checklist-style critique that's structured rather than impressionistic.

## The prompt

```
Critique the methods section of this paper for a journal club presentation. The paper is a [study type — e.g., retrospective cohort, RCT, diagnostic accuracy study, systematic review].

Use the appropriate reporting guideline as your framework:
- RCT → CONSORT
- Observational study → STROBE
- Diagnostic accuracy → STARD
- Systematic review/meta-analysis → PRISMA
- Prediction model → TRIPOD
- Other → [name the guideline you're using]

Provide:

1. A checklist of the key reporting items expected for this study type.
2. For each item, mark whether the paper addresses it adequately, partially, or not at all. Quote specifically from the methods if needed.
3. The 3 most consequential gaps — the ones a peer reviewer would flag.
4. The 1 design choice that most constrains the paper's interpretability, with a specific suggested alternative.

If I haven't given you the full methods section, ask for it.

Paper methods: [paste methods section or full paper]
```

## Expected output

A structured checklist with adequacy ratings, three named consequential gaps, and one design critique with an alternative. Length: ~400-700 words.

## Common failure modes

- The critique is generic and could apply to any paper.
- The model invents items not in the actual paper.
- The 'suggested alternative' design isn't actually feasible given the research question.

## Required human verification

- Cross-check the critique against the actual paper. The model will sometimes critique items the paper addresses (just not in the section the model expected).
- If you're presenting this critique at journal club, run it by a faculty member with methods expertise — there's no substitute for human review of methodological critique.
