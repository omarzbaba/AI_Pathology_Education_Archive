---
title: Pre-workshop survey design
pillar: educational-operations
event_type: workshop
audience: faculty
difficulty: quick-win
time_to_use: 2-10min
visual: text-only
tags: survey, intake
verified_models: TODO
best_model: Claude Haiku 4.5
last_updated: 2026-05-17
---

## What this prompt does

Design a short pre-workshop survey that captures attendee level, expectations, and content preferences without burning their goodwill.

## When to use it

3-4 weeks before the workshop, when you want enough data to calibrate content but not so much that response rate craters.

## The prompt

```
Design a pre-workshop survey for [workshop title]. Audience: [audience description].

The survey should:

1. Take **under 3 minutes** to complete. Hard cap.
2. Include 5-8 questions total.
3. Capture the data I actually need to calibrate the workshop, not nice-to-haves.

Required data:
- Their baseline familiarity with the topic (single Likert or skill-anchored multiple choice).
- What they're hoping to walk away with (free text, max 1 sentence).
- Their role and PGY/years in practice.
- Any specific topic they want covered (free text, optional).

Format each question with:
- The question itself.
- The response format (single-select, multi-select, Likert 1-5, free text).
- Why the question is in the survey (what decision will I make with the answer?).

End with a one-sentence email template for sending the survey link.

**Important — refinement:** After generating the survey, estimate the actual completion time at a normal reading pace. If it exceeds 3 minutes, cut a question. Optimize for response rate.
```

## Expected output

A 5-8 question survey with response formats and explicit rationale for each question. Plus an email template.

## Common failure modes

- Survey is too long; response rate will be poor.
- Questions don't actually inform decisions you'll make.
- Free text fields are too open and produce unanalyzable results.

## Required human verification

- Pilot-test the survey with 2-3 representative attendees and time them. Adjust if it takes more than 3 minutes.
- Map each question to a specific decision you'll make based on the result. If you can't map a question to a decision, cut it.

## Best model and why

**Claude Haiku 4.5** — Survey design is a quick structured task. Haiku is fast and sufficient. Bump to Sonnet only if the audience is unusual or you need novel question types.
