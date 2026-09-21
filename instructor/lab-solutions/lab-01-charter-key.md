# Lab 1 Answer Key — Project Charter

**Grading: pass / refine.** "Refine" = resubmit once with fixes; both grades
require the reflection answers.

## Model charter content (what a pass looks like)

**Constraints identified (≥ 4 required):** 17-week fixed deadline (calendar
rule R4); staffing (3 devs, 1 QA, 1 DE, PM 50%); vendor SOW cap 1,950,000;
LMS vendor schema dependency; 48-hour result SLA. Strong answers also catch
the implicit constraint that QA stays independent of dev.

**Objectives (accept any 2–3 of this quality):**
- Publish semester results within 48 h of ceremony end (verified in staging
  rehearsal at G) — deadline: rollout week.
- Portal p95 response ≤ 2.0 s at 3,000 concurrent users (load test, 3 runs).
- Peak-registration outages: zero (measured across first registration window
  post-rollout).

**Scope in:** portal web app, LMS adapter, analytics repository (§A spine).
**Scope out (accept ≥ 3):** mobile app; fee payment processing itself; legacy
archive migration beyond active results; department-level dashboards.

**Success criteria:** must map to data-pack §G (p95 ≤ 2.0 s; SLA finish with
≥ 2 h margin; escapes ≤ 2; regression ≤ 25 min) — each with verification
method and verifier (QA lead, registrar acceptance).

**Risks:** accept any cause→event→effect chains (R1 vendor schema, R8 legacy
dates are the strongest candidates). Milestones: end B (schema), end E
(pipeline), end G (test pass), rollout H.

**Authority table (pass = concrete):** PM decides task-level re-sequencing
within float; escalates anything moving critical activities, any vendor SOW
change, any scope addition; sponsor decides funding and acceptance.

## Common wrong answers → correction

| Student error | Correction |
|---|---|
| "Make the portal fast and reliable" as objective | no measure, no target, no date — rewrite SMART |
| Out-scope omitted | every stakeholder assumption becomes a change request later |
| Success criteria = restated objectives | criteria are *verified evidence*, not aspirations |
| "PM manages the project" as authority | states nothing; need decide-alone vs escalate lists |
| Promise of mobile app "if time permits" | if time permits = no scope decision made; either in or out |

## Reflection answers (guidance)

1. **Preventing line:** the 48-hour SLA + load-test acceptance criteria — the
   2018 failure was publishing under peak load without performance evidence.
2. Common wants students must park: vendor SLA penalties for schema changes
   (R7 mitigation is contractual, not magical); "and also migrate 10 years of
   archives" — parking lot.
3. Signatories: registrar (sponsor, funds + accepts), vendor manager (SOW
   binding), IT head (capacity commitment). Signature = resources and
   decisions committed, not enthusiasm.

## Preparation notes for instructor

Run Lab 1 the same week as L06. Students will under-specify authority
limits — that is the teaching moment for the L06 escalation discussion.
Collect charters before Lab 2: Lab 2's stakeholder register needs a signed
charter to hang the register on.
