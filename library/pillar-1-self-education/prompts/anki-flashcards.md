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
best_model: Claude Haiku 4.5
last_updated: 2026-05-17
---

## What this prompt does

Converts a topic, paper, set of notes, or lecture into Anki-import-ready flashcards in tab-separated format. The prompt enforces *atomic* cards (one fact per card), *specific* questions (not "what is X"), and *verification flags* for any specific value the model isn't certain about.

## When to use it

Within an hour of finishing a dense reading session, while the material is still fresh enough for you to spot misformulated cards quickly. Also useful for converting a lecture's slide deck into review material.

**Not for:** building a comprehensive deck from scratch (this is for incremental additions, not bulk creation), high-stakes question banks (those need editorial review per card), or material you're seeing for the first time (study first, then make cards).

## The prompt

```
You are generating Anki flashcards from source material. Output must be tab-separated, atomic, and specific. If you cannot verify a specific value (cutoff, dose, gene name), flag it [VERIFY] rather than committing to it.

## What I'm converting

- **Source:** [topic name / paper citation / pasted notes / lecture title]
- **Source material:** [paste the content, or describe if it's a known topic]
- **Number of cards:** [e.g., 15 — don't pad; fewer good cards is better than more weak ones]
- **Card style:** [Basic Q/A — default, unless I say cloze]
- **My level:** [PGY level — calibrates how specific the questions should be]

## Output format — tab-separated, one card per line

Each line:
`question[TAB]answer`

## Rules — applied to every card

1. **Atomic.** Each card tests ONE fact or concept. If a card uses "and" or "or" in the answer, split it into two cards.
2. **Specific question framing.** "What is X?" is a weak question. "In a patient with X, what laboratory finding distinguishes A from B?" is strong. Questions should require retrieval, not recognition.
3. **Use actual numbers, names, and details from the source.** If the source doesn't have a specific value and you're filling it in from memory, append [VERIFY] to the answer.
4. **No clozes unless I asked.** Plain Q/A only by default.
5. **Don't pad to reach N cards.** If the material only supports 10 good cards, give me 10.
6. **No card should test two things at once.** "What are the four causes of X?" is weak (forces dump). "Among the four causes of X, which one is associated with [specific feature]?" is strong.

## After the cards, add a brief note

Add one short paragraph noting:
- What you deliberately did NOT make a card for (and why)
- Any [VERIFY]-flagged values I should double-check before adding the deck to active review

## Hard rules

- Tab-separated format, no extra commentary mixed with cards
- Atomic cards always
- [VERIFY] flag on any value you're not certain about
- Source-grounded specificity over generic phrasing

## What I will NOT accept

- "What is X?" style cards as default framing
- Cards that test multiple facts ("List the three reasons for Y")
- Padding with weak cards to reach the requested number
- Confidently stated specific values without verification
```

## Expected output

N tab-separated lines (one card per line) plus a brief note about exclusions and verification flags. Lines should be import-ready: paste into Anki → Import → Text File.

## Common failure modes

- **"What is X" cards.** Push back: "Reframe these as specific retrieval questions."
- **Cards testing multiple facts.** Split them.
- **Confidently made-up specific values.** Add [VERIFY] manually before adding to your deck.

## Required human verification

- Scan every answer with a specific numerical value, drug dose, gene name, or threshold. Verify against the source. The model sometimes invents plausible-looking specifics.
- For cards built from your own notes, double-check that the model preserved your wording rather than rewriting subtly.

## Best model and why

**Claude Haiku 4.5** — flashcard conversion is a fast, structured task. Haiku handles it well at a fraction of the cost. Bump to **Sonnet 4.6** only if the source material is dense (methods-heavy paper, complex algorithm) where atomicity is harder to maintain.
