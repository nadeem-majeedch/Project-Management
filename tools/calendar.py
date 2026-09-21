#!/usr/bin/env python3
"""PM-401 one-click semester calendar generator.

Single source of truth:
  - planning/course-data.yaml    (FIXED course content: 32 lectures, CLOs,
                                  activities, assessment plan)
  - planning/schedule-config.yaml (INSTRUCTOR-OWNED dates: semester start,
                                  teaching days, holidays, configured flag)
  - docs/labs/lab-*.md front matter (lab -> lecture mapping)

Outputs (all in docs/calendar/, linked from the site):
  - index.md        student-friendly web view (16-week grid, relative weeks
                    until the instructor configures real dates)
  - printable.md    print-optimized one-table-per-week view
  - schedule.csv    exportable CSV (lecture-level)
  - schedule.ics    iCalendar file (only when configured: true; otherwise
                    not written at all — no invented dates)

Validation (always runs; nonzero exit on failure):
  - 32 lectures, numbered 1..32, weeks 1..16, 2 per week
  - every lecture has >= 1 CLO and >= 1 activity
  - lecture links resolve to docs/lectures/L<n>-*.md; lab links to
    docs/labs/lab-*.md
  - when configured: every scheduled date lands on a declared teaching day
    and outside the holiday list; lectures stay within 16 teaching weeks

Usage: python tools/calendar.py
"""

from __future__ import annotations

import csv
import glob
import sys
from datetime import date, timedelta
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "calendar"
COURSE_FILE = ROOT / "planning" / "course-data.yaml"
CONFIG_FILE = ROOT / "planning" / "schedule-config.yaml"

failures: list[str] = []


def fail(msg: str) -> None:
    failures.append(msg)


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            data = yaml.safe_load(text[3:end]) or {}
            return data if isinstance(data, dict) else {}
    return {}


def rel_posix(p: Path) -> str:
    return p.relative_to(ROOT / "docs").as_posix().removesuffix(".md")


# ---------------------------------------------------------------------------
# Load authoritative sources
# ---------------------------------------------------------------------------

course_doc = load_yaml(COURSE_FILE)
lectures = sorted(course_doc["lectures"], key=lambda x: x["num"])
assessment_plan = course_doc["assessment_plan"]

cfg = load_yaml(CONFIG_FILE)
configured: bool = bool(cfg.get("configured", False))

lab_by_lecture: dict[int, dict] = {}
for f in sorted(glob.glob(str(ROOT / "docs" / "labs" / "lab-*.md"))):
    fm = front_matter(Path(f))
    if fm.get("lecture") and fm.get("lab"):
        lab_by_lecture[int(fm["lecture"])] = {
            "lab": int(fm["lab"]),
            "path": rel_posix(Path(f)),
            "title": str(fm.get("title", "")).replace(f"Lab {fm['lab']} — ", ""),
        }


# ---------------------------------------------------------------------------
# Validation of the fixed roster
# ---------------------------------------------------------------------------

if [x["num"] for x in lectures] != list(range(1, 33)):
    fail(f"lecture numbering broken: {[x['num'] for x in lectures]}")
weeks = {x["num"]: x["week"] for x in lectures}
for wk in range(1, 17):
    ls = [x for x in lectures if x["week"] == wk]
    if len(ls) != 2:
        fail(f"week {wk} has {len(ls)} lectures, expected 2")
for x in lectures:
    if not x.get("clo"):
        fail(f"L{x['num']:02d}: no CLOs")
    if not x.get("activities"):
        fail(f"L{x['num']:02d}: no activities")


# ---------------------------------------------------------------------------
# Schedule math (teaching-day aware)
# ---------------------------------------------------------------------------

def build_schedule(cfg: dict) -> list[date | None]:
    """Return a date (or None when unconfigured) per lecture, sliding off
    holidays onto the next teaching day."""
    if not configured:
        return [None] * 32
    start = date.fromisoformat(str(cfg["semester_start"]))
    days = [int(d) for d in cfg.get("teaching_days", [1, 3])]
    holidays = {date.fromisoformat(str(h)) for h in cfg.get("holidays", [])}
    if len(days) < 2:
        fail("schedule-config: teaching_days must list at least 2 days")
    if start.weekday() + 1 not in days:
        fail(
            f"semester_start {start} is a {start.strftime('%A')} but teaching "
            f"days are {days} — first lecture must fall on a teaching day"
        )
    # walk the calendar, consuming teaching days, skipping holidays
    scheduled: list[date | None] = []
    cursor = start
    for _lec in lectures:
        while cursor in holidays or (cursor.weekday() + 1) not in days:
            cursor += timedelta(days=1)
        scheduled.append(cursor)
        cursor += timedelta(days=1)
    # range check: week 16's second lecture must be within ~16 teaching weeks
    last = scheduled[-1]
    if last is not None:
        span_days = (last - start).days
        if span_days > 7 * 16 + 13:  # 16 weeks plus slack for holidays
            fail(
                f"last lecture lands {span_days} days after start "
                f"(> 16 teaching weeks + holiday slack) — check holidays"
            )
    return scheduled


dates = build_schedule(cfg)
def week_starts(dates: list[date | None]) -> list[date | None]:
    """Display window start per teaching week = that week's first lecture
    date (anchors travel with holiday slides, so the range always contains
    both lectures)."""
    starts = []
    for wk in range(1, 17):
        lec = min((x for x in lectures if x["week"] == wk), key=lambda x: x["num"])
        starts.append(dates[lec["num"] - 1])
    return starts


wk_starts = week_starts(dates)

if configured and dates[0] is not None:
    seen = set()
    for i, d in enumerate(dates, 1):
        if d in seen:
            fail(f"two lectures scheduled on {d} (L{i:02d}) — check teaching_days")
        seen.add(d)


# ---------------------------------------------------------------------------
# Assessment events derived from the plan
# ---------------------------------------------------------------------------

QUIZ_LECTURES = {4: "Quiz 1 (L01–L04)", 12: "Quiz 2 (L09–L12)", 26: "Quiz 3 (L21–L26)"}
ASSIGNMENT_EVENTS = {
    16: "A2 Assignment 1 due (Scope & Schedule)",
    19: "A3 Assignment 2 due (Risk Register)",
    21: "A4 Assignment 3 due (EVM Analysis)",
}
MILESTONE_EVENTS = {
    8: "Capstone M1: team + charter",
    12: "Capstone M2: plan skeleton",
    27: "Capstone M3: plan draft for peer review",
    32: "Capstone M4: final defense",
}


def events_for(num: int) -> list[str]:
    out = []
    if num in QUIZ_LECTURES:
        out.append(QUIZ_LECTURES[num])
    if num in ASSIGNMENT_EVENTS:
        out.append(ASSIGNMENT_EVENTS[num])
    if num in MILESTONE_EVENTS:
        out.append(MILESTONE_EVENTS[num])
    return out


# ---------------------------------------------------------------------------
# Generators
# ---------------------------------------------------------------------------

def lecture_link(num: int) -> str:
    matches = list((ROOT / "docs" / "lectures").glob(f"L{num:02d}-*.md"))
    if not matches:
        fail(f"L{num:02d}: lecture page missing in docs/lectures/")
        return f"L{num:02d}"
    if len(matches) > 1:
        fail(f"L{num:02d}: multiple lecture pages match {matches}")
    # calendar pages live in docs/calendar/ -> relative prefix is ../
    return f"[L{num:02d}](../{rel_posix(matches[0])})"


def fmt_date(d: date | None) -> str:
    return d.strftime("%a %b %d, %Y") if d else "—"


def week_range(wk: int) -> str:
    if not configured or wk_starts[wk - 1] is None:
        return "—"
    s = wk_starts[wk - 1]
    e = s + timedelta(days=6)
    return f"{s.strftime('%b %d')} – {e.strftime('%b %d, %Y')}"


def build_rows() -> list[dict]:
    rows = []
    for x in lectures:
        n = x["num"]
        lab = lab_by_lecture.get(n)
        rows.append(
            {
                "num": n,
                "week": x["week"],
                "unit": x["unit"],
                "code": x["code"],
                "title": x["title"],
                "date": dates[n - 1],
                "date_str": fmt_date(dates[n - 1]),
                "clo": ", ".join(x["clo"]),
                "activities": x.get("activities") or [],
                "assessment": x.get("assessment") or "",
                "events": events_for(n),
                "lab": lab,
                "path": lecture_link(n),
                "cases": x.get("cases") or [],
            }
        )
    return rows


rows = build_rows()


def web_view() -> str:
    if not configured:
        note = (
            "> **Dates are not configured yet.** The instructor sets the semester\n"
            "> start, teaching days, and holidays in `planning/schedule-config.yaml`;\n"
            "> until then this calendar shows **relative weeks only** — no invented\n"
            "> dates. Once configured, real dates appear here and in the\n"
            "> [CSV](schedule.csv) / iCalendar exports."
        )
    else:
        label = (cfg.get("term_label") or "").strip()
        note = (
            "> Semester dates configured by the instructor"
            + (f" — {label}" if label else "")
            + ".\n> Export: [schedule.csv](schedule.csv) · [schedule.ics](schedule.ics)"
        )
    lines = [
        "<!-- AUTO-GENERATED by tools/calendar.py from planning/course-data.yaml",
        "     + planning/schedule-config.yaml. Edit the YAML, not this file. -->",
        "",
        "# Semester calendar",
        "",
        note,
        "",
        "## Calendar at a glance",
        "",
        "| Wk | Date | Lecture | Topic (unit) | CLOs | Lab | Assessments & milestones |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        lab_cell = (
            f"[Lab {r['lab']['lab']}](../{r['lab']['path']}.md)" if r["lab"] else "—"
        )
        events = "; ".join(r["events"]) if r["events"] else "—"
        lines.append(
            f"| {r['week']} | {r['date_str']} | {r['path']} | "
            f"{r['title']} *({r['unit']})* | {r['clo']} | {lab_cell} | {events} |"
        )
    lines += [
        "",
        "## What each column means",
        "",
        "- **Lecture** links to the full teaching notes for that session.",
        "- **CLOs** are the course learning outcomes exercised that day",
        "  ([CLO definitions](../syllabus/clos.md)).",
        "- **Lab** links the paired hands-on brief ([all labs](../labs/index.md));",
        "  weeks without a lab have none assigned.",
        "- **Assessments & milestones** list quizzes, assignment dues, and",
        "  capstone milestones landing that lecture — details in",
        "  [grading](../assessments/grading.md) and the",
        "  [capstone milestones](../capstone/milestones.md).",
        "",
    ]
    return "\n".join(lines)


def printable_view() -> str:
    lines = [
        "<!-- AUTO-GENERATED by tools/calendar.py — do not edit. -->",
        "",
        "# Printable semester calendar",
        "",
        (
            "> Relative weeks only — instructor has not configured dates yet."
            if not configured
            else f"> Term: {cfg.get('term_label') or 'configured semester'} — dates instructor-configured."
        ),
        "Print with the browser (Ctrl/Cmd+P); this page is a single table per week.",
        "",
    ]
    for wk in range(1, 17):
        wk_rows = [r for r in rows if r["week"] == wk]
        lines += [
            f"## Week {wk} — {week_range(wk)}",
            "",
            "| Lecture | Date | Topic | CLOs | Lab | Assessments |",
            "|---|---|---|---|---|---|",
        ]
        for r in wk_rows:
            lab_cell = f"Lab {r['lab']['lab']}" if r["lab"] else "—"
            lines.append(
                f"| {r['path']} | {r['date_str']} | {r['title']} ({r['unit']}) "
                f"| {r['clo']} | {lab_cell} | {'; '.join(r['events']) or '—'} |"
            )
        lines.append("")
    return "\n".join(lines)


def csv_export() -> str:
    import io

    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(
        [
            "lecture_no",
            "week",
            "unit",
            "date",
            "title",
            "clos",
            "lab",
            "lab_link",
            "assessments_milestones",
            "lecture_page",
        ]
    )
    for r in rows:
        w.writerow(
            [
                r["num"],
                r["week"],
                r["unit"],
                r["date"].isoformat() if r["date"] else "",
                r["title"],
                r["clo"],
                r["lab"]["lab"] if r["lab"] else "",
                (ROOT / "docs" / (r["lab"]["path"] + ".md")).name if r["lab"] else "",
                "; ".join(r["events"]),
                r["path"].split("/")[-1] + ".md",
            ]
        )
    return buf.getvalue()


def ics_export() -> str | None:
    if not configured:
        return None  # never emit invented dates

    def stamp(d: date) -> str:
        return d.strftime("%Y%m%d")

    out = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//PM-401//Semester Calendar//EN",
        "CALSCALE:GREGORIAN",
        "X-WR-CALNAME:PM-401 Project Management",
    ]
    for r in rows:
        d = r["date"]
        if d is None:
            continue
        desc = (
            f"Week {r['week']} · Unit {r['unit']} · CLOs: {r['clo']}"
            + (f" · Lab {r['lab']['lab']}" if r["lab"] else "")
            + (f" · {', '.join(r['events'])}" if r["events"] else "")
        )
        out += [
            "BEGIN:VEVENT",
            f"UID:pm401-L{r['num']:02d}@nadeem-majeedch.github.io",
            f"DTSTAMP:{stamp(date.today())}",
            f"DTSTART;VALUE=DATE:{stamp(d)}",
            f"SUMMARY:L{r['num']:02d} {r['title']}",
            f"DESCRIPTION:{desc}",
            "END:VEVENT",
        ]
    out.append("END:VCALENDAR")
    # RFC 5545 requires CRLF; write with newline="" below to keep it.
    return "\r\n".join(out) + "\r\n"


# ---------------------------------------------------------------------------
# Write outputs
# ---------------------------------------------------------------------------

OUT.mkdir(parents=True, exist_ok=True)
(OUT / "index.md").write_text(web_view(), encoding="utf-8")
(OUT / "printable.md").write_text(printable_view(), encoding="utf-8")
(OUT / "schedule.csv").write_text(csv_export(), encoding="utf-8")
ics = ics_export()
if ics is not None:
    # newline="" keeps the generator's CRLF line endings intact on Windows
    (OUT / "schedule.ics").write_text(ics, encoding="utf-8", newline="")
elif (OUT / "schedule.ics").exists():
    # dates were un-configured after a configured run — never ship stale dates
    (OUT / "schedule.ics").unlink()
    print("  docs/calendar/schedule.ics  REMOVED (stale; dates not configured)")

print(f"calendar: configured={configured}")
print(f"  docs/calendar/index.md      ({len(rows)} lecture rows)")
print(f"  docs/calendar/printable.md  (16 week tables)")
print(f"  docs/calendar/schedule.csv")
print(f"  docs/calendar/schedule.ics  {'written' if ics else 'SKIPPED (dates not configured)'}")

if failures:
    print(f"\nCALENDAR FAIL ({len(failures)}):")
    for f in failures:
        print(" -", f)
    sys.exit(1)
print("CALENDAR PASS")
