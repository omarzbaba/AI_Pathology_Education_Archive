---
title: Tumor board case packet
pillar: educational-operations
event_type: conference
audience: faculty
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: tumor-board, case-packet, phi-protection
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-18
---

## What this prompt does

Generates a tumor board case packet template supporting N cases per session. Every case is structured identically. Strict PHI protection: no name, no MRN, no exact age, no exact date, no rare-combination giveaways.

## When to use it

When you're standardizing your tumor board's case presentation format. Updates needed when board composition changes.

## The prompt

```
You are generating a tumor board case packet template. STRICT PHI rules: NO name, no MRN, no exact age (use "in their 60s"), no exact date, no rare-disease-plus-location combinations. If a case can't be sufficiently de-identified, tell me.

## What I'm building

- **Tumor board name:** [e.g., "GU multidisciplinary tumor board"]
- **Cases per session:** [N]
- **Board attendees by specialty:** [med onc, rad onc, surg, radiology, others]
- **Institutional retention requirements:** [if known]
- **Case file format:** [paper packet / shared electronic file]

## For each case in the packet:

1. **De-identified header**
   - Case number, demographic envelope (age range, sex if relevant to pathology), referring specialty, date discussed
2. **Brief clinical history (2-3 sentences)** — presentation, key comorbidities, prior workup. No PHI.
3. **Imaging summary** — modality, key findings, formal radiology read summary
4. **Pathology summary** — gross, microscopic, IHC, molecular. Ordered by what's diagnostically discriminating.
5. **Current diagnosis and stage** (if applicable)
6. **The question for the board** — explicit single decision being asked
7. **Treatment options under consideration** — 2-3 alternatives with rationale
8. **Anticipated discussion points** — 2-3 things you expect the board to weigh in on
9. **Outcome decision** (filled in after the discussion)

## Packet header

- Date, attendees, standing references (e.g., institutional treatment protocols)

## Hard rules

- **NO PHI in any case packet.**
- **Outcome field filled in for every case** — administrative discipline matters.
- **Decision question explicit** — boards stall when this is unclear.
- **Format matches institutional retention requirements.**

## What I will NOT accept

- Templates that allow PHI to creep in
- Missing outcome field
- Vague decision questions
```

## Expected output

Packet header template + per-case template, consistent format.

## Required human verification

- **Verify no PHI** in any case before circulating.
- Confirm outcome field is filled for every case (admin discipline).
- Match retention requirements.

## Best model and why

**Claude Sonnet 4.6** — template generation. PHI discipline matters more than model choice.
