---
title: Forward case drill — diagnosis to expected findings
pillar: self-education
event_type: n/a
audience: resident
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: case-based, drilling, expected-findings
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Reverses the usual study direction: instead of given-findings-name-diagnosis, you name a diagnosis and the model generates the full constellation of findings you would expect, labeled by diagnostic weight (pathognomonic / highly supportive / supportive / non-specific) and including the findings that would RULE THE DIAGNOSIS OUT.

The discipline this builds: distinguishing features that are *truly pathognomonic* from features that are *highly characteristic* — a distinction over-collapsed in most learning resources.

## When to use it

When you're studying a diagnosis you've read about but haven't seen many times. Also useful as the second step in a learning chain after [Concept explanation at level](library.html#/library/pillar-1-self-education/prompts/concept-explanation-at-level) — first understand the entity, then drill the findings.

**Not for:** real case interpretation (different prompt and different stakes), exhaustive textbook coverage (just read the chapter), or first-time learning of the entity (concept explanation first).

## The prompt

```
You are generating the expected-findings constellation for a diagnosis I'm studying. Be strict about labeling pathognomonic features — over-labeling is the most common failure mode here.

## What I'm studying

- **Diagnosis:** [exact entity name — e.g., "follicular lymphoma, grade 1-2", not just "FL"]
- **My level:** [PGY level + relevant rotation context]
- **Why I'm studying it:** [optional — board prep, sign-out, teaching prep]

## What to produce — 5 sections

### 1. Clinical presentation

- Demographics (age range, sex, predisposing factors)
- Common symptoms and presentations
- Typical workup that brings the patient to pathology
- Common comorbidities or associations

### 2. Laboratory findings

- What's elevated, what's low, what's normal-but-tested (with reference ranges)
- Findings that would specifically be ordered for this differential
- Findings that should be normal in this entity (negative findings matter)

### 3. Imaging findings

- Modality typically used
- What's seen, organized by what's diagnostic vs supportive

### 4. Morphologic and histopathologic findings

- Low power: architecture, distribution
- Mid power: cell populations, stromal context
- High power: cellular detail (nuclear features, cytoplasm)
- IHC: typical positive and negative stains, with clone where clone-dependent
- Molecular: characteristic alterations, with source for each

### 5. Findings that RULE THE DIAGNOSIS OUT

This is the most underrated section. What negative findings should make you reconsider? What positive findings would force you to switch to a different diagnosis?

## Labeling — strict rules

For EVERY finding, label it:
- **[Pathognomonic]** — UNIQUE to this diagnosis. If a finding appears in any other entity, it's not pathognomonic. Almost no features are truly pathognomonic.
- **[Highly supportive]** — Strongly suggests this diagnosis but not unique
- **[Supportive]** — Consistent with the diagnosis but also present in others on the differential
- **[Non-specific]** — Common but doesn't help discriminate

Over-labeling pathognomonic findings is the most common failure mode. If in doubt, downgrade.

## Source any specific value

Cutoffs, reference ranges, percentages, classification criteria — cite the source: `[WHO HAEM5]`, `[NCCN v2.2024]`, etc.

## After the constellation

Ask me ONE question: "On a sign-out, which 2-3 findings would you prioritize describing, and why?"

Wait for my answer before discussing.

## Hard rules

- Strict pathognomonic discipline
- Source any specific value
- Include negative findings (Section 5 is non-negotiable)
- IHC clones named where clone-dependent
- No invented features

## What I will NOT accept

- Liberal use of "pathognomonic"
- Section 5 (rule-out findings) omitted
- Specific values without sources
- Cell-by-cell description rather than weighted by diagnostic importance
```

## Expected output

5 sections covering clinical / lab / imaging / morphology / rule-out findings, each finding labeled by diagnostic weight, sourced values, ending with a prioritization question for you.

## Common failure modes

- **Over-use of "pathognomonic."** Push back: "Verify — is this finding actually unique to this entity, or does it appear in [related entity]?"
- **Section 5 (rule-out) is thin or omitted.** Push for it.
- **Missing IHC clone information** where it matters.

## Required human verification

- Verify the pathognomonic labels against your subspecialty's current reference. The model overuses the label.
- Cross-check the morphologic findings against your subspecialty atlas.
- Verify any cited classification version is current.

## Best model and why

**Claude Opus 4.7** — distinguishing pathognomonic from supportive findings requires both medical knowledge depth and discipline about labels. Opus is more careful with this distinction than Sonnet.
