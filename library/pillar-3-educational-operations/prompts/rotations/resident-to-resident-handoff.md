---
title: Resident-to-resident handoff document
pillar: educational-operations
event_type: rotation
audience: program-director
difficulty: quick-win
time_to_use: 2-10min
visual: text-only
tags: handoff, peer
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-17
---

## What this prompt does

Generate a resident-to-resident handoff document covering what the incoming resident needs to know in their first week.

## When to use it

Last day of the rotation, when the outgoing resident has the most context and the lowest motivation to write it down. The template lowers the activation energy.

## The prompt

```
Generate a peer-to-peer rotation handoff template for [rotation name]. Audience: the next resident starting this rotation.

The template structures the outgoing resident's tacit knowledge into usable form. Sections:

1. **Welcome and orientation moment**: a 2-3 sentence note from the outgoing resident on what to know on day 1.
2. **What the syllabus doesn't tell you**: 3-5 practical tips that aren't in the formal documents (where to find the on-service charger, who actually approves sign-out late, which attending wants what kind of preview).
3. **Three attendings I worked with the most**: name and a sentence on what each cares about most (e.g., 'Dr. X wants the smear scanned before sign-out, period').
4. **The single most useful resource I found**: the article, textbook, app, or website that made the rotation easier.
5. **The mistake I made early and what I'd do differently**: vulnerable but useful.
6. **The case or moment I learned the most from**: brief, anonymized.
7. **Open offer**: 'I'm happy to answer questions by [contact method] for the first week if you have them'.

Tone: peer-to-peer, slightly informal, honest. This is NOT a formal evaluation document — it's collegial advice.

**Important — refinement:** Strip patient identifiers from any case mentioned. Be diplomatic but honest about attendings — aim for 'Dr. X prefers a written preview before sign-out' rather than personal critique.
```

## Expected output

A template the outgoing resident can complete in 20 minutes that gives the incoming resident a week's head start.

## Common failure modes

- Becomes too formal; outgoing residents don't write candidly.
- Identifies cases with potential to identify patients.
- 'Three attendings' notes are too candid and reflect badly on the attending.

## Required human verification

- Strip patient identifiers from any cases described.
- Be diplomatic about attendings; aim for accurate without being unkind.
- The 'mistake' should be one the outgoing resident is comfortable putting in writing.

## Best model and why

**Claude Sonnet 4.6** — Peer-to-peer template with friendly voice — Sonnet is appropriate. Strip any PHI before pasting case content regardless of model.
