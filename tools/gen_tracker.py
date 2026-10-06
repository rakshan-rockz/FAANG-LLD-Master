#!/usr/bin/env python3
"""Regenerate progress/tracker.md from plan/roadmap/phase-*.md (+ TRACK-switch.md).

Preserves Status / Conf / Last touched (concept rows), Best score / Attempts / Last (case studies),
Score / Date (mocks) and gate progress for IDs that still exist, so it is safe to re-run after editing
the roadmap.

Usage:
  python3 tools/gen_tracker.py              regenerate progress/tracker.md
  python3 tools/gen_tracker.py --summary    one-line summary (used by the SessionStart hook)
  python3 tools/gen_tracker.py --forecast   session counts by type, hours, reading, track total
  python3 tools/gen_tracker.py --check      verify TRACK-switch.md covers every roadmap row exactly once
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRACKER = os.path.join(ROOT, "progress", "tracker.md")
STATUS = os.path.join(ROOT, "progress", "STATUS.md")
TRACK = os.path.join(ROOT, "plan", "roadmap", "TRACK-switch.md")
CONCEPT = ("L", "DD", "C", "WE", "K", "CR", "CL")    # concept-level rows (status / conf)
CASES = ("MC", "LD")                                 # scored case studies
MOCKS = ("M", "Baseline")
HOURS = {"L": 1.25, "DD": 1.5, "C": 1.25, "WE": 1.25, "K": 0.75, "CR": 1, "CL": 2, "MC": 3,
         "LD": 1.5, "M": 1.5, "R": 1, "Gate": 3, "Intake": 1.5, "Baseline": 1.5}
READ_H, OVERHEAD = 2.0, 0.20
ID_RE = re.compile(r"^\d+\.\d+\.\d+$")
BOOK_RE = re.compile(r"📖\s*(HFDP|GoF|CC|Refactoring|CCiA|JCIP)\s+ch(\d+)")


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def topic_of(txt):
    b = re.search(r"\*\*(.+?)\*\*", txt)
    t = b.group(1) if b else re.split(r": | — | · |; ", re.sub(r"[`*]", "", txt), maxsplit=1)[0]
    return t.replace("Kata: ", "Kata: ").strip()[:90]


# ---- roadmap -----------------------------------------------------------------------------------
phases, rows = [], []          # rows: (phase, id, type, topic, text)
for f in sorted(glob.glob(os.path.join(ROOT, "plan", "roadmap", "phase-*.md"))):
    ph = int(re.search(r"phase-(\d+)", f).group(1))
    phases.append((ph, open(f, encoding="utf-8").readline().strip("# \n")))
    for line in open(f, encoding="utf-8"):
        c = cells(line)
        if len(c) >= 3 and ID_RE.match(c[0]):
            txt = " | ".join(c[2:])
            rows.append((ph, c[0], c[1], topic_of(txt), txt))
by_id = {r[1]: r for r in rows}

# ---- switch track ------------------------------------------------------------------------------
track, track_h, deferred, track_reading = [], {}, [], []
if os.path.exists(TRACK):
    section = None
    for line in open(TRACK, encoding="utf-8"):
        if line.startswith("## "):
            section = "order" if "Order" in line else ("deferred" if "Deferred" in line else None)
            continue
        c = cells(line)
        if section == "order" and len(c) >= 6 and ID_RE.match(c[1]):
            track.append(c[1])
            try:
                track_h[c[1]] = float(c[5])
            except ValueError:
                track_h[c[1]] = HOURS.get(c[2], 0)
        elif section == "deferred" and len(c) >= 2 and ID_RE.match(c[0]):
            deferred.append(c[0])
        if section == "order" and line.startswith("**Reading"):
            track_reading += BOOK_RE.findall(line)
in_track = set(track)


def active_and_next():
    act, nxt = "depth", None
    if os.path.exists(STATUS):
        s = open(STATUS, encoding="utf-8").read()
        m = re.search(r"\*\*Active track:\*\*\s*(\w+)", s)
        act = m.group(1) if m else act
        m = re.search(r"\*\*Next session:\*\*[^\n]*?(\d+\.\d+\.\d+)", s)
        nxt = m.group(1) if m else None
    return act, nxt


# ---- previous progress -------------------------------------------------------------------------
old_c, old_case, old_mock, old_gate = {}, {}, {}, {}
if os.path.exists(TRACKER):
    sec = None
    for line in open(TRACKER, encoding="utf-8"):
        if line.startswith("## "):
            sec = "case" if "Case studies" in line else "mock" if "Mocks" in line else \
                  "gate" if "Gates" in line else "concept"
            continue
        c = cells(line)
        if sec == "concept" and len(c) == 7 and ID_RE.match(c[0]):
            old_c[c[0]] = c[4:7]
        elif sec == "case" and len(c) == 7 and ID_RE.match(c[0]):
            old_case[c[0]] = c[4:7]
        elif sec == "mock" and len(c) == 6 and ID_RE.match(c[0]):
            old_mock[c[0]] = c[4:6]
        elif sec == "gate" and len(c) == 5 and re.match(r"^Gate \d+$", c[0]):
            old_gate[c[0]] = c[2:5]

concept_rows = [r for r in rows if r[2] in CONCEPT]
case_rows = [r for r in rows if r[2] in CASES]
mock_rows = [r for r in rows if r[2] in MOCKS]
gate_rows = [r for r in rows if r[2] == "Gate"]
st = lambda i: old_c.get(i, ("⬜", "", ""))[0]
mastered = sum(st(r[1]) == "✅" for r in concept_rows)
started = sum(st(r[1]) == "🟨" for r in concept_rows)
scored = [r for r in case_rows if old_case.get(r[1], ("",))[0]]
mocks_done = [r for r in mock_rows if old_mock.get(r[1], ("",))[0]]
gates_passed = sum(1 for r in gate_rows if old_gate.get(f"Gate {r[0]}", ("⬜",))[0] == "✅")


def track_position():
    act, nxt = active_and_next()
    if not track:
        return act, ""
    k = track.index(nxt) if nxt in in_track else (len(track) if act == "depth" else 0)
    done_h = sum(track_h[i] for i in track[:k]) * (1 + OVERHEAD)
    tot_h = (sum(track_h.values()) + READ_H * len(track_reading)) * (1 + OVERHEAD)
    return act, f"🎯 switch track: {k}/{len(track)} sessions done (~{done_h:.0f} of ~{tot_h:.0f} h)"


if "--summary" in sys.argv:
    act, pos = track_position()
    print(f"Concepts ✅ {mastered} · 🟨 {started} · of {len(concept_rows)} | Case studies scored "
          f"{len(scored)}/{len(case_rows)} | Mocks {len(mocks_done)}/{len(mock_rows)} | Gates "
          f"{gates_passed}/{len(gate_rows)} | Active track: {act}" + (f" | {pos}" if pos else ""))
    sys.exit(0)

if "--check" in sys.argv:
    all_ids = [r[1] for r in rows]
    missing = [i for i in all_ids if i not in in_track and i not in deferred]
    dup = sorted({i for i in track + deferred if (track + deferred).count(i) > 1})
    unknown = [i for i in track + deferred if i not in by_id]
    order_ok = [by_id[i] for i in track if i in by_id]
    wrong_order = [a[1] for a, b in zip(order_ok, order_ok[1:])
                   if tuple(map(int, a[1].split("."))) > tuple(map(int, b[1].split(".")))]
    mism = [i for i in track if i in by_id and by_id[i][2] != next(
        (cells(l)[2] for l in open(TRACK, encoding="utf-8") if cells(l)[1:2] == [i]), by_id[i][2])]
    print(f"roadmap rows {len(all_ids)} · track {len(track)} · deferred {len(deferred)}")
    for name, lst in (("missing (neither track nor deferred)", missing), ("duplicated", dup),
                      ("unknown IDs", unknown), ("track out of roadmap order after", wrong_order),
                      ("type mismatch", mism)):
        print(f"{name}: {', '.join(lst) if lst else 'none'}")
    sys.exit(1 if (missing or dup or unknown or wrong_order or mism) else 0)

if "--forecast" in sys.argv:
    counts = {}
    for r in rows:
        counts[r[2]] = counts.get(r[2], 0) + 1
    books = {}
    for r in rows:
        for b, ch in BOOK_RE.findall(r[4]):
            books.setdefault(b, set()).add(int(ch))
    n_ch = sum(len(v) for v in books.values())
    order = ["Intake", "Baseline", "L", "DD", "C", "WE", "K", "CR", "CL", "MC", "LD", "M", "R", "Gate"]
    sess_h = 0.0
    print("| Type | Sessions | h each | Hours |\n|---|---:|---:|---:|")
    for t in order + sorted(set(counts) - set(order)):
        if t in counts:
            h = counts[t] * HOURS.get(t, 0)
            sess_h += h
            print(f"| {t} | {counts[t]} | {HOURS.get(t, 0)} | {h:.2f} |")
    print(f"| **All sessions** | **{len(rows)}** | | **{sess_h:.2f}** |")
    print(f"\nReading: {n_ch} chapters × {READ_H} h = {n_ch * READ_H:.1f} h  "
          + " · ".join(f"{b} {sorted(v)}" for b, v in sorted(books.items())))
    full = (sess_h + n_ch * READ_H) * (1 + OVERHEAD)
    print(f"Full course: ({sess_h:.2f} + {n_ch * READ_H:.1f}) × {1 + OVERHEAD:.2f} = {full:.1f} h")
    if track:
        th = sum(track_h.values())
        tr = READ_H * len(track_reading)
        tcount = {}
        for i in track:
            tcount[by_id[i][2]] = tcount.get(by_id[i][2], 0) + 1 if i in by_id else 0
        print(f"Switch track: {len(track)} sessions ({', '.join(f'{k} {v}' for k, v in tcount.items())}); "
              f"({th:.2f} + reading {tr:.1f}) × {1 + OVERHEAD:.2f} = {(th + tr) * (1 + OVERHEAD):.1f} h")
    sys.exit(0)

# ---- write -------------------------------------------------------------------------------------
act, pos = track_position()
tick = lambda i: "🎯" if i in in_track else ""
out = ["# Curriculum Tracker", "",
       "Generated by `tools/gen_tracker.py` from `plan/roadmap/` (re-run after roadmap edits; progress is preserved).",
       "Status: ⬜ not started · 🟨 taught, mastery bar not yet met · ✅ mastered (recognition + understanding +",
       "construction + adaptation + retention). Conf 1–5. 🎯 = in the switch track (`plan/roadmap/TRACK-switch.md`).", "",
       f"**Concept rows:** ✅ {mastered} · 🟨 {started} · total {len(concept_rows)}  ",
       f"**Case studies scored:** {len(scored)} / {len(case_rows)} · **Mocks:** {len(mocks_done)} / {len(mock_rows)} · "
       f"**Gates:** {gates_passed} / {len(gate_rows)}  ",
       f"**Active track:** {act}" + (f" · {pos}" if pos else "")]
for ph, title in phases:
    pr = [r for r in concept_rows if r[0] == ph]
    if not pr:
        continue
    out += ["", f"## {title}", "", "| ID | Type | 🎯 | Topic | Status | Conf | Last touched |",
            "|---|---|---|---|---|---|---|"]
    for r in pr:
        s, cf, lt = old_c.get(r[1], ("⬜", "", ""))
        out.append(f"| {r[1]} | {r[2]} | {tick(r[1])} | {r[3]} | {s} | {cf} | {lt} |")
out += ["", "## Case studies (MC machine coding · LD discussion)", "",
        "Best score /100 (bands: <50 No hire · 50–64 Lean no · 65–79 Lean hire · 80–89 Hire · 90+ Strong hire).", "",
        "| ID | Type | 🎯 | Case study | Best /100 | Attempts | Last |", "|---|---|---|---|---|---|---|"]
for r in case_rows:
    b, a, l = old_case.get(r[1], ("", "", ""))
    out.append(f"| {r[1]} | {r[2]} | {tick(r[1])} | {r[3]} | {b} | {a} | {l} |")
out += ["", "## Mocks", "", "| ID | Type | 🎯 | Session | Score /100 | Date |", "|---|---|---|---|---|---|"]
for r in mock_rows:
    s, d = old_mock.get(r[1], ("", ""))
    out.append(f"| {r[1]} | {r[2]} | {tick(r[1])} | {r[3]} | {s} | {d} |")
out += ["", "## Gates", "", "| Gate | 🎯 | Status | Attempts | Passed on |", "|---|---|---|---|---|"]
for r in gate_rows:
    s, a, p = old_gate.get(f"Gate {r[0]}", ("⬜", "", ""))
    out.append(f"| Gate {r[0]} | {tick(r[1])} | {s} | {a} | {p} |")
open(TRACKER, "w", encoding="utf-8").write("\n".join(out) + "\n")
print(f"{len(phases)} phases, {len(rows)} rows: {len(concept_rows)} concept, {len(case_rows)} case studies, "
      f"{len(mock_rows)} mocks, {len(gate_rows)} gates; switch track {len(track)} rows -> {TRACKER}")
