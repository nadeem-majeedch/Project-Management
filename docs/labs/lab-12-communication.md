---
title: "Lab 12 — Communication Plan"
lab: 12
week: 10
lecture: 20
time: "2 hours in-lab + 1 hour refinement"
deliverable: "Communication matrix + channel rules + governance comms"
submitted: "LMS, within one week"
---

# Lab 12 — Communication Plan

## 1. Objectives
1. Design the communication matrix from Lab 2's stakeholder needs — one row per *need*, not per person.
2. Install the channel rules that prevent the 2018 failure modes (worse-earlier, n+1, escalation ladder).
3. Specify governance communication: RAG dashboard, CCB minutes, change log, escalation memos.

## 2. Background & scenario
Week 9 ended badly: the E-claim audit (Lab 13 preview) and a stalled vendor
integration are now public knowledge inside the university. The registrar's
trust took a hit — not because of the numbers, but because she heard about
the audit from the QA lead's status email *after* asking "how are we doing?"
in a corridor. The 2018 pattern is repeating. Your communication plan is the
fix: rules that make bad news travel *faster* than good news.

## 3. Required tools
- [Communication plan template](../templates/communication-plan-template.md)
- Lab 2 stakeholder register (needs + engagement gaps)
- [Data pack story + §D status](data-pack.md)

## 4. Step-by-step instructions
1. **Needs-first table (25 min).** From the register: every stakeholder × what they need to know × why. Merge into needs-rows (the registrar's "weekly confidence read" and "early warning" are two rows, not one).
2. **Matrix (30 min).** For each need: channel, cadence, owner, artifact, feedback loop (who responds, how fast). Include students-as-users: what do they get, and through whom?
3. **Channel rules (20 min).** Write the escalation ladder with SLAs per rung; the n+1 rule; the worse-earlier deadline (≤ 24 h of confirmation); meeting hygiene.
4. **Governance comms (25 min).** Specify the four artifacts: RAG dashboard contents, CCB minutes (decisions + recorded dissent), change log, escalation memo format (situation/complication/question/answer).
5. **Failure-mode check (15 min).** For each of the four failure modes in the template: the specific rule in your plan that prevents it. If a rule is missing, add it.
6. **Refine (out of lab, 1 h).**

## 5. Your tasks (checklist)
- [ ] Needs table traces to Lab 2 register IDs
- [ ] Matrix rows are needs, each with feedback loop + SLA
- [ ] Escalation ladder with SLAs; n+1 and worse-earlier rules written
- [ ] Four governance artifacts specified
- [ ] Failure-mode table completed with your own prevention rules

## 6. Expected outputs
`communication-plan.md`. Submit via LMS.

## 7. Reflection questions
1. Which single rule in your plan would have prevented the corridor-trust failure of week 9? Quote it.
2. Students are thousands of stakeholders — the matrix can't give each a row. What is your aggregation strategy, and who owns it?
3. The n+1 rule costs the team time (writing proposals with problems). When is that cost *wrong* to pay?

## 8. Assessment rubric (pass / refine)
| Dimension | Pass | Refine |
|---|---|---|
| Needs-first | traces to register, merged into needs-rows | person-per-row |
| Matrix | feedback loop + SLA on every row | channel lists only |
| Channel rules | concrete SLAs and deadlines | platitudes |
| Governance artifacts | all four specified | dashboard only |
| Failure modes | specific prevention per mode | table left generic |

## 9. Related material
[Lecture 20 — Monitoring & control](../lectures/L20-20-monitoring-control.md) ·
[Lecture 26 — Communication & negotiation](../lectures/L26-26-communication-negotiation.md) ·
[Lab 15's recovery decision rides on these channels](lab-15-change-recovery.md)
