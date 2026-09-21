# CAMPUS-MEND — Lab Data Pack

**Educational scenario.** All organizations, teams, names, and figures are
fictional teaching data for PM-401 labs. This file is the single dataset for
every lab, so numbers stay consistent across labs, assignments, and the
answer checker.

## The story

Northlake University's student portal (attendance, course registration,
results, fee challans) runs on a custom platform built in-house in 2018.
Semester-start peaks crash it 30–60 minutes at a time; result-day outages
sparked a student-union complaint and a fixed 48-hour publishing delay.
The registrar gave Northlake IT a 17-week window aligned to the January
semester break to rebuild the student-facing platform. The replacement,
**CAMPUS-MEND**, keeps the same student-facing features but re-architects
the core: a portal web app, an LMS adapter, and a new analytics
repository. Legacy contracts and exam rules pin two external
dependencies: the LMS vendor's schema (R7) and the academic-calendar
rule (R4) that results must publish within 48 hours.

**Constraints you inherit (do not change them):** team of 3 developers
(≈ 80 pooled product h/wk after ceremonies), 1 QA engineer (40 h/wk),
1 data engineer dedicated to the project (40 h/wk), PM at 50% (20 h/wk);
2 contract testers join during testing (G). Fixed deadline (week 17);
vendor SOW capped at PKR 1,950,000; two hard external dependencies
(LMS vendor schema + 48-hour result SLA); QA independent of dev.

## A. Core schedule — eight work packages (Lab 4 onward)

| ID | Name | Predecessors | Duration (weeks) |
|---|---|---|---|
| A | Legacy audit & requirements sign-off | — | 2 |
| B | Database & schema design | A | 3 |
| C | Portal web app build | B | 4 |
| D | Analytics repository | B | 5 |
| E | Streaming feature pipeline | D | 4 |
| F | LMS adapter build | B, C | 3 |
| G | System & performance testing | C, E, F | 2 |
| H | Rollout & 48h result SLA validation | G | 1 |
| **Project** | | | **17 weeks** |

## B. Hour and rate data (Labs 3, 5, 6)

| Package | Dev h | QA h | DE h | PM h |
|---|---|---|---|---|
| A Legacy audit & requirements sign-off | 40 | 20 | 0 | 8 |
| B Database & schema design | 80 | 20 | 40 | 8 |
| C Portal web app build | 320 | 80 | 0 | 24 |
| D Analytics repository | 120 | 20 | 200 | 12 |
| E Streaming feature pipeline | 120 | 20 | 120 | 12 |
| F LMS adapter build | 120 | 40 | 0 | 16 |
| G System & performance testing | 40 | 240 | 0 | 8 |
| H Rollout & SLA validation | 24 | 40 | 8 | 8 |
| **Total** | **864** | **480** | **368** | **96** |

**Rates (internal staff, blended):** Developer PKR 1,800/h · QA PKR 1,200/h ·
Data Engineer PKR 2,400/h · PM PKR 2,200/h · vendor (LMS adapter work) PKR 2,500/h.
Indirect rate **25% of labor**. **Contingency 10% of the subtotal**
(labor + indirects + direct costs). Vendor SOW cap: PKR 1,950,000.
(Management reserve 5% sits *above* the baseline and is sponsor-held —
it never appears in the cost baseline.)

## C. Baseline budget (Lab 6 answer anchor)

| Line | Amount (PKR) |
|---|---|
| Labor | 3,225,600 |
| Indirects (25% of labor) | 806,400 |
| Direct costs (licenses + GPU) | 88,000 |
| Subtotal | 4,120,000 |
| Contingency (10% of subtotal) | 412,000 |
| **Cost baseline** | **4,532,000** |

Direct costs: LMS adapter vendor effort is inside the SOW cap; licenses:
monitoring tool PKR 40,000; test-data generation + GPU hours PKR 48,000.
The vendor SOW is a *fixed-price* contract constraint, not a baseline line.
Management reserve = 5% of baseline = PKR 226,600 (sponsor-held; funding
ask = PKR 4,758,600).

## D. Status data at end of week 9 (Labs 13 & 15) — the mid-project crisis

Baseline plan at end of week 9: 9 weeks elapsed of 17. Planned value,
time-phased per the baseline S-curve (CAMPUS-MEND lab data pack §C):

- PV (end of week 9) = **PKR 2,026,000**
- EV = **PKR 1,762,000** (accepted work per EV rules)
- AC = **PKR 2,041,000**
- Physical status: A, B, C, D, F complete; **E (Streaming features)
  ~55% complete** per the team, but the QA ticket-sampling audit
  verifies only **40%** of E's scope done and the LMS-adapter integration
  spike is stalled (F "done" hides an open integration ticket).

## E. Risk data (Lab 9 seed set — you must complete it)

Scale definitions (5-point): P = 1 (<10%) to 5 (>70% within the 17-week
horizon); impact rated separately on schedule (S), cost (C), quality (Q),
each 1–5; **declared score = max(S,C,Q) × P**. Bands: Low ≤ 5,
Medium 6–11, High 12–15, Critical 16–25.

| ID | Cause → event → effect | P | S | C | Q | Owner |
|---|---|---|---|---|---|---|
| R1 | LMS vendor schema changes mid-build → adapter rework → integration slip | 3 | 4 | 2 | 3 | PM |
| R2 | DE resignation during D/E → pipeline stalls → 48h SLA risk | 2 | 5 | 3 | 2 | PM |
| R3 | Inconsistent label eras in legacy results → biased reporting | 3 | 1 | 2 | 5 | QA |
| R4 | **Realized**: academic-calendar rule (48h) binds → deadline fixed | — | — | — | — | Sponsor |
| R5 | Governance gate demands extra evidence → rework of test artifacts | 4 | 3 | 2 | 2 | PM |
| R6 | GPU quota cut → analytics validation queues → E slips | 2 | 3 | 2 | 2 | DE |
| R7 | Vendor delivery slips 2 weeks → F late → G compresses | 2 | 4 | 3 | 1 | PM |
| R8 | Legacy result dates use ambiguous formats → migration defects | 4 | 3 | 2 | 4 | DE |

## F. Backlog (Lab 14) — 10 items, CAMPUS-MEND sprint

| ID | Item | Points | Value (1–10) | Type |
|---|---|---|---|---|
| B1 | Registration deadlocks during peak — fix + load test | 13 | 10 | |
| B2 | Provision test-data generation for peak replay | 3 | 4 | |
| B3 | Attendance API caching layer | 8 | 9 | |
| B4 | Fee challan reconciliation report | 5 | 7 | |
| B5 | LMS roster sync — retry & dead-letter handling | 8 | 6 | |
| B6 | Result-publishing pipeline — staging rehearsal | 13 | 9 | |
| B7 | Student notification service (SMS/email) | 5 | 5 | |
| B8 | Dashboard: portal latency + error budget | 3 | 3 | |
| B9 | Schema migration rollback drill | 5 | 8 | |
| B10 | Accessibility pass on portal forms | 3 | 2 | |

Total backlog = 66 points. Sprint length 2 weeks. The development team is
4 people (3 devs + 1 QA), 10 productive hours/person/week.

## G. Quality and measurement targets (Labs 8, 13)

- Portal p95 page response ≤ 2.0 s under 3,000 concurrent users.
- Batch result publication job completes within the 48-hour SLA with
  ≥ 2 hours of margin.
- Defect escape rate to production ≤ 2 per release; regression suite runs
  ≤ 25 minutes.
- WBS dictionary QA hours are the audit budget: E's QA allocation is
  20 h — a 55%-claim without tickets against those hours is an EV red flag.

## H. How labs use this pack

| Lab | Sections used |
|---|---|
| 1 Charter, 2 Stakeholders | The story + constraints (you add no new facts) |
| 3 Scope & WBS | §A, §B (hours become scope evidence) |
| 4 Network & CPM | §A |
| 5 Gantt & resources | §A, §B |
| 6 Cost baseline | §B, §C |
| 7 Quality plan | §G |
| 8 Communication plan | The story + stakeholder outputs of Lab 2 |
| 9–10 Risk register, P×I | §E |
| 11 Monte Carlo | §A (perturb 3 packages; script provided) |
| 12 Monitoring dashboard | §D |
| 13 EVM & recovery | §D |
| 14 Agile backlog & sprint | §F |
| 15 Change control & recovery plan | §D + Lab 13 outputs |
| 16 Capstone pack assembly | All prior outputs |

**Integrity note:** the data pack is teaching data. Where an assignment or
the capstone requires "your own project," use your own scenario — reusing
CAMPUS-MEND numbers there is allowed only with citation to this pack.
