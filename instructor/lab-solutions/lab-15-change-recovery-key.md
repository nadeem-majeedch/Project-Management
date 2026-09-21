# Lab 15 Answer Key — Change Control & Recovery Plan

## Options analysis (model; ≥ 4 required with numbers)

| Option | What changes | Cost | Finish forecast (method) | Risk introduced | Constraint check |
|---|---|---|---|---|---|
| O1 Crash D+E | D 5→4, E 4→3 (Lab 4 slopes) | 60,000 + 75,000 = 135,000 from contingency | EAC₁ path re-pass: ≈ 1.5 wk recovered → finish ≈ wk 18.5 | compresses QA time | Deadline: FAIL alone (finish still > 17) → pair with O3 |
| O2 Fast-track E over D tail | overlap SS+2 | ≈ 0 direct; rework p ≈ 30% ≈ 110k expected | ≈ 2 wk calendar gain | rework on streaming features | Deadline: FAIL alone; QA rework eats G's window |
| O3 De-scope | defer B7-class items from re-plan (not Must items) | 0 (scope moved to phase 2) | finish wk 17 achievable with O1 | stakeholder friction (union watches) | PASS with O1; SLA PASS |
| O4 Fund the gap | contingency 412k + MR request ≈ 320k | new ask ≈ 720k | holds wk 17.5–18 scope-complete | sponsor trust; sets precedent | Deadline: FAIL unless paired with scope cut |

**Model decision:** O1 + O3 combined (crash 135k from contingency + defer
non-Must scope) → credible wk-17 finish at SLA evidence level; MR untouched
(held for true unknowns); vendor SOW unchanged. O4 alone rejected: money
doesn't buy calendar under a fixed deadline without scope movement.

## CCB decision record (model minutes)

- **Present:** Registrar (chair), vendor manager, PM, QA lead, union
  observer. **Options presented:** O1–O4 with numbers above.
- **Decision:** O1+O3; CR-009; re-baseline: scope (B7 deferred), contingency
  redraw 412k → 277k after crash spend; finish forecast wk 17 at P50 post-
  crash; effective immediately.
- **Dissent recorded:** QA lead opposed compressing E by 1 week (test
  evidence thinner at G gate); mitigations: rehearsal runs +2, escape
  analysis mandatory at closure. Union observer asked the student question;
  B1/B6 protected, deferred items are non-Must.
- **Effective:** week 10 start; owner PM.

## Re-forecast (model)

- New ask: no change to funding ceiling (crash funded from contingency);
  contingency redraw documented in CR-009.
- Finish forecast: wk 17, confidence ≈ P50 post-crash (state honestly: ≈
  40–50%; P80 ≈ wk 17.5 with de-scope insurance).
- TCPI re-check: with re-baselined BAC' ≈ 4,397k (4,532k − 135k crash −
  deferred scope value) and corrected-EV CPI ≈ 0.803, TCPI' = (BAC' − EV') /
  (BAC' − AC) — students must show their arithmetic; the honest reading is
  that TCPI' lands near 0.95–1.00 → credible *only because* scope moved;
  without the de-scope it stays > 1.10 → not credible.
- Dashboard Views 1–2 updated: Cost AMBER (CPI < 0.95 but EAC within
  re-baselined ceiling), Schedule AMBER (SPI improving, forecast within
  deadline at P50).

## Integrity check (model)

The compressed plan demands no sustained CPI > 1.05: the recovery buys
calendar with scope and 135k, not with a promised efficiency miracle. If a
student's option requires CPI 1.05+ without structural change (capacity,
scope, or method change), it fails the integrity gate — return it.

## Common wrong answers

| Error | Correction |
|---|---|
| Options checked against constraints only at the end | every option, immediately |
| "Work overtime" as an option | not structural; 8 weeks of overtime is a capacity change — cost it or drop it |
| MR spent in the CCB decision | MR is sponsor-held for unknowns; using it here needs the sponsor's separate signature, not CCB mood |
| De-scope picks student-visible Must items | de-scope order: Could → Should; Must items under the 48h rule are untouchable |
| Dissent omitted from minutes | recorded dissent is the audit trail; consensus theater fails governance |
| TCPI re-check skipped | the re-baseline is only credible with the new TCPI shown |

## Reflection guidance

1. The calendar rule (fixed deadline) killed O2/O4-as-sole-option —
   constraints discovered *before* planning (charter) are design inputs;
   discovered *during* (week 9) they become decision killers. Same rule,
   different cost.
2. De-scope protects: B1/B6 (Must, student-critical) first; B7
   notifications and B10 accessibility go to phase 2 with registrar-visible
   rationale — the union observer's presence is the safeguard.
3. Honest framing: "The original baseline was set before discovery risk was
   quantified; we are asking for contingency we already held, plus scope
   deferral, to protect the SLA — not new money for the same scope."

## Preparation notes

Assign CCB roles a day early; the registrar role needs the Lab 12 RAG
dashboard in hand. Record actual minutes during the simulation — students
reuse this artifact in the capstone's governance section. This is the
semester's decision lab: protect the 40-minute CCB window from overrun.
