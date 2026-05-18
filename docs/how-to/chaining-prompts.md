---
title: Chaining prompts in one session — the conversation discipline
last_updated: 2026-05-18
difficulty: intermediate
category: sessions
---

Almost all the prompts in this library are designed to be used in sequence within a single conversation, not as one-shot queries. This is the single biggest mental shift that separates a casual ChatGPT user from someone who gets real value out of LLMs for serious work.

This guide is about that pattern. By the end you'll know when chaining helps, when it hurts, when to start fresh, and how to structure a productive session — with three worked examples, one per pillar.

---

## Part 1 — The core principle

A modern LLM maintains *state* across the turns of a conversation. It remembers:

- What you asked earlier
- What it answered
- What you corrected
- What you specified about yourself, the audience, the task
- The format you've been using
- The terminology you prefer

This state is what makes chaining work. When you've spent two messages calibrating the model to "PGY-2 in their first month of blood bank, prefers concise explanations," the third message inherits that calibration. You don't restate the context.

By contrast, when you open a fresh chat tomorrow, that state is gone. The model has no memory of yesterday's calibration (with rare exceptions for paid tiers with explicit memory enabled, which is a separate topic).

This is also why "one-shot" prompts — a single message that expects a complete, finished answer — are the wrong mental model for almost all serious work. The real pattern is conversational: you and the model iterate together.

---

## Part 2 — When chaining helps (compounding context)

Chaining helps when each turn builds on what came before. The state compounds in your favor.

**Pillar I example:** in a board-prep session you might do:

1. *"I'm a PGY-3 on heme path service. Let's drill MGUS. Start by quizzing me on the diagnostic criteria — one question at a time, wait for my answer."*
2. *(You answer; the model checks your answer and corrects gently.)*
3. *"Good. Now do five more, escalating difficulty. Move from definition to mechanism to edge cases."*
4. *"Now ask me to interpret a specific SPEP trace pattern in words. Don't tell me the answer until I commit."*
5. *(You answer.)*
6. *"Walk me through the workup decision tree for a patient with what I just described, the way you'd talk through it with a fellow."*

Six turns. Forty-five minutes. By turn 6, the model knows your level (PGY-3), your topic focus (MGUS), how you've been answering (your strengths and gaps), and the conversational tone you've been using. It can produce a sophisticated walk-through that would have required a 500-word prompt if asked cold.

This is the value of chaining: compounded context produces calibrated output that would be hard to elicit any other way.

---

## Part 3 — When chaining hurts (anchoring on wrong framing)

The same state that makes chaining useful can hurt you when the early framing was wrong. The model anchors on its first interpretation and resists updating.

**Pathology example:** suppose you start a session asking, "Walk me through the workup for thrombocytopenia in a 30-year-old woman, post-partum, day 4." The model frames the discussion around post-partum-specific causes. You realize three turns in that the patient is actually 80 years old, not 30, and there's no post-partum context at all. You correct.

But the model has spent three turns thinking about HELLP, ITP-in-pregnancy, post-partum hemorrhage. It will often re-state corrections without fully re-framing — you'll see ghost references to "as I mentioned earlier in the post-partum context" even after you've corrected. The early frame leaks in.

**Sign that you should start fresh:**

- The model keeps referencing facts from earlier turns that were wrong or got corrected
- The model defends an earlier interpretation that you've explicitly retracted
- The conversation has drifted away from what you actually wanted to do
- You've issued more than two corrections to the same misconception

When this happens, open a fresh conversation. Recap the right framing in the opening message. The state lost is less valuable than the state corrupted.

---

## Part 4 — When to start fresh (and how)

Beyond corrupted framing, several other situations call for a fresh session:

- **Topic shift.** You're done with MGUS and want to drill ITP. State from the previous topic is irrelevant noise. Start fresh.
- **Calibration shift.** You're done teaching yourself and want to draft an OSCE for residents. Different audience, different output shape. Start fresh.
- **Long context.** The conversation has stretched past 40+ turns and you notice the model forgetting things from early in the session. Approaching context-window limit. Start fresh with a recap.
- **A different model.** You want to switch from Sonnet to Opus for a hard subproblem. New session, new model, fresh framing.

**How to start fresh well:** open a new conversation and lead with a one-paragraph recap of the relevant context. Don't dump the whole previous conversation; summarize the calibration and the current state.

Example recap opening: *"I'm a PGY-3 on heme path. We've already covered MGUS workup. Now I want to drill diagnostic algorithm for AIHA — start by asking me what I'd expect to see on a peripheral smear in cold-type vs warm-type."*

This recap, two sentences, restores the calibration the new session needs. Don't paste 5,000 words of previous chat; that's both wasteful and brings the corrupted framing with you.

---

## Part 5 — Three worked examples, one per pillar

### Example 1 — Pillar I: a 45-minute board-prep drill

**Goal:** thorough self-quiz on the diagnostic approach to chronic lymphocytic leukemia (CLL) vs lymphoma differential.

| Turn | You | Model (summary) |
|------|------|-----------------|
| 1 | "I'm a PGY-3 studying for boards. Drill me on CLL vs SLL vs MCL vs MZL — start by asking me the immunophenotype that distinguishes them." | Asks the question, doesn't answer yet. |
| 2 | *Your answer attempt.* | Marks what you got right; corrects specifics; doesn't restate everything. |
| 3 | "Now show me a flow plot description and ask me which entity." | Describes a CD5+, CD23+, lambda-restricted pattern with weak surface Ig. Asks the entity. |
| 4 | *Your answer.* | Confirms or corrects. |
| 5 | "Give me three more flow descriptions of decreasing typicality, escalating difficulty." | Three plots, the third one genuinely ambiguous. |
| 6 | "What additional studies would I order on the ambiguous case?" | Walks through FISH, cyclin D1 IHC, IgVH mutation status — calibrated to PGY-3, not PGY-1. |
| 7 | "If FISH shows t(11;14), how does that change my read of the morphology?" | Discusses MCL-specific features to look for retroactively. |
| 8 | "Now quiz me on three rapid-fire morphology calls — typical CLL, blastoid MCL, marginal zone." | Three image descriptions, asks for diagnosis. |

The 8th turn is a far more sophisticated drill than turn 1. It depends on the cumulative context: the model knows what you can and can't do, where to push, what level to pitch to.

If you'd asked turn 8 cold, you'd have had to write a 400-word prompt explaining your level, the entities, the format, the calibration. With chaining, two-sentence prompts suffice.

### Example 2 — Pillar II: building a teaching set in 25 minutes

**Goal:** a coherent teaching set on autoimmune hemolytic anemia — one case vignette, two matched-pair distractors, three MCQs.

| Turn | You | Model |
|------|------|-------|
| 1 | "Act as an attending hematopathologist designing teaching material. Generate a PGY-2-level case vignette for warm AIHA. Include presenting symptoms, basic labs, peripheral smear description, DAT result. ~200 words." | Generates the vignette. |
| 2 | "Critique your own vignette. What would a strong PGY-2 catch about the case that a weak PGY-2 would miss?" | Lists the discriminating features. |
| 3 | "Generate a matched-pair distractor case: same presentation pattern but actually cold-type AIHA. Change only what's necessary." | Cold-type version, minimal changes, true matched pair. |
| 4 | "Now a third matched case: looks like AIHA but is actually drug-induced." | Third case. |
| 5 | "Three MCQs that would discriminate a resident who understands warm vs cold vs drug-induced AIHA. Bloom level 'analyze'. Five choices, one best answer, two-sentence rationale per choice." | Three MCQs. |
| 6 | "Critique each MCQ. Which is the weakest, and why?" | Honest critique. The third MCQ has overlapping correct answers; flag it. |
| 7 | "Rewrite MCQ 3 to fix the issue." | Cleaner version. |

What you have at the end: one validated case, two matched distractors, three reviewed MCQs. The chaining is essential because the matched-pair logic (turns 3–4) depends on the original vignette being in working memory.

### Example 3 — Pillar III: drafting an orientation packet in 30 minutes

**Goal:** a new-resident orientation one-pager for a CP rotation.

| Turn | You | Model |
|------|------|-------|
| 1 | "Draft a one-pager orientation document for a PGY-1 starting their first CP rotation at an academic medical center. Sections: what you'll do day-to-day, what to read this week, who to ask for help, common pitfalls. Calibrated to someone who's never done CP before." | Generates draft. |
| 2 | "The 'common pitfalls' section is too generic. Replace it with three pitfalls specific to a first-week resident in a hospital with a large transfusion service." | Replaces section with specifics. |
| 3 | "Add a 'first sign-out' subsection: what the resident should expect, who runs it, what to do the night before." | Adds the subsection. |
| 4 | "Critique the whole packet from the perspective of an actual PGY-1 reading it the night before they start. What's confusing? What's missing? What's preachy?" | Honest critique. |
| 5 | "Revise based on your critique. Keep length under one page." | Revised version. |
| 6 | "Now generate a matching one-pager for the supervising attending — 'how to onboard a new PGY-1 this week.' Mirror structure." | Attending version. |

Four turns of building plus two of critique and revision. The attending one-pager (turn 6) is much better than it would have been cold — it can match the resident one-pager because the model has both in working memory.

---

## Part 6 — Anti-patterns to avoid

**1. Opening fresh conversations for every question.** Especially common with new users who treat ChatGPT like Google. You lose all the calibration. If you're on the same topic and same audience, stay in the same session.

**2. Issuing tiny corrections without explaining why.** "No, fix that." The model doesn't know what to fix. Better: "The third paragraph has the wrong drug name — replace [X] with [Y]. The rest is fine." Specificity helps.

**3. Letting the conversation sprawl.** A 40-turn conversation that's covered six unrelated topics is not chaining; it's chaos. The model forgets early turns; you forget what you've asked. Topic-locked sessions of 5–12 turns are usually the sweet spot.

**4. Pasting full earlier conversations into a new chat.** "Here's everything we discussed yesterday — now continue." This brings the corrupted framing forward. Instead: summarize the relevant context in two sentences.

**5. Re-stating the audience every turn.** "As I mentioned, I'm a PGY-3…" The model already knows. Repetition is friction.

---

## Part 7 — Practical session shapes

For each pillar, a default session structure that tends to work:

**Self-education:** *Calibrate → drill → critique → extend.* Spend the first turn establishing your level. Drill for 4–6 turns. Have the model critique your reasoning. Extend to a related topic only if state still feels fresh.

**Teaching:** *Generate → critique → revise → expand.* Generate a draft (vignette, MCQ, outline). Have the model critique its own work. Revise. Generate a matched second piece using the first as anchor.

**Operations:** *Draft → reality-check → revise → mirror.* Draft the document. Reality-check from the recipient's perspective ("read this as the new resident who will receive it"). Revise. Generate the mirror document (e.g., attending-facing version of the resident-facing one).

---

## Part 8 — One last point on memory

Some paid AI products (ChatGPT's "Memory" feature, Claude with explicit memory in Projects) extend state *across* conversations. You can tell ChatGPT "remember that I'm a PGY-3 on heme path" and it will carry that across sessions.

This is useful but adds a new failure mode: stale memory. You change rotations, and the model still thinks you're on heme. Periodically review and clear the memory.

Without explicit memory features, every new conversation is fresh. Plan accordingly: write the opening message of a new conversation as if briefing a smart colleague who has never met you. Three sentences of context, then your question.

---

## Part 9 — Practical checklist

For your next serious AI session:

- [ ] I established calibration in the first turn (level, audience, format)
- [ ] I built on the same conversation rather than opening a new one for related questions
- [ ] When the model produced a draft, I asked for a critique before accepting
- [ ] When I corrected the model, I specified what to change and why
- [ ] When framing got corrupted, I started a fresh session with a brief recap
- [ ] I kept the session topic-locked (one task at a time, not six)
- [ ] I noticed when the conversation got too long and split into a new session before it degraded

If you can answer yes to all seven, your sessions will produce dramatically more value than cold one-shot prompts. That's the entire skill.
