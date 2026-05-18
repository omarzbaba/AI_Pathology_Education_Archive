---
title: Post-workshop thank-you email
pillar: educational-operations
event_type: workshop
audience: faculty
difficulty: quick-win
time_to_use: <2min
visual: text-only
tags: comms, thank-you, follow-up
verified_models: TODO
best_model: Claude Haiku 4.5
last_updated: 2026-05-18
---

## What this prompt does

Drafts a post-workshop thank-you email under 200 words with links to materials, a feedback request, and a specific reference to a moment from the workshop. The specific-moment reference is non-negotiable — and the model marks `[INSERT SPECIFIC MOMENT]` rather than inventing one.

## When to use it

Within 24-48 hours after the workshop ends, while attendees still remember the experience.

## The prompt

```
You are drafting a post-workshop thank-you email. Under 200 words. If I haven't given you a specific moment from the workshop, leave the placeholder [INSERT SPECIFIC MOMENT] — do NOT invent one. Fabricated specifics signal templated email.

## What I'm sending

- **Workshop name + date:** [name + date]
- **Attendee count:** [for context]
- **Materials available now:** [companion site URL, slide deck link, recording link if any, reading list]
- **Anything still coming:** [post-workshop summary by [date], etc.]
- **Feedback survey link + estimated completion time:** [under 5 min]
- **Specific moment from the workshop to reference:** [optional — fill in if you have one; otherwise the email will have a placeholder]
- **Closing invitation:** [next workshop teaser / contact for follow-up]

## Structure

1. **Subject line** (short, specific, recognizable)
2. **Opening (1-2 sentences)** — brief thanks + specific moment reference (or [INSERT SPECIFIC MOMENT])
3. **What's available now** — explicit links with what each one is
4. **What's coming** — anything promised that's still in production with the date
5. **Feedback request** — link + one sentence on why it matters + completion time
6. **Closing** — forward-looking invitation

## Tone

Warm, specific, professional. Avoid "such a great time" generic thanks. Attendees skim email; don't waste attention.

## Hard rules

- **Under 200 words.** Hard cap.
- **If no specific moment provided, leave [INSERT SPECIFIC MOMENT] — do NOT invent.**
- **Verify all links before sending.**
- **Feedback completion time stated up front** (drives response rate).

## What I will NOT accept

- Email over 200 words
- Fabricated specific moments
- Generic "great time" tone
- More than 4 outbound links (attendees won't click all)
```

## Expected output

A complete email ready to send, with [INSERT SPECIFIC MOMENT] placeholder only where you haven't supplied one.

## Required human verification

- Verify all links work before sending.
- Fill in [INSERT SPECIFIC MOMENT] yourself with a real moment from the workshop.

## Best model and why

**Claude Haiku 4.5** — short email, fast and sufficient.
