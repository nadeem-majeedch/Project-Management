# Project Management — PM-401

[![Course](https://img.shields.io/badge/course-PM--401%20Project%20Management-indigo)](docs/syllabus/course-description.md)
[![Level](https://img.shields.io/badge/level-Semester%207%20%C2%B7%20BS%20CS%20%2F%20BS%20DS-blue)](docs/syllabus/course-description.md)
[![Lectures](https://img.shields.io/badge/lectures-32%20%C3%97%202h%20%C2%B7%2064%20hours-indigo)](docs/lectures/index.md)
[![Cases](https://img.shields.io/badge/case%20studies-105%20progressive-purple)](docs/cases/index.md)
[![Labs](https://img.shields.io/badge/hands--on%20labs-16-teal)](docs/labs/index.md)
[![CI](https://github.com/nadeem-majeedch/Project-Management/actions/workflows/ci.yml/badge.svg)](https://github.com/nadeem-majeedch/Project-Management/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A complete, open university course on **Project Management for software and
data science projects**, taught to 7th-semester **BS Computer Science** and
**BS Data Science** students at the **Department of Data Science, Faculty of
Computing & Information Technology, University of the Punjab, Lahore**.

Everything a student, independent learner, or fellow instructor needs is in
this repository: 32 fully prepared lectures, 16 graded labs with a shared
scenario data pack, 105 progressive case studies with machine-verified
arithmetic, a complete assessment system, a team capstone with defense
rubrics, and the tooling that keeps all of it internally consistent.

> **GitHub Pages deployment: pending verification.**
> The Pages workflow and repository settings are configured as documented in
> the [deployment guide](#github-pages-deployment); the live URL will be
> listed here once a successful deployment is verified. Until then, every
> page below is readable directly in this repository.

---

## Course overview

| Field | Value |
|---|---|
| **Code & title** | PM-401 — Project Management |
| **Programs** | BS Computer Science · BS Data Science |
| **Semester** | 7 (senior undergraduate) |
| **Credit hours** | 3 + 1 |
| **Structure** | 16 weeks · 32 lectures × 2 h · 64 contact hours |
| **Instructor** | **Dr. Muhammad Nadeem Majeed**, Associate Professor, Department of Data Science, FCIT, University of the Punjab, Lahore |
| **Standards** | PMBOK Guide 7th ed. (PMI, 2021) · ISO 21502:2020 · ISO 31000:2018 · Scrum Guide 2020 |
| **Assessment** | 8 components, weights summing to 100%, capstone defense included |

**What makes this course different:** every technique is exercised on both
**software projects** (web platforms, migrations, regulated systems) and
**data/ML projects** (model risk gates, data-quality rules, cloud-cost
control, experiment-driven backlogs). Quantitative methods — PERT, CPM,
Monte Carlo, earned value — are taught with worked, machine-verified
numbers; leadership, negotiation, governance, and ethics are taught with
role-plays and dilemma instruments rather than recycled slides.

## Learning outcomes

Graduates of this course can (full, measurable statements in the
[CLO reference](docs/syllabus/clos.md)):

1. **Classify and justify** — PMBOK 7 principles, performance domains, and life-cycle choices against explicit criteria (CLO1)
2. **Plan quantitatively** — scope statements, 100%-rule WBS, PERT estimates, CPM networks with correct float, levelled Gantt baselines (CLO2)
3. **Cost and control** — bottom-up budgets with S-curves, quality/data-quality plans, and the full earned-value set (CV, SV, CPI, SPI, EAC, TCPI) (CLO3)
4. **Manage uncertainty** — 18+ normalized risks per scenario, EMV and Monte Carlo quantification, owned and triggered responses aligned to ISO 31000 (CLO4)
5. **Deliver adaptively** — Scrum events, Kanban WIP limits via Little's Law, hypothesis-driven data/ML backlogs, BATNA-based negotiation (CLO5)
6. **Integrate and defend** — a complete, internally consistent project management plan, defended orally with ethics, governance, sustainability, and responsible-AI positions (CLO6)

## Quick navigation

| I want to… | Go to |
|---|---|
| Understand the course | [Course description](docs/syllabus/course-description.md) · [Learning outcomes](docs/syllabus/clos.md) |
| See the semester | [Detailed syllabus](docs/syllabus/detailed-syllabus.md) · [16-week schedule](docs/syllabus/weekly-schedule.md) · [Calendar](docs/calendar/index.md) |
| Study the lectures | [All 32 lectures](docs/lectures/index.md) (index below) |
| Practice | [16 labs](docs/labs/index.md) · [15 templates](docs/templates/index.md) · [105 cases](docs/cases/index.md) |
| Take assessments | [Assessments](docs/assessments/index.md) · [Assignments](docs/assignments/index.md) · [Capstone](docs/capstone/index.md) |
| Look things up | [Glossary](docs/resources/glossary.md) · [Standards library](docs/resources/standards-library.md) · [Downloads](docs/downloads.md) · [FAQ](docs/faq.md) |
| Teach this course | [Instructor resources](#instructor-resources) below |

---

## The 32-lecture schedule

Seven units across 16 weeks; each lecture is a self-contained page with
objectives, worked examples (where calculations apply), activities,
misconceptions, and references. Case codes link to the corresponding case
briefs.

| Wk | Unit | Lecture | Title | CLO | In class |
|---|---|---|---|---|---|
| 1 | U1 | [L01](docs/lectures/L01-01-why-projects-fail.md) | Why Projects Fail: The Case for Project Management | CLO1 | [CS-01](docs/cases/CS-01.md), [CS-02](docs/cases/CS-02.md) |
| 1 | U1 | [L02](docs/lectures/L02-02-strategy-portfolio.md) | Strategy, Portfolios, Programs & Projects | CLO1 | [CS-03](docs/cases/CS-03.md) |
| 2 | U1 | [L03](docs/lectures/L03-03-pmbok7-principles-domains.md) | PMBOK Guide 7: Principles & Performance Domains | CLO1 | [CS-04](docs/cases/CS-04.md) |
| 2 | U1 | [L04](docs/lectures/L04-04-roles-profession.md) | Roles, Competencies & the PM Profession | CLO1 | [CS-05](docs/cases/CS-05.md) · **Quiz 1** |
| 3 | U2 | [L05](docs/lectures/L05-05-lifecycles.md) | Life Cycles: Predictive, Adaptive, Hybrid | CLO1, CLO5 | [CS-06](docs/cases/CS-06.md), [CS-07](docs/cases/CS-07.md) |
| 3 | U2 | [L06](docs/lectures/L06-06-charter.md) | Project Charter & Business Case | CLO1, CLO2 | [CS-08](docs/cases/CS-08.md) |
| 4 | U2 | [L07](docs/lectures/L07-07-stakeholders.md) | Stakeholder Identification & Analysis | CLO5 | [CS-09](docs/cases/CS-09.md), [CS-10](docs/cases/CS-10.md) |
| 4 | U2 | [L08](docs/lectures/L08-08-tailoring.md) | Tailoring for Software & Data Projects | CLO1, CLO5 | [CS-11](docs/cases/CS-11.md) · **capstone teams form** |
| 5 | U3 | [L09](docs/lectures/L09-09-scope-wbs.md) | Scope & Work Breakdown Structure | CLO2 | [CS-12](docs/cases/CS-12.md), [CS-13](docs/cases/CS-13.md) |
| 5 | U3 | [L10](docs/lectures/L10-10-estimation.md) | Estimation: Size, Effort, Duration | CLO2 | [CS-14](docs/cases/CS-14.md) |
| 6 | U3 | [L11](docs/lectures/L11-11-cpm-pert.md) | Network Logic, CPM & PERT | CLO2 | [CS-15](docs/cases/CS-15.md) |
| 6 | U3 | [L12](docs/lectures/L12-12-schedule-tools.md) | Schedules, Gantt Charts & Resource Levelling | CLO2 | [CS-16](docs/cases/CS-16.md) · **Quiz 2** |
| 7 | U3 | [L13](docs/lectures/L13-13-cost-budget.md) | Cost Estimating & Budgeting | CLO3 | [CS-17](docs/cases/CS-17.md) |
| 7 | U3 | [L14](docs/lectures/L14-14-quality-data-quality.md) | Quality & Data-Quality Planning | CLO3 | [CS-18](docs/cases/CS-18.md), [CS-19](docs/cases/CS-19.md) · **Assignment 1 released** |
| 8 | U4 | [L15](docs/lectures/L15-15-risk-foundations.md) | Risk Management Foundations (ISO 31000) | CLO4 | [CS-20](docs/cases/CS-20.md), [CS-21](docs/cases/CS-21.md) |
| 8 | U4 | [L16](docs/lectures/L16-16-quant-risk-simulation.md) | Quantitative Risk: PERT, Trees & Simulation | CLO4 | [CS-22](docs/cases/CS-22.md) · **Assignment 1 due** |
| 9 | U4 | [L17](docs/lectures/L17-17-risk-response.md) | Risk Responses, Issues & Reserves | CLO4 | [CS-23](docs/cases/CS-23.md) · **Assignment 2 released** |
| 9 | U4 | [L18](docs/lectures/L18-18-procurement.md) | Procurement & Vendor Management | CLO3, CLO4 | [CS-24](docs/cases/CS-24.md), [CS-25](docs/cases/CS-25.md) |
| 10 | U4 | [L19](docs/lectures/L19-19-evm.md) | Earned Value Management | CLO4 | [CS-26](docs/cases/CS-26.md) · **Assignment 2 due, A3 released** |
| 10 | U4 | [L20](docs/lectures/L20-20-monitoring-control.md) | Monitoring, Dashboards & Change Control | CLO4 | [CS-27](docs/cases/CS-27.md) · **midterm window opens** |
| 11 | U5 | [L21](docs/lectures/L21-21-scrum.md) | Scrum in Practice | CLO5 | [CS-28](docs/cases/CS-28.md), [CS-29](docs/cases/CS-29.md) · **Assignment 3 due** |
| 11 | U5 | [L22](docs/lectures/L22-22-kanban-flow.md) | Kanban, Flow & Throughput | CLO5 | [CS-30](docs/cases/CS-30.md) |
| 12 | U5 | [L23](docs/lectures/L23-23-agile-data-ml.md) | Agile for Data Science & ML Projects | CLO5 | [CS-31](docs/cases/CS-31.md), [CS-32](docs/cases/CS-32.md) |
| 12 | U5 | [L24](docs/lectures/L24-24-scaling-hybrid.md) | Scaling Frameworks & Hybrid Delivery | CLO5 | [CS-33](docs/cases/CS-33.md) |
| 13 | U5 | [L25](docs/lectures/L25-25-team-performance.md) | Team Performance & Leadership | CLO5 | [CS-34](docs/cases/CS-34.md), [CS-35](docs/cases/CS-35.md) |
| 13 | U5 | [L26](docs/lectures/L26-26-communication-negotiation.md) | Stakeholder Communication & Negotiation | CLO5 | [CS-36](docs/cases/CS-36.md), [CS-37](docs/cases/CS-37.md) · **Quiz 3** |
| 14 | U6 | [L27](docs/lectures/L27-27-master-plan.md) | The Master Project Plan: Integrating Everything | CLO6 | [CS-38](docs/cases/CS-38.md) · **capstone plan draft due** |
| 14 | U6 | [L28](docs/lectures/L28-28-ethics-governance.md) | Ethics, Governance & Professional Responsibility | CLO6 | [CS-39](docs/cases/CS-39.md) |
| 15 | U6 | [L29](docs/lectures/L29-29-sustainability-benefits.md) | Sustainability & Benefits Realization | CLO6 | [CS-40](docs/cases/CS-40.md) |
| 15 | U6 | [L30](docs/lectures/L30-30-closure-lessons.md) | Closing Projects & Lessons Learned | CLO6 | [CS-41](docs/cases/CS-41.md) |
| 16 | U7 | [L31](docs/lectures/L31-31-ai-assisted-pm.md) | AI-Assisted Project Management | CLO6 | [CS-42](docs/cases/CS-42.md) |
| 16 | U7 | [L32](docs/lectures/L32-32-capstone-synthesis.md) | Capstone Defense & Course Synthesis | CLO6 | [CS-43](docs/cases/CS-43.md) · **capstone due, final exam window** |

### Module overview (course units)

| Unit | Weeks | Lectures | Focus |
|---|---|---|---|
| **U1 — Foundations & Strategy** | 1–2 | L01–L04 | Why projects fail; portfolio thinking; PMBOK 7; roles |
| **U2 — Life Cycles & Initiating** | 3–4 | L05–L08 | Predictive/agile/hybrid; charter; stakeholders; tailoring |
| **U3 — Planning the Work** | 5–7 | L09–L14 | Scope, WBS, estimation, CPM/PERT, budget, quality |
| **U4 — Risk, Uncertainty & Control** | 8–10 | L15–L20 | ISO 31000 risk, simulation, procurement, EVM, change control |
| **U5 — Adaptive Delivery & Teams** | 11–13 | L21–L26 | Scrum, Kanban, data/ML agility, scaling, teams, negotiation |
| **U6 — Integration, Ethics & Closing** | 14–15 | L27–L30 | Master plan, ethics, sustainability, closure |
| **U7 — Synthesis & Capstone** | 16 | L31–L32 | AI-assisted PM; capstone defense |

---

## Practical learning

### Labs (16, scenario-driven)

All labs share one educational scenario — **CAMPUS-MEND**, a university
portal rebuild described in the [data pack](docs/labs/data-pack.md) — so
artifacts compound from week to week. Every calculation has an
independently checkable answer.

| Lab | Topic | Brief |
|---|---|---|
| 1 | Project charter | [lab-01](docs/labs/lab-01-charter.md) |
| 2 | Stakeholder register & power–interest grid | [lab-02](docs/labs/lab-02-stakeholders.md) |
| 3 | Requirements, scope statement & WBS | [lab-03](docs/labs/lab-03-scope-wbs.md) |
| 4 | Dependency network & critical path | [lab-04](docs/labs/lab-04-cpm-network.md) |
| 5 | WBS dictionary | [lab-05](docs/labs/lab-05-wbs-dictionary.md) |
| 6 | Gantt chart & resource allocation | [lab-06](docs/labs/lab-06-gantt-resources.md) |
| 7 | Cost baseline | [lab-07](docs/labs/lab-07-cost-baseline.md) |
| 8 | Quality management plan | [lab-08](docs/labs/lab-08-quality-plan.md) |
| 9 | Risk register | [lab-09](docs/labs/lab-09-risk-register.md) |
| 10 | Probability–impact matrix | [lab-10](docs/labs/lab-10-probability-impact.md) |
| 11 | Monte Carlo simulation | [lab-11](docs/labs/lab-11-monte-carlo.md) |
| 12 | Communication plan | [lab-12](docs/labs/lab-12-communication.md) |
| 13 | EVM project recovery | [lab-13](docs/labs/lab-13-evm-recovery.md) |
| 14 | Agile sprint planning | [lab-14](docs/labs/lab-14-agile-sprint.md) |
| 15 | Change control & recovery plan | [lab-15](docs/labs/lab-15-change-recovery.md) |
| 16 | Capstone pack assembly | [lab-16](docs/labs/lab-16-capstone-pack.md) |

### Templates (15, editable)

[Charter](docs/templates/charter-template.md) ·
[Stakeholder register](docs/templates/stakeholder-register-template.md) ·
[Scope statement](docs/templates/scope-statement-template.md) ·
[WBS](docs/templates/wbs-template.md) ·
[WBS dictionary](docs/templates/wbs-dictionary-template.md) ·
[Activity dependencies](docs/templates/activity-dependency-template.md) ·
[CPM worksheet](docs/templates/cpm-worksheet-template.md) ·
[Gantt & resources](docs/templates/gantt-resource-template.md) ·
[Cost baseline](docs/templates/cost-baseline-template.md) ·
[Quality plan](docs/templates/quality-plan-template.md) ·
[Risk register](docs/templates/risk-register-template.md) ·
[P×I matrix](docs/templates/probability-impact-template.md) ·
[Communication plan](docs/templates/communication-plan-template.md) ·
[Monitoring dashboard](docs/templates/monitoring-dashboard-template.md) ·
[Sprint planning](docs/templates/sprint-planning-template.md) —
plus [CSV versions](docs/downloads.md) of the numerical templates.

### Case studies (105, progressive)

Four difficulty bands with an index supporting filtering by level, domain,
and lecture anchor: **beginner CS-01–20**, **intermediate CS-21–45**,
**advanced CS-46–75**, **expert CS-76–105**. Forty-three cases anchor
specific lectures (see schedule above); the remainder extend practice.
Thirty-two cases carry machine-verified numerical solutions (CPM, float,
EVM, EMV, Monte Carlo, resource levelling). Start at the
[case index](docs/cases/index.md).

### Capstone

Teams build and defend a complete project management plan for a software or
data-science project: [specification](docs/capstone/specification.md) ·
[milestones](docs/capstone/milestones.md) ·
[charter & scope](docs/capstone/capstone-charter.md) ·
[rubric](docs/capstone/capstone-rubric.md) ·
[presentation rubric](docs/capstone/presentation-rubric.md) ·
[peer review](docs/capstone/peer-review.md) ·
[defense format](docs/capstone/defense-format.md).

## Assessment

| Component | Weight | What it covers |
|---|---|---|
| A1 · Quizzes (best 2 of 3) | 10% | L01–04, L09–12, L21–26 — [quiz guide](docs/assessments/quiz-guide.md) |
| A2 · Assignment 1 — Scope & Schedule | 10% | WBS, PERT, CPM, Gantt — [brief](docs/assignments/a1-scope-schedule.md) |
| A3 · Assignment 2 — Risk Register | 10% | ISO 31000-aligned register & responses — [brief](docs/assignments/a2-risk-register.md) |
| A4 · Assignment 3 — EVM Analysis | 10% | Full earned-value diagnosis — [brief](docs/assignments/a3-evm-analysis.md) |
| A5 · Midterm exam (L01–L20) | 20% | Concepts + planning math + EVM — [exam guide](docs/assessments/exam-guide.md) |
| A6 · Case portfolio | 10% | 12 written case analyses across the semester |
| A7 · Capstone project & defense | 25% | Team plan + oral defense — [spec](docs/capstone/specification.md) |
| A8 · Final exam (comprehensive) | 5% | Emphasis L21–L32 |

Grading rules, policies, and academic integrity live under
[Assessments](docs/assessments/index.md):
[grading](docs/assessments/grading.md) ·
[strategy](docs/assessments/assessment-strategy.md) ·
[policies](docs/assessments/policies.md) ·
[academic integrity & responsible AI](docs/assessments/academic-integrity.md).

---

## Start here

### Student path

1. Read the [course description](docs/syllabus/course-description.md) and [outcomes](docs/syllabus/clos.md)
2. Review the [detailed syllabus](docs/syllabus/detailed-syllabus.md) and [weekly schedule](docs/syllabus/weekly-schedule.md)
3. Open the [calendar](docs/calendar/index.md) and note assessment dates
4. Before each class, skim that week's two [lectures](docs/lectures/index.md)
5. Complete the weekly [lab](docs/labs/index.md) using the [data pack](docs/labs/data-pack.md) and [templates](docs/templates/index.md)
6. Attempt the [case studies](docs/cases/index.md) — twelve become your portfolio
7. Prepare for [quizzes, assignments, and exams](docs/assessments/index.md) using their guides
8. Build your [capstone](docs/capstone/index.md) from week 4 onward and defend it in week 16

### Instructor path (adapting this course)

1. Review the [syllabus](docs/syllabus/detailed-syllabus.md), [CLO maps](docs/syllabus/clos.md), and the [grading framework](docs/assessments/grading.md)
2. Read the [lecture delivery plan](instructor/handover/README.md) and per-lecture [teaching packages](instructor/teaching-packages/) (notes, activities, timings)
3. Prepare from the [slide decks](instructor/slides/) — build with `tools/build_slides.py`
4. Select [labs](docs/labs/index.md) and check the [answer keys](instructor/lab-solutions/) and [rubrics](instructor/rubrics/)
5. Choose [progressive cases](docs/cases/index.md); model answers in [instructor/answer-keys/cases/](instructor/answer-keys/cases/)
6. Assemble quizzes/exams from the [question bank](instructor/exam-bank/) — verify with the marking guides
7. Configure [semester dates](planning/schedule-config.yaml), regenerate the [calendar](docs/calendar/index.md), and re-run validation (below)
8. Read the [final quality audit](planning/11-quality-audit.md) and the readiness checklist in the [handover package](instructor/handover/README.md)

### Reader path (independent learners)

1. [Course description](docs/syllabus/course-description.md) — the shape of the field
2. Any lecture that interests you — each is self-contained, e.g. [EVM](docs/lectures/L19-19-evm.md), [risk](docs/lectures/L15-15-risk-foundations.md), [Scrum](docs/lectures/L21-21-scrum.md)
3. Worked numerical examples are in the lectures and the [CPM](docs/templates/cpm-worksheet-template.md)/[EVM](docs/labs/lab-13-evm-recovery.md) artifacts
4. Test yourself on the [case studies](docs/cases/index.md) — difficulty is labelled
5. Finish with the [glossary](docs/resources/glossary.md) and [references](docs/syllabus/textbooks.md)

---

## Instructor resources

All instructor materials live under [`instructor/`](instructor/README.md) —
**excluded from the published website and its search index**, but present in
this repository:

| Directory | Contents |
|---|---|
| [`teaching-packages/`](instructor/teaching-packages/) | 32 instructor-ready packages: teaching notes, definitions, worked examples, misconceptions, activities, 2-hour plans |
| [`slides/`](instructor/slides/) | 32 Marp-flavored decks + shared theme; HTML builds in [`slides/build/`](instructor/slides/build/index.html) |
| [`lesson-plans/`](instructor/lesson-plans/) | Per-lecture two-hour session plans |
| [`answer-keys/`](instructor/answer-keys/) | 105 case model answers + alternatives |
| [`lab-solutions/`](instructor/lab-solutions/) | 16 lab answer keys with verification data |
| [`exam-bank/`](instructor/exam-bank/) | Question banks per unit, midterm & final papers, marking guides |
| [`rubrics/`](instructor/rubrics/) | Assessment and capstone rubrics |
| [`handover/`](instructor/handover/README.md) | Complete instructor handover package |

> **Visibility note for adopters.** This is a public repository: anything in
> `instructor/` is readable by anyone browsing the code, even though it never
> appears on the website. GitHub repository visibility offers no reliable
> mechanism for hiding sensitive material. Keep genuinely restricted content
> (live exam papers before the exam, student records, personal data) out of
> this repository entirely, or move this repository to a private setting.

## References

Primary standards and textbooks, with full citations and how each is used:

- [Textbooks & references](docs/syllabus/textbooks.md) — PMBOK 7 (PMI, 2021), ISO 21502:2020, ISO 31000:2018, Scrum Guide 2020, and supporting texts
- [Standards library](docs/resources/standards-library.md) — mapped to lectures and domains

---

## Building and maintaining the course

### Repository layout

| Path | Contents |
|---|---|
| `docs/` | The published course site (MkDocs Material): lectures, cases, syllabus, assessments, capstone, templates, calendar |
| `instructor/` | Instructor-only materials — **never published to the website** |
| `planning/` | Architecture dossier: `course-data.yaml`, `case-catalog.yaml`, `schedule-config.yaml` + 13 design/audit documents |
| `tools/` | Generator, calendar, validators, and audit scripts (Python 3.12, standard library + MkDocs) |
| `.github/workflows/` | `ci.yml` (validation on every push) · `pages.yml` (Pages deployment) |

### Single source of truth

All course structure derives from two planning files; generated files carry
an `AUTO-GENERATED` notice and hand-edits to them are rejected by the
validator. **Edit the YAML, never the output:**

- `planning/course-data.yaml` — 32 lectures, CLOs, units, assessment plan
- `planning/case-catalog.yaml` — 105 cases with levels, domains, anchors, verified numerics
- `planning/schedule-config.yaml` — instructor-owned semester dates (`configured`, `semester_start`, `teaching_days`, `holidays`)

While dates are unconfigured, the site shows relative weeks and claims no
institutional dates; setting `configured: true` produces real dates, a
printable view, `schedule.csv`, and a valid `schedule.ics`.

### Local development

```bash
python -m venv .venv
.venv/Scripts/pip install -r requirements.txt    # Windows
# source .venv/bin/activate && pip install -r requirements.txt   # macOS/Linux

python tools/scaffold.py                          # regenerate lectures/cases/schedule from YAML
python -m mkdocs serve                            # preview at http://localhost:8000
```

### Full validation suite

```bash
python tools/scaffold.py            # regenerate from planning YAML
python tools/calendar.py            # regenerate semester calendar (web/printable/CSV/ICS)
python tools/validate.py            # architecture gates 1–15
python tools/check_cases.py         # 105 cases: 380+ numeric assertions
python tools/check_answers.py       # lab answer-key arithmetic chains
python tools/check_slides.py        # 32 slide decks: structure + numbers
python tools/build_slides.py        # rebuild instructor/slides/build/ HTML
python -m mkdocs build --strict --site-dir site
python tools/check_links.py         # every built href/src resolves; no absolute paths
python tools/audit_repo.py          # full quality audit (VERIFIED/WARNING/NOT-TESTED/BLOCKER)
```

Current status at last audit: **PASS WITH WARNINGS** — 25 verified, 1
warning, 1 not tested, 0 blockers
([audit report](planning/11-quality-audit.md), re-runnable via
`tools/audit_repo.py`).

### GitHub Pages deployment

The site deploys with the **GitHub Actions artifact method**
(`actions/configure-pages` → `actions/upload-pages-artifact` →
`actions/deploy-pages`; no `gh-pages` branch). The `pages.yml` workflow
validates all gates, builds strictly, checks that the template library and
no instructor content reach the artifact, then deploys.

**One-time repository settings (manual, not yet verifiable locally):**

1. Push `main` with these files.
2. GitHub **Settings → Pages → Build and deployment → Source: “GitHub Actions”** — without this the first deploy fails.
3. The workflow runs automatically on every push to `main` (manual dispatch and `site-*` tags also work).
4. When the run succeeds, the site appears at
   `https://nadeem-majeedch.github.io/Project-Management/` — that URL is
   intentionally **not** asserted as live anywhere in this README until a
   deployment is verified.

Diagnostic detail and the evidence trail for the original 404:
[docs-meta/github-pages-diagnostic-report.md](docs-meta/github-pages-diagnostic-report.md).

## Contributing

Corrections and improvements are welcome from students and educators:
open an issue describing the section (lecture number, case ID, lab number),
or a pull request against `main`. Content changes must keep the validation
suite green — regenerate derived files from the planning YAML rather than
editing them, and run `python tools/validate.py` before submitting.

## Academic integrity & responsible AI

Enrolled students: the [academic integrity policy](docs/assessments/academic-integrity.md)
defines collaboration boundaries, citation expectations, and the course's
AI-use rules (disclosure, verification duties, and which artifacts must
remain human-authored). The capstone requires an explicit AI-use statement.

## License

MIT for the code, configuration, and tooling — see [LICENSE](LICENSE).
Course content (lectures, cases, assessments, planning documents) ©
Dr. Muhammad Nadeem Majeed, published for students and educators; reuse
with attribution.

## Course status & maintenance

- **Content complete:** 32/32 lectures, 16/16 labs, 105/105 cases, full assessment system — last full audit [planning/11-quality-audit.md](planning/11-quality-audit.md)
- **Maintenance model:** edit planning YAML → `python tools/scaffold.py` → validators; CI (`ci.yml`) re-runs all gates on every push
- **Semester dates:** configured by the instructor in `planning/schedule-config.yaml` (currently unconfigured — the site shows relative weeks only)
- **Known open items:** tracked in the [audit report](planning/11-quality-audit.md) findings register (e.g., a flagged question-bank variant for instructor re-computation, the L19 rounding footnote)
