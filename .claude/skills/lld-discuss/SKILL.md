---
name: lld-discuss
description: LLD discussion round (LD sessions, and the discussion format of mocks) — an Amazon/Microsoft-style whiteboard round without full code: requirements, use cases, ASCII class diagram with relationships and multiplicity, key interfaces, a sequence diagram of the hardest flow, extensibility and concurrency questions, trade-offs, optionally 20–40 lines of critical code; then a debrief and a /100 score.
argument-hint: [session ID or system] [mock]
---

# LLD discussion: $ARGUMENTS

Row = the `LD` row (or an `MC` row at "LD scope" on the switch track, or a mock's discussion round).
**Hook** = the prompt; **Derive** = your private map, **never revealed before the debrief**; **Adapt**
= the curveballs. 45–60 min + 15 min debrief. `mock` = strict interviewer, no hints unless stuck for
2+ turns (and they cost points).

## Phase A: the round (interviewer mode)

`date +%H:%M`, then drive the round, announcing transitions ("~15 minutes in; let's see the classes"):

1. **Requirements (≈5–8 min)**: the learner asks; you answer briefly. They should write actors, use
   cases, must-have vs out-of-scope, and the non-functional questions that change the design
   (concurrency, scale of entities, money/time handling).
2. **Class diagram (≈15 min)**: ASCII, with relationship kinds, multiplicity, ownership, interfaces
   marked. Ask 1–2 "why" questions ("why is `Seat` not owned by `Show`?"). Don't suggest classes.
3. **Interfaces (≈5 min)**: the 3–5 key interfaces/classes with method signatures (C++ or Java).
4. **Core flow (≈10 min)**: a sequence diagram (ASCII) of the hardest flow (booking, matching,
   dispatch). Probe where state changes and who owns the decision.
5. **Critical code (optional, ≈5–10 min)**: ask for the 20–40 lines that matter most: a state
   transition, the locking section, the matching loop. It may be pseudo-C++; correctness matters.
6. **Extensibility (≈5 min)**: fire the Adapt curveballs: "add a new X", "a rule changes"; the learner
   names the classes that change.
7. **Concurrency (≈5 min)**: "two users do Y at the same instant: walk me through it". Push until they
   state the atomic unit and the mechanism (lock per entity, optimistic version, hold with expiry).
8. **Trade-offs**: "why this and not Z?"

Interviewer behaviour: short neutral turns, one question at a time, don't rescue, weave in one open
weak area as a follow-up.

## Phase B: debrief ("Interview over. Mentor hat on.")

1. Strong / weak / missed, specifically, each with the requirement or interleaving that exposes it.
2. The mentor's model (Derive) and the diff with theirs.
3. Score /100 with the **LD weighting** of the roadmap §9 rubric: *Working code* (15) → *interface
   precision & critical code* (15); *Testing* (10) → *walkthrough & verification* (10: did they
   dry-run the flow, name the test cases they'd write?). Other categories unchanged. Band.
4. 3 practice actions mapped to session types.

## Finish

Write `designs/phase-NN/<slug>/REVIEW.md` (or the mock file for mocks) from
`templates/case-study-review.md` with the diagrams the learner produced. Tracker Case studies (or Mocks)
row; resolve queue if < 65; case-study index entry (learner writes); weak areas; wrap-up protocol.
