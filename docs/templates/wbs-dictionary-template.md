<!--
Template: WBS dictionary (Lab 5) — one row per work package
The dictionary is what makes a WBS executable: without acceptance criteria and
EV rules, "percent complete" is a negotiation, not a measurement.
Keep rows short; put detailed prose in linked files if truly needed.
-->

# WBS Dictionary — [Project name]

| WBS ID | Work package | Description (2–3 lines) | Owner | Predecessors | Estimate (O/M/P → PERT) | Acceptance criterion | EV rule | QA budget |
|---|---|---|---|---|---|---|---|---|
| 1.4.1 | | | | | / / → | | | |
| 1.4.2 | | | | | / / → | | | |
| 1.4.3 | | | | | / / → | | | |

*(example — delete)* `E Streaming feature pipeline` — owner: DE ·
O/M/P = 3/4/5 wk → PERT 4.0 · acceptance: p95 freshness ≤ 5 min on replay
load, evidence in staging · EV rule: 0/100 at acceptance · QA budget: 20 h
(from data-pack §B) — **any completion claim must show tickets against those hours.**

## EV-rule palette (pick per package; avoid raw percent-complete)
| Rule | Use when |
|---|---|
| 0/100 | short packages; binary acceptance evidence exists |
| 50/50 | packages ≤ 2 weeks; start is objective, finish is verifiable |
| Weighted milestones (e.g. 30/30/40) | long packages with natural evidence gates |
| Percent-complete | **avoid** — unverifiable; if used, pair with ticket audit |

## Change discipline
Dictionary edits are baselined artifacts: changes after sign-off go through
change control with a CR reference. Add column `Changed by CR#` only after
baseline approval.
