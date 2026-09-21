# Lab 9 Answer Key — Risk Register

## Seed register completed (model responses)

| ID | Score/Band | Response | Action (model) | Trigger | Residual |
|---|---|---|---|---|---|
| R1 vendor schema | 12 High | Mitigate | joint schema-change SLA + adapter contract tests in CI (owner: PM + vendor mgr; by end B) | vendor change-request hits F's scope | P 3→2, I 4→3 |
| R2 DE resignation | 10 Medium | Mitigate | pair-second on D/E; pipeline runbook by end D | DE gives notice during wks 5–14 | P 2→2, I 5→3 |
| R3 label eras | 15 High | Mitigate | era-mapping audit at D gate + era-consistency test in suite (owner: QA) | era test fails on any release build | P 3→2, I 5→4 |
| R4 calendar rule | realized | — | constraint; escalated to sponsor at charter; H's acceptance requires SLA evidence | n/a | n/a |
| R5 governance evidence | 12 High | Mitigate | pre-agree evidence templates with audit office before G | audit office rejects G's evidence pack | P 4→3, I 3→2 |
| R6 GPU quota | 6 Medium | Accept (active) | reservation request now; batch-time fallback documented | quota cut during D/E | — |
| R7 vendor slip | 8 Medium | Mitigate + transfer | week-9 checkpoint clause in SOW; F start buffer from float | vendor misses wk-9 checkpoint deliverable | P 2→2, I 4→3 |
| R8 legacy dates | 16 Critical | Mitigate | date-format census in legacy audit (A) + parsing test suite (owner: DE) | migration dry-run defects > threshold | P 4→2, I 4→3 |

**Extension families (pass requires all + 1 opportunity):** people (second
on DE, QA single-point), vendor (R7 covers), data quality (era drift in
*new* data, peak-replay data mismatch), security/privacy (student PII in
analytics repo — access design + audit), governance (evidence templates,
R5), **opportunity (model):** "Analytics repo schema reusable for registrar's
KPI dashboards (P3/I3) — *enhance*: discuss phase-2 funding with registrar
at G gate; abandon trigger: recovery plan consumes all slack."

## Score arithmetic (checker-verified)

R1 12 High · R2 10 Medium · R3 15 High · R5 12 High · R6 6 Medium ·
R7 8 Medium · R8 16 Critical. Own risks must follow score = max(S,C,Q) × P
and the band table; checker validates rows students add to the worksheet CSV.

## Common wrong answers

| Error | Correction |
|---|---|
| "Risk: vendor" | cause → event → effect required; bare nouns rejected |
| Response "monitor closely" on High | High needs funded action + trigger; monitoring is for Medium |
| Trigger = restated risk | trigger is the *observable early signal*, not the event itself |
| Residual = 0 | mitigation reduces, rarely eliminates; residual < primary, ≠ zero |
| R4 kept as open risk | realized → constraint + escalation; keeping it is register pollution |
| All risks negative | missed opportunity family — exploit/enhance discipline required |

## Reflection guidance

1. R8 (P4) gets the funded action first — the cause (ambiguous formats,
   *known now*) is cheap to attack in package A; R2's low P but huge I
   justifies cheap mitigation (pairing), not first funding. Score orders
   attention; cause orders action.
2. Model answer: R1 mitigation via contractual SLA increases R7-style
   adversarial friction (cost dimension worsens while schedule improves) —
   trades across dimensions are normal; declare them.
3. Opportunity exploit costs effort from D's team; abandon when the
   recovery plan (Lab 15) consumes the slack that made it affordable.

## Preparation notes

Grade statements hard — statement discipline is the transferable skill.
The worksheet CSV + checker catch arithmetic, freeing you to read *triggers*,
which is where quality lives. Lab 10 needs this register complete.
