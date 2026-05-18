---
title: The LLM landscape — which model to use when, with pathology examples
last_updated: 2026-05-18
difficulty: advanced
category: tools
---

A working pathologist does not need to know the architecture of a transformer or the gradient-descent optimizer that trained it. What they need is a decision framework for "given a specific teaching, learning, or operational task, which AI tool should I open?" — because the answer changes by task, by model, and by the month.

This guide gives you that framework. It assumes nothing about your prior exposure to LLMs; it ends with concrete recommendations for each pillar of the library.

---

## Part 1 — Why this matters

The decision of *which* LLM to use changes the output more than most pathologists realize. The same prompt, the same context, the same question — asked of different models — produces meaningfully different answers in detail level, accuracy on rare entities, tendency to hedge, ability to follow format constraints, and (critically for our work) tendency to fabricate citations or numerical thresholds.

A clinician who uses only one LLM is making a tool choice the same way they'd be making a microscope choice if they only owned one objective. Sometimes the cheap fast one is correct; sometimes it isn't; the practiced user knows when to switch.

The cost of trying multiple tools is low. The cost of using the wrong one for a high-stakes task is high.

---

## Part 2 — The major providers (as of 2026)

Four providers matter for pathology educators right now. A handful of others matter for specialty use cases.

### Anthropic — Claude

Anthropic's Claude family is the default the library is built around, for three reasons specific to medical work:

- **Calibrated refusal.** Claude is more willing to say "I don't have enough information to answer this" than competitors, which is the right reflex for clinical questions where confident-wrong is the dangerous failure mode.
- **Longer working context.** Claude's context windows have led the industry through 2025–2026, which matters when you're synthesizing across multiple guideline documents or long teaching cases.
- **Strong instruction following.** Claude reliably honors format constraints ("respond as three paragraphs with the layer named at the start"), which is exactly what the library's prompts depend on.

Current model tiers:

- **Claude Opus 4.7** — the flagship. Highest reasoning quality, best for ambiguous clinical scenarios, paper critique, designing OSCEs that have to be defensible. Slower, more expensive per token. Use it when you'd otherwise ask a colleague for a second opinion.
- **Claude Sonnet 4.6** — the workhorse. Used by ~70% of the library's prompts. Fast enough for iteration, accurate enough for board-prep work, calibrated enough not to bluff. This should be your default unless you have a reason to escalate or de-escalate.
- **Claude Haiku 4.5** — the small/fast model. Use it for high-volume low-stakes tasks (drafting many flashcards, summarizing many short articles, generating dozens of MCQs to be reviewed in bulk). Cheaper, faster, less depth.

Access: claude.ai (web UI), the Anthropic API, or via Claude Projects (the source-grounded equivalent of NotebookLM).

### OpenAI — ChatGPT

The most widely used LLM family, period. Different strengths than Claude:

- **Stronger multimodal.** OpenAI's image-handling has historically been the most polished — useful for any prompt that involves uploading a photomicrograph, gel image, or chart.
- **Reasoning models.** The "o-series" (o1, o3, o4) use extended chain-of-thought before responding. They are slower and more expensive per query but materially better at problems that require explicit step-by-step reasoning. For an unusual molecular result interpretation or a multi-step diagnostic algorithm, the reasoning models earn their cost.
- **Custom GPTs.** The OpenAI equivalent of Claude Projects / NotebookLM — you can build a persistent "GPT" that's loaded with your sources and shareable with colleagues.

Current model tiers (the naming is unfortunately complicated):

- **GPT-4.5 / GPT-5** — flagship general-purpose, comparable to Claude Opus
- **GPT-4o / GPT-4o-mini** — the fast workhorse and the small/cheap variant
- **o3 / o4** — reasoning models for complex problems

Access: chatgpt.com (web UI), the OpenAI API, Custom GPTs in the same UI.

### Google — Gemini and NotebookLM

Google's Gemini family powers two things you care about:

- **Gemini in its own UI** (gemini.google.com) — general-purpose chat. Strengths: very long context (often the longest of any provider), strong at math/code, free tier is generous. Weaknesses: tends to be more terse than Claude or GPT and historically more prone to hallucinated citations on medical questions.
- **NotebookLM** — Google's source-grounded notebook tool, built on top of Gemini but with strict retrieval discipline. The library has an entire [decision guide](library.html#/docs/how-to/notebooklm-vs-claude-projects) on when NotebookLM beats Claude Projects. Briefly: NotebookLM is the strongest tool when your single requirement is "answer ONLY from the documents I uploaded, with citations back to the source passage."

Current Gemini tiers:

- **Gemini 2.5 Pro** — flagship, multimodal, long context
- **Gemini 2.5 Flash** — fast and cheap
- **NotebookLM** — separate product, source-grounded

Access: gemini.google.com, notebooklm.google.com, or the Google AI Studio API.

### Meta — Llama (open-weight)

Llama is the most prominent **open-weight** family — meaning the model weights are downloadable and can be run on your own hardware. For most pathologists this is irrelevant; for a few specific situations it matters:

- **You have absolute confidentiality requirements** that prohibit any data leaving your network. Running Llama on a local GPU means the data never crosses your firewall.
- **You're building a custom tool** for your institution and want to host the model yourself.
- **You want to fine-tune** a model on your own materials (rare, but Llama supports this).

Quality-wise, the flagship Llama models are roughly one tier behind Claude / GPT / Gemini flagships. For 99% of educational use, you should use the hosted commercial models.

Access: Meta releases the weights; you run them yourself (or use a hosting service like Together AI, Groq, or Hugging Face Inference).

---

## Part 3 — A few specialty tools worth knowing

Not LLMs themselves, but built on top of them:

- **Perplexity** — search-grounded LLM. Answers questions by searching the live web and citing real URLs, with the model synthesizing across results. Useful when you need *current* information (the model's training cutoff doesn't include this week's NEJM). Less useful when you need depth on a single topic — the search-grounding pulls toward whatever's most-cited online, which is sometimes shallow.
- **NotebookLM** (covered above) — source-grounded, citation-strict.
- **Claude Projects** (covered above) — persistent project context with both source-grounding and broader reasoning.
- **GitHub Copilot, Cursor, Claude Code** — coding assistants. Not directly clinical, but if you're building tools (like this site) they matter.
- **Voice models** (Whisper, gpt-4o voice, ElevenLabs) — for transcription and audio. Useful for converting sign-out audio into structured notes (with strict PHI controls).

---

## Part 4 — The model-tier decision

Within any provider, picking the right tier is more important than picking the right provider.

| Tier | When to use | When not to |
|---|---|---|
| **Flagship** (Opus, GPT-4.5/5, Gemini Pro) | High-stakes, ambiguous, or long-context work. Paper critiques, OSCE design, anything you'd send to a colleague for review. | Routine tasks. You'll pay 3-10× more for a marginally better answer. |
| **Medium** (Sonnet, GPT-4o, Gemini Flash) | The default for almost everything. Self-quizzing, comparison drills, slide outlines, rotation materials. Fast iteration, accurate enough. | When you've tried it and the answer was wrong on a critical detail — escalate to flagship for a second pass. |
| **Small** (Haiku, GPT-4o-mini) | High-volume drafting: many MCQs at once, many flashcards, many summary paragraphs to be reviewed in bulk. Bulk tasks where you'll edit downstream anyway. | Anything where the first answer needs to be high quality. Don't use for OSCE design. |
| **Reasoning** (o3, Claude with extended thinking) | Multi-step diagnostic puzzles. Unusual molecular results. Anything where the answer requires *showing the work*, not just stating the conclusion. | Quick factual questions. Reasoning models are slow and expensive for tasks that don't need them. |

The most common pathologist mistake is defaulting to flagship for everything ("I want the best, so I'll use Opus"). The better discipline is: start at medium, escalate when you have a specific reason.

---

## Part 5 — Pathology-specific picks, by pillar

### Pillar I — Self-Education

| Use case | Best tool | Why |
|---|---|---|
| Concept explanation at level | Claude Sonnet 4.6 | Strongest at calibrated three-layer explanations. The library defaults to this. |
| Self-quizzing one MCQ at a time | Claude Sonnet 4.6 or GPT-4o | Both are accurate; switch if either gives confident-wrong on your subspecialty. |
| Bulk MCQ generation (50+) | Claude Haiku 4.5 or GPT-4o-mini | High volume; you'll review downstream anyway. |
| Diagnostic algorithm walkthrough | Claude Opus 4.7 (or o3 for unusual cases) | Multi-step reasoning earns the flagship. |
| Multimodal photomicrograph | GPT-4o or Claude Sonnet 4.6 | GPT historically polished on image input; Claude has narrowed the gap. Try both. |
| Source-grounded board prep notebook | NotebookLM | Strictest grounding; citations link to source passages. |
| Source-grounded sign-out preview | Claude Projects | Better when you also want broader reasoning beyond the strict corpus. |
| Paper critique against your corpus | Claude Opus 4.7 in a Project | Needs reasoning + source-grounding. |
| Cross-source comparison | NotebookLM | Built for "how do these sources differ on X?". |

### Pillar II — Teaching

| Use case | Best tool | Why |
|---|---|---|
| One-hour slide outline | Claude Sonnet 4.6 | Strong at structured outlines with named sections. |
| Speaker notes for existing slides | GPT-4o or Claude Sonnet 4.6 | Either works; pick whichever you're already in. |
| Case vignette generation | Claude Sonnet 4.6 | Calibrated to PGY level reliably. |
| Matched case-pair distractors | Claude Opus 4.7 | The "match the original but change ONE feature" task benefits from flagship reasoning. |
| OSCE station design | Claude Opus 4.7 | High stakes — students' eval depends on it. |
| Bloom-leveled MCQs | Claude Sonnet 4.6 | Reliable at hitting the requested cognitive level. |
| Resident feedback note drafting | Claude Sonnet 4.6 | Calibrated, doesn't over-praise or under-document. |
| Letter of recommendation starting draft | Claude Opus 4.7 | Worth the flagship for something a colleague will read. |
| Visual metaphor brainstorm | GPT-4o or Claude Sonnet 4.6 | Creative tasks where divergence is the goal — try both. |
| Microscopy teaching session structure | Claude Sonnet 4.6 | Strong at structured pedagogical formats. |

### Pillar III — Educational Operations

| Use case | Best tool | Why |
|---|---|---|
| Rotation orientation one-pager | Claude Haiku 4.5 or GPT-4o-mini | Format-driven, repeatable; small model is fine. |
| Reading list (PGY-calibrated) | Claude Sonnet 4.6 | Needs to be accurate on landmark papers; medium tier is right. |
| Daily / call / block schedules | Claude Haiku 4.5 | Almost entirely format work. |
| Evaluation rubrics | Claude Sonnet 4.6 | Rubric design needs calibration on what "competent" means at level. |
| Workshop run-of-show | Claude Sonnet 4.6 | Structured operational document. |
| Conference packet | Claude Sonnet 4.6 | Multi-document synthesis. |
| Medical education abstract | Claude Opus 4.7 | Single-shot polish matters. Worth flagship for something going to a journal. |
| IRB / QI protocol skeleton | Claude Opus 4.7 | Compliance language has narrow margin for error. |
| Promotion portfolio narrative | Claude Opus 4.7 | Career stakes. Use the best tool. |

---

## Part 6 — Cost: a practical note

Educational use of the major LLMs is genuinely cheap. Typical pathologist usage patterns:

- **Web UI subscription**: $20/month for ChatGPT Plus, Claude Pro, or Gemini Advanced. This covers nearly all interactive use for one person. Includes all model tiers, file uploads, and the source-grounded notebook tools.
- **API usage** (only if you're building tools): metered per token. For typical educational tasks, even heavy use rarely exceeds $5–20/month per active user. The library's prompts, for instance, cost fractions of a cent each via API.
- **NotebookLM**: free tier covers ~50 notebooks, generous query limits. Paid tier (Google One AI) is $20/month.

The principle: **don't optimize for cost in education**. The expensive thing is your time, not the API bill. Pick the tool that gets the right answer fastest, not the one that saves $0.04 per query.

The single exception: if you're building a tool that will run continuously (e.g., a residency match scoring system), then API costs become a real budget item and the cheap-fast-tier discipline matters.

---

## Part 7 — Privacy considerations (per provider)

Brief, because the [Privacy and copyright for source-grounded AI](library.html#/docs/how-to/privacy-and-copyright) guide covers this in depth:

- **All major providers** (Anthropic, OpenAI, Google) offer enterprise / business tiers with stricter data segregation — your inputs are not used for training. Consumer tiers vary; read the current ToS.
- **Patient material**: never upload to any of them. The institutional risk is not worth the marginal educational benefit. Use published teaching material instead.
- **Open-weight models** (Llama, Mistral, others run locally) are the only way to guarantee data never leaves your hardware. For pathologists, this matters in research contexts where you're working with truly sensitive corpora.

---

## Part 8 — Staying current

The model landscape changes every 2–4 months. A guide written today is partially obsolete in a quarter. To stay current without becoming a hobbyist:

- **Re-evaluate quarterly.** Once every three months, run your two or three most-frequent prompts through the current flagship of each provider. Note any meaningful quality changes.
- **Watch for capability changes, not just version numbers.** A new model with the same family name can have substantially different behavior — better at images, worse at long context, more cautious, less cautious.
- **Subscribe to one summary source**, not many. Anthropic's [news page](https://www.anthropic.com/news), Simon Willison's blog, or one substack you trust. Don't drown in AI Twitter.
- **Trust your own benchmarks more than vendor benchmarks.** A model that wins on MMLU might lose on your specific pathology question.

---

## Part 9 — A short decision tree

When you have a task, walk this in order:

1. **Is the task source-grounded?** (you have specific documents the answer must come from)
   - Strict citation requirement → **NotebookLM**
   - Sustained project across weeks → **Claude Projects**
   - Quick paste-in → generic chat with sources pasted

2. **Is the task high-stakes or ambiguous?** (clinical decision, OSCE design, letter of rec)
   - Yes → **Claude Opus 4.7** (or reasoning model if multi-step)
   - No → continue

3. **Is the task high-volume or bulk?** (50 MCQs, many flashcards, many summaries)
   - Yes → **Claude Haiku 4.5 / GPT-4o-mini**, review in bulk
   - No → continue

4. **Default**: **Claude Sonnet 4.6** for most everything else.

5. **If the answer feels wrong**, switch providers (Claude ↔ GPT) for a second opinion before assuming the model is right. Different models hallucinate different things.

---

## Part 10 — One honest closing note

The list of "which model is best" will be different a year from now. The discipline is what stays the same:

- Match tool to task, not to habit.
- Verify before trusting.
- Switch tools when one keeps getting it wrong.
- Don't pay attention to model names; pay attention to behavior on *your* prompts.

If you internalize that, the specifics in this guide will keep updating themselves.
