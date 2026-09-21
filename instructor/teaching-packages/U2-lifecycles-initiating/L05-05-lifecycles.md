# Lecture 05 — Life Cycles: Predictive, Adaptive, Hybrid

> **Package for:** L05 · Week 3 · Unit U2 · CLO1, CLO5 · Bloom: Understand
> **Case anchors:** CS-06 (five vignettes), CS-07 (hybrid for a regulated data product)
> Companion: [`L05` skeleton](../../../docs/lectures/L05-05-lifecycles.md) · [CS-06](../../../docs/cases/CS-06.md) · [CS-07](../../../docs/cases/CS-07.md)

## Learning objectives

1. Distinguish predictive, iterative, incremental, adaptive, and hybrid life cycles.
2. Choose a development approach for a project vignette using at least three explicit criteria.
3. Sketch a hybrid structure (predictive wrapper, adaptive core, or gated agile) and name its trade-offs.
4. Explain why the life-cycle choice precedes and constrains planning choices.

## Required prior knowledge

- L03 domains (development approach & life cycle domain).
- L01 failure modes (why the wrong cycle hurts).

## Teaching notes

The conceptual hill: **uncertainty chooses the cycle, not fashion.** Students
arrive with the folk belief that "agile is modern and waterfall is failed."
Reframe from the first ten minutes: a regulatory migration with a fixed
external date and known requirements is *safer* predictive; a startup MVP is
*safer* adaptive. Wrong-cycle failures are real and common in both directions.

Use the Stacey matrix as the shared language: agreement on *what* (requirements
certainty) × agreement on *how* (technical certainty). Then run the five
vignettes (CS-06) as the decision gym. CS-07 deepens into hybrid design where
compliance gates wrap sprints — foreshadow the regulated-data theme that
returns in L23/L28.

This lecture starts the course's Apply-turn: from here on, choices must be
*defended with criteria*, not taste.

## Definitions & concepts

- **Predictive (plan-driven)** — scope fixed early; phases gate the work;
  value delivered at the end. Control-heavy, feedback-light.
- **Iterative** — repeat cycles to refine *one* understanding (prototype
  loops); scope still largely fixed, understanding improves.
- **Incremental** — output delivered in usable slices; each slice adds
  value.
- **Adaptive** — short cycles, evolving scope, outcome-driven backlogs
  (Scrum/Kanban live here — L21/L22).
- **Hybrid** — deliberate mixture: predictive wrapper + adaptive core,
  phase-gated agile, adaptive discovery + predictive rollout.
- **Stacey axes** — requirements certainty × technical certainty.
- **Requirements volatility** — expected rate of legitimate requirement
  change over the project horizon.

## Practical examples

**CS:** payroll replacement with statutory reports (predictive — fixed scope,
fixed legal date) vs a student-feedback analytics dashboard (incremental —
each dashboard ships value) vs a campus-app startup MVP (adaptive).

**DS:** a medication-reconciliation platform (MEDSYNC) mixing a predictable
ingestion core (predictive, versioned interfaces) with exploratory model work
(adaptive discovery spikes) — the classic DS hybrid; contrast a fixed-scope
legacy-data migration to a regulated warehouse (predictive, audit trail
dominates).

## Worked example

**Choosing via criteria (board decision, three criteria scored):**

Vignette: *"TelcoCare wants a churn-reduction product; the data exists but
unverified; the business will accept three quarterly releases; regulators
require model documentation."*

| Criterion | Signal | Points to |
|---|---|---|
| Requirements volatility | high (product shape unknown) | adaptive |
| Regulatory exposure | high (documentation gates) | predictive wrapper |
| Feedback cadence | quarterly acceptable | incremental delivery inside |

Decision: **hybrid** — discovery sprints for data/model work (adaptive),
quarterly release gates with fixed documentation evidence (predictive);
regulatory gate owns go/no-go. Then the trade-off talk: the wrapper slows the
core (compliance evidence takes real sprint capacity — budget it, ~15–20%).
That honesty — hybrids pay a tax — separates mature answers from buzzwords.

## Common misconceptions

| Misconception | Correction |
|---|---|
| "Waterfall is always the bad old way." | With stable, regulated, safety-critical scope, predictive control is the *safer* choice. |
| "Agile means no documentation." | Adaptive cycles still produce the evidence the domain requires — just just-in-time and proportionate (tailoring, L08). |
| "Hybrid is a cop-out / the worst of both." | A *designed* hybrid assigns each workstream the cycle that fits it; the tax is managed, not suffered. |
| "Iterative and incremental are synonyms." | Iteration refines understanding; increment delivers usable value — orthogonal, combinable. |

## Classroom activities

1. **CS-06 vignette gauntlet (35 min):** five vignettes, teams commit to a
   cycle each with three-criteria defense; votes conflict deliberately.
2. **CS-07 hybrid sketch (25 min):** draw the phase/sprint diagram with gates
   and audit checkpoints for MEDSYNC.
3. **Stacey placement (10 min):** plot eight course-seed projects on the
   matrix; defend quadrant edges.

## Discussion questions

1. Your sponsor mandates "agile" for the payroll replacement. What do you do? (Dialogue rehearsal — options and consequences.)
2. Which axis of the Stacey matrix is harder to assess honestly in a data project — what or how?
3. What early evidence would tell you the chosen cycle is wrong, and by when?

## Practical exercise

**In class (CS-06 deliverable):** completed choice matrix. **Take home
(20 min):** pick one team project idea for the capstone (teams form at L08)
and write its three-criteria life-cycle argument — this becomes raw material
for the L08 team charter.

## Formative assessment (exit ticket)

1. Which cycle for: fixed regulatory date, known scope, no feedback needed?
2. One *cost* of hybrid delivery.
3. Name the two Stacey axes.

## Reading & references

- PMI. (2021). *PMBOK Guide* (7th ed.) — Development Approach & Life Cycle
  Performance Domain chapter.
- Agile Manifesto (2001) — values, for the adaptive side of the spectrum.
- Fowler, M. *The New Methodology* (martinfowler.com) — background on
  method choice by volatility; check the current revision date when citing.

## Two-hour teaching plan

| Slot | Segment | Materials |
|---|---|---|
| 0:00–0:10 | Hook: "mandated agile" story | — |
| 0:10–0:30 | Spectrum definitions; Stacey matrix | matrix handout |
| 0:30–0:50 | Worked example: hybrid decision with criteria | board decision table |
| 0:50–1:00 | Break | |
| 1:00–1:35 | CS-06 gauntlet (5 vignettes × defense) | vignette cards |
| 1:35–1:55 | CS-07 hybrid sketch + gallery walk | flipcharts |
| 1:55–2:00 | Exit ticket | slips |

## Instructor preparation notes

- Prepare the five vignettes on separate cards with *conflicting* signals so
  team answers genuinely diverge.
- Pre-draw the Stacey matrix large on a board or wall for the placement drill.
- Note which teams choose predictive for vignette 3 — probe their reasoning in
  debrief; the trap is reflexive adaptive bias.

## Linked resources

- Lecture skeleton: [`docs/lectures/L05`](../../../docs/lectures/L05-05-lifecycles.md)
- Cases: [CS-06](../../../docs/cases/CS-06.md) · [CS-07](../../../docs/cases/CS-07.md)
- Forward: [Scrum L21](../../../docs/lectures/L21-21-scrum.md) ·
  [tailoring L08](../../../docs/lectures/L08-08-tailoring.md)
- Detailed syllabus: [KA-METHODS row](../../../docs/syllabus/detailed-syllabus.md)
