---
title: Source-grounded MCQ generation
pillar: self-education
event_type: n/a
audience: resident
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: source-grounded, mcq, board-prep
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-18
---

## What this prompt does

The source-grounded version of [MCQ generation with rationales](library.html#/library/pillar-1-self-education/prompts/mcq-generation-with-rationales). Generates board-style MCQs from YOUR uploaded study materials, with every answer's correctness traceable to a specific source passage. Useful when you want to test against material you've actually been reading.

## When to use it

Inside a board prep notebook when you want practice questions calibrated to YOUR specific source material rather than generic board questions. Note: AI-generated MCQs are study tools, not validated assessment items — use real qbanks for serious prep.

## The prompt

```
You are generating MCQs from the sources uploaded to this notebook. Every
question's answer must trace to a specific uploaded source passage. If you
cannot generate a question from the sources on a topic, say so rather than
inventing.

## What I'm requesting

- **Topic from the corpus:** [be specific — e.g., "diagnostic workup of
  isolated prolonged aPTT"]
- **Number of questions:** [usually 3-5 for a focused drill]
- **Target level:** [PGY level / board level]
- **Question style:** [clinical vignette / lab values only / mixed]

## Format for each question

```
Question N (sourced from: [Source filename or title, section if applicable]):

[Vignette]

A. [Choice]
B. [Choice]
C. [Choice]
D. [Choice]
E. [Choice]

---

ANSWER: [Letter]

SOURCE PASSAGE FOR THE ANSWER:
[Quote or paraphrase the specific passage in the uploaded source that
contains the answer]

RATIONALES FOR EACH CHOICE:
A. [Why correct OR what misunderstanding leads here, with source citation
where relevant]
B. [Same]
C. [Same]
D. [Same]
E. [Same]

TEACHING POINT: The cognitive skill or content this question tests.
```

## Source-grounding rules

- **Every question must trace to specific uploaded source content.**
- **The "correct" answer must be VERIFIABLY in the source** — not interpolated
  from the source.
- **Distractor rationales should reflect actual misconceptions** the source
  addresses, where possible.
- **If you cannot generate a good MCQ from the sources on a topic,** tell me
  the corpus is thin on that topic rather than inventing.

## What I will NOT accept

- "Correct" answers that aren't actually in the uploaded source
- Citations to source passages that don't contain the claim
- Questions whose answers come from general knowledge dressed up as
  source-grounded
- Distractor rationales that are obviously implausible
```

## Expected output

N MCQs with verifiable source citations, vignette, choices, sourced answer, sourced rationales, teaching point.

## Common failure modes

- **Confabulated source passages.** The model claims the answer is in Section X but Section X doesn't contain it. Verify spot-checks.
- **"Source-grounded" questions that are really general-knowledge** dressed up. The vignette and choices are generic; only the citation is sourced.
- **Distractor rationales that don't trace to anything** (made-up misconceptions).

## Required human verification

- **VERIFY EVERY CORRECT ANSWER against the cited source passage.** The model's confidence about correctness should not be trusted.
- **For high-stakes use** (sharing with co-residents, using for formal assessment), 100% verification — not just spot-checks.
- **Remember these are study aids, not psychometrically validated questions.** Real qbanks for real board prep.

## Best model and why

**Claude Opus 4.7 via Claude Projects** — distractor generation with substantive rationales benefits from Opus's depth. **NotebookLM** for tighter source-citation linkage but weaker distractor quality.
