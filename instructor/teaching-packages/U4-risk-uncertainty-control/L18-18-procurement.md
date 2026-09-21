# Lecture 18 — Procurement & Vendor Management

> **Package for:** L18 · Week 9 · Unit U4 · CLO3, CLO4 · Bloom: Apply
> **Case anchors:** CS-24 (contract-type selection), CS-25 (ML-API SLA)
> Companion: [`L18` skeleton](../../../docs/lectures/L18-18-procurement.md) · [CS-24](../../../docs/cases/CS-24.md) · [CS-25](../../../docs/cases/CS-25.md)

## Learning objectives

1. Run a make-or-buy analysis with explicit cost and capability criteria.
2. Choose contract types (FP/T&M/cost-plus) by matching risk allocation to the work's uncertainty.
3. Draft measurable SLA acceptance criteria for a technical service (incl. an ML API).
4. Apply vendor-lifecycle controls: RFP anatomy, evaluation, exit clauses.

## Required prior knowledge

- L15/L17 (risk transfer as a response strategy — contracts are its instrument).
- L13 (cost structures: fixed vs variable reappear as contract types).

## Teaching notes

Procurement fails in engineering curricula because it sounds commercial. Make
it engineering: **a contract is a risk-allocation and information-allocation
device.** The rule that carries the lecture: *whoever controls the uncertainty
should carry its price* — fixed-price transfers cost risk to a vendor who
cannot control it, so the price inflates or quality surrenders (adverse
selection + lipstick estimation); T&M hands all risk to the buyer when scope
is actually stable. Matching beats optimizing.

Second spine: **exit is designed at entry.** Lock-in (egress fees, proprietary
formats, data gravity) is negotiated when you have leverage, not when you need
out. The ML-API SLA case (CS-25) makes acceptance measurable: latency
percentiles, accuracy-drift bands, availability windows, rollback duties —
vague SLAs are the vendor equivalent of vague success criteria (L06 echo).

The DS-specific trap: model-quality SLAs ("95% accuracy") are *uncontractable
as stated* — accuracy depends on incoming data the vendor doesn't control.
Teach the repair: define drift bands against an agreed baseline and a
measurement protocol (who runs what test set, when).

## Definitions & concepts

- **Make-or-buy** — capability/cost/control analysis; often "both" (buy the
  commodity, build the differentiator).
- **FP (firm fixed price)** — vendor carries cost risk; best when scope is
  well-specified. **T&M (time & materials)** — buyer carries scope risk; best
  when work is exploratory/small. **Cost-plus** — vendor carries least;
  fits genuine R&D with audit rights; variants (fixed-fee, incentive-fee).
- **SLA** — measurable service commitments: percentiles (p95/p99), windows,
  drift bands, remedies (credits), measurement protocol.
- **RFP anatomy** — context, scope, evaluation criteria & weights (publish
  them — CS-97's bias lesson again), submission format, exit/transition
  requirements.
- **Exit clause set** — data export formats, transition assistance period,
  knowledge-transfer duties, last-renewal notice.

## Practical examples

**CS:** identity-management integration — buy (commodity SSO) + build the
student-facing UX; FP for the well-specified SSO integration, T&M for the
exploratory accessibility refactor.

**DS:** churn-scoring API (TelcoCare): FP is *wrong* for the model-quality
part (vendor doesn't control your incoming data) but right for infra uptime;
the mature contract splits: infra SLA (FP-style credits) + model drift band
(joint measurement protocol) + data-quality responsibilities on the buyer
(your gates, L14, become contract references!). Exit: model artifacts +
training-code escrow, 60-day transition assistance.

## Worked example

**Contract-type matching with risk arithmetic (board):**

Scenario table with the "who controls the uncertainty" test:

| Work | Uncertainty controller | Type | Why |
|---|---|---|---|
| SSO integration (fixed spec, 30 interfaces) | Vendor | **FP** | Scope stable; vendor prices its own efficiency |
| 6-week accessibility exploration | Nobody yet | **T&M with cap** | Discovery; buyer keeps control, cap limits exposure |
| Novel fraud-detection R&D | Shared | **Cost-plus-incentive** | True R&D; incentive fee ties to milestone evidence |
| Cloud compute 3-yr | Shared (usage) | **Committed-use + overage** | Volume certainty priced, spikes flexible |

Then the inflation demo: take the FP SSO job priced at $120k; deliberately
under-specify 8 interfaces ("details later") → vendor's rational bid adds a
risk premium ≈ p(rework) × cost ≈ 0.5 × 8 × $6k = **+$24k** and tighter
change-request pricing. **The spec quality *is* the discount.** Students
compute their own premium for two specification levels — procurement quality
is requirements quality (L09's scope statement pays rent here).

## Common misconceptions

| Misconception | Correction |
|---|---|
| "FP transfers all risk to the vendor." | It transfers *cost* risk; quality/relationship risks resurface, and unpriced scope ambiguity inflates the price. |
| "T&M is a blank check." | With caps, evidence of progress, and Named-Resource clauses, T&M is the honest choice for genuine discovery. |
| "SLA = uptime percentage." | Modern technical SLAs cover percentiles, drift bands, and remediation duties; uptime alone measures almost nothing user-relevant. |
| "Exit clauses are pessimistic rudeness." | They are leverage-neutral instruments that keep the relationship professional; absence of exit *is* the lock-in. |
| "Procurement is the buying office's job." | Engineers define the *technical* acceptance evidence; without it the contract has no teeth. |

## Classroom activities

1. **CS-24 contract-type scenarios (25 min):** four sourcing cases; teams
   choose + defend with the uncertainty-control test.
2. **CS-25 SLA drafting (35 min):** measurable criteria for the churn API —
   latency p95, drift band vs agreed baseline, availability window, rollback
   duty, measurement protocol (who/what/when).
3. **Exit-clause checklist (10 min):** five SaaS dependencies; teams write the
   three exit provisions each one most needs.
4. **Spec-premium demo (10 min):** the $24k inflation arithmetic as a
   call-and-response computation.

## Discussion questions

1. Your vendor's model drift exceeds the band, but *your* data quality also degraded. Whose breach is it — and what contract language would have prevented the dispute?
2. When is cost-plus the *ethical* choice rather than a naive one? (Think: paying for honest R&D vs incentivizing overruns.)
3. What data-gravity lock-in does your capstone's storage choice create, and what exit provision offsets it?

## Practical exercise

**In class:** CS-24 + CS-25 deliverables. **Take home (30 min):** procurement
section for the capstone plan: one make-or-buy decision with criteria, one
contract-type recommendation, three exit provisions for the biggest external
dependency. DS teams: the SLA table from CS-25 adapted to their own model
dependencies.

## Formative assessment (exit ticket)

1. Which contract type when scope is well-known? When genuinely unknown?
2. Name three components of a measurable SLA beyond "uptime."
3. Why does a vague specification raise a fixed price?

## Reading & references

- PMI. (2021). *PMBOK Guide* (7th ed.) — Uncertainty domain (agreements/
  transfer) and Project Work domain (procurement practices).
- PMI. (2017). *PMBOK Guide* (6th ed.) — "Conduct Procurements"/"Control
  Procurements" (contract-type taxonomy).
- [Case CS-67](../../../docs/cases/index.md) (homework lane) — vendor
  risk-transfer clause review; pairs with today.

## Two-hour teaching plan

| Slot | Segment | Materials |
|---|---|---|
| 0:00–0:08 | Hook: the SLA that measured nothing | — |
| 0:08–0:28 | Make-or-buy; contract types as risk allocation | scenario table |
| 0:28–0:50 | Worked example: matching + spec-premium arithmetic | board |
| 0:50–1:00 | Break | |
| 1:00–1:25 | CS-24 scenarios | CS-24 brief |
| 1:25–1:55 | CS-25 SLA drafting + exit checklist | CS-25 brief |
| 1:55–2:00 | Exit ticket | slips |

## Instructor preparation notes

- Verify the spec-premium arithmetic table before class ($6k/interface
  assumption is stated in the brief — keep brief and board consistent).
- SLA drafting needs a baseline-definition handout (measurement protocol
  skeleton) or teams will produce aspirational prose.
- Bridge check: A3 (risk register + responses) due after L19 — remind; the
  SLA drafting today is *also* transfer-strategy practice for A3.

## Linked resources

- Lecture skeleton: [`docs/lectures/L18`](../../../docs/lectures/L18-18-procurement.md)
- Cases: [CS-24](../../../docs/cases/CS-24.md) · [CS-25](../../../docs/cases/CS-25.md)
- Assignment: [A3 brief](../../../docs/assignments/a2-risk-register.md)
- Forward: [governance L28](../../../docs/lectures/L28-28-ethics-governance.md)
  (vendor oversight is a governance structure) ·
  [exit-clause case CS-79 (homework lane)](../../../docs/cases/index.md).
