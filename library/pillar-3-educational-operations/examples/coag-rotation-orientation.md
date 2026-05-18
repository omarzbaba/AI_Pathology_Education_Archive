---
title: Worked example — Coagulation rotation orientation packet
pillar: educational-operations
event_type: rotation
audience: program-director
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: rotation, orientation, coagulation, packet, worked-example
verified_models: Claude Sonnet 4.5, GPT-4o
best_model: Claude Sonnet 4.6
last_updated: 2026-05-18
---

## What this example shows

A program director used AI to draft a coagulation rotation orientation packet for a 4-week PGY-3 rotation. Total work: ~25 minutes — 8 minutes to write the input prompt, 2 minutes for the model to generate the draft, 15 minutes of editing.

The example shows the **input → draft → final** progression with side-by-side commentary on what was kept, what was rewritten, and what was deleted entirely. The most important pattern: **institutional vocabulary, judgment-derived pitfalls, and named contacts** are content the model fundamentally cannot generate — only humans with operational knowledge of the rotation can supply them.

This is the most useful example in Pillar 3 because it demonstrates the **scaffold-and-replace** pattern that's the right model for educational operations work: AI builds the structure; you replace the placeholder content with the substance that makes it usable.

## Setup

- **PD:** CP program director, ~5 years in role
- **Rotation:** 4-week PGY-3 coagulation rotation at an academic medical center
- **Audience:** Incoming PGY-3 residents (4-6 per year)
- **Tool:** Claude Sonnet 4.6
- **Time invested:** 25 minutes total
- **From-scratch comparison:** ~90-120 minutes for the same packet
- **Net savings:** ~70-95 minutes, plus better structure than under-time-pressure first drafts

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
> Use SI units. Use the phrase "the resident will" for objectives. Do not use any patient names or institutional identifiers.

*Annotation: the prompt is doing the prompt-engineering work well — specifying length, structure, level, formatting conventions, and what NOT to include. What it doesn't do (and what the PD added in subsequent uses): ask the model to explicitly flag which sections will need institutional substitution.*

## AI-generated draft (excerpted)

### Welcome to the Coagulation Rotation

> Welcome to your four weeks on the coagulation service. This rotation will give you hands-on experience interpreting routine and special coagulation testing, participating in patient management discussions with hematology and surgery teams, and developing the diagnostic reasoning skills needed for an independent CP practice. We are excited to have you, and we expect a lot of you — both are true.

### Rotation goals

> By the end of the rotation, the resident will:
>
> - Interpret routine coagulation testing (PT, aPTT, fibrinogen, D-dimer) and identify patterns suggestive of common acquired and inherited bleeding disorders.
> - Order and interpret a focused workup for a patient with isolated prolonged aPTT, including mixing studies and factor assays.
> - Distinguish DIC from other consumptive coagulopathies using laboratory and clinical findings.
> - Recognize and triage critical coag values, including appropriate communication with the clinical team.
> - Participate in at least three coag consults per week with progressive autonomy.

*[Rest of the draft followed the requested sections.]*

## Faculty edits — what changed and why

### Welcome paragraph: KEPT verbatim

The draft welcome paragraph was kept exactly as written. "We are excited to have you, and we expect a lot of you — both are true" was the one line the PD wanted to keep. *The model's; not the PD's.*

*Annotation: this is unusual — most AI-generated openings get rewritten. The model's phrasing of "both are true" struck the PD as exactly right for the tone he wanted. Worth keeping when it lands.*

### Rotation goals: 3 of 5 kept, 2 substantively rewritten

**Kept:**
- PT/aPTT/fibrinogen/D-dimer interpretation goal
- Isolated prolonged aPTT workup goal
- DIC distinction goal

**Rewrote goal 4** (critical values):

> Original: "Recognize and triage critical coag values, including appropriate communication with the clinical team."
>
> **Edited to: "Manage the panic-value workflow for critical INR and fibrinogen results, including triggering the institutional reversal protocol where appropriate, documenting the call in the LIS, and following up on disposition by end of shift."**

*Annotation: "appropriate communication" is the kind of vague language the model defaults to. The PD replaced it with the specific institutional workflow — the panic value, the reversal protocol, the LIS documentation, the end-of-shift follow-up. **This is content the model fundamentally cannot generate** because it depends on knowing the institution.*

**Rewrote goal 5** (autonomy gradient):

> Original: "Participate in at least three coag consults per week with progressive autonomy."
>
> **Edited to: "By week 4, the resident will independently formulate the workup plan and recommendation for routine consults, with attending review only at the final sign-out step."**

*Annotation: "progressive autonomy" is empty. The edited version specifies the endpoint — independent workup formulation by week 4 — which is assessable.*

### Required reading: 4 of 5 kept, 1 swapped

The model drafted a reasonable reading list:
- 2 current textbook chapters
- 2 ISTH guideline summaries
- 1 recent review article on lupus anticoagulant testing

The PD swapped one of the items:

> **Removed:** The recent review article on lupus anticoagulant testing (good, but not the most important on day 1)
>
> **Replaced with:** The institutional massive transfusion protocol document — not findable to the model, and the most important single document for a resident on this rotation.

*Annotation: this swap is the most common pattern in operations editing. The model defaults to publicly available references; the most important documents for a real rotation are often institutional.*

### Common pitfalls: REWROTE ENTIRELY

The model's drafted pitfalls were generic:
- "Don't rely on a single value"
- "Remember to consider pre-analytical factors"
- "Always think about the clinical context"

The PD replaced them with three specific failure modes she had seen in residents:

> 1. **Reflexive mixing study on every prolonged aPTT.** A prolonged aPTT in a patient on heparin doesn't need a mixing study — confirm heparin contamination first.
> 2. **Calling a panic INR without checking the medication list.** The PD wants to know about the warfarin dose change before being woken up at 2 am about an INR of 5 on a stable outpatient.
> 3. **Treating D-dimer as a diagnostic test.** D-dimer is a screening test with a high negative predictive value, not a positive predictive one. Residents in their first week routinely overstate the meaning of a positive D-dimer.

*Annotation: these pitfalls are **judgment-derived** — they come from watching residents make the same mistakes over years. **The model cannot generate them.** This is the most reliable rule of thumb: anything that requires longitudinal observation of trainees is content you supply, not content AI generates.*

### "What success looks like" section: structure kept, milestones customized

The model drafted reasonable week 1 / week 2 / week 4 milestones. The PD kept the structure but tightened the week 4 milestone to align with her program's milestone sub-competency language for CP-3 (Laboratory Operations and Quality Assurance).

## Time accounting

| Step | Time |
|------|------|
| Writing the input prompt | 8 min |
| Model generation | 2 min |
| Reading + first edit pass | 8 min |
| Inserting institution-specific content | 5 min |
| Final polish | 2 min |
| **Total** | **25 min** |

Estimated time from-scratch: 90-120 minutes.
**Net savings:** ~70-95 minutes.

## What this example does NOT show

- The model cannot generate **institutional vocabulary** — protocol names, contact roles, specific LIS workflows. Every PD needs to bring these.
- The model cannot generate **judgment-derived pitfalls** that come from watching residents make the same mistakes for years.
- The packet still needs to be **reviewed by the lab director and the chief technologist** before distribution — for accuracy and for buy-in. AI does not change the institutional review process; it only changes the time to first draft.
- This was a relatively well-scoped rotation. A more complex rotation (multi-service, longer duration, more attendings) would require more editing.

## How to use this pattern for other rotations

The same input-prompt structure works for any rotation. Replace "coagulation" with "blood bank", "microbiology", "chemistry", "hematopathology" — the model will produce a structurally similar draft. **The judgment-derived sections (pitfalls, institutional specifics, autonomy gradient) are what you bring.**

Rule of thumb: **expect to rewrite the "common pitfalls" section entirely**, swap 1-2 reading list items, and customize the autonomy gradient. The welcome paragraph, schedule template, and overall structure are usually fine as drafted.

## Related prompts

- [Rotation orientation one-pager](library.html#/library/pillar-3-educational-operations/prompts/rotations/orientation-onepager) — for the shorter one-page version
- [Rotation expectations document](library.html#/library/pillar-3-educational-operations/prompts/rotations/expectations-doc) — for the formal handbook version
- [Rotation reading list with rationale](library.html#/library/pillar-3-educational-operations/prompts/rotations/reading-list)
- [Daily schedule template](library.html#/library/pillar-3-educational-operations/prompts/rotations/daily-schedule)
