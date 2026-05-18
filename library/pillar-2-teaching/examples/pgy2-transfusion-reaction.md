---
title: Worked example — Designing a PGY-2 transfusion reaction teaching session
pillar: teaching
event_type: n/a
audience: faculty
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: transfusion, vignette, mcq, teaching-session, worked-example
verified_models: Claude Sonnet 4.5, GPT-4o
best_model: Claude Opus 4.7
last_updated: 2026-05-18
---

## What this example shows

A 35-minute design session where a CP faculty member built a 50-minute small-group teaching session on transfusion reactions for PGY-2 residents in their first month of blood bank. The session uses one ambiguous case vignette and three matched MCQs.

The example shows three things side by side:

1. **The input prompt** — what the faculty member asked for
2. **The AI-generated draft** — what came back
3. **The faculty edits** — what changed, and why each change matters

**The point of showing the edits is that the model's first draft is structurally plausible but pedagogically generic.** The discriminating features that make a vignette *teachable* — the deliberately ambiguous fever onset, the wrong distractor that resembles a common misconception, the matched-pair logic — are judgment calls a human teacher has to make.

This is the most important example in Pillar 2 because it shows the **edit-as-discipline** pattern: AI gives you the scaffold; you supply what makes the session land.

## Setup

- **Faculty member:** CP faculty, ~10 years on blood bank service
- **Audience:** 4 PGY-2 residents in their first month of blood bank
- **Format:** 50-minute small group; 1 vignette + 3 MCQs + discussion
- **Tool:** Claude Opus 4.7 (chosen for nuanced vignette generation)
- **Time invested:** 35 minutes (8 min prompt drafting + 2 min generation + 20 min editing + 5 min final review)
- **Outcome:** A vignette that residents reliably get wrong in instructive ways; 3 MCQs that produce discussion rather than rapid agreement

## Input prompt

> I'm a CP faculty member designing a 50-minute small-group session for PGY-2 residents in their first month of blood bank. The learning objective is: "Given a transfusion reaction scenario, the resident will distinguish between febrile non-hemolytic, acute hemolytic, and TRALI reactions based on the temporal pattern and clinical findings, and will name the immediate management steps for each."
>
> Generate **one case vignette** where the reaction type is intentionally ambiguous between febrile non-hemolytic and acute hemolytic. The vignette should be 4-6 sentences. Then generate **three MCQs** based on the vignette. The first MCQ should test recognition of the reaction type, the second should test the next best management step, and the third should test the underlying mechanism. For each MCQ, provide all 4 answer choices and a rationale for each choice.
>
> Calibrate to a PGY-2 — appropriate complexity, no esoteric distractors. Use SI units. Do not use any patient names or institutional identifiers.

*Annotation: the prompt is doing several things right — naming the level explicitly, naming the cognitive challenge (ambiguity), specifying length, specifying calibration. What it's NOT doing well: it doesn't ask the model to identify the discriminating feature that makes the case ambiguous, or to suggest a teaching beat for the discussion. The faculty member learned to add these in subsequent uses.*

## AI-generated draft (Claude Opus 4.7)

### Vignette

> A 58-year-old patient receiving the second unit of packed red blood cells for symptomatic anemia develops a temperature rise from 37.0°C to 38.5°C approximately 45 minutes into the transfusion. The patient reports mild chills but no back pain. Blood pressure is 118/76 mmHg, heart rate is 92 bpm, oxygen saturation is 98% on room air. The transfusion is paused.

### MCQ 1 — Most likely reaction type

> A. Febrile non-hemolytic transfusion reaction *(correct)*
> B. Acute hemolytic transfusion reaction
> C. TRALI
> D. Allergic reaction
>
> Rationale A: Fever ≥1°C above baseline without hemodynamic instability, hypoxia, or back pain is most consistent with FNHTR.
> Rationale B: Acute hemolytic reactions classically present with fever AND hypotension, back pain, hemoglobinuria.
> Rationale C: TRALI presents within 6 hours of transfusion with hypoxia and bilateral pulmonary infiltrates.
> Rationale D: Allergic reactions present with urticaria, pruritus, and in severe cases bronchospasm.

### MCQ 2 — Next best step

> A. Restart transfusion at slower rate
> B. Administer epinephrine
> C. Send patient and unit samples to blood bank for workup *(correct)*
> D. Premedicate with diphenhydramine and restart
>
> *[rationales follow]*

### MCQ 3 — Mechanism

> A. Recipient antibodies against donor leukocyte HLA antigens *(correct)*
> B. ABO incompatibility with intravascular hemolysis
> C. Donor antibodies against recipient HLA antigens in the lung
> D. IgE-mediated mast cell degranulation
>
> *[rationales follow]*

## Faculty edits — annotated

### Vignette edits

The faculty member made three substantive changes:

1. *Original: "approximately 45 minutes into the transfusion."*
   **Edited to: "approximately 25 minutes into the transfusion."**
   *Reason: 45 minutes makes the case too easy — it sits comfortably in FNHTR territory. 25 minutes is in the overlap window where both FNHTR and an early acute hemolytic reaction are reasonable. The point of the case is to BE ambiguous; the model produced an unambiguous case.*

2. *Original: "but no back pain."*
   **Edited to: "no back pain reported. Patient is sedated for end-stage liver disease and unable to give a reliable subjective history."**
   *Reason: removing the patient's ability to self-report ambiguates the case appropriately. This forces the resident to rely on the objective findings — which is the actual clinical situation residents face. The model's case was too clean.*

3. *Original: "blood pressure is 118/76 mmHg"*
   **Edited to: "blood pressure is 102/68 mmHg (was 124/76 mmHg pre-transfusion)."**
   *Reason: a borderline drop is exactly the kind of finding that distinguishes a teachable vignette from a giveaway. The resident has to decide whether a 14-point drop matters in this context.*

### MCQ 1 edits

After the vignette edits, the faculty member **flipped the correct answer** to "acute hemolytic transfusion reaction" and rewrote the rationales to emphasize:

- The "1°C above baseline" criterion alone is **necessary but not sufficient** for FNHTR
- A blood pressure drop, even a small one, in a patient who can't self-report **forces the workup**
- The discriminating principle: *when in doubt, treat as the worse possibility until disproven*

*Annotation: this is the highest-value edit in the entire example. The model's vignette and MCQ were internally consistent (FNHTR) but pedagogically wrong (too easy). The faculty member changed both together to preserve internal consistency while shifting the cognitive challenge.*

### MCQ 2 edits

The faculty member kept the MCQ structure but added a discussion note for the facilitator:

> Even residents who correctly pick C ("send to blood bank") often skip the **most time-sensitive step BEFORE that**: maintain IV access with normal saline (NOT the blood bag's tubing — change it) and send a urinalysis for free hemoglobin. Use this as a teaching moment about prioritization, not just identification.

*Annotation: the model produced a question with one correct answer. The faculty member added a layer the model didn't think to add — what experienced clinicians do before sending the workup. This is the kind of judgment-derived content the model cannot generate.*

### MCQ 3 — distractor revision

The faculty member kept this MCQ largely as drafted but revised one distractor:

> Replace D ("IgE-mediated mast cell degranulation") with "**Cytokine release from donor leukocytes accumulated during storage**".
>
> This is a much more dangerous distractor because it's actually a *contributing mechanism* to FNHTR — it lets you ask a follow-up question about why leukoreduction reduces FNHTR risk, even though the primary mechanism in the chosen scenario is now acute hemolytic.

*Annotation: an obvious throwaway distractor (D-original) gives residents a free elimination. A plausibly-related distractor (D-revised) requires thought and opens a path to a deeper teaching moment.*

## Final teaching-ready output

After ~20 minutes of editing, the faculty member had:

- A vignette that requires the resident to integrate three pieces of evidence (timing, BP drop, inability to self-report)
- Three MCQs that progress from recognition → action → mechanism
- A facilitator note that surfaces a common cognitive shortcut (jumping to workup without IV access and free-hemoglobin urinalysis)
- One distractor revision that opens a path to a follow-up question on leukoreduction

**Time saved vs starting from scratch: ~30 minutes.** Time spent editing: ~20 minutes. **Net: ~10 minutes saved, plus a more pedagogically deliberate session** than the faculty member would have built under time pressure.

## What this example does NOT show

- This is not a session designed for a board exam. The MCQs are pedagogical; they would not necessarily pass psychometric review.
- The model did not generate the *teaching judgment* — when to make a case ambiguous, when to keep a distractor mild, when to add a facilitator note. That came from the faculty member.
- A separate review pass for **demographic representation** (age, sex, race) across a series of cases is needed at the course level, not the single-case level. See [Guardrails](library.html#/docs/guardrails).
- The faculty member knew transfusion reactions cold. **If you don't know the topic deeply, the model's first draft will fool you.** This pattern is most useful for topics within your active expertise.

## How to use this pattern

For your own teaching session design:

1. **Draft the prompt** using the [Case vignette at PGY level](library.html#/library/pillar-2-teaching/prompts/case-vignette-pgy) prompt as a template
2. **Generate** — but read the output as a STARTING SCAFFOLD, not a finished session
3. **Pressure-test for ambiguity** — is the case too easy? Too hard? Right shape?
4. **Edit the vignette FIRST**, then re-align the MCQs to match
5. **Add facilitator notes** that capture judgment the model can't generate
6. **Pressure-test with a co-faculty** colleague before delivery

## Related prompts

- [Case vignette at PGY level](library.html#/library/pillar-2-teaching/prompts/case-vignette-pgy)
- [Matched case pair — reactive vs neoplastic](library.html#/library/pillar-2-teaching/prompts/matched-case-pair)
- [Bloom's taxonomy MCQ generation](library.html#/library/pillar-2-teaching/prompts/blooms-mcq)
- [Guardrails](library.html#/docs/guardrails)
