---
title: Audience poll question generation
pillar: teaching
event_type: n/a
audience: faculty
difficulty: quick-win
time_to_use: <2min
visual: text-only
tags: polls, audience-engagement, live-teaching
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Generates audience poll questions for a live talk — designed for engagement and misconception-surfacing, not assessment. Each poll has a "wrong" answer that most of the audience will pick (by design — that's where the teaching beat is), with notes on what to say at each likely audience distribution.

The discipline this enforces: a poll where everyone gets it right immediately is a failed poll.

## When to use it

When you're delivering a 30-60 minute talk and want 2-3 polling moments to break the lecture rhythm and surface misconceptions. Pairs well with the slide outline prompt.

**Not for:** assessment questions (use MCQ generator), polls in workshops (different format and audience dynamics), or audiences who won't engage with polls (read the room first).

## The prompt

```
You are generating audience poll questions for a live talk. These are teaching moments, not assessments. A poll where everyone gets it right immediately is a failed poll — the wrong answer must be plausibly attractive.

## What I'm building

- **Talk topic and duration:** [e.g., "approach to monoclonal gammopathy, 45 min"]
- **Audience:** [PGY level / faculty / mixed — calibrates difficulty]
- **Number of polls:** [usually 2-3]
- **Where in the talk you want them:** [optional — e.g., "after the diagnosis section, before treatment"]

## For each poll, produce

1. **The question** — short stem, ideally 3 answer choices (not 5). Should be answerable in 30-60 seconds.
2. **Answer choices** with the correct answer marked
3. **The "intended wrong answer"** — the answer most of the audience will pick. This is the teaching opportunity.
4. **Why residents pick the wrong answer** — the specific misconception or cognitive shortcut.
5. **Predicted audience distribution** (e.g., "30% correct, 50% intended wrong, 20% other")
6. **Suggested placement in the talk** — where it serves as a transition or misconception-surfacing moment
7. **What to say at each likely result:**
   - "If 60% pick the intended wrong answer..." → your teaching response
   - "If they all get it right..." → your pivot (still useful, just shorter)
   - "If they split..." → your acknowledgment

## Hard rules

- **Each poll must have a "wrong" answer that's plausibly attractive.** No obvious throwaways.
- **The teaching response — what to say after the poll — is non-negotiable.** Without it, the poll lands flat.
- **Don't over-poll.** 2-3 polls in a 45-min talk is right; more becomes a quiz show.
- **Specific placement.** "Use this poll somewhere in the talk" is not specific.

## What I will NOT accept

- Polls with obvious right answers
- "Suggested wrong" that no one would actually pick
- No teaching response for the most likely audience distribution
```

## Expected output

N polls with all 7 elements. Total ~500-800 words for 3 polls.

## Common failure modes

- **Obvious right answer.** Push back: "Make the wrong answer more attractive."
- **Generic teaching responses.** Push back for specific.

## Required human verification

- Pre-test the poll with a colleague at the target audience level — if they get the intended-wrong answer right cold, the poll won't work.
- Verify the correct answer.

## Best model and why

**Claude Sonnet 4.6** — poll generation with predicted distributions is well within Sonnet's range. The discipline (plausibly-wrong answer) matters more than model depth.
