# Lecture 12 — Schedules, Gantt Charts & Resource Levelling

> **Package for:** L12 · Week 6 · Unit U3 · CLO2 · Bloom: Apply · **Quiz 2 today (L09–L12)**
> **Case anchor:** CS-16 (Gantt baseline + levelling)
> Companion: [`L12` skeleton](../../../docs/lectures/L12-12-schedule-tools.md) · [CS-16 brief](../../../docs/cases/CS-16.md)

## Learning objectives

1. Translate a CPM network into a baselined Gantt with milestones.
2. Detect resource overallocation and level a schedule time-constrained (moving work into float).
3. Distinguish levelling (extend/absorb) from smoothing (within float) — and the cost each hides.
4. Run schedule-quality checks (logic completeness, constraint abuse, long durations — DCMA-style heuristics).

## Required prior knowledge

- L11 network + floats (today consumes them directly).
- Basic Gantt familiarity from any prior project course.

## Teaching notes

The Gantt is the *communication* face of the network — students can already
draw bars; what they lack is the discipline underneath: **the baseline is a
promise record, and levelling is a trade, not a cleanup.** Keep the lecture
tool-light (any tool works; principles transfer) and trade-heavy.

Run **Quiz 2 (15 min)** first (estimation + network items). Then the
mechanics: network → Gantt (bars inherit logic, not aesthetics), milestones as
zero-duration *commitments*, baseline = snapshot taken once. The worked
example is a levelling computation: a 200%-loaded engineer becomes a
time-feasible plan by moving non-critical work into float — students compute
*where* it can go and what risk that purchases (float consumption → new
critical risk).

Quality checks close the technical arc: missing predecessors, "start-on-date"
constraints painted over missing logic, 60-day tasks (unmeasurable) — the
DCMA-style heuristics give them a portable audit checklist.

## Definitions & concepts

- **Gantt chart** — time-scaled bar view of scheduled activities; bars inherit
  dependencies from the network.
- **Milestone** — zero-duration commitment point (external date, gate,
  handover); anchor for reporting.
- **Baseline** — the approved schedule snapshot; variance is measured *against
  it*; changed only through control (L20).
- **Resource levelling** — resolve overallocation by moving/lengthening work
  (may extend the project). **Smoothing** — move work only *within free float*
  (end date untouched).
- **Hammock/summary task** — rolled-up grouping; a reporting device, not logic.
- **Schedule quality heuristics** — no missing logic, minimal hard constraints,
  no lags-as-fudge, bounded durations, float respect.

## Practical examples

**CS:** the portal Gantt — UI and engine tracks run parallel; one senior dev
appears on both tracks' review tasks (overallocation); smoothing moves UI
review into its 3-day float. Milestones: *schema freeze* (external), *UAT
start* (gate).

**DS:** streaming-features engineer loaded 150% during ingestion + feature
parallelism (the L11 SS+2lag overlap produced this — name the cause!). Fix by
sequence: pull the monitoring-design task (4 d, 5 d float) after the batch
validation task; note the trade: streaming slips 3 days, absorbing 60% of the
path's buffer — the drift-monitoring design now sits near-critical. Data
projects also *buy hardware time*: training-cluster windows are a resource
with a queue; show the queue as a constraint, not a bar.

## Worked example

**Levelling computation (board):**

Bilal is allocated: Rule format (wk 3, 100%), Engine integration tests
(wk 3–4, 50%), plus a legacy maintenance task (wk 3, 50%) = **200% in week 3**.

| Task | Float | Duration | Move? |
|---|---|---|---|
| Rule format (critical, B-path) | 0 | 1 wk | **No** — moves the end date |
| Integration tests | 2 wk (total), 0 free (successor = milestone) | 2 wk | Shift start wk3→wk5 |
| Maintenance | 3 wk total | 1 wk | Shift wk3→wk6 |

Result: week-3 load = 100% ✓; end date unchanged ✓; **but** integration
tests consumed 2 of 2 float weeks — the C-path (float 2) is now critical.
Risk note recorded: the compression reserve is spent; any slip on tests now
moves the project. That risk note *is* the deliverable of levelling —
unrecorded trades are how plans rot silently.

## Common misconceptions

| Misconception | Correction |
|---|---|
| "The Gantt *is* the schedule." | It is a view; the logic network is the schedule. A Gantt without dependencies is a wish list. |
| "Baseline once, update always." | Update *progress* against the baseline; never edit the baseline to hide drift (that is L20 territory). |
| "Levelling is free." | Every move spends float or money; record the residual risk (the worked example's whole point). |
| "Milestones are just tasks with zero days." | They are commitments (often external); every milestone needs an owner and evidence. |
| "60-day tasks are fine if the work is big." | Long tasks hide trouble; decompose to checkpoints ≤ ~2–4 weeks for measurable progress. |

## Classroom activities

1. **Quiz 2 (15 min).**
2. **CS-16 build & baseline (30 min):** teams create the 10-week Gantt from
   the L11-style data, baseline it, then receive the overallocation twist.
3. **Levelling trade-off memo (20 min):** produce the before/after load table
   + the risk note (worked-example format).
4. **Schedule audit speed-run (10 min):** a deliberately flawed Gantt
   (missing logic ×2, date constraint ×1, one 90-day task); teams list defects
   in 4 minutes.

## Discussion questions

1. Who is allowed to approve spending float in your team — and where is that written?
2. Your smoothed plan consumed most of a near-critical path's buffer. Which monitoring indicator changes first?
3. On a DS project, what kinds of *resources* (not people) constrain the schedule, and how do they appear in a Gantt?

## Practical exercise

**In class:** CS-16 deliverable (baseline + levelled plan + risk note).
**Take home (feeds A2, final section):** baseline the A2 schedule, produce the
resource histogram, resolve overallocations with a recorded trade note per
move. A2 is now complete — submission due after L16; rubric preview on the
[assignment brief](../../../docs/assignments/a1-scope-schedule.md).

## Formative assessment (exit ticket)

1. Levelling vs smoothing — one sentence each.
2. What does a baseline *record*?
3. Name two schedule-quality defects and their fixes.

## Reading & references

- PMI. (2021). *PMBOK Guide* (7th ed.) — Planning domain (schedule models,
  milestones, baselining).
- [Lab 5 brief](../../../docs/labs/index.md) — Gantt + levelling artifact
  (this week's lab runs the same mechanics on the team project).
- [Assignment 1 brief](../../../docs/assignments/a1-scope-schedule.md).

## Two-hour teaching plan

| Slot | Segment | Materials |
|---|---|---|
| 0:00–0:15 | **Quiz 2** (L09–L12) | quiz papers |
| 0:15–0:35 | Network → Gantt; milestones; baselining discipline | tool-agnostic slides |
| 0:35–0:50 | Worked example: levelling with trade record | board table |
| 0:50–1:00 | Break | |
| 1:00–1:30 | CS-16 build & baseline | CS-16 brief |
| 1:30–1:50 | Levelling memo + histogram | template sheet |
| 1:50–1:57 | Schedule audit speed-run | flawed Gantt |
| 1:57–2:00 | Exit ticket | slips |

## Instructor preparation notes

- Quiz 2 papers: 1 mini-network + 2 estimation items (blueprint in the
  [exam bank](../../exam-bank/README.md)).
- Pre-build the flawed Gantt for the audit speed-run; four planted defects is
  the right count for 4 minutes.
- CS-16 needs the overallocation *twist card* distributed only after teams
  baseline — timing discipline is part of the exercise.

## Linked resources

- Lecture skeleton: [`docs/lectures/L12`](../../../docs/lectures/L12-12-schedule-tools.md)
- Case: [CS-16](../../../docs/cases/CS-16.md) · Lab 5: [labs index](../../../docs/labs/index.md)
- Assignment: [A2 brief](../../../docs/assignments/a1-scope-schedule.md)
- Forward: [cost L13](../../../docs/lectures/L13-13-cost-budget.md) — the
  levelled plan becomes the costing input · [change control L20](../../../docs/lectures/L20-20-monitoring-control.md).
