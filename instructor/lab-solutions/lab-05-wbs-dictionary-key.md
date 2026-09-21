# Lab 5 Answer Key — WBS Dictionary

## Model dictionary rows (accept equivalent quality; arithmetic must match)

| Pkg | Owner | O/M/P (wk) | PERT | Acceptance criterion (observable) | EV rule | QA h |
|---|---|---|---|---|---|---|
| A | PM | 2/2/2.5 | 2.08 | requirements doc signed by registrar + exams office | 0/100 | 20 |
| B | DE lead | 3/3/4 | 3.17 | schema passes data-contract test; migration dry-run clean | 0/100 | 20 |
| C | Dev lead | 3.5/4/5.5 | 4.17 | peak replay: zero deadlocks; code reviewed | 0/100 | 80 |
| D | DE | 4/5/7 | 5.17 | freshness queries ≤ 5 min p95; era audit passed | 0/100 | 20 |
| E | DE | 3/4/8 | 4.50 | p95 freshness ≤ 5 min on replay load, staging evidence | 0/100 | 20 |
| F | Vendor + PM | 3/3/4 | 3.17 | **integration ticket closed** + roster sync dead-letter drill passed | 50/50 | 40 |
| G | QA lead | 2/2/2.5 | 2.08 | load test 3 runs ≤ 2.0 s p95; SLA rehearsal ≥ 2 h margin | weighted 30/30/40 | 240 |
| H | PM + QA | 1/1/1 | 1.0 | 48 h SLA validated in production window | 0/100 | 40 |

QA split: 20+20+80+20+20+40+240+40 = **480** ✓. E-audit rule: any % claim on
E requires tickets against E's 20 QA h (Lab 13 enforces it).

**EV-rule rationale (pass requires a line per choice):** H binary SLA
evidence → 0/100; G has three natural evidence gates → 30/30/40; F's start is
objective (vendor handover), finish verifiable (ticket) → 50/50; E claims
must stay auditable → 0/100 at staging acceptance, never percent-complete.

**PERT skew note (model):** E right-skewed (O 3 < M 4 < P 8): integration
surprises add work, never remove it — PERT 4.5 sits above M, honest about the
tail. Same logic on B (legacy mess can only add).

## Common wrong answers

| Error | Correction |
|---|---|
| Acceptance = "works correctly" | name the observable evidence (test, document, drill) |
| Percent-complete chosen for E | the exact rule Lab 13's crisis exposes; must be 0/100 or milestone |
| QA split ≠ 480 | arithmetic drift — usually G's 240 misplaced |
| PERT symmetric on integration packages | integration risk is right-skewed; O/M/P must reflect it |
| No change-discipline footer | dictionary is baselined; edits need CR reference |

## Reflection guidance

1. 0/100 forces *finish* evidence before any credit; percent-complete lets
   belief drive EV — the 55% myth in mini-form.
2. F's criterion must demand the integration ticket closed + dead-letter
   drill — otherwise week 9's "F complete with open ticket" is legitimate.
3. 0/100 understates mid-flight progress (bias toward late credit) — safe
   for SLA credibility, annoying for morale; the opposite bias (inflation)
   is the dangerous one.

## Preparation notes

Collect dictionaries before Lab 7 — the budget lab reads estimates and QA
hours directly. Flag any row where acceptance is unverifiable; those rows
become Lab 13's measurement traps.
