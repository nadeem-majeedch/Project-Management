<!--
Template: Monitoring dashboard + recovery plan (Labs 12 & 15)
The dashboard is one page, four views, each with an explicit threshold —
a number without a threshold is decoration. The recovery section is where
the numbers become decisions; no "work harder" is allowed as an action.
-->

# Monitoring Dashboard & Recovery Plan — [Project name]

**Status date:** [end of week __] · **Prepared by:** [PM] · **Next review:** [date]

## View 1 — Overall RAG
| Dimension | Status (R/A/G) | Threshold that defines each color | Evidence |
|---|---|---|---|
| Schedule | | G: SPI ≥ 0.95 · A: 0.90–0.95 · R: < 0.90 | EVM row below |
| Cost | | G: CPI ≥ 0.95 · A: 0.90–0.95 · R: < 0.90 | EVM row below |
| Scope | | G: no unapproved scope drift · R: any uncontrolled change | CR log |
| Quality | | G: all gates passed · R: escape or missed gate | quality plan §4 |
| Risk | | G: no Critical open · R: Critical open > 1 gate | register top 5 |

## View 2 — EVM snapshot (numbers from data-pack §D when status week = 9)
| Metric | Value | Reading |
|---|---|---|
| PV / EV / AC | / / | |
| CV = EV − AC | | |
| SV = EV − PV | | |
| CPI = EV / AC | | |
| SPI = EV / PV | | |
| EAC (variant + why this variant) | | |
| TCPI (to BAC) | | |

## View 3 — Milestone & critical-path tracker
| Milestone | Baseline date | Forecast | Δ (wks) | Buffer left |
|---|---|---|---|---|

**Critical-path drift:** [which activities moved; float consumed on near-critical paths]

## View 4 — Top risks & issues this week
| ID | Risk/Issue | Band | Movement (↑↓→) | Action status | Trigger status |
|---|---|---|---|---|---|

## Recovery plan (only when R/A on schedule or cost)
### Facts (no interpretation)
- [EVM indices; physical audit findings; vendor status — cite sources]

### Options (each with numbers, no vibes)
| Option | What changes | Cost impact | Finish forecast (state method: EAC__/CPM re-pass) | Risk introduced | Decides |
|---|---|---|---|---|---|
| O1 Re-baseline (cut scope) | | | | | sponsor |
| O2 Fast-track [activities] | | | | rework p≈[__%] | PM |
| O3 Crash [activity] (slope = ___/wk) | | | | | sponsor (funds) |
| O4 De-scope to defer [items] | | | | | sponsor |

### Recommendation + decision request
[One option, justified by the numbers above; what you need from whom by when.]

**Integrity rule:** TCPI credibility check is mandatory — if TCPI > 1.10,
the plan must show why sustained efficiency can jump that much, or choose
a scope/date option instead.
