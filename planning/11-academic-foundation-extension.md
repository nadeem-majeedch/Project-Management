# 11 — Academic Foundation Extension (Prompt 1)

**Scope:** this document records what Prompt 1 added on top of the Prompt-0
architecture, what changed structurally, and where instructor decisions are
marked. Nothing from Prompt 0 was replaced; only additive sharpening occurred.

## 1. What changed structurally

| Artifact | Change |
|---|---|
| `planning/course-data.yaml` | CLO1/CLO2/CLO4/CLO5 statements sharpened to measurable verbs with observable evidence; CLO5 weighted to Apply; added `knowledge_areas:` map linking PMBOK/ISO knowledge areas → CLOs → lectures |
| `tools/scaffold.py` | now also generates `docs/syllabus/detailed-syllabus.md` (knowledge-area × lecture map with descriptions) |
| `tools/validate.py` | new **gate 9** — foundation consistency (see §4) |
| `docs/syllabus/course-description.md` | added measurable Course Objectives (CO1–CO4), detailed eligibility & prerequisites, Data Science track note, pointers to new foundation pages |
| `docs/syllabus/detailed-syllabus.md` | **new** — knowledge-area map, 7-unit prose, per-CLO teaching+assessment chain |
| `docs/syllabus/textbooks.md` | **new** — required/recommended/supplementary references with edition discipline |
| `docs/syllabus/course-policies.md` | **new** — attendance, communication, workload, missed work, devices, recorded lectures, audits, expectations (published complement to `assessments/policies.md` which stays assessment-only) |
| `docs/syllabus/delivery-methodology.md` | **new** — session anatomy, method mix, DS/CS example threading, team model, accessibility |
| `docs/assessments/grading.md` | added **Instructor decisions** box (unspecified values flagged, not silently chosen) |
| `docs/assessments/assessment-strategy.md` | **new** — why 8 components, constructive alignment, workload table, CLO evidence map |
| `docs/assessments/academic-integrity.md` | **new** — integrity commitments + 5-clause responsible-AI policy with disclosure template |
| `docs/resources/glossary.md` | 27 → 42 terms (added governance & responsible-AI terms incl. data governance, data steward, model card, PICT, governance gate) |
| `docs/capstone/capstone-charter.md` | added **two equivalent tracks** — Software PM and Data Science PM (DS uses standard CRISP-DM reference with course-adapted execution) |
| `docs/index.md` | landing page now surfaces the full academic foundation |
| `mkdocs.yml` | nav extended (Syllabus 6 entries, Assessments 5, capstone track anchors) |
| `planning/07`, `planning/09` | inventory + IA updated for all new pages |

## 2. Measurable CLOs (v1.1 — the assessment-design contract)

Each CLO now names condition, verb, object, and observable evidence.

| CLO | Measurable statement (condensed — canonical in YAML) | Bloom | Evidence |
|---|---|---|---|
| CLO1 | **Given a PMBOK 7 domain map**, classify PM principles/domains and life-cycle models; **given a project vignette**, justify a predictive/adaptive/hybrid choice with ≥ 3 criteria | Understand | quiz items, midterm MCQ/short |
| CLO2 | **Given requirements**, build a WBS (100% rule) with PERT estimates and a CPM network (float/critical path) and produce a levelling, time-feasible Gantt | Apply | A2 artifacts, lab checklists, midterm |
| CLO3 | **Given activity costs**, develop a bottom-up budget + S-curve and a quality/data-quality plan (≥ 4 metrics and ≥ 8 enforceable rules); **given PV/EV/AC**, compute EVM set correctly | Apply | midterm problems; case analyses; capstone budget |
| CLO4 | **Given a scenario**, identify ≥ 18 risks in cause-risk-effect form, quantify ≥ 1 via EMV/simulation, propose owned+triggered responses; **given PV/EV/AC**, diagnose and recommend recovery | Analyze | A3/A4 artifacts, capstone checkpoint |
| CLO5 | **Given a delivery context**, operate Scrum/Kanban/hybrid flow: sprint plan w/ goal+capacity, WIP limits w/ flow metrics, hypothesis-driven data backlog, team agreement, negotiation/BATNA prep | Apply | lab artifacts, case portfolio, capstone process evidence |
| CLO6 | **Given a project brief**, design a complete PM plan (all baselines + risk + communication + data governance) and defend trade-offs in Q&A, integrating ethics, sustainability, AI-use norms | Create | capstone plan + defense vs rubric |

## 3. Knowledge-area coverage map (generated into detailed-syllabus)

Ten areas (predictive+agile+hybrid methods; initiation & governance; scope;
schedule; cost; quality; resources; risk; communications & stakeholders;
procurement; change; closure; leadership & ethics; data governance &
responsible AI) each map to CLOs and the lectures that carry them — verified
by validator gate 9 (every area touches ≥ 1 lecture, every lecture ≥ 1 area).

## 4. Validator gate 9 — foundation consistency

Gate 9 executes on every `tools/validate.py` run:

1. CLO statements are measurable (Bloom verb family present in statement).
2. Σ assessment weights = 100.
3. Every CLO has ≥ 2 assessment components **or** a documented practice note (the CLO3 case is handled this way, explicitly, not silently).
4. Every knowledge area maps to ≥ 1 lecture; every lecture ≥ 1 area.
5. Every lecture = 1 unit; every CLO has ≥ 1 lecture; workload fields consistent: 32 × 2 = 64 h.
6. Generated-file hand-edit detection (gate 5, unchanged).

## 5. Instructor decisions (explicitly marked, not chosen)

Where Prompt 1's requirements said "clearly marked instructor decisions where
values are not specified," the published grading page now carries a callout
listing the values the instructor must set before week 1, e.g.:

- rubric **level-to-point conversion** (4-point → % mapping)
- pass threshold besides midterm ≥ 40%
- appeals deadline & second-referee policy
- participation grade (none in v1.1)
- lab grade ceiling (pass/refine as **ungraded completion gates** in v1.1)

These are also tracked in `planning/10-generation-and-validation-plan.md` §5.

## 6. Sources (no invented citations)

All references resolve to published artifacts — see
`docs/syllabus/textbooks.md` for the annotated list with role-per-item:

- PMI, PMBOK Guide 7th ed. (2021) and 6th ed. (2017)
- PMI, Code of Ethics and Professional Conduct
- PMI, PMP Examination Content Outline (2021)
- ISO 21502:2020; ISO 31000:2018
- Schwaber & Sutherland, Scrum Guide (2020)
- Fountain, *The Pipeline: A Picture of Homebrew Production* (2020, self-published) — data-project life-cycle reference; access note marked "confirm details before citing"
- Fowler, "The New Methodology" (martinfowler.com) — hybrid/scaled-methods context; revision date flagged for the reader to verify at citation time
- Womack & Jones, *Lean Thinking* (1996) — flow/WIP foundations for Kanban

Citation format required in coursework: body. (year). *title* (edition). publisher.

## 7. Compliance matrix (Prompt 1 deliverable → artifact)

| # | Required item | Primary artifact(s) |
|---|---|---|
| 1 | Title & description | `docs/syllabus/course-description.md` |
| 2 | Course objectives | same (CO1–CO4) |
| 3 | Prerequisites | same |
| 4 | Detailed syllabus | `docs/syllabus/detailed-syllabus.md` (generated) |
| 5 | 5–8 measurable CLOs | course-data.yaml `clos` (6, sharpened) |
| 6 | CLO-to-lecture mapping | `planning/04-clo-mapping.md` (generated) + detailed-syllabus |
| 7 | CLO-to-assessment mapping | `docs/assessments/grading.md` + `assessment-strategy.md` |
| 8 | Weekly schedule | `docs/syllabus/weekly-schedule.md` (generated) |
| 9 | Assessment strategy | `docs/assessments/assessment-strategy.md` |
| 10 | Grading scheme + instructor decisions | `docs/assessments/grading.md` |
| 11 | Textbooks & references | `docs/syllabus/textbooks.md` |
| 12 | Integrity & responsible AI | `docs/assessments/academic-integrity.md` |
| 13 | Glossary | `docs/resources/glossary.md` (42 terms) |
| 14 | Policies & expectations | `docs/syllabus/course-policies.md` |
| 15 | Delivery methodology | `docs/syllabus/delivery-methodology.md` |
| 16 | Project & capstone requirements | `docs/capstone/*` + DS/CS tracks |
