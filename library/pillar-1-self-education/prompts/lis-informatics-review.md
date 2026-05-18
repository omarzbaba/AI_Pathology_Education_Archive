---
title: LIS / informatics concept review
pillar: self-education
event_type: n/a
audience: resident
difficulty: intermediate
time_to_use: 2-10min
visual: text-only
tags: informatics, lis, standards
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Bridges the vocabulary gap between clinical pathologists and informatics. You name a concept (HL7 segments, FHIR resources, middleware autoverification, LOINC mapping, instrument interfacing); the model gives you the mental model, the working vocabulary, the most common failure mode, and one specific question you can ask in a vendor or IT meeting that distinguishes a substantive answer from a hand-wave.

## When to use it

Before an informatics committee meeting, when evaluating a vendor proposal, when a workflow issue gets escalated to IT, or when you want to participate substantively in a discussion about lab IT infrastructure rather than just listening.

**Not for:** deep informatics certification prep (read a textbook), implementation-specific configuration questions (those need an actual informaticist), or settled questions you can just look up.

## The prompt

```
You are explaining an informatics concept to me — a clinical pathologist who runs a lab but is not a full-time informaticist. The goal is to give me the mental model, the working vocabulary, and the ability to participate meaningfully in a vendor or IT meeting on this topic.

## What I'm asking about

- **Concept:** [e.g., "HL7 v2.5.1 ORU result segment structure", "FHIR Observation resource", "middleware autoverification logic", "LOINC code harmonization across two instruments", "IHE LAW profile"]
- **My existing knowledge:** [what I know already and what's still fuzzy]
- **The specific situation prompting this:** [optional — e.g., "we're evaluating a middleware vendor next week", "our chemistry instrument is throwing OBX-5 errors"]

## What to produce — 5 parts

### 1. The problem this concept solves (2-3 sentences)

Why does this thing exist? What does it make possible that wasn't possible before? Ground it in a concrete lab problem.

### 2. The mental model (2-3 sentences)

An analogy or simplified description that captures the essence. Be careful: the analogy should illuminate, not mislead. If the analogy breaks down at a critical point, name where.

### 3. The working vocabulary (5-7 terms)

The terms I'll hear thrown around in a meeting, each with a one-sentence definition. These are the words I need to follow the conversation — not exhaustive, just the high-frequency ones.

### 4. The most common failure mode in real labs (2-3 sentences)

The thing that breaks. What goes wrong, what it looks like (downtime, wrong results, missed criticals), what the typical root cause is, and what the fix typically involves.

### 5. One question I can ask in a meeting (1 question + brief rationale)

A specific question that, if asked, would distinguish a vendor who knows what they're doing from one who's improvising. Or a question that would clarify a confusion point that's slowing your meeting. The question should be answerable but not trivial — a good vendor will respect that you asked it.

## Hard rules

- **Cite specific standards by name and version** where applicable. "HL7 v2.5.1 OBX-5", "FHIR R4 Observation.code", "LOINC 33747-0". Do not paraphrase the standard.
- **If you're not sure whether a term or concept is current vocabulary**, say so. Informatics terminology changes (HL7 v2 → FHIR; SNOMED-CT version drift).
- **The mental model analogy must be honest about where it breaks.** Cute analogies that mislead are worse than no analogy.
- **The "common failure mode" should be a real-world failure**, not a textbook risk.
- **The "question to ask" must be specific enough to use in a meeting** without further translation.

## What I will NOT accept

- Vocabulary terms that are themselves opaque (defining one informatics term using three others I don't know)
- A "common failure mode" that's generic ("configuration errors happen")
- An analogy that's accurate at the surface but breaks at the point of usefulness
- A vendor question that's so basic any answer would seem fine
```

## Expected output

Five parts in order. Total length 400-600 words. The vendor question is often the most useful part — it gives you a concrete handle for the meeting.

## Common failure modes

- **Model uses informatics jargon while explaining informatics jargon** (recursive opacity). Push back: "Define [term you used] in plain language too."
- **The "most common failure mode" is generic** rather than the actual recurring failure in real labs. Push back for specific.
- **Standard versions misnamed.** Verify against the actual standard.

## Required human verification

- Verify any cited standard, segment name, code, or version against authoritative documentation (HL7.org, hl7.fhir.org, LOINC.org).
- For high-stakes situations (vendor selection, contract review), have an informaticist colleague pressure-test the question you plan to ask before relying on it.
- The mental model is most useful when validated by someone who has actually built or maintained this in production.

## Best model and why

**Claude Opus 4.7** — informatics standards (HL7, FHIR, LOINC) require depth and specificity. Opus cites segment names and resource types more reliably than Sonnet and is more careful about version disclosure. **Avoid GPT models** for this prompt — they confuse HL7 v2 segment names with FHIR resource fields more often than is comfortable.
