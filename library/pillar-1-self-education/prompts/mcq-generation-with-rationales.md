---
title: MCQ generation with rationales
pillar: self-education
event_type: n/a
audience: resident
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: mcq, board-prep, question-writing
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Generates board-style MCQs with detailed rationales for **every** answer choice — not just the correct one. The rationales for incorrect choices are the highest-yield learning, because they teach the cognitive moves that distinguish strong test-takers from weak ones.

The prompt is designed to produce questions that test *application and analysis*, not memorization, and that have *plausible* distractors rather than throwaways.

## When to use it

After studying a topic, to actively retrieve and stress-test what you've learned. Also useful for building a personal review bank organized by topic. Best with the [Question bank gap analysis](library.html#/library/pillar-1-self-education/prompts/question-bank-gap-analysis) prompt — generate questions on your weak topics, then track which ones you miss.

**Not for:** replacing a real qbank for board prep (real qbanks have psychometric validation; AI-generated questions don't), questions for formal assessment (use validated items), or topics where you don't yet have foundational knowledge (read first, then drill).

## The prompt

```
You are a board-style MCQ writer for pathology residents. Generate questions that test reasoning, not retrieval. The rationales for incorrect answers are the highest-yield part of your output — write them like a teacher explaining the cognitive trap each distractor represents.

## What I'm requesting

- **Topic:** [be specific — e.g., "interpretation of the indirect antiglobulin test (IAT) in blood bank crossmatch", not just "blood bank"]
- **Number of questions:** [e.g., 5]
- **Target level:** [e.g., "PGY-2 in their first month of blood bank", or "RISE exam", "AP/CP boards", "ABPath in-service"]
- **Question style:** [e.g., "USMLE-style clinical vignette" or "compressed stem with lab values only"]

## Format for each question

```
Question N:
[Vignette of 2-5 sentences — clinical or laboratory context, ending in a clear question]

A. [Choice]
B. [Choice]
C. [Choice]
D. [Choice]
E. [Choice]

---

ANSWER: [Letter]

RATIONALE FOR EACH CHOICE:

A. [Why this is correct OR what specific misunderstanding makes a resident pick this incorrectly. Be specific about the cognitive error.]
B. [Same.]
C. [Same.]
D. [Same.]
E. [Same.]

TEACHING POINT (1-2 sentences): The single most important concept this question tests.
```

## Hard rules

- **Vignettes must include enough clinical context to reason from.** A bare question is not a board-style MCQ.
- **Distractors must be plausible to someone with partial knowledge.** "Obviously wrong" distractors are throwaways. Each distractor should represent a specific cognitive error a real resident would make.
- **Distractor rationales must be SUBSTANTIVE.** "This is incorrect because A is correct" is not a rationale. Say WHAT misunderstanding leads to picking that answer.
- **Calibrate to the stated level.** PGY-2 questions should not require fellowship-level knowledge; board questions should not be trivially easy.
- **DO NOT reproduce or closely paraphrase real published board questions.** If the topic is so narrow that you can't generate original questions safely, tell me — do not invent.
- **One unambiguous best answer.** If two answers could be defensible, the question is broken.

## What I will NOT accept

- Distractors that are clearly wrong on inspection
- "This is incorrect because the correct answer is A" non-rationales
- Vignettes that are decorative (clinical context that doesn't actually inform the question)
- Questions where the correct answer is in the longest choice (a classic test-writing tell)
- Questions that test memorization of a single fact dressed up as a vignette
```

## Expected output

The requested number of questions in the format above, each with five plausible answer choices, full per-choice rationales, and a one-line teaching point. Total length scales with number of questions — usually ~250-350 words per question.

## Common failure modes

- **Obvious throwaway distractors.** Push back: "Distractor C is obviously wrong. Replace it with something that represents an actual misconception."
- **Pseudo-rationales.** Push back: "Your rationale for choice B doesn't say WHY someone would pick it. Explain the cognitive error."
- **Application questions that actually test recall.** Push back: "Could a resident who memorized facts answer this without reasoning? If yes, it's not application."
- **Vignettes that don't add value.** Push back: "Strip the vignette — does the question still make sense? If yes, your vignette is decorative."

## Required human verification

- **Verify the correct answer against an authoritative source** every single time. AI-generated MCQs frequently have plausible-looking-but-wrong correct answers, especially for nuanced topics. The rationales sound convincing for both the right and the wrong answer, which is the failure mode that matters most.
- **Verify the distractor rationales.** A confidently-wrong distractor rationale teaches the wrong concept.
- **For any specific value cited** (cutoff, threshold, dose), verify against current guideline.
- **Show one question to a colleague who knows the topic** — if they spot a flaw you missed, the question needs more work.

## Best model and why

**Claude Opus 4.7** — generating plausible distractors and substantive wrong-answer rationales is where Opus materially outperforms Sonnet. Sonnet rationales tend toward formulaic; Opus produces rationales that read like a teacher explaining the trap. For high-stakes use (formal assessment, board prep banks), use Opus. For quick review questions during a study session, Sonnet is sufficient.
