---
title: Audience poll question generation
pillar: teaching
event_type: n/a
audience: faculty
difficulty: quick-win
time_to_use: <2min
visual: text-only
tags: lecture, polls
verified_models: TODO
last_updated: 2026-05-17
---

## What this prompt does

Generate audience poll questions at specific moments in a lecture to drive engagement and surface misconceptions. Different from MCQs — polls are designed for live response and discussion, not assessment.

## When to use it

When you're delivering a 30-60 minute talk and want to break up the lecture rhythm with 2-3 polling moments. Poll questions need different design than test questions.

## The prompt

```
Generate [N] audience poll questions for a [duration]-minute lecture on [topic] for [audience].

Each poll should:

1. Be answerable in 30-60 seconds — short stem, ideally 3 answer choices (not 5).
2. **Have a 'wrong' answer that most of the audience will pick**, by design. The polling moment is teaching, not assessment — the value is in the wrong answer being common and the explanation being illuminating.
3. **Map to a specific point in the lecture** where it serves as a transition or a moment of misconception-surfacing.
4. Include a 1-2 sentence note for me on how to use the result: what to say when the audience splits 60/30/10, what to say when they all get it right.

For each poll, provide:

- The question and answer choices.
- The intended placement in the lecture.
- The likely audience distribution.
- The teaching beat that follows.
```

## Expected output

N polls with placement, expected distribution, and follow-up teaching beats. The polls should feel like *teaching moments*, not pop quizzes.

## Common failure modes

- Polls are designed as assessment, with one obvious right answer — kills engagement.
- The 'common wrong answer' is not actually common — model misjudges audience.
- No suggestion for what to do with the result, so the poll lands flat.

## Required human verification

- Run the poll past a colleague at the target audience level. If they get the 'intended wrong answer' right cold, the poll won't work as designed.
- Verify the correct answer.
