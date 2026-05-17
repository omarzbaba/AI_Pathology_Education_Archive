---
title: Tumor board case presentation template
pillar: teaching
event_type: n/a
audience: faculty
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: tumor-board, presentation
verified_models: TODO
last_updated: 2026-05-17
---

## What this prompt does

Generate a tumor board case presentation outline given clinical history, imaging, and pathology findings. Tumor board presentations have a specific structure that AI can reliably scaffold.

## When to use it

When you're presenting a case at tumor board and need a structured outline to follow. Especially useful as a residency teaching tool — junior residents need to learn the structure.

## The prompt

```
Generate a tumor board case presentation outline for the following case:

- **Clinical history (de-identified):** [paste, no PHI]
- **Imaging findings:** [paste]
- **Pathology findings:** [paste — gross, microscopic, IHC, molecular as available]
- **Question for the board:** [what decision are you bringing to the multidisciplinary group? — staging, treatment plan, second opinion, etc.]

Outline structure:

1. **One-sentence patient summary** (anonymized): age range, key comorbidity if relevant, presentation.
2. **Imaging summary** in radiologist-friendly framing: what they need to know to interpret the pathology.
3. **Pathology in order:** gross → microscopic → IHC → molecular. Lead with the diagnostic features, not the workup history.
4. **Diagnosis and stage** if available.
5. **The decision point** — what the board is being asked to advise on.
6. **The 2-3 most likely questions** from the board (med onc, rad onc, surg, radiology) and the data points you should have ready.

Length: 3-4 minutes of presentation time. No PHI.
```

## Expected output

A structured outline ready to present, with anticipated questions and data points to have ready.

## Common failure modes

- Outline includes information that would identify a patient.
- The 'decision point' is buried rather than stated explicitly.
- Anticipated questions miss the actual ones that get asked at your institution's tumor board.

## Required human verification

- **No PHI ever.** Strip names, MRNs, exact ages, dates of service, institutional identifiers.
- Verify the pathology summary against your sign-out — the model may simplify in ways that mislead.
- Run anticipated questions by a colleague who attends your tumor board regularly.
