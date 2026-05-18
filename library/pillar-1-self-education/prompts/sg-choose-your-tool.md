---
title: Choose your tool — NotebookLM vs Claude Projects vs generic chat
pillar: self-education
event_type: n/a
audience: resident
difficulty: quick-win
time_to_use: <2min
visual: text-only
tags: source-grounded, notebooklm, claude-projects, decision-rubric
verified_models: TODO
best_model: Claude Sonnet 4.6
last_updated: 2026-05-18
---

## What this prompt does

A decision rubric for which AI tool to use when. Source-grounded AI (NotebookLM, Claude Projects, ChatGPT Custom GPTs) is different from generic chat — different strengths, different failure modes, different prep work. This guide tells you which one fits your task.

## When to use it

The first time you're considering uploading source materials to an AI tool. Also useful to re-check periodically as the tools evolve (capabilities shift every few months).

## The decision rubric

Walk yourself through these questions in order. The first "yes" determines your tool.

```
DECISION RUBRIC — pick the first one that matches

## Step 1: Do you need the AI to answer ONLY from the materials you provide?
(e.g., you're learning a specific guideline and don't want the model to mix in
its own knowledge, or you're studying for boards and want answers grounded only
in the source you're being tested on)

YES → Use NotebookLM (Google).
- Strongest at "answer only from these sources" grounding
- Citations link back to specific source passages
- Limited model choice (Google's underlying model)
- Free tier available; works well for personal study

GO TO Step 2 if NO.

## Step 2: Do you need to chat with sources AND have a sustained project that
evolves over weeks/months (curriculum design, rotation prep, ongoing journal club)?

YES → Use Claude Projects.
- Project persists; you can add/remove sources over time
- Stronger generic reasoning than NotebookLM if you want both source-grounding
  AND broader knowledge
- Better for collaborative team use within a single project
- Requires Claude Pro/Team subscription

GO TO Step 3 if NO.

## Step 3: Are you doing a quick task where you'd just paste the source into
the conversation each time and don't need a persistent setup?

YES → Use generic chat (Claude.ai, ChatGPT, etc.) with sources pasted in.
- Lowest friction
- No setup
- Source must fit context window
- Loses source after conversation ends

## Step 4: None of the above?

You probably want generic chat. Source-grounded tools are overhead you don't
need for casual queries.

## After picking, ask yourself:
- What's my privacy obligation for these sources? (See the privacy guide.)
- What's the copyright status? (See the privacy guide.)
- How will I verify the model is actually staying grounded vs drifting?
```

## Expected output

A clear decision: which tool you'll use for THIS use case. Plus awareness of the privacy/copyright considerations before you upload anything.

## Common failure modes

- **Defaulting to whatever tool you have a subscription for** rather than what fits the task. NotebookLM is free; if your task is "answer ONLY from these sources," it's likely better than your $20/month subscription.
- **Building a heavy Claude Project for a task that needed 10 minutes of generic chat.** Source-grounded setup is overhead; don't pay it unnecessarily.
- **Assuming the tool will "remember" sources across conversations** when it only persists within a project. Reset behavior varies by tool.

## Required human verification

- **Verify the tool's current grounding behavior before relying on it for high-stakes use.** Capabilities change every few months; what was true 6 months ago may not be true now.
- **Verify your privacy obligation** before uploading institutional materials. See the source-grounded privacy guide.

## Best model and why

This is a meta-prompt about choosing tools, not a prompt to give to a model. **Claude Sonnet 4.6** can help you think through the rubric if your case is ambiguous, but mostly you're using your own judgment here.
