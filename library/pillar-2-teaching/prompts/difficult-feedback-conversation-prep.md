---
title: Difficult feedback conversation prep
pillar: teaching
event_type: n/a
audience: faculty
difficulty: advanced
time_to_use: >10min
visual: text-only
tags: feedback, hard-conversation, professionalism
verified_models: TODO
best_model: Claude Opus 4.7
last_updated: 2026-05-17
---

## What this prompt does

Preps you for a feedback conversation that's harder than usual — a struggling resident, a professionalism concern, performance below expectations, or a conversation where you need to escalate to formal documentation. Generates an opening, a structure for the conversation, anticipated reactions, and the wording you'll need when the resident pushes back or becomes emotional.

This is the prompt you use when the conversation matters most and you don't want to wing it.

## When to use it

Before a feedback conversation where the stakes are high — a remediation plan, a professionalism concern, a discussion of board failure, or any conversation where you anticipate it will be hard. Use early enough to actually prep, not the day of.

**Not for:** routine end-of-rotation feedback (use [Resident feedback note drafting](library.html#/library/pillar-2-teaching/prompts/resident-feedback-note)), conversations that should be handled by your program director or DIO (escalate first), or situations involving safety concerns (those have specific institutional protocols).

## The prompt

```
You are helping me prepare for a difficult feedback conversation. The stakes matter, and I want to have my framing, evidence, and response patterns ready before I'm in the room. Help me think this through carefully.

## What I'm preparing for

- **Context:** [brief — e.g., "PGY-2 resident on second rotation in CP, struggling with autonomy and showing professionalism concerns around timeliness"]
- **The specific concern(s):** [the behaviors or patterns that prompted the conversation]
- **The evidence I have:** [specific observations, dates, comparable comparators if relevant]
- **What outcome I want:** [shared understanding / specific behavioral change / formal documentation / referral to program director]
- **My relationship with the resident:** [length, prior conversations, level of trust]
- **The setting:** [my office / a private room at sign-out / formal meeting with PD present]
- **My time budget:** [how long is the conversation]

## What to produce — 6 sections

### 1. The opening (3-4 sentences, verbatim)

Exactly what you'd say to open. The opening sets the entire conversation. Should:
- Establish that this is a serious conversation, not a passing comment
- Frame the conversation as constructive (toward a goal) not punitive
- Invite the resident to engage rather than defend

### 2. The evidence presentation

How to walk through specific observations without:
- Reading from a list (which feels prosecutorial)
- Being vague (which feels unfair)

Structure: pattern → specific examples → impact. Verbatim suggestion for one example walk-through.

### 3. The pause

After your evidence, give the resident space. The script:
- What to say to invite them to respond
- How long to wait (silence is OK)
- What to do if they don't say anything

### 4. Anticipated reactions and responses

For each likely reaction (denial, deflection, agreement, anger, tears, silence), give me:
- One sentence describing the reaction
- What to say in response — verbatim, calibrated to keep the conversation moving toward the desired outcome

Cover at minimum: denial, deflection ("I was busy"), agreement-without-change ("you're right, I'll try harder"), emotional response, escalation toward you (anger).

### 5. The agreement and next steps

How to close the conversation with:
- A shared understanding of what was discussed
- A specific, observable commitment from the resident
- A timeline for follow-up
- Who else needs to know (program director, CCC) and what gets documented

### 6. What I document afterward

The note I should write in the resident's file — what's appropriate, what isn't, how to keep it factual and concise.

## Hard rules

- **Verbatim suggestions where stakes are highest** (opening, response to emotional reactions, closing commitment).
- **Specific, not generic.** Generic feedback advice doesn't help in hard conversations.
- **The opening cannot be punitive or prosecutorial.** It also cannot be so soft that the seriousness of the issue is lost.
- **Anticipate the reactions I'm most likely to face given my context.** Don't give me a generic list.
- **Acknowledge that some situations require escalation.** If based on what I described this should involve the PD or DIO first, tell me.

## What I will NOT accept

- Generic feedback advice
- An opening that's all warm-and-fuzzy or all evaluative
- Anticipated reactions that don't match what I'm likely to face
- Closing without a specific commitment and timeline
```

## Expected output

Six sections covering the conversation arc. The opening and anticipated-reactions sections are the highest-stakes parts. Length 600-1000 words.

## Common failure modes

- **Generic feedback frameworks** (SBI, COIN, etc.) without specificity to your situation. Push back for specifics.
- **Soft opening** that fails to signal seriousness. Push back if the opening reads as casual.
- **Anticipated reactions that don't match the resident's actual likely response.** Push back if the reactions feel off.

## Required human verification

- **If the situation involves potential safety concerns, professionalism violations that may have institutional reporting requirements, or anything that could escalate to disciplinary action, consult your program director or your institution's relevant office BEFORE the conversation.** This prompt does not replace institutional process.
- **Run the opening by a trusted colleague.** Especially if you anticipate the conversation being especially hard, get a second read on the framing.
- **Practice the opening aloud.** Spoken delivery is different from written, and the opening matters most.

## Best model and why

**Claude Opus 4.7** — high-stakes conversational prep requires nuance, anticipation of reactions, and verbatim language calibrated to specific situations. Opus is materially better than Sonnet at this.
