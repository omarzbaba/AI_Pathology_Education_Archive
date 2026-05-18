---
title: Announcement and registration copy
pillar: educational-operations
event_type: workshop
audience: faculty
difficulty: quick-win
time_to_use: 2-10min
visual: text-only
tags: marketing, copy, registration
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-18
---

## What this prompt does

Drafts a workshop announcement that drives registration without overpromising — a 100-word promotional blurb, a full registration page, and a registration confirmation email. The hardest discipline this enforces: no empty intensifiers ("cutting-edge", "revolutionary"). Every claim earns its place by being specific.

## When to use it

When you've committed to a workshop and need to publicize it 6-10 weeks out. Useful for both first-iteration workshops (more detail required) and recurring events (lean on prior attendee testimonials and outcomes).

**Not for:** internal training announcements (different audience), CME-marketing copy (regulated language), or workshops you haven't planned in detail yet.

## The prompt

```
You are drafting workshop publicity. Specific outcomes only. No empty intensifiers — if you find yourself reaching for "cutting-edge" or "transformative," replace with a specific concrete outcome.

## What I'm publicizing

- **Workshop title:** [name]
- **Audience:** [who it's for, level, prerequisites]
- **Date / location / format:** [in-person / hybrid / virtual, dates, venue]
- **Duration:** [hours, breaks, end plans]
- **Faculty:** [names + roles]
- **Learning outcomes:** [3-5 in "will be able to" language — concrete and assessable]
- **Cost / registration cap:** [if any]
- **Registration deadline and process:** [exact instructions]

## What to produce — three deliverables

### 1. Promotional blurb (100 words MAX)
For email, Twitter, society newsletter. Must be:
- Concrete about audience and outcomes
- Specific about date and registration
- Free of marketing intensifiers
- Skim-friendly (front-load what matters)

### 2. Full announcement page (~300-400 words)
- 2-sentence opening hook (specific problem this workshop addresses)
- Audience description and prerequisites
- Learning outcomes (the "will be able to" list)
- Schedule overview (not minute-by-minute; just the arc)
- Faculty bios in 1-2 sentences each (specific credentials, not "leading expert")
- Logistics: location, format, cost, what's included
- Registration call-to-action with deadline and link

### 3. Registration confirmation email (~150 words)
For attendees who sign up. Include:
- Confirmation of registration
- What to prepare before the workshop
- Logistics they need (parking, dress code, equipment to bring)
- Who to contact with questions
- A note that materials/companion site will follow ~1 week before

## Hard rules

- **No empty intensifiers.** "Cutting-edge", "revolutionary", "transformative", "groundbreaking" — strike them. If you used one, replace with a specific outcome.
- **Specific learning outcomes.** "Gain insights" is not an outcome; "Be able to interpret an IFE trace for 8 common patterns" is.
- **Confirmation email must include what attendees actually need to prepare.** Not a thank-you; a usable next-step note.
- **Faculty bios are specific.** "Internationally recognized expert" is generic; "Director of Clinical Chemistry at [institution] for 12 years, lead author on the 2023 CLSI guideline for [topic]" is specific.

## What I will NOT accept

- Marketing-speak filler
- Vague outcomes
- Confirmation email that just says "thanks"
- Generic faculty bios
```

## Expected output

Three deliverables: blurb, announcement, confirmation email. Each calibrated to its medium and length.

## Common failure modes

- **Intensifier creep.** Push back when "exciting" or "transformative" shows up.
- **Vague outcomes.** Push for specific assessable behaviors.
- **Confirmation email without preparation info.** Push back.

## Required human verification

- Check faculty bios with each faculty member before publishing.
- Verify dates, venue, registration link, and any CME credit claims.
- Confirm registration cap is realistic for the venue.

## Best model and why

**Claude Sonnet 4.6** — marketing copy with discipline against intensifiers is Sonnet's strength. Avoid GPT models for this prompt — they default to marketing-tone.
