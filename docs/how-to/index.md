---
title: How-to
last_updated: 2026-05-18
---

This section collects the tutorials, decision guides, and orientation material that sit alongside the prompt library. Prompts in the three pillars are *do this* templates; the entries here are *how to think about it* essays.

## Start here if you're new

### [Your first 30 minutes with an LLM](library.html#/docs/how-to/first-30-minutes)

The absolute-beginner onboarding. Pick a tool, write your first prompt with intent, read the response critically, iterate, try a real pathology question, and learn what not to do — all in 30 minutes. Read this first if you've never used ChatGPT, Claude, or Gemini with purpose.

### [How to use this library](library.html#/docs/how-to/use-this-library)

The structure of every prompt entry, how to adapt prompts to your own context, the "chain prompts in one session" pattern, and the rules for using multimodal prompts safely. Read this second.

### [How to write a good prompt](library.html#/docs/how-to/how-to-write-a-good-prompt)

A teaching-grade tutorial on prompt writing — the five components every prompt needs, how to iterate in three rounds, common failure modes, and a worked example. Designed to double as the basis for a one-hour resident or faculty teaching session (session outline included).

---

## Reading what comes back

### [What to do when the AI is wrong](library.html#/docs/how-to/what-to-do-when-ai-is-wrong)

The companion skill to prompt-writing. The five failure modes (confident-wrong, soft hedging, hallucinated citations, drug-name swaps, threshold drift), how to spot each, the discipline of pushing back productively without telling the model the answer, and when to switch models entirely or walk away. The single most important critical-reading guide in this set.

### [Bias in medical AI — watching for it, working around it](library.html#/docs/how-to/bias-in-medical-ai)

Where the bias comes from, pathology-specific examples (dermpath on darker skin, hematology reference ranges from non-representative cohorts, classic-case defaults), how it surfaces in MCQ generation and case vignettes, and a practical checklist for countering it in your own teaching materials.

---

## Working in sessions

### [Chaining prompts in one session — the conversation discipline](library.html#/docs/how-to/chaining-prompts)

When chaining compounds context in your favor, when it corrupts framing, when to start fresh, and how to structure a productive session. Three worked examples — one per pillar — showing 8-turn sessions that produce dramatically more value than equivalent cold one-shot prompts.

### [Working with images — multimodal AI for pathology](library.html#/docs/how-to/working-with-images)

Specific to our visual specialty. The non-negotiable rules on patient material, technical quality of uploads (resolution, crop, magnification, stain ID), which models perform best on which image types, the framing trap (oracle vs tutor), cross-model verification, and a 30-minute photomicrograph study workflow.

---

## Understanding the tools

The two essays below are the literacy layer — what the technology actually is, who makes which model, and the vocabulary you'll see in any technical conversation about AI in medicine. Read these before you start spending real money or building tools.

### [The LLM landscape — which model to use when](library.html#/docs/how-to/llm-comparison)

A working-pathologist's decision framework for which AI model to open for which task. Covers the four major providers (Anthropic, OpenAI, Google, Meta), the tier system (flagship / medium / small / reasoning models), pathology-specific picks for every use case across the three pillars, cost realities, privacy considerations, and how to stay current as the landscape shifts.

### [Tokens, context windows, and APIs — how the plumbing works](library.html#/docs/how-to/tokens-and-apis)

The technical literacy layer. What a token is, why pricing is structured the way it is, the difference between the web UI and the API, common parameters worth understanding (temperature, system message, streaming), prompt caching, embeddings, open-weight models, and a glossary card for the vocabulary. Intended for the clinician who has used ChatGPT in the browser and is starting to wonder whether they should build something.

---

## Making the library yours

### [Adapting prompts to your subspecialty](library.html#/docs/how-to/adapt-prompts-to-subspecialty)

The library defaults to heme-path / CP framing. Four worked rewrites — dermpath, peds path, forensic, cytopath — show how to adapt any library prompt to your subspecialty by editing four predictable slots (audience, vocabulary, institutional context, conventions). The skill compounds: the first adaptation takes 20 minutes; the tenth takes 3.

### [Common mistakes and antipatterns](library.html#/docs/how-to/common-mistakes)

The catalog of "what not to do" — twelve antipatterns ranked by frequency and consequence. Over-reliance, single-shot mindset, copy-paste-without-editing, citing AI as a source, building unused notebooks, letting AI write things you can't defend. Read once for orientation; come back when you notice yourself drifting.

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

## Scholarly and ethical practice

### [Disclosure and authorship — crediting AI in academic work](library.html#/docs/how-to/disclosure-and-authorship)

When and how to disclose AI use in manuscripts, posters, slides, letters of recommendation, and teaching materials. Current journal policy (ICMJE, JAMA, NEJM, Lancet, BMJ), worked disclosure language for common scenarios, the gray-zone cases, pathology-specific norms, and the line between "AI-assisted" and "AI-written" (and why crossing it is the misconduct boundary).

---

## Read this before you use anything

The [Guardrails](library.html#/docs/guardrails) page covers PHI, accuracy verification, bias, authorship/disclosure norms, and the structural plausibility failure mode in AI-assisted writing. It's short. Read it once.
