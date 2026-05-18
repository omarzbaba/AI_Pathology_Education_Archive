---
title: Visiting professor invitation letter
pillar: educational-operations
event_type: conference
audience: faculty
difficulty: quick-win
time_to_use: 2-10min
visual: text-only
tags: visiting-professor, invitation, hospitality
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Drafts the formal invitation letter to a visiting professor for a grand rounds talk or visiting professorship. Substantive enough that the invitee takes it seriously, gracious enough that the relationship starts well, specific enough that they understand exactly what's being asked.

## When to use it

When you're hosting a visiting professor or grand rounds speaker and need to send the formal invitation 3-6 months ahead. Useful both for first-time invitations and for invitations to people you know well (different tone for each).

**Not for:** casual speaker requests (use a short email), CME-accredited industry-funded events (those have specific compliance requirements), or follow-up communications.

## The prompt

```
You are drafting an invitation letter to a visiting professor. Substantive but not effusive. Specific enough that they know exactly what's being asked.

## What I'm inviting

- **Speaker:** [name, current title and institution]
- **Relationship to invitee:** [I don't know them / met at a conference / mentor relationship / longstanding colleague]
- **Event:** [grand rounds / visiting professorship / named lecture / conference keynote]
- **Date and location:** [specific date, my institution]
- **Honorarium and travel:** [what's offered]
- **Format:** [1-hour grand rounds / half-day visit / full-day visit with multiple activities]
- **Why this speaker specifically:** [their expertise that matches our need — be specific]
- **What I want them to talk about:** [topic + level of audience]
- **The signer of the letter:** [me / department chair / program director]

## Letter structure (one page, ~300-400 words)

### Paragraph 1: Opening + invitation
- Formal address (Dr. [Last Name])
- The invitation, stated clearly in the first 1-2 sentences (event, date)
- A specific reason WHY this person — referencing their work, not generic praise

### Paragraph 2: What's being asked
- The talk topic with specificity (not just "anything in your area of expertise")
- Audience description (how many, what level)
- Logistics: location, format, audience composition

### Paragraph 3: What's offered
- Honorarium (named, even if "we'll provide an honorarium" with details to follow)
- Travel and accommodation logistics
- Any additional activities (sign-out visit, meeting with residents, dinner with faculty)

### Paragraph 4: Practical next steps
- What I'm asking them to confirm
- Date by which I'd appreciate a response
- Who they'll work with on logistics
- An offer to chat by phone if they have questions

### Closing
- Warm but professional
- Signature with full title and institution

## Tone

- Substantive — they should believe we've thought about why we're inviting them
- Not effusive — no "honored," "thrilled," "exceptional"
- Specific — generic invitations get declined
- Respectful of their time

## Hard rules

- **One page maximum.** Long letters signal you're padding.
- **Specific 'why this speaker'** in paragraph 1 — referencing their work, not generic praise.
- **Honorarium and travel offer mentioned even if details follow.** Avoiding it implies stinginess.
- **Specific topic suggestion.** "Anything in your area" is lazy; "we'd love your take on [specific question we're wrestling with]" is generous.

## What I will NOT accept

- A letter that could have been sent to any speaker
- Effusive language ("honored," "thrilled," "tremendously excited")
- Vague topic suggestion
- Missing logistics
```

## Expected output

A one-page formal invitation letter (~300-400 words) ready to send.

## Common failure modes

- **Generic.** Push back: "What specifically about this person?"
- **Effusive.** Push back: "Less 'honored,' more substance."
- **Vague topic.** Push back.

## Required human verification

- Verify the speaker's current title, institution, and preferred form of address.
- If institutional honorarium policies apply, confirm the offered amount complies.
- For CME-accredited events, additional disclosure language may be required.

## Best model and why

**Claude Sonnet 4.6** — formal correspondence with specific calibration is Sonnet's strength.
