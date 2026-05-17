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

Generate a side-by-side comparison of two entities that are easy to confuse, focused on the *discriminating* features rather than a comprehensive list of differences.

## When to use it

When you can name two entities but routinely confuse them, or when you've gotten a board-style question wrong because you picked the wrong one. The output is best when the entities are at the same diagnostic level (e.g., two specific entities, not 'lymphoma vs leukemia').

## The prompt

```
Compare and contrast [entity A] and [entity B] for a [PGY level] pathology resident.

Structure your response as:

1. **One-sentence orientation:** how do these two entities relate to each other in the differential? (Same family? Lookalikes? Sequential along a spectrum?)
2. **Discriminating features:** a table with rows for the features that actually distinguish them. Each row should be a feature where the two entities differ in a clinically meaningful way. Skip features they share.
3. **The single best discriminator:** if you could only ask one question or order one test, which one resolves the differential?
4. **The classic trap:** the feature most likely to make a resident pick the wrong answer, and how to avoid it.

Use the discriminating features your textbook actually uses, not generic ones.

**Important — refinement:** If a discriminating feature depends on a specific classification version (e.g., WHO 5th edition vs. ICC 2022), state which version you're using. Discrimination rules drift between editions.
```

## Expected output

A short orientation sentence, a 4-8 row table of discriminating features, a named best discriminator with rationale, and one named trap. The table rows should be the features you'd write on a flashcard, not exhaustive.

## Common failure modes

- The table includes features the two entities share (wasted space).
- The "best discriminator" is something not actually orderable in real practice.
- The "classic trap" is generic ("don't confuse them!") rather than a specific feature.

## Required human verification

- Confirm the discriminating features against your subspecialty's reference text. Models can confuse features between similar entities, especially for rarer diagnoses.
- If a specific stain pattern or molecular finding is named, verify it's the current convention (e.g., WHO classification version).

## Best model and why

**Claude Sonnet 4.6** — Sonnet renders structured comparison tables cleanly and stays specific about discriminators. For comparisons that require sub-edition precision (e.g., WHO 5th vs ICC), bump to Opus 4.7 — Sonnet sometimes blurs version-specific discriminators.
