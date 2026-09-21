# Lecture 14 — Quality & Data-Quality Planning

> **Package for:** L14 · Week 7 · Unit U3 · CLO3 · Bloom: Apply · **A2 released today**
> **Case anchors:** CS-18 (quality metrics), CS-19 (data-quality rules)
> Companion: [`L14` skeleton](../../../docs/lectures/L14-14-quality-data-quality.md) · [CS-18](../../../docs/cases/CS-18.md) · [CS-19](../../../docs/cases/CS-19.md)

## Learning objectives

1. Distinguish grade vs quality, prevention vs inspection, verification vs validation.
2. Define measurable quality metrics with targets and measurement methods for a software system.
3. Write enforceable data-quality rules across the six dimensions and wire them into pipeline gates.
4. Compute a cost-of-quality trade-off and defend a testing-depth decision.

## Required prior knowledge

- L06 acceptance criteria (metrics formalize them).
- DS track: awareness that "the data was bad" is a *planning* failure, not an excuse.

## Teaching notes

Quality planning has a reputational problem among engineers: it sounds like
bureaucracy. Rebuild it as **decision evidence**: every quality metric is a
future *decision* (ship/hold/rollback) bought in advance. Verification =
"did we build the thing right?" (against specs); validation = "did we build
the right thing?" (against need). The L6th-ed vocabulary survives; the
7th-edition framing is the *quality* principle and Delivery/Measurement
domains.

The data-quality half is the DS spine's first full treatment. Teach the six
dimensions as **rule-writing fuel**: accuracy, completeness, consistency,
timeliness, validity, uniqueness. A dimension without an enforceable rule is a
slogan — the CS-19 workshop exists to convert slogans into pipeline gates
(that word returns in L23's model gates and KA-DATA-AI).

Cost-of-quality gives the arithmetic: prevention/inspection/internal-failure/
external-failure — the later a defect is caught, the more it costs. The
worked example quantifies the testing-depth decision (CS-62's setup).

## Definitions & concepts

- **Quality** — conformance to requirements + fitness for use; **grade** —
  feature richness (low grade can be high quality).
- **Prevention over inspection** — building quality in beats detecting failure
  later (COQ arithmetic makes this concrete).
- **Verification vs validation** — spec vs need (the clinical-system dispute
  in CS-73 is the exam-lane case).
- **Six data-quality dimensions** — accuracy (matches reality), completeness
  (nothing missing), consistency (no contradictions across sources),
  timeliness (fresh enough for the decision), validity ( conforms to format/
  range), uniqueness (no duplicates).
- **Data-quality gate** — an automated checkpoint blocking promotion when
  rules fail (the pipeline's quality conscience).
- **Cost of quality (COQ)** — prevention + appraisal + internal failure +
  external failure.

## Practical examples

**CS (CS-18):** registration system metrics — decision-relevant, not
vanity: *p95 registration latency ≤ 300 ms* (failover: capacity), *escaped
defects per release ≤ 2 critical* (test effectiveness), *accessibility
violations = 0 high-severity* (legal), *post-release support tickets ≤ 5/wk
for 4 weeks* (fitness for use).

**DS (CS-19):** churn dataset rules — *uniqueness*: `customer_id` unique per
snapshot; *completeness*: `churn_label` present for ≥ 98% of active accounts;
*validity*: `tenure_months` ∈ [0, 900]; *consistency*: `plan_tier` matches the
billing system's plan table; *timeliness*: snapshot age ≤ 24 h at scoring;
*accuracy*: 200-record monthly audit sample vs CRM source with error rate
≤ 1%. Each rule gets: threshold, severity, remediation (block/quarantine/
alert), owner.

## Worked example

**Cost-of-quality trade (board arithmetic):**

Feature: medication-dose recommendation (MEDSYNC-adjacent, safety-relevant).
Options: (A) standard testing depth; (B) extended depth (property-based +
independent review).

| COQ element | A ($) | B ($) |
|---|---|---|
| Prevention (design reviews, standards) | 2,000 | 3,500 |
| Appraisal (testing, review) | 6,000 | 11,000 |
| Expected internal failure (caught in-house) | 8,000 | 3,000 |
| Expected external failure (escaped; recall + harm) | 40,000 | 9,000 |
| **Total COQ** | **56,000** | **26,500** |

Walk it: B spends +$6,500 upfront and avoids ~$36,000 of failure cost — but
the *numbers* are estimates; the decision discipline is the lesson: external
failure carries distributional risk (harm, regulatory), so B also reduces
variance, not just expectation. Then the counter-case: for an internal
reporting dashboard, the same B option fails the proportionality test — COQ
arithmetic supports the *tailoring* of quality depth, not maximal testing
everywhere.

## Common misconceptions

| Misconception | Correction |
|---|---|
| "Quality = testing." | Testing is appraisal; most quality is built (or not) in prevention — design reviews, standards, data contracts. |
| "The data team will fix data quality during modeling." | Unplanned DQ work is a schedule risk (L15 will register it); gates make it visible and early. |
| "100% test coverage = quality." | Coverage measures *execution*, not assertion strength or fitness for use. |
| "Data-quality rules live in the model." | They live in the pipeline *before* features; a model cannot repair its inputs. |
| "We'll add monitoring later." | Monitoring design is a deliverable of planning; retrofit drift detection is how silent failures persist (L23/L29). |

## Classroom activities

1. **CS-18 metrics workshop (25 min):** four metrics with target + method +
   decision served; veto any metric without a decision attached.
2. **CS-19 rule writing (35 min):** eight enforceable rules across all six
   dimensions for the churn dataset (threshold, severity, remediation, owner).
3. **V&V sorting (10 min):** twelve activities → verification or validation;
   the "clinicians reject the workflow" item is the boundary case.
4. **COQ mini-decision (10 min):** the dashboard counter-case; teams argue
   option A with arithmetic.

## Discussion questions

1. Which data-quality dimension fails most quietly on your capstone data — and what gate would catch it?
2. Who owns a failed nightly gate at 3 a.m.? Name the role, not the person (L04 echoes).
3. Your fairness threshold (a quality metric for models) conflicts with raw accuracy. Who decides, and at what point in the project? (Seeds L23/L28.)

## Practical exercise

**In class:** CS-18 + CS-19 deliverables. **Take home (25 min):** draft ≥ 4
quality/data-quality metrics *and* ≥ 8 rules for your capstone project's data
(or system, CS track) — this section joins the capstone plan (L27) and, for
DS teams, the model risk gate checklist.

## Formative assessment (exit ticket)

1. Verification vs validation in one line each.
2. Name three data-quality dimensions and one rule each (short form).
3. In the worked example, what made option B's *variance* argument, not just its expectation argument?

## Reading & references

- PMI. (2021). *PMBOK Guide* (7th ed.) — Quality principle; Measurement and
  Delivery domains.
- PMI. (2017). *PMBOK Guide* (6th ed.) — "Plan Quality Management" (COQ
  taxonomy).
- [Templates](../../../docs/resources/templates.md): quality metrics sheet;
  [Assignment 1 brief](../../../docs/assignments/a1-scope-schedule.md)
  (released today; WBS/estimation/network/Gantt sections).

## Two-hour teaching plan

| Slot | Segment | Materials |
|---|---|---|
| 0:00–0:10 | Hook: the model that was accurate and useless (data drifted) | — |
| 0:10–0:25 | Quality concepts; V&V; COQ taxonomy | board |
| 0:25–0:40 | Data-quality dimensions → rule anatomy | rule table |
| 0:40–0:50 | Worked example: COQ trade + counter-case | board arithmetic |
| 0:50–1:00 | Break | |
| 1:00–1:25 | CS-18 metrics workshop | CS-18 brief |
| 1:25–1:55 | CS-19 rule writing + V&V sort | CS-19 brief |
| 1:55–2:00 | Exit ticket + A2 release | slips |

## Instructor preparation notes

- Prepare the rule-anatomy table (rule, threshold, severity, remediation,
  owner) as a handout; students copy the *shape*, not the content.
- The COQ worked example must land the counter-case — prepare the dashboard
  numbers ($400 external failure) so the proportionality turn is crisp.
- A2 release logistics: brief + rubric on LMS today; due after L16 (window
  spans the Monte Carlo week).

## Linked resources

- Lecture skeleton: [`docs/lectures/L14`](../../../docs/lectures/L14-14-quality-data-quality.md)
- Cases: [CS-18](../../../docs/cases/CS-18.md) · [CS-19](../../../docs/cases/CS-19.md)
- Assignment: [A2 brief](../../../docs/assignments/a1-scope-schedule.md)
- Forward: [risk L15](../../../docs/lectures/L15-15-risk-foundations.md) —
  data-quality failure becomes a named, owned risk ·
  [model gates L23](../../../docs/lectures/L23-23-agile-data-ml.md).
