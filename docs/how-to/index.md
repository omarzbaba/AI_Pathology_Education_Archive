---
title: How-to
last_updated: 2026-05-18
---

This section collects the tutorials, decision guides, and orientation material that sit alongside the prompt library. Prompts in the three pillars are *do this* templates; the entries here are *how to think about it* essays.

## Start here if you're new

### [How to use this library](library.html#/docs/how-to/use-this-library)

The structure of every prompt entry, how to adapt prompts to your own context, the "chain prompts in one session" pattern, and the rules for using multimodal prompts safely. Read this first if you've never used the library.

### [How to write a good prompt](library.html#/docs/how-to/how-to-write-a-good-prompt)

A teaching-grade tutorial on prompt writing — the five components every prompt needs, how to iterate in three rounds, common failure modes, and a worked example. Designed to double as the basis for a one-hour resident or faculty teaching session (session outline included).

---

## Understanding the tools

The two essays below are the literacy layer — what the technology actually is, who makes which model, and the vocabulary you'll see in any technical conversation about AI in medicine. Read these before you start spending real money or building tools.

### [The LLM landscape — which model to use when](library.html#/docs/how-to/llm-comparison)

A working-pathologist's decision framework for which AI model to open for which task. Covers the four major providers (Anthropic, OpenAI, Google, Meta), the tier system (flagship / medium / small / reasoning models), pathology-specific picks for every use case across the three pillars, cost realities, privacy considerations, and how to stay current as the landscape shifts.

### [Tokens, context windows, and APIs — how the plumbing works](library.html#/docs/how-to/tokens-and-apis)

The technical literacy layer. What a token is, why pricing is structured the way it is, the difference between the web UI and the API, common parameters worth understanding (temperature, system message, streaming), prompt caching, embeddings, open-weight models, and a glossary card for the vocabulary. Intended for the clinician who has used ChatGPT in the browser and is starting to wonder whether they should build something.

---

## Source-grounded AI (NotebookLM, Claude Projects, Custom GPTs)

Source-grounded tools — where you upload your own materials and the AI answers from them — are a different shape of tool than generic chat. Different prep, different strengths, different failure modes. These four entries cover what you need to know before you set one up.

### [NotebookLM vs Claude Projects vs generic chat — choose your tool](library.html#/docs/how-to/notebooklm-vs-claude-projects)

A decision rubric for which tool fits your task. Free vs paid, persistent vs throwaway, grounded vs general — work through the four steps and the answer is usually clear.

### [Privacy and copyright for source-grounded AI](library.html#/docs/how-to/privacy-and-copyright)

The hard rules. Six categories of source material, from "never upload" (patient material) to "generally OK" (your own notes). Read this before you upload anything.

### [Source curation principles for AI notebooks](library.html#/docs/how-to/curate-sources)

Seven principles for choosing what belongs in your notebook. Curation is the work; a noisy corpus produces noisy answers.

### [Verify your AI notebook is actually grounded](library.html#/docs/how-to/verify-grounding)

A 5-test protocol for checking whether your notebook is genuinely answering from your sources or drifting into the model's general training data. Run it at setup and monthly thereafter.

---

## Read this before you use anything

The [Guardrails](library.html#/docs/guardrails) page covers PHI, accuracy verification, bias, authorship/disclosure norms, and the structural plausibility failure mode in AI-assisted writing. It's short. Read it once.
