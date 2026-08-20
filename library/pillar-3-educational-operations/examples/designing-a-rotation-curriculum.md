---
title: Flagship walkthrough — Designing a resident's rotation curriculum
pillar: educational-operations
event_type: rotation
audience: faculty
difficulty: advanced
time_to_use: >10min
visual: text-only
tags: transfusion-medicine, coagulation, curriculum-design, rotation, milestones, worked-example, flagship
verified_models: Claude Sonnet 4.6
best_model: Claude Sonnet 4.6
last_updated: 2026-08-20
---

## Start here

This is the **poster-child case for Pillar III**, and it is deliberately the widest of the three.
Pillar II builds one teaching hour. This builds **the path a resident travels for four weeks** — and
in doing so it orchestrates the other two pillars rather than replacing them.

**The situation.** Dr. Okafor has just been made rotation director for the four-week transfusion
medicine and coagulation rotation. What exists is a folder of slides from three previous directors,
no written curriculum, no assessment plan, and a PGY-2 starting in eighteen days.

**What she ends with.** A milestone-mapped rotation blueprint, a week-by-week sequence, an orientation
packet, a verified reading list, an assessment scheme, an evaluation instrument, and a sign-off
checklist — plus a fabricated requirement she caught before it became programme policy.

<ul class="flagship__meta">
<li>18 days &middot; ~6 h of design</li>
<li>8 steps, 3 pillars used</li>
<li>Faculty &middot; rotation director</li>
<li>1 fabricated requirement caught</li>
</ul>

<div class="note">Note how often this walkthrough hands off to Pillar II. That is the point: operations
work is mostly deciding <em>what</em> gets taught, <em>when</em>, and <em>how it is assessed</em> —
then delegating the building of each session to the teaching pillar.</div>

---

## Decide what the rotation is for

<details class="step">
<summary>Step 1 &middot; Scope it against what a PGY-2 must actually be able to do</summary>
<div class="step__body">
<p class="step__card">Card used: <a href="library.html#/library/pillar-3-educational-operations/prompts/rotations/expectations-doc">Rotation expectations document</a></p>

> I'm designing a four-week transfusion medicine and coagulation rotation for a PGY-2 in an academic
> hospital with a level-1 trauma centre, an apheresis service and a special coagulation lab. Help me
> decide scope: what must a PGY-2 be independently entrustable for by the end, what should they merely
> be exposed to, and what is genuinely out of scope for four weeks? Push back on anything I'm likely
> to over-scope.

<div class="note">"Push back on anything I'm likely to over-scope" is the highest-value clause in this
whole walkthrough. First-time rotation directors reliably build a fellowship curriculum and hand it to
a second-year resident. The model's pushback on molecular coagulopathy workup was correct and saved a
week of the schedule.</div>

<div class="verify"><strong>Verify:</strong> the model does not know your service volumes, your call
structure, or which attendings actually cover which days. Every scope decision it proposes is a
hypothesis about your institution that only you can confirm.</div>
</div>
</details>

<details class="step">
<summary>Step 2 &middot; Map to milestones — and the fabrication that nearly shipped</summary>
<div class="step__body">
<p class="step__card">Cards used: <a href="library.html#/library/pillar-3-educational-operations/prompts/rotations/evaluation-rubric">Evaluation rubric</a> &middot; <a href="library.html#/library/pillar-2-teaching/prompts/acgme-epa-objectives">ACGME / EPA-mapped objectives</a> <em>(Pillar II)</em></p>

> Map each entrustable outcome to the most relevant ACGME pathology milestone, and tell me the minimum
> evidence that would justify signing it off.

> **Model:** …this maps to the milestone requiring **a minimum of 20 documented apheresis procedures
> before sign-off**…

<div class="caught"><strong>The error, and why this one is dangerous.</strong> No such numeric
requirement exists. The model produced a plausible, specific, policy-shaped number — the format of a
real requirement, with none of the substance. Unlike a wrong marker on a quiz, a fabricated
requirement of this kind does not get caught by a learner. It gets written into a syllabus, quoted to
residents, and cited in a programme review, because it looks exactly like the thing it is imitating.
</div>

<div class="note">Dr. Okafor caught it because she had read the milestones that month and knew they
are written as narrative behavioural descriptors, not procedure counts. Anyone less recently steeped
in the document would plausibly have accepted it.</div>

<div class="verify"><strong>Verify:</strong> never let a model tell you what an accrediting body
requires. Open the current milestone document and the programme requirements yourself and quote from
them. Treat any specific number, threshold or deadline the model produces about accreditation as
false until you have seen it in the source.</div>
</div>
</details>

---

## Lay out the four weeks

<details class="step">
<summary>Step 3 &middot; Sequence so each week earns the next</summary>
<div class="step__body">
<p class="step__card">Card used: <a href="library.html#/library/pillar-3-educational-operations/prompts/rotations/rotation-block-scheduling">Rotation block scheduling</a></p>

> Sequence the four weeks so each builds on the last: component therapy and compatibility first,
> then massive transfusion and emergency release, then apheresis, then coagulopathy workup. For each
> week give the bench time, the expected independent activity, and the one concept that must be solid
> before the following week makes sense.

<div class="note">The last clause creates the dependency chain. Without it you get four self-contained
weeks in arbitrary order — which is what most inherited rotations already are.</div>
</div>
</details>

<details class="step">
<summary>Step 4 &middot; Orientation the resident reads on day one</summary>
<div class="step__body">
<p class="step__card">Card used: <a href="library.html#/library/pillar-3-educational-operations/prompts/rotations/orientation-onepager">Orientation one-pager</a> &middot; see also the <a href="library.html#/library/pillar-3-educational-operations/examples/coag-rotation-orientation">coagulation orientation example</a></p>

> Turn the blueprint into a two-page orientation packet: what the rotation is for, the weekly shape,
> who to contact, what to read before day one, how they'll be assessed, and what "doing well" looks
> like. Plain language, addressed to the resident.

<div class="verify"><strong>Verify:</strong> every contact name, pager, room, and start time is
institutional fact the model cannot know. Fill those yourself; do not let it guess a placeholder that
looks like a real extension.</div>
</div>
</details>

<details class="step">
<summary>Step 5 &middot; A reading list you have actually opened</summary>
<div class="step__body">
<p class="step__card">Card used: <a href="library.html#/library/pillar-3-educational-operations/prompts/rotations/reading-list">Rotation reading list</a></p>

> Propose a reading list of at most eight items, weighted to the first two weeks. For each, tell me
> what question it answers and roughly how long it takes. Suggest search terms and source types rather
> than specific citations — I will locate and verify each one myself.

<div class="caught"><strong>Ask for search terms, not citations.</strong> Requesting a reading list by
citation is the single most reliable way to receive fabricated references — plausible authors,
plausible journals, plausible years, no such paper. Asking instead for the <em>question</em> each
reading should answer keeps the model doing the part it is good at and leaves retrieval where it
belongs, with you and the databases.</div>
</div>
</details>

---

## Decide how you will know it worked

<details class="step">
<summary>Step 6 &middot; Assessment that matches the entrustment claim</summary>
<div class="step__body">
<p class="step__card">Cards used: <a href="library.html#/library/pillar-3-educational-operations/prompts/rotations/evaluation-rubric">Evaluation rubric</a> &middot; <a href="library.html#/library/pillar-2-teaching/prompts/blooms-mcq">Bloom's-level MCQs</a> &middot; <a href="library.html#/library/pillar-2-teaching/prompts/osce-station">OSCE-style station</a> <em>(last two from Pillar II)</em></p>

> For each entrustable outcome, propose the lightest assessment that would actually justify signing it
> off — knowledge check, observed encounter, or direct observation with a checklist. Tell me where I'm
> proposing to assess something I have no realistic way to observe in four weeks.

<div class="note">This is where curriculum design stops being a document and becomes honest. Two of the
original outcomes could not be observed in four weeks on this service, and were rewritten as exposure
rather than entrustment.</div>
</div>
</details>

<details class="step">
<summary>Step 7 &middot; Feedback that is specific enough to act on</summary>
<div class="step__body">
<p class="step__card">Cards used: <a href="library.html#/library/pillar-3-educational-operations/prompts/rotations/mid-rotation-feedback">Mid-rotation feedback</a> &middot; <a href="library.html#/library/pillar-3-educational-operations/prompts/rotations/end-of-rotation-evaluation">End-of-rotation evaluation</a> &middot; <a href="library.html#/library/pillar-2-teaching/prompts/ccc-narrative-comment">CCC narrative comment</a> <em>(Pillar II)</em></p>

> Draft a mid-rotation feedback template and an end-of-rotation evaluation form keyed to the outcomes
> above. Each item must describe an observable behaviour at a stated level, not a Likert adjective.

<div class="verify"><strong>Verify:</strong> no real resident's performance, name, or identifying
detail goes into a model. Build the instrument with the model; fill it in yourself, offline.</div>
</div>
</details>

<details class="step">
<summary>Step 8 &middot; Make it something the next director inherits</summary>
<div class="step__body">
<p class="step__card">Card used: <a href="library.html#/library/pillar-3-educational-operations/companion-app-builder/README">Companion app builder</a></p>

> Assemble everything into a single rotation handbook with a table of contents, a block checklist the
> resident can tick, and a one-page sign-off sheet for me. Structure it so a future director can revise
> one week without rebuilding the document.

<div class="note">The folder of slides Dr. Okafor inherited was unmaintainable because it had no
structure to revise. The last step of operations work is always making the artefact survive you.</div>
</div>
</details>

---

## Now do it yourself

1. **Scope** — entrustable vs exposed vs out of scope, with pushback invited
2. **Map** — to milestones you have read yourself
3. **Sequence** — each week earns the next
4. **Orient** — plain language, real contacts
5. **Read** — search terms, never citations
6. **Assess** — the lightest thing that justifies sign-off
7. **Evaluate** — observable behaviours, no PHI, no real resident data
8. **Package** — so the next director can revise it

**The rule for this pillar.** Errors here do not land on one learner in one hour — they land on every
resident who rotates through, for as long as the document survives. That asymmetry is why the
verification standard for operations material is higher than for anything you teach live, and why the
fabricated apheresis requirement in Step 2 is the most consequential error in all three walkthroughs.
