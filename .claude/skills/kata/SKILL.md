---
name: kata
description: Kata (K sessions) — the learner implements a pattern, primitive or skeleton from a blank file under a time limit, from understanding not memory (invariant/structure stated first), compiled with checks, tested with minitest, stress-tested if concurrent; failures go to the cold redo queue.
argument-hint: [session ID or kata name]
---

# Kata: $ARGUMENTS

Spec = the `K` row (target time, spec, checks, file) or the argument. Examples: toolchain, polymorphic
hierarchy, Money value type, replace-conditional-with-polymorphism, registry factory + builder,
decorator chain, undo/redo, safe observer, Gilded Rose, `minitest.hpp`, semaphore + latch, bounded
blocking queue, the machine-coding skeleton.

1. **Structure first (1–2 min, spoken)**: before typing, the learner states the structure and the
   invariant ("two cvs over one mutex; `put` waits while full or until closed; `close` wakes both").
   A vague statement gets one sharpening question.
2. **Blank file, timed**: in the row's `File` directory. `date +%H:%M` at start; target time from the row.
   No notes, no previous files, no looking at `designs/` history.
3. **Compile & test**: `tools/run.sh` / `tools/run.sh --test` (minitest from 5.2.2 on; plain `assert`
   before). Concurrent katas: `tools/stress.sh … 500`. Claude may supply a stress harness; the learner
   writes the kata itself.
4. **Review**: the row's checks, then ownership/const/`noexcept`, boundaries, and (concurrent) the
   interleaving argument. Record time and whether it passed first or second try.
5. **Pass** (checks met, within time, first or second try) → note it in the tracker row; if it's a
   primitive or pattern, the learner copies the core with a 2-line comment (invariant, complexity/cost)
   into the matching `reference/` file entry. **Fail** → what broke, and `kata:<name>` into
   `progress/resolve-queue.md` at +3/+14/+45.

## Finish

Tracker row for the K session (🟨 on pass; ✅ only after a later cold redo also passes); STATUS log line
with times; wrap-up protocol.
