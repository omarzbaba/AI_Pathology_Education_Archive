---
title: Anki flashcard generation
pillar: self-education
event_type: n/a
audience: resident
difficulty: quick-win
time_to_use: 2-10min
visual: text-only
tags: spaced-repetition, anki
verified_models: TODO
last_updated: 2026-05-17
---

## What this prompt does

Convert a topic, paper, or set of notes into Anki-ready flashcards in a format you can paste directly into Anki's import dialog. The structure matters because Anki rewards atomic, single-concept cards.

## When to use it

When you've just done dense reading and want to convert it into spaced-repetition material before you forget. Best within an hour of the reading session.

## The prompt

```
Convert the following [topic / source: paper title / notes] into Anki flashcards.

Output format: tab-separated values, one card per line. Each line is:

`question[TAB]answer`

Rules:

1. **Atomic cards.** Each card tests ONE fact or concept. If a card has 'and' or 'or' in the answer, split it into two cards.
2. **Specific questions.** 'What is X?' is weak. 'In a patient with X, what laboratory finding distinguishes A from B?' is strong.
3. **No clozes** unless I ask. Plain Q/A only.
4. **Aim for [N] cards.** Don't pad. If the material doesn't justify N cards, give me fewer good ones.
5. Use the actual numbers, names, and details from the source. If you don't know a specific value, leave it blank rather than guessing.

After the cards, add a one-sentence note about anything in the source you decided NOT to make a card for and why.
```

## Expected output

N tab-separated lines, one card per line, plus a brief note on what was deliberately excluded. The cards should be import-ready: paste into Anki → Import → Text File.

## Common failure modes

- Cards that test 'what is X' without context — useless for retention. Ask for more specific question framings.
- Cards that try to test multiple facts at once. Split them.
- Made-up specific values when the source didn't have them. Verify any specific number, dose, or threshold before incorporating into your deck.

## Required human verification

- Scan the answers for any numerical value, drug dose, gene name, or specific reference range. Verify each against the source or an authoritative reference. The model will sometimes invent plausible-looking specifics.
