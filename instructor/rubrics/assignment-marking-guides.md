# Marking Guides — Assignments (A2, A3, A4)

> **INSTRUCTOR ONLY — not published to the site.**
> These guides operationalize the weight guides published in the student
> briefs ([A2](../../docs/assignments/a1-scope-schedule.md),
> [A3](../../docs/assignments/a2-risk-register.md),
> [A4](../../docs/assignments/a3-evm-analysis.md)). Component weights are
> fixed by the briefs; the 0–3 level anchors below are the instructor layer.
> Rubric-to-percentage conversion remains a flagged instructor decision
> (grading page, warning block).

## General conventions (all three assignments)

- Method marks: correct technique with arithmetic slips → −1/slip, capped at
  −20% of the artifact's marks; wrong method → 0 for the item regardless of
  the answer.
- Assumption honesty: conclusions from *unstated* assumptions cap that
  artifact at "developing."
- AI disclosure: disclosed assistance is legitimate; undisclosed structural
  drafting → 0 for the artifact plus the integrity escalation path.
- Return within one week with artifact-level comments; the two most common
  errors are debriefed in the next lab.

## A2 — Scope & Schedule (10% · CLO2 · due after L16)

| Artifact (weight) | 2 — proficient | 3 — exemplary |
|---|---|---|
| Scope + WBS + dictionary (30%) | ≥ 3 levels, 100% rule holds on test, dictionary for 2 packages | dictionary entries carry acceptance criteria; exclusions pre-empt the 3 likeliest disputes (CS-50 pattern) |
| Estimates + rationale (25%) | O/M/P on all packages with stated basis | calibration data cited (CS-14 pattern); ranges survive a "defend the P" probe |
| CPM + float table (25%) | both passes complete, CP correct | float interpreted as risk (near-critical paths named; L11/L19 connections) |
| Gantt + milestones (20%) | baselined, milestones match network | levelling decisions shown with float consumption stated (CS-16 pattern) |

**Common failure patterns to check first:** org-chart WBS; PERT applied to
the M value; backward pass using LF = EF for non-terminal activities
(L11's known trap); milestones dated from the Gantt, not the network.

## A3 — Risk Register & Responses (10% · CLO4 · due after L19)

| Artifact (weight) | 2 — proficient | 3 — exemplary |
|---|---|---|
| Register ≥ 18 risks (35%) | normalized cause→risk→effect; qualified (prob/impact scales) | risks span all taught categories incl. data-quality/AI-specific (L23/L28 links) |
| EMV analysis (15%) | EMV computed on the quantified subset | EMV re-ranking vs P×I discussed; magnitude-blindness named (CS-21 lesson) |
| Response plans top 10 (35%) | strategy + owner + trigger per response | secondary risks named and owned; baseline-impact flags correct (CS-23 pattern) |
| Contingency sizing + defense (15%) | defensible sizing logic stated | sizing tied to EMV total and residual exposure, with the sponsor-conversation drafted (CS-73 link) |

**Viva probes for AI-drafted registers (next lab):** "why is this the
correct strategy for R7?", "which response changes the critical path?",
"what secondary risk did your transfer create?"

## A4 — EVM Case Analysis (10% · CLO4 · due after L21)

| Artifact (weight) | 2 — proficient | 3 — exemplary |
|---|---|---|
| EVM computation (40%) | full indicator set, formulas shown with numbers substituted | all four EAC variants with the *assumption* each encodes (L19's table) |
| Diagnosis incl. traps (30%) | CPI/SPI read together; direction stated | measurement traps named — committed costs (CS-51), EV-rule gaming, response to SPI-1.0/CPI-0.8 pattern (QB-U4-08) |
| Recovery comparison (20%) | two options compared against evidence | efficiency-assumption tested like CS-82: historical rate, named cause, checkpoint date |
| EV rule design (10%) | a consistent EV rule proposed | rule resists gaming; credits partial completion defensibly |

**Hard rule from the brief:** unexplained results score zero regardless of
final index values — the diagnosis layer is where A4 is won.
