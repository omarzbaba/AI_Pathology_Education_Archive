---
title: Journal club packet generation
pillar: educational-operations
event_type: conference
audience: faculty
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: journal-club, packet
verified_models: TODO
best_model: Claude Opus 4.7 with paper attached
last_updated: 2026-05-17
---

## What this prompt does

Generate a journal club packet with paper summary, background context, key results, methodologic critique, and discussion questions.

## When to use it

One week before journal club, when you're the lead and want to send pre-reading to attendees that ensures real discussion.

## The prompt

```
Generate a journal club packet for the following paper:

- **Paper**: [full citation]
- **Audience**: [PGY level, mix of residents and faculty]
- **Discussion format**: [traditional, debate, structured critique, etc.]

The packet should include:

1. **One-paragraph background**: the state of the field before this paper. What question made this paper worth doing?
2. **The study summary**: design, population, key results with numbers. Neutral framing, not yet interpretive.
3. **Methodologic critique** (using the appropriate reporting guideline framework — see the [Paper methods critique prompt](library.html#/library/pillar-1-self-education/prompts/paper-methods-critique)):
   - 2 specific strengths of the methods.
   - 2-3 specific limitations.
4. **The 'so what'**: what could this paper change about practice? What barriers exist to that change?
5. **5 discussion questions** ordered from concrete to contested:
   - Methods or numbers question.
   - Generalizability question.
   - Comparison-to-prior-literature question.
   - Practice-change question.
   - A genuinely contested question.
6. **Attendee preparation note**: what they should think about before arriving.

Length: 2-3 pages. No PHI.

**Important — refinement:** If you don't have the full paper text, say so and refuse to generate the packet. Fabricated background, methods, or numbers in a journal club packet undermine the entire session.
```

## Expected output

A complete packet ready to send to attendees a week before journal club.

## Common failure modes

- Critique is generic.
- Discussion questions are leading rather than open.
- Background context misses the paper's intellectual lineage.

## Required human verification

- Verify all numbers against the actual paper.
- Pre-test the contested question with a colleague.
- Confirm citations are accurate.

## Best model and why

**Claude Opus 4.7 with paper attached** — Quality depends on actually reading the paper. Opus with PDF attached, or Gemini 2.5 Pro for very long papers. Refuse the prompt if you don't have the paper text.
