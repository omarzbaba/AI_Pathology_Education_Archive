---
title: Case vignette at PGY level
pillar: teaching
event_type: n/a
audience: faculty
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: vignette, case-based, level-calibration
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Generates a case vignette calibrated to a specific PGY level, with the right complexity, the right amount of clinical context, and demographics that reflect actual epidemiology rather than the textbook-archetype default. Also generates the intended diagnosis, the 2-3 most likely wrong answers at this level (with WHY each is appealing), and a discussion question.

The harder discipline this prompt enforces: vignettes should vary patient demographics across cases. A series of 20 vignettes all about middle-aged white men teaches residents to anchor on that archetype.

## When to use it

Designing case-based teaching, board-style question writing, or building a case bank for resident education. Especially useful when you want a specific cognitive challenge (e.g., "ambiguous lab data integration") rather than just a topic.

**Not for:** real case presentations (use the tumor board prompt instead), case-based assessment that needs psychometric validation, or first-time learning of an entity (use concept explanation first).

## The prompt

```
You are generating a case vignette for teaching. Calibration to PGY level is the entire point — the wrong calibration teaches nothing or frustrates the resident.

## What I'm requesting

- **Topic / diagnosis being taught:** [specific entity, not category]
- **Target audience:** [PGY level + rotation context]
- **Specific cognitive challenge:** [optional — e.g., "ambiguous initial labs", "atypical demographic", "discordant findings"]
- **Constraints:** [SI units, specific terminology, anything else]

## Level calibration guidance — apply explicitly

- **PGY-1:** classic presentation, one main differential to resolve, all relevant data given, no significant red herrings, no atypical demographics.
- **PGY-2:** typical presentation with a complicating factor (comorbidity that obscures the picture, a 'positive' test result that's actually a red herring, atypical demographic for the diagnosis).
- **PGY-3:** atypical presentation, ambiguous lab/imaging data, must integrate multiple discordant findings, decision under uncertainty.
- **PGY-4 / Fellow:** rare entity OR atypical presentation of common entity, requires judgment calls under significant uncertainty, considers cost/risk of further workup.

## What to produce

### The vignette

- **Length:** 4-7 sentences
- **Demographics:** include detail relevant to the differential. **Do NOT default to middle-aged white male.** Reflect the actual epidemiology of the condition; vary across cases when building a series.
- **Data:** include what the resident needs to reason from, no more
- **Ending:** stop at the point where the resident must commit to an interpretation or next step

### The intended diagnosis

State it explicitly.

### The 2-3 most likely wrong answers at this level

For each wrong answer:
- The wrong diagnosis
- WHY a resident at this level would pick it (the specific cognitive error or anchor)
- What in the vignette should have ruled it out

### Discussion question

One question to ask after the resident commits to their interpretation. Should require them to defend or critique their reasoning, not just restate it.

## Hard rules

- **PGY-1 vignettes do not have red herrings.** They're not "easy"; they're calibrated.
- **PGY-3 and Fellow vignettes must have genuine ambiguity.** Not just a longer vignette.
- **Demographics reflect the disease's actual epidemiology.** If the condition is more common in older Black men, that's the demographic to use, not a generic 50-year-old white man.
- **The wrong-answer analysis is the highest-value part.** Generic "they're wrong because the right answer is X" is unacceptable.
- **No PHI.** Vignettes are fictional or sufficiently genericized.

## What I will NOT accept

- A "PGY-3" vignette where the answer is obvious
- Demographics defaulted to textbook archetype
- Wrong-answer analysis that doesn't name the specific cognitive error
- A discussion question that's just "what would you do next?"
```

## Expected output

The vignette + intended diagnosis + 2-3 wrong-answer analysis + discussion question. Length depends on case; typically 400-600 words total.

## Common failure modes

- **Calibration miss** — "PGY-3" vignette that's PGY-1 difficulty. Push back.
- **Textbook demographics by default.** Push back: "Vary the demographic."
- **Generic wrong-answer analysis.** Push back: "What's the SPECIFIC cognitive error?"

## Required human verification

- Pressure-test the vignette against a resident at the target level before using in a session — is the difficulty actually right?
- Check demographics across a series — over 10-20 vignettes, is the distribution defensible?
- Verify clinical details (drug doses, lab cutoffs, classification version) against current source.

## Best model and why

**Claude Opus 4.7** — calibrating difficulty to PGY level, varying demographics intelligently, and generating substantive wrong-answer analyses all reward depth. Sonnet vignettes tend toward "classic presentation" regardless of stated level.
