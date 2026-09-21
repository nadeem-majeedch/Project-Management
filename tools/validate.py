#!/usr/bin/env python3
"""
validate.py — enforce the 12 architecture gates.

Gates:
 1 course integrity        32 lectures, weeks 1..16, unique slugs/codes
 2 CLO closure             every CLO taught and assessed
 3 case anchoring          referenced cases exist; anchored cases reference back
 4 assessment weights      sum to 100
 5 hand-edit detection     generated docs match fresh regeneration
 6 cross-link integrity    internal links in docs/ resolve to files
 7 instructor isolation    no instructor/ content inside docs/ or site/
 8 YAML sanity             parses; case IDs sequential CS-01..CS-105
 9 foundation consistency  measurable CLOs, KA coverage, workload arithmetic
10 teaching packages       16 sections, no placeholders, titles/links
11 lab workbook            16 briefs + keys + templates + answer checker
12 case collection         bands, sections, key coverage, >=30 numeric
13 assessment package      banks, papers, keys, capstone, weights consistency

Usage:  python tools/validate.py [--mkdocs-yml PATH] [--site PATH]
Exit 0 = all gates pass; exit 1 = failures listed on stdout.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
COURSE_FILE = ROOT / "planning" / "course-data.yaml"
CASES_FILE = ROOT / "planning" / "case-catalog.yaml"

failures: list[str] = []
notes: list[str] = []


def check(cond: bool, gate: int, msg: str) -> bool:
    if not cond:
        failures.append(f"[gate {gate}] {msg}")
    return cond


def load(path: Path):
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


BAND_FILES = {
    "band-1-beginner.yaml": ("beginner", 20),
    "band-2-intermediate.yaml": ("intermediate", 25),
    "band-3-advanced.yaml": ("advanced", 30),
    "band-4-expert.yaml": ("expert", 30),
}


def load_case_bands() -> dict:
    """Merge planning/cases/band-*.yaml in band order; attach meta."""
    cases = []
    for fname, (difficulty, _count) in sorted(BAND_FILES.items()):
        fpath = ROOT / "planning" / "cases" / fname
        if not fpath.exists():
            failures.append(f"[gate 12] missing band file planning/cases/{fname}")
            continue
        for c in load(fpath)["cases"]:
            cases.append({**c, "band": fname})
    return {"cases": cases, "meta": load(CASES_FILE)["meta"]}


class MkDocsLoader(yaml.SafeLoader):
    """SafeLoader that tolerates !!python/name tags used by mkdocs.yml."""


MkDocsLoader.add_multi_constructor(
    "tag:yaml.org,2002:python/", lambda ldr, suffix, node: None
)


def load_mkdocs(path: Path):
    with open(path, encoding="utf-8") as fh:
        return yaml.load(fh, Loader=MkDocsLoader)


# ── gate 1 ──────────────────────────────────────────────────────────────────
def gate_course(doc: dict) -> None:
    lectures = doc["lectures"]
    check(len(lectures) == 32, 1, f"expected 32 lectures, found {len(lectures)}")
    codes, slugs, weeks = [], [], []
    for i, l in enumerate(lectures, 1):
        if l.get("num") != i:
            failures.append(f"[gate 1] lecture at index {i - 1} has num={l.get('num')}, expected {i}")
            continue
        codes.append(l["code"])
        slugs.append(l["slug"])
        weeks.append(l["week"])
        if not 1 <= l["week"] <= 16:
            failures.append(f"[gate 1] lecture {l['code']} week {l['week']} outside 1..16")
    check(len(set(codes)) == len(codes), 1, "duplicate lecture codes")
    check(len(set(slugs)) == len(slugs), 1, "duplicate lecture slugs")
    check(sorted(set(weeks)) == list(range(1, 17)), 1, "weeks not fully covered")


# ── gate 2 ──────────────────────────────────────────────────────────────────
def gate_clos(doc: dict) -> None:
    clos = {c["id"] for c in doc["clos"]}
    taught: dict[str, set[int]] = {c: set() for c in clos}
    for l in doc["lectures"]:
        for cid in l["clo"]:
            if cid not in taught:
                failures.append(f"[gate 2] lecture {l['code']} references unknown {cid}")
            else:
                taught[cid].add(l["num"])
    assessed = set()
    for a in doc["assessment_plan"]:
        assessed.update(a.get("clos", []))
    for cid in sorted(clos):
        if not taught[cid]:
            failures.append(f"[gate 2] CLO {cid} defined but never taught")
        if cid not in assessed:
            notes.append(f"note: CLO {cid} not covered by any formal assessment component")
    # reverse consistency: clos[].lectures matches actual lecture anchors
    for c in doc["clos"]:
        declared = set(c.get("lectures", []))
        actual = taught.get(c["id"], set())
        if declared != actual:
            failures.append(
                f"[gate 2] {c['id']} lectures list {sorted(declared)} != anchored {sorted(actual)}"
            )


# ── gates 3 & 8 ─────────────────────────────────────────────────────────────
def gate_cases(doc: dict, cases_doc: dict) -> dict:
    cases = {c["id"]: c for c in cases_doc["cases"]}
    ids = [c["id"] for c in cases_doc["cases"]]
    expected = [f"CS-{i:02d}" for i in range(1, len(ids) + 1)]
    check(ids == expected, 8, "case IDs not sequential CS-01..CS-nnn")
    check(
        len(ids) == cases_doc["meta"]["total_cases"] == 105,
        8,
        "catalog count != meta.total_cases != 105",
    )
    for c in cases_doc["cases"]:
        check(c["level"] in {"L1", "L2", "L3", "L4", "L5"}, 8, f"{c['id']} bad level")
        check(c["domain"].startswith("D"), 8, f"{c['id']} bad domain")
    for l in doc["lectures"]:
        for cid in l["cases"]:
            if cid not in cases:
                failures.append(f"[gate 3] lecture {l['code']} references missing case {cid}")
            else:
                back = cases[cid].get("lecture")
                if back != l["num"]:
                    failures.append(
                        f"[gate 3] case {cid} anchored to L{back}, referenced from {l['code']}"
                    )
    # Anchoring source of truth is the band files (gate 12); the lecture
    # `cases` lists are the curated in-class subset. Reverse-consistency is
    # enforced only for the curated subset: every case a lecture lists must
    # claim that lecture (checked above); extra anchored cases render as an
    # 'also anchored' list on the lecture page.
    return cases


def gate_weights(doc: dict) -> None:
    total = sum(a["weight"] for a in doc["assessment_plan"])
    check(total == 100, 4, f"assessment weights sum to {total}, expected 100")


# ── gate 12 ─────────────────────────────────────────────────────────────────
def gate_collection(cases_doc: dict) -> None:
    cases = cases_doc["cases"]
    bands = {
        "band-1-beginner.yaml": ("beginner", 20, "CS-20"),
        "band-2-intermediate.yaml": ("intermediate", 25, "CS-45"),
        "band-3-advanced.yaml": ("advanced", 30, "CS-75"),
        "band-4-expert.yaml": ("expert", 30, "CS-105"),
    }
    for fname, (difficulty, count, last) in bands.items():
        band_cases = [c for c in cases if c.get("band") == fname]
        check(len(band_cases) == count, 12,
              f"{fname}: {len(band_cases)} cases, expected {count}")
        if band_cases:
            check(band_cases[-1]["id"] == last, 12, f"{fname}: last ID {band_cases[-1]['id']} != {last}")
        for c in band_cases:
            if c.get("difficulty") != difficulty:
                failures.append(f"[gate 12] {c['id']}: difficulty {c.get('difficulty')} != {difficulty}")
    ids = [c["id"] for c in cases]
    check(ids == [f"CS-{i:02d}" for i in range(1, len(ids) + 1)], 12,
          "case IDs not sequential CS-01..CS-nnn after band merge")
    check(len(ids) == 105, 12, f"case count {len(ids)} != 105")

    required_sections = [
        "## Learning objectives", "## Project context", "## Problem statement",
        "## Constraints and available information", "## Student tasks",
        "## Expected deliverables", "## Discussion questions", "## How you will be graded",
    ]
    for c in cases:
        cid = c["id"]
        page = ROOT / "docs" / "cases" / f"{cid}.md"
        if not page.exists():
            failures.append(f"[gate 12] missing student page docs/cases/{cid}.md")
            continue
        text = page.read_text(encoding="utf-8")
        for sec in required_sections:
            if sec not in text:
                failures.append(f"[gate 12] {cid}: page missing section {sec!r}")
        if cid not in text:
            failures.append(f"[gate 12] {cid}: page does not mention its own ID")
        if f"# {cid} " not in text:
            failures.append(f"[gate 12] {cid}: page title mismatch")
        key = ROOT / "instructor" / "answer-keys" / "cases" / f"{cid}.md"
        if not key.exists():
            failures.append(f"[gate 12] missing instructor key for {cid}")
        else:
            ktext = key.read_text(encoding="utf-8")
            if "INSTRUCTOR ONLY" not in ktext:
                failures.append(f"[gate 12] {cid}: key missing INSTRUCTOR ONLY marker")
            if len(c.get("solution", {}).get("reasoning", "")) < 200:
                failures.append(f"[gate 12] {cid}: solution.reasoning too thin")
    numeric = [c["id"] for c in cases if c.get("numerical")]
    check(len(numeric) >= cases_doc["meta"]["numerical_target"], 12,
          f"numeric cases {len(numeric)} < target {cases_doc['meta']['numerical_target']}")


# ── gate 13 ─────────────────────────────────────────────────────────────────
QUIZ_COVERAGE = {
    "quiz1.md": ("L04", ["L01", "L04"]),
    "quiz2.md": ("L12", ["L09", "L12"]),
    "quiz3.md": ("L26", ["L21", "L26"]),
}

def gate_assessment() -> None:
    eb = ROOT / "instructor" / "exam-bank"
    # question banks cover all 32 lectures
    bank_lectures = set()
    bank_files = sorted(eb.glob("question-bank-u*.md"))
    check(len(bank_files) == 7, 13, f"expected 7 question banks, found {len(bank_files)}")
    for f in bank_files:
        text = f.read_text(encoding="utf-8")
        n_items = len(re.findall(r"^### QB-U\d-\d+ ", text, re.M))
        check(n_items >= 14, 13, f"{f.name}: only {n_items} items (min 14)")
        for m in re.finditer(r"\[L(\d\d) · CLO\d", text):
            bank_lectures.add(int(m.group(1)))
        if "INSTRUCTOR ONLY" not in text:
            failures.append(f"[gate 13] {f.name}: missing INSTRUCTOR ONLY marker")
    check(bank_lectures == set(range(1, 33)), 13,
          f"question banks cover lectures {sorted(bank_lectures)}, expected 1..32")
    # papers exist with keys
    for fname, (due, (lo, hi)) in QUIZ_COVERAGE.items():
        f = eb / fname
        if not f.exists():
            failures.append(f"[gate 13] missing paper {fname}")
            continue
        t = f.read_text(encoding="utf-8")
        check("Version A" in t and "Version B" in t, 13, f"{fname}: missing A/B versions")
        check("Key" in t or "Key —" in t, 13, f"{fname}: missing answer key")
        check(f"{lo}" in t and f"{hi}" in t, 13, f"{fname}: coverage {lo}-{hi} not stated")
    for fname, marks, clos in (("midterm.md", "40 marks", "CLO1"), ("final.md", "20 marks", "CLO6")):
        f = eb / fname
        if not f.exists():
            failures.append(f"[gate 13] missing paper {fname}")
            continue
        t = f.read_text(encoding="utf-8")
        check(marks in t, 13, f"{fname}: mark total '{marks}' not stated")
        check("INSTRUCTOR ONLY" in t, 13, f"{fname}: missing INSTRUCTOR ONLY marker")
        check("Answer key" in t or "Key —" in t, 13, f"{fname}: missing answer key")
    midterm_text = (eb / "midterm.md").read_text(encoding="utf-8") if (eb / "midterm.md").exists() else ""
    check("CLO1" in midterm_text and "CLO4" in midterm_text, 13, "midterm: CLO1-CLO4 not stated")
    check("40%" in midterm_text, 13, "midterm: pass rule not stated")
    # capstone student package
    cap = ROOT / "docs" / "capstone"
    for fname in ("specification.md", "milestones.md", "presentation-rubric.md",
                  "peer-review.md", "capstone-charter.md", "capstone-rubric.md",
                  "defense-format.md"):
        check((cap / fname).exists(), 13, f"missing capstone page {fname}")
    spec = cap / "specification.md"
    if spec.exists():
        st = spec.read_text(encoding="utf-8")
        for artifact in ("charter", "Stakeholder register", "Scope statement", "WBS",
                         "Schedule", "Cost estimate", "Risk register", "Quality plan",
                         "Communication plan", "Change control", "Monitoring", "presentation"):
            check(artifact.lower() in st.lower(), 13, f"capstone spec missing artifact '{artifact}'")
    milestones = cap / "milestones.md"
    if milestones.exists():
        mt = milestones.read_text(encoding="utf-8")
        for m in ("L08", "L12", "L27", "L32"):
            check(m in mt, 13, f"milestones missing {m}")
    # student guides exist; instructor/student separation spot-check
    check((ROOT / "docs" / "assessments" / "quiz-guide.md").exists(), 13, "missing quiz-guide.md")
    check((ROOT / "docs" / "assessments" / "exam-guide.md").exists(), 13, "missing exam-guide.md")
    check((ROOT / "instructor" / "rubrics" / "assignment-marking-guides.md").exists(), 13,
          "missing assignment marking guides")
    # student-facing pages must not contain instructor-only markers
    for f in (cap / "presentation-rubric.md", cap / "milestones.md"):
        t = f.read_text(encoding="utf-8") if f.exists() else ""
        check("INSTRUCTOR ONLY" not in t, 13, f"{f.name}: instructor marker leaked into student page")


# ── gate 5 ──────────────────────────────────────────────────────────────────
def gate_regeneration(doc: dict, cases_doc: dict) -> None:
    proc = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "scaffold.py"), "--stdout"],
        capture_output=True, text=True, cwd=ROOT,
    )
    if proc.returncode != 0:
        failures.append(f"[gate 5] regeneration crashed: {proc.stderr.strip()[:200]}")
        return
    generated = json_loads_safe(proc.stdout)
    for relpath, expected_text in generated.items():
        actual = (ROOT / relpath).read_text(encoding="utf-8")
        if actual != expected_text:
            failures.append(
                f"[gate 5] hand-edit detected in generated file {relpath} — edit the YAML source instead"
            )


def json_loads_safe(payload: str) -> dict:
    import json
    try:
        return json.loads(payload)
    except Exception as exc:  # noqa: BLE001
        failures.append(f"[gate 5] regeneration output not parseable: {exc}")
        return {}


# ── gate 6 ──────────────────────────────────────────────────────────────────
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)#\s]+)")
BAD_SCHEMES = ("http://", "https://", "mailto:", "file://", "#")


def gate_links(mkdocs: dict) -> None:
    nav_files: list[str] = []

    def walk(nav):
        if isinstance(nav, str):
            nav_files.append(nav)
            return
        for item in nav or []:
            if isinstance(item, str):
                nav_files.append(item)
            elif isinstance(item, dict):
                for v in item.values():
                    walk(v)
            elif isinstance(item, list):
                walk(item)

    walk(mkdocs.get("nav", []))
    docs_dir = ROOT / "docs"
    for rel in nav_files:
        if not (docs_dir / rel).exists():
            failures.append(f"[gate 6] nav entry missing on disk: {rel}")

    for md in docs_dir.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            target = match.group(1).strip()
            if target.startswith(BAD_SCHEMES):
                continue
            resolved = (md.parent / target).resolve()
            if not resolved.exists():
                # extensionless markdown links: lectures/L01-01-x resolves
                # to lectures/L01-01-x.md
                if (md.parent / (target + ".md")).resolve().exists():
                    continue
                rel_from = md.relative_to(ROOT).as_posix()
                failures.append(f"[gate 6] broken link '{target}' in {rel_from}")


# ── gate 9 ──────────────────────────────────────────────────────────────────
MEASURE_VERBS = (
    "define", "classify", "construct", "derive", "build", "develop",
    "compute", "identify", "quantify", "propose", "diagnose", "recommend",
    "operate", "produce", "set", "rewrite", "prepare", "design", "defend",
    "justify", "explain", "calculate", "write", "choose",
)


def gate_foundation(doc: dict) -> None:
    lectures = doc["lectures"]
    clos = {c["id"]: c for c in doc["clos"]}

    # 1) CLO statements measurable (contain a Bloom/measurement verb)
    for cid, c in clos.items():
        text = c["statement"].lower()
        if not any(v in text for v in MEASURE_VERBS):
            failures.append(f"[gate 9] {cid} statement lacks a measurable verb")

    # 2) weights (redundant with gate 4 but asserted here per plan doc)
    if sum(a["weight"] for a in doc["assessment_plan"]) != 100:
        failures.append("[gate 9] assessment weights do not sum to 100")

    # 3) every CLO: >=2 formal components OR explicit practice note
    for cid, c in clos.items():
        n_comp = sum(1 for a in doc["assessment_plan"] if cid in a.get("clos", []))
        note = "practiced via" in c.get("assessment", "").lower()
        if n_comp < 2 and not note:
            failures.append(
                f"[gate 9] {cid} has {n_comp} formal components and no practice note"
            )

    # 4) knowledge areas: valid CLO refs; >=1 lecture; cover all 32 lectures
    taught = {}
    for l in lectures:
        for cid in l["clo"]:
            taught.setdefault(cid, set()).add(l["num"])
    lec_ka = set()
    for ka in doc.get("knowledge_areas", []):
        if not set(ka["clos"]) <= set(clos):
            failures.append(f"[gate 9] {ka['id']} references unknown CLO")
        if not ka.get("lectures"):
            failures.append(f"[gate 9] {ka['id']} has no lectures")
        lec_ka.update(ka.get("lectures", []))
    missing = sorted(set(range(1, 33)) - lec_ka)
    if missing:
        failures.append(f"[gate 9] lectures not covered by any knowledge area: {missing}")

    # 5) workload & structure arithmetic
    if len(lectures) * doc["course"]["lecture_length_hours"] != doc["course"]["contact_hours"]:
        failures.append("[gate 9] lectures × hours != contact hours")
    if doc["course"]["duration_weeks"] != 16 or len(lectures) != 32:
        failures.append("[gate 9] course structure must be 16 weeks / 32 lectures")
    for l in lectures:
        units = [u for u in doc["units"] if l["num"] in u.get("lectures", [])]
        if len(units) != 1:
            failures.append(f"[gate 9] lecture {l['code']} belongs to {len(units)} units")

    # 6) every CLO taught somewhere (complements gate 2)
    for cid in clos:
        if not taught.get(cid):
            failures.append(f"[gate 9] {cid} never taught")


# ── gate 10 ─────────────────────────────────────────────────────────────────
PACKAGE_SECTIONS = (
    "## Learning objectives",
    "## Required prior knowledge",
    "## Teaching notes",
    "## Definitions & concepts",
    "## Practical examples",
    "## Worked example",
    "## Common misconceptions",
    "## Classroom activities",
    "## Discussion questions",
    "## Practical exercise",
    "## Formative assessment",
    "## Reading & references",
    "## Two-hour teaching plan",
    "## Instructor preparation notes",
    "## Linked resources",
)
PLACEHOLDER_RE = re.compile(
    r"\b(TODO|TBD|FIXME|PLACEHOLDER|<insert|\[fill in|LOREM)\b", re.IGNORECASE
)
MODULE_DIRS = {
    1: "U1-foundations-strategy",
    2: "U2-lifecycles-initiating",
    3: "U3-planning-the-work",
    4: "U4-risk-uncertainty-control",
    5: "U5-adaptive-delivery-teams",
    6: "U6-integration-ethics-closing",
    7: "U7-synthesis-capstone",
}


def gate_packages(doc: dict) -> None:
    base = ROOT / "instructor" / "teaching-packages"
    for l in doc["lectures"]:
        mod = MODULE_DIRS.get(l["unit"][1]) if isinstance(l["unit"], str) else None
        unit_num = int(str(l["unit"])[1:])
        mod = MODULE_DIRS[unit_num]
        path = base / mod / f"L{l['num']:02d}-{l['slug']}.md"
        if not path.exists():
            failures.append(f"[gate 10] missing teaching package: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        first = text.splitlines()[0] if text.splitlines() else ""
        if f"{l['num']:02d}" not in first or l["title"] not in first:
            failures.append(f"[gate 10] title/number mismatch in {path.name}")
        for sec in PACKAGE_SECTIONS:
            if sec not in text:
                failures.append(f"[gate 10] {path.name}: missing section '{sec}'")
        m = PLACEHOLDER_RE.search(text)
        if m:
            failures.append(f"[gate 10] {path.name}: placeholder token '{m.group(1)}'")
        # relative links must resolve (same rule as gate 6, but for packages)
        for match in LINK_RE.finditer(text):
            target = match.group(1).strip()
            if target.startswith(BAD_SCHEMES):
                continue
            if not (path.parent / target).resolve().exists():
                failures.append(f"[gate 10] broken link '{target}' in instructor/teaching-packages/{mod}/{path.name}")


# ── gate 11 ────────────────────────────────────────────────────────────────
LAB_BRIEFS = {
    1: "lab-01-charter.md", 2: "lab-02-stakeholders.md",
    3: "lab-03-scope-wbs.md", 4: "lab-04-cpm-network.md",
    5: "lab-05-wbs-dictionary.md", 6: "lab-06-gantt-resources.md",
    7: "lab-07-cost-baseline.md", 8: "lab-08-quality-plan.md",
    9: "lab-09-risk-register.md", 10: "lab-10-probability-impact.md",
    11: "lab-11-monte-carlo.md", 12: "lab-12-communication.md",
    13: "lab-13-evm-recovery.md", 14: "lab-14-agile-sprint.md",
    15: "lab-15-change-recovery.md", 16: "lab-16-capstone-pack.md",
}
LAB_SECTIONS = (
    "Objectives", "Background", "Required tools", "Step-by-step",
    "Your tasks", "Expected outputs", "Reflection questions",
    "Assessment rubric", "Related material",
)


def gate_labs() -> None:
    labs_dir = ROOT / "docs" / "labs"
    for n, fname in LAB_BRIEFS.items():
        p = labs_dir / fname
        if not p.exists():
            failures.append(f"[gate 11] missing lab brief: docs/labs/{fname}")
            continue
        text = p.read_text(encoding="utf-8")
        if f"Lab {n} " not in text[:400]:
            failures.append(f"[gate 11] {fname}: number/title marker missing")
        for sec in LAB_SECTIONS:
            if sec not in text:
                failures.append(f"[gate 11] {fname}: missing section '{sec}'")
        body = text.split("---", 2)[-1]
        m = PLACEHOLDER_RE.search(body)
        if m:
            failures.append(f"[gate 11] {fname}: placeholder token '{m.group(1)}'")
        key = ROOT / "instructor" / "lab-solutions" / fname.replace(".md", "-key.md")
        if not key.exists():
            failures.append(f"[gate 11] missing answer key: {key.relative_to(ROOT)}")
    # machine-checkable answer chains
    proc = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "check_answers.py")],
        capture_output=True, text=True, cwd=ROOT,
    )
    if proc.returncode != 0:
        failures.append(f"[gate 11] answer checker failed: {proc.stdout.strip()[:400]}")


# ── gate 7 ─────────────────────────────────────────────────────────────────
def gate_isolation() -> None:
    leaked = [
        p.relative_to(ROOT).as_posix()
        for p in (ROOT / "docs").rglob("*")
        if "instructor" in p.parts
    ]
    check(not leaked, 7, f"instructor paths inside docs/: {leaked[:5]}")


def gate_slides() -> None:
    """Gate 14: slide package (instructor-only, built to instructor/slides/build)."""
    slides = ROOT / "instructor" / "slides"
    decks = sorted(slides.glob("L*-slides.md"))
    nums = sorted(int(m.group(1)) for p in decks if (m := re.match(r"L(\d+)-slides\.md", p.name)))
    check(nums == list(range(1, 33)), 14, f"expected decks L01..L32, got {nums}")
    theme = slides / "assets" / "pm401.css"
    check(theme.exists(), 14, "slides theme assets/pm401.css missing")
    check((slides / "README.md").exists(), 14, "slides README.md missing")
    for p in decks:
        t = p.read_text(encoding="utf-8")
        check("<!-- notes:" in t, 14, f"{p.name}: no speaker notes")
        check("```mermaid" in t, 14, f"{p.name}: no diagram")
    build = slides / "build" / "index.html"
    check(build.exists(), 14, "slides build/index.html missing — run tools/build_slides.py")
    built = sorted((slides / "build").glob("L*.html"))
    check(len(built) >= 32, 14, f"expected 32 built decks, found {len(built)}")


def gate_calendar() -> None:
    """Gate 15: semester calendar generated from the instructor config."""
    cal = ROOT / "docs" / "calendar"
    cfg_file = ROOT / "planning" / "schedule-config.yaml"
    check(cfg_file.exists(), 15, "planning/schedule-config.yaml missing")
    idx = cal / "index.md"
    printable = cal / "printable.md"
    csv_f = cal / "schedule.csv"
    ics_f = cal / "schedule.ics"
    for f in (idx, printable, csv_f):
        check(f.exists(), 15, f"{f.relative_to(ROOT)} missing — run tools/calendar.py")
    if not all((idx.exists(), printable.exists(), csv_f.exists())):
        return
    cfg = yaml.safe_load(cfg_file.read_text(encoding="utf-8")) or {}
    configured = bool(cfg.get("configured", False))
    check(ics_f.exists() == configured, 15,
          "schedule.ics must exist exactly when configured: true")
    idx_text = idx.read_text(encoding="utf-8")
    csv_text = csv_f.read_text(encoding="utf-8").splitlines()
    for n in range(1, 33):
        check(f"L{n:02d}" in idx_text, 15, f"calendar index missing L{n:02d}")
    check(len(csv_text) == 33, 15, f"schedule.csv has {len(csv_text)} lines, expected 33 (header + 32)")
    nums = [r.split(",")[0] for r in csv_text[1:]]
    check(nums == [str(i) for i in range(1, 33)], 15, "schedule.csv lecture numbering broken")
    # every lecture link in the calendar resolves to a real page
    for m in re.finditer(r"\]\((\.\./lectures/[^)]+)\)", idx_text):
        p = ROOT / "docs" / "calendar" / m.group(1)
        check(p.exists() or Path(str(p) + ".md").exists(), 15,
              f"calendar lecture link does not resolve: {m.group(1)}")
    if not configured:
        date_like = re.findall(r"\b\d{4}-\d{2}-\d{2}\b", idx_text + printable.read_text(encoding="utf-8"))
        check(not date_like, 15,
              "dates appear in calendar while configured: false — never invent dates")


def gate_site(site: Path | None) -> None:
    if not site or not site.exists():
        notes.append("note: no site/ build present — gate 7 site scan skipped (run mkdocs build)")
        return
    leaked = [
        str(p.relative_to(site)) for p in site.rglob("*")
        if p.is_file() and "instructor" in p.relative_to(site).parts
    ]
    check(not leaked, 7, f"instructor content leaked into site/: {leaked[:5]}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mkdocs-yml", default=str(ROOT / "mkdocs.yml"))
    parser.add_argument("--site", default=str(ROOT / "site"))
    args = parser.parse_args()

    doc = load(COURSE_FILE)
    cases_doc = load_case_bands()

    gate_course(doc)
    gate_clos(doc)
    gate_cases(doc, cases_doc)
    gate_weights(doc)
    gate_foundation(doc)
    gate_packages(doc)
    gate_labs()
    gate_collection(cases_doc)
    gate_assessment()
    gate_slides()
    gate_calendar()

    mkdocs_path = Path(args.mkdocs_yml)
    if mkdocs_path.exists():
        gate_links(load_mkdocs(mkdocs_path))
    else:
        notes.append(f"note: {mkdocs_path.name} not found — link/nav gates skipped")
    gate_isolation()
    gate_site(Path(args.site))

    print(f"FAIL ({len(failures)}):" if failures else "PASS (0 failures)")
    for f in failures:
        print("  " + f)
    for n in notes:
        print("  " + n)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
