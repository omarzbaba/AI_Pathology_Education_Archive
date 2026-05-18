---
title: Journal club discussion questions
pillar: teaching
event_type: n/a
audience: faculty
difficulty: quick-win
time_to_use: <2min
visual: text-only
tags: journal-club, discussion, escalating-questions
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Generates 5 discussion questions for journal club, ordered from concrete (methods, numbers) to abstract (implications, practice-change) and ending with one genuinely contested question that reasonable experts disagree about.

## When to use it

When you're leading journal club and want a question set that escalates rather than stays at one level. Especially valuable for stalling-out discussions ("any questions?" → silence).

**Not for:** generating the pre-read packet (use [Journal club packet generation](library.html#/library/pillar-3-educational-operations/prompts/conferences-and-journal-clubs/journal-club-packet)), discussion of methods alone (use [Paper methods critique](library.html#/library/pillar-1-self-education/prompts/paper-methods-critique)), or contexts where you can't ground questions in the actual paper.

## The prompt

```
You are generating 5 discussion questions for journal club. They must escalate from concrete to contested. The fifth question is the test — if it has an obvious right answer in current literature, it's not actually contested.

## What I'm requesting

- **Paper:** [citation or attached PDF]
- **Audience:** [PGY level + faculty mix]
- **Discussion length:** [usually 30-45 min for questions]
- **My role:** [discussion leader / participant prepping]

## Honesty check first

Do you have access to the actual paper text? If not, say so. Questions generated from title alone fabricate methods and findings.

## Generate 5 questions, ordered

### Question 1: Concrete methods question
A specific design choice or analytic approach to scrutinize. Answer should be in the paper.

### Question 2: Finding-level question
How confident should we be in the headline result given the design? Requires interpretation, not just recall.

### Question 3: Generalizability question
Does this apply to our patient population? What specifically about ours would limit applicability?

### Question 4: Practice-change question
Should this change what we do, and if so, in what specific setting for which patients?

### Question 5: Contested question
One that reasonable experts would genuinely disagree on. Should provoke real debate.

## For each question, also provide

- **Question text** (the actual question)
- **What this question opens up** — what discussion thread does it start?
- **The "wrong" or shallow response** likely to come up early and how to redirect

## Hard rules

- **Questions must escalate.** Q1 should be answerable from the paper; Q5 should not have a single right answer.
- **Q5 must be genuinely contested.** Pressure-test: if the answer is obvious to literate experts, it's not Q5.
- **No leading questions** ("Don't you think...?").
- **Each question should be answerable in 5-8 minutes of discussion** — not a thesis topic.

## What I will NOT accept

- All questions at the same abstraction level
- Q5 that has an obvious settled answer
- Leading questions
- Generic questions that could apply to any paper
```

## Expected output

5 questions with productivity notes and predicted-shallow-response handling. Length ~400-600 words.

## Common failure modes

- **All questions at the same level.** Push back: "Question 5 should be more abstract than Question 1."
- **Q5 has an obvious answer.** Push back: "What's something experts disagree on?"

## Required human verification

- Pre-test Q5 with a colleague — if they immediately agree with you, not contested.
- Verify questions are answerable from the actual paper.

## Best model and why

**Claude Sonnet 4.6** — question escalation across abstraction levels is well within Sonnet's range.
