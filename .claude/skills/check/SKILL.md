---
name: check
description: Compile, run, test, stress and review the learner's own C++ or Java design code — warnings and checked builds, the driver demo, minitest suites, concurrency stress runs, then a line-referenced review of design (responsibilities, relationships, ownership, extensibility), correctness, concurrency, tests and code quality. Never rewrites the learner's code.
argument-hint: [path to file or design dir]
---

# Check: $ARGUMENTS

Layout: `designs/<phase>/<slug>/` with sources, `main.cpp` (driver/demo) and `tests.cpp` (minitest), or
Java `Main.java` / `Tests.java`. `designs/lib/minitest.hpp` is on the include path.

1. **Read** every file fully. Ask the learner first: "Which part are you least sure about?" Their answer
   is part of the review.
2. **Build & run the driver**: `tools/run.sh <dir>` (C++20, `-Wall -Wextra -Wshadow -pthread`,
   bounds-checked STL; ASan/UBSan only if they link: on this machine they don't). Report every warning;
   they're often the bug. Java: `tools/run.sh <dir>` (javac `-Xlint:all`, `java -ea`).
3. **Tests**: `tools/run.sh --test <dir>`. Then the edge-case catalogue for the domain (empty/zero,
   one, capacity boundaries, duplicate IDs, unknown IDs, repeated operations (exit twice, cancel
   twice), time boundaries, money rounding, invalid state transitions). The learner proposes at least
   half; missing tests are review items, not things you write for them.
4. **Concurrency** (if any shared state or threads): `tools/stress.sh <dir> 300 10` (or `--test`),
   `TSAN=1` attempted. On failure or hang, show the output and ask the learner to write the interleaving;
   don't diagnose it for them. If they claim thread safety without a stress test, ask for one.
5. **Review** (file:line references, most costly first):
   - **Design**: responsibilities in the right class (information expert), god classes, relationships
     and ownership (`unique_ptr` vs raw vs `shared_ptr` vs ID), encapsulation leaks (mutable refs
     returned), patterns without a stated axis of change, missing abstraction where a curveball will
     hurt. For each: *the requirement change that exposes it*.
   - **Correctness**: bugs with the input that triggers each.
   - **Concurrency**: shared state, unguarded access, check-then-act, locks held across calls out,
     lock order, cv predicates.
   - **C++/Java pitfalls**: slicing, missing virtual destructor, dangling views, Rule-of-Zero
     violations, `double` for money, `equals/hashCode`, iterator invalidation.
   - **Tests**: what's untested that matters.
   - **Quality**: names, function size, error handling, const-correctness.
   Ask the learner to fix; re-check after fixes.
6. Log mistakes by category for wrap-up (`progress/weak-areas.md`).
