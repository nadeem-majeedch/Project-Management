<!--
Template: Risk register (Lab 9; feeds A3 and the capstone)
Statement discipline: CAUSE → EVENT → EFFECT, no bare nouns.
Scoring: P (1–5, within project horizon); impact S/C/Q each 1–5;
declared score = max(S,C,Q) × P. Every risk gets owner, response, trigger,
and residual — a risk without a trigger cannot be managed.
-->

# Risk Register — [Project name]

| ID | Cause → Event → Effect | P | S | C | Q | Score | Band | Response strategy | Action (what/who/when) | Trigger | Residual P | Residual I |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | | | | | | | | | | | | |

*(seed rows: copy the 8 from `campus-mend-risks.csv`, add ≥ 8 of your own —
people, vendor, data-quality, security/privacy, governance, and at least one
opportunity.)*

## Response strategy cheat-sheet
| Threat strategy | Use when |
|---|---|
| Avoid | cause is removable (change plan/requirement) |
| Mitigate | reduce P or I below a threshold; fund the action |
| Transfer | a contract/insurance carries it better than you |
| Accept (active) | watch + trigger + funded fallback |
| Accept (passive) | Low band; no action, reviewed at gates |
| Escalate | outside your authority (e.g. R4-type constraint) |

Opportunities: exploit / share / enhance / accept — same discipline.

## Register health checks (before submitting)
| Check | Result |
|---|---|
| Every statement has all three parts (cause/event/effect) | ☐ |
| No issues disguised as risks (already happening = issue list) | ☐ |
| At least one opportunity with an exploit/enhance action | ☐ |
| Every High/Critical has a funded action + trigger | ☐ |
| Residual scores stated for all mitigated risks | ☐ |
| Realized risks (e.g. R4) moved to constraints with an escalation note | ☐ |
