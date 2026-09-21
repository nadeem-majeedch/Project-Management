---
title: Capstone Specification
---

# Capstone Specification (A7 — 25%, CLO5 + CLO6)

The capstone is an **integrated project management plan plus its defense** —
not a built product. Teams of 3–5 produce the complete planning system for
one project, prove the plan's internal consistency, and defend the judgment
behind it.

## The two tracks

Choose **one** track; both defend in the same session against the same
rubric.

### Track A — Software engineering project

Typical seeds: a CAMPUSHUB module build, a GRIDSENSE alert-delivery feature,
an approved external/employer project.

- **Scope shape:** feature-oriented WBS; integration and UAT milestones.
- **Schedule shape:** sprint-based delivery with integration windows.
- **Cost emphasis:** person-months, licenses, environments.
- **Quality plan:** test coverage targets, defect-density gates, review
  discipline.

### Track B — Data science / ML project

Typical seeds: TELCOCARE churn model, GRIDSENSE anomaly detection, MEDSYNC
analytics.

- **Scope shape:** pipeline-stage WBS — ingestion → features → model →
  serving → monitoring.
- **Schedule shape:** experiment-gated — discovery spikes feeding training
  milestones.
- **Cost emphasis:** compute hours, storage, cloud price volatility.
- **Quality plan:** data-quality rules **and** model-quality gates.
- **Extra required section — the model risk gate:** metrics, fairness
  bounds across segments, drift monitoring, rollback plan
  (case [CS-74](../cases/CS-74.md) is the worked pattern).

## Required artifacts (both tracks)

The master plan must contain all twelve; each has a course template linked
from [Templates](../resources/templates.md).

| # | Artifact | Evidence of proficiency |
|---|---|---|
| 1 | Project charter | SMART objectives, measurable success criteria, sponsor authority |
| 2 | Stakeholder register | ≥ 10 stakeholders with exchanges; power/interest grid; engagement plan |
| 3 | Scope statement | in/out lists, explicit exclusions, acceptance criteria |
| 4 | WBS + dictionary | deliverable-oriented, 100% rule holds, dictionary for ≥ 2 packages |
| 5 | Schedule | estimates with basis, network with critical path, baselined Gantt, milestones |
| 6 | Cost estimate | bottom-up, contingency justified line-by-line, reserve separated |
| 7 | Risk register | ≥ 15 normalized risks, scored, owned responses with triggers, residual |
| 8 | Quality plan | metrics with provenance; Track B adds data-quality rules + fairness gates |
| 9 | Communication plan | audience-mapped cadence; covers every grid quadrant |
| 10 | Change control approach | CCB composition, threshold rules, baseline mechanics |
| 11 | Monitoring approach | indicators, review cadence, escalation thresholds |
| 12 | Final presentation | ≤ 12 slides, defense format followed |

## Consistency requirements (where most marks live)

The rubric's *internal consistency* dimension is 20% — these are checked
literally ([instructor stress tests](#) apply verbatim):

1. Milestone dates match the network output — the critical path drives the
   Gantt, not the other way round.
2. Cost baseline totals reconcile to the bottom-up sheet + contingency.
3. Every risk scored ≥ 15 (or High band) has owner, trigger, response, and
   residual stated.
4. The communication matrix covers every stakeholder the grid places in
   manage-closely and keep-satisfied.

## Tailoring justification

Every artifact cut from heavyweight practice needs a written defense tied to
**this project's attributes** (duration, team size, regulatory context,
stakeholder count). "The template said so" and "we skipped it to save time"
are both zeros — replacement, not removal.

## Ethics, AI, and data (graded, not decorative)

- All data synthetic or public; consent/governance treatment of data is a
  plan section, not a footnote ([CS-100](../cases/CS-100.md) pattern).
- Standards cited by edition/year (PMBOK 7, ISO 31000, Scrum Guide 2020).
- AI assistance disclosed per the [integrity policy](../assessments/academic-integrity.md)
  and **defended in Q&A** — you must show where AI output was rejected.

## Process evidence

Export your team's board/sprint history from the semester's labs. The
history must show real cadence — backfilled boards are detectable and score
0 on the team-process dimension.

## Eligibility and registration

- Seed-catalog projects (MEDSYNC, TELCOCARE, CAMPUSHUB, GRIDSENSE,
  VOLTPAY, AGROSENSE), or instructor-approved external project with a
  written sponsor brief.
- No live production systems; no real personal data.
- Track choice and one-paragraph project brief due at **L12** with the
  [charter](capstone-charter.md).
