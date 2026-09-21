# Lecture 02 — Strategy, Portfolios, Programs & Projects

> **Package for:** L02 · Week 1 · Unit U1 · CLO1 · Bloom: Understand
> **Case anchors:** CS-03 (portfolio cut-line, in class), CS-95 (rebalancing after strategy shift — homework lane)
> Companion: [`L02` skeleton](../../../docs/lectures/L02-02-strategy-portfolio.md) · [CS-03 brief](../../../docs/cases/CS-03.md)

## Learning objectives

1. Define portfolio, program, project, and operations and place real work correctly among them.
2. Apply a weighted scoring model to candidate projects and defend a funding cut line.
3. Explain why portfolio selection errors dwarf execution errors.
4. Relate a single project's charter back to portfolio-level intent.

## Required prior knowledge

- L01 (project vs operations; why failure matters).
- Arithmetic comfort with weighted averages.

## Teaching notes

The big idea: **doing the right projects beats doing projects right.** Students
rarely think about *selection*; they think delivery is the whole game. Use the
scale asymmetry: a delivery overrun costs weeks; funding the wrong project
wastes the whole budget.

Teaching sequence: definitions via a university example (the university runs
*dozens* of concurrent projects — who decides which?), then the weighted
scorecard as this lecture's calculation (light but real), then CS-03 as a
cut-line negotiation. Emphasize that scores are *arguments*, not truth: the
weights encode strategy, and changing weights changes the decision — that is
the point, not a flaw.

Connect forward: the charter (L06) inherits its objectives from portfolio
intent; benefits measurement returns in L29.

## Definitions & concepts

- **Portfolio** — the set of programs/projects an organization funds to
  achieve strategy; managed *collectively* (PMBOK 7 vocabulary).
- **Program** — related projects managed together for benefits unavailable
  from managing them separately.
- **Project / operations** — as in L01; operations sit *outside* the portfolio.
- **Weighted scoring model** — criteria × weights × scores, summed; a
  decision-support device, not a decision machine.
- **Stage gate** — a scheduled decision point where a named body reviews
  evidence and authorizes continued investment.
- **Benefits realization** — ensuring promised value actually appears after
  delivery (deep-dives in L29).

## Practical examples

**CS:** the university IT portfolio — student portal rewrite, classroom
scheduling optimization, network upgrade, research-computing onboarding.
Which is a program? (Portal + identity system + help-desk revamp = program:
shared benefits, interdependencies.)

**DS:** a telecom data-science portfolio — churn model, network-failure
prediction, marketing uplift testing, fraud detection. Discussion: fraud
detection carries regulatory weight; uplift is experimental — the portfolio
should *balance* horizons, not only maximize expected value.

## Worked example

**Weighted scoring (board computation):**

Criteria and weights (sum = 100): strategic fit 40, feasibility 30,
benefit size 30. Candidates scored 1–5:

| Candidate | Fit (40) | Feasibility (30) | Benefit (30) | Weighted total |
|---|---|---|---|---|
| A — registration rewrite | 4 | 3 | 4 | 0.4·4 + 0.3·3 + 0.3·4 = **3.7** |
| B — scheduling optimizer | 3 | 2 | 5 | 1.2 + 0.6 + 1.5 = **3.3** |
| C — portal accessibility | 5 | 4 | 2 | 2.0 + 1.2 + 0.6 = **3.8** |
| D — campus social app | 2 | 4 | 1 | 0.8 + 1.2 + 0.3 = **2.3** |

Budget funds two. Cut line falls between C (3.8) / A (3.7) and B (3.3).
Then perturb: raise "benefit" weight to 50 and B jumps to 3.7 — the decision
flips. **Lesson:** the cut line is a strategy statement; defend weights, not
just scores. Note the weakness this model hides: it says nothing about
*interdependency* (A and C may share the same identity-system work — a program
lens, not a scorecard lens).

## Common misconceptions

| Misconception | Correction |
|---|---|
| "Higher score = fund it." | Scores encode debatable weights; the *debate* is the governance. Interdependencies can override ranks. |
| "Portfolio management is big-company bureaucracy." | Any team choosing among five side projects is doing portfolio management. |
| "Program = big project." | A program manages *multiple* projects for shared benefits; size is not the criterion. |
| "Once funded, a project stays funded." | Gates exist to stop work; killing early is success, not failure. |

## Classroom activities

1. **CS-03 cut-line negotiation (30 min):** teams score six candidates, then
   two teams must agree a joint cut line with different weight sheets — the
   negotiation is the point.
2. **Portfolio or not? (10 min):** classify nine one-liners as
   project/program/portfolio/operations.
3. **Weight critique (10 min):** give a scorecard that always favors legacy
   work (CS-97's setup); teams find the bias in the weights.

## Discussion questions

1. Who at the university should own the cut line — and what happens to projects one point below it?
2. How would you detect that your scoring weights are wrong *before* funding follows them?
3. What evidence would convince you to kill a project your team loves?

## Practical exercise

**In class, then finish at home (CS-03 deliverable):** produce the scorecard
plus a 200-word funding recommendation addressed to the CIO, including one
paragraph on what the recommendation *cannot* see (interdependencies, risks,
people). Homework lane: CS-95 rebalancing memo is portfolio-eligible for
analysis.

## Formative assessment (exit ticket)

1. Portfolio vs program in one sentence each.
2. If weights change and the decision flips, is the model broken? Why not?
3. One thing a scorecard cannot tell the funding committee.

## Reading & references

- PMI. (2021). *PMBOK Guide* (7th ed.) — portfolio/program vocabulary.
- ISO 21502:2020 — governance vocabulary for stage gates and sponsorship.
- [Templates: value scorecard skeleton](../../../docs/resources/templates.md).

## Two-hour teaching plan

| Slot | Segment | Materials |
|---|---|---|
| 0:00–0:08 | Hook: "who decides what gets funded here?" | — |
| 0:08–0:28 | Definitions: portfolio/program/project/operations | classification examples |
| 0:28–0:50 | Worked example: weighted scoring + weight perturbation | board computation |
| 0:50–1:00 | Break | |
| 1:00–1:30 | CS-03 negotiation in teams | CS-03 briefs |
| 1:30–1:45 | Debrief: weights as strategy; kill criteria | team cut lines |
| 1:45–1:55 | CS-97 weight-bias critique plenary | critique sheet |
| 1:55–2:00 | Exit ticket | slips |

## Instructor preparation notes

- Pre-build the scoring spreadsheet with the four worked candidates and a
  blank row per team; verify the perturbation math before class.
- Decide whether CS-95 runs as homework or in-class depending on pace.
- Review CS-03/CS-95/CS-97 facilitation notes in the answer keys area.

## Linked resources

- Lecture skeleton: [`docs/lectures/L02`](../../../docs/lectures/L02-02-strategy-portfolio.md)
- Case: [CS-03](../../../docs/cases/CS-03.md); homework-lane case CS-95 (LMS)
- Template: [value scorecard](../../../docs/resources/templates.md)
- Forward links: [charter lecture L06](../../../docs/lectures/L06-06-charter.md) · benefits (L29) in [detailed syllabus](../../../docs/syllabus/detailed-syllabus.md)
