---
name: today
description: Start the next LLD session — runs due spaced reviews and cold redos, then resumes the next session ID on the active track (switch → TRACK-switch.md order; depth → roadmap order) with the right skill.
---

# Start the next session

1. Run `date +%F`. Read `progress/STATUS.md` (**Active track**, **Next session**, resume point),
   `progress/profile.md`, `progress/review-queue.md`, `progress/resolve-queue.md`,
   `progress/weak-areas.md`, the row's phase file `plan/roadmap/phase-NN.md`, and, if the active track
   is `switch`, `plan/roadmap/TRACK-switch.md` (the row's **Scope**).
2. If `progress/profile.md` is blank → the next session is 0.0.1 (`/intake`). If there's no baseline in
   `mocks/` → 0.0.2 (`/mock baseline`).
3. Locate the **Next session** row. If STATUS notes a resume point, resume there. If the last log entry
   is **7+ days old**, open with a 10-minute re-entry: explain-back of the last 2 concepts touched and a
   3-minute class-diagram sketch of the last case study, cold.
4. **Scope:** on the switch track, a row whose Scope is `switch: …` is taught at that scope (include
   the folded content it names; skip what it says waits). On the depth track, teach the full row, and
   for rows already done at switch scope teach only what was deferred (check the tracker and lesson note).
5. Present a ≤ 7-line plan:
   - due concept reviews (count + topics) and due cold redos (count + items)
   - session ID · type · title · track scope; for `L`/`DD`/`C` rows the **Hook** only (never the
     principle/pattern name); for `MC`/`LD` the one-line prompt only (never the Derive field)
   - one weak area to resurface
   - short on time? offer the **floor day**: due reviews + `/quiz 5`, or one kata redo
   Ask "Ready?"
6. On go: due reviews first (≤ 10 min; each = 2-min explain-back + one curveball + structure sketch;
   mark ✅/❌ in the queue), then at most one due cold redo (the rest roll over), then the session:

   | Type | Skill |
   |---|---|
   | Intake | `/intake` |
   | Baseline | `/mock baseline` |
   | L | `/lesson <ID> learn` |
   | DD | `/lesson <ID> deep-dive` |
   | C | `/lesson <ID> compare` |
   | WE | `/lesson <ID> we` |
   | K | `/kata <ID>` |
   | MC | `/mc <ID>` |
   | LD | `/lld-discuss <ID>` |
   | CR | `/critique <ID>` |
   | CL | `/conc <ID>` |
   | M | `/mock <ID>` (format and company from the row) |
   | R | `/weekly-review` |
   | Gate | `/gate <phase>` (switch track: only criteria not marked *switch: deferred*, plus folded gates) |

7. **Build rule:** before a new `L`, check that the previous lesson's **Build** exists in `designs/` and
   compiles. If not, finish it first and say why (knowledge that was never built decays fastest).
8. Finish with the wrap-up protocol in `CLAUDE.md` (`/wrap`).
