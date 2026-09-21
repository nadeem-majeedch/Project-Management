# Lecture 22 — Kanban, Flow & Throughput

> **Package for:** L22 · Week 11 · Unit U5 · CLO5 · Bloom: Apply
> **Case anchor:** CS-30 (WIP limits as throttles)
> Companion: [`L22` skeleton](../../../docs/lectures/L22-22-kanban-flow.md) · [CS-30 brief](../../../docs/cases/CS-30.md)

## Learning objectives

1. Apply the Kanban method's practices: visualize, limit WIP, manage flow, explicit policies, feedback loops, improve.
2. Compute and interpret lead time, cycle time, throughput — and read a cumulative flow diagram.
3. Use Little's Law to connect WIP, throughput, and cycle time quantitatively.
4. Choose Scrum vs Kanban for a given work context with criteria.

## Required prior knowledge

- L10/L21 (velocity as forecast; sprint cadence) — today's flow metrics are
  the alternative forecasting engine.
- Comfort with percentiles (program statistics prerequisite).

## Teaching notes

Kanban is the data scientist's native method — it *is* queueing statistics —
and the lecture's arithmetic core reflects that: Little's Law done honestly,
cycle-time percentiles computed from real card history. But the conceptual
hill is **WIP as the control variable**: students believe speed comes from
starting work; flow teaches speed comes from *finishing* it. The CS-30
simulation (with/without WIP limits) delivers that viscerally — run it before
the formulas, so the math explains an experience rather than replacing one.

Second spine: Scrum vs Kanban is not a religion contest but a **cadence and
interrupt-profile decision**. Sprint cadence buys planning rhythm and focus;
flow buys interrupt tolerance and continuous delivery. Ops/support-heavy work
and data-pipeline queues usually fit flow; feature-product work with fixed
stakeholder cadences fits sprints. Give criteria, not verdicts.

## Definitions & concepts

- **Kanban method practices** — visualize the workflow; limit WIP; manage
  flow; make policies explicit; implement feedback loops; improve
  collaboratively.
- **Lead time** — request → delivery (customer clock). **Cycle time** — work
  start → finish (team clock). **Throughput** — items finished per unit time.
- **Little's Law** — `L = λ × W`: average WIP = throughput × average cycle
  time. Control WIP → change cycle time at fixed throughput.
- **CFD (cumulative flow diagram)** — arrivals vs departures bands; widening
  bands = aging work; flat departure = blocked flow.
- **Percentile forecasting** — "85% of items finish in ≤ X days" from card
  history — the flow-native replacement for velocity.

## Practical examples

**CS:** a maintenance/support team drowned in "urgent" — board with explicit
columns (Ready/Build/Review/Verify/Done), WIP limits (Build 2, Review 2),
pull policy ("finish over start"). Compare: sprint model kept failing on
interrupt volume; flow absorbs interrupts at explicit expedite lanes.

**DS:** the feature pipeline as a kanban — columns = ingest → validate →
featurize → train → gate → deploy; WIP limit on *train* = one experiment per
data scientist (GPU queue is the physical WIP limit!); cycle-time percentiles
drive the retraining SLA ("90% of retraining cycles complete in ≤ 3 days").
The expedite lane = incident model fixes.

## Worked example

**Little's Law + percentile forecasting (board, full arithmetic):**

Card history (last 6 weeks, 46 cards finished):

- Throughput λ = 46/30 working days ≈ **1.53 items/day**
- Average WIP observed L ≈ 7.2 items → implied cycle time W = L/λ = 7.2/1.53
  ≈ **4.7 days**
- Percentiles from the same history: p50 = 3 d, p85 = **9 d**, p95 = 14 d.

**Intervention arithmetic:** the team cuts WIP limit from 7 to 4 (and stops
starting under pressure): assume throughput holds ~1.5/day (same people, same
work) → W = 4/1.5 ≈ **2.7 days** average — but the *honest* effect is less
mean and much *less variance* (context switching drops); the p95 tail shrinks
more than the mean. State the caveat like a statistician: Little's Law is an
identity for *steady-state averages* — it predicts the direction and rough
size of the trade, not a guaranteed value; the follow-up measurement (2 weeks
of new history) is part of the intervention.

Forecast use: "24 feature requests in the backlog" → at 1.5/day ≈ 16 working
days to clear; report as "85% of similar items finish ≤ 9 days" per item, and
backlog-clears-by from throughput — never promise the mean.

## Common misconceptions

| Misconception | Correction |
|---|---|
| "Kanban = a board with sticky notes." | The board visualizes; the *method* is WIP limits + policies + feedback. A board without WIP limits is a wall of anxiety. |
| "WIP limits slow us down." | They trade utilization theater for finish-rate; the simulation shows cycle time *improves*. |
| "Little's Law gives exact predictions." | It is a steady-state identity connecting averages; use it for direction + magnitude of trades, then measure. |
| "Throughput = velocity in disguise." | Velocity sums *estimates* of planned scope per sprint; throughput counts *finished items* per day — different units, different failure modes. |
| "Flow work needs no goals." | Flow systems still set service expectations (SLOs) and improvement goals — cadence-less ≠ aimless. |

## Classroom activities

1. **CS-30 simulation (35 min):** paper-based pull system, two rounds (no
   limits vs WIP-limited); teams record cycle times; debrief computes
   Little's Law on their own round data.
2. **CFD reading clinic (15 min):** three pre-drawn CFDs (healthy, aging,
   blocked); teams diagnose and prescribe.
3. **Method-choice tribunal (15 min):** four work contexts (ops team, feature
   squad, ML pipeline, compliance project); teams argue Scrum/Kanban/hybrid
   with criteria.

## Discussion questions

1. What is the *real* WIP limit on your capstone's data work — and is it explicit or accidental (GPU queue, one senior reviewer)?
2. Your p95 cycle time is 14 days but stakeholders expect 3. Which conversation fixes it: expectation, WIP, or staffing? What arithmetic supports each?
3. When does a Scrum team legitimately add an expedite lane — and what policy keeps it from becoming the main lane?

## Practical exercise

**In class:** CS-30 deliverable (simulation results + flow conclusions).
**Take home (25 min):** instrument your capstone board: define columns,
policies, and WIP limits; after one week, compute throughput and cycle-time
percentiles from your own history (≥ 12 cards) — the L24 scaling session
consumes this data.

## Formative assessment (exit ticket)

1. Little's Law — write it and name each variable's unit.
2. Lead vs cycle time — one sentence.
3. Your CFD's arrival band widens while departures stay flat. Diagnosis?

## Reading & references

- Womack & Jones. (1996). *Lean Thinking* — flow/queue foundations
  ([textbooks page](../../../docs/syllabus/textbooks.md)).
- Anderson, *Kanban* — optional deepening (library), referenced for the
  method's practices.
- [Lab 10 brief](../../../docs/labs/index.md) — flow metrics artifact.

## Two-hour teaching plan

| Slot | Segment | Materials |
|---|---|---|
| 0:00–0:10 | Hook: start everything, finish nothing (the simulation tease) | — |
| 0:10–0:28 | Method practices; lead/cycle/throughput; CFD anatomy | board |
| 0:28–0:50 | Worked example: Little's Law + percentiles + intervention | board arithmetic |
| 0:50–1:00 | Break | |
| 1:00–1:35 | CS-30 simulation rounds + debrief | sim kits |
| 1:35–1:50 | CFD clinic + method tribunal | CFD handouts |
| 1:50–1:57 | Capstone board instrumentation briefing | — |
| 1:57–2:00 | Exit ticket | slips |

## Instructor preparation notes

- Print CS-30 sim kits (cards, column tents, WIP tokens) ×8 teams; test the
  round timings once — round 2 must be *visibly* faster to land the lesson.
- Pre-draw the three CFDs; the "blocked" one has the departure flatline in the
  Review column (review WIP limit is the prescribed fix).
- Team board-tooling check: confirm every capstone team can instrument their
  board this week (process-evidence pipeline depends on it).

## Linked resources

- Lecture skeleton: [`docs/lectures/L22`](../../../docs/lectures/L22-22-kanban-flow.md)
- Case: [CS-30](../../../docs/cases/CS-30.md) · Lab 10: [labs index](../../../docs/labs/index.md)
- Forward: [ML sprints L23](../../../docs/lectures/L23-23-agile-data-ml.md)
  (flow mechanics inside data work) · [scaling L24](../../../docs/lectures/L24-24-scaling-hybrid.md)
  (dependency boards are flow systems at program scale).
