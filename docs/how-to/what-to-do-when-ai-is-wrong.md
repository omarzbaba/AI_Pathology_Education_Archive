---
title: What to do when the AI is wrong — a critical-reading skill
last_updated: 2026-05-18
difficulty: intermediate
category: reading
---

The companion to *How to write a good prompt* is *how to read what comes back*. The model will be wrong. Sometimes obviously; more dangerously, often subtly, in ways the response itself does not signal. The discipline of catching these errors and responding to them is the single skill that separates a productive AI user from a hazardous one.

This guide is about that discipline. The intended reader has used an LLM a few times, written reasonable prompts, and now wants to learn to read responses the way a senior attending reads a junior resident's note: charitably but never credulously.

---

## Part 1 — The five failure modes

Almost every problematic AI response falls into one of five patterns. Learn to name them and you'll spot them faster.

### Failure 1 — Confident-wrong

The response sounds right. The grammar is fluent. The structure mirrors textbook writing. But a specific factual claim is wrong: a threshold is off by a factor of ten, a drug name is close but not quite right, a guideline recommendation is attributed to the wrong organization.

This is the most dangerous failure because the surface signal is *correct*. There is no hedge, no qualification, no stumble in the prose. You only catch it if you already know the right answer or you verify it externally.

**Pathology example:** asked about the M-spike cutoff for symptomatic myeloma, the model returns a confident "3 g/dL" — close to the historical IMWG threshold but not what current guidelines say, and not how the question is operationally settled in practice. Fluent, wrong, undetectable from the text alone.

**How to catch it:** verify every numerical threshold against your authoritative source. Never trust a model-recalled number for a clinical decision.

### Failure 2 — Soft hedging

Every sentence is so hedged that nothing is actionable. "Could be," "may include," "in some cases," "depending on the clinical context." The response reads as comprehensive while saying nothing specific. You walk away feeling informed but unable to act.

This often happens when you ask a question the model is uncertain about. Instead of saying "I'm not sure," it produces fluent hedge-speak.

**Pathology example:** "Is this lesion benign?" gets back four paragraphs of "could be," "may suggest," "would depend on" — useful as a differential framework but useless as the answer you actually asked for.

**How to catch it:** count the hedges. If more than half the sentences include one, the answer is mush. Push back with: *"For each item, state your confidence (high / medium / low). Reserve hedging for items where you have a specific reason to be uncertain — don't hedge as a writing style."*

### Failure 3 — Hallucinated citations

The response cites a specific paper, guideline, or authority that either does not exist, exists but doesn't contain the claim attributed to it, or exists but is attributed to the wrong year / wrong authors / wrong journal.

The model is filling in plausible-sounding bibliography because it knows that citations make answers feel authoritative. The bibliography is a feature of the response style, not of actual sourcing.

**Pathology example:** "Per the 2024 ASH guideline, the threshold is X." When you look up the 2024 ASH guideline, no such recommendation exists; the guideline either says something different or doesn't address the topic at all.

**How to catch it:** never cite an AI-supplied citation in your own work without opening the actual paper or guideline and confirming the claim is there. If the source has a DOI, look it up. If it has a guideline section number, open the PDF and find that section. The work of verification is the work; do not skip it.

### Failure 4 — Drug-name and entity swaps

The model substitutes a similar-sounding drug, gene, or entity for the correct one. Particularly common with newer agents, rare entities, and drugs that share generic-name fragments.

**Pathology example:** asked about a drug for AIHA, the model returns a confident answer naming a drug that exists but is indicated for a different autoimmune cytopenia. Or it confuses *daratumumab* with *carfilzomib* (both myeloma drugs, very different mechanisms, very different uses). Or it merges two CDx names into one that sounds plausible but isn't real.

**How to catch it:** verify drug names against the FDA label or a maintained reference (UpToDate, DynaMed). For genes / entities, verify against an authoritative database (OMIM, COSMIC, the WHO classification).

### Failure 5 — Threshold and reference-range drift

A specific subspecies of confident-wrong: the model recalls an old version of a numerical threshold that has since been updated. Guidelines change; the model's training data is frozen. Diagnostic cutoffs that moved in the last 1–2 years are particularly prone.

**Pathology example:** the model gives you the 2018 IMWG cutoff when the 2024 update changed it. Or the previous WHO ed criteria when the current edition revised them.

**How to catch it:** when a numerical threshold is clinically relevant, *always* check the current published guideline. Add this to your prompts: *"For any numerical threshold or diagnostic cutoff, flag it explicitly so I can verify against the current guideline — do not trust your memory for these."*

---

## Part 2 — The five-minute audit

When you receive a response and need to evaluate it before using it, walk this five-step audit. It takes about five minutes for a typical response.

1. **Identify every numerical claim.** Thresholds, cutoffs, percentages, sensitivities, dosages, intervals. Mark them.
2. **Identify every named entity.** Drugs, genes, diseases, antibodies, classifications. Mark them.
3. **Identify every citation.** Papers, guidelines, organizations attributed with specific claims. Mark them.
4. **Identify the strongest factual claim.** The one sentence that, if wrong, would most undermine the answer.
5. **Verify them in roughly that priority order.** Numerical and strongest claim first, since they have the highest blast radius.

If any of the first three categories pass spot-check (numerical correct, names correct, citations real), trust grows. If any fail, treat the whole response as suspect and start over.

This is not a one-time exercise. It's a permanent posture for high-stakes use.

---

## Part 3 — How to push back productively

When the model is wrong, you have three reflexive options. Two of them are bad.

**Bad option A — accept the answer anyway.** Out of social politeness, out of cognitive ease, out of "well, it's probably fine." This is how AI errors propagate into real clinical decisions, slide decks, MCQs, and resident teaching.

**Bad option B — correct the model in conversation and then trust the next answer.** Almost everyone does this. You say "actually, the threshold is X, not Y" and the model immediately agrees: "*You're right, the threshold is X. Let me revise…*" You feel validated. **The model is exploiting your correction.** It is generating a response calibrated to your stated correction, not actually fact-checking itself. If you'd told it the wrong threshold, it would have agreed with that too.

**Good option — push back with structure.** Instead of telling the model the right answer, ask it to defend its own:

- *"You stated [X]. What's the source for that?"*
- *"That threshold doesn't match what I learned. Walk me through your reasoning for that number."*
- *"Cite the specific guideline or paper that contains the recommendation you just gave. If you don't have a specific source, say so explicitly."*

If the model can't defend its answer, you've caught a hallucination. If it can, you've learned something — or you've identified a real disagreement to look up.

The discipline: **never tell the model the correct answer in the same turn you're checking it.** Force the model to defend its own claim first.

---

## Part 4 — Cross-model verification

When a question matters and you've got time, ask the same question to two different model families (Claude and ChatGPT, or one of them and Gemini). Different models hallucinate different things. If they agree on a substantive answer, your trust should rise. If they disagree, you've identified a question worth verifying against a primary source.

This is especially valuable for:

- Drug names and indications
- Specific guideline citations
- Numerical thresholds
- Rare-entity differentials

It is overkill for:

- Format-driven tasks (rubrics, schedules, outlines)
- Generative tasks where divergence is the point (vignettes, MCQ distractors)
- Bulk drafting (you're going to review the output anyway)

A useful habit: when you escalate to your flagship-tier model for a hard question (Opus, GPT-4.5, Gemini Pro), also run it past your medium-tier of the *other* provider as a cross-check. Cheap insurance against single-vendor hallucinations.

---

## Part 5 — When to switch models entirely

Sometimes the model you're using keeps getting a specific topic wrong, no matter how you prompt. Signs:

- Three reasonable prompts in a row produce confidently-wrong answers on the same general topic
- The model insists on a fact that is verifiably wrong even after you push back with citations
- The model's tone goes brittle ("Yes, you're correct, however my position remains…") — a known failure mode where the model defends its earlier wrong answer rather than updating

When you see this pattern, **switch to a different model family entirely.** Claude → GPT, or vice versa. The two models have different training data and different blind spots. A question that's a known weakness for one is often a strength for the other.

This is the closest thing to "the AI is just wrong about X" you should accept. Don't conclude this from one bad answer; conclude it after the pattern persists across reasonable attempts.

---

## Part 6 — When to walk away

Some questions are beyond what AI can usefully help with right now. Recognizing these saves you time and protects you from over-reliance.

Walk away when:

- The question is about your specific patient (use the EMR, not an AI)
- The question requires real-time information the model couldn't have (this week's case at tumor board, today's lab numbers)
- The question is about your specific institutional protocol (the AI cannot know it; either you tell it the protocol or you check the protocol directly)
- The question is about something so rare that you can't independently verify the answer (zebras in your subspecialty where you'd be relying on AI for things you can't catch errors on)
- The stakes are too high for verification (rare diagnostic situations where any error matters and you can't afford the time to spot-check)

In each of these cases, the right next step is a human source — colleague, textbook, current guideline, patient chart — not a re-phrased prompt to the model.

---

## Part 7 — The temperament shift

Most of the discipline above is technique. The deeper shift is temperament. The pathologists who use AI well share a posture:

- They expect to be wrong roughly 10–20% of the time on factual questions, and they design their workflow assuming that
- They never feel pressure to accept an answer just because the prose flows
- They don't reason "the AI said it, so I'm covered" — they reason "I'm signing this work, the AI is a draft"
- They feel comfortable saying "I don't know, and the AI didn't help either; let me look it up" instead of treating that as a failure

This is the same posture you bring to a junior resident's draft of a tumor-board slide. You don't expect it to be perfect. You don't get angry when it isn't. You read it carefully, mark what needs fixing, and ask the resident to take another pass. The AI is a tireless resident with one specific blind spot you must always remember: it does not know when it is wrong.

---

## Part 8 — Practical checklist

Use this card next to your workstation for the first month of serious AI use.

- [ ] I identified every numerical claim before trusting the response
- [ ] I verified at least one specific claim against a primary source
- [ ] I did not tell the model the correct answer before checking its reasoning
- [ ] If I pushed back, I asked the model to defend its claim rather than supplying the right answer
- [ ] If the model insisted on a wrong answer after pushback, I switched to a different model family
- [ ] I did not cite the AI as a source in any output that will be read by others
- [ ] If this answer matters to a patient, a learner's grade, or my own publication record, it has been verified against an authoritative source

If you can answer yes to all seven before using a response, you have done the work. If you can't, do it before you do.
