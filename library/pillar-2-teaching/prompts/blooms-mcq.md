---
title: Bloom's taxonomy MCQ generation
pillar: teaching
event_type: n/a
audience: faculty
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: mcq, assessment, blooms, cognitive-level
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Generates MCQs at specified Bloom's taxonomy levels — Application, Analysis, Evaluation — with rationales calibrated to the cognitive task each question tests. Avoids the default failure mode of disguising Recall as Application by adding a clinical vignette to a recall question.

## When to use it

When building formative or summative assessment items that test reasoning rather than memorization. Especially useful when designing assessments that need to demonstrate cognitive level discrimination (CCC documentation, milestone-aligned exams).

**Not for:** quick review questions (use [MCQ generation with rationales](library.html#/library/pillar-1-self-education/prompts/mcq-generation-with-rationales)), questions for board exam prep where you want a mix that matches real board distribution, or formal assessment items that need psychometric validation.

## The prompt

```
You are generating MCQs across Bloom's taxonomy levels. Discipline test: a question that can be answered by retrieving a memorized fact is Recall, regardless of how clinical-looking the vignette is. Be honest about cognitive level.

## What I'm generating

- **Topic:** [be specific]
- **Audience level:** [PGY level + subspecialty rotation context]
- **Number of questions:** [N]
- **Distribution across Bloom's levels:**
  - **Application:** [X%] — use knowledge in a new situation (typical clinical vignette)
  - **Analysis:** [Y%] — distinguish, compare, organize (requires breaking down a complex case)
  - **Evaluation:** [Z%] — justify a decision based on criteria (requires choosing among multiple acceptable approaches)

Avoid Remember/Understand level questions — they don't test what residents actually need.

## For each question, produce

```
Question N (Bloom's level: [Application / Analysis / Evaluation]):

[Vignette — clinical or laboratory context]

A. [Choice]
B. [Choice]
C. [Choice]
D. [Choice]
E. [Choice]

---

ANSWER: [Letter]

LEVEL JUSTIFICATION: [Name the specific cognitive task this question requires. What does the resident have to DO to answer this — not just remember, but DO?]

RATIONALES:
A. [Why correct OR what cognitive shortcut leads to this wrong answer]
B. [Same]
C. [Same]
D. [Same]
E. [Same]

TEACHING POINT (1 sentence): The cognitive skill this question is assessing.
```

## Hard rules — the discipline tests

- **Discipline test #1: Can a resident answer this by retrieving a memorized fact?** If yes, it's Recall, not Application. Mark it as Recall and offer to escalate.
- **Discipline test #2: For Application, does the resident need to apply the concept in a NEW situation,** not just identify which textbook entity matches the vignette? If they're matching, it's still Recall.
- **Discipline test #3: For Analysis, must the resident BREAK DOWN a complex scenario** into discriminating components? If they're just identifying the right answer, it's Application or below.
- **Discipline test #4: For Evaluation, must the resident JUSTIFY a choice among multiple defensible options?** If there's only one right answer with the rest being clearly wrong, it's not Evaluation.
- **Source any specific value cited** in the question or rationales.
- **Distractors must be plausible** — represent real cognitive errors, not throwaways.

## What I will NOT accept

- "Application" questions that are recall dressed in a vignette
- Distractors that are obviously wrong
- "Evaluation" questions with one right answer and four obviously wrong ones
- Level justifications that are vague ("requires higher-order thinking")
```

## Expected output

N questions with verified Bloom's level, level justification, full rationales, and teaching point. Typically 300-450 words per question.

## Common failure modes

- **Recall mislabeled as Application.** The dominant failure mode. Push back: "A resident who memorized [fact] could answer this without applying anything. This is Recall."
- **Evaluation questions with one obvious answer.** Push back: "All five answers should be defensible to some degree. What's wrong with each that makes the chosen one best?"
- **Generic level justifications.** Push back: "Name the specific cognitive task."

## Required human verification

- Verify the correct answer against an authoritative source.
- Pressure-test the Bloom's level: would a memorizer answer it correctly without reasoning? If yes, the level is over-stated.
- Have a colleague who teaches this topic review the question and the level designation before formal use.

## Best model and why

**Claude Opus 4.7** — Bloom's level calibration is genuinely difficult; Sonnet often mis-labels questions. Opus is more disciplined about identifying when a clinical vignette is just dressing for a recall question.
