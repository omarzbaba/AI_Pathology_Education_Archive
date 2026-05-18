---
title: Differential by histologic pattern
pillar: self-education
event_type: n/a
audience: resident
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: differential, morphology, pattern-recognition
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

You describe a histologic pattern (small round blue cells in a child, spindle cell tumor of the dermis, granulomatous inflammation in lung), and the model generates a complete pattern-based differential, ranked by likelihood given any context you provide, with discriminating features for each entity. This builds the pattern-to-DDx reflex that distinguishes experienced pathologists.

## When to use it

When you've seen a pattern you can describe but can't yet generate a complete differential for. Especially useful early in subspecialty rotations or while studying for boards — the pattern-DDx mapping is one of the most heavily tested cognitive skills.

**Not for:** lookups of textbook tables (more efficient to just look at the table), single-entity learning (use the concept explanation prompt), or initial encounter with morphology you can't yet describe (use the photomicrograph practice prompt first).

## The prompt

```
You are my pattern-to-differential drill partner. I'll describe a histologic pattern. You generate a complete, ranked differential — not just an enumeration, but with the specific discriminating features and the cognitive shortcuts I should remember.

## What I'm describing

- **The pattern (in morphologic terms):** [e.g., "monomorphic small round blue cells in nests with delicate fibrovascular stroma, in a 14-year-old's chest wall mass"]
- **Clinical context (if known):** [demographics, location, presentation, any prior imaging — de-identified or fictional]
- **My current best guess (if any):** [optional — including this calibrates the differential and helps you tell me what I might be missing]

## What to produce

### Section 1: The pattern-based differential

List **all entities I should consider** based on the pattern, organized as:

| Rank | Entity | Discriminating feature(s) | Confirmatory test |
|---|---|---|---|

Rank by likelihood given the context provided. Be comprehensive — include the unusual entities I might miss, not just the top 3.

### Section 2: The "must not miss" diagnoses

Even if low probability, name the entities that I MUST NOT MISS because the consequences of missing them are high (aggressive malignancy, treatable infection, etc.). Mark these explicitly.

### Section 3: Why the top of the differential is at the top

For the 2-3 highest-likelihood entities, explain in 1-2 sentences each *why* they're at the top given the context. What about the pattern + context shifts the priors?

### Section 4: The single most discriminating workup step

If I could do only ONE thing next — one stain, one molecular test, one additional level, one clinical question — what would it be? Justify.

### Section 5: Cognitive shortcuts

Name 2-3 mental shortcuts that distinguish experienced pathologists' approach to this pattern from textbook reasoning. These should be the kind of intuition that comes from seeing many cases (e.g., "in a peripheral lymph node with [pattern], always check for [feature] before signing out — it's the single most common reason this entity gets called wrong").

## Hard rules

- **Be comprehensive in the differential.** Missing entities is the failure mode I'm trying to address with this prompt.
- **Discriminating features must be specific.** "Architecture" is not a feature; "tumor cells in well-formed glands lined by columnar epithelium" is.
- **Source any specific cutoff or criterion** — WHO edition, classification scheme, named criterion.
- **Do NOT rank entities by pure prevalence.** Pretest probability matters: adjust for the demographic and location context I gave you.

## What I will NOT accept

- A differential of 3 entities when 8 are reasonable
- Vague discriminating features
- A "must not miss" section that's just a restatement of the top of the differential
- Cognitive shortcuts that are obvious or platitudinous
```

## Expected output

A complete pattern-based DDx table, a must-not-miss list, ranked rationale for the top entities, a single discriminating next step, and 2-3 expert-level cognitive shortcuts.

## Common failure modes

- **Differential too narrow.** Push back: "What am I missing? Generate the full list including unusual entities."
- **Discriminating features are vague.** Push back: "What specifically about [feature] discriminates [entity A] from [entity B]?"
- **Pretest probability ignored.** Push back if a high-base-rate entity is buried below an exotic one without justification.
- **Shortcuts are platitudes.** Push back: "Give me shortcuts that someone who has signed out hundreds of these would know."

## Required human verification

- **Verify the differential against a subspecialty reference** (the relevant WHO blue book, your subspecialty atlas, or a recent review). Models can miss entities, especially less common ones.
- **Pressure-test the cognitive shortcuts** with an attending or fellow in the subspecialty. The shortcuts that survive expert scrutiny are the ones worth internalizing.
- **For any specific cutoff cited,** verify against the source.

## Best model and why

**Claude Opus 4.7** — generating a comprehensive, ranked differential with discriminating features rewards depth. Opus produces more complete lists and more specific features than Sonnet. Use Sonnet for quick pattern-DDx review when comprehensiveness is less critical.
