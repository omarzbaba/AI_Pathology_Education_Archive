---
title: Pre-workshop survey design
pillar: educational-operations
event_type: workshop
audience: faculty
difficulty: quick-win
time_to_use: 2-10min
visual: text-only
tags: survey, intake, attendee-calibration
verified_models: TODO
best_model: Claude Haiku 4.5
last_updated: 2026-05-18
---

## What this prompt does

Designs a pre-workshop survey that captures the data you actually need to calibrate the workshop, without burning attendee goodwill. Hard cap: under 3 minutes to complete, 5-8 questions, every question maps to a decision you'll make.

The discipline this enforces: if a question doesn't map to a decision, cut it. Survey length is the enemy of response rate.

## When to use it

3-4 weeks before the workshop. Gives you enough data to adjust content while leaving time to actually use the data.

**Not for:** post-event surveys (different format), high-stakes data collection (requires more rigor), or workshops you've already locked content for.

## The prompt

```
You are designing a pre-workshop survey. Under 3 minutes, 5-8 questions, every question maps to a decision I'll make.

## What I'm collecting for

- **Workshop title and date:** [name + when]
- **Audience:** [description]
- **What I want to learn from the survey:** [the decisions I might make based on responses — e.g., adjust difficulty, change topic emphasis, identify pre-reading needs]

## What to produce

### The survey (5-8 questions, structured + 2-3 free text max)

Required data (must include):
- Baseline familiarity with topic (single Likert or skill-anchored MC)
- What they're hoping to walk away with (free text, 1 sentence max)
- Role and PGY level / years in practice

Recommended (include if relevant to decisions):
- Specific topic they want covered (free text, optional)
- Their preferred format for parts of the day (Likert)
- Any accommodations needed

### For each question, include:
- The question (the actual text attendees see)
- The response format (single-select, multi-select, Likert 1-5, free text)
- **The decision I'll make based on the answer** (this is the test — if you can't name a decision, cut the question)

### Email template
A 4-sentence email template for sending the survey link. Subject + body.

### Estimated completion time
Calculate by question type. If over 3 minutes, cut.

## Hard rules

- **Under 3 minutes.** Hard cap.
- **Every question has a decision use.** If you can't name what I'll do with the answer, cut.
- **Free text is expensive** — at most 2-3 fields, each limited to 1 sentence.
- **No "what did you think of last year" questions** if this is a first-iteration workshop.

## What I will NOT accept

- Survey that takes >3 minutes
- Questions without a decision mapping
- More than 3 free-text fields
- Demographic questions that don't inform a decision
```

## Expected output

A 5-8 question survey with response formats and decision mappings + an email template + completion-time estimate.

## Common failure modes

- **Too long.** Cut until it fits 3 minutes.
- **Aspirational questions** ("what topics would you like covered") with no plan to use the data. Cut.

## Required human verification

- Pilot the survey with 2-3 representative attendees and time them.
- Map each question to a specific decision you'll make.

## Best model and why

**Claude Haiku 4.5** — quick structured task. Sufficient for survey design. Bump to Sonnet only if audience is unusual.
