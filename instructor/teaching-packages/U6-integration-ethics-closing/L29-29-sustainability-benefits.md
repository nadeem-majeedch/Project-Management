# Lecture 29 — Sustainability & Benefits Realization

> **Package for:** L29 · Week 15 · Unit U6 · CLO6 · Bloom: Evaluate
> **Case anchor:** CS-40 (benefits map + compute footprint)
> Companion: [`L29` skeleton](../../../docs/lectures/L29-29-sustainability-benefits.md) · [CS-40 brief](../../../docs/cases/CS-40.md)

## Learning objectives

1. Build a benefits map linking deliverables → outcomes → benefits → strategic intent, with owners and measures.
2. Distinguish outputs from outcomes from benefits — and audit a "benefits shortfall" case.
3. Estimate a data project's compute footprint and apply a reduction decision with trade-offs.
4. Design an operations-handover package that survives the project team's dissolution.

## Required prior knowledge

- L06 (the charter's benefit claims — today's audit target), L02 (portfolio
  intent), L23 (model monitoring — the operations half).

## Teaching notes

Mostly non-quantitative, with two honest numbers sessions: the benefits map
(structured, no math) and a **back-of-envelope footprint estimate** (simple
arithmetic, honestly caveated — the teaching point is the *decision* the
estimate feeds, not decimal precision).

The conceptual hill: **projects deliver outputs; organizations bank
benefits.** Students conflate "we shipped the model" with "retention
improved." The benefits map forces the chain: deliverable (scoring service) →
outcome (targeted offers reach the right customers) → benefit (churn
reduction vs the do-nothing baseline, measured by finance, owned by a name)
→ intent (portfolio strategy from L02). The 12-months-later shortfall audit
(CS-104 homework lane) shows what happens when the chain is never measured.

Sustainability gets the DS treatment: compute is a real, measurable
environmental and budget line; the estimate session quantifies a training
program and asks a genuine trade — accuracy vs footprint — which is also an
*ethics* decision (who consents to the footprint: the team, the sponsor, the
planet? links to L28).

## Definitions & concepts

- **Output / outcome / benefit** — artifact produced / change in
  organizational behavior or state / measurable improvement vs baseline.
- **Benefits map** — the causal chain with owner + measure + timing per
  benefit; the audit instrument for CS-104-style shortfalls.
- **Benefit owner** — the *business* name accountable for the benefit landing
  after handover (never the PM).
- **Benefits realization plan** — when and how each benefit is measured
  post-project (the charter's claims, scheduled).
- **Sustainability lenses** — environmental, social, economic (triple
  bottom line vocabulary) applied to delivery choices.
- **Operations handover** — support model, runbooks, knowledge transfer,
  access & license transitions, monitoring acceptance; the project's *exit*
  from the product's life.

## Practical examples

**CS:** portal benefits map — deliverable: self-service registration;
outcome: advisors stop manual enrollment fixes; benefit: advising hours
reclaimed (finance-measured), owner: registrar; measurement: hours logged in
the advising system, baseline vs post-term. The shortfall audit: 12 months
later, hours *not* reclaimed — because the manual workaround persisted
(adoption was never an outcome owner's job). Lesson: the missing map row.

**DS:** churn-model benefits chain — scoring service (output) → offers
targeted to top-decile (outcome) → churn −8% vs control in a 6-week holdout
(benefit; owner: retention director; measure: control-group design). The
footprint estimate: monthly retraining at 120 GPU-hours × 12 months ≈ 1,440
GPU-h/yr; at ~0.4 kWh/GPU-h ≈ 576 kWh; converted with the operator's published
energy-mix factor — the *number matters less than the decision*: a bigger
model promises +0.5 pt lift for +40% compute. Who decides? The sponsor, with
the footprint line shown — sustainability as a governance-visible trade, not
an engineer's private conscience.

## Worked example

**Benefits map (board, full table):**

| Deliverable | Outcome | Benefit | Owner | Measure | When measured |
|---|---|---|---|---|---|
| Scoring service | Offers reach top-decile | Retention campaign conversion ↑ | Retention director | Lift vs control, 6-wk holdout | Q3 + quarterly |
| Playbook + training | Call center uses model output | Handle-time on churn calls ↓ 20% | Ops lead | Call system logs, vs baseline month | Q4 |
| Fairness report | Offers pass equity review | Regulatory readiness | Model risk owner | Review passed, documented | At each gate |

Then the audit question that kills weak maps: *which row has no owner in the
business?* (Playbook row usually dies — training delivered ≠ behavior
changed.) Repair: adoption metric + ops owner, added before handover.

**Footprint arithmetic (board):** current: 120 GPU-h/mo × 12 = 1,440 h/yr.
Option B (+40% compute): 2,016 h/yr → Δ576 h/yr ≈ Δ230 kWh/yr (at 0.4 kWh/h)
— then the honest caveats: kWh/GPU-h varies by hardware; energy-mix factors
are regional and published by the operator; the *decision* is relative
(+40%) and budget-linked, with the environmental line shown alongside. The
deliverable is the trade memo: lift +0.5 pt vs +40% compute — and who owns
the yes.

## Common misconceptions

| Misconception | Correction |
|---|---|
| "The project is done at go-live." | Go-live is the *start* of benefit life; closure (L30) formally ends the project, the product's value story continues. |
| "Benefits = deliverables delivered." | Outputs ≠ outcomes ≠ benefits; unmapped chains produce the 12-month shortfall audit's shrug. |
| "The PM owns the benefits." | The PM *enables*; business owners own benefits — otherwise nobody in the line is accountable for them after the team dissolves. |
| "Sustainability is an environmental-only checkbox." | It has social and economic lenses too (team sustainability, price volatility) — the footprint trade is all three at once. |
| "Handover = forwarding the repo link." | Handover is a designed package: runbooks, support model, access, monitoring acceptance, named recipients — otherwise the product decays quietly. |

## Classroom activities

1. **CS-40 benefits map build (30 min):** full table for the churn product;
   owner-or-die audit applied; one row repaired.
2. **Footprint trade memo (20 min):** estimate + trade memo (lift vs compute)
   with the governance question answered: who signs.
3. **Handover package design (20 min):** checklist for the capstone: support
   model, runbook list, access transitions, monitoring acceptance, lessons
   archive.

## Discussion questions

1. Which benefit row in your capstone's map will never be measured — and what would it take to measure it this semester instead of "someday"?
2. Your sponsor wants the +40% compute option but "doesn't want to hear about the footprint." What are your honest options, and which does the L28 protocol recommend?
3. What does your handover package assume about the recipient team that you haven't verified?

## Practical exercise

**In class:** CS-40 deliverables (map + memo). **Take home (25 min, capstone
section):** benefits map + handover checklist for the team's own project —
the last two sections of the master plan (L27 template); sustainability line
added if compute is material.

## Formative assessment (exit ticket)

1. Output → outcome → benefit: place "advising hours reclaimed" and "self-service registration."
2. Who owns a post-project benefit — and in what document is that visible?
3. What three items make a handover package real rather than a link?

## Reading & references

- PMI. (2021). *PMBOK Guide* (7th ed.) — value delivery system; Measurement
  domain (benefits measures).
- PMI. (2017). *PMBOK Guide* (6th ed.) — benefits-management vocabulary in
  the program context.
- [Capstone rubric](../../../docs/capstone/capstone-rubric.md) — the
  benefits/handover rows the defense touches.

## Two-hour teaching plan

| Slot | Segment | Materials |
|---|---|---|
| 0:00–0:10 | Hook: the system that shipped and changed nothing (CS-104 teaser) | — |
| 0:10–0:28 | Output/outcome/benefit; the map's anatomy; ownership doctrine | board |
| 0:28–0:50 | Worked examples: benefits map + footprint trade memo | board tables |
| 0:50–1:00 | Break | |
| 1:00–1:30 | CS-40 map build + owner audit | CS-40 brief |
| 1:30–1:50 | Footprint memo + handover checklist | template sheets |
| 1:55–2:00 | Exit ticket | slips |

## Instructor preparation notes

- Keep footprint factors explicitly caveated (hardware/region variance) —
  the teaching goal is the *governance-visible trade*, and model honesty is
  part of the lesson.
- Benefits map template pre-printed with the owner-or-die audit row.
- Collect the take-home next week (L30) — it completes teams' master-plan
  sections before sign-off.

## Linked resources

- Lecture skeleton: [`docs/lectures/L29`](../../../docs/lectures/L29-29-sustainability-benefits.md)
- Case: [CS-40](../../../docs/cases/CS-40.md) · CS-104 (homework lane — shortfall audit, [case directory](../../../docs/cases/index.md))
- Forward: [closure L30](../../../docs/lectures/L30-30-closure-lessons.md) ·
  [defense format](../../../docs/capstone/defense-format.md) (benefits in
  the 10-minute outline).
