# GitHub Pages 404 — Diagnostic Report

**Date:** September 21, 2026
**Method:** live GitHub REST API fetches, live page fetch, local inspection of workflows and configuration; no guessing.
**Symptom:** `https://nadeem-majeedch.github.io/Project-Management/` returns 404.

---

## 1. Observed configuration (evidence)

| # | Observation | Evidence source |
|---|---|---|
| O1 | Repository is **public** (`"private": false`), so Pages availability is not a billing/visibility issue | GitHub REST API `GET /repos/nadeem-majeedch/Project-Management` (fetched live this session) |
| O2 | Default branch is `main`, single branch, no `gh-pages` branch exists | API `GET /branches` → only `main`; API `GET /tags` → `[]` |
| O3 | Local `main` matches remote HEAD exactly (`30f348879f…`, "workflow upadate") — every workflow fix is already pushed | API `GET /commits?per_page=3` vs `git rev-parse HEAD` |
| O4 | **`pages.yml` has never executed.** `GET /actions/workflows/pages.yml/runs` → `{"total_count": 0, "workflow_runs": []}` | API (live) |
| O5 | The only trigger able to start `pages.yml` was `workflow_dispatch` or a `site-*` tag. No tag has ever existed (O2), and no manual dispatch was ever recorded (O4) | Local `pages.yml` inspection + API evidence |
| O6 | The deployment pipeline itself is sound: on `main` pushes, `ci.yml` ran three times, most recently run #3 (`35559017442`) with **conclusion: success** — gates, arithmetic checks, strict build, link check all pass on GitHub's own runner | API `GET /actions/runs?per_page=10` (live) |
| O7 | Site configuration is subpath-correct: `site_url: https://nadeem-majeedch.github.io/Project-Management/` in `mkdocs.yml`; `configure-pages@v5` → `upload-pages-artifact@v3 (path: site)` → `deploy-pages@v4`; correct `permissions` and `concurrency` | Local inspection of `mkdocs.yml`, `pages.yml` |
| O8 | The built site has a real `index.html` and resolves links relative to the subpath (verified repeatedly by `tools/check_links.py` over 21k+ href/src attributes; `404.html` legitimately uses `site_url`-prefixed links) | Local build + link checker |

## 2. Cause classification

| Cause hypothesis | Verdict | Evidence |
|---|---|---|
| Framework/base-path misconfiguration | **Ruled out** | O7, O8 — MkDocs Material, correct `site_url`, relative assets, subpath validated |
| Wrong artifact directory uploaded | **Ruled out** | O7 — `upload-pages-artifact` path is `site`, which matches `--site-dir site` |
| Invalid workflow / bad YAML | **Ruled out** | O6 — CI succeeds on GitHub's runner; both workflows parse; step structure validated |
| Missing `index.html` | **Ruled out** | O8 |
| Missing permissions / concurrency misconfig | **Ruled out** | O7 — `pages: write`, `id-token: write`, `environment: github-pages` present |
| **Site never deployed — deployment never triggered** | **CONFIRMED** | O4 + O5: zero `pages.yml` runs, no tag, no dispatch; 404 = "no deployment has ever been created" |

**Root cause:** the Pages workflow was triggerable only by manual dispatch or
a `site-*` tag; neither ever occurred, so no deployment was ever created.
The website pipeline was healthy and unexecuted — a trigger gap, not a
build defect.

## 3. Causes that cannot be verified locally

| Item | Why not verifiable here | Status |
|---|---|---|
| Repository **Settings → Pages → Source** | No API access to repo settings without an admin token; not observable in the clone | **NOT VERIFIED** — must be checked by the owner |
| Whether the workflow's Pages environment (`github-pages`) needs first-run approval | Applies only to fork scenarios; this is the owner's own repo | Unlikely to apply |
| Actual deployment behavior after push | Requires GitHub Actions runtime | **NOT RUN — requires push + workflow execution** |

## 4. Corrections applied (this session)

1. **`.github/workflows/pages.yml`** — added `push: branches: [main]` to the
   trigger block (merged with the existing `site-*` tag trigger so no
   duplicate YAML key remains; workflow-dispatch retained). The deployment
   gap is closed structurally: every push to `main` now builds and deploys.
2. **README.md** — rewritten as a full course portal with an explicit
   "deployment pending verification" notice; no unverified URL claims.

## 5. Manual settings required (owner action — cannot be done from here)

1. **Settings → Pages → Build and deployment → Source: “GitHub Actions”.**
   This is the single most likely remaining blocker if the next deploy run
   fails — `actions/deploy-pages` requires it (a common first-run failure
   mode with this action). It cannot be set or confirmed from the local clone.
2. Push `main` (the workflow changes in this session need to be committed first).
3. Watch the **pages** workflow run in the Actions tab.
4. Verify `https://nadeem-majeedch.github.io/Project-Management/` returns
   200 and render the home page.

## 6. Failure-mode reference (for whoever troubleshoots next)

| If the next pages run… | Then… |
|---|---|
| Fails at **Deploy to GitHub Pages** with an HTTP 404 on the Pages API | Source is not "GitHub Actions" — do manual step 1 |
| Fails at **Configure Pages** | Pages not yet enabled and no admin token available to the action; use manual step 1 |
| Fails in **Build site (strict)** | A content regression — CI (`ci.yml`) should have caught the same failure first; compare the two runs |
| Succeeds but the URL still 404s | Check the run's `environment: github-pages` URL output; a few minutes of propagation delay is normal |

## 7. Verification status of this fix

- Workflow YAML: **VERIFIED** — parses; trigger block is
  `push: {branches: [main], tags: [site-*]}, workflow_dispatch`; step
  structure valid (no `with` without `uses`).
- Local strict build + link check: **VERIFIED** — run this session (see
  `docs-meta/public-release-audit.md`).
- **Deployment itself: NOT VERIFIED** — requires the manual settings and a
  push; per project rules this is explicitly not claimed as fixed.
