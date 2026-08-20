---
title: Flagship walkthrough — From empty calendar slot to a taught session
pillar: teaching
event_type: didactic session
audience: faculty
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: clinical-chemistry, immunoassay-interference, session-design, mcq, osce, worked-example, flagship
verified_models: Claude Sonnet 4.6
best_model: Claude Sonnet 4.6
last_updated: 2026-08-20
---

## Start here

This is the **poster-child case for Pillar II**. One faculty member, one empty hour on the residency
calendar, one week's notice — and **eight prompts from this pillar in sequence**, ending in material
you could teach from tomorrow.

**The situation.** Dr. Reyes has been asked to fill a one-hour PGY-2 didactic slot on
**immunoassay interference** in clinical chemistry. She knows the content cold from the bench. What
she does not have is a session: no objectives, no cases, no assessment, no slides, and about ninety
minutes of protected time to build all of it.

**What she ends with.** Three milestone-mapped objectives, a paired teaching case, a six-item quiz she
has personally audited, an OSCE-style station with a scoring checklist, a slide skeleton, and
facilitator notes — plus one confidently-wrong model claim she caught before it reached a learner.

<ul class="flagship__meta">
<li>90 minutes of prep</li>
<li>8 prompts chained</li>
<li>Faculty &middot; clinical chemistry</li>
<li>1 model error caught</li>
</ul>

---

## Frame the session

<details class="step">
<summary>Step 1 &middot; Objectives that map to something, not vibes</summary>
<div class="step__body">
<p class="step__card">Card used: <a href="library.html#/library/pillar-2-teaching/prompts/acgme-epa-objectives">ACGME / EPA-mapped objectives</a></p>

> Write three learning objectives for a one-hour PGY-2 session on immunoassay interference in clinical
> chemistry. Each must be observable and assessable in that hour — no "understand" or "appreciate."
> For each, propose the most relevant ACGME pathology milestone and mark your confidence.
> Flag any objective you cannot confidently map.

<div class="note">The confidence flag is doing real work. It converts a mapping the model would
otherwise assert into a proposal Dr. Reyes reviews — and it surfaced one objective the model itself
could not place, which turned out to be the one worth cutting for time.</div>

<div class="verify"><strong>Verify:</strong> milestone language is program- and version-specific.
Check every proposed mapping against your own program's current milestone document before it goes on
a syllabus. Do not let the model quote milestone text back to you as authoritative.</div>
</div>
</details>

---

## Build the teaching material

<details class="step">
<summary>Step 2 &middot; A case with the trap built in</summary>
<div class="step__body">
<p class="step__card">Card used: <a href="library.html#/library/pillar-2-teaching/prompts/case-vignette-pgy">Case vignette at PGY level</a></p>

> Build a PGY-2 teaching case on immunoassay interference. A young woman with a suppressed TSH and an
> elevated free T4 whose clinical picture does not fit Graves disease. Give history, the initial
> results, and the sequence of results as the workup proceeds. Keep every value internally consistent.
> Label it explicitly as hypothetical and de-identified. Do not reveal the mechanism — the case should
> make the resident ask for the right next test.

<div class="note">"Do not reveal the mechanism" is the difference between a case and a worked example.
Left unconstrained, models write the answer into the stem.</div>
</div>
</details>

<details class="step">
<summary>Step 3 &middot; The contrast case that forces discrimination</summary>
<div class="step__body">
<p class="step__card">Card used: <a href="library.html#/library/pillar-2-teaching/prompts/matched-case-pair">Matched case pair</a></p>

> Now write a matched second case with a nearly identical presentation but a different interference
> mechanism, so residents must discriminate rather than pattern-match. Tell me which single finding
> separates them and at what point in the workup it becomes available.

<div class="note">A single case teaches recognition. A matched pair teaches discrimination — the thing
that actually transfers to the bench. This is the highest-leverage prompt in the whole session build.</div>
</div>
</details>

<details class="step">
<summary>Step 4 &middot; Where the model gets it wrong</summary>
<div class="step__body">
<p class="step__card">Card used: <a href="library.html#/library/pillar-2-teaching/prompts/blooms-mcq">Bloom's-level MCQs</a></p>

> Write six single-best-answer questions at application level on immunoassay interference — hook effect,
> biotin, heterophile antibody, macroanalyte. Give the key and a one-line rationale for why each
> distractor is wrong. Do not write any item where more than one option could be defended.

> **Model:** …Item 3. A patient taking high-dose biotin has a **falsely elevated** TSH on a
> sandwich immunoassay…

<div class="caught"><strong>The error.</strong> That is backwards, and it is the single most commonly
confused point in the topic. In a <em>sandwich</em> (immunometric) assay, biotin interference produces
a falsely <em>low</em> result; the falsely <em>high</em> result occurs in <em>competitive</em> assays.
That inversion is exactly what produces the classic biotin picture of a low TSH with a high free T4
mimicking Graves — which is the presentation in the case Dr. Reyes had just built two steps earlier.
Had it shipped, the quiz would have contradicted the teaching case, and taught the misconception the
session exists to correct.</div>

<div class="note">She caught it because the item disagreed with her own case. That internal
contradiction is a useful audit trick: build the case before the questions, then read the questions
<em>against</em> the case rather than on their own.</div>

<div class="verify"><strong>Verify:</strong> answer every generated item yourself before reading the
key, and resolve disagreements against a primary source. Two of the six items here also had a second
defensible answer despite the instruction not to write one. Generated items are a drafting aid; they
are not a question bank until a human has audited every key and every rationale.</div>
</div>
</details>

<details class="step">
<summary>Step 5 &middot; A station that tests the reasoning, not the recall</summary>
<div class="step__body">
<p class="step__card">Card used: <a href="library.html#/library/pillar-2-teaching/prompts/osce-station">OSCE-style station</a></p>

> Convert the first case into a 7-minute OSCE-style station: candidate instructions, examiner
> instructions, and a scoring checklist. The checklist must reward the reasoning steps — recognizing
> the discrepancy, naming the mechanism, choosing the confirmatory test — not keyword recall.

<div class="verify"><strong>Verify:</strong> read the checklist and ask whether a resident who reasoned
correctly but used different words would still score. If not, the checklist is testing vocabulary.</div>
</div>
</details>

---

## Package and deliver

<details class="step">
<summary>Step 6 &middot; Slide skeleton, built around the arc</summary>
<div class="step__body">
<p class="step__card">Card used: <a href="library.html#/library/pillar-2-teaching/prompts/slide-outline-1hr">One-hour slide outline</a></p>

> Draft a slide outline for the hour using a problem → mechanism → discrimination → practice arc.
> Cases first, mechanism second. Mark where the two cases, the six questions and the station belong.
> Titles and bullet skeletons only — I will build the slides and supply all figures myself.

<div class="note">"I will supply all figures myself" is not incidental. AI-generated histology,
gel images or instrument traces have no place in teaching material — a synthetic image can instil
morphology or a pattern that does not exist.</div>
</div>
</details>

<details class="step">
<summary>Step 7 &middot; Notes that survive teaching it at 7 a.m.</summary>
<div class="step__body">
<p class="step__card">Card used: <a href="library.html#/library/pillar-2-teaching/prompts/speaker-notes">Speaker notes</a></p>

> Write facilitator notes for each slide: the point to make, the question to ask the room, the wrong
> answer residents most commonly give, and how to redirect it. Two to three sentences per slide.

<div class="note">The "most common wrong answer" field is what turns notes into teaching. It is also
the field to check hardest — the model is inferring what learners get wrong, and your own experience
of what this specific group gets wrong is better evidence.</div>
</div>
</details>

<details class="step">
<summary>Step 8 &middot; Screen it before it reaches a learner</summary>
<div class="step__body">
<p class="step__card">Card used: <a href="library.html#/library/pillar-2-teaching/prompts/audience-polls">Audience polls</a></p>

> Give me two polling questions to open and close the session, designed to expose the biotin
> misconception specifically. Then review both cases and all six items and tell me where demographic
> detail is doing no teaching work, or where a default assumption about age, sex or resource setting
> has crept in.

<div class="caught"><strong>Worth doing every time.</strong> Both original vignettes defaulted to
young women, which the thyroid presentation makes plausible but which also quietly teaches a
demographic association the mechanism does not have. One case was switched. Generated cases inherit
whatever associations sit in the training data; if you do not screen for it, you teach it.</div>
</div>
</details>

---

## Now do it yourself

Substitute your own topic and run the same eight steps:

1. **Objectives** — observable, assessable, mapped, with confidence flagged
2. **Case** — mechanism withheld
3. **Matched pair** — force discrimination
4. **Items** — then audit every key against your own case
5. **Station** — score the reasoning
6. **Slide outline** — your figures, always
7. **Facilitator notes** — including the common wrong answer
8. **Poll + bias screen** — before anyone sees it

**The rule for this pillar.** Everything above is a draft until a content expert signs it. The model
shortened ninety minutes of building into thirty; it did not shorten the reviewing, and the one place
Dr. Reyes might have skipped review is precisely where it was wrong.
