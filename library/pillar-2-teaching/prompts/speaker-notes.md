---
title: Speaker notes for existing slides
pillar: teaching
event_type: n/a
audience: faculty
difficulty: quick-win
time_to_use: 2-10min
visual: text-only
tags: lecture, speaker-notes, spoken-voice
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Generates speaker notes for your existing slide deck: paste your slide titles + bullets, get back per-slide notes that expand bullets into spoken prose, include the specific example to use, mark interaction beats, and bridge to the next slide. Notes are in SPOKEN voice — short sentences, no jargon you wouldn't actually say.

## When to use it

When you've built slides but haven't yet rehearsed, or when you'll be delivering the same talk multiple times and want a script to anchor your first pass. The notes get refined each iteration.

**Not for:** writing the slides themselves (use the slide outline prompt), generating substantive new content (the model fills in connective tissue — your bullets supply the substance), or any context where written-voice formality is expected (different format).

## The prompt

```
You are generating speaker notes for an existing slide deck. Notes must be in SPOKEN voice. Aloud-test as you write — if a sentence reads like written prose, rewrite for the ear.

## What I'm providing

- **Talk title and duration:** [e.g., "Approach to monoclonal gammopathy, 45 min + 15 min Q&A"]
- **Audience:** [PGY level / faculty / mixed]
- **Slide content:** [paste slide titles + bullet content, one slide per block]
- **My specific examples / anecdotes / cases:** [paste the ones I want to use]
- **My delivery style:** [conversational / formal / Socratic — pick]

## For each slide, produce

1. **Transition sentence from the previous slide** (1 sentence — the bridge that makes the lecture feel continuous)
2. **Expansion of each bullet into 2-3 spoken sentences** (more than the slide says, less than a paragraph)
3. **The specific example, anecdote, or analogy I should use here** — drawn from what I gave you. If I didn't provide one for a slide that needs it, mark `[INSERT EXAMPLE]`.
4. **Bridge sentence to the next slide** (1 sentence)
5. **Interaction marker** if this slide has a poll, audience question, or case to think about — bracketed `[PAUSE FOR POLL]` or similar

## For visual/diagram slides with minimal text

Speaker notes should be LONGER, not shorter. The visual is your prompt; the notes are where you explain what the audience sees. Walk through the visual systematically: "On the left, you'll see... in the middle... on the right..."

## Tone and voice

- **Short sentences.** Speakers can hold ~15 words at a time, not 40.
- **Conversational vocabulary.** If a word feels like reading-vocab, replace it.
- **First person plural** where appropriate ("we know", "we've seen") rather than passive voice.
- **One thought per sentence.** Embedded clauses lose listeners.

## Hard rules

- **Notes are spoken voice, not written voice.** If a sentence reads like a journal article, rewrite for the ear.
- **Do not invent clinical content** I didn't provide on the slides. Connective tissue only.
- **Mark `[INSERT EXAMPLE]`** rather than making up an anecdote.
- **Transition sentences are non-optional.** They make the lecture feel continuous.

## What I will NOT accept

- Notes that sound like written prose ("It is important to recognize that...")
- Generic examples ("a recent case")
- Slide notes that fabricate content not on the slide
- Missing transitions
```

## Expected output

Per-slide notes with transitions, expansions, specific examples, bridges, and interaction markers. Length scales with number of slides.

## Common failure modes

- **Written voice slipping in.** Push back: "Read aloud. Does it sound like you?"
- **Fabricated examples** when you didn't supply one. Push back: "Mark [INSERT EXAMPLE]; don't invent."
- **Generic clinical content added** beyond what's on the slide. Push back.

## Required human verification

- Verify any clinical content the model added beyond what was on the slide. The model fills gaps and sometimes fills them wrong.
- Rehearse the notes aloud. Spoken language reveals problems written language hides.

## Best model and why

**Claude Sonnet 4.6** — expanding bullets into natural spoken voice is a workhorse task. Sonnet's voice is more natural for spoken delivery than GPT-4o (tends toward written register).
