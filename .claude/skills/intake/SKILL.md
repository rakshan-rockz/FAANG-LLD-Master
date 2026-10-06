---
name: intake
description: Intake interview (session 0.0.1, refreshed at gates) — captures level (SDE-2 to confirm), target companies and their LLD/machine-coding formats, timeline, machine-coding language, C++/Java/OOP/concurrency background and preferences into progress/profile.md, with short unscored calibration exercises.
---

# Intake interview

Goal: fill `progress/profile.md` so emphasis, examples, mock formats and difficulty fit this learner.
~35–45 min. **Content is never reduced based on intake**; only emphasis, examples, company styles,
language choice and pacing advice change. The track (switch/depth) is already set in STATUS; confirm it.

1. Explain in 3 lines why this matters (company formats differ: Flipkart machine coding vs Atlassian
   code design vs Amazon LLD discussion; the MC language changes how fast you can build; background
   decides where to push hardest).
2. Ask the profile sections **a few questions at a time**: level & years of experience (confirm SDE-2)
   → target companies in priority order and any known round formats → timeline (offers by ~June 2027;
   when do applications start?) → rhythm (weekday time, weekend 3-hour slots for MCs) → background:
   what they design and build at QNu Labs, OOP/design reviews they've been through, concurrency
   they've written (and bugs they've hit), past LLD/MC rounds → C++ and Java fluency → preferences
   (voice, bluntness, what throws them off). Probe vague answers ("'some multithreading': which
   primitives, and what broke?").
3. **Decide the machine-coding language** with the learner: C++ (primary, strongest) vs Java (less
   boilerplate in 90 min; many Indian evaluators read Java). Record the decision per company if it
   differs. This is a decision for the learner; give the trade-off honestly.
4. Calibration (unscored, ~10 min, notes only):
   - a 4-minute modelling prompt ("classes for a coffee shop's order flow"): note nouns, relationships, god-class tendency
   - a C++ snippet with a slicing bug and a missing virtual destructor
   - "is this thread-safe?" on a 10-line check-then-act cache
   - "Strategy or State?" for one scenario
5. State the calibration: the bar for their targets (SDE-2: a working, extensible, tested build in 90
   min scoring ≥ 80; a clean LLD discussion; correct concurrency on shared state), company-format
   emphasis (PLAN §5), where you'll push hardest, the weekly rhythm for the switch track (~5–6 h/week:
   2 lessons + 1 build or lab, MCs on weekends). If a real interview date is near, say what the track
   covers by then and suggest extra mocks, never skipped content.
6. Write `progress/profile.md`; update `progress/STATUS.md` (Started date; next = 0.0.2 baseline;
   switch-track position row 2). Run the wrap-up protocol.
