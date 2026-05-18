---
title: Matched case pair — reactive vs neoplastic
pillar: teaching
event_type: n/a
audience: faculty
difficulty: advanced
time_to_use: 2-10min
visual: text-only
tags: vignette, differential, paired-cases
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Generates two case vignettes that share superficial features but diverge on a specific discriminating feature — the one you want to teach. The pair structure forces residents to NOTICE the discriminator rather than pattern-match to a likely diagnosis. The hardest discipline this enforces: the cases must be parallel in every dimension EXCEPT the intended discriminator.

## When to use it

When teaching a differential where two entities are commonly confused, especially when the discrimination is taught in a textbook but rarely drilled in cases. Pairs well with sign-out teaching or journal club discussion.

**Not for:** generic case generation (use [Case vignette at PGY level](library.html#/library/pillar-2-teaching/prompts/case-vignette-pgy)), broader pattern discrimination (use [Differential by histologic pattern](library.html#/library/pillar-1-self-education/prompts/differential-by-histologic-pattern)), or pairs where you don't yet know what the discriminating feature should be.

## The prompt

```
You are generating a matched case pair for teaching a specific discrimination. The pair must be parallel in every dimension EXCEPT the intended discriminator.

## What I'm requesting

- **Entity A and Entity B to discriminate:** [be specific — e.g., "reactive follicular hyperplasia (Entity A) vs grade 1-2 follicular lymphoma (Entity B)"]
- **The discriminating feature(s) I want to teach:** [name the specific feature — e.g., "bcl-2 positivity in follicles, absent in reactive and present in FL"]
- **Audience level:** [PGY level + rotation context]
- **Cognitive trap to avoid:** [optional — e.g., "residents tend to anchor on architecture and miss the IHC"]

## What to produce

### Case A

- **Vignette (4-6 sentences):** clinical context, presentation, initial findings
- **Histology description:** what's on the slide at low → high power
- **Workup results:** IHC, molecular as relevant
- **The discriminating feature as it appears in THIS case** (positive or negative)
- **Intended diagnosis:** stated explicitly

### Case B

Same structure. **Parallel to Case A in every dimension** (similar age range, similar location, similar presenting complaint, similar initial workup architecture) EXCEPT for the discriminating feature.

### Side-by-side comparison table

| Feature | Case A | Case B |
|---|---|---|

Include the features that are SAME (so residents notice that the difference is NOT in those features) and the discriminating feature(s).

### The 'aha' question

When residents see both side by side, what specific question crystallizes the discrimination? Phrase the exact question — not "ask them to compare," the question itself.

## Hard rules

- **Parallelism is the entire point.** If the cases differ in age, sex, location, presenting complaint, etc., the discrimination becomes confounded.
- **The discriminating feature must be the SAME feature in both cases** — present in one, absent in the other (or different in a specific way). Not "Case A has X, Case B has Y."
- **The 'aha' question is non-negotiable.** Without it, the pair is just two cases.
- **No PHI.** Both vignettes are fictional or sufficiently genericized.

## What I will NOT accept

- Pairs that differ in confounding features
- Discriminators that depend on tests I can't get in real practice
- 'Aha' questions that are leading rather than illuminating
- Vignettes of very different lengths or detail levels (signals the difference)
```

## Expected output

Two parallel cases + side-by-side table + 'aha' question. Length ~500-700 words.

## Common failure modes

- **Confounded cases.** Push back: "Cases differ in [feature]. Make them parallel."
- **'Aha' question is leading.** Push back: "Make it open-ended."

## Required human verification

- Verify the discriminator is what current practice actually uses (not an outdated criterion).
- Pressure-test with a resident who hasn't been taught the discrimination — do they notice it, or does the pair feel like "two cases"?

## Best model and why

**Claude Opus 4.7** — parallel construction with a single deliberate difference is harder than it looks. Opus is more disciplined about NOT varying confounding features.
