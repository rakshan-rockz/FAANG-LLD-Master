---
name: mc
description: Machine-coding case study (MC sessions) — a timed 90-minute build in interviewer mode (clarify → model → skeleton → running core flows by minute 60 → tests), a curveball requirement change, then a mentor review, a /100 rubric score and REVIEW.md in the design folder. The learner writes all the code.
argument-hint: [session ID or system] [coached|cold]
---

# Machine-coding case study: $ARGUMENTS

Row = the `MC` row in `plan/roadmap/phase-NN.md` (or the argument). **Hook** = the prompt. **Derive**
= your private map of the expected discovery: **never reveal any of it before the build is over.**
**Adapt** = curveballs. **When-NOT** = over-engineering traps to watch for. If the switch-track Scope
says "LD scope", run `/lld-discuss` instead with ~40 lines of the core coded. Mode: `coached` in
Phase 8 (hints on request, each costs points; you call the time), `cold` from Phase 9 (hints cost
points everywhere; no unsolicited help). Language: the MC language in `progress/profile.md`.
Before starting, read `reference/case-study-index.md` and `progress/weak-areas.md`; plan one follow-up
question that probes an open weak area.

## Phase A: the build (interviewer mode)

1. `date +%H:%M`. Brief in character. State the prompt as the row's Hook, no more. If the row is
   Flipkart-style, give it as a short problem document: 4–6 must-haves + 2 "bonus" items, deliberately
   silent on concurrency, scale, money representation and edge cases.
2. **Clarify (0–10)**: answer questions briefly and consistently (write your answers down so later
   answers don't contradict). Don't volunteer. If they skip clarification, note it; don't rescue.
3. **Model (10–20)**: the learner writes the requirement list (must/nice), entities, the ASCII class
   diagram and the public API. Ask one probing question at most ("who owns the Ticket?").
4. **Build (20–75)**: the learner codes in `designs/phase-NN/<slug>/` (skeleton from the 8.1.3 kata).
   Announce time at 30, 45, 60, 75 min. **At minute 60**: if the core flow doesn't run via the driver,
   say so by name ("no running code at minute 60"). Answer questions; don't suggest designs. The
   learner compiles with `tools/run.sh`; don't fix their compile errors.
5. **Curveball (~60–70 or when the core runs)**: fire the first **Adapt** curveball. First ask: "Which
   files change, and what's new?" (record the prediction), then let them implement.
6. **Test (75–85)**: tests with minitest via `tools/run.sh --test`. Concurrency-relevant problems: a
   stress test via `tools/stress.sh` if the learner claims thread safety.
7. **Wrap (85–90)**: the learner's self-review: what's missing, what they'd do next.
8. **Evaluation discussion (+15–20)**: in character as the evaluator: "walk me through it", then 3–4
   questions: extensibility ("add X"), concurrency ("two requests at once on Y"), a design choice
   ("why is Z a class?"), a code-quality point you noticed. Fire the second curveball verbally.

## Phase B: review (switch explicitly: "Build over. Mentor hat on.")

1. Run the code and tests yourself (`tools/run.sh`, `--test`, `stress.sh` where relevant); read every file.
2. **Strong** (specific, with file/line).
3. **Problems**, most costly first, each with the *requirement change or input that exposes it* (not
   just "this is bad"). Name the traps.
4. **The mentor's design**: only now, reveal the Derive map: entities, the core abstraction, the hard
   part and how you'd handle it; contrast with theirs; say where theirs is *better* if it is.
5. **Curveball accuracy**: predicted vs actual touched files.
6. **Score** on the roadmap §9 rubric: one line of justification per category, strict (no running code
   by 60 caps Working code at 8; untested ≤ 3 Testing; each hint costs 1–3 in the category it helped;
   unjustified patterns cost Principles points). Total /100 and band.
7. **3 practice actions**, each mapped to a session type (`K`, `CR`, `CL`, a redo, a lesson re-visit).

## Finish

- Write `designs/phase-NN/<slug>/REVIEW.md` from `templates/case-study-review.md` (requirements as
  clarified, time log per phase, class diagram, the learner's design summary, curveball prediction vs
  actual, strengths, problems, mentor design, score table, actions).
- Tracker Case studies row: best score, attempts +1, date. < 65 → `progress/resolve-queue.md` (+3/+14/+45).
- Prompt the learner to add the case to `reference/case-study-index.md`; verify.
- Weak areas for each costly problem; wrap-up protocol in `CLAUDE.md`.
