---
title: Blood smear systematic review walkthrough
pillar: self-education
event_type: n/a
audience: resident
difficulty: intermediate
time_to_use: 2-10min
visual: multimodal
tags: blood-smear, hematology, systematic-review, multimodal
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Builds the habit of reading a peripheral blood smear systematically — RBCs, WBCs, platelets, in that order, with specific observations at each magnification — rather than pattern-matching to the most likely diagnosis. This discipline distinguishes pathologists who catch the second finding from those who anchor on the first.

## When to use it

During your first weeks of clinical hematology or when you're trying to break the habit of going straight to "what is this" rather than "what do I see." Pairs well with a teaching atlas of smears.

**Not for:** real patient smears (use your scope), settled diagnoses (look those up), or quick pattern matching when speed matters (different drill).

## Safety

Published teaching images or public-domain only. No real patient smears. See [Guardrails](library.html#/docs/guardrails).

## The prompt

```
You are my blood smear reading discipline coach. I'll upload a peripheral blood smear image (teaching case, confirmed). Walk me through the systematic review I should perform every single time.

## What I'm uploading

- **Stain and magnification:** [e.g., "Wright-Giemsa at 1000x oil immersion"]
- **Clinical context (if known):** [optional — including this changes the discipline test]
- **Source:** [confirm: teaching atlas / public domain / cleared collection]

## The systematic review you'll walk through

### Pass 1: Low power (10-20x)

Before any cellular detail, describe:
- Smear quality (well-spread vs thick/thin, monolayer adequacy, distribution)
- General cellularity (hypo/normo/hypercellular vs the white count)
- Distribution patterns (clumping, rouleaux, agglutination)
- Anything immediately unusual at low power (large cell aggregates, parasites, schistocytes obvious at low power)

### Pass 2: RBC review (40-100x)

In ORDER, comment on:
- **Size** (anisocytosis, micro vs macro vs normocytic; compare to small lymphocyte nucleus)
- **Shape** (poikilocytosis: sickle, target, spherocytes, schistocytes, teardrops, burr cells, acanthocytes, ovalocytes, stomatocytes)
- **Color** (hypochromasia, polychromasia)
- **Inclusions** (Howell-Jolly, basophilic stippling, Pappenheimer, Heinz, Cabot rings, parasites)
- **Distribution** (rouleaux, agglutination, autoagglutination)

### Pass 3: WBC review (100x oil)

In ORDER:
- **Estimated count vs reported count** (rough estimate × 1500 per HPF for 100x oil)
- **Differential** (neutrophils, bands, lymphs, monos, eos, basos)
- **Neutrophil abnormalities** (hypogranulation, hypersegmentation, toxic changes, Döhle bodies, Auer rods, dysplastic features)
- **Lymphocyte abnormalities** (reactive vs atypical lymphs, blasts, hairy cells, Sézary cells, smudge cells)
- **Monocytes** (atypical, dysplastic)
- **Blasts** (count per area, morphology if present)

### Pass 4: Platelet review (100x oil)

- **Estimated count** (per HPF × 15-20K for 100x oil; flag if discordant with reported count)
- **Size** (giant platelets, normal size variation)
- **Clumping** (genuine vs EDTA-induced)
- **Morphology** (granulation, fragmented platelets)

### Pass 5: Anything I should NOT miss

Even if low probability, what should I make sure I looked for given the context provided? Examples: parasites in fever of unknown origin, schistocytes in suspected TTP, blasts in cytopenia.

### Then ask me ONE check question

Before revealing your impression, ask me about ONE specific observation from one of the passes. Wait for my answer.

## Hard rules

- **Walk through every pass, in order.** Don't skip Pass 1 because it seems too basic — that's where smear quality issues that confound everything else are caught.
- **Estimated counts must be physiologic.** A patient with reported WBC of 100K should have proportionally more cells per HPF; if the smear doesn't match, name the discrepancy.
- **Do NOT skip to a diagnosis until I commit.**
- **If a finding is borderline or ambiguous, say so.** Do not commit to "schistocytes present" if you're seeing 1-2 per HPF that are equivocal.
```

## Expected output

Five passes in order with specific observations at each, then a check question waiting for your answer. The five-pass structure is the entire point — repeating it builds the reflex.

## Common failure modes

- **Skipping the low-power pass.** This is where smear quality issues hide. Push back if Pass 1 is perfunctory.
- **Confident overcalls** of subtle findings. Schistocytes are over-called constantly; the model should reflect that calibration.
- **Estimated counts disconnected from the reported CBC.** Push back when math doesn't add up.
- **Premature diagnostic commitment.** Same fix as the other multimodal prompts.

## Required human verification

- **Compare against the published key** for the teaching case. The five passes are the discipline; the specific findings are where you check the model.
- **For schistocytes, blasts, parasites, or other high-stakes findings the model identifies,** verify against the published key — these are the findings where AI false-positives can mislead.

## Best model and why

**Claude Sonnet 4.6** for the systematic structure and most multimodal pattern recognition. **Gemini 2.5 Pro** if you want maximum fine-detail visual analysis. The discipline of the five passes matters more than model choice.
