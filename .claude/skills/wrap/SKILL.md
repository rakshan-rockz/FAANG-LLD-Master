---
name: wrap
description: End the current LLD session — write the lesson note / REVIEW.md / mock file / review file as applicable, update tracker, weak areas, review and redo queues, STATUS (next row on the active track) and the README progress block, and verify the learner's reference entries.
---

# Wrap up this session

Follow the **Wrap-up protocol** in `CLAUDE.md` exactly, based on everything in this conversation.

- Only mark a row ✅ if the full mastery bar (roadmap §4) has been demonstrated across sessions;
  otherwise 🟨. Case studies: record the score honestly; no rounding up.
- Lesson notes: complete and standalone, with the **Discovery Path**. Never thinner than what was taught.
- Record hint rungs honestly; H2+ katas and case studies < 65 go to the redo queue.
- **Next session** = the next row on the **active track**: switch → the next row in
  `plan/roadmap/TRACK-switch.md` § Order (update the "Switch track position" line); depth → the next
  roadmap row not yet done (skipping rows completed in full; rows done at switch scope return for their
  deferred parts). Track finished → tell the learner, set `**Active track:** depth`, and the next
  session is the first remaining roadmap row.
- After editing phase files or if the tracker looks stale, run `python3 tools/gen_tracker.py`.
- Run `date +%F` for dates.

Finish with a 2–3 line summary: what was recorded, current confidence, what's next (ID + type + Hook
only, never the pattern name).
