# Lecture 13 — Cost Estimating & Budgeting

> **Package for:** L13 · Week 7 · Unit U3 · CLO3 · Bloom: Apply
> **Case anchor:** CS-17 (bottom-up budget for GRIDSENSE)
> Companion: [`L13` skeleton](../../../docs/lectures/L13-13-cost-budget.md) · [CS-17 brief](../../../docs/cases/CS-17.md)

## Learning objectives

1. Build a bottom-up cost estimate from work-package effort + rates + direct costs.
2. Assemble a time-phased budget (S-curve) with contingency vs management reserve separated.
3. Reconcile a budget with funding limits (annual caps).
4. Name the cost realities that make data projects misbehave (compute, storage, price volatility).

## Required prior knowledge

- L10 effort estimates (hours); L12 levelled schedule (the time phasing).
- Percent/decimal arithmetic — nothing heavier.

## Teaching notes

Cost is where scope becomes real. The teaching spine: **cost = effort × rate +
direct costs, then time-phase it, then protect it with two *different* kinds
of money.** The contingency/management-reserve distinction is the concept
students most often blur: contingency is *yours* (identified risks, PM
controls, visible in the S-curve); management reserve is the *sponsor's*
(unidentified risk, change control to access). Conflating them hides either
overspending or insufficient buffers.

The second spine is data-project cost realism: cloud spend behaves like a
utility bill with feedback loops — training runs, storage growth, egress
fees. Students routinely cost people and forget the machine. CS-17 is built on
GRIDSENSE precisely to force compute into the open.

Time-phasing needs the *schedule* (L12) not just totals — show the same 940 h
becoming two different S-curves depending on sequencing; cost and schedule are
one system, not two documents (the integrative theme the midterm probes).

## Definitions & concepts

- **Direct vs indirect costs** — billed to the project vs shared overhead
  (applied as a rate).
- **Fixed vs variable** — licenses vs compute-hours (DS: the variable half
  dominates and is *usage*-sensitive).
- **Bottom-up estimate** — Σ over work packages: effort × rate + direct costs.
- **Contingency reserve** — for *identified* risks; derived (L16 shows a
  simulation-driven derivation), visible in the cost baseline.
- **Management reserve** — for *unknown* risk; held above the baseline;
  accessed via change control.
- **Cost baseline** — time-phased budget = S-curve (cumulative spend plan).
- **Funding-limit reconciliation** — smooth spend against fiscal-year caps
  (or re-plan).

## Practical examples

**CS:** CampusHub — 5 developers × 4.5 months + 1 designer (2 months part-
time) + licenses (monitoring tool) + training material production; overhead
at 60% of labor.

**DS:** GRIDSENSE — same labor math *plus*: training-cluster hours (GPU),
storage growth (telemetry retention), egress for stakeholder reporting
extracts, and a price-volatility allowance. The volatility allowance is the
honest response to cloud pricing — a small, named contingency sub-line, not
silent padding.

## Worked example

**Bottom-up budget + S-curve (board, full arithmetic):**

Assumptions: blended developer rate **$45/h**; data engineer **$50/h**;
overhead 60% of labor; contingency from risk analysis = **10% of baseline**
(L16 will derive it properly); management reserve = 5% (sponsor-held, *not*
in the baseline).

**Labor (from L09/L10 package estimates):**

| Role | Hours | Rate | Cost |
|---|---|---|---|
| Developers (3 × 280 h) | 840 | $45 | $37,800 |
| Data engineer | 200 | $50 | $10,000 |
| PM (15% of team effort ≈ 155 h) | 155 | $45 | $6,975 |
| **Labor subtotal** | | | **$54,775** |

**Direct costs:** monitoring tool license $2,400; GPU cluster 120 h × $2.20 =
$264; storage 4 TB × $0.023/GB-month ≈ $92/mo × 9 mo = **$828**; egress
allowance $300. **Direct subtotal = $3,792.**

**Baseline build:**
- Labor + direct = 54,775 + 3,792 = **$58,567**
- Contingency 10% = **$5,857** → **cost baseline = $64,424**
- Management reserve 5% = $3,221 → **total funding ask = $67,645**

**Time-phasing to the S-curve** (from the levelled schedule; approx
months 1–9):

| Month | Planned spend ($) | Cumulative ($) |
|---|---|---|
| 1 | 4,200 | 4,200 |
| 2 | 5,400 | 9,600 |
| 3 | 7,800 | 17,400 |
| 4 | 9,200 | 26,600 |
| 5 | 9,200 | 35,800 |
| 6 | 9,400 | 45,200 |
| 7 | 8,600 | 53,800 |
| 8 | 6,400 | 60,200 |
| 9 | 4,224 | **64,424** ✓ |

Shape lesson: slow start (staffing ramp), hump (parallel build), flat tail
(hardening/closure). Ask what a *straight line* would imply — nobody staffs
that way. Then the fiscal-year twist: if funding caps at $30k/fiscal year and
the plan crosses April 1 at month 7 cumulative $53.8k → the year-2 slice is
$34.4k > $30k cap. Options: shift the last $4.4k of discretionary work
(documentation polish) earlier/defer it, or request cap relief. **The S-curve
is a negotiation instrument, not just a drawing.**

## Common misconceptions

| Misconception | Correction |
|---|---|
| "Contingency is slush; cut it to look lean." | Removing identified-risk funding just moves the risk to the reserve conversation (or the failure report). Size it from risk, defend it, own it. |
| "Compute costs are rounding errors." | On data projects they are a first-class line with usage feedback loops; unmonitored GPU spend is the classic overrun (CS-57). |
| "The budget is the estimate." | The estimate is what it *should* cost; the baseline is when/where it is *planned* to spend; reserves sit differently — three artifacts. |
| "Management reserve is mine to spend." | It is the sponsor's; spending it is a change decision, not a PM discretion. |

## Classroom activities

1. **CS-17 budget build (35 min):** teams produce the full GRIDSENSE budget
   with a labor table, direct-cost table, contingency rationale, and S-curve
   sketch; compute totals to the dollar.
2. **Cost-type sorting (10 min):** 12 cost items → direct/indirect ×
   fixed/variable grid; the egress-fee corner generates good arguments.
3. **Funding-cap reconciliation (10 min):** re-slice the worked example under
   the $30k cap; teams propose the least-damage re-plan.

## Discussion questions

1. Where should cloud price volatility live: contingency, a named sub-line, or the management reserve? Defend with control consequences.
2. Your sponsor says "10% contingency is fear; 5%." What evidence changes their mind — and what if the evidence is L16's simulation? (Forward hook.)
3. What does the S-curve of a *data* project look like when the compute hump lands in month 6 — and what risk does that timing carry?

## Practical exercise

**In class:** CS-17 deliverable (budget + S-curve). **Take home (30 min, feeds
the capstone):** cost the *team's* project bottom-up (labor + direct +
contingency separated), sketch the S-curve, and write the one-paragraph
contingency defense. This becomes the capstone cost baseline section (L27
assembles it).

## Formative assessment (exit ticket)

1. Contingency vs management reserve — who controls each, and for what?
2. Baseline build: labor $50,000, direct $5,000, contingency 10% — what is the cost baseline? ($60,500.)
3. Name two cost lines a data project has that a CS project usually doesn't.

## Reading & references

- PMI. (2021). *PMBOK Guide* (7th ed.) — Planning domain (cost estimation,
  budgeting, reserves) and Measurement domain (cost variance — forward link
  to L19).
- [Lab 6 brief](../../../docs/labs/index.md) — cost baseline artifact.
- [Case CS-57](../../../docs/cases/index.md) (homework lane) — cloud overrun
  tracing; pairs with today's volatility sub-line.

## Two-hour teaching plan

| Slot | Segment | Materials |
|---|---|---|
| 0:00–0:10 | Hook: the GPU bill that outgrew the payroll | — |
| 0:10–0:28 | Cost families; bottom-up build; reserves doctrine | board tables |
| 0:28–0:50 | Worked example: budget → S-curve → funding-cap reconciliation | board arithmetic |
| 0:50–1:00 | Break | |
| 1:00–1:35 | CS-17 team budget build | CS-17 brief |
| 1:35–1:50 | Sorting + cap reconciliation drills | item cards |
| 1:50–1:57 | Capstone cost-baseline homework briefing | — |
| 1:57–2:00 | Exit ticket | slips |

## Instructor preparation notes

- Verify all arithmetic on the worked example *twice*; public math errors in
  a costing lecture are memorable (the wrong way).
- Print the 12 cost-type cards; egress and license-vs-build items spark the
  best arguments.
- CS-17 rates are given in the brief — teams must not invent market rates;
  the *structure* is the deliverable.

## Linked resources

- Lecture skeleton: [`docs/lectures/L13`](../../../docs/lectures/L13-13-cost-budget.md)
- Case: [CS-17](../../../docs/cases/CS-17.md) · Lab 6: [labs index](../../../docs/labs/index.md)
- Forward: [EVM L19](../../../docs/lectures/L19-19-evm.md) consumes the
  baseline's PV · [Monte Carlo L16](../../../docs/lectures/L16-16-quant-risk-simulation.md)
  derives the contingency properly.
