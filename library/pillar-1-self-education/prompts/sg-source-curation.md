---
title: Source curation principles for AI notebooks
pillar: self-education
event_type: n/a
audience: resident
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: source-grounded, curation, principles
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-18
---

## What this prompt does

Principles for choosing what to upload to your AI notebook. The discipline that distinguishes a useful notebook from a noisy one: every source should earn its place. Curation IS the work.

## When to use it

When building any source-grounded notebook (board prep, sign-out, journal club, institutional). Re-read when your notebook starts producing low-quality responses — the cause is almost always corpus drift.

## The principles

```
SOURCE CURATION PRINCIPLES

## Principle 1: Quality over quantity

Notebooks degrade as corpus grows beyond 25-30 documents. Retrieval gets
fuzzier; the model spreads attention across too many sources; responses
become average-of-everything rather than grounded-in-best-source.

**Rule of thumb:** if you wouldn't recommend a source to a colleague, it
doesn't belong in your notebook.

## Principle 2: Mix source types deliberately

A healthy corpus has:
- 30-40% foundational references (textbook chapters, foundational papers)
- 30-40% current evidence (recent review articles, current guidelines)
- 10-20% landmark papers (historical context, why the field thinks this way)
- 10-20% your own notes (rotation notes, attending preferences, case logs)

A corpus that's 100% review articles is shallow. A corpus that's 100%
primary literature is exhausting. Mix deliberately.

## Principle 3: Recency matters but isn't everything

For most subspecialties, sources within the last 5 years are most current.
But:
- Landmark papers from any era stay relevant (the original 1985 paper
  defining [X] is still cited weekly)
- Guidelines have specific versions — make sure you have the CURRENT one,
  not the prior one
- For rapidly evolving fields (molecular pathology, AI in pathology),
  even 2-year-old reviews can be stale

## Principle 4: Exclude what would contaminate retrieval

DO NOT upload:
- **Old qbank questions verbatim** — they bias the notebook toward
  test-question framing
- **Pirated copyrighted material** — copyright and ethics issue
- **Unpublished resident notes from other residents** without permission
- **Patient material of any kind** — never, under any circumstances
- **Drafts of your own papers** that are still under review (confidentiality)
- **Anything you'd be embarrassed for an AI tool to "learn from"** even
  though it doesn't really learn from your notebook in the training sense

## Principle 5: Document your sources

Maintain a separate doc (not in the notebook, in your own notes) listing:
- What's in the notebook
- Why each source is there
- When it was added
- When to re-evaluate

When you revisit the notebook in 6 months, this doc tells you what's stale.

## Principle 6: Iterate

Curation is not a one-time setup. Every 2-4 weeks:
- Remove sources that turned out to be redundant
- Remove sources whose answers you've memorized (they're no longer
  earning their place)
- Add 1-2 new high-yield sources as the field evolves
- Re-check the notebook's responses against current literature

## Principle 7: Different notebooks for different purposes

A board prep notebook needs different sources than a journal club notebook
than a sign-out preview notebook. Resist the temptation to build "one big
notebook for everything." Different use cases need different corpora.
```

## Expected output

A clearer mental model for what belongs in your notebook and what doesn't. Practical filter for the next time you're considering uploading something.

## Common failure modes

- **"More is better" instinct.** Resist. Quality > quantity for retrieval.
- **Uploading qbank questions** and then being surprised when the notebook produces test-style framing.
- **Never auditing the corpus.** A notebook built once and never updated decays.

## Required human verification

- The curation principles are heuristics, not rules. Calibrate to your subspecialty and use case.
- For specific copyright questions about institutional material, consult your institutional library or legal/compliance office.

## Best model and why

This is a principles document, not a prompt. **Claude Sonnet 4.6** can help you think through specific curation decisions if you're unsure.
