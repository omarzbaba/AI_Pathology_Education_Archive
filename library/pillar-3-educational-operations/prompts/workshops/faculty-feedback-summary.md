---
title: Faculty feedback summary email
pillar: educational-operations
event_type: workshop
audience: faculty
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: comms, debrief
verified_models: TODO
last_updated: 2026-05-17
---

## What this prompt does

Convert raw feedback comments into a summary email to faculty, themed by issue and ordered by frequency, with suggested actions.

## When to use it

1-2 weeks after the workshop, when feedback is in but faculty are still close enough to the event to engage with it.

## The prompt

```
Convert the following raw attendee feedback into a faculty debrief email.

Raw feedback: [paste the feedback comments — could be from a survey, exit ticket, or post-event responses]

Structure the debrief:

1. **One-paragraph summary**: overall reception, response rate, top-level themes.
2. **What worked** (themes that came up positively, ordered by frequency, with example quotes — paraphrased to preserve anonymity if needed).
3. **What didn't work** (themes that came up negatively, ordered by frequency, with example quotes).
4. **The signal vs the noise**: which comments represent systemic issues vs one-off complaints. Be honest with faculty about both.
5. **Suggested actions for the next iteration**: 3-5 specific changes, ranked by ease × impact.
6. **A note on response rate and selection bias**: who responded and who didn't, and what that means for interpreting the data.

Tone: data-forward, no defensiveness, no minimization of critical feedback. Faculty trust this kind of debrief when it's honest.
```

## Expected output

A debrief email with all six sections, paraphrased quotes for anonymity, and ranked suggested actions.

## Common failure modes

- Selective reporting that favors positive feedback.
- Quotes that could identify individual respondents.
- Suggested actions are aspirational rather than operational.

## Required human verification

- Re-read against the raw feedback — confirm you haven't omitted significant negative themes.
- Anonymize all quotes — even paraphrased, check that no quote could be traced to a specific person.
- Run the debrief past one trusted faculty member before sending to the wider group.
