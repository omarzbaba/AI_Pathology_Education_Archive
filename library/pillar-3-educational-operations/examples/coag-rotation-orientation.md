---
title: Worked example — Coagulation rotation orientation packet
pillar: educational-operations
event_type: rotation
audience: program-director
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: rotation, orientation, coagulation, packet
verified_models: Claude Sonnet 4.5, GPT-4o
last_updated: 2026-05-17
---

## What this example shows

A program director used AI to draft a coagulation rotation orientation packet for a 4-week PGY-3 rotation. The total work took ~25 minutes — 8 minutes to write the input prompt, 2 minutes for the model to generate the draft, and 15 minutes of editing.

The example shows the **input → draft → final** progression with side-by-side commentary on what was kept, what was rewritten, and what was deleted.

## Input prompt

> I'm a CP program director. Generate a 4-page rotation orientation packet for a 4-week PGY-3 coagulation rotation at an academic medical center with a high-volume special coagulation lab. The packet should include:
>
> 1. A welcome paragraph (3-4 sentences, professional but human)
> 2. Rotation goals (5 bullets, milestone-aligned)
> 3. Weekly schedule template (typical Monday-Friday — sign-out at 8 am, didactics, case review, protected reading time, end-of-day wrap-up)
> 4. Key contacts (lab director, attending, fellow, charge tech, scheduler) — use placeholders for names
> 5. Required reading for week 1 (5 references) with one-sentence rationale per reference
> 6. Common pitfalls (3 specific to PGY-3s starting coag)
> 7. What success looks like by the end of week 1, week 2, week 4
>
> Use SI units. Use the phrase "the resident will" for objectives. Do not use any patient names or institutional identifiers. The tone should be welcoming but expectations should be explicit.

## AI-generated draft (excerpted)

> **Welcome to the Coagulation Rotation**
>
> Welcome to your four weeks on the coagulation service. This rotation will give you hands-on experience interpreting routine and special coagulation testing, participating in patient management discussions with hematology and surgery teams, and developing the diagnostic reasoning skills needed for an independent CP practice. We are excited to have you, and we expect a lot of you — both are true.
>
> **Rotation goals**
>
> By the end of the rotation, the resident will:
>
> - Interpret routine coagulation testing (PT, aPTT, fibrinogen, D-dimer) and identify patterns suggestive of common acquired and inherited bleeding disorders.
> - Order and interpret a focused workup for a patient with isolated prolonged aPTT, including mixing studies and factor assays.
> - Distinguish DIC from other consumptive coagulopathies using laboratory and clinical findings.
> - Recognize and triage critical coag values, including appropriate communication with the clinical team.
> - Participate in at least three coag consults per week with progressive autonomy.
>
> *[rest of the draft followed the requested sections]*

## Faculty edits — what changed and why

### Welcome paragraph: kept as drafted

The draft welcome paragraph was kept verbatim. "We are excited to have you, and we expect a lot of you — both are true" was the one line the PD wanted to keep; it was the model's, not the PD's.

### Rotation goals: 3 of 5 kept, 2 rewritten

**Kept:** the PT/aPTT/fibrinogen/D-dimer interpretation goal, the isolated prolonged aPTT workup goal, and the DIC distinction goal.

**Rewrote goal 4:** "Recognize and triage critical coag values" was too vague. The PD edited it to: "**Manage the panic-value workflow for critical INR and fibrinogen results, including triggering the institutional reversal protocol where appropriate, documenting the call in the LIS, and following up on disposition by end of shift.**" This is institution-specific and the model couldn't have generated it.

**Rewrote goal 5:** "At least three coag consults per week with progressive autonomy" was a fine number, but the PD wanted to add explicit autonomy gradient language: "**By week 4, the resident will independently formulate the workup plan and recommendation for routine consults, with attending review only at the final sign-out step.**"

### Required reading: 4 of 5 kept, 1 swapped

The model drafted a reasonable reading list (current textbook chapters, two ISTH guideline summaries, two recent review articles). The PD swapped one of the review articles for an **institutional protocol document** — the local massive transfusion protocol — which is not findable to the model and is the most important single document for a resident on this rotation.

### Common pitfalls: rewrote entirely

The model's drafted pitfalls were generic ("don't rely on a single value", "remember to consider pre-analytical factors"). The PD replaced them with three specific failure modes she had seen in residents:

> 1. **Reflexive mixing study on every prolonged aPTT.** A prolonged aPTT in a patient on heparin doesn't need a mixing study — confirm heparin contamination first.
> 2. **Calling a panic INR without checking the medication list.** The PD wants to know about the warfarin dose change before being woken up at 2 am about an INR of 5 on a stable outpatient.
> 3. **Treating D-dimer as a diagnostic test.** D-dimer is a screening test with a high negative predictive value, not a positive predictive one. Residents in their first week routinely overstate the meaning of a positive D-dimer.

These pitfalls are **judgment-derived**, not text-derived. The model could not have generated them.

### "What success looks like" section: kept the structure, customized the milestones

The model drafted reasonable week 1 / week 2 / week 4 milestones. The PD kept the structure but tightened the week 4 milestone to align with the program's milestone sub-competency language for CP-3 (Laboratory Operations and Quality Assurance).

## Time accounting

| Step | Time |
|---|---|
| Writing the input prompt | 8 min |
| Model generation | 2 min |
| Reading + first edit pass | 8 min |
| Inserting institution-specific content | 5 min |
| Final polish | 2 min |
| **Total** | **25 min** |

Estimated time from-scratch for the same packet: 90-120 minutes. Net savings: ~70-95 minutes.

## What this example does NOT show

- The model cannot generate **institutional vocabulary** — protocol names, contact roles, the specific LIS workflow. Every PD needs to bring these.
- The model cannot generate the **judgment-derived pitfalls** that come from watching residents make the same mistakes for years.
- The packet still needs to be **reviewed by the lab director and the chief technologist** before distribution — both for accuracy and for buy-in. AI does not change the institutional review process; it only changes the time to first draft.

## Reusing this approach for other rotations

The same input-prompt structure works for any rotation. Replace "coagulation" with "blood bank", "microbiology", "chemistry", "hematopathology" — the model will produce a structurally similar draft. The judgment-derived sections (pitfalls, institutional specifics, autonomy gradient) are what you bring.
