# Lecture 23 — Agile for Data Science & ML Projects

> **Package for:** L23 · Week 12 · Unit U5 · CLO5 · Bloom: Apply
> **Case anchors:** CS-31 (hypothesis-first rewrite), CS-32 (model DoD)
> Companion: [`L23` skeleton](../../../docs/lectures/L23-23-agile-data-ml.md) · [CS-31](../../../docs/cases/CS-31.md) · [CS-32](../../../docs/cases/CS-32.md)

## Learning objectives

1. Explain why vanilla Scrum mechanics mis-fit discovery-heavy data work, and what to adapt.
2. Rewrite a feature-first ML backlog into a hypothesis-driven one with measurable outcomes.
3. Draft a model Definition of Done: metrics, fairness thresholds, monitoring, rollback.
4. Plan data/ML work with uncertainty budgets and pivot/hold/kill reviews.

## Required prior knowledge

- L21/L22 (sprint and flow mechanics — being adapted here), L14 (data-quality
  gates; the model gate concept).
- DS track: their own project-course experience; CS track: cases supply
  context.

## Teaching notes

The honest frame: **Scrum assumes you can define "done" for a slice of
product; discovery work can't always** — a two-week sprint can end with
"the hypothesis died, here's what we learned," and that must count as
delivered *learning*, not as failure. The lecture adapts the mechanics to
that reality instead of pretending the mismatch away: sprints as
*experiment containers*, spikes as first-class citizens, negative results as
increment-worthy.

Backlog quality is the teachable core. Feature-first items ("build churn
model v2", "improve accuracy") are unfalsifiable wishes. Hypothesis-first
items name: the belief being tested, the evidence that would confirm/refute,
the cost of the test, and the decision the test feeds. CS-31's rewrite drill
is the session's center — full worked example below.

The model DoD (CS-32) turns the L14 quality work + L15 risk register into a
*release gate checklist*: performance metrics with thresholds, fairness gaps
with bounds, monitoring hooks wired, rollback rehearsed. This is the DS
spine's keystone artifact and a named capstone section for DS-track teams.

## Definitions & concepts

- **Discovery spikes** — time-boxed experiments with exit criteria; negative
  results are deliverables (learning) when the exit criterion is met.
- **Hypothesis backlog** — items shaped as testable beliefs feeding decisions,
  not features to build.
- **Uncertainty budget** — a planned allowance of discovery capacity per
  sprint (e.g., 25–30% of capacity as spikes until the problem stabilizes).
- **Model Definition of Done** — the gate checklist: metric thresholds,
  fairness bounds, monitoring hooks, rollback plan, documentation (model
  card draft).
- **Pivot/hold/kill review** — a scheduled decision on the *direction*, not
  the sprint: continue, adapt, or stop (the agile answer to sunk cost).
- **CRISP-DM contrast** — business/data/prep/model/eval/deploy phases;
  adaptive delivery overlaps its loops rather than replacing them (the
  [textbooks page](../../../docs/syllabus/textbooks.md) Fountain reference
  maps the full data life cycle).

## Practical examples

**CS-track analog (so CS students engage):** A/B-testing a UI change is the
same shape as a model experiment — hypothesis, metric, guardrails, decision
rule; the backlog item is the *test*, not the button.

**DS (TelcoCare churn):** feature-first backlog items and their hypothesis
rewrites (worked example). Model DoD for the churn model: AUC ≥ 0.80 on
frozen holdout; top-decile lift ≥ 0.25; fairness gap across age bands ≤ 5 pts;
DQ gates green on scoring inputs; monitoring wired (drift score + fairness
trend + latency); rollback = previous model artifact re-deployable in ≤ 30
minutes; model card drafted.

## Worked example

**Hypothesis-first rewrite (board, before/after):**

| Feature-first (given) | Hypothesis-first rewrite |
|---|---|
| "Build churn model v2 with more features" | "Belief: tenure-decay features explain the Q2 churn spike. Test: add 4 tenure-decay features to baseline model. Confirm: AUC +≥ 0.02 on frozen holdout. Cost: 1.5 d. Decision: if no lift, the spike is *not* feature-driven → pivot to service-interaction data." |
| "Improve model accuracy" | Unusable as written — no belief, no threshold, no decision. (Keep one of these in the drill; students must *kill* an item and say why.) |
| "Deploy model to production" | "Belief: batch scoring meets the freshness SLA. Test: shadow-deploy on 1 wk of live traffic. Confirm: p95 scoring latency ≤ 2 min & DQ gates green ≥ 98%. Cost: 2 d. Decision: go/no-go for the gate review." |
| "Handle data quality issues" | "Belief: the 3 DQ rules from L14 catch the CRM import failure mode. Test: replay last quarter's imports through the gate. Confirm: zero silent bad-batches reach features. Cost: 0.5 d. Decision: rules → production gate or redesign." |

Then the sprint shape: 60–70% build capacity on confirmed-direction work,
25–30% as the uncertainty budget (spikes), 10% operations. The sprint review
presents *evidence against hypotheses*, not screenshots; the pivot/hold/kill
review runs monthly, not per-sprint (protects direction from weekly mood).

## Common misconceptions

| Misconception | Correction |
|---|---|
| "Negative results mean wasted sprints." | A well-posed test that refutes a belief *changed the plan correctly* — that is delivery in discovery work; the waste is unfalsifiable items. |
| "Accuracy is the release criterion." | Accuracy without fairness bounds, monitoring, and rollback is a deployment risk, not a done state — the model DoD exists because of this. |
| "Data science can't be agile." | The *mechanics* adapt (experiment containers, uncertainty budgets); the values (working software, collaboration, response to learning) fit data work *better*. |
| "Spikes are what you do when blocked." | Spikes are planned, budgeted discovery with exit criteria — not unplanned escape hatches. |
| "The model gate is bureaucracy between data science and shipping." | The gate is the *contract* that makes "done" meaningful for systems whose behavior drifts after release. |

## Classroom activities

1. **CS-31 rewrite drill (35 min):** six feature-first items → hypothesis
   form (belief/test/confirm/cost/decision); one item must be killed with a
   stated reason.
2. **CS-32 model DoD workshop (30 min):** full checklist for the churn model;
   CS-track teams write the equivalent for an A/B-tested UI feature (the
   transfer test).
3. **Uncertainty-budget simulation (10 min):** given a sprint with 2 failed
   hypotheses, re-plan next sprint's budget — does discovery capacity rise or
   fall, and why?

## Discussion questions

1. Your strongest hypothesis died in week 2 of a 3-month timeline. What does the pivot/hold/kill review decide — and what does sunk-cost pressure argue instead?
2. Who sets the fairness threshold in your model DoD — the data scientist, the sponsor, or the regulator-shaped stakeholder? At which meeting does it get fixed?
3. For a CS-track product, what is your "model DoD" equivalent — what makes a *feature* done beyond code-complete?

## Practical exercise

**In class:** CS-31 + CS-32 deliverables. **Take home (30 min, capstone
section):** rewrite three of your team's backlog items into hypothesis form
and draft the model/feature DoD for your own project — both join the capstone
plan (DS teams: this *is* the model-risk-gate section).

## Formative assessment (exit ticket)

1. Name the five parts of a hypothesis-first backlog item.
2. What is an uncertainty budget, and what sprint capacity typically feeds it?
3. Rollback belongs in the DoD because ___. (Complete the sentence.)

## Reading & references

- Fountain, K. (2020). *The Pipeline: A Picture of Homebrew Production* —
  the data life cycle in one concrete walk ([textbooks page](../../../docs/syllabus/textbooks.md);
  confirm access before citing).
- Schwaber & Sutherland. (2020). *The Scrum Guide* — being adapted, so know
  the base.
- [Lab 11 brief](../../../docs/labs/index.md) — backlog rewrite artifact.

## Two-hour teaching plan

| Slot | Segment | Materials |
|---|---|---|
| 0:00–0:10 | Hook: the sprint that "failed" and saved the quarter | — |
| 0:10–0:28 | Why vanilla mis-fits; spikes; uncertainty budget | board |
| 0:28–0:50 | Worked example: backlog rewrite + sprint shape | board table |
| 0:50–1:00 | Break | |
| 1:00–1:30 | CS-31 rewrite drill | CS-31 brief |
| 1:30–1:55 | CS-32 model DoD workshop (both tracks) | DoD template |
| 1:55–2:00 | Exit ticket | slips |

## Instructor preparation notes

- Seed CS-31 with one deliberately unfalsifiable item ("improve accuracy") —
  the kill discussion is the exercise's credibility moment.
- DoD template handout: metric/baseline/threshold/measurement-owner rows —
  CS-track teams need the transfer guidance explicit.
- Capstone link check: DS-track teams' gate checklists from today feed L27's
  master plan; log which teams completed them.

## Linked resources

- Lecture skeleton: [`docs/lectures/L23`](../../../docs/lectures/L23-23-agile-data-ml.md)
- Cases: [CS-31](../../../docs/cases/CS-31.md) · [CS-32](../../../docs/cases/CS-32.md)
- Lab 11: [labs index](../../../docs/labs/index.md)
- Forward: [ethics L28](../../../docs/lectures/L28-28-ethics-governance.md)
  (fairness thresholds are governance decisions) ·
  [capstone tracks](../../../docs/capstone/capstone-charter.md).
