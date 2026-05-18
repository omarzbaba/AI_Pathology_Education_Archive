---
title: Adapting prompts to your subspecialty — making the library yours
last_updated: 2026-05-18
difficulty: intermediate
category: practice
---

The library is opinionated. It was built by a heme-path / CP-leaning clinical pathologist and the prompts default to that orientation: SPEP traces, blood smears, transfusion workflows, board-prep aimed at the CP boards. A dermpath, peds path, neuropath, forensic, or cytopath user will read those prompts and reasonably ask: *do I just use them as-is, or do I need to adapt them?*

The answer is: **adapt them, every time, in four specific places.** This guide is the working manual for doing that — with four worked rewrites that show the pattern.

---

## Part 1 — Why adapt rather than swap

You might assume the right move is to find or build a separate prompt library for your subspecialty. In some cases, eventually, you will. But for now:

**Most prompts in this library are about the *cognitive task*, not the *content*.** A "concept explanation at level" prompt has a structure (three layers, calibrated to PGY-2, follow-up question to check understanding) that is identical across heme path, dermpath, and forensic. The content slot changes; the scaffold doesn't.

**The library scaffold is a teachable skill.** Once you know how to adapt a heme-path prompt to dermpath, you can adapt any heme-path prompt to dermpath. That generalizes. Building a separate library from scratch doesn't.

**Adaptation produces better prompts than building from a blank page.** The library prompts have been refined through dozens of iterations. They've absorbed lessons about failure modes, format constraints, calibration. Your dermpath rewrite starts ahead of where you'd start cold.

---

## Part 2 — The four edit points

Every prompt in the library can be adapted by editing these four things. They cluster predictably.

### Edit point 1 — Audience level and calibration

The library defaults to PGY-2/3 clinical pathology. If your context is different, change the calibration string explicitly:

- *"PGY-2 in their first month of blood bank"* → *"dermpath fellow three months into the year"*
- *"resident on heme path service"* → *"PGY-3 on forensic autopsy service"*
- *"attending hematopathologist"* → *"pediatric soft tissue tumor specialist"*

This is the highest-leverage single change. Without it, output reads as off-target — the right cognitive structure, the wrong calibration.

### Edit point 2 — Subspecialty vocabulary

The library uses heme-path / CP vocabulary: "smear," "panel," "trace," "differential by morphologic features." A dermpath prompt should use *dermpath* vocabulary: "specimen," "biopsy," "histologic features," "differential by architectural pattern." A peds path prompt should use *peds path* vocabulary: "germinal matrix," "biphenotypic," "small round blue cell tumor."

The model will follow whatever vocabulary you use in the prompt. If you use heme vocabulary asking a dermpath question, the response will subtly inherit heme conventions. Use the vocabulary your subspecialty actually uses.

### Edit point 3 — Institutional and clinical context

The library defaults to "academic medical center with a large transfusion service." Replace with your context:

- A community hospital dermpath group sees different presentations than a dedicated dermpath center
- A forensic medical examiner's office has different workflows than a hospital autopsy service
- A pediatric tertiary center sees different rare entities than a general hospital

The more specific your context, the more useful the output. *"At our 200-bed community hospital, the dermpath service signs out ~50 cases/day, most from outpatient dermatology"* anchors the model far better than *"a hospital dermpath service."*

### Edit point 4 — Constraints, units, and conventions

Subspecialty-specific conventions matter. State them:

- **Forensic:** state your jurisdiction's reporting requirements explicitly
- **Cytopath:** state the classification system (Bethesda, Milan, Paris) you're working in
- **Peds:** state the relevant pediatric staging system (e.g., Children's Oncology Group risk stratification)
- **Dermpath:** state the dermatopathology nomenclature convention (e.g., AJCC for melanoma, NCCN for cutaneous lymphoma)
- **Heme:** state which classification (current WHO edition, ICC) and which guideline body (IMWG, NCCN, ASH)

Without these, the model defaults to whatever's most-common-in-training-data, which may not be what your subspecialty uses.

---

## Part 3 — Worked rewrite 1: concept explanation for dermpath

**Original** (library, heme-CP framing):

> Act as a senior hematopathologist explaining a concept to a PGY-2 in their first month of blood bank. Explain [concept] in three layers: (1) one-sentence version a first-year resident would understand; (2) mechanistic explanation a PGY-2 should know after a month of blood bank; (3) nuanced detail distinguishing a strong fellow. After the three layers, ask me one follow-up question that targets the most likely misunderstanding at this level.

**Adapted for dermpath:**

> Act as a senior dermatopathologist explaining a concept to a dermpath fellow three months into their fellowship year. Explain [concept] in three layers: (1) the one-sentence version a clinical dermatology resident would understand; (2) the histologic explanation a dermpath fellow should be solid on by month three; (3) the nuanced morphologic or molecular detail that distinguishes a fellow ready to sign out solo. After the three layers, ask me one follow-up question that targets the most likely misunderstanding at the dermpath-fellow level — focus on architectural or cytologic features, not on clinical management.

**Notes on what changed:**

- Role: hematopathologist → dermatopathologist
- Audience: PGY-2 in blood bank → dermpath fellow at month 3
- Calibration anchors: "first month of blood bank" → "three months into fellowship"
- Audience for layer 1: first-year resident → clinical dermatology resident (matches the consult flow)
- Layer 3 anchor: "strong fellow" → "fellow ready to sign out solo" (more concrete in dermpath context)
- Follow-up scope: explicitly constrained to morphology/molecular, away from clinical management (dermpath fellows aren't running treatment)

---

## Part 4 — Worked rewrite 2: case vignette for peds path

**Original** (library, generic teaching framing):

> Generate a case vignette suitable for a PGY-3 on a teaching service. Include: chief complaint, basic history, key labs, peripheral smear description, immunophenotype, relevant cytogenetics. Calibrate to a resident who has seen ~10 cases of this entity. Make the presentation classic but not trivial. ~250 words.

**Adapted for peds path:**

> Generate a case vignette suitable for a pediatric pathology fellow on the soft tissue tumor service. Include: clinical presentation (age, anatomic site, duration, any associated symptoms), imaging findings (CT/MRI description), gross description, histologic features (architectural pattern, cytologic features, mitotic activity), relevant IHC panel results, and molecular findings (e.g., FISH for known fusions, NGS panel summary if relevant). Calibrate to a fellow who has rotated through soft tissue for two weeks. Make the presentation a reasonably common pediatric small round blue cell tumor — not the rarest entity but not the most obvious either. Note the patient's age explicitly (this is pediatric — be precise about age range) and any features that would change the differential (e.g., metaphysis vs diaphysis, deep vs superficial soft tissue). ~300 words.

**Notes on what changed:**

- Audience: PGY-3 on teaching service → pediatric pathology fellow on soft tissue service (specific subspecialty rotation)
- Components requested: heme-path components (smear, immunophenotype, cytogenetics) → peds soft tissue components (clinical + imaging + gross + histology + IHC + molecular)
- Calibration: "10 cases of this entity" → "rotated through soft tissue for two weeks" (rotation-time calibration is more honest for peds where case volume varies hugely)
- Difficulty framing: "classic but not trivial" → "common pediatric small round blue cell tumor — not rarest, not most obvious" (this is the peds-specific differential framing)
- Explicit anchors: age precision, anatomic detail — both are critical for peds soft tissue differentials in ways they aren't for heme
- Word count: bumped up to reflect the more component-rich vignette

---

## Part 5 — Worked rewrite 3: differential by histologic pattern for forensic

**Original** (library):

> I'll describe a histologic pattern. Generate a differential of 4–6 entities, ranked by likelihood given the description. For each entity, give one sentence on why it's in the differential and one sentence on what additional finding would help confirm or exclude it. Then ask me which entity I favor and why.

**Adapted for forensic pathology:**

> I'll describe a histologic finding from an autopsy case. Context: medical examiner's office, decedent presented as a death in custody. Generate a differential of 4–6 cause-of-death mechanisms or contributory findings that are consistent with the histologic finding I describe. For each:
>
> 1. One sentence on why it's in the differential
> 2. One sentence on what additional ancillary testing (toxicology, microbiology, postmortem CT, etc.) would help confirm or exclude
> 3. One sentence on how this finding would be characterized in the autopsy report (anatomic vs immediate cause vs contributory)
>
> Rank by likelihood. After the differential, ask me which mechanism I favor, why, and what other organ systems I want to examine next.

**Notes on what changed:**

- Context: generic histology → autopsy / forensic with explicit case context (death in custody — this changes the differential calculus enormously)
- "Differential" reframed: entities → cause-of-death mechanisms / contributory findings (forensic framing is mechanistic, not just diagnostic)
- Ancillary testing slot: changed from "additional finding to confirm/exclude" to specifically forensic ancillary tests (tox, postmortem CT, micro)
- Added a third slot on report characterization (anatomic / immediate / contributory cause) — central to forensic reasoning, irrelevant to surgical pathology
- Final question reframed: "what next entity to investigate" → "what other organ systems to examine" (matches how autopsy actually unfolds)

This rewrite is more aggressive than the dermpath one because forensic pathology has a fundamentally different cognitive structure from surgical pathology. The library scaffold (describe → differential → confirm) still works, but the slots get re-filled.

---

## Part 6 — Worked rewrite 4: sign-out teaching turn for cytopath

**Original** (library):

> Help me prepare a 5–8 minute teaching turn for sign-out. I'll describe a case. Generate:
> 1. The teaching point (one sentence — what's the takeaway?)
> 2. The setup: how to introduce the case in 60 seconds without giving away the diagnosis
> 3. Two discussion questions to ask the residents at the scope, in escalating difficulty
> 4. The "common misread" to call out explicitly
> 5. A follow-up reading or reference for residents who want to go deeper

**Adapted for cytopath:**

> Help me prepare a 5–8 minute teaching turn for the cytopathology multi-headed scope. I'll describe a case (FNA or fluid cytology). Generate:
>
> 1. The teaching point (one sentence — what's the takeaway? Focus on the diagnostic feature or the differential trap, not the clinical management)
> 2. The setup: how to introduce the case in 60 seconds without giving away the diagnosis. Note the specimen type and the relevant clinical/radiologic context but withhold the cell block findings.
> 3. Two scope-side discussion questions for the cytopath fellow and the rotating cytotech students, in escalating difficulty. First question on smear / liquid-based preparation cellularity and architecture; second on individual cell features (nuclear features, N:C ratio, chromatin pattern).
> 4. The "common misread" to call out explicitly — particularly any Bethesda / Milan / Paris category that this case might be mis-assigned to.
> 5. A follow-up reading or reference. Prefer the most recent edition of the relevant classification system (Bethesda for thyroid FNA, Milan for salivary, Paris for urine, etc.) or a high-yield review article.

**Notes on what changed:**

- Anchor changed: generic sign-out → cytopath multi-headed scope (different physical setup, different participants)
- Specimen type explicitly added: FNA or fluid (cytopath universal context)
- Setup constraint: withhold cell block findings (cell block is often the diagnostic ace in cytopath — withholding it during the teaching moment is standard)
- Discussion questions: escalation pattern made cytopath-specific (preparation/architecture → individual cell features) rather than generic
- Misread call-out: anchored to the classification system in use (Bethesda / Milan / Paris)
- Reading recommendation: explicitly biased toward the relevant classification system (more useful for cytopath than generic review articles)

---

## Part 7 — The pattern

If you study the four rewrites above, the pattern is consistent:

1. **The cognitive scaffold doesn't change.** The structure of "three layers of explanation," or "differential with confirmation steps," or "5-minute teaching turn with discussion questions" is portable across subspecialties.

2. **The slots get re-filled with subspecialty content.** Vocabulary, audience, conventions, classification systems, ancillary tests — these are the things that change.

3. **The calibration anchors change to match how time-on-rotation actually works in your specialty.** Heme path measures in "weeks of blood bank"; peds soft tissue measures in "weeks of soft tissue rotation"; forensic measures in "cases of [type]"; cytopath measures in "fellowship months."

4. **Subspecialty-specific conventions get stated explicitly** that wouldn't need to be stated in the original.

Once you've adapted three or four prompts following this pattern, you'll find the next ones come fast. The first adaptation is the slow one; subsequent adaptations are mostly find-and-replace plus a few targeted additions.

---

## Part 8 — When to keep the original instead of adapting

A few cases where adaptation is unnecessary:

- **Pillar III operations prompts** (rotation orientation, evaluation rubrics, workshop run-of-show) are often subspecialty-agnostic. The orientation packet for a CP rotation and the orientation packet for a dermpath rotation share more than they differ.
- **Pure format prompts** (slide outline, syllabus, abstract) are subspecialty-agnostic. The format is the value.
- **Generic chains** (concept-explanation followed by self-quiz) port across subspecialties with minimal adaptation if the topic content is what you'd be plugging in anyway.

The prompts that always need adaptation are the ones with embedded subspecialty content: smear descriptions, immunophenotype assumptions, classification systems, ancillary test panels, specific guideline citations.

---

## Part 9 — Contributing your rewrites back

If you've done a careful subspecialty adaptation of a prompt, that's valuable. Use the [Submit a prompt](submit.html) form to add your version to the library — credited to you. Over time, the library will accumulate a parallel set of subspecialty-specific variants alongside the heme-CP defaults, and users will be able to pick the variant closest to their context.

The library is meant to grow this way. Your dermpath rewrite of "concept-explanation at level" is potentially useful to every dermpath user who comes after you. Submit it.

---

## Part 10 — Practical workflow for adaptation

Your first time adapting:

1. **Pick a single library prompt** that addresses a task you actually do in your subspecialty.
2. **Identify the four edit points** in that prompt: audience level, vocabulary, institutional/clinical context, conventions/units.
3. **Edit each one** with your subspecialty's equivalent.
4. **Run the adapted prompt** in a session. Read the response. Note what's still off.
5. **Re-edit.** Usually you'll catch one or two anchors you missed.
6. **Run again.** Output should now feel native to your subspecialty.
7. **Save the adapted version** as a template (a `.md` file in your own notes, or pasted into a Claude Project).
8. **Submit it back** to the library if it's substantially better than the original for your subspecialty.

Total time for the first adaptation: ~20 minutes. Total time for the tenth: ~3 minutes. The skill compounds quickly once you've internalized the pattern.
