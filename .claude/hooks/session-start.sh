#!/usr/bin/env bash
# Injects programme status into every new Claude session.
dir="${CLAUDE_PROJECT_DIR:-$(pwd)}"
today=$(date +%F)
# Due = unmarked date cells <= today in the schedule columns (review-queue: +2.. from field 5;
# resolve-queue: +3.. from field 6). Done cells are prefixed with ✅/❌ and don't match.
open=$(awk '/^## Open/{f=1;next} /^## /{f=0} f && /^\| [0-9]{4}-/' "$dir/progress/weak-areas.md" 2>/dev/null | wc -l)
rev=$(awk -F'|' -v t="$today" 'NR>2 && /^\| /{for(i=5;i<=NF;i++){g=$i; gsub(/ /,"",g); if(g ~ /^[0-9]{4}-[0-9]{2}-[0-9]{2}$/ && g<=t) n++}} END{print n+0}' "$dir/progress/review-queue.md" 2>/dev/null)
res=$(awk -F'|' -v t="$today" 'NR>2 && /^\| /{for(i=6;i<=NF;i++){g=$i; gsub(/ /,"",g); if(g ~ /^[0-9]{4}-[0-9]{2}-[0-9]{2}$/ && g<=t) n++}} END{print n+0}' "$dir/progress/resolve-queue.md" 2>/dev/null)
echo "Today: $today · $(python3 "$dir/tools/gen_tracker.py" --summary 2>/dev/null)"
echo "Due now: concept reviews $rev · cold redos $res · open weak areas $open"
echo
cat "$dir/progress/STATUS.md" 2>/dev/null
echo
echo "Design-discovery first, mastery-gated. Resume from 'Next session' on the active track (switch → plan/roadmap/TRACK-switch.md order; depth → roadmap order). Suggest /today if the learner hasn't said what they want."
