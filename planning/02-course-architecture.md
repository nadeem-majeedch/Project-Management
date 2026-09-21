# 02 — Course Architecture

**Course:** PM-401 Project Management · 7th-semester BS Computer Science & BS Data Science
**Instructor:** Dr. Muhammad Nadeem Majeed · 16 weeks · 32 lectures × 2 h · 64 contact hours

## 1. Design principles

1. **Single source of truth.** All schedules, CLO maps, and lecture skeletons derive from two YAML files (`planning/course-data.yaml`, `planning/case-catalog.yaml`) via `tools/scaffold.py`. Hand-editing generated files is prohibited and detected by the validator.
2. **Standards-anchored, not standards-bound.** PMBOK Guide 7 (PMI, 2021) supplies the principle/domain vocabulary; PMBOK 6 (PMI, 2017) is retained deliberately for the 49-process and ITTO vocabulary that certification bodies and interviewers still use. ISO 21502:2020 and ISO 31000:2018 anchor governance and risk. Scrum Guide 2020 anchors adaptive delivery. Where PMBOK 8 is referenced, the reference is marked "verify before publication" because its public documentation is still stabilizing.
3. **Case-driven progression.** 105 cases climb five levels (drill → strategic). Every lecture has at least one anchor case; every case names concepts, a deliverable, and a seed project.
4. **Bloom-honest outcomes.** CLOs start at Understand and terminate at Create; the CLO×lecture matrix records the level each lecture actually targets, not aspirational verbs.
5. **Student/instructor separation.** `docs/` is the published site. `instructor/` (lesson plans, answer keys, exam bank, rubrics) is excluded from MkDocs and guarded by a CI check that fails the build if it leaks into `site/`.
6. **Regeneration, not drift.** `tools/validate.py` fails on hand-edits to generated files, broken cross-links, CLO/assessment inconsistencies, and unpublished-directory leaks.

## 2. Repository map

```
Project-Management/
├── docs/                        # PUBLISHED course site (MkDocs root)
│   ├── index.md                 # landing page
│   ├── syllabus/                # course description, schedule, policies
│   ├── lectures/                # 32 pages + curriculum map (generated)
│   ├── cases/                   # 43 case briefs + directory (generated)
│   ├── assessments/             # quiz/assignment specs, grading, integrity
│   ├── labs/                    # 12 hands-on lab briefs (skeleton)
│   ├── assignments/             # 3 assignment briefs (skeleton)
│   ├── capstone/                # capstone charter, rubric, defense format
│   ├── resources/               # glossary, templates, standards library
│   └── stylesheets/             # custom CSS
├── instructor/                  # NEVER published (validator-enforced)
│   ├── teaching-packages/       # 32 full teaching packages by module (U1–U7)
│   ├── lesson-plans/            # 32 generated 2-hour timing plans
│   ├── answer-keys/             # case index + facilitation notes
│   ├── lab-solutions/           # 16 lab answer keys + machine-readable answers
│   ├── exam-bank/               # quiz/midterm/final item shells
│   └── rubrics/                 # case-portfolio and capstone rubrics
├── planning/                    # this architecture dossier
├── tools/                       # scaffold.py (generator), validate.py (gates), check_answers.py
├── .github/workflows/           # ci.yml (validate+build), pages.yml (deploy)
├── mkdocs.yml                   # site configuration
└── requirements.txt             # pinned dependencies
```

## 3. Seven units across sixteen weeks

| Unit | Title | Weeks | Lectures | spine |
|---|---|---|---|---|
| U1 | Foundations & Strategy | 1–2 | 1–4 | why PM, portfolio, PMBOK 7, roles |
| U2 | Life Cycles & Initiating | 3–4 | 5–8 | life cycles, charter, stakeholders, tailoring |
| U3 | Planning the Work | 5–7 | 9–14 | scope/WBS, estimation, CPM/PERT, cost, quality |
| U4 | Risk, Uncertainty & Control | 8–10 | 15–20 | risk, quant risk, responses, procurement, EVM, control |
| U5 | Adaptive Delivery & Teams | 11–13 | 21–26 | Scrum, Kanban, data-ML agile, scaling, teams, communication |
| U6 | Integration, Ethics & Closing | 14–15 | 27–30 | master plan, ethics, benefits, closure |
| U7 | Synthesis & Capstone | 16 | 31–32 | AI-assisted PM, capstone defense |

The unit order follows the project life cycle so that each unit's assessment feeds the next: scoping (U3) produces artifacts the risk unit (U4) consumes; the capstone (U7) assembles everything built since U2.

## 4. Standards & source register

| Standard / source | Use in course |
|---|---|
| PMBOK Guide 7th ed. (PMI, 2021) | 12 principles, 8 performance domains (L03 backbone) |
| PMBOK Guide 6th ed. (PMI, 2017) | process/ITTO vocabulary (L03, L09–L20 terminology) |
| ISO 21502:2020 | governance vocabulary (L02, L28) |
| ISO 31000:2018 | risk process (L15–L17 backbone) |
| Agile Manifesto (2001); Scrum Guide 2020 | L21–L24 backbone |
| PMI Code of Ethics & Professional Conduct | L28 backbone |
| PMI Talent Triangle | L04 competency framing |

No statistics, findings, or citations are asserted in generated skeletons; content-bearing pages must cite from this register or better, and the validator flags unsupported superlatives.

## 5. Tooling decisions

| Concern | Choice | Why |
|---|---|---|
| Site | MkDocs Material | see 01-report §5 |
| Data | YAML (pyyaml) | reviewable diffs; no database |
| Generator/validator | Python stdlib + pyyaml | runs on CI without extra services |
| Diagrams | Mermaid fenced blocks | rendered natively by Material |
| CI | GitHub Actions | repo-native; free tier sufficient |
