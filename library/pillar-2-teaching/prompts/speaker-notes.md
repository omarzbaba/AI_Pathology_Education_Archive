---
title: Speaker notes for existing slides
pillar: teaching
event_type: n/a
audience: faculty
difficulty: quick-win
time_to_use: 2-10min
visual: text-only
tags: lecture, speaker-notes
verified_models: TODO
last_updated: 2026-05-17
---

## What this prompt does

Generate speaker notes for an existing slide deck by pasting slide titles and bullet points, with the model filling in the connective tissue between bullets.

## When to use it

When you've made slides but haven't rehearsed yet, and need a script to anchor your first pass through the deck. Best for talks you'll give multiple times — the notes get refined each iteration.

## The prompt

```
Generate speaker notes for the following slide deck. The talk is [N] minutes total for [audience].

For each slide, write speaker notes that:

1. Open with a transition sentence connecting from the previous slide.
2. Explain each bullet in 2-3 spoken sentences (more than the slide says, less than a paragraph).
3. Include the one specific example, anecdote, or analogy I should use here. Be concrete — 'the Bethesda case from last week' not 'a recent case'.
4. End with a bridge sentence to the next slide.

If a slide is a visual or a diagram with minimal text, the speaker notes should be longer — that's where I'm explaining what the audience sees.

Mark moments to pause for questions or audience interaction.

Slides:
[paste slide titles + bullet content, one slide per block]
```

## Expected output

Per-slide speaker notes with transitions, expansions, specific examples, and bridges. The notes should be in spoken voice, not written voice — short sentences, no jargon you wouldn't actually say.

## Common failure modes

- The notes are written voice ('It is important to recognize that...') rather than spoken voice.
- The 'specific example' is generic ('think of a recent case').
- Transition sentences are formulaic ('Moving on to slide X').

## Required human verification

- Verify any clinical content the model adds beyond what was on the slide. The model fills in gaps and sometimes fills them with confident-wrong content.
- Rehearse the notes aloud. Spoken language reveals problems written language hides.
