---
title: Faculty feedback summary email
pillar: educational-operations
event_type: workshop
audience: faculty
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: feedback, debrief, themes
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Converts raw attendee feedback into a faculty debrief email organized by theme, ordered by frequency, with honest separation of signal vs noise and ranked suggested actions.

## When to use it

1-2 weeks after the event, when feedback has come in but faculty are still engaged enough to act on it.

**Not for:** real-time feedback during the event, individual feedback to a specific faculty member (different conversation), or contexts where faculty don't want the unvarnished read.

## The prompt

```
You are converting raw attendee feedback into a faculty debrief email. Be honest about negative themes; don't minimize. Anonymize quotes.

## What I'm providing

- **Event and date:** [name + when]
- **Raw feedback:** [paste survey responses, exit tickets, post-event comments]
- **Response rate:** [N respondents out of M attendees]
- **Audience to send debrief to:** [all faculty involved / leadership only / etc.]

## Structure

### 1. One-paragraph summary
Overall reception, response rate, top-level themes (positive AND negative).

### 2. What worked (themes, ordered by frequency)
Paraphrased example quotes (preserving anonymity).

### 3. What didn't work (themes, ordered by frequency)
Same structure as #2. Do NOT minimize.

### 4. Signal vs noise
Which comments represent systemic issues vs one-off complaints. Be honest about both — but don't dismiss minority voices that point to real issues.

### 5. Suggested actions for next iteration
3-5 specific changes, ranked by ease × impact.

### 6. Response rate and selection bias note
Who responded, who didn't, what that means for interpretation.

## Hard rules

- **Quote anonymity.** If a quote could identify the respondent (small group, distinctive phrasing), paraphrase further.
- **Do NOT embellish quotes.** That erodes faculty trust.
- **Do NOT minimize negative themes.** Selective reporting is detected.
- **Actions must be specific.** Generic "improve communication" is not actionable.

## What I will NOT accept

- Selective reporting favoring positive feedback
- Embellished or smoothed quotes
- Actions without owners or specifics
- Quotes that could identify respondents
```

## Expected output

A debrief email with 6 sections, paraphrased quotes preserving anonymity, ranked actions.

## Common failure modes

- **Positive bias.** Push back: "Did I miss negative themes?"
- **Quote embellishment.** Verify against raw text.
- **Aspirational actions.** Push for specifics.

## Required human verification

- Re-read against raw feedback — confirm negative themes preserved.
- Anonymize ALL quotes — including paraphrased versions.
- Run by one trusted faculty member before sending widely.

## Best model and why

**Claude Opus 4.7** — theme synthesis from raw feedback rewards depth. Opus is better at signal-vs-noise distinction.
