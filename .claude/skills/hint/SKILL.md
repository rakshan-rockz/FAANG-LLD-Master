---
name: hint
description: Give exactly one rung up the hint ladder (H0 process nudge → H1 principle pointer → H2 observation → H3 structure → H4 walkthrough) for the design, build or concurrency problem the learner is working on, and record the rung. Never gives the full design or code in one step.
argument-hint: [problem or session ID]
---

# Hint: $ARGUMENTS

1. Identify the problem (the one in progress, or the argument; if it's outside a session, ask for the
   requirement and what they've tried).
2. Determine the current rung: the highest already given for this problem in this conversation. If
   none, first ask: "What's your current design, and which requirement change or test breaks it?" An
   answer to that is H0.
3. Give **exactly the next rung** (roadmap §8):
   - **H0** Process: a question about the process ("List what changed between the two requirements.
     Which classes did you edit?", "What's shared between these threads?")
   - **H1** Principle pointer: a principle/heuristic by name, as a question about *this* design ("Which
     principle does 'adding a type edits existing logic' violate?", "Which two operations must be
     atomic together?")
   - **H2** Observation: one specific fact about this design ("The flow is identical for every method;
     only 'how to charge' varies.", "The check and the insert are under different lock acquisitions.")
   - **H3** Structure: the abstraction / relationship / synchronisation to introduce ("An interface for
     charging, one implementation per method, chosen at construction." / "Hold one lock across check
     and insert, or use a single atomic compute.") The learner still assembles it.
   - **H4** Walkthrough: the full design and why it works. The learner still writes the code.
4. ≤ 5 lines. End by handing it back: "Try it with that. Want to talk it through?"
5. "Just tell me" → next rung; H4 only if asked again after the time box. Never paste solution code.
6. Record the rung for wrap-up: lesson note Discovery Path; in `MC`/`M`/`LD` sessions it costs rubric
   points in the category it helped; H2+ on a kata → resolve queue.
