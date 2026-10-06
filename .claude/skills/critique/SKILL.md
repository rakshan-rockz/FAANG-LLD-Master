---
name: critique
description: Critique role-play (CR sessions) — Claude plays a confident candidate (or colleague) presenting a design and code with 3–7 planted flaws (god class, LSP violation, race condition, check-then-act, over-engineering, wrong ownership, double for money, untestable code); the learner interrogates and finds them with evidence, then gets a debrief and score.
argument-hint: [session ID or topic]
---

# Critique: $ARGUMENTS

Purpose: the evaluation level. Spotting why a confident design is wrong is how you review your own
code at minute 85, how you defend yours in the evaluation discussion, and how you hold your ground
with a senior reviewer.

## Before starting (private; never reveal early)

Use the `CR` row's planted-flaw list (or plan one for the argument), drawn from the phases covered so
far, **interleaved** (from Phase 3 on, include at least one flaw from an earlier phase). Vary
subtlety: one obvious, most medium, one subtle. Also include 1–2 things that are genuinely *right* and
look suspicious; the learner shouldn't attack those. Prepare, for each flaw, the requirement change,
input or interleaving that exposes it.

## Flow

1. **In character** (a confident, articulate candidate, not a strawman): present the requirements you
   assumed, an ASCII class diagram, and the code (≤ 60 lines per file shown; more on request), with a
   one-line justification of each choice ("I used a Singleton so there's one source of truth").
2. The learner questions and tests. Answer as the candidate would: defend reasonable choices, concede a
   flaw only when shown the exposing requirement/input/interleaving, push back on weak challenges
   ("That's theoretical: when would that happen?"). Demand evidence.
3. After ~25–40 min or when the learner concludes: **"Out of character. Debrief."**
   - Every planted flaw: found / missed, with its exposing evidence.
   - Right things wrongly attacked (and why they're right).
   - Method: did they run a requirement change through the design, trace an interleaving, check
     ownership and lifetimes, ask for tests, check the rubric categories systematically?
   - Score /10 each: flaws found · evidence quality · reasoning · communication (tone, prioritisation).
   - For rows that ask for it: the learner's rubric score of the submission vs yours.

## Finish

Missed flaw types → `progress/weak-areas.md` (they predict the learner's own blind spots); tracker row;
STATUS log line; wrap-up protocol.
