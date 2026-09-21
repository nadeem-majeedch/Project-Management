# Project Management — PM-401

A complete, open course site for **Project Management (PM-401)**, taught to
7th-semester **BS Computer Science** and **BS Data Science** students by
**Dr. Muhammad Nadeem Majeed**.

- **16 weeks · 32 lectures × 2 h · 64 contact hours**
- **105 progressive case studies** (43 anchored in class), 12 labs, 3 assignments, capstone defense
- Anchored to **PMBOK 7 (PMI, 2021)**, **ISO 21502:2020**, **ISO 31000:2018**, **Scrum Guide 2020**
- Published with **MkDocs Material** on **GitHub Pages**

## Repository layout

| Path | Contents |
|---|---|
| `docs/` | the published course site (lectures, cases, syllabus, assessments, capstone, resources) |
| `instructor/` | instructor-only materials — lesson plans, answer keys, exam bank, rubrics — **never published** |
| `planning/` | course architecture dossier: data files + 10 design documents |
| `tools/` | `scaffold.py` (generator) · `validate.py` (8 architecture gates) |
| `.github/workflows/` | `ci.yml` (validate + strict build) · `pages.yml` (manual Pages deploy) |

## How the course is maintained

All course structure lives in two data files:

- `planning/course-data.yaml` — 32 lectures, CLOs, units, assessment plan
- `planning/case-catalog.yaml` — 105 cases with levels, domains, anchors

```bash
# edit the YAML, then regenerate everything downstream
python tools/scaffold.py

# run the 8 architecture gates (structure, links, CLO closure, leak check…)
python tools/validate.py
```

Generated files carry an `AUTO-GENERATED` notice; hand-edits to them are
detected and rejected by the validator. Edit the YAML, never the output.

## Local setup

```bash
python -m venv .venv
.venv/Scripts/pip install -r requirements.txt    # Windows
# source .venv/bin/activate && pip install -r requirements.txt   # macOS/Linux

python tools/scaffold.py
python tools/validate.py
python -m mkdocs serve            # http://localhost:8000
```

## Local build and full validation

```bash
python tools/scaffold.py            # regenerate lectures/cases/schedule from planning YAML
python tools/calendar.py            # regenerate semester calendar (web/printable/CSV/ICS)
python tools/validate.py            # content gates 1-15 (15 = calendar)
python tools/check_cases.py         # 105 cases: 380 numeric assertions
python tools/check_answers.py       # lab answer-key arithmetic chains
python tools/check_slides.py        # 32 slide decks: structure + numbers
python tools/build_slides.py        # rebuild instructor/slides/build/ HTML
python -m mkdocs build --strict --site-dir site
python tools/check_links.py         # every built href/src resolves; no absolute paths
```

### Semester calendar (one-click)

The calendar is generated from two files — never hand-edit the outputs:

- `planning/course-data.yaml` — **fixed course content** (32 lectures, CLOs,
  activities, assessment plan)
- `planning/schedule-config.yaml` — **instructor-owned dates**:
  `configured: true/false`, `semester_start`, `teaching_days`, `holidays`,
  `term_label`

While `configured: false`, the site shows relative weeks (Week 1–16) and
claims **no** institutional dates; no `.ics` file is emitted. Set
`configured: true` and the fields above, then run
`python tools/calendar.py` — real dates appear on the
[calendar page](docs/calendar/index.md), the weekly schedule, a
[printable view](docs/calendar/printable.md), `schedule.csv`, and a
valid `schedule.ics` importable into Outlook/Google Calendar. Lectures
falling on holidays slide to the next teaching day automatically; a start
date that is not a teaching day fails validation instead of guessing.

`tools/check_links.py` needs a fresh build (it reads `site/`). A green run
means every internal link resolves, no root-absolute paths exist outside the
404 page, and no local filesystem paths leaked into the output.

## Publishing to GitHub Pages

The site deploys with the **GitHub Actions artifact method** (no `gh-pages`
branch): `.github/workflows/pages.yml` validates all gates, builds strictly,
and uploads the `site/` artifact with `actions/upload-pages-artifact` →
`actions/deploy-pages`.

### One-time repository setup (manual)

1. Push `main` with these files.
2. GitHub **Settings → Pages → Build and deployment → Source: select
   “GitHub Actions”** (not “Deploy from a branch”). Without this the first
   deploy run fails with a 404 on the Pages API.
3. Actions → **pages** → *Run workflow* (manual dispatch by design; to
   auto-deploy on every push to `main`, add `branches: [main]` under the
   workflow's `push:` trigger).
4. Site: <https://nadeem-majeedch.github.io/Project-Management/>

The `site_url` in `mkdocs.yml` already points at the project subpath, so all
asset links are emitted relative and work under
`/Project-Management/` without further configuration.

## License

MIT for the code and configuration. Course content © Dr. Muhammad Nadeem
Majeed — see [LICENSE](LICENSE).
