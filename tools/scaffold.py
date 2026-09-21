#!/usr/bin/env python3
"""
scaffold.py — Generate course artifacts from the single source of truth.

Inputs:
  planning/course-data.yaml   32 lectures, CLOs, units, assessment plan
  planning/case-catalog.yaml  meta + band files (planning/cases/band-*.yaml): 105 progressive cases

Outputs (all safe to regenerate; do not hand-edit):
  docs/lectures/L<nn>-<slug>.md        32 lecture pages
  docs/syllabus/weekly-schedule.md     16-week table
  docs/lectures/index.md               curriculum map
  planning/04-clo-mapping.md           CLO x lecture matrix
  planning/06-case-matrix.md           case x lecture/level matrix
  instructor/lesson-plans/L<nn>.md     32 instructor plans (NOT published)
  instructor/answer-keys/case-index.md case index (NOT published)
  instructor/answer-keys/cases/CS-XX.md  105 answer keys (NOT published)

Run:  python tools/scaffold.py
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date, timedelta
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
COURSE_FILE = ROOT / "planning" / "course-data.yaml"
CASES_FILE = ROOT / "planning" / "case-catalog.yaml"
CASE_BAND_FILES = [
    ROOT / "planning" / "cases" / "band-1-beginner.yaml",
    ROOT / "planning" / "cases" / "band-2-intermediate.yaml",
    ROOT / "planning" / "cases" / "band-3-advanced.yaml",
    ROOT / "planning" / "cases" / "band-4-expert.yaml",
]
BAND_OF = {}
for _i, _name in enumerate([
    "beginner", "intermediate", "advanced", "expert",
], 1):
    BAND_OF["band-%d-%s.yaml" % (_i, _name)] = _name
BAND_RANGE = {
    "beginner": "CS-01..CS-20",
    "intermediate": "CS-21..CS-45",
    "advanced": "CS-46..CS-75",
    "expert": "CS-76..CS-105",
}


def load_cases() -> list:
    """Merge the four band files (in band order) into one case list."""
    cases = []
    for f in CASE_BAND_FILES:
        band = BAND_OF[f.name]
        for c in load_yaml(f)["cases"]:
            cases.append({**c, "band": band})
    return cases

HEADER_NOTE = (
    "<!-- AUTO-GENERATED from planning/*.yaml via tools/scaffold.py. "
    "Edit the YAML, not this file. -->\n\n"
)


def load_yaml(path: Path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def p(*parts) -> Path:
    return ROOT.joinpath(*parts)


STDOUT_MODE = False
OUTPUT: dict[str, str] = {}


def write(path: Path, text: str) -> None:
    rel = path.relative_to(ROOT).as_posix()
    if STDOUT_MODE:
        OUTPUT[rel] = text
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")
    print(f"  wrote {rel}")


def render_topics(topics: list) -> str:
    out = []
    for i, t in enumerate(topics, 1):
        out.append(f"### {i}. {t['title']}\n")
        for b in t["bullets"]:
            out.append(f"- {b}")
        out.append("")
    return "\n".join(out)


def render_activities(activities: list) -> str:
    return "\n".join(f"- {a}" for a in activities)


# ────────────────────────────────────────────────────────────────────────────
# Lecture pages
# ────────────────────────────────────────────────────────────────────────────
def lecture_page(l: dict, course: dict, case_by_id: dict, anchored_by_lecture: dict) -> str:
    cases_md = "\n".join(
        f"- [{cid}](../cases/{cid}.md) — {case_by_id[cid]['title']} "
        f"({case_by_id[cid]['level']})"
        for cid in l["cases"]
    )
    extra = [cid for cid in anchored_by_lecture.get(l["num"], [])
             if cid not in set(l["cases"])]
    extra_md = ""
    if extra:
        extra_md = (
            "\n\n**Also anchored here** (distributed via the case directory):\n\n"
            + ", ".join(f"[{cid}](../cases/{cid}.md)" for cid in extra)
        )
    clo_line = ", ".join(l["clo"])
    pagevars = (
        "---\n"
        f'title: "Lecture {l["num"]:02d} — {l["title"]}"\n'
        f"description: {l["tagline"]}\n"
        "---\n\n"
    )
    body = f"""{pagevars}{HEADER_NOTE}# Lecture {l["num"]:02d} — {l["title"]}

!!! abstract "At a glance"
    **Unit:** {l["unit"]} · **Week {l["week"]}** · **CLOs:** {clo_line} ·
    **Bloom:** {l["bloom"]}

    {l["tagline"]}

## Session topics & takeaways

This session covers:

""" + "\n".join(
        f"{j}. {b}"
        for i, t in enumerate(l["topics"], 1)
        for j, b in enumerate(t["bullets"], (i - 1) * len(t["bullets"]) + 1)
    ) + f"""

## Core content

{render_topics(l["topics"])}
## Case anchors

{cases_md}{extra_md}

## In-class activities

{render_activities(l["activities"])}

## After this lecture

"""
    if l.get("assessment"):
        body += f"- **{l["assessment"]}**\n"
    else:
        body += (
            "- Read the assigned case anchors above before the next session.\n"
            "- Add at least one question or objection to the unit discussion thread.\n"
        )
    body += f"""
## Session checklist

- [ ] Slides reviewed ({course['instructor']})
- [ ] Case anchor(s) printed / linked
- [ ] Activity materials ready
- [ ] Announcements posted

--8<-- "docs/lectures/lesson-footer.md"

*[{course['code']}](../syllabus/course-description.md) ·
[{course['instructor']}](https://github.com/nadeem-majeedch) ·
Week {l['week']} of {course['duration_weeks']} ·
{course['contact_hours']} contact hours*
"""
    return body


# ────────────────────────────────────────────────────────────────────────────
# Curriculum map (docs/lectures/index.md)
# ────────────────────────────────────────────────────────────────────────────
def curriculum_map(course: dict, lectures: list, units: list) -> str:
    rows = []
    for l in lectures:
        rows.append(
            f"| [{l['code']}](L{l['num']:02d}-{l['slug']}.md) | {l['title']} "
            f"| {l['unit']} | {l['week']} | {', '.join(l['clo'])} "
            f"| {l['bloom']} | {', '.join(l['cases'])} |"
        )
    unit_lines = []
    for u in units:
        wk = ", ".join(f"W{w}" for w in u["weeks"])
        unit_lines.append(
            f"### {u['id']} — {u['title']} ({wk})\n\n{u['description']}\n"
        )
    return (
        HEADER_NOTE
        + f"""# Curriculum map — 32 lectures

> **{course['code']} {course['title']}** · {course['level']} ·
> {', '.join(course['programs'])}
> Instructor: {course['instructor']} · {course['duration_weeks']} weeks ·
> {course['lecture_hours']} lectures x {course['lecture_length_hours']} h =
> {course['contact_hours']} contact hours

## Units at a glance

{chr(10).join(unit_lines)}

## Lecture-by-lecture map

| Lec | Title | Unit | Week | CLOs | Bloom | Cases |
|-----|-------|------|------|------|-------|-------|
{chr(10).join(rows)}

*Generated from `planning/course-data.yaml`. See
[planning/](https://github.com/nadeem-majeedch/Project-Management/tree/main/planning)
for the design documents.*
"""
    )


# ────────────────────────────────────────────────────────────────────────────
# Weekly schedule (docs/syllabus/weekly-schedule.md)
# ────────────────────────────────────────────────────────────────────────────
def weekly_schedule(course: dict, lectures: list, assessment_plan: list) -> str:
    # Dates come ONLY from planning/schedule-config.yaml (instructor-owned).
    # While configured: false, the table shows relative weeks and no dates.
    cfg_file = ROOT / "planning" / "schedule-config.yaml"
    cfg = yaml.safe_load(cfg_file.read_text(encoding="utf-8")) if cfg_file.exists() else {}
    configured = bool(cfg.get("configured", False))
    MON = date.fromisoformat(str(cfg["semester_start"])) if configured else None
    week_rows = []
    for wk in range(1, 17):
        if configured and MON is not None:
            mon = MON + timedelta(weeks=wk - 1)
            date_cell = f"{mon.strftime('%b %d')} \u2013 {(mon + timedelta(days=6)).strftime('%b %d, %Y')}"
        else:
            date_cell = "\u2014"
        ls = [x for x in lectures if x["week"] == wk]
        titles = "; ".join(f"{x['code']} {x['title']}" for x in ls)
        unit_ids = sorted({x["unit"] for x in ls})
        a_notes = []
        for x in ls:
            if x.get("assessment"):
                a_notes.append(x["assessment"])
        for a in assessment_plan:
            if a["schedule"].startswith(f"W{wk} "):
                a_notes.append(f"{a['name']} ({a['schedule']})")
        a_cell = "; ".join(a_notes) if a_notes else "—"
        week_rows.append(
            f"| {wk} | {date_cell} "
            f"| {', '.join(unit_ids)} | {titles} | {a_cell} |"
        )
    key = "\n".join(
        f"| {a['id']} | {a['name']} | {a['weight']}% | {a['clos']} | {a['schedule']} |"
        for a in assessment_plan
    )
    if configured:
        date_note = (
            f"> Semester dates are **instructor-configured** — week 1 begins"
            f"{f' ({cfg.get('term_label', '').strip()})' if cfg.get('term_label') else ''} "
            f"in the week of **{MON.strftime('%B %d, %Y')}**. Holidays shift "
            "individual lectures; see the [semester calendar](../calendar/index.md)."
        )
    else:
        date_note = (
            "> **Dates are not configured.** The instructor sets the semester "
            "start, teaching days, and holidays in `planning/schedule-config.yaml`; "
            "until then this schedule shows **relative weeks only**. After "
            "configuration, dates appear here and in the "
            "[semester calendar](../calendar/index.md)."
        )
    return (
        HEADER_NOTE
        + f"""# Weekly schedule

{date_note}

| Week | Dates | Units | Lectures | Assessment due |
|------|-------|-------|----------|----------------|
{chr(10).join(week_rows)}

## Assessment key

| ID | Component | Weight | CLOs | Timing |
|----|-----------|--------|------|--------|
{key}
"""
    )


# ────────────────────────────────────────────────────────────────────────────
# CLO x lecture mapping (planning/04-clo-mapping.md)
# ────────────────────────────────────────────────────────────────────────────
def clo_mapping(clos: list, lectures: list, assessment_plan: list) -> str:
    marks = {c["id"]: {} for c in clos}
    for l in lectures:
        for cid in l["clo"]:
            if cid in marks:
                marks[cid][l["num"]] = l["code"]
    rows = []
    for c in clos:
        cells = []
        for l in lectures:
            cells.append(f"**{marks[c['id']][l['num']]}**" if l["num"] in marks[c["id"]] else "·")
        bloom = ", ".join(sorted({l["bloom"] for l in lectures if l["num"] in marks[c["id"]]}))
        assess = "; ".join(
            a["name"] for a in assessment_plan if c["id"] in a.get("clos", [])
        )
        rows.append(
            f"| {c['id']} | {bloom} | {' · '.join(cells)} | {assess} |"
        )
    header = "| CLO | Bloom levels | " + " | ".join(l["code"] for l in lectures) + " |"
    rule = "|-----|" + "-----|" * len(lectures)
    statement_rows = "\n".join(
        f"| {c['id']} | {c['statement'].strip()} | {c['assessment']} |"
        for c in clos
    )
    return (
        HEADER_NOTE
        + f"""# CLO-to-lecture mapping

> Generated from `planning/course-data.yaml` (clos + lectures).

## Outcome statements

| CLO | Statement | Assessed by |
|-----|-----------|-------------|
{statement_rows}

## Coverage matrix (bold = primary coverage)

{header}
{rule}
{chr(10).join(rows)}

## Reading the matrix

- A bold cell means the CLO is **primarily taught and practiced** in that lecture.
- Bloom level is taken as the highest level targeted across those lectures.
- Every CLO maps to at least one assessment component (see
  [Assessment framework](03-assessment-framework.md)).
"""
    )


# ────────────────────────────────────────────────────────────────────────────
# Case matrix (planning/06-case-matrix.md)
# ────────────────────────────────────────────────────────────────────────────
def case_matrix(cases: list, lectures: list) -> str:
    lecture_of = {l["num"]: l["code"] for l in lectures}
    rows = []
    for c in cases:
        lec = lecture_of.get(c["lecture"], "—") if c["lecture"] else "—"
        uses = ", ".join(c["use"])
        rows.append(
            f"| {c['id']} | {c['title']} | {c['domain']} | {c['level']} | {lec} | {uses} |"
        )
    dist_levels = {}
    dist_domains = {}
    for c in cases:
        dist_levels[c["level"]] = dist_levels.get(c["level"], 0) + 1
        dist_domains[c["domain"]] = dist_domains.get(c["domain"], 0) + 1
    lv = "  ".join(f"{k}: {v}" for k, v in sorted(dist_levels.items()))
    dm = "  ".join(f"{k}: {v}" for k, v in sorted(dist_domains.items()))
    return (
        HEADER_NOTE
        + f"""# Case-study matrix (105 cases)

> Generated from `planning/case-catalog.yaml`.

## Progression snapshot

| Level | Meaning | Count |
|-------|---------|-------|
| L1 | Single-concept drill | {dist_levels.get('L1', 0)} |
| L2 | Two-concept applied | {dist_levels.get('L2', 0)} |
| L3 | Multi-concept analysis | {dist_levels.get('L3', 0)} |
| L4 | Cross-domain integration | {dist_levels.get('L4', 0)} |
| L5 | Open-ended strategic | {dist_levels.get('L5', 0)} |

## Domain snapshot

{dm}

## Full matrix

| ID | Title | Domain | Level | Anchored in | Use |
|----|-------|--------|-------|-------------|-----|
{chr(10).join(rows)}
"""
    )


# ────────────────────────────────────────────────────────────────────────────
# Case pages (student view)
# ────────────────────────────────────────────────────────────────────────────
LEVEL_MEANING = {
    "L1": "Single-concept drill",
    "L2": "Two-concept applied",
    "L3": "Multi-concept analysis",
    "L4": "Cross-domain integration",
    "L5": "Open-ended strategic",
}


def case_page(c: dict, case_by_id: dict) -> str:
    if c.get("lecture"):
        lecture_code = f"[Lecture {c['lecture']:02d}](../lectures/L{c['lecture']:02d}-{c.get('lecture_slug', '')}.md)"
        anchor_line = f"- Anchored in {lecture_code}."
    else:
        anchor_line = "- Distributed through the LMS (no in-class anchor)."
    difficulty_label = c.get("difficulty", "—").capitalize()
    return HEADER_NOTE + f"""# {c['id']} — {c['title']}

!!! info "Case card"
    **Difficulty:** {difficulty_label} ({BAND_RANGE[c['band']]}) ·
    **Level:** {c['level']} — {LEVEL_MEANING[c['level']]} ·
    **Domain:** {c['domain']} · **Seed project:** {c.get('seed') or 'standalone'}

## Learning objectives

""" + "\n".join(f"{i}. {o}" for i, o in enumerate(c["objectives"], 1)) + f"""

## Project context

{c['context']}

## Problem statement

{c['problem']}

## Constraints and available information

""" + "\n".join(f"- {x}" for x in c["constraints"]) + f"""

## Student tasks

""" + "\n".join(f"{i}. {t}" for i, t in enumerate(c["tasks"], 1)) + f"""

## Expected deliverables

""" + "\n".join(f"- {d}" for d in c["deliverables"]) + f"""

## Discussion questions

""" + "\n".join(f"1. {q}" for q in c["discussion"]) + f"""

## How you will be graded

{c['rubric']}

## Where this case appears

{anchor_line}
- Suggested use: {', '.join(c['use'])}.

*Submit individual case analyses to the course LMS unless announced otherwise.
Answer keys and facilitation notes are instructor-only and are not published.*
"""


def case_key(c: dict) -> str:
    """Instructor-only answer key; never published to the site."""
    sol = c.get("solution", {})
    alts = sol.get("alternatives") or []
    alt_md = "\n".join(f"- {a}" for a in alts) if alts else "- None recorded."
    numeric_md = ""
    if c.get("numeric"):
        n = c["numeric"]
        rows = []
        if "steps" in n:
            for s in n["steps"]:
                rows.append(f"| {s['name']} | `{s['expr']}` | {s['expect']} |")
            numeric_md = ("\n## Machine-checked values\n\n"
                          "Recomputed from the data block by `tools/check_cases.py`.\n\n"
                          "| Step | Expression | Value |\n|---|---|---|\n"
                          + "\n".join(rows) + "\n")
        else:
            numeric_md = ("\n## Machine-checked values\n\n"
                          "Recomputed from the data block by `tools/check_cases.py` — "
                          "see the data/expected blocks in `planning/cases/" + 
                          "` and the checker output.\n")
    calc_md = f"\n**Calculations:** {sol['calculations']}\n" if sol.get("calculations") else ""
    return """# Answer key — {cid} · {title}

> **INSTRUCTOR ONLY — not published to the site.**

**Model answer:** {model}

## Reasoning

{reasoning}

## Alternatives and evaluation criteria

{alts}{calc_md}{numeric_md}
## Facilitation

{lesson}
""".format(
        cid=c["id"], title=c["title"], model=sol["model"],
        reasoning=sol["reasoning"], alts=alt_md, calc_md=calc_md,
        numeric_md=numeric_md,
        lesson=sol.get("lesson_for_instructor", "—"),
    )


def case_directory(cases: list) -> str:
    sections = []
    for band in ("beginner", "intermediate", "advanced", "expert"):
        rows = []
        for c in cases:
            if c.get("band") != band:
                continue
            lec = f"L{c['lecture']:02d}" if c.get("lecture") else "LMS"
            nums = "🔢" if c.get("numerical") else ""
            rows.append(
                f"| [{c['id']}]({c['id']}.md) | {c['title']} {nums} | "
                f"{c['level']} | {lec} |"
            )
        title = band.capitalize()
        sections.append(
            f"## {title} — {BAND_RANGE[band]}\n\n"
            f"| ID | Title | Level | Anchored in |\n|----|-------|-------|-------------|\n"
            + "\n".join(rows)
        )
    n_num = sum(1 for c in cases if c.get("numerical"))
    anchored = sum(1 for c in cases if c.get("lecture"))
    return HEADER_NOTE + f"""# Case studies — 105 progressive cases

All 105 cases are published as briefs. 🔢 marks the {n_num} cases with a
machine-checked numerical core. {anchored} are anchored to in-class lectures;
the rest are distributed through the LMS for homework, exams, and the
portfolio/capstone feeders.

""" + "\n\n".join(sections) + f"""

## Tags

Search the tags below to filter by theme.

{tag_cloud(cases)}

*Full progression design lives in the repository planning dossier
(`planning/08-case-study-architecture.md`). Answer keys and facilitation notes
are instructor-only and are not published.*
"""


def tag_cloud(cases: list) -> str:
    counts = {}
    for c in cases:
        for t in c.get("tags", []):
            counts[t] = counts.get(t, 0) + 1
    items = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    return "\n".join(
        f"**{t}** ×{n}" + (" ·" if i < len(items) - 1 else "")
        for i, (t, n) in enumerate(items)
    )


# ────────────────────────────────────────────────────────────────────────────
# Detailed syllabus (knowledge-area map + unit prose + CLO chain)
# ────────────────────────────────────────────────────────────────────────────
def detailed_syllabus(doc: dict) -> str:
    course = doc["course"]
    lectures = doc["lectures"]
    units = doc["units"]
    clos = {c["id"]: c for c in doc["clos"]}
    lec_by_num = {l["num"]: l for l in lectures}

    ka_rows = []
    for ka in doc.get("knowledge_areas", []):
        lecs = ", ".join(lec_by_num[n]["code"] for n in ka["lectures"])
        ka_rows.append(
            f"| {ka['id']} | {ka['title']} | {', '.join(ka['clos'])} | {lecs} |"
        )

    unit_lines = []
    for u in units:
        lec_codes = ", ".join(lec_by_num[n]["code"] for n in u["lectures"])
        unit_lines.append(
            f"### {u['id']} — {u['title']} · {lec_codes}\n\n{u['description']}\n"
        )

    clo_lines = []
    for cid, c in clos.items():
        ta = ", ".join(lec_by_num[n]["code"] for n in c["lectures"])
        clo_lines.append(
            f"### {cid} — {c['bloom']}\n\n{c['statement'].strip()}\n\n"
            f"*Taught in:* {ta}. *Assessed by:* {c['assessment']}.\n"
        )

    return (
        HEADER_NOTE
        + f"""# Detailed Syllabus

> **{course['code']} {course['title']}** · {course['level']} ·
> {', '.join(course['programs'])} · {course['duration_weeks']} weeks ·
> {course['lecture_hours']} lectures × {course['lecture_length_hours']} h =
> {course['contact_hours']} contact hours
>
> Companion pages: [course description](course-description.md) ·
> [weekly schedule](weekly-schedule.md) · [textbooks](textbooks.md) ·
> [policies](course-policies.md) · [delivery methodology](delivery-methodology.md)

## 1. Knowledge-area coverage map

Every lecture advances at least one knowledge area; every area is exercised
in at least one lecture and assessed through its mapped CLOs.

| Area | Title | CLOs | Carried by lectures |
|------|-------|------|---------------------|
{chr(10).join(ka_rows)}

## 2. Unit structure

{chr(10).join(unit_lines)}
## 3. Course learning outcomes — teaching & assessment chain

{chr(10).join(clo_lines)}
*The full CLO × lecture matrix (32 columns) is machine-generated in the
repository planning dossier (`planning/04-clo-mapping.md`); the per-CLO view
above is the student-facing summary.*
"""
    )


def lesson_plan(l: dict, case_by_id: dict) -> str:
    case_lines = "\n".join(
        f"- {cid}: {case_by_id[cid]['title']} (level {case_by_id[cid]['level']}, "
        f"uses {', '.join(case_by_id[cid]['use'])}, "
        f"{'numeric' if case_by_id[cid].get('numerical') else 'discussion'})"
        for cid in l["cases"]
    )
    timing = [
        ("0:00–0:10", "Hook: " + l["tagline"]),
        ("0:10–0:50", f"Block 1: {l['topics'][0]['title']}"),
        ("0:50–1:30", f"Block 2: {l['topics'][1]['title']} + activity"),
        ("1:30–2:00", f"Block 3: {l['topics'][2]['title']} + activity + wrap-up"),
    ]
    timing_rows = "\n".join(f"| {t} | {what} |" for t, what in timing)
    return f"""# Lesson plan — {l['code']} {l['title']}

> **INSTRUCTOR ONLY — not published to the course site.**

**Week {l['week']} · Unit {l['unit']} · CLOs {', '.join(l['clo'])} · Bloom {l['bloom']}**

## Timing plan (2 hours)

| Slot | Segment |
|------|---------|
{timing_rows}

## Talking points

{render_topics(l["topics"])}
## Cases to run

{case_lines}

## Activities to facilitate

{render_activities(l["activities"])}

## Anticipated misconceptions (to be filled per lecture)

- (blank — instructor fills during delivery iteration)

## Assessment notes

{l.get('assessment') or 'No anchored assessment.'}
"""


# ────────────────────────────────────────────────────────────────────────────
# Instructor case index (NOT published)
# ────────────────────────────────────────────────────────────────────────────
def case_index(cases: list) -> str:
    rows = "\n".join(
        f"| [{c['id']}](../instructor/answer-keys/cases/{c['id']}.md) | {c['title']} | "
        f"{c['difficulty'].capitalize()} | {c['domain']} | {c['level']} | "
        f"{', '.join(c['use'])} | {'yes' if c.get('numerical') else ''} |"
        for c in cases
    )
    return (
        "# Instructor case index\n\n"
        "> **INSTRUCTOR ONLY — not published.** Links point to the full answer keys.\n\n"
        "| ID | Title | Difficulty | Domain | Level | Use | Numeric |\n"
        "|----|-------|-----------|--------|-------|-----|---------|\n"
        + rows
        + "\n"
    )


# ────────────────────────────────────────────────────────────────────────────
def main() -> int:
    global STDOUT_MODE
    parser = argparse.ArgumentParser()
    parser.add_argument("--stdout", action="store_true",
                        help="emit generated files as JSON instead of writing to disk")
    args = parser.parse_args()
    STDOUT_MODE = args.stdout

    doc = load_yaml(COURSE_FILE)
    cases_doc = {"cases": load_cases()}
    course = doc["course"]
    lectures = doc["lectures"]
    case_by_id = {c["id"]: c for c in cases_doc["cases"]}

    print("Generating course artifacts...")

    # 1) 32 lecture pages
    anchored_by_lecture = {}
    for c in cases_doc["cases"]:
        if c.get("lecture"):
            anchored_by_lecture.setdefault(c["lecture"], []).append(c["id"])
    for l in lectures:
        write(p("docs", "lectures", f"L{l['num']:02d}-{l['slug']}.md"),
              lecture_page(l, course, case_by_id, anchored_by_lecture))

    # 2) curriculum map + schedule
    write(p("docs", "lectures", "index.md"),
          curriculum_map(course, lectures, doc["units"]))
    write(p("docs", "syllabus", "weekly-schedule.md"),
          weekly_schedule(course, lectures, doc["assessment_plan"]))
    write(p("docs", "syllabus", "detailed-syllabus.md"), detailed_syllabus(doc))

    # 3) planning matrices
    write(p("planning", "04-clo-mapping.md"),
          clo_mapping(doc["clos"], lectures, doc["assessment_plan"]))
    write(p("planning", "06-case-matrix.md"),
          case_matrix(cases_doc["cases"], lectures))

    # 4) instructor materials (not published)
    for l in lectures:
        write(p("instructor", "lesson-plans", f"{l['code']}.md"), lesson_plan(l, case_by_id))
    write(p("instructor", "answer-keys", "case-index.md"), case_index(cases_doc["cases"]))

    # 5) shared lecture footer include
    write(p("docs", "lectures", "lesson-footer.md"),
          "*[Back to curriculum map](index.md) · "
          "[Course description](../syllabus/course-description.md) · "
          "[All cases](../cases/index.md) · Report an issue on GitHub.*\n")

    # 6) case pages (student view — full briefs; answers stay in instructor/)
    slug_of = {l["num"]: l["slug"] for l in lectures}
    for c in cases_doc["cases"]:
        cc = {**c, "lecture_slug": slug_of[c["lecture"]]} if c.get("lecture") else c
        write(p("docs", "cases", f"{c['id']}.md"), case_page(cc, case_by_id))
        write(p("instructor", "answer-keys", "cases", f"{c['id']}.md"), case_key(cc))
    write(p("docs", "cases", "index.md"), case_directory(cases_doc["cases"]))

    if STDOUT_MODE:
        print(json.dumps(OUTPUT))
    else:
        print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
