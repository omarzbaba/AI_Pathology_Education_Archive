---
title: Tumor board case presentation template
pillar: teaching
event_type: n/a
audience: faculty
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: tumor-board, presentation, structured-format
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Generates a tumor board case presentation outline that walks through history → imaging → pathology in the order the audience needs it, ends with an explicit decision question for the board, and anticipates the 2-3 most likely follow-up questions.

The hardest discipline: strip ALL patient identifiers before generating the outline. The model cannot un-see identifiers once they're in the conversation.

## When to use it

When you're presenting a case at tumor board and need a structured outline. Also useful as a teaching tool for junior residents who need to learn the structure.

**Not for:** real-time presentation prep (use the tumor board prep coaching prompt instead), generating the packet (use [Tumor board case packet](library.html#/library/pillar-3-educational-operations/prompts/conferences-and-journal-clubs/tumor-board-case-packet)), or cases that can't be sufficiently de-identified.

## The prompt

```
You are generating a tumor board case presentation outline. STRIP ALL PATIENT IDENTIFIERS before generating. No name, no MRN, no exact age, no exact date, no rare-combination giveaways.

## Provenance check first

Confirm the case I'm pasting is sufficiently de-identified. If anything looks identifiable, STOP and tell me before generating the outline.

## What I'm presenting

- **Clinical history (de-identified):** [paste — age range, sex if relevant, brief presentation, comorbidities, prior workup]
- **Imaging findings:** [paste summary]
- **Pathology findings:** [paste — gross, microscopic, IHC, molecular as available]
- **Question for the board:** [the explicit decision being asked — staging, treatment, second opinion, etc.]
- **Tumor board type:** [GU MDTB, GI MDTB, etc.]

## Outline structure (3-4 minutes of presentation)

1. **One-sentence patient summary** (anonymized): age range, key comorbidity if relevant, presentation
2. **Imaging summary** in radiologist-friendly framing — what they need to know to interpret the pathology
3. **Pathology in order:** gross → microscopic → IHC → molecular. Lead with diagnostic features, not workup history.
4. **Diagnosis and stage** (if applicable)
5. **The decision point** — what the board is being asked to advise on, stated explicitly
6. **2-3 most likely questions from the board** — from med onc, rad onc, surg, radiology — and the data points to have ready

Length: 3-4 minutes of presentation time. No PHI.

## Hard rules

- **No PHI ever** — strip identifiers before generating.
- **Decision point explicit, not buried.** The board should know what you're asking by minute 1.
- **Anticipated questions from each relevant specialty** present at YOUR institution's board.
- **Pathology presented in DIAGNOSTIC order** (what tells you the diagnosis first) not workup chronological order.

## What I will NOT accept

- Any identifiable patient information
- Decision question buried at the end
- Generic anticipated questions that don't match the case
- Pathology in workup-chronological order (boring) rather than diagnostic-priority order
```

## Expected output

A structured outline ready to present (~400-600 words) plus anticipated questions and data points.

## Common failure modes

- **Identifiable info slipping through.** Strip BEFORE pasting.
- **Decision question buried.** Push back.

## Required human verification

- **No PHI ever** — verify de-identification.
- Verify pathology summary against your sign-out.
- Run anticipated questions by a colleague who attends your tumor board regularly.

## Best model and why

**Claude Sonnet 4.6** — structured case outlines are Sonnet's wheelhouse. PHI discipline is more important than model choice.
