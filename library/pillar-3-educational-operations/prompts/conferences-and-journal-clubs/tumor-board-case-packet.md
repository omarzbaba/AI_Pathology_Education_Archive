---
title: Tumor board case packet
pillar: educational-operations
event_type: conference
audience: faculty
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: tumor-board, packet
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Generate a tumor board case packet with history, imaging summary, pathology findings, treatment options, and discussion questions.

## When to use it

When you're preparing cases for an upcoming tumor board. The packet structure ensures the cases get presented consistently.

## The prompt

```
Generate a tumor board case packet template for [tumor board name — e.g., 'GU multidisciplinary tumor board']. The template should support presentation of [N] cases per session.

For each case in the packet:

1. **De-identified header**: case number, demographic envelope (age range, sex if relevant to pathology), referring specialty, date case was discussed.
2. **Brief clinical history** (2-3 sentences): presentation, key comorbidities, prior workup. No PHI.
3. **Imaging summary**: modality, key findings, formal radiology read summary.
4. **Pathology summary**: gross findings, microscopic findings, IHC results, molecular results. Organized by what's diagnostically discriminating.
5. **Current diagnosis and stage** (if applicable).
6. **The question for the board**: explicit, single decision being asked of the multidisciplinary group.
7. **Treatment options under consideration**: 2-3 alternatives with rationale for each.
8. **Anticipated discussion points**: 2-3 things you expect the board to weigh in on.
9. **Outcome decision** (filled in after the discussion).

Plus a packet header with date, attendees, and any standing references (e.g., institutional treatment protocols).

The packet should be PHI-free and suitable for retention as part of the case file.

**Important — refinement:** STRONG REMINDER: strip ALL patient identifiers from each case. No name, no MRN, no accession number, no exact age (use 'in their 60s'), no exact date of service, no institutional identifiers, no rare-disease-plus-location combinations that enable re-identification. If a case feels like it cannot be sufficiently de-identified, tell me.
```

## Expected output

A template for the packet header + a per-case template. Together they support consistent case presentation.

## Common failure modes

- Templates that allow PHI to creep in.
- The 'question for the board' is unclear, leading to unfocused discussion.
- No outcome field — board decisions don't get documented.

## Required human verification

- **Verify no PHI** in any case packet before circulating.
- Confirm the 'outcome decision' field is filled in for every case (administrative discipline matters).
- Match the packet format to institutional retention requirements.

## Best model and why

**Claude Sonnet 4.6** — Template generation — Sonnet is sufficient. The PHI discipline is the entire safety story here; verify before pasting case material regardless of model.
