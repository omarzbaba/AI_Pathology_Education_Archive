---
title: Q&A preparation document
pillar: educational-operations
event_type: conference
audience: faculty
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: qa, prep
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Generate a Q&A preparation document anticipating audience questions and providing concise, evidence-backed responses.

## When to use it

The day before any presentation where the Q&A is high-stakes — board meeting, departmental presentation, conference talk, grant defense.

## The prompt

```
Help me prepare for the Q&A portion of [presentation title], on [date]. The audience is [audience description].

Generate a Q&A prep document organized as:

1. **The 5-10 questions most likely to come up**, ranked by likelihood. For each:
   - The question (phrased as I'd actually hear it).
   - The questioner's likely angle (technical objection, clinical concern, scope question, etc.).
   - A 2-3 sentence response, evidence-backed.
   - The follow-up question I should anticipate.
   - Any pre-prepared data, citation, or slide I should have ready.

2. **The 2 hardest questions**: the ones I'd dread getting. Spend more time on these. Acknowledge if I genuinely don't have a good answer; suggest how to respond honestly while preserving credibility.

3. **The 1 question I cannot answer**: if there's a question with no good answer (e.g., results not yet available), draft a response that doesn't dodge but acknowledges the gap.

4. **Time management**: how long to spend per answer to leave time for multiple questions. What to do if Q&A runs short or long.

5. **Body and voice**: where to look, how to handle hostile questioners, how to redirect off-topic questions.

End with: the one question I should hope someone asks, because it lets me make my strongest point.

**Important — refinement:** The 'hardest questions' should be genuinely hard, not softballs disguised as challenges. If you can answer one of your own 'hard' questions easily, escalate the difficulty. The 2 hardest questions are the most valuable part of this document.
```

## Expected output

A prep document I can study the night before. Length: 3-5 pages. Should reduce surprise during actual Q&A.

## Common failure modes

- The 'hardest questions' are softball.
- 'I cannot answer' responses dodge rather than acknowledge.
- Time management guidance is generic.

## Required human verification

- Have a colleague pose the anticipated questions to you and rate your responses. The questions you flail on need more prep.
- Verify any data, citations, or numbers you plan to reference.
- The 'one question I hope someone asks' should actually be a question someone might ask, not a planted one that would be obvious.

## Best model and why

**Claude Opus 4.7** — Anticipating sophisticated hostile or content-expert questions requires depth and a kind of mental adversarialism. Opus is materially better than Sonnet at the 'hardest questions' section.
