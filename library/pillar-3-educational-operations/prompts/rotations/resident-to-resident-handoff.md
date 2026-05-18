---
title: Resident-to-resident handoff document
pillar: educational-operations
event_type: rotation
audience: resident
difficulty: quick-win
time_to_use: 2-10min
visual: text-only
tags: handoff, peer, tacit-knowledge
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-18
---

## What this prompt does

Generates a peer-to-peer handoff template that captures the outgoing resident's tacit knowledge for the incoming resident — practical tips, attending preferences, useful resources, the early mistake to avoid. Lowers activation energy on a write-up that residents otherwise skip.

The discipline this enforces: be diplomatic but honest about attendings; strip patient identifiers from any cases mentioned.

## When to use it

Last day of the rotation, when the outgoing resident has the most context and the lowest motivation to document it.

## The prompt

```
You are generating a peer-to-peer rotation handoff template. Strip patient identifiers from any case mentioned. Be diplomatic about attendings — accurate but not unkind.

## What I'm providing

- **Rotation:** [name]
- **My duration on the rotation:** [how long I was on]
- **Audience:** [the next resident — their PGY level]
- **Tone:** [collegial, peer-to-peer, slightly informal]

## What to produce

### Welcome + day-1 orientation moment (2-3 sentences)
A note from the outgoing resident on what to know on day 1.

### What the syllabus doesn't tell you (3-5 practical tips)
Where to find the on-service charger, who actually approves late sign-out, which attending wants what kind of preview — the stuff that takes a week to figure out otherwise.

### Three attendings I worked with most
Name + one sentence on what each cares about most (e.g., "Dr. X wants the smear scanned before sign-out, period"). Be specific without being unkind.

### The single most useful resource I found
The article, textbook, app, or website that made the rotation easier.

### The mistake I made early and what I'd do differently
Vulnerable but useful. Generic doesn't help; specific does.

### The case or moment I learned the most from
Brief, anonymized. Strip identifiers.

### Open offer
"I'm happy to answer questions by [contact method] for the first week if you have them."

## Tone

Peer-to-peer, slightly informal, honest. NOT a formal evaluation document. Collegial advice.

## Hard rules

- **No PHI** — strip identifiers from any case mentioned.
- **Diplomatic about attendings** — accurate without being unkind.
- **Specific, not platitudes.** "Work hard and be nice" is useless.

## What I will NOT accept

- Cases with potential identifiers
- Personal attacks on attendings
- Generic advice
```

## Expected output

A template the outgoing resident can complete in 20 minutes, giving the incoming resident a week's head start.

## Required human verification

- Strip patient identifiers from any cases described.
- Be diplomatic about attendings — re-read with that lens.

## Best model and why

**Claude Sonnet 4.6** — peer-to-peer template with friendly voice.
