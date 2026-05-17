---
title: Post-workshop thank-you email
pillar: educational-operations
event_type: workshop
audience: faculty
difficulty: quick-win
time_to_use: <2min
visual: text-only
tags: comms, thank-you
verified_models: TODO
best_model: Claude Haiku 4.5
last_updated: 2026-05-17
---

## What this prompt does

Draft a post-workshop thank-you email to attendees with a link to the companion materials and a feedback request.

## When to use it

Within 24-48 hours after the workshop ends, while attendees still remember the experience.

## The prompt

```
Draft a post-workshop thank-you email to attendees of [workshop name] held on [date].

The email should:

1. **Subject line** (short, specific, recognizable in a busy inbox).
2. **Opening** (1-2 sentences): brief thanks and a specific reference to a moment from the workshop (you'll need to fill this in with the actual moment).
3. **What's available now**: links to the companion materials site, slides, recordings (if any), reading list — be explicit about what each link goes to.
4. **What's coming**: anything you've promised that's still in production (e.g., 'we'll share the post-workshop summary by [date]').
5. **Feedback request**: link to the survey, with a one-sentence explanation of why their feedback matters (this affects response rate). 5 minutes max.
6. **Closing**: a forward-looking invitation (next workshop, contact for follow-up questions).

Tone: warm, specific, professional. Avoid 'we had such a great time' generic thanks.

Length: under 200 words. Attendees skim email; don't waste their attention.

**Important — refinement:** If I haven't given you a specific moment from the workshop to reference, leave the placeholder `[INSERT SPECIFIC MOMENT]` rather than inventing one. A fabricated reference signals to attendees that the email is templated.
```

## Expected output

A complete email ready to send, with placeholders only for the specific 'moment from the workshop' line.

## Common failure modes

- Generic 'thanks for attending' tone that signals you didn't actually pay attention.
- Too many links — attendees won't click any.
- Feedback survey buried.

## Required human verification

- Verify all links work before sending.
- The specific 'moment' line has to come from you — the model doesn't know what happened in the room.

## Best model and why

**Claude Haiku 4.5** — Short email under 200 words — Haiku is fast and sufficient. The specific moment from the workshop has to come from you regardless.
