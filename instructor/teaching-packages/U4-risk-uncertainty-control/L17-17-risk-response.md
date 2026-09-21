# Lecture 17 — Risk Responses, Issues & Reserves

> **Package for:** L17 · Week 9 · Unit U4 · CLO4 · Bloom: Evaluate · **A3 released today**
> **Case anchor:** CS-23 (response plans for the top ten)
> Companion: [`L17` skeleton](../../../docs/lectures/L17-17-risk-response.md) · [CS-23 brief](../../../docs/cases/CS-23.md)

## Learning objectives

1. Choose and justify response strategies for threats (escalate/avoid/mitigate/transfer/accept) and opportunities (exploit/share/enhance/accept).
2. Write complete response plans: owner, trigger, action, residual risk.
3. Track secondary and residual risk after treatment.
4. Operate an issue log distinct from the register, and defend reserve access rules.

## Required prior knowledge

- L15 register + scoring (the top ten being responded to).
- L13 reserves (contingency vs management reserve — today's access rules).

## Teaching notes

Responses are where risk work becomes *contracts with named humans*. The
lecture's discipline: **every response names an owner, a trigger, and a
residual** — a response without a trigger is a wish, without an owner is a
hope, without a residual is a fantasy. Drill the three failsafes through
CS-23.

Teach strategies with the cost angle: transfer has a price (insurance,
contracts — L18 deepens), mitigation has a cost curve (spend vs probability
reduction), accept has two flavors (active: a funded fallback; passive: "we'll
deal with it" — which is the failure mode dressed as a strategy). Opportunities
get equal billing — the *exploit* example (pull work forward to capture an
early-market window) is worth ten minutes; students have never treated upside
with process.

A3 releases today (register + responses); the session IS the response
workshop, so the brief and the case interlock by design.

## Definitions & concepts

- **Threat strategies** — *escalate* (outside project authority — to program/
  portfolio), *avoid* (eliminate the cause), *mitigate* (reduce P or I),
  *transfer* (shift consequence — insurance, fixed-price contracts, hedging),
  *accept* (active: funded contingency plan; passive: documented inaction).
- **Opportunity strategies** — *exploit* (make it certain), *share* (partner
  for capability), *enhance* (raise P or +I), *accept* (take it if it comes).
- **Trigger condition** — the observable early-warning that starts the
  contingency plan.
- **Residual risk** — what remains *after* the response (expected!). 
  **Secondary risk** — *created by* the response (the classic: fast-tracking
  creates rework risk).
- **Issue log** — occurred problems with assignments and due dates; distinct
  lifecycle from risks.

## Practical examples

**CS:** vendor rate-limit risk (L15's R1) — options: *mitigate* (batch + cache
design, cost 30 h), *transfer* (vendor SLA with credits, negotiation cost),
*avoid* (change architecture to event-driven ingestion — expensive, removes
the cause). Walk choosing: mitigation cost vs expected impact; the trigger
("queue depth > 2× baseline for 2 h") and residual ("extreme-day bursts still
delay alerts ≤ 1 h").

**DS:** label-era inconsistency (L15's R3, critical) — *mitigate*: era-bound
retraining + fairness threshold monitoring (cost: 60 h + gate extension);
residual: pre-migration records remain less reliable — documented, with a
monitoring metric. Secondary risk: the era-based split reduces training
volume per cohort (new statistical risk — smaller cohorts, wider CIs; goes in
the register!).

## Worked example

**Response-plan table (board, full fields) for three top risks:**

| Risk (short) | Strategy | Owner | Trigger | Action | Residual / secondary |
|---|---|---|---|---|---|
| R1 Ingestion freshness (12) | Mitigate | Data eng lead | Queue depth > 2× baseline 2 h | Batch+cache redesign (30 h, funded from contingency) | Bursts ≤ 1 h delay (accepted) |
| R3 Label-era bias (15) | Mitigate | Model risk owner | Fairness gap > 5 pts in monitoring | Era-bound retrain + monitoring metric (60 h) | Cohort CIs widen; pre-era records less reliable |
| R5 Gate demands evidence (12) | Avoid (via preparation) | PM | Gate agenda published | Pre-build evidence pack for both gate outcomes (20 h) | Gate date may still slip (transferred to schedule buffer) |

Then the anti-examples (passive accept dressed as strategy): "monitor" with
no trigger; "PM will handle it" with no action; "mitigate" with no residual.
Students rewrite each into a complete plan — the rewrite IS the learning
objective in miniature.

## Common misconceptions

| Misconception | Correction |
|---|---|
| "Mitigate everything high." | Strategy choice weighs cost of response vs expected impact; some highs are cheapest to avoid or transfer, some lows to accept actively. |
| "Transfer means the risk is gone." | The consequence moved; the project usually retains secondary exposure (vendor fails → re-integration). |
| "Accept = do nothing = lazy." | *Active* accept funds a fallback; passive accept must be documented and visible. |
| "Responses remove the risk." | They leave residuals and can create secondaries — both go back in the register (the loop, ISO 31000). |
| "The risk owner does the work." | The owner *watches and triggers*; action owners may differ — both named. |

## Classroom activities

1. **CS-23 response workshop (40 min):** top-ten risks → complete plans;
   swap-and-attack: another team hunts for the missing trigger/owner/residual.
2. **Strategy tournament (15 min):** five risks, five teams each assigned a
   *different* strategy for the same risk; pitch; class judges cost-effectiveness.
3. **Anti-example rewrite (10 min):** the three broken plans above, repaired
   live on the board.

## Discussion questions

1. Which of your own responses has the weakest trigger — what observation would fire it reliably, and can you instrument that this semester?
2. When is *escalating* a risk the professionally correct move rather than an admission of failure? (Leadership bridge: L26/L28.)
3. Your mitigation created a secondary risk with a higher score than the residual of the risk it treated. Now what?

## Practical exercise

**In class:** CS-23 deliverable. **Take home (feeds A3):** complete response
plans for your own top-ten (owners, triggers, residuals, secondaries) +
contingency sizing paragraph (bridging L13/L16 evidence). **A3 due after
L19.**

## Formative assessment (exit ticket)

1. Name the five threat strategies; which one is a sponsor decision?
2. What two fields does a trigger need to be usable?
3. Secondary vs residual — one sentence each.

## Reading & references

- ISO 31000:2018 — treatment step of the risk process.
- PMI. (2021). *PMBOK Guide* (7th ed.) — Uncertainty domain (responses,
  secondary/residual risk).
- [Assignment 2 brief](../../../docs/assignments/a2-risk-register.md) (released today).

## Two-hour teaching plan

| Slot | Segment | Materials |
|---|---|---|
| 0:00–0:10 | Hook: the response that said "monitor" and died | — |
| 0:10–0:30 | Strategy families; owner/trigger/residual doctrine | board |
| 0:30–0:50 | Worked example: three complete plans + anti-examples | board table |
| 0:50–1:00 | Break | |
| 1:00–1:40 | CS-23 workshop + swap-attack | CS-23 brief |
| 1:40–1:55 | Strategy tournament pitches | strategy cards |
| 1:55–2:00 | Exit ticket + A3 release | slips |

## Instructor preparation notes

- Pre-select the tournament risk (one where all five strategies are genuinely
  defensible — usually a vendor/data-access risk).
- Prepare the anti-example cards; the rewrite drill runs twice as well when
  the failures are funny but recognizable.
- A3 rubric check: response-completeness fields must match today's table
  exactly (owner, trigger, action, residual, secondary).

## Linked resources

- Lecture skeleton: [`docs/lectures/L17`](../../../docs/lectures/L17-17-risk-response.md)
- Case: [CS-23](../../../docs/cases/CS-23.md)
- Assignment: [A3 brief](../../../docs/assignments/a2-risk-register.md)
- Forward: [procurement L18](../../../docs/lectures/L18-18-procurement.md)
  (transfer deepens) · [EVM L19](../../../docs/lectures/L19-19-evm.md) ·
  [opportunity register CS-66 (homework lane)](../../../docs/cases/index.md).
