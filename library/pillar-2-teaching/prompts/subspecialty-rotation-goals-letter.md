---
title: Sub-specialty rotation goals letter
pillar: teaching
event_type: rotation
audience: resident
difficulty: quick-win
time_to_use: 2-10min
visual: text-only
tags: rotation, goal-setting, communication
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Drafts the "here's what I'd like to get out of this rotation" letter or email that a resident sends to their incoming rotation director a week or two before the rotation starts. Signals intent, sets expectations, and gives the rotation director something to plan around. The letter is short (under 200 words) but does real work.

This is an under-used communication move — most residents arrive on day 1 with no advance signal of what they want from the rotation. The letter changes that.

## When to use it

1-2 weeks before a rotation starts, when you want to arrive with a clear sense of what you're hoping to get out of it. Especially valuable for elective rotations and sub-specialty rotations where the attending has discretion about what to teach.

**Not for:** rotations where you've been assigned a strict curriculum (less leverage), as a substitute for an in-person orientation conversation, or for rotations where you don't actually have a clear sense of what you want.

## The prompt

```
You are drafting a short letter or email I will send to my incoming rotation director. Goal: signal intent, set realistic expectations, give them something to plan around. Tone: warm, specific, professional. Length: under 200 words.

## What I'm telling them

- **Rotation:** [name and dates]
- **My level:** [PGY level + subspecialty trajectory if relevant]
- **What I'd like to get out of this rotation:** [the 2-3 specific goals — e.g., "I'm going into hematopathology and want maximum exposure to flow cytometry interpretation"]
- **What I've already done that's relevant:** [optional — courses, prior rotations, projects]
- **What I'm flexible about / would defer to your judgment on:** [showing I'm not over-prescriptive]
- **Specific asks (if any):** [optional — e.g., "if possible, I'd love to attend at least one molecular sign-out"]
- **The rotation director's name and how I should address them:** [name + Dr./first name based on their preference]

## Letter structure (under 200 words)

1. **Greeting + acknowledgment of the upcoming rotation** (1 sentence)
2. **A short statement of who I am and why I'm excited about this rotation** (2-3 sentences) — specific, not gushing
3. **The 2-3 specific goals**, framed as "I'd be most grateful for opportunities to..." (3-4 sentences)
4. **A line acknowledging your flexibility** ("happy to defer to your judgment on what's possible given the case mix")
5. **A specific offer** (something I can bring — preparation, a topic I can present, willingness to come in early for sign-out)
6. **Close** (looking forward to learning, formal sign-off)

## Hard rules

- Under 200 words. Hard cap.
- Specific goals, not "I want to learn a lot"
- Tone that's confident without being entitled
- An offer of something I bring, not just a list of asks
- No empty intensifiers ("excited", "thrilled", "honored" — pick one and use sparingly)

## What I will NOT accept

- A letter over 200 words
- Generic goals
- All asks, no offers
- Tone that's either obsequious or presumptuous
```

## Expected output

A short, structured letter or email under 200 words. Should read like a thoughtful resident wrote it in 5 minutes, not like AI generated it.

## Common failure modes

- **Over-length.** Push back: "Cut it to 180 words."
- **Generic goals.** Push back: "What specifically?"
- **No offer.** Push back: "What do I bring?"

## Required human verification

- Read aloud — does it sound like you? If not, rewrite.
- Check the rotation director's preferred mode of address (some prefer first name, some Dr.).
- Send 1-2 weeks ahead, not 1-2 days. The point is to give them time to plan.

## Best model and why

**Claude Sonnet 4.6** — short professional correspondence is Sonnet's strength. Opus would over-elaborate; Haiku might miss the tone calibration.
