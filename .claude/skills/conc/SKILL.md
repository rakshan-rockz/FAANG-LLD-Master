---
name: conc
description: Concurrency lab (CL sessions) — the learner states the invariant, writes the concurrent C++ (and Java) code, then breaks it with tools/stress.sh, injected yields and deliberately wrong variants, explains every failure as an exact interleaving, fixes it and argues correctness; throughput measured where relevant.
argument-hint: [session ID or problem]
---

# Concurrency lab: $ARGUMENTS

Row = the `CL` row (Build / Break / Stress / Java). Code lives in `designs/phase-NN/<slug>/`. Tools:
`tools/run.sh` (add `TSAN=1` to try ThreadSanitizer; on this machine it doesn't link, so it prints a
note and continues), `tools/stress.sh <file|dir> [runs] [timeout]` (repeats runs, reports failures and
hangs, pins every 4th run to one core), `NOCHECK=1 tools/run.sh` for timing.

## Flow (one step per turn)

1. **Predict**: before any code, the learner writes (a) the invariant(s) ("each item consumed exactly
   once; `0 ≤ size ≤ cap`"), (b) the shared state and what guards it, (c) the hazards they expect.
   Sharpen vague invariants with one question.
2. **Build**: the learner writes it. The program must **check its own invariant** and exit non-zero
   (assert/abort) when it fails, or stress runs prove nothing. Harness first if the row is a LeetCode
   puzzle: random start orders, many iterations, exact-output assertion.
3. **Break**:
   - `tools/stress.sh` (≥ 300 runs, timeout 5–10 s).
   - Inject `std::this_thread::yield()` / a short `sleep_for` between suspicious steps (check → act,
     read → write, unlock → notify) to widen windows.
   - Run the row's **deliberately wrong variants** (e.g. `if` instead of `while` around `wait`, one cv
     with `notify_one` for two predicates, lock released before the write) and watch them fail.
4. **Explain the interleaving**: for every failure or hang, the learner writes the exact schedule
   ("T1 checks `empty()` → false; T2 takes the last item; T1 pops an empty deque"). No fix is
   accepted before this. If they're stuck, hint ladder (H0: "which two operations must be atomic
   together?").
5. **Fix & argue**: fix, re-stress, then state in 2–3 sentences why it's correct (the lock covers the
   whole invariant; the predicate is re-checked under the lock after every wake; the global lock order
   is by ID; happens-before edge is release→acquire on X).
6. **Measure** (if the row asks): coarse vs fine-grained, `NOCHECK=1`, a few thread counts; explain
   the numbers (contention, cache-line bouncing, oversubscription).
7. **Java**: the row's Java version; name the differences (intrinsic locks, `Condition`, `volatile`,
   `java.util.concurrent` types) and whether the same bug is possible.
8. **Interview framing**: "Explain your solution to an interviewer in 90 seconds, including why it
   can't deadlock."

Remember: clean stress runs are evidence, not proof. The argument is the proof.

## Finish

Lesson note in `lessons/phase-NN/<ID>-<Slug>.md` (template; include the failing interleavings and the
correctness argument verbatim); the learner updates `reference/concurrency-primitives.md` (verify);
tracker row 🟨; weak areas for every hazard they didn't predict; wrap-up protocol.
