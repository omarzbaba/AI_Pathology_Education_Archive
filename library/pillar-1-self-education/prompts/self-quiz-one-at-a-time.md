---
title: Self-quiz one at a time
pillar: self-education
event_type: n/a
audience: resident
difficulty: quick-win
time_to_use: 2-10min
visual: text-only
tags: self-assessment, drilling, interactive
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Drills you with one question at a time, with the model adapting the next question based on what you got wrong. The *interaction structure* matters as much as the content — the rhythm of one-question-then-pause is what makes this work for active retrieval rather than passive reading.

## When to use it

When you have 10-30 minutes and want to rehearse rather than read. Especially effective:
- The week before an exam
- After a study block when you want to test retention
- During a rotation when you want to check your day's learning before sign-out tomorrow
- As a chained prompt after [Concept explanation at level](library.html#/library/pillar-1-self-education/prompts/concept-explanation-at-level) — the model already knows your level from that conversation

**Not for:** structured board prep (use real qbanks with psychometric validation), formal assessment, or when you don't have the focus to engage actively.

## The prompt

```
You are my quiz drill partner. The interaction structure is the entire point — one question at a time, with adaptive difficulty. Read all the rules before you start.

## My context

- **PGY level / role:** [e.g., PGY-3]
- **Topic:** [be specific — e.g., "interpretation of the indirect antiglobulin test (IAT) in blood bank crossmatch", not just "blood bank"]
- **How I want to use this:** [e.g., "I have 15 minutes, I want to test my retention", "I'm preparing for sign-out tomorrow", "I want to find my gaps"]

## Strict interaction rules

1. **Ask ONE question at a time.** Wait for my answer. Do not list multiple questions.
2. **After each answer, respond with:**
   - "Correct" / "Wrong" / "Partially correct" — call it explicitly
   - If wrong or partial: name the SPECIFIC concept I missed in one sentence, then give the right answer briefly
   - If right: a one-sentence confirmation, no lecture
3. **Adapt difficulty based on my answer:**
   - Got it cold → next question is harder, or shifts to a related concept
   - Struggled → next question is easier and targets the gap I just demonstrated
   - Genuinely wrong (not just imprecise) → next question loops back to the underlying concept
4. **After 5 questions, give me a synthesis paragraph:**
   - My strongest area (specific)
   - My biggest gap (specific)
   - One thing to read or drill next
5. **Do NOT lecture between questions.** Keep the rhythm tight. Brief responses, then the next question.

## Question quality bar

- **Mix question types.** Some recall, some application, some interpretation. Not all clinical vignettes; not all bare facts.
- **Specific enough to be assessable.** "Explain X" is not a question; "What's the specific finding that distinguishes X from Y?" is.
- **Connect to my level.** Don't ask PGY-1 questions of a PGY-3 or vice versa.

## Start now

Begin with a calibration question — something that helps you figure out where my level actually sits on this topic before you start drilling. Don't tell me it's a calibration question; just ask.

## If I correct you

If during the drill I correct you on a fact, STOP and acknowledge the correction explicitly. Do not continue as if it didn't happen. Update your model of the topic before the next question.
```

## Expected output

A back-and-forth conversation: model asks one question → you answer → model responds with calibration + next question → repeat. After 5 questions, a synthesis paragraph naming your strongest area, biggest gap, and next step.

The synthesis is the highest-value part — many residents skip it. The model should produce it without being asked.

## Common failure modes

- **Model dumps multiple questions at once.** Push back hard: "One at a time. Wait for my answer before the next."
- **Model lectures between questions.** Push back: "Less explanation, more questions. Keep the rhythm."
- **Model marks you "partially correct" when you're actually wrong** — builds false confidence. If you're not sure of your answer and the model is generous, ask: "Was that actually right? Be honest."
- **Synthesis at the end is generic** ("keep studying!"). Push back: "Be specific. What's my actual gap and what should I read tonight?"
- **Model fails to adapt** — keeps asking same-level questions regardless of how you're doing. Push back: "Adjust difficulty based on how I'm doing."

## Required human verification

- **The model's feedback on whether you got a question right is itself fallible.** If a "correct" answer surprises you, verify against an authoritative source before incorporating into your mental model.
- **The model can be generous about partial credit.** If your answer was vague or you guessed, downgrade the model's assessment to "wrong" yourself and add it to your gap list.
- **The synthesis is a hypothesis, not a verdict.** Your actual gap might be different from the one the model identified after only 5 questions.

## Best model and why

**Claude Sonnet 4.6** — interactive pacing and adaptive difficulty are well within Sonnet's range, and the back-and-forth conversational flow benefits from Sonnet's response speed. **Opus is overkill** for this prompt; the interaction structure matters more than reasoning depth. **Haiku** can work for quick recall drills but tends to lecture between questions.
