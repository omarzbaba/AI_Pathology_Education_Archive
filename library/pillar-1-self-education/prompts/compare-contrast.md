---
title: Compare and contrast
pillar: self-education
event_type: n/a
audience: resident
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: differential, entity-comparison
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Produces a focused side-by-side comparison of two entities you confuse, organized around the *discriminating* features that actually separate them — not a comprehensive list of every difference. The output is a table you can put on a flashcard, plus the single best discriminator and the classic trap.

## When to use it

When you've gotten a board-style question wrong because you picked the wrong one of a pair, when you can name both entities but routinely confuse them, or when you want to drill an entity-vs-entity discrimination before sign-out.

**Not for:** comparisons across a whole category (use [Differential by histologic pattern](library.html#/library/pillar-1-self-education/prompts/differential-by-histologic-pattern) instead) or first-time learning of either entity (read about each first).

## The prompt

```
You are helping me sharpen my discrimination between two entities I confuse. The output is a focused comparison, not a comprehensive list of every difference. Discriminating features only.

## What I'm comparing

- **Entity A:** [be specific — e.g., "follicular lymphoma, grade 1-2"]
- **Entity B:** [e.g., "reactive follicular hyperplasia"]
- **My level:** [PGY level + relevant rotation context]
- **What I get wrong:** [optional — the specific way I mistake them, if I know]

## What to produce

### 1. One-sentence orientation

How do these two entities relate to each other in the differential? (Same family but malignant vs reactive? Both subtypes of X? Lookalikes on H&E but resolved by IHC?)

### 2. Discriminating features table

| Feature | Entity A | Entity B |
|---|---|---|

Each row is a feature where they **differ in a clinically meaningful way**. Skip features they share. Aim for 4-8 rows — not more.

### 3. The single best discriminator

If you could ask only ONE question or order ONE test to resolve the differential, what is it? Justify in one sentence.

### 4. The classic trap

The single feature most likely to push a resident toward the WRONG answer, and how to avoid the trap. Be specific about the cognitive error — not "be careful," but "residents often see [feature] and conclude [wrong entity], because they forget that [feature] is also present in [right entity] when [condition]."

### 5. Source any version-dependent features

If a discriminating feature depends on a specific classification version (WHO 5th vs ICC 2022, NCCN year, etc.), state which version explicitly. Discrimination rules drift between editions.

## Hard rules

- Use the discriminating features your subspecialty's reference text actually uses, not generic ones I could guess
- If a "discriminator" depends on a test I can't realistically order in real practice, say so
- If a specific IHC stain is named, name the clone if the discrimination is clone-dependent
- Do not list shared features (waste of space)
- Do not invent discriminators you're not sure about — say so instead

## What I will NOT accept

- A table where most rows describe features both entities share
- A "best discriminator" that's not actually orderable
- A classic trap that's generic ("look carefully")
```

## Expected output

A 4-section comparison: orientation sentence, 4-8 row table, named best discriminator, named trap. Plus version disclosure for any classification-dependent feature.

## Common failure modes

- **Table includes shared features.** Push back: "Cut rows where they're the same."
- **Discriminators that are actually wrong** (mistaken for one another in subtypes). Verify against your subspecialty atlas.
- **Generic trap** ("be careful with morphology"). Push back: "Name the specific feature that misleads."

## Required human verification

- Confirm the discriminating features against your subspecialty's current reference. Models can confuse features between similar entities, especially for rarer diagnoses.
- If a specific stain pattern is named, confirm clone and current convention.
- Pressure-test the "best discriminator" with an attending — is it actually what they'd use?

## Best model and why

**Claude Sonnet 4.6** — structured comparison tables are Sonnet's strength. For comparisons that require sub-edition precision (WHO 5th vs ICC 2022 for hematopoietic neoplasms, for example), use **Opus 4.7** — Sonnet sometimes blurs version-specific discriminators.
