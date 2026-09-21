# 10 — Generation & Validation Plan

## 1. Pipeline

```
planning/course-data.yaml ─┐
                           ├─ tools/scaffold.py ─→ docs/{lectures,cases,syllabus}/*
planning/case-catalog.yaml ┘                       instructor/{lesson-plans,answer-keys}/*
                                                   planning/{04,06}.md
                     edit YAML → run scaffold → run validate → build → deploy
```

Regeneration is idempotent and non-destructive: it rewrites only generated
files (marked with an auto-generated HTML comment) and never touches
hand-authored pages.

## 2. Validation gates (tools/validate.py)

| # | Gate | Failure condition |
|---|---|---|
| 1 | Course integrity | ≠ 32 lectures, weeks outside 1–16, duplicate slugs/codes |
| 2 | CLO closure | a CLO defined but never taught, or taught but unassessed |
| 3 | Case anchoring | referenced case missing; anchored case missing a lecture |
| 4 | Assessment weights | Σ weights ≠ 100 |
| 5 | Hand-edit detection | generated file's content diverges from regeneration |
| 6 | Cross-link integrity | internal `.md` links in generated docs that don't resolve |
| 7 | Instructor leak | any `instructor/` path inside `docs/` or `site/` |
| 8 | YAML sanity | both YAML files parse; case IDs sequential CS-01..CS-105 |
| 9 | Foundation consistency (Prompt 1) | measurable CLO verbs; every CLO ≥ 2 formal assessments or an explicit practice note; every knowledge area ≥ 1 lecture; all 32 lectures covered by KAs; 32 × 2 h = 64 h; unit/lecture 1:1 |

## 3. Executed validation log (updated as commands actually run)

| Command | Status | Actual result |
|---|---|---|
| `python tools/scaffold.py` | ✅ executed | exit 0; generated 32 lecture pages, 43 case briefs + case directory, curriculum map, weekly schedule, 32 instructor lesson plans, instructor case index, 2 planning matrices, lesson footer |
| `python tools/validate.py` | ✅ executed | first run correctly FAILed with 279 findings (stale CLO↔lecture lists, nav-walker bug, trailing-slash links); after 3 fixes → **PASS (0 failures)**, including gate 7 scan over the built `site/` |
| `pip install -r requirements.txt` (in `.venv`) | ✅ executed | mkdocs 1.6.1, Material 9.7.7 installed |
| `mkdocs build --strict --site-dir site` | ✅ executed | first run aborted on `not_in_nav` config type + 1 warning (broken planning link, broken anchor); after fixes → **strict build clean in ~1.3 s, 99 HTML pages, 0 warnings** |
| Instructor-leak grep over `site/` | ✅ executed | no instructor files in build; only benign prose mentions ("instructor's email") |
| **Teaching-package generation (32 packages)** | ✅ executed | 32 hand-authored packages under `instructor/teaching-packages/U1–U7/`; gate 10 added (16 required sections, no placeholders, title/numbering vs YAML, relative-link resolution). During authoring the gate caught: (a) its own over-strict title check (fixed), (b) 7 files with one-level-too-shallow relative links into instructor/ subfolders (fixed). Final: **PASS (0 failures), all 10 gates** |
| **Lab workbook + templates (16 labs)** | ✅ executed | 16 student briefs in `docs/labs/` + CAMPUS-MEND scenario data pack; 15 Markdown templates + 9 CSV worksheets in `docs/templates/`; 16 instructor keys + 5 machine-readable answer files in `instructor/lab-solutions/`; deterministic Monte Carlo script `tools/campus_mend_sim.py` (seed 42, 20k trials). Gate 11 added: brief existence + 9 sections + keys, and it runs `tools/check_answers.py`, which recomputes every chain (budget→baseline→EVM, CPM pass re-execution, risk scores, sprint capacity, simulation vs pinned JSON, student-file leak scan). The checker caught and forced corrections: C's free float (2→0), EAC₁ rounding (5,250,000→5,249,611), and a budget addition error (labor 3,228,800→3,225,600). Final: **PASS (0 failures), all 11 gates** |

*(This section is a running log: every row gains an actual result only after
the command has been executed in the working session.)*

## 4. Failure-handling policy

- **Gate 5 trips** after a deliberate hand-edit to a generated file → move the
  edit into the YAML or the generator, then regenerate. Never bypass.
- **Gate 6 trips** → fix the slug in YAML, never the generated link.
- **Gate 7 trips** → remove the leaked path from `docs/`; `instructor/` is
  source-of-truth-local and must stay so.
- **mkdocs --strict warnings** → fix, don't suppress; suppression rots fast.

## 5. Remaining work (post-architecture backlog)

| Item | Owner | Trigger |
|---|---|---|
| Author 32 lecture slide decks (narrative depth) | instructor | per week of delivery |
| Fill exam bank items (Q1–Q3, midterm, final) | instructor | 2 weeks before each |
| Finalize rubric wording (4 rubrics) | instructor | before L08 capstone kickoff |
| Write 62 extension case full texts | instructor / TA | rolling, 1 week ahead of each unit |
| Populate lab briefs (12) & assignment briefs (3) | instructor | per unit |
| First `mkdocs gh-deploy` + set Pages source | instructor | after first manual commit/push |
| Curriculum review after first delivery | instructor + students | end of semester |

## 6. Known limitations (disclosed)

- Weekly-schedule dates assume a 2026-09-14 Monday start; regenerating with a
  real semester start is a one-constant change (`MON` in tools/scaffold.py).
- PMBOK 8 references are explicitly marked "verify before publication."
- Assessment↔CLO coverage for CLO3 is thin (single formal component) —
  accepted for v1.0 and flagged in 05-framework §2.
- Quiz 3 timing (L26) sits late in U5; if delivery lags, move to L25.
