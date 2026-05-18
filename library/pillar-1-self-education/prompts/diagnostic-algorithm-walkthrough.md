---
title: Diagnostic algorithm walkthrough
pillar: self-education
event_type: n/a
audience: resident
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: algorithm, diagnostic-workup, guidelines
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Walks through a published diagnostic algorithm step by step — not just naming what happens at each decision point but explaining *why* the question is being asked there, what the answer rules in or out, what the common pitfalls are, and which decision point is most clinically consequential to get right.

Algorithms are easy to apply mechanically and hard to apply with judgment. This prompt builds the judgment.

## When to use it

When you're encountering a clinical algorithm for the first time, when you've used one mechanically without really understanding why each branch exists, or the night before sign-out where the algorithm will come up.

**Not for:** algorithm lookup (just look at the published algorithm), real-time clinical application (use the actual algorithm + your attending), or generating new algorithms (different task).

## The prompt

```
You are walking me through a published diagnostic algorithm. Be specific to the published version. Don't generalize to "similar" protocols.

## What I'm asking about

- **Algorithm:** [exact name and version — e.g., "ISTH 2018 overt DIC scoring", "BSH 2023 guideline for warfarin reversal", "2022 ELN AML response criteria"]
- **My level:** [PGY level + relevant context]
- **What prompted this:** [optional — a case, a board question, a teaching session]

## Version disclosure first

State the version of the algorithm you're walking through. If the algorithm has been substantially revised in the last 5 years, note BOTH:
- The version you're describing
- What changed in the revision (and why it matters clinically)

If you're not certain which version is current, say so explicitly.

## What to produce — node by node

For each decision point in the algorithm:

1. **The question or test being asked at this node** (stated precisely)
2. **Why this question is being asked HERE** — what does the answer rule in or rule out at this point in the workflow?
3. **What happens if positive/yes** — next node, immediate management implication
4. **What happens if negative/no** — next node, what's been ruled out
5. **The common pitfall at this decision point** — the specific way residents mis-apply this step (not "be careful," but "residents often forget that this test has a 24-hour turnaround and order it before they're committed to the rest of the algorithm")

After walking through every node:

### The single most clinically consequential decision point

Of all the nodes in this algorithm, which one carries the highest cost of error? Why? What does getting it wrong cause?

### How to avoid those errors

Specific cognitive moves: a verification step, a sanity check, a question to ask before committing.

## Hard rules

- **Be specific to the published version.** If your version is 2024 and I'm using 2018 at my institution, the discrepancy matters.
- **Pitfalls must be specific, observed-from-real-practice.** Not generic.
- **Do not invent algorithm nodes.** If you're uncertain about the exact structure, ask me to paste the algorithm.
- **Source the algorithm name and year.** Society + version + year.
- **Acknowledge uncertainty** about whether the algorithm has been revised since your training data.

## What I will NOT accept

- Walkthrough that could apply to any "similar" algorithm
- Generic pitfalls ("don't forget to check the value")
- Confidently named cutoffs that aren't in the actual algorithm
- No version disclosure
```

## Expected output

Per-node walkthrough (question / why / yes branch / no branch / pitfall) followed by the most-consequential-node analysis. Length scales with number of nodes; typically 400-800 words for a 5-7 step algorithm.

## Common failure modes

- **Two similar algorithms conflated** (ISTH overt vs non-overt DIC criteria, for example). Push back: "Which one are you walking through?"
- **Pitfalls generic** rather than specific. Push back.
- **Invented or misremembered cutoffs.** Verify against the actual algorithm.

## Required human verification

- **Verify the walkthrough against the actual published algorithm.** Society guideline, original paper, institutional protocol — whatever the authoritative source is.
- **Verify the version is current.** Algorithms get revised; the model may reference an older version without flagging.
- **Pressure-test the "most consequential node" with an attending who uses this algorithm regularly.** Their clinical experience reveals which errors actually cause harm vs which are theoretical.

## Best model and why

**Claude Opus 4.7** — multi-step algorithm walkthroughs with specific guideline versions reward Opus's depth. Sonnet works but more often conflates similar protocols.
