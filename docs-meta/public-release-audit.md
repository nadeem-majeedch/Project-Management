# Public Release Audit — PM-401 Course Portal & GitHub Pages Repair

**Date:** September 21, 2026 · **Auditor:** Codebuff (automated + evidence-based)
**Scope:** root README portal, GitHub Pages 404 diagnosis and repair, workflow changes, link/content validation.
**Companion documents:** [github-pages-diagnostic-report.md](github-pages-diagnostic-report.md) · [planning/11-quality-audit.md](../planning/11-quality-audit.md)

Status legend: **VERIFIED** (evidence from an executed check), **NOT VERIFIED**
(requires actions unavailable here), **WARNING** (real but non-blocking),
**BLOCKER** (must fix before release). No PASS is asserted without evidence.

---

## 1. Findings register

| # | Area | Finding | Status | Evidence |
|---|---|---|---|---|
| F1 | README | Root README is now a complete course portal: overview table, 6 outcomes, quick navigation, full 32-lecture schedule, 7-unit module overview, labs/templates/cases/capstone, assessment table, three start-here pathways, instructor resources with visibility note, references, build/deploy/validation, contribution, integrity, license, status | **VERIFIED** | Written this session; structure inspected; 199 relative links machine-checked (below) |
| F2 | README | Every relative link in README resolves to an existing file | **VERIFIED** | Link sweep: `199 resolve OK, 0 broken` |
| F3 | README | Badge counts match reality (32 lectures, 16 labs, 105 cases, 15 templates); CI badge points at the real workflow; no fabricated badges | **VERIFIED** | Glob cross-check: 32/16/105/15 confirmed (an initial script count of 33 was a checker artifact — `lesson-footer.md` matches `L*.md` but is not a lecture; recount with `^L` filter = 32) |
| F4 | README | No unverified deployment claims: live URL appears only inside the "pending verification" notice; the deployment section explicitly states the URL "is intentionally not asserted as live" | **VERIFIED** | README text inspection |
| F5 | README | Instructor materials are labeled with an explicit public-repo visibility note; no answer-key content appears in README or site nav | **VERIFIED** | README inspection; instructor content lives only under `instructor/` (never in `docs/`) |
| F6 | Pages 404 | Root cause confirmed: `pages.yml` had **zero runs** (API: `total_count: 0`), no `site-*` tag exists (API: `[]`), triggers were dispatch/tag-only → no deployment was ever created | **VERIFIED** | Live API fetches this session; full trail in the diagnostic report |
| F7 | Pages fix | `pages.yml` now triggers on every push to `main` (plus dispatch and tags); YAML parses; step structure valid | **VERIFIED** | Local `yaml.safe_load` parse: `push: {branches: [main], tags: [site-*]}, workflow_dispatch`; no `with`-without-`uses` steps |
| F8 | Site build | Strict MkDocs build exits 0 with zero `INFO`/`WARNING` diagnostics (two real defects fixed during audit, see F11/F12) | **VERIFIED** | `mkdocs build --strict` → exit 0; grep for diagnostics → empty |
| F9 | Site links | Built-site link check: all internal href/src resolve, no root-absolute paths outside 404.html, no filesystem leaks | **VERIFIED** | `tools/check_links.py` → `LINK CHECK: PASS` |
| F10 | Calendar deploy-readiness | Calendar lecture/lab links now emit real `.html` hrefs in built HTML (e.g., `href="../lectures/L01-01-why-projects-fail.html"`) — previously extensionless, which would 404 on static hosting | **VERIFIED** | `grep` on `site/calendar/index.html` after regeneration + rebuild |
| F11 | Defect fixed | `tools/calendar.py` `rel_posix()` stripped `.md`, producing extensionless links MkDocs left as-is; fixed to preserve `.md`; lab-link consumer de-duplicated (`.md.md` regression caught and fixed) | **VERIFIED** | Before/after greps on generated files; strict build exit restored to 0 |
| F12 | Defect fixed | `docs/faq.md` linked a nonexistent `#prerequisites` anchor; corrected to `#eligibility-prerequisites` | **VERIFIED** | Strict build flagged it; heading list inspected; rebuild clean |
| F13 | Workflows | Both workflow YAMLs parse; `ci.yml` step structure valid (this class of defect was previously fixed after a GitHub "Invalid workflow file" failure; `audit_repo.py` E1 now guards it) | **VERIFIED** | Parse + step-structure check → OK for both files |
| F14 | Secrets/placeholders | Secret-pattern scan clean; no TODO/placeholder links in README or site | **VERIFIED** | `tools/audit_repo.py` E2/E3 → clean |
| F15 | Course structure | 32 lectures / 16 weeks / 7 units / CLO mapping / assessment weights = 100 | **VERIFIED** | `tools/validate.py` gates 1–15 → `PASS (0 failures)` |
| F16 | Deployment | **The website is NOT live.** The live URL still returns 404 at audit time. Deployment requires: owner commit/push → Settings→Pages→Source=GitHub Actions (if not already set) → successful `pages` run. None of these have occurred yet | **NOT VERIFIED** | Live fetch of `https://nadeem-majeedch.github.io/Project-Management/` → 404 (fetched this session); no local ability to push or change repo settings |
| F17 | Pages settings | Repository **Settings → Pages → Source: “GitHub Actions”** — required by `actions/deploy-pages`, not observable or settable from the clone | **NOT VERIFIED** | Requires repo-admin web UI |
| F18 | Actions runtime | The new push-triggered `pages.yml` has never executed (it cannot, until pushed) | **NOT VERIFIED** | API: zero runs for the workflow |
| F19 | Repository visibility | Repo is public (API: `"private": false`) — course is publicly accessible as a repository right now, independent of Pages | **VERIFIED** | Live API fetch |
| F20 | Workflow auto-deploy behavior | Once pushed with Settings configured, every push to `main` deploys — instructor should be aware commits (e.g., exam content) publish immediately | **WARNING** | By-design consequence of F7; see advisory below |

**Summary: 15 VERIFIED · 3 NOT VERIFIED · 1 WARNING · 0 BLOCKERS.**

## 2. Advisory (F20)

The workflow now deploys on every push to `main`. All site content is
student-safe, but the instructor should remember that anything committed to
`main` — including future edits — publishes to the public site on push. If a
staging style is preferred, revert the `push: branches: [main]` trigger in
`pages.yml` to dispatch/tag-only (the original design), or keep sensitive
drafts out of `main`.

## 3. Files changed for this release

| File | Change |
|---|---|
| `README.md` | Rewritten as full course portal (modified) |
| `.github/workflows/pages.yml` | Added `push: branches: [main]` trigger; comments updated (modified) |
| `tools/calendar.py` | `rel_posix()` keeps `.md`; lab link consumer fixed (modified) |
| `docs/calendar/index.md`, `printable.md`, `schedule.csv` | Regenerated with `.md` links (modified, generated outputs) |
| `docs/faq.md` | Anchor fix `#prerequisites` → `#eligibility-prerequisites` (modified) |
| `docs-meta/github-pages-diagnostic-report.md` | Created |
| `docs-meta/public-release-audit.md` | Created (this file) |

Nothing deleted. Nothing committed or pushed.

## 4. Manual deployment checklist (owner)

- [ ] Review the diff of this release (7 files above)
- [ ] Commit and push to `main`
- [ ] GitHub **Settings → Pages → Build and deployment → Source: “GitHub Actions”** (skip if already set)
- [ ] Open **Actions → pages** and confirm the run goes green (it now triggers automatically on the push; *Run workflow* also available)
- [ ] Open `https://nadeem-majeedch.github.io/Project-Management/` and verify the home page renders (expect 200)
- [ ] Spot-check: Calendar page lecture links resolve; Templates page reachable; search returns results
- [ ] After a verified 200, update the README "pending verification" notice to state the verified live URL with the date of verification

## 5. Final release status

**VERIFIED LOCALLY, DEPLOYMENT PENDING** — all locally testable checks pass
with evidence; the 404's root cause is documented and structurally repaired;
the deployment itself cannot be verified without the owner's push and Pages
setting, and is explicitly not claimed as live.
