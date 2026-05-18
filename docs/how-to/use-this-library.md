---
title: How to use this library
last_updated: 2026-05-18
---

## The shape of a prompt entry

Every prompt in this library is a Markdown file with the same seven-section structure. Knowing the structure lets you skim a prompt in 30 seconds and decide whether it's relevant.

**The frontmatter metadata card** at the top of each prompt page tells you the pillar, audience, difficulty, time-to-use, and the AI models the prompt has been verified on. Read this first.

**What this prompt does** — one or two sentences. If the intent doesn't match what you're trying to do, stop reading and pick a different prompt.

**When to use it** — the specific scenario where this prompt earns its keep. Often calls out scenarios where the prompt is *not* the right tool.

**The prompt** — copy-paste-ready text in a code block. Use the copy button in the top-right corner. The prompt is meant to be edited; the verbatim form is a starting point.

**Expected output** — what a good response looks like and what to do with it. If the model's response doesn't match this shape, you've miscalibrated; rewrite the prompt and try again.

**Common failure modes** — the things that typically go wrong with this prompt, written by someone who has run it dozens of times. These are not theoretical risks; they're observed patterns.

**Required human verification** — the specific checks you must do before treating the output as usable. This is the non-negotiable part. Skipping verification turns a useful prompt into a liability.

## Adapting prompts to your context

The library is opinionated toward an academic Clinical Pathology context with a focus on resident education. Adapt prompts to your context by editing four things in the prompt body:

1. **Level.** "PGY-2 in their first month of blood bank" is specific. "Resident" is not. Specificity makes the output usable.
2. **Subspecialty vocabulary.** Replace generic terms with the terms your service uses. "The on-service attending" lands differently than "the supervising faculty member" and your residents will notice.
3. **Institutional context.** Reference your institution's protocols, LIS, panel order sets, sign-out workflow. The model cannot know these, and the output is generic without them.
4. **Constraints.** SI vs conventional units, US vs international guidelines, your CME/MOC requirements. State them explicitly.

A prompt that took 90 seconds to copy and 4 minutes to customize is well-spent time. A prompt copied verbatim and used un-edited is a wasted opportunity.

## Chain prompts in one session

Most of the prompts in this library are designed to be used in sequence within the same conversation, not as one-shot queries. The model maintains state across turns — it remembers your level, your preferences, the corrections you made earlier. Chaining works because of this state:

- **Pillar I example:** *calibrate → explain → drill → critique my reasoning*. Four prompts, one session, ~15–20 minutes. Far more effective than four cold queries.
- **Pillar II example:** *generate vignette → critique vignette → generate matched-pair distractor → generate 3 MCQs*. One session, ~25 minutes. The matched-pair distractor would not work as well without the prior context.
- **Pillar III example:** *generate orientation packet outline → flesh out section 1 → flesh out section 2 → suggest pitfalls based on what's already in the document*. The "suggest pitfalls" step relies on the model seeing the rest of the packet.

Avoid the temptation to start a new conversation for each turn. Cold conversations are cheap but they are also context-free.

## Using multimodal prompts safely

A small number of prompts in this library are explicitly multimodal — you upload an image (typically a photomicrograph, gel, or trace) and the model interprets it. Three rules:

1. **Never upload real patient images.** Not de-identified institutional cases, not anonymized service material, not snapshots of your computer screen at the scope. Use published teaching cases, public-domain images, or your own legitimately-cleared collection. If you cannot demonstrate consent and de-identification on demand, do not upload.
2. **Always verify the model's interpretation against a known answer.** The published-teaching-case approach makes this easy: you already know what the case is supposed to be. Multimodal AI is improving rapidly but still routinely confident-wrong on subtle morphology.
3. **Frame multimodal sessions as practice, not consult.** The format that works is "I'm using this image to drill my interpretive reflex" — not "tell me what this is." See the [SPEP self-quiz worked example](library.html#/library/pillar-1-self-education/examples/spep-self-quiz) for the right framing.

## Sharing variants you discover

If you find a prompt that works much better with a particular tweak — a phrasing that fixes a common failure mode, a calibration that produces consistently better output for your subspecialty — the author would like to hear about it. The library is meant to grow.

Use the [Submit a prompt](submit.html) form to send a variant, or use the floating **Feedback** button at the bottom-right of any page. Useful contributions will be credited and added to the prompt file with attribution — see the [Contributors page](library.html#/docs/contributors).

## Read this before you use anything

The library has one document that everyone should read at least once: the [Guardrails](library.html#/docs/guardrails) page. It covers PHI, accuracy verification, bias, authorship and disclosure norms, and the structural plausibility failure mode in AI-assisted writing. Read it. It is short.
