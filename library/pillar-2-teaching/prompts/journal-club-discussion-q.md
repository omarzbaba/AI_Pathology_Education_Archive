---
title: Journal club discussion questions
pillar: teaching
event_type: n/a
audience: faculty
difficulty: quick-win
time_to_use: <2min
visual: text-only
tags: journal-club, discussion
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Generate 5 discussion questions for a journal club paper, ranging from methods critique to clinical implications.

## When to use it

When you're leading journal club and want a question set that escalates from concrete to abstract, ensuring the discussion doesn't stall at 'I liked the paper'.

## The prompt

```
Generate 5 discussion questions for a journal club discussion of [paper citation]. The audience is [PGY level] residents and faculty.

Structure the questions to escalate:

1. **A concrete methods question** — what specific design choice or analytic approach should we scrutinize? Answer should be in the paper.
2. **A finding-level question** — how confident should we be in the headline result, given the design? Requires interpretation.
3. **A generalizability question** — does this result apply to our patient population? Requires connecting paper to practice.
4. **A practice-change question** — should this change what we do, and if so, how? Requires judgment.
5. **A contested question** — one that reasonable people would disagree on. Should provoke real debate.

For each question, include:
- The question itself.
- One sentence on what makes it a productive question (what discussion does it open?).
- The 'wrong' response that's most likely to come up early in discussion and how to redirect.

**Important — refinement:** Pressure-test question 5 (the contested one): if it has a clear answer in current literature, it's not actually contested. Replace it with one that reasonable experts genuinely disagree about.
```

## Expected output

5 escalating questions with productivity notes and predicted-wrong-response handling. The fifth question should be genuinely contested.

## Common failure modes

- All 5 questions are at the same level of abstraction.
- The 'contested question' has an obvious right answer and doesn't actually provoke debate.
- The 'wrong response' is straw-man rather than the real misconception.

## Required human verification

- Verify the methods-level question is answerable from the actual paper.
- Pre-test the contested question with a colleague — if they immediately agree with you, it's not actually contested.

## Best model and why

**Claude Sonnet 4.6** — Question escalation across abstraction levels is well within Sonnet's range. Pressure-test the 'contested' question regardless of model.
