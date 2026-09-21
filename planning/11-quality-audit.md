# PM-401 Repository Quality Audit Report

**Date:** September 20, 2026 · **Auditor:** Codebuff (automated + evidence-based)
**Method:** Every claim below was verified by execution or direct inspection —
nothing is asserted from memory. The audit is re-runnable at any time:

```bash
python tools/audit_repo.py          # this report's checks
python tools/validate.py            # content gates 1-15
python tools/check_cases.py         # numeric case assertions
python tools/check_answers.py       # lab answer-key chains
python tools/check_slides.py        # slide package
python tools/check_links.py         # built-site links (after mkdocs build)
```

---

## 1. Executive summary

**Overall status: PASS WITH WARNINGS**

| Verdict | Count |
|---|---|
| Verified | 25 |
| Warning | 1 |
| Not tested | 1 |
| Blocker | 0 |

The repository is structurally complete, numerically sound (independently
recomputed, not self-attested), and the published site is clean, subpath-safe,
and free of instructor leaks. The single warning is a documented rounding
convention; the single not-tested item is GitHub Actions runtime behavior,
which cannot execute without pushing.

---

## 2. Findings register

Legend: **V** = Verified · **W** = Warning · **N** = Not tested · **B** = Blocker

### A. Academic completeness

| ID | St | Finding | Evidence |
|---|---|---|---|
| A1 | V | 32/32 lecture pages on disk, numbering sequential L01–L32, matching 32 roster entries | `glob` + roster parse |
| A2 | V | 6 CLOs defined; every CLO taught (3–9 lectures each) and assessed by ≥ 1 component | course-data.yaml cross-walk |
| A3 | V | Assessment weights sum to exactly 100 | A1–A8 = 10/10/10/10/20/10/25/5 |
| A4 | V | 105 cases in 4 sequential bands: Beginner 20, Intermediate 25, Advanced 30, Expert 30 | band YAML parse, IDs 1..105 gapless |
| A5 | V | All 32 teaching packages carry both CS and Data Science content | regex sweep: 0 packages missing DS content |

### B. Teaching quality

| ID | St | Finding | Evidence |
|---|---|---|---|
| B1 | V | All 32 packages contain all 16 required sections (objectives → linked resources) | section-presence sweep |
| B2 | V | Learning objectives use measurable Bloom verbs in 32/32 packages | verb-pattern match on objectives sections |
| B3 | V | 16 labs each carry objectives, steps, expected outputs, reflection, rubric | section sweep |
| B4 | V | Lab answer keys 16/16 (instructor-only location) | file count |
| B5 | V | Case answer keys 105/105 with reasoning/alternatives blocks | file count + earlier structural checks |

### C. Numerical correctness

| ID | St | Finding | Evidence |
|---|---|---|---|
| C1 | V | CS-15 CPM duration **28** independently recomputed from activity table (fresh forward/backward pass written for this audit) | matches key; multiple zero-float branches are the case's documented design |
| C2 | V | CS-26 EVM: CPI 0.8947, EAC₁ 4,470,588, TCPI 1.0952 — recomputed from raw data, exact match | independent arithmetic |
| C3 | **W** | L19 slide/table EAC₁ 74,050 is computed from **rounded** CPI 0.87; exact value is 74,118 (0.09% deviation). EAC₃ similarly 81,780 vs exact 81,742. Pedagogically defensible (matches the teaching package's rounded walk-through) but should carry a rounding footnote | recomputation during audit |
| C4 | V | CampusHub budget chain: labor 54,775 → baseline 64,424 recomputed exactly; consistent across L13 package, L19 slides, and check_answers.py | multiplication + roll-up |
| C5 | V | 32 numeric cases ≥ 30 required; 380 assertions machine-recomputed by check_cases.py | existing checker + audit |

### D. Website quality

| ID | St | Finding | Evidence |
|---|---|---|---|
| D1 | V | All 57 nav entries resolve to real files | nav walk + disk check |
| D2 | V | `site_url` correct for project subpath; asset links relative | mkdocs.yml + built HTML scan |
| D3 | V | `templates/` re-included against MkDocs ≥ 1.6 hard exclusion | `exclude_docs: !templates/` present; CI smoke test guards it |
| D4 | V | Zero instructor content in built `site/` (210 pages scanned) | rglob scan, both live and in audit tool |
| D5 | V | Calendar pages in build; 32-row grid with 7 required columns verified **live in a browser session** | registered preview + DOM inspection |
| D6 | V | Accessibility/layout live checks passed: search present, skip-link present, palette toggle, viewport meta, `lang=en`, no heading-level skips, 0 images without alt, 0 instructor links in rendered nav | DOM inspection via preview |
| D7 | V | `check_links.py`: 21,865 href/src attributes, 0 broken, 0 root-absolute (outside 404.html), 0 fs leaks | executed this audit |

### E. Technical quality

| ID | St | Finding | Evidence |
|---|---|---|---|
| E1 | V | Both workflows parse as valid YAML; pages.yml uses the current artifact method | yaml.safe_load executed |
| E2 | V | Secret-pattern scan clean across .py/.yml/.yaml/.md/.csv/.css | rglob scan, venv/site excluded |
| E3 | V | No placeholder residue (LOREM/FIXME/TBD:/XXX:) in any Markdown | rglob scan |
| E4 | V | 8/8 validation tools present and all executed successfully during this audit | direct runs |
| E5 | **N** | GitHub Actions runtime behavior (Pages deploy) not tested — requires push; syntax verified locally, manual setup steps documented in README | environment limitation |

---

## 3. Warnings (all minor, none block publication)

| ID | Area | Warning | Recommended action | Priority |
|---|---|---|---|---|
| W1 | D | **Inventory doc staleness** — `planning/07` still described labs/assignments/capstone/templates as "shells" from an early phase, contradicting the authored files. *(Fixed during this audit — rows now reflect 16 labs, 3 briefs, 8 capstone pages, 27 template files.)* | None — corrected | Resolved |
| W2 | C | **L19 EAC rounding** — 74,050 (rounded-CPI) vs 74,118 (exact). Appears consistently in teaching package, slides, and exam key, so students see one number; the derivation teaches the rounded-CPI shortcut deliberately. | Add one footnote to the L19 teaching package at next edit: "with unrounded CPI, EAC₁ = 74,118". | Low |
| W3 | E | **QB-U6 variant flagged by its own author** — one alternative exam item is marked "instructor must recompute before use" (the primary chain is machine-verified). | Recompute before first use, or delete the variant. | Low |
| W4 | A | **Calendar dates unconfigured** — by design; `schedule-config.yaml` awaits instructor input, so no institutional dates appear anywhere (this is compliance, not a defect, but is flagged so it isn't forgotten). | Set `configured: true` + dates before semester start; regenerate. | Medium (time-bound) |
| W5 | E | **Python version drift** — local runs used Python 3.14.7; workflows pin 3.12; `requirements.txt` documents no floor. Behavior identical in practice (stdlib + pyyaml only), but CI/local parity is informal. | Add a one-line Python-version note to requirements.txt or README. | Low |

## 4. Prioritized remediation plan

| # | Action | Files | Priority | Effort |
|---|---|---|---|---|
| 1 | Configure semester dates in `planning/schedule-config.yaml` (`configured: true`, start, days, holidays) and regenerate | 1 config + regenerated outputs | **High** (time-bound) | 5 min |
| 2 | Recompute or delete the flagged QB-U6 variant before first exam use | 1 exam-bank file | High (before use) | 10 min |
| 3 | Add rounding footnote to L19 EVM material | 1–2 files | Medium | 5 min |
| 4 | Document Python floor (3.12) alongside pip requirements | README/requirements | Low | 2 min |
| 5 | After push: run the pages workflow once and confirm the live site (E5 → Verified) | GitHub settings + Actions | High (requires push) | 15 min |

No blockers: nothing in this list prevents committing and publishing.

## 5. Verification commands actually executed during this audit

| Command | Result |
|---|---|
| `python tools/validate.py` | PASS (0 failures) — gates 1–15 |
| `python tools/check_cases.py` | PASS — 105 cases, 380 numeric assertions |
| `python tools/check_answers.py` | CHECK PASS |
| `python tools/check_slides.py` | SLIDES PASS — 32 decks, 38 diagrams |
| `python tools/calendar.py` | CALENDAR PASS (unconfigured mode; ICS correctly withheld) |
| `python tools/scaffold.py` | exit 0 |
| `python tools/audit_repo.py` | **PASS WITH WARNINGS** (25 V / 1 W / 1 N / 0 B) |
| `mkdocs build --strict --site-dir site` | exit 0, 210 HTML pages, 0 warnings |
| `python tools/check_links.py` | LINK CHECK: PASS |
| Live preview DOM inspection (home + calendar) | all structural/a11y checks passed |

## 6. Final status

> **PASS WITH WARNINGS**
>
> All deliverables exist and are internally consistent; all numeric claims
> sampled were independently verified; the published layer is complete,
> accessible, and leak-free; tooling is comprehensive and all of it runs.
> The warnings are low-effort instructor follow-ups (rounding footnote, one
> flagged exam variant, date configuration) — none affect correctness of
> what is already published.

Nothing was committed or pushed during this audit; the test HTTP server used
for live preview was shut down afterwards.
