---
title: Worked example — Designing a PGY-2 transfusion reaction teaching session
pillar: teaching
event_type: n/a
audience: faculty
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: transfusion, vignette, mcq, teaching-session
verified_models: Claude Sonnet 4.5, GPT-4o
last_updated: 2026-05-17
---

## What this example shows

A 35-minute design session where a CP faculty member built a 50-minute small-group teaching session on transfusion reactions for PGY-2 residents in their first month of blood bank. The session uses one ambiguous case vignette and three matched MCQs.

The example shows three things side by side:

1. **The input prompt** — what the faculty member asked for
2. **The AI-generated draft** — what came back
3. **The faculty edits** — what changed, and why

The point of showing the edits is that **the model's first draft is structurally plausible but pedagogically generic**. The discriminating features that make a vignette teachable — the deliberately ambiguous fever onset, the wrong distractor that resembles a common misconception — are choices a human teacher has to make.

## Input prompt

> I'm a CP faculty member designing a 50-minute small-group session for PGY-2 residents in their first month of blood bank. The learning objective is: "Given a transfusion reaction scenario, the resident will distinguish between febrile non-hemolytic, acute hemolytic, and TRALI reactions based on the temporal pattern and clinical findings, and will name the immediate management steps for each."
>
> Generate **one case vignette** where the reaction type is intentionally ambiguous between febrile non-hemolytic and acute hemolytic. The vignette should be 4-6 sentences. Then generate **three MCQs** based on the vignette. The first MCQ should test recognition of the reaction type, the second should test the next best management step, and the third should test the underlying mechanism. For each MCQ, provide all 4 answer choices and a rationale for each choice.
>
> Calibrate to a PGY-2 — appropriate complexity, no esoteric distractors. Use SI units. Do not use any patient names or institutional identifiers.

## AI-generated draft (Claude Sonnet 4.5)

> **Case vignette**
>
> A 58-year-old patient receiving the second unit of packed red blood cells for symptomatic anemia develops a temperature rise from 37.0°C to 38.5°C approximately 45 minutes into the transfusion. The patient reports mild chills but no back pain. Blood pressure is 118/76 mmHg, heart rate is 92 bpm, oxygen saturation is 98% on room air. The transfusion is paused.
>
> **MCQ 1 — Most likely reaction type**
>
> A. Febrile non-hemolytic transfusion reaction *(correct)*
> B. Acute hemolytic transfusion reaction
> C. TRALI
> D. Allergic reaction
>
> Rationale A: Fever ≥1°C above baseline without hemodynamic instability, hypoxia, or back pain is most consistent with FNHTR.
> Rationale B: Acute hemolytic reactions classically present with fever AND hypotension, back pain, hemoglobinuria.
> Rationale C: TRALI presents within 6 hours of transfusion with hypoxia and bilateral pulmonary infiltrates.
> Rationale D: Allergic reactions present with urticaria, pruritus, and in severe cases bronchospasm.
>
> **MCQ 2 — Next best step**
>
> A. Restart transfusion at slower rate
> B. Administer epinephrine
> C. Send patient and unit samples to blood bank for workup *(correct)*
> D. Premedicate with diphenhydramine and restart
>
> *[rationales follow]*
>
> **MCQ 3 — Mechanism**
>
> A. Recipient antibodies against donor leukocyte HLA antigens *(correct)*
> B. ABO incompatibility with intravascular hemolysis
> C. Donor antibodies against recipient HLA antigens in the lung
> D. IgE-mediated mast cell degranulation
>
> *[rationales follow]*

## Faculty edits (annotated in **bold red** in the actual edit, simulated here in italics)

### Vignette edits

The faculty member made three changes:

1. *Original: "approximately 45 minutes into the transfusion."*
   **Edited to: "approximately 25 minutes into the transfusion."**
   *Reason: 45 minutes makes the case too easy — it sits comfortably in FNHTR territory. 25 minutes is in the overlap window where both FNHTR and an early acute hemolytic reaction are reasonable.*

2. *Original: "but no back pain."*
   **Edited to: "no back pain reported. Patient is sedated for end-stage liver disease and unable to give a reliable subjective history."**
   *Reason: removing the patient's ability to self-report ambiguates the case appropriately. This forces the resident to rely on the objective findings, which is the actual clinical situation.*

3. *Original: "blood pressure is 118/76 mmHg"*
   **Edited to: "blood pressure is 102/68 mmHg (was 124/76 mmHg pre-transfusion)."**
   *Reason: a borderline drop is exactly the kind of finding that distinguishes a teachable vignette from a giveaway. The resident has to decide whether 14-point drop matters.*

### MCQ 1 edits

The faculty member **flipped the correct answer** to "acute hemolytic transfusion reaction" given the vignette edits, and rewrote the rationales to emphasize:

- The "1°C above baseline" criterion alone is **necessary but not sufficient** for FNHTR
- A blood pressure drop, even a small one, in a patient who can't self-report **forces the workup**
- The discriminating principle: *when in doubt, treat as the worse possibility until disproven*

### MCQ 2 edits

The faculty member added a discussion note for the facilitator:

> Even residents who correctly pick C ("send to blood bank") often skip the **most time-sensitive step before that**, which is to also **maintain IV access with normal saline** and **send a urinalysis for free hemoglobin**. Use this as a teaching moment about prioritization, not just identification.

### MCQ 3

The faculty member kept this MCQ largely as drafted but added a distractor revision:

> Replace D ("IgE-mediated mast cell degranulation") with "**Cytokine release from donor leukocytes accumulated during storage**". This is a much more dangerous distractor because it's actually a *contributing mechanism* to FNHTR — it lets you ask a follow-up question about why leukoreduction reduces FNHTR risk.

## Final teaching-ready output

After ~15 minutes of editing, the faculty member had:

- A vignette that requires the resident to integrate three pieces of evidence (timing, BP drop, inability to self-report)
- Three MCQs that progress from recognition to action to mechanism
- A facilitator note that surfaces a common cognitive shortcut
- One distractor revision that opens a path to a follow-up question on leukoreduction

**Time saved vs starting from scratch: ~30 minutes.** Time spent editing: ~15 minutes. Net: ~15 minutes saved, plus a more pedagogically deliberate session than the faculty member would have built under time pressure.

## What this example does NOT show

- This is not a session designed for a board exam. The MCQs are pedagogical; they would not necessarily pass a psychometric review.
- The model did not generate the *teaching judgment* — when to make a case ambiguous, when to keep a distractor mild, when to add a facilitator note. That came from the faculty member.
- A separate review pass for demographic representation (age, sex, race) of patients across a series of cases is needed at the course level, not the single-case level. See [Guardrails](library.html#/docs/guardrails).
