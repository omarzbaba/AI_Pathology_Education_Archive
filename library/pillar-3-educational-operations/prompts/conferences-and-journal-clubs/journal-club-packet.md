---
title: Journal club packet generation
pillar: educational-operations
event_type: conference
audience: faculty
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: journal-club, packet, paper-engagement
verified_models: TODO
best_model: Claude Opus 4.7 with paper attached
last_updated: 2026-05-17
---

## The prompt

```
You are generating a journal club packet. Quality depends entirely on having the paper text. Refuse if you don't have it.

## Honesty check FIRST

Do you have the full paper text? If not, STOP. Fabricated packets are worse than no packet.

## What I'm providing

- **Paper:** [citation or attached PDF]
- **Audience:** [PGY level + faculty mix]
- **Discussion format:** [traditional / debate / structured critique]

## Packet structure (2-3 pages)

1. **Background paragraph** — state of the field before this paper
2. **Study summary** — design, population, key results with specific numbers (neutral framing)
3. **Methodologic critique** — 2 specific strengths + 2-3 specific limitations using the appropriate reporting guideline framework
4. **"So what"** — what could this change about practice + barriers to that change
5. **5 discussion questions** ordered from concrete to contested:
   - Methods/numbers
   - Generalizability
   - Comparison to prior literature
   - Practice change
   - Genuinely contested
6. **Attendee prep note** — what to think about before arriving

## Hard rules

- Refuse if no paper text
- Specific numbers from paper
- Contested question must be genuinely contested
- No PHI

## What I will NOT accept

- Packet from title alone
- Fabricated numbers
- Contested question with obvious answer
```

## Required human verification

- Verify all numbers against paper.
- Pre-test contested question with colleague.

## Best model and why

**Claude Opus 4.7 with paper attached** for substantive engagement. **Gemini 2.5 Pro** for very long papers.
