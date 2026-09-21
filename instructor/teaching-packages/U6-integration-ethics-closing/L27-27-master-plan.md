# Lecture 27 — The Master Project Plan: Integrating Everything

> **Package for:** L27 · Week 14 · Unit U6 · CLO6 · Bloom: Create · **Capstone plan draft due today**
> **Case anchor:** CS-38 (assembly + red-team review)
> Companion: [`L27` skeleton](../../../docs/lectures/L27-27-master-plan.md) · [CS-38 brief](../../../docs/cases/CS-38.md)

## Learning objectives

1. Assemble the capstone master plan from semester artifacts into one coherent document.
2. Run the four consistency stress tests (schedule↔resource↔budget↔risk↔communication) and repair the findings.
3. Conduct a peer red-team review that surfaces inconsistencies the authors cannot see.
4. Justify tailoring decisions in writing, at plan level.

## Required prior knowledge

- The whole semester's artifacts: WBS (L09), network/Gantt (L11–L12), budget
  (L13), quality/DQ (L14), register (L15–L17), DoD/model gate (L23), board
  evidence (L21–L22).

## Teaching notes

This is the semester's integration day — the lecture *is* the workshop. The
conceptual core: **plans fail at the seams, not in the sections.** Each
semester artifact was built to be locally correct; integration asks whether
they are *mutually* correct: the schedule's critical path must consume the
budget's hump; the register's top risks must have funded responses; the
communication plan must serve the register's stakeholders.

The four stress tests (below) are the instrument; the red-team is the engine.
Structure the room as a consulting shop: assemble (30), test (20), red-team
exchange (35), repair (25). Your role: circulate with the stress-test sheet
and force arithmetic honesty — most teams discover their plan is three
documents in a trenchcoat.

The tailoring-justification section is graded separately in the rubric —
teams must *write* what they cut and why (the L08 worksheet becomes prose).

## Definitions & concepts

- **Master plan** — the integrated document: charter, baselines (scope/
  schedule/cost), subsidiary plans (quality/DQ, risk, communication,
  procurement), tailoring justification, governance.
- **Consistency stress tests** —
  1. *Schedule↔Budget:* S-curve hump matches critical-path load; contingency
     appears in both.
  2. *Risk↔Budget:* every funded response names its contingency source;
     unfunded highs are decisions, not oversights.
  3. *Schedule↔Risk:* near-critical paths (float ≤ 2) have named monitoring.
  4. *Comms↔Stakeholders:* every register stakeholder appears in the matrix;
     every quadrant has a channel.
- **Red-team review** — adversarial peer review against the rubric; findings
  are logged as issues with owners (process discipline applies to plan work).
- **Plan sign-off gate** — sponsor (instructor) acceptance; the defense (L32)
  defends the *approved* plan.

## Practical examples

**CS:** the portal plan's seam failure (the classic): schedule shows testing
in weeks 8–9, budget's labor line drops 30% in week 8 (another project's
people) — the stress test catches it; repair: re-phase or re-fund, decision
recorded.

**DS:** the churn plan's seam: the model gate (L23 DoD) requires fairness
evidence, but the schedule has no fairness-audit task and the budget no
audit hours — the gate is unfunded theater. Repair: +40 h audit task on the
path (it gates rollout — it *is* critical), contingency re-derived.

## Worked example

**Running stress test 2 (board, with numbers):**

Team plan extract: contingency $5,857 (L13's 10%); register top risks:
R1 ingestion (mitigation cost 30 h ≈ $1,350 — *funded from where?*), R3
label-era bias (mitigation 60 h ≈ $2,700 + audit 40 h ≈ $1,800 — total
$4,500), R5 gate evidence ($900).

Arithmetic: funded responses = 1,350 + 4,500 + 900 = **$6,750 > $5,857
contingency** — the plan promises responses it cannot pay for. Findings:
(a) either de-scope one response (which? decide by score: R3 is critical —
keep; R5 could be absorbed into PM hours — 20 h is already in the plan),
(b) or raise contingency with L16-style evidence. Repair chosen: R5 absorbed
(0 net), R1+R3 funded = $5,850 ≈ contingency ✓ — and the *decision trail is
written into the risk section*, which is what the rubric's "internal
consistency" dimension wants: not a perfect plan, a *traceably reasoned* one.

## Common misconceptions

| Misconception | Correction |
|---|---|
| "A plan is a document collection." | Integration is the deliverable; the stress tests exist because seams fail silently. |
| "Red-team findings are attacks." | They are the cheapest possible failures — found on paper, not on the project; the rubric rewards closing them. |
| "Tailoring justification is for the appendix." | It is a rubric dimension because cut-without-reason is how projects lie to themselves (L08's doctrine, now graded). |
| "Consistency means perfect numbers." | It means *traceable decisions* — the worked example's repair trail is the standard, not a spreadsheet that balances by luck. |
| "The plan is done when written." | It is done when red-teamed, repaired, and signed — the defense defends the *gate-approved* version. |

## Classroom activities

1. **Assembly sprint (30 min):** sections from semester artifacts into the
   master-plan template; missing sections logged (not invented).
2. **Stress-test gauntlet (20 min):** teams run all four tests on their own
   plan; findings logged with severity.
3. **CS-38 red-team exchange (35 min):** plans swapped; reviewers use the
   rubric as attack sheet; ≥ 5 findings required, each with a repair
   suggestion.
4. **Repair block (25 min):** fixes applied live; instructor circulates on
   the seam failures.

## Discussion questions

1. Which stress test caught your plan — and why did the seam exist (what earlier decision caused it)?
2. Your red-teamer flagged the tailoring section as "cuts without defenses." What would convince them — and what does that tell you about the defense you'll give at L32?
3. The repair changed your critical path. What must happen *formally* before the baseline moves? (L20's CCB — governance discipline to the end.)

## Practical exercise

**In class:** CS-38 deliverable (integrated skeleton + findings log). **Take
home (team, due L30):** full master plan v2 with red-team repairs and the
tailoring justification — the version the L32 defense defends. Instructor
sign-off requests go through the LMS.

## Formative assessment (exit ticket)

1. Name the four stress tests.
2. What makes a red-team finding "closed"?
3. Where does the tailoring justification live, and which rubric dimension grades it?

## Reading & references

- PMI. (2021). *PMBOK Guide* (7th ed.) — Planning domain (the integration
  logic); Delivery domain.
- [Capstone rubric](../../../docs/capstone/capstone-rubric.md) — the
  red-team's attack sheet; [charter & tracks](../../../docs/capstone/capstone-charter.md)
  for the section list.

## Two-hour teaching plan

| Slot | Segment | Materials |
|---|---|---|
| 0:00–0:08 | Hook: the plan that balanced perfectly and wasn't one plan | — |
| 0:08–0:30 | Master-plan anatomy; four stress tests; work order | board |
| 0:30–0:50 | Worked example: risk↔budget arithmetic + repair trail | board |
| 0:50–1:00 | Break | |
| 1:00–1:30 | Assembly + stress tests | template + artifacts |
| 1:30–1:55 | CS-38 red-team exchange | rubric sheets |
| 1:55–2:00 | Repair block start + exit ticket | — |

## Instructor preparation notes

- Print rubric-based red-team sheets (the [capstone rubric](../../../docs/capstone/capstone-rubric.md)
  with finding-log columns).
- Verify *before* class that every team's draft exists (L20 checkpoint);
  teams without drafts join a parallel assembly room — the red-team needs
  complete targets.
- Sign-off queue: set LMS deadline for v2 requests; the defense schedule
  (L32 order) publishes at sign-off.

## Linked resources

- Lecture skeleton: [`docs/lectures/L27`](../../../docs/lectures/L27-27-master-plan.md)
- Case: [CS-38](../../../docs/cases/CS-38.md)
- Capstone: [rubric](../../../docs/capstone/capstone-rubric.md) ·
  [charter & tracks](../../../docs/capstone/capstone-charter.md) ·
  [defense format](../../../docs/capstone/defense-format.md)
- Forward: [ethics L28](../../../docs/lectures/L28-28-ethics-governance.md)
  (governance section of the plan).
