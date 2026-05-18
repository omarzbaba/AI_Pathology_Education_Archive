---
title: Knowledge gap discovery from uploaded sources
pillar: self-education
event_type: n/a
audience: resident
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: source-grounded, gap-discovery, study-planning
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-18
---

## What this prompt does

Asks the notebook to surface YOUR knowledge gaps relative to YOUR uploaded study material — through an adaptive quiz that progressively narrows on weak topics, then summarizes the gaps with specific reading recommendations from the corpus.

This is metacognition aided: the notebook helps you discover what you don't know that you don't know, based on a corpus you've decided defines "what you should know."

## When to use it

After a study block, when planning the next week of board prep, or when you have a sense you're weak somewhere but can't pin down what. Best done in a single 30-60 minute session.

## The prompt

```
You are helping me discover knowledge gaps from the sources in this notebook.
Adaptive quiz: start broad, narrow on weakness, then summarize what I should
study and which sources to read.

## My context

- **PGY level + use case:** [e.g., "PGY-3, 8 weeks until ABPath in-service"]
- **Topic scope:** [broad area to cover — e.g., "all of plasma cell neoplasms
  as covered in this notebook"]
- **Time I have for this session:** [e.g., 45 minutes]
- **My current self-assessment:** [optional — where I think my gaps are]

## Adaptive quiz protocol

### Phase 1: Breadth probe (10 questions)

Ask 10 broad questions covering the topic, one at a time, drawn from
different uploaded sources. Wait for my answer to each. Track which I
get right, partially right, wrong.

### Phase 2: Identify weak topic

After 10 questions, identify the topic (or 2-3 topics) where my responses
indicate genuine knowledge gaps (not just imprecise wording, but real
misunderstanding).

### Phase 3: Narrow drill (5-8 questions on weak topic)

Drill the identified weak topic with progressively more specific questions.
Continue until you've characterized the gap precisely:
- Is it a recall failure (I know the concept but couldn't retrieve)?
- Is it a concept gap (I don't understand the underlying mechanism)?
- Is it an integration gap (I know the pieces but can't connect them)?

### Phase 4: Gap summary

Produce a written summary:

**Topic with confirmed gap:** [name]
**Type of gap:** recall / concept / integration
**Specific subtopics where I'm weak:** [list]
**Source passages to re-read:** [specific sources and sections]
**Estimated time to address:** [hours]
**A check question I should be able to answer after re-reading:**
[specific question]

### Phase 5: Action plan

Based on the gap and my stated time budget, recommend:
- The highest-priority action to take this week
- What I should drop or defer
- When to re-test (suggest a date)

## Source-grounding rules

- All questions drawn from uploaded sources.
- Source citations on every "correct" answer.
- Reading recommendations cite specific sources in the corpus.
- If a gap is in a topic the corpus doesn't cover well, name that as
  a corpus limitation, not just my gap.

## What I will NOT accept

- Generic "study harder" recommendations
- Gap summary that doesn't name specific sources
- Quiz that doesn't actually adapt based on my responses
```

## Expected output

A 5-phase adaptive session ending with a specific gap diagnosis and source-grounded study recommendation. Takes 30-60 minutes of active engagement.

## Common failure modes

- **Model labels you "wrong" generously** to find gaps. Be skeptical — sometimes you really did know it.
- **Recommendations to "re-read" sources that don't actually address the gap.** Verify the recommended source contains what you need.
- **Gap diagnoses that confuse recall failure with concept gap.** The interventions differ — push back if labeling feels off.

## Required human verification

- **Verify the gap diagnosis** against your own sense of where you struggle. The model is one diagnostic; your self-assessment is another.
- **Verify the recommended reading actually addresses the gap** by opening the source.
- **Re-test after re-reading** to confirm the gap is closed.

## Best model and why

**Claude Opus 4.7 via Claude Projects** — adaptive reasoning across many turns rewards Opus. **NotebookLM** can do this but the adaptive logic is less smooth.
