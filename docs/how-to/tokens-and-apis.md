---
title: Tokens, context windows, and APIs — how the plumbing works
last_updated: 2026-05-18
difficulty: advanced
category: tools
---

You don't need to understand the math of how a language model is trained. But you do need to understand the unit it charges by, the limit it operates within, and the difference between the chat window and the API — because all three change which prompts you can run, what they cost, and where they break.

This guide gives you that mental model. The intended audience is a clinician who has used ChatGPT or Claude in the browser and is starting to wonder whether they should build something with the API.

---

## Part 1 — What is a token?

A token is the unit a language model thinks in. It's roughly a syllable, a short word, or part of a longer word. It is *not* a character and *not* a word. The exact tokenization depends on the model.

Some intuition:

- "Pathology" is 1 token in most modern tokenizers.
- "Hematopathology" is usually 2–3 tokens.
- "MGUS" is usually 1 token.
- "M-spike" is usually 2 tokens.
- A typical English sentence is roughly 1 token per word, sometimes a little more.
- A typical paragraph of medical writing is 100–200 tokens.
- A typical guideline document (10 pages) is 5,000–10,000 tokens.

You can use OpenAI's [Tokenizer](https://platform.openai.com/tokenizer) or similar tools to see exactly how a piece of text breaks down. Useful one-time exercise: paste a paragraph from your own notes and look at the segmentation. You'll never forget what a token is after that.

**Why this matters:** every limit and every price in an LLM is expressed in tokens. Context window: tokens. Pricing: tokens. Rate limits: tokens. If you think in characters or words, you'll mis-estimate everything.

---

## Part 2 — Input vs output tokens

Every API call has two token counts that get billed separately:

- **Input tokens** — everything you send to the model: the prompt, the system message, the uploaded document, the conversation history, the few-shot examples. Cheaper per token.
- **Output tokens** — everything the model generates back. More expensive per token (usually 3–5× the input rate).

Why the asymmetry? Generating output is computationally more expensive than processing input. The model has to run its full inference pass for each output token; input tokens get processed in parallel.

**Practical implications:**

- Long prompts with short answers are cheap.
- Short prompts with long answers (e.g., "write me a 5,000-word case write-up") are expensive even though the input is tiny.
- If you're processing the same long document repeatedly (a guideline you keep asking questions of), you're paying for the input tokens *every single time* unless you use prompt caching (see Part 9).

---

## Part 3 — The context window

The context window is the maximum number of tokens (input + output, combined) that the model can hold in its working memory for a single conversation. When you exceed it, older messages start to drop off the front, and the model literally cannot see them anymore.

Current context windows (as of 2026):

- **Claude Sonnet 4.6**: 1M tokens (~750,000 words, or a small textbook)
- **Claude Opus 4.7**: 1M tokens
- **GPT-4o**: 128K tokens (~95,000 words)
- **Gemini 2.5 Pro**: 2M tokens (currently industry-leading)
- **Llama 3 (open weights)**: typically 128K, varies by deployment

For most pathology educational use, a 200K window is plenty. You start to need the very large windows when you're working with:

- Multiple long guideline documents in one conversation
- A full textbook chapter plus your own teaching notes
- A long sign-out / case-series transcript you're asking nuanced questions of
- An entire week of journal articles you're synthesizing

**The hidden gotcha:** even within the official window, model performance degrades on very long contexts. A model with a 1M-token window may struggle to "find" a specific fact buried at token 800,000 unless you draw its attention there explicitly. This is called the *needle-in-a-haystack* problem and the major models perform on it differently. Treat the official context window as a soft upper limit, not a guarantee of quality.

---

## Part 4 — How pricing works (and what it actually costs)

Pricing is per million tokens (MTok), separately for input and output. Approximate rates as of 2026 (these change frequently — always check the vendor page):

| Model | Input $/MTok | Output $/MTok |
|---|---|---|
| Claude Opus 4.7 | $15 | $75 |
| Claude Sonnet 4.6 | $3 | $15 |
| Claude Haiku 4.5 | $0.25 | $1.25 |
| GPT-4.5 / GPT-5 | $10–30 | $30–120 |
| GPT-4o | $2.50 | $10 |
| GPT-4o-mini | $0.15 | $0.60 |
| Gemini 2.5 Pro | $1.25 | $5 |
| Gemini 2.5 Flash | $0.075 | $0.30 |
| o3 (reasoning) | $15 | $60 |

**Worked examples for pathology workflows:**

- *Self-quizzing session* — 20 questions, ~300 input tokens each, ~400 output tokens each, on Claude Sonnet:
  20 × (300 × $3/1M + 400 × $15/1M) = **$0.14 for an hour of board prep**

- *Generating 50 MCQs* — 1,000-token prompt, 500-token output per question, on Claude Haiku:
  1,000 × $0.25/1M + 50 × 500 × $1.25/1M = **$0.03 for the whole batch**

- *Paper critique* — 8,000-token paper + 1,000-token prompt, 2,000-token response, on Claude Opus:
  9,000 × $15/1M + 2,000 × $75/1M = **$0.29 per paper**

- *Generating a 10-slide lecture outline* — 500-token prompt, 3,000-token output, on Claude Sonnet:
  500 × $3/1M + 3,000 × $15/1M = **$0.05 per lecture**

For comparison: a single Starbucks latte funds about 500 self-quizzing sessions or 200 paper critiques.

The web UI subscriptions ($20/month for ChatGPT Plus, Claude Pro, Gemini Advanced) wrap all of this in a flat fee with usage limits high enough that interactive personal use never approaches the cap.

---

## Part 5 — Rate limits

Two kinds:

- **Requests per minute (RPM)** — how many API calls you can make.
- **Tokens per minute (TPM)** — total token throughput allowed.

For interactive personal use, both are wildly higher than you'll ever hit. Where they matter:

- **Bulk operations** (processing 500 articles in a batch script)
- **Multi-user applications** (a residency-wide tool)
- **Real-time streaming workflows**

Vendors publish their per-tier limits. New API accounts start at the lowest tier and rate-limit-bump as you build usage history. If you're scaling, this is something to plan around; for most pathology educational use, you'll never see a rate limit.

---

## Part 6 — Web UIs vs APIs (when to use which)

The same underlying model is available two ways:

### Web UI (claude.ai, chatgpt.com, gemini.google.com)

- One human, one keyboard, conversational interface
- Includes file upload, image upload, voice, persistent conversations
- Source-grounded variants (Custom GPTs, Claude Projects, NotebookLM) live here
- Flat-fee pricing (~$20/month)
- This is what 95% of pathologists need, 100% of the time.

### API (programmatic access)

- Your code calls the model
- Streaming responses back to your software
- Per-token billing, no flat fee
- Required for: building a tool, automating a workflow, integrating into other systems
- Skill required: at minimum, basic comfort with a programming language (Python, JavaScript, or curl-from-the-terminal)

**The transition point** for a pathology educator: when you start saying "I wish this happened automatically every Monday morning" or "I wish residents could submit X and have it processed without my involvement." That's when you cross from the UI to the API.

This site, for instance, uses the API in three places: the Cloud Functions that email you on new submissions, the returning-visitor lookup, and the feedback widget's underlying Firestore call. None of those would work as a pasted-in chat conversation.

---

## Part 7 — Common API parameters worth understanding

If you're using the API at all, four parameters shape every call. The web UI hides them; the API exposes them.

### Temperature

Controls randomness, scale 0 to 1 (or 0 to 2 depending on vendor).

- **0** = deterministic, same output every time
- **0.7** = the default for most casual chat — varied, natural-sounding
- **1.0+** = creative, unpredictable, sometimes incoherent

For pathology educational work:

- **Use 0–0.2** when you want consistency: generating standardized MCQs, structured rubrics, anything that needs to look the same each time.
- **Use 0.5–0.8** for divergent thinking: visual metaphor brainstorm, OSCE scenario ideas, "give me five different ways to explain this."
- **Avoid >1.0** for anything clinical.

### Max output tokens

Hard cap on how long the response can be. Set this when you have a specific length budget. Useful for cost control on long-output tasks. Note: setting it too low will truncate mid-sentence.

### Top-p (nucleus sampling)

Similar to temperature, controls the breadth of vocabulary the model considers per token. Most users should leave this at default (0.95–1.0) and only adjust temperature.

### System message

A special "voice in the model's ear" that frames the whole conversation. Different from a regular prompt — the system message says "you are X, do Y, never Z" and persists across all turns. The library's role-setting prompts ("Act as an experienced hematopathology attending") would more properly be in the system message slot when used via API.

---

## Part 8 — Streaming responses

When the model generates output, it does so token by token (~30–50 tokens per second for fast models, slower for flagships and reasoning models).

- **Non-streaming**: you wait for the full response, then it appears all at once. Simpler to write code for.
- **Streaming**: tokens arrive as they're generated, like watching someone type. Better user experience for any interactive use; the user sees progress, can interrupt early, doesn't stare at a spinner.

If you're building a tool with a user-facing interface, streaming is almost always worth the extra code. If you're processing in batch (no human watching), non-streaming is simpler.

---

## Part 9 — Prompt caching (Anthropic's killer feature)

Anthropic introduced **prompt caching** in 2024 and it changes the economics of source-grounded work substantially.

The problem: if you're asking questions of a 50,000-token guideline document, you pay for those 50,000 input tokens on every single question. Ten questions = 500,000 input tokens you've paid for, and the model has done the same processing ten times.

With prompt caching:

- You mark a portion of the prompt as cacheable (e.g., the guideline document)
- First request: pays full price plus a small write fee
- Subsequent requests (within ~5 minutes): pays only 10% of the input cost for the cached portion

For source-grounded workflows where the same corpus is queried repeatedly, this turns "expensive" into "negligible."

Currently: Anthropic implements this most cleanly. OpenAI has an analogous feature. Google's API supports something similar via their context-caching API. If you're building a tool that asks many questions of a fixed corpus, design with caching in mind.

---

## Part 10 — Embeddings, briefly

You'll see the word "embeddings" in any technical AI discussion. Quick definition:

An **embedding** is a numerical vector representing the *meaning* of a piece of text. Two semantically similar pieces of text have similar vectors; semantically different pieces have different vectors.

Use cases pathologists encounter:

- **Semantic search** ("find the article in my collection most relevant to this question") works on embeddings, not keyword matching.
- **RAG** (retrieval-augmented generation) — the architecture underneath NotebookLM and Claude Projects — uses embeddings to pull the most-relevant chunks of your sources for each question.
- **Deduplication** — finding two patient cases that describe the same entity differently uses embedding similarity.

You usually don't need to think about embeddings directly; the tools (NotebookLM, Claude Projects, custom RAG systems) handle them. But if you ever build a search interface for your own materials, this is the substrate.

Cost: very cheap. Generating an embedding for a paragraph costs fractions of a cent.

---

## Part 11 — Open-weight models, briefly

A few terms worth being able to parse when you hear them:

- **Open-weight** — the model's parameters are downloadable. You can run it on your own hardware (Llama, Mistral, DeepSeek, Qwen). Not the same as "open source" — the training code and data are usually still proprietary.
- **Quantized** — a compressed version of the model that runs on smaller hardware. Trade-off: faster + cheaper, slightly worse quality. A typical pathologist isn't choosing quantization levels; tools like Ollama handle this for you.
- **Fine-tuned** — a base model further trained on a specific dataset to specialize it. Rare for pathology use cases because the quality of in-context learning (few-shot examples in the prompt) has caught up to fine-tuning for most tasks.
- **Parameter count** (7B, 70B, 405B) — rough proxy for capability, but not deterministic. A well-trained 70B model can outperform a poorly-trained 405B model. Don't fixate on the number.

When this matters for you: never, unless you have a research collaboration that requires the model to run on-premises (e.g., truly sensitive clinical data) or you're building tooling for an institution that prohibits external API calls.

---

## Part 12 — Practical implications

A short list of decisions this guide should now make easier:

1. **You will mis-estimate context window needs the first time.** When you hit the limit, the model will start forgetting earlier turns silently. The fix is to either summarize earlier turns into a shorter recap, or start a fresh session with the recap as the new opening.

2. **You will be surprised how cheap interactive use is.** The single biggest mistake is over-optimizing for cost on a $0.10 task. Just use the right model.

3. **You will eventually want the API.** When you start saying "I do this every week, can it just happen automatically?" the answer is yes, but it's an API call away. The transition is smaller than it looks once you have a working example.

4. **You will hit a prompt-caching aha moment** the first time you realize the same 50,000-token corpus is being re-processed on every question. When that day comes, look up your provider's caching API.

5. **You will outgrow the web UI for certain workflows.** That's a healthy sign of escalating use, not a failure of the UI.

---

## Part 13 — A glossary card to keep nearby

- **LLM** — Large Language Model. The underlying model family (Claude, GPT, Gemini).
- **Token** — the unit of text the model processes. Roughly a syllable.
- **Context window** — the maximum number of tokens the model can hold at once.
- **Input / output tokens** — billed separately, output is more expensive.
- **System message** — a persistent instruction that frames the whole conversation.
- **Temperature** — randomness control. Low for consistency, higher for creativity.
- **Streaming** — tokens delivered as they're generated, vs all at once.
- **RAG** — Retrieval-Augmented Generation. The architecture for source-grounded answers.
- **Embedding** — a vector that represents the meaning of a piece of text.
- **API** — programmatic access to the model, vs the web UI.
- **Rate limit** — how many requests / tokens you can send per minute.
- **Prompt caching** — paying once for a piece of input that's re-used across requests.
- **Open-weight** — model parameters are downloadable; you can run on your own hardware.
- **Quantized** — a compressed model that runs on smaller hardware with slight quality cost.
- **Fine-tuned** — a base model further trained for a specific use case.

If you can use all of these in a sentence without hesitation, you've moved past the curious-onlooker stage. From here it's deciding what you want to build.
