---
title: Downloadable Resources
---

# Downloadable resources

Only files that actually exist in the repository are listed. Every link opens
the raw file — use your browser's *Save as* (or right-click → Save link as).

## Template library (Markdown)

Editable masters — copy into your project repo and fill. The full annotated
set lives in the [template library](templates/index.md).

- [Charter template](templates/charter-template.md)
- [Stakeholder register](templates/stakeholder-register-template.md)
- [Scope statement](templates/scope-statement-template.md)
- [WBS](templates/wbs-template.md) ·
  [WBS dictionary](templates/wbs-dictionary-template.md)
- [Activity dependency table](templates/activity-dependency-template.md) ·
  [CPM worksheet](templates/cpm-worksheet-template.md)
- [Gantt & resource plan](templates/gantt-resource-template.md)
- [Cost baseline](templates/cost-baseline-template.md)
- [Quality plan](templates/quality-plan-template.md)
- [Risk register](templates/risk-register-template.md) ·
  [Probability–impact worksheet](templates/probability-impact-template.md)
- [Communication plan](templates/communication-plan-template.md)
- [Monitoring dashboard](templates/monitoring-dashboard-template.md)
- [Sprint planning](templates/sprint-planning-template.md)

## Spreadsheet-compatible worksheets (CSV)

Open directly in Excel, Google Sheets, or LibreOffice. These carry the
CAMPUS-MEND educational scenario data used across the labs (clearly labeled
fictional data — see the [data pack](labs/data-pack.md)).

- [Core schedule](templates/data/campus-mend-schedule.csv) — 8-package §A schedule
- [Budget build](templates/data/campus-mend-budget.csv) — role hours, rates, cost chain
- [Hours roll-up](templates/data/campus-mend-hours.csv) — WBS-level effort
- [Backlog](templates/data/campus-mend-backlog.csv) — sprint-planning item set
- [Risk list](templates/data/campus-mend-risks.csv) — register rows for Lab 9
- [Status snapshot, week 9](templates/data/campus-mend-status-wk9.csv) — EVM inputs for Lab 13
- [EVM status, week 9](templates/data/evm-status-wk9.csv) — PV/EV/AC status worksheet
- [CPM pass worksheet](templates/data/cpm-pass-worksheet.csv) — blank forward/backward pass grid
- [Risk-score worksheet](templates/data/risk-score-worksheet.csv) — blank P×I scoring grid
- [Sprint-plan worksheet](templates/data/sprint-plan-worksheet.csv) — blank sprint commitment sheet
- [WBS hours worksheet](templates/data/wbs-hours-worksheet.csv) — blank 100%-rule roll-up grid
- [Monitoring worksheet, week 9](templates/data/monitoring-week9-worksheet.csv) — blank control-chart grid

## Lab workbook

The [labs index](labs/index.md) links all 16 briefs; each brief is
printable from the browser. The scenario
[data pack](labs/data-pack.md) is the shared context for Labs 1–16.

## Monte Carlo simulator (Python, standard library only)

`tools/campus_mend_sim.py` in the
[repository](https://github.com/nadeem-majeedch/Project-Management) — the
deterministic, seeded schedule simulator used in Lab 11. Run:
`python tools/campus_mend_sim.py` (no third-party packages required).
