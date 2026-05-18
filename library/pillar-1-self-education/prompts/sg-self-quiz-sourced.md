---
title: Source-grounded self-quiz from notebook material
pillar: self-education
event_type: n/a
audience: resident
difficulty: quick-win
time_to_use: 2-10min
visual: text-only
tags: source-grounded, self-quiz, drilling
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-18
---

## What this prompt does

The source-grounded version of [Self-quiz one at a time](library.html#/library/pillar-1-self-education/prompts/self-quiz-one-at-a-time). Drills you with questions that the model generates FROM your uploaded sources, with the answers traceable to specific source passages. Useful for active retrieval against YOUR specific study material.

## When to use it

Inside a board prep notebook when you want to test retention of the actual material you've been reading — not generic board questions.

## The prompt

```
You are my quiz partner working ONLY from the sources uploaded to this
notebook. Generate questions from those sources, not from your general
knowledge. Cite the source for each question's answer.

## My context

- **PGY level + topic:** [level + topic from the corpus]
- **Number of questions for this round:** [usually 5-10]
- **Difficulty calibration:** [recall / application / synthesis — pick one]

## Strict interaction rules

1. **Ask ONE question at a time.** Wait for my answer.
2. **Each question must be answerable from the uploaded sources.** If you
   can't generate a good question from the sources on this topic, tell me
   the corpus is thin on this topic rather than making up a question.
3. **After my answer, give feedback:**
   - "Correct" / "Wrong" / "Partially correct"
   - Cite the source that contains the answer: `[Source X, section Y]`
   - If wrong, name the specific gap and direct me to the source passage
4. **Adapt difficulty based on my response.**
5. **After [N] questions, give synthesis:**
   - Strongest area (cite specific responses)
   - Biggest gap (cite specific responses)
   - Which source I should re-read to address the gap

## Source-grounding rules

- **Every question must trace to a specific uploaded source.**
- **Every answer must cite the source where it's found.**
- **Do not generate questions whose answers come from your general
  knowledge rather than the uploaded corpus.**
- **If you correct me, the correction must be sourced.**

## Start now

Begin with a calibration question on [topic] drawn from the uploaded
sources. Don't tell me it's calibration; just ask.
```

## Expected output

A back-and-forth where every question and every correction is traceable to a specific uploaded source.

## Common failure modes

- **Questions whose "correct" answer is actually from the model's general knowledge** rather than your sources. Catch by asking "where in the corpus does this come from?"
- **Correction citations that don't match the source.** Verify spot-checks.
- **Model abandons source-grounding when retrieval is weak** — falls back to general knowledge silently. Watch for unsourced confidence.

## Required human verification

- **Spot-check 20-30% of citations** against the actual source.
- **For any answer that surprises you, verify directly.**
- **If the model seems consistently to "always have an answer" regardless of corpus content,** the grounding is decorative. Switch tools.

## Best model and why

**NotebookLM** for tightest grounding. **Claude Sonnet 4.6 via Claude Projects** for more conversational drill rhythm.
