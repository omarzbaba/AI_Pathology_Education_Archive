---
title: Flagship walkthrough — Three weeks to close your weakest topic
pillar: self-education
event_type: n/a
audience: resident
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: hematopathology, flow-cytometry, cll, mantle-cell, board-prep, worked-example, flagship
verified_models: Claude Sonnet 4.6
best_model: Claude Sonnet 4.6
last_updated: 2026-08-20
---

## Start here

This is the **poster-child case for Pillar I**. It is not a single prompt — it is a three-week
self-study loop that a PGY-2 actually ran, using **eight prompts from this pillar in sequence**.
Each step below names the card it came from, so you can lift the same arc onto your own weak topic.

**The situation.** Nadia is a PGY-2 with three weeks until the in-service exam. Her practice-test
breakdown is worst in hematopathology, and within that, worst on **mature B-cell lymphoproliferative
disorders by flow immunophenotype** — specifically the CD5-positive pair, CLL/SLL versus mantle cell
lymphoma. She keeps getting them backwards under time pressure.

**What she ends with.** A 30-card Anki deck she trusts, a written discriminator table she built
herself, and one model error she caught and can now explain to someone else — which is the real
test of whether the topic is closed.

<ul class="flagship__meta">
<li>3 weeks elapsed &middot; ~4 h total</li>
<li>8 prompts, one conversation thread each week</li>
<li>PGY-2 &middot; hematopathology</li>
<li>1 model error caught</li>
</ul>

---

## Week 1 — Find the real gap, then plan

<details class="step">
<summary>Step 1 &middot; Name the gap precisely, not vaguely</summary>
<div class="step__body">
<p class="step__card">Card used: <a href="library.html#/library/pillar-1-self-education/prompts/question-bank-gap-analysis">Question bank gap analysis</a></p>

> I'm a PGY-2 three weeks out from the in-service exam. Here are my practice-test percentages by
> category [pasted]. Don't just rank them — tell me which weak areas are *high-yield and fixable in
> three weeks* versus which are low-yield or too broad to fix now. For the top area, break it into
> the specific sub-skills I'd need, and tell me which single sub-skill failure most likely explains
> the others.

> **Model:** Your hematopathology score (54%) is both the lowest and the highest-yield to attack…
> Within it, the recurring failure is not memory of individual markers but **discrimination between
> entities that share a marker** — most often CD5-positive B-cell processes. Fixing the CD5+ triage
> would likely lift several adjacent question types.

<div class="note">The value here is the reframe. Nadia's own read was "I'm bad at heme." The model
turned that into a testable sub-skill — CD5+ discrimination — which is small enough to actually close
in three weeks. A vaguer prompt ("what should I study?") returns a study plan for the whole specialty.</div>

<div class="verify"><strong>Verify:</strong> the model is reasoning from percentages you supplied,
not from knowledge of your exam. Sanity-check its "high-yield" claim against your program's blueprint
or the ABPath content outline before you commit three weeks to it.</div>
</div>
</details>

<details class="step">
<summary>Step 2 &middot; Turn the gap into a dated schedule</summary>
<div class="step__body">
<p class="step__card">Card used: <a href="library.html#/library/pillar-1-self-education/prompts/board-prep-schedule">Board prep schedule</a></p>

> Build me a three-week plan to close the CD5+ B-cell discrimination gap. I have 40 minutes on
> weekdays and 90 minutes on Sundays. Sequence it so I *learn* in week 1, *drill* in week 2, and
> *test cold* in week 3. Put spaced review of week-1 material into weeks 2 and 3.

<div class="note">Two constraints do the work: the real time budget, and the learn → drill → test-cold
structure. Without the second, models produce a flat reading list. With it, you get something shaped
like actual deliberate practice.</div>
</div>
</details>

---

## Week 1 — Build the mental model

<details class="step">
<summary>Step 3 &middot; Get the concept at your level, not the textbook's</summary>
<div class="step__body">
<p class="step__card">Card used: <a href="library.html#/library/pillar-1-self-education/prompts/concept-explanation-at-level">Concept explanation at level</a></p>

> Explain how a routine clinical flow panel triages a mature B-cell lymphoproliferative disorder.
> I'm a PGY-2 who can read a dot plot and knows the common markers, but I lose the thread when a case
> is CD5-positive. Start from what question each marker is actually answering, not from a marker list.
> Flag anything you're uncertain about.

<div class="note">"Start from what question each marker is answering" is the whole prompt. It forces
an explanation organized around reasoning rather than a table she could have read in the book — and a
table is exactly what a generic prompt returns.</div>
</div>
</details>

<details class="step">
<summary>Step 4 &middot; Force the discriminators out into the open</summary>
<div class="step__body">
<p class="step__card">Card used: <a href="library.html#/library/pillar-1-self-education/prompts/compare-contrast">Compare and contrast</a></p>

> Compare CLL/SLL and mantle cell lymphoma. Organize the answer *only* around features that actually
> discriminate them in practice — skip everything they share. For each discriminator, tell me how
> reliable it is and by what method it is assessed.

> **Model:** CD23 (positive in CLL, negative or dim in MCL), CD200 (bright in CLL, negative in MCL),
> LEF1 (positive in CLL, negative in MCL), surface immunoglobulin intensity (dim in CLL, bright in MCL),
> FMC7… and **cyclin D1, which you can add to your flow panel to confirm mantle cell.**

<div class="caught"><strong>The error — and this is the point of the whole example.</strong>
That last clause is wrong. Cyclin D1 is a <em>nuclear</em> protein; in routine clinical practice it is
assessed by immunohistochemistry on tissue or clot section, or inferred from t(11;14) by FISH — it is
not part of a standard clinical flow panel. Everything before it was correct, which is exactly what
makes it dangerous: the error is one clause deep inside an otherwise accurate answer, phrased with the
same confidence as the true statements.</div>

<div class="note">Nadia caught it because she had seen cyclin D1 reported on an IHC panel, not a flow
report, and the mismatch registered. That is the skill this pillar exists to protect — and it is the
skill you do not build if the model does the discriminating for you. She pushed back:</div>

> **Nadia:** Cyclin D1 is nuclear and I've only ever seen it on IHC or as t(11;14) by FISH. Is it
> actually run on routine clinical flow?

> **Model:** You're right, and I overstated that. Cyclin D1 is not a routine clinical flow marker…
> the standard confirmatory approaches are IHC or FISH for t(11;14).

<div class="verify"><strong>Verify:</strong> every discriminator in this table was checked against
the WHO classification and the lab's own validated flow panel before it went into the Anki deck.
A discriminator that is real in the literature may still not exist on your instrument.</div>
</div>
</details>

---

## Week 2 — Drill it

<details class="step">
<summary>Step 5 &middot; Quiz one question at a time, no lecturing</summary>
<div class="step__body">
<p class="step__card">Card used: <a href="library.html#/library/pillar-1-self-education/prompts/self-quiz-one-at-a-time">Self-quiz one at a time</a></p>

> Quiz me on CD5+ B-cell discrimination. One question at a time. Wait for my answer before the next
> one. Do not give me the answer unless I say I'm stuck. Start broad and narrow. If I get one wrong,
> ask a follow-up that isolates *why* I got it wrong rather than telling me the answer.

<div class="note">The last sentence converts a quiz into diagnosis. Without it the model corrects you
and moves on; with it, you find out whether you missed the marker or missed the reasoning.</div>
</div>
</details>

<details class="step">
<summary>Step 6 &middot; Work backwards from findings to diagnosis</summary>
<div class="step__body">
<p class="step__card">Card used: <a href="library.html#/library/pillar-1-self-education/prompts/reverse-case-drill">Reverse case drill (findings → Dx)</a></p>

> Give me a flow immunophenotype only — no clinical history, no diagnosis. I'll tell you my
> differential and the single next test I'd order. Then critique my reasoning before revealing
> anything. Make some of them deliberately ambiguous so the honest answer is "I need more information."

<div class="note">Asking for deliberately ambiguous cases is what stops this from becoming pattern
matching on tidy vignettes. Real panels are frequently equivocal, and "I need the IHC" is often the
correct answer — a drill that never allows that answer trains the wrong reflex.</div>
</div>
</details>

---

## Week 3 — Test cold, then bank it

<details class="step">
<summary>Step 7 &middot; Generate items — then audit them</summary>
<div class="step__body">
<p class="step__card">Card used: <a href="library.html#/library/pillar-1-self-education/prompts/mcq-generation-with-rationales">MCQ generation with rationales</a></p>

> Write 10 single-best-answer questions on CD5+ B-cell LPD discrimination at application level.
> For each, give the key and a one-line rationale for why every distractor is wrong. Do not write any
> item where more than one option could be defended as correct.

<div class="caught"><strong>Expect failures here.</strong> Two of the ten had a second defensible
answer despite the instruction, and one rationale misstated CD200 as "variably positive in MCL." The
published evidence on LLM-generated assessment items reports exactly this pattern — items lacking a
single defensible key, and confidently wrong explanations. Generated items are a <em>drafting</em> aid;
they are not a question bank until a human has audited every key.</div>

<div class="verify"><strong>Verify:</strong> answer each item yourself <em>before</em> reading the key.
Where you disagree with the model, resolve it against a primary source — not against the model.</div>
</div>
</details>

<details class="step">
<summary>Step 8 &middot; Bank only what survived verification</summary>
<div class="step__body">
<p class="step__card">Card used: <a href="library.html#/library/pillar-1-self-education/prompts/anki-flashcards">Anki flashcard generation</a></p>

> Convert the discriminator table we built into Anki cards, one discriminator per card, front =
> the discriminating question, back = the answer plus the method it's assessed by. Tab-separated,
> no preamble.

<div class="note">"One discriminator per card" and "plus the method" are deliberate. The method field
is what would have caught the cyclin D1 error at review time even if she had missed it in week 1 —
the deck encodes the correction, not just the fact.</div>

<div class="verify"><strong>Verify:</strong> 30 cards went in; four were dropped at review because
the discriminator could not be confirmed against the WHO classification or the local panel. A deck you
have not audited is a deck that drills your errors into permanent memory.</div>
</div>
</details>

---

## Now do it yourself

The arc transfers to any weak topic. Substitute yours and run the same eight steps:

1. **Gap analysis** — name the sub-skill, not the subject
2. **Schedule** — real time budget, learn → drill → test-cold
3. **Concept at level** — organized around what each finding answers
4. **Compare and contrast** — discriminators only, with method and reliability
5. **Self-quiz** — one at a time, diagnose the miss
6. **Reverse drill** — findings first, ambiguity allowed
7. **MCQ generation** — then audit every key
8. **Flashcards** — bank only what survived

**The one rule.** If you finish a loop and the model was never wrong, you were not checking. Somewhere
in three weeks it will state something confidently and incorrectly. Finding it is not a failure of the
tool — it is the evidence that you have built the competence the tool cannot give you.
