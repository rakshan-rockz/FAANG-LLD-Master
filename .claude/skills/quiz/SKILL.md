---
name: quiz
description: Rapid retrieval-practice quiz on covered LLD material — principle/pattern explain-backs, "which pattern and why not the other", smell spotting, ownership/member-type questions, "is this thread-safe?", interleavings, rubric judgements — weighted toward due reviews, weak areas and low-confidence rows. Also the 15-minute floor day.
argument-hint: [topic] [n questions]
---

# Quiz: $ARGUMENTS

1. Read `progress/review-queue.md`, `progress/tracker.md`, `progress/weak-areas.md`. Pool = 🟨/✅ rows
   (plus the given topic). Weight: due reviews > open weak areas > confidence ≤ 3 > oldest "Last
   touched". Never quiz untaught (⬜) material.
2. Ask 8 questions by default (or n), **one at a time**, mixing:
   - "Explain X in 2 sentences, including when NOT to use it"
   - scenario → "which principle/pattern (or none), and why not the nearest alternative?"
   - a 10–15-line snippet → "name the smell / violation and the requirement change that hurts"
   - "sketch the structure of X in ASCII in 2 minutes"
   - ownership: "these 4 classes: write the member types"
   - concurrency: "is this thread-safe? give the interleaving if not"; "which memory order, and why?"
   - curveball: "this design + new requirement: which files change?"
   - C++/Java fundamentals tied to design (slicing, virtual destructor, `equals/hashCode`)
3. After each: ✅ / ⚠️ partial / ❌ + a 1–3 line correction. No lectures.
4. End with x/n and the 2–3 topics that need work.

## Finish

Update tracker confidence, mark review-queue items ✅/❌ (❌ resets to +2 and opens a weak area), resolve
weak areas answered correctly for the second time, STATUS log line.
