# 09 — Website Information Architecture

**Framework:** MkDocs Material · **Config:** `mkdocs.yml` · **URL scheme:** `https://nadeem-majeedch.github.io/Project-Management/`

## 1. Navigation tree (as configured in mkdocs.yml)

```
Home                        docs/index.md
Syllabus                    docs/syllabus/
  Course Description        course-description.md (objectives, CLOs, prerequisites)
  Detailed Syllabus         detailed-syllabus.md (generated: KA map, units, CLO chains)
  Weekly Schedule           weekly-schedule.md (generated)
  Textbooks & References    textbooks.md
  Course Policies           course-policies.md
  Delivery Methodology      delivery-methodology.md
Lectures                    docs/lectures/index.md (curriculum map)
  L01 … L32                 L<nn>-<slug>.md (flat, numbered)
Cases                       docs/cases/index.md
  CS-01 … CS-43             <id>.md (flat)
Assessments                 docs/assessments/
  Grading & Components      grading.md (incl. instructor-decisions callout)
  Assessment Strategy       assessment-strategy.md
  Course Policies           policies.md (assessment rules)
  Academic Integrity & AI   academic-integrity.md
Labs                        docs/labs/index.md
Assignments                 docs/assignments/index.md
Capstone                    docs/capstone/
  Charter & Scope           capstone-charter.md (CS + DS tracks)
  Rubric                    capstone-rubric.md
  Defense Format            defense-format.md
Resources                   docs/resources/
  Glossary                  glossary.md (42 terms incl. governance & responsible AI)
  Templates                 templates.md
  Standards Library         standards-library.md
```

Design rules:

- **Flat, numbered filenames** (`L01-…`, `CS-01`) keep lexicographic order
  stable in file browsers, URL bars, and nav.
- **Max depth 2.** Course sites fail when nav becomes a maze; every page is
  ≤ 2 clicks from Home.
- **Lecture pages self-link:** each lecture links its case anchors, the
  curriculum map, and the course description; case pages link back.
- **`templates/` needs an explicit re-include.** MkDocs ≥ 1.6 hard-codes
  `/templates/` as a default docs exclusion (`_default_exclude` in
  `mkdocs/structure/files.py`), so the student template library is published
  only because `mkdocs.yml` sets `exclude_docs: "!templates/"` (a negation
  pattern appended *after* the defaults). If the config line is removed,
  every page under `docs/templates/` silently disappears from the build while
  remaining in nav — CI's strict build plus the templates-page smoke check
  (`site/templates/index.html` must exist) guard against that.

## 2. What is deliberately NOT on the site

| Content | Location | Enforcement |
|---|---|---|
| **Full teaching packages** (32, by module) | `instructor/teaching-packages/` | outside `docs/`; gate 10 + CI leak check |
| Instructor lesson plans | `instructor/lesson-plans/` | outside `docs/`; CI fails if `site/` contains `instructor/` |
| Answer keys & case solutions | `instructor/answer-keys/` | same |
| Lab answer keys + machine-readable answers | `instructor/lab-solutions/` | outside `docs/`; gate 7 + gate 11 (answer checker) + CI leak check |
| Exam bank | `instructor/exam-bank/` | same |
| Rubric masters | `instructor/rubrics/` | same |
| Extension cases CS-44..105 | LMS distribution | never rendered by MkDocs |

## 3. Page templates

| Template | Sections |
|---|---|
| Lecture page (generated) | pagevars → auto-gen notice → H1 → at-a-glint admonition → session topics → core content → case anchors → activities → after-this-lecture → session checklist → footer include |
| Case brief (generated) | auto-gen notice → H1 → case-card admonition → scenario → task → deliverable → concepts → where-this-appears → submission note |
| Syllabus pages (hand) | prose with tables; Policies page mirrors planning/05 §4 verbatim |
| Directory pages | one table per resource class, link-first |

## 4. Theming & features in mkdocs.yml

- `palette: indigo / deep purple`, system light-dark toggle
- `features:` navigation.tabs, navigation.top, navigation.indexes,
  content.code.copy, search.highlight, search.share
- `strict: true` — warnings fail the build
- `plugins:` search; offline-safe assets (no external font CDN required at build)
- Mermaid fenced blocks render natively (Material ≥ 9)
- custom CSS: `docs/stylesheets/custom.css` (table density, case-card accent)

## 5. Publication pipeline

```
push/PR → ci.yml   → validate.py → mkdocs build --strict → artifact check (no instructor/ leak)
manual dispatch → pages.yml → mkdocs gh-deploy --force → GitHub Pages (gh-pages branch)
```

Deploy is **manual-dispatch only** for v1.0 (instructor-controlled release);
switching to push-to-main deploys is a one-line change recorded for the
future. First deploy creates `gh-pages`; Pages source must then be set to
`gh-pages` branch in repo Settings → Pages (one manual step documented in
README §5).

## 6. URL & SEO hygiene

- Canonical site_url set in mkdocs.yml; og metadata via Material defaults.
- All internal links relative; validator rejects `file://`, absolute repo
  paths, and unresolved anchors.
- Numbered slugs make shared URLs stable across content edits — only a
  lecture's *title* may change without breaking links, never its slug.
