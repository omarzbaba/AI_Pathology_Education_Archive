---
title: How to write a good prompt — a teaching tutorial
last_updated: 2026-05-18
difficulty: beginner
category: start
---

This tutorial is the one piece of writing in the library you can hand to a learner who has never thought carefully about prompting. Read it once for yourself, then use it as the basis for a one-hour teaching session — there's a session outline at the end.

The goal is not "prompt engineering" as a technical specialty. The goal is to teach the same discipline you'd use writing a referral, an attending's sign-out note, or a question for your fellow on rounds: be specific about who you are talking to, what you want, and how you'll know whether the answer is any good.

---

## Part 1 — Why most prompts fail

A surprising number of physicians have tried AI, gotten a mediocre answer, and concluded the tool isn't ready. Almost always, the issue was the prompt, not the model.

Mediocre prompts share three traits:

1. **Vague audience.** The prompt didn't say *who* the answer was for. The model defaults to a generic "intelligent adult," which is no one in particular.
2. **Vague output shape.** The prompt didn't say what form the answer should take. The model defaults to ~3 paragraphs of prose, which is rarely what you actually wanted.
3. **No verification cue.** The prompt didn't ask the model to surface its own uncertainty, cite its sources, or admit what it doesn't know. The model defaults to fluent confidence, which is the most dangerous output mode for medical work.

A well-formed prompt fixes all three.

---

## Part 2 — The five components of a good prompt

A useful prompt has five components, usually in this order. Skipping any of them is the most common cause of disappointment.

### Component 1: Role (who the model is)

Set the model's voice and frame of reference in one sentence. The reason to do this isn't because the model becomes a different entity — it doesn't — but because role-setting language pulls the relevant patterns from the model's training data to the front. A model asked to "respond as an attending hematopathologist supervising a PGY-2" will draw on patterns from hematopathology teaching corpora, not generic clinical writing.

**Examples:**

- "Act as an experienced cytopathology fellow signing out alongside a junior resident."
- "You are a board examiner writing distractors for an AP/CP-style MCQ."
- "Respond as a journal club facilitator who has read this paper carefully and wants to draw out methodology concerns."

The role isn't decoration. It changes the texture of the output noticeably. If you skip it, you get a default texture that is rarely what you want.

### Component 2: Context (what the model needs to know that it can't infer)

The model knows medicine in general. It does not know:

- Your institution's specific protocols
- Your subspecialty conventions ("at our institution, we use the WHO 2024 not 2022 nomenclature")
- The level of the learner you're writing for
- The specific clinical scenario (what's the patient population, what's the stake, what's already been tried)
- Your own past corrections and preferences in this conversation (if it's a fresh session)

Give the model the context that would change the answer. Don't give it context that wouldn't.

A good test: read your prompt out loud as if you were briefing a smart visiting fellow who has never been to your service. Did you tell them everything they'd need to give a useful answer? Did you over-explain things they'd already know?

### Component 3: Task (what you actually want)

This sounds obvious. It is the most commonly skipped step.

The task should be a verb plus a clear deliverable. Not "tell me about MGUS" — that's a topic, not a task. Better: "explain the diagnostic criteria for MGUS as I would present them to a first-year resident in three layers — basic, mechanistic, nuanced." Now the model has a target.

If your task has multiple parts, number them. The model is much better at handling "do these three things in order" than "address these issues somehow."

### Component 4: Format (the shape of the answer)

Specify the output structure explicitly. If you don't, the model picks a default that is usually wrong for your purpose.

- "Respond in a numbered list of 5–7 items, each one sentence."
- "Respond as a one-page handout suitable for printing, with section headers."
- "Respond as a single paragraph, no bullets, 100–150 words."
- "Respond as a JSON object with fields *diagnosis*, *confidence*, *next_steps*."
- "Respond as 3 multiple choice questions with 5 options each, the correct answer marked, and a 2-sentence rationale per option."

Format is the single highest-leverage component to add to a weak prompt. A vague topic plus a specific output shape often produces a usable answer; a great topic plus a vague output shape often does not.

### Component 5: Verification cue (how the model should signal its uncertainty)

This is the component most physicians omit and most regret omitting. By default, models produce fluent, confident text whether or not they actually know the answer. You have to ask them to do otherwise.

Add a sentence like one of these:

- "At the end, list any claim in your answer that you are less than 80% confident about, and what you'd verify against."
- "If any part of this requires checking the current guideline, flag it explicitly rather than answering from memory."
- "Cite the specific source you're drawing each numerical threshold from. If you don't have a specific source, say so."
- "After your answer, list two things you might be wrong about and how I could check."

The model will not be perfectly calibrated — but it will be measurably more honest than it would have been without the cue, and the verification list itself often points you to the specific things you should re-check.

---

## Part 3 — Domain anchoring for pathology

The five components above apply to any prompt. Pathology adds a few specific anchors that meaningfully improve output.

**Specify the modality.** "Photomicrograph" vs "gross" vs "molecular result" vs "SPEP trace" vs "guideline text" vs "patient chart excerpt" — each has different conventions. The model handles each better when told which one to expect.

**Specify the level of evidence you want.** "Cite the relevant CAP guideline statement" gets a different answer than "explain the general clinical reasoning." Be explicit.

**Specify the audience's calibration, not just their title.** "PGY-2 in the first month of blood bank, has had two days of didactics, has seen no real cases" is more useful than "junior resident."

**Specify the failure mode you're trying to avoid.** "Do not jump to a diagnosis without articulating the pattern-recognition reasoning step first" is more useful than "be thorough." The model knows what to avoid better than it knows what "thorough" means.

**Specify the verification step.** "Don't rely on a recalled drug name; verify against the FDA label or note that verification is needed" prevents a common, dangerous failure mode where models confidently produce a near-correct drug name.

---

## Part 4 — Iteration: three rounds is usually enough

Almost no prompt works perfectly first time. The right mental model is "draft, observe, revise" — like writing a referral.

**Round 1: Draft.** Write the prompt with all five components. Run it. Read the output critically. Don't be satisfied.

**Round 2: Diagnose.** What's wrong with the output?

- *Wrong level?* Calibration was off — be more specific about audience.
- *Wrong format?* Format spec was vague — be more explicit.
- *Confidently wrong on facts?* You forgot the verification cue.
- *Missed a critical edge case?* You forgot to mention it in context.
- *Generic textbook output?* The role and context didn't pull the model into your specific situation.

**Round 3: Refine.** Edit the prompt — don't start over. Re-run.

By round 3, you usually have a prompt that's good enough to save as a template. Save it. The third version is the durable one.

Three rounds is also the right teaching unit. Show a learner all three rounds; the diagnosis step is where the learning happens.

---

## Part 5 — Few-shot vs zero-shot: when to use each

A **zero-shot** prompt asks the model to do the task without giving it examples. ("Write three multiple-choice questions about MGUS.")

A **few-shot** prompt gives the model 1–3 examples of the kind of output you want before asking it to produce more. ("Here are two MCQs in the style I want. Now write three more on different MGUS sub-topics in the same style.")

**Use zero-shot when:**

- The task is straightforward and your format spec is clear
- You don't have good examples ready
- You're exploring what the model can do

**Use few-shot when:**

- The task has a specific stylistic convention you can't fully specify in words
- The model has produced near-misses you can show as "more like this"
- You're trying to enforce a specific format the model keeps drifting from

Few-shot is more work to set up but produces measurably more consistent output. For repeated tasks (you'll use this prompt monthly), invest in few-shot. For one-offs, zero-shot is fine.

---

## Part 6 — Structured output

When the answer needs to be processed (counted, sorted, fed into another tool, compared across many prompts), force the model to produce structured output.

Structured doesn't mean JSON necessarily. It means *predictable shape*. Options:

- **Numbered list** with a fixed number of items
- **Named sections** with required headers ("## Diagnosis", "## Differential", "## Next steps")
- **Two-column table** with fixed columns
- **JSON object** with named fields and type constraints

Models follow structure they're explicitly given, and they follow structure better when you give an example. A prompt that says "respond as a JSON object with fields *finding*, *grade*, *certainty (0–100)*, *next_step*" plus a single example will produce parseable output 95%+ of the time. The same prompt without the example produces it 60% of the time.

If you're building anything that processes model output downstream — a study tool, a curriculum-generation pipeline, a triage screen — structured output is non-negotiable.

---

## Part 7 — Model selection: when to use which

Briefly, since this is covered in the prompt-level metadata across the library:

- **Sonnet** (current: Claude Sonnet 4.6) — the default for almost everything in this library. Fast, accurate enough, calibrated enough, low enough cost. Use this unless you have a specific reason not to.
- **Opus** (Claude Opus 4.7) — when the task requires deep reasoning, long-context synthesis, or you've already had Sonnet near-miss on something and want a second opinion from a more capable model.
- **Haiku** (Claude Haiku 4.5) — for high-volume, low-stakes tasks (drafting many similar items at once). Cheaper. Less depth.

Other vendors' models have analogous tiers. The principle generalizes: use the cheapest model that produces correct output, and graduate to a more capable model only when correctness is the bottleneck.

A common trap: defaulting to the most capable model because "it's better." It isn't always — and the latency cost is real when you're iterating. Start with Sonnet-tier, escalate only when needed.

---

## Part 8 — A worked example, in three rounds

Here's what the iterative process looks like end-to-end. The task: get a brief, learner-appropriate explanation of monoclonal gammopathy of undetermined significance (MGUS) for a first-month PGY-2 in CP.

### Round 1 — the naive prompt

> Explain MGUS.

**What you get:** ~250 words of generic Wikipedia-style explanation. Probably accurate. Probably not at the right level. Probably no acknowledgement of the cases where the boundaries are fuzzy.

**Diagnosis:** No role, no audience, no format, no verification cue. The 1990s default.

### Round 2 — adding the components

> Act as an experienced hematopathology attending teaching a PGY-2 in their first month of CP. Explain MGUS in three layers: (1) the one-sentence version a first-year resident would understand; (2) the mechanistic explanation a PGY-2 should know after a month of blood bank; (3) the nuance that would distinguish a strong fellow. Respond as three paragraphs with the layer named at the start of each. At the end, flag any specific numerical threshold (e.g., M-spike cutoff) that I should verify against the current IMWG criteria rather than trusting your memory.

**What you get:** Three-layer explanation calibrated to the audience, with the M-spike cutoff explicitly flagged for verification. Much closer to usable.

**Diagnosis:** Mostly works. But the layers blur together in length — the "first-year" layer is 80 words and the "strong fellow" layer is 60. The model is generating average-length paragraphs rather than respecting the differential complexity.

### Round 3 — tightening the format and adding a verification structure

> Act as an experienced hematopathology attending teaching a PGY-2 in their first month of CP. Explain MGUS in three layers of increasing depth:
>
> 1. **The one-sentence version** a first-year resident would understand. Exactly one sentence.
> 2. **The mechanistic explanation** a PGY-2 should know after a month of blood bank. 3–5 sentences. Include the diagnostic criteria but flag any numerical threshold (e.g., M-spike cutoff) that I should verify against the current IMWG criteria rather than trusting your memory.
> 3. **The nuance** that would distinguish a strong fellow. 3–5 sentences. Focus on edge cases, evolving classification, or recent literature shifts.
>
> After the three layers, end with one follow-up question I should be able to answer if I understood layer 2 correctly. The question should target the most likely misunderstanding for someone at this level.

**What you get:** Three properly-calibrated layers, named thresholds flagged for verification, plus a self-check question targeting a known misunderstanding. This is a prompt worth saving.

The third version is what you'd build a prompt template from. The first version is what most people try, conclude "AI isn't ready," and abandon. The difference is twenty minutes of iteration.

---

## Part 9 — Common failure modes (and how to design against them)

| Failure mode | What it looks like | Design against it by |
|---|---|---|
| **Hallucinated citation** | The model cites a paper or guideline that doesn't exist, or cites a real one that doesn't contain the claim | Ask: "cite the specific source for each numerical claim; if you don't have a specific source, say so" |
| **Soft hedging** | The answer is full of "could be," "may be," "in some cases" — nothing actionable | Ask: "for each item, state your confidence level (high/medium/low); reserve hedging for genuinely uncertain points only" |
| **Off-target detail level** | The answer is too elementary, or too dense, or assumes background the learner doesn't have | Specify audience calibration precisely; use "first month of blood bank" not "junior resident" |
| **Jumps to diagnosis without showing reasoning** | The answer gives a conclusion but skips the pattern-recognition steps | Ask: "before giving the diagnosis, list the 2–3 morphologic features that drove your interpretation" |
| **Average-of-everything** | The answer reads like the average of every textbook chapter ever written, with no specific point of view | Strengthen the role; specify "from the perspective of someone who actually signs out this material weekly" |
| **Confidently wrong on a current threshold** | A diagnostic cutoff has changed in the current guideline; the model uses the old one fluently | Always add the verification cue for numerical thresholds; don't trust memory |
| **Drops the format** | You asked for JSON or a table and got prose | Provide one example of the format; restate the format requirement at the end of the prompt |

---

## Part 10 — Practical checklist

Before you press Send, the prompt should pass this checklist:

- [ ] Is there a **role** that pulls the model into the right frame?
- [ ] Is the **context** sufficient — and not bloated with what the model already knows?
- [ ] Is the **task** a clear verb plus deliverable, with multi-part tasks numbered?
- [ ] Is the **format** specified concretely (length, structure, named sections)?
- [ ] Is there a **verification cue** for the things you don't want the model to bluff on?
- [ ] If you've used this prompt before and it drifted, did you add a one-line example to anchor it?
- [ ] Would a colleague reading this prompt understand exactly what answer you wanted?

If you can answer yes to all seven, you have a prompt worth running. If you can't, fix the missing component first — it's faster than running a weak prompt and re-iterating from a confusing answer.

---

## Appendix — One-hour teaching session outline

This tutorial maps directly to a one-hour resident or faculty teaching session. Suggested structure:

**0–5 min — Opening.** Show a generic ChatGPT/Claude answer to a single-word prompt ("MGUS"). Ask the room: would you use this output? Most will say no. Ask why.

**5–20 min — The five components (Part 2).** Walk through each, with one example per component. Take questions. Emphasize that the verification cue is the most-skipped, most-regretted component.

**20–30 min — Pathology-specific anchors (Part 3).** Brief. The audience is pathology; the examples land naturally.

**30–45 min — Worked iteration (Part 8).** Live demo, ideally. Take a learner-suggested topic and walk through rounds 1–2–3 in real time. The diagnosis step (round 2 → round 3) is where the learning happens. Slow down there.

**45–55 min — Failure modes (Part 9).** Walk through the table. Ask the room which they've seen. Many will recognize the "confidently wrong on threshold" pattern.

**55–60 min — Practical checklist (Part 10).** Hand it out as a one-pager. Encourage learners to keep it next to their workstation for the first week.

**Optional — homework.** Ask each learner to bring one prompt they ran in the last week, plus the output, to the next session. Workshop them together. This is where the skill consolidates.
