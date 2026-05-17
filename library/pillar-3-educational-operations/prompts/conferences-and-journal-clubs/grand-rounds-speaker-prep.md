---
title: Grand rounds speaker prep
pillar: educational-operations
event_type: conference
audience: faculty
difficulty: intermediate
time_to_use: >10min
visual: text-only
tags: grand-rounds, speaker-prep
verified_models: TODO
last_updated: 2026-05-17
---

## What this prompt does

Generate a grand rounds speaker prep document with audience profile, expected questions, recommended visuals, and timing breakdown.

## When to use it

2-3 weeks before grand rounds, when you've accepted the invitation and need to start preparing. Skips the 'where do I even start' phase.

## The prompt

```
I'm giving grand rounds on [topic] at [institution] on [date]. The talk is [duration] minutes plus Q&A. The audience is [mix — usually attendings, fellows, residents, sometimes med students or outside guests].

Help me prepare. Generate:

1. **Audience profile**: who's likely in the room, what they know about the topic coming in, what they want to walk away with.
2. **Talk structure** (high-level): opening hook (which approach — a case? a statistic? a contrarian framing?), 3-4 content beats, synthesis. Estimated timing for each.
3. **Recommended visuals**: 2-3 specific visuals that will land in this audience (a graph, a side-by-side comparison, a clinical photo) — describe what each would show.
4. **5 questions** I should be ready for:
   - 2 from a content expert (the attending in the audience who knows the topic best).
   - 2 from a generalist (the medical director or chief who wants the high-level take).
   - 1 from a trainee (the resident who wants the practical takeaway).
5. **What to NOT do**: 2-3 framings, opening lines, or rhetorical moves that will misfire with this audience at this institution.
6. **A 'walking away' line**: the one sentence the audience should remember 24 hours later.
```

## Expected output

A prep document I can use to structure my preparation, not a script. Includes audience-specific Q&A prep.

## Common failure modes

- 'Audience profile' is generic.
- 'What not to do' is empty or platitudinous.
- The walking-away line is too long or too vague.

## Required human verification

- Run the audience profile by a colleague at the host institution if you can — they'll know specifics you don't.
- The walking-away line should be testable: would the audience be able to repeat it tomorrow?
