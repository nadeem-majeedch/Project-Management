# Lecture 20 — Monitoring, Dashboards & Change Control

> **Package for:** L20 · Week 10 · Unit U4 · CLO4 · Bloom: Evaluate · **Midterm window opens; capstone checkpoint**
> **Case anchor:** CS-27 (sponsor dashboard + mock CCB)
> Companion: [`L20` skeleton](../../../docs/lectures/L20-20-monitoring-control.md) · [CS-27 brief](../../../docs/cases/CS-27.md)

## Learning objectives

1. Distinguish leading from lagging indicators and choose a project's vital few.
2. Design a one-page sponsor dashboard where every RAG status is defensible from data.
3. Run an integrated change-control process: CR lifecycle, CCB decision, baseline update.
4. Connect monitoring to intervention: what threshold triggers what action, decided in advance.

## Required prior knowledge

- L19 (the indices that feed dashboards), L12 (the baseline being protected).
- L15/L17 (triggers — today formalizes them into governance).

## Teaching notes

Monitoring fails in two symmetric ways: drowning stakeholders in metrics, or
reporting status as mood. The doctrine students carry out: **every metric
earns its place by enabling a decision, and every status color is a *claim
with evidence*.** The RAG discipline: red is not failure — red is "intervention
required and requested"; a green report that hides a known slip is the only
unforgivable status (ties directly to the ethics spine, L28).

The second half is **integrated change control** — the first genuinely
*governance-flavored* session: CR intake → impact analysis (all baselines at
once: scope/schedule/cost/risk) → CCB decision → baseline update →
communication. The mock CCB (CS-27) is the course's best energy spike: five
CRs, one board, hard timeboxes, and the discovery that "just say yes to
everything" *is* a baseline decision with consequences.

The midterm window opens this week; the capstone checkpoint happens in the
case work (teams re-baseline their own plan against their CR outcomes).

## Definitions & concepts

- **Leading vs lagging indicators** — predict trouble vs record it (e.g.,
  review-defect rate vs delivered defects; DS: data-freshness lag vs model
  drift alert).
- **Vital few** — the 4–7 metrics that drive decisions; everything else is
  reference.
- **RAG discipline** — Red/Amber/Green *with evidence and requested decision*;
  text labels always accompany color (accessibility + honesty).
- **Integrated change control** — single process evaluating a change against
  *all* baselines simultaneously; **CCB** — the named decision body (chair,
  members, quorum, cadence).
- **CR lifecycle** — submitted → impact-analyzed → decided (approve/reject/
  defer) → baselines updated → communicated. No "orally approved" changes.
- **Threshold-action pairs** — pre-agreed: metric breach → named action →
  named owner (monitoring without pre-agreed action is spectatorship).

## Practical examples

**CS dashboard (registration rewrite):** burn-up of acceptance-tested features
(leading: review-defect trend), schedule confidence (P80 from the L16 run vs
committed date), budget burn vs S-curve, top-3 risks movement, milestone
readiness (schema freeze). Every tile names its action threshold.

**DS dashboard (churn model):** data-freshness lag (hours), data-quality gate
pass rate, feature-drift score, fairness-gap trend vs the 5-pt threshold,
model-gate evidence status, compute spend vs plan. The drift tile's
threshold-action pair: gap > 5 pts → freeze offers + trigger retraining
decision (the L17 trigger, now governed).

## Worked example

**Building the dashboard from evidence (board walk-through):**

| Tile | Data source | Green/Amber/Red rule | Action on breach |
|---|---|---|---|
| Schedule confidence | P80 vs commitment | G: P80 ≤ commit; A: ≤ commit+10%; R: > | R → re-baseline request to CCB |
| Cost burn | AC/EV vs S-curve | G: CPI ≥ 0.95; A: 0.90–0.95; R: < 0.90 | R → corrective plan + forecast EAC₄ |
| DQ gate pass rate | pipeline logs | G ≥ 98%; A 95–98%; R < 95% | R → quarantine batch, hold scoring |
| Fairness gap | monitoring metric | G ≤ 5 pts; A 5–7; R > 7 | R → freeze offers; retrain decision |
| Top risks | register movement | G: no new highs; R: new high or trigger fired | R → response review at next gate |

Then the **mock CCB (CS-27, 35 min)**: five CRs — one innocent (typo fixes:
approve, batch), one scope creep wearing a tiny price tag ("one extra report
column" — approve *with* the pipeline-cost line item it implies), one
gold-plating (reject with dignity: recorded, revisitable), one emergency
(regulatory date: approve, but *which baseline moves?* — the board must name
the sacrificed scope or added money), one sneaky (a "schedule-only" change
that quietly needs +1 FTE — the impact analysis catches it). Chair rotates per
table; minutes are a deliverable: decision, rationale, baseline impact,
communication plan.

## Common misconceptions

| Misconception | Correction |
|---|---|
| "More metrics = better monitoring." | Dashboards are decision instruments; every tile must earn removal resistance. |
| "Green means nothing can hurt us." | Green means "within tolerance *and* no intervention requested" — confidence is stated, never implied. |
| "CCB is bureaucracy for small projects." | The *function* (no uncontrolled baseline change) scales down to a weekly change log review (L08 tailoring); the *ceremony* scales. |
| "Approving changes fast is good service." | Speed without impact analysis just externalizes the cost to the end; the CR's price includes its ripples. |
| "Red status damages credibility." | Honest red with a requested decision builds it; discovering hidden red later destroys it (L28's disclosure spine). |

## Classroom activities

1. **CS-27 dashboard build (30 min):** one page, five tiles, threshold-action
   pairs written per tile; peer test: "can you defend green from the data?"
2. **Mock CCB (35 min):** five CRs, rotating chairs, minutes required;
   instructor plays sponsor pushing for the sneaky CR.
3. **Leading-indicator hunt (10 min):** given eight lagging metrics, propose
   the leading twin each needs.

## Discussion questions

1. Your sponsor wants "one number" for project health. What do you offer instead, and what does the one number destroy?
2. Which of your capstone's threshold-action pairs would fire first — and is the action you pre-agreed actually fundable?
3. The CCB approved a scope change but nobody updated the risk register. What will this cost, and at which meeting does it surface?

## Practical exercise

**In class:** CS-27 deliverables (dashboard + minutes). **Take home (20 min,
capstone checkpoint):** teams apply the CCB outcome to *their own* plan —
produce the updated baseline delta and the communication note. This artifact
joins the process-evidence pack (rubric dimension: team process).

## Formative assessment (exit ticket)

1. Leading vs lagging — one example each from a data project.
2. What must a red status carry to be acceptable?
3. Name the CCB decision outputs for a CR (decision, ___, ___, ___).

## Reading & references

- PMI. (2021). *PMBOK Guide* (7th ed.) — Measurement domain; Project Work
  domain (change practice).
- PMI. (2017). *PMBOK Guide* (6th ed.) — "Perform Integrated Change Control"
  (the canonical CCB treatment).
- [Lab 12 brief](../../../docs/labs/index.md) — sponsor dashboard artifact
  (runs week 13; today's session is its rehearsal).

## Two-hour teaching plan

| Slot | Segment | Materials |
|---|---|---|
| 0:00–0:08 | Hook: the dashboard that was all green (and the project was not) | — |
| 0:08–0:28 | Vital few; leading/lagging; RAG discipline | board |
| 0:28–0:50 | Worked example: tiles + threshold-action pairs | board table |
| 0:50–1:00 | Break | |
| 1:00–1:30 | CS-27 dashboard build | CS-27 brief |
| 1:30–1:55 | Mock CCB (5 CRs, minutes) | CR cards |
| 1:55–2:00 | Exit ticket + midterm logistics | slips |

## Instructor preparation notes

- Prepare the five CR cards with their hidden ripples (the +1 FTE one is the
  debrief's centerpiece); keep the sponsor role script short and pushy.
- Midterm logistics confirmed: window, duration, allowed materials, AID
  policy (no devices) — post to LMS today.
- Capstone checkpoint: verify every team submits the baseline-delta artifact;
  it is the L27 red-team's raw material.

## Linked resources

- Lecture skeleton: [`docs/lectures/L20`](../../../docs/lectures/L20-20-monitoring-control.md)
- Case: [CS-27](../../../docs/cases/CS-27.md) · Lab 12: [labs index](../../../docs/labs/index.md)
- Forward: [Scrum L21](../../../docs/lectures/L21-21-scrum.md) (adaptive-side
  monitoring) · [master plan L27](../../../docs/lectures/L27-27-master-plan.md)
  (the baselines being defended).
