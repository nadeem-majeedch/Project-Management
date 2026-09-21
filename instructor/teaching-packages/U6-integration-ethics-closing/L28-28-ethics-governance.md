# Lecture 28 — Ethics, Governance & Professional Responsibility

> **Package for:** L28 · Week 14 · Unit U6 · CLO6 · Bloom: Evaluate
> **Case anchor:** CS-39 (four ethics dilemmas in writing) · homework lane: CS-100 (privacy collision)
> Companion: [`L28` skeleton](../../../docs/lectures/L28-28-ethics-governance.md) · [CS-39 brief](../../../docs/cases/CS-39.md)

## Learning objectives

1. Apply the four PMI Code of Ethics values (responsibility, respect, fairness, honesty) to concrete delivery dilemmas, distinguishing aspirational from mandatory standards.
2. Design a project governance model: decision rights, escalation paths, gates, and audit evidence.
3. Run an ethics decision protocol (legality → policy → harm → disclosure) on a data-ethics collision.
4. Identify the reporting obligations that survive hierarchy pressure — and the career-safe ways to discharge them.

## Required prior knowledge

- L26 (bad-news delivery — the reporting muscle ethics depends on).
- L23/L14 (fairness thresholds and DQ gates — governance objects).
- The [integrity & AI policy](../../../docs/assessments/academic-integrity.md) — today generalizes it to professional practice.

## Teaching notes

**Deliberately non-quantitative.** The risk in teaching ethics is moralizing;
the risk in teaching governance is org-chart recitation. Both are avoided by
doing: students *apply* the Code to written dilemmas (CS-39) and *design* a
governance model for their capstone (workshop artifact). The instructor's
discipline: never tell students the "right answer" first — position papers
are defended against the values, then critiqued for *operational* gaps (what
does the decision cost, who bears it, what happens next quarter).

Frame the Code honestly: it binds PMI members contractually, but the four
values function as the profession's *shared reasoning standard* — useful even
where unenforceable. Distinguish **aspirational** (we strive) from **mandatory**
(we must; e.g., mandatory honesty about qualifications, mandatory reporting of
violations) — students learn that the *mandatory* layer is where careers are
actually protected or lost.

The governance segment connects the semester: the CCB (L20), the model gate
(L23), the steering cadence (L24) are all *governance objects*; today names
the pattern — decision rights, evidence, cadence, escalation — and the
capstone's governance section gets designed with it.

## Definitions & concepts

- **PMI Code of Ethics values** — *responsibility* (own decisions and their
  consequences), *respect* (others' resources, capabilities, differences),
  *fairness* (conflict-of-interest hygiene, impartiality), *honesty* (truthful
  reporting and communication).
- **Aspirational vs mandatory standards** — strive-to vs must-do; violations
  of the mandatory layer carry process consequences.
- **Governance model** — the project's decision system: which body decides
  what (decision rights), on what evidence, at what cadence, with what
  escalation path.
- **Ethics decision protocol (course form)** — (1) legality, (2) policy/Code,
  (3) harm analysis (who bears it, how reversible), (4) disclosure duty and
  channel.
- **Escalation** — moving a decision/risk to the body *authorized* for it
  (L17's escalate strategy, formalized); not an admission of failure.

## Practical examples

**CS:** governance model for the portal rewrite — sponsor owns scope/budget
decisions (weekly written state); CCB (L20) owns baseline changes; tech lead
owns architecture (decision rights registered); escalation path:
PM → sponsor → steering (with evidence pack template). The dilemma: the
registrar (sponsor) asks you to quietly drop the accessibility fixes to hit
the date. Protocol walk: legal? (possibly not — disability obligations);
policy? (quality metrics said zero high-severity violations — L14's
criteria); harm? (excluded students, retro-fit cost later); disclosure?
(you cannot report it as "done" — honesty is mandatory). Options: descope
*publicly* with the sponsor's signature, not silently.

**DS:** the churn model's fairness threshold is breached two weeks before
the board demo (the L26 bad-news thread, now with ethics teeth). Protocol:
legal? (discrimination exposure); policy? (threshold was a recorded
governance decision); harm? (segmented customers, trust); disclosure?
(board, regulator-shaped stakeholders). The professional spine: *the
threshold outlives the demo* — governance decisions bind, and honoring them
upward is the DS track's defining integrity test.

## Worked example

**Capstone governance model, fully designed (board template):**

| Decision class | Decider | Evidence required | Cadence | Escalation |
|---|---|---|---|---|
| Scope/baseline changes | CCB (chair: PM) | impact analysis all baselines (L20) | weekly | sponsor |
| Model/feature release gate | model risk owner + PO | gate checklist complete (L23 DoD) | per release | sponsor |
| Data access/approval | data steward | DQ rules + purpose statement (L14) | on request | sponsor+legal |
| Architecture | tech/data lead | ADR (architecture decision record) | as needed | tech review |
| Emergency production fix | on-call lead | incident ticket + retro within 24 h | immediate | sponsor (notify) |

Teach the reading: *evidence* column = the artifact each decision consumes
(the semester's artifacts reassembled as governance); *escalation* column =
pre-agreed paths that make escalation routine, not dramatic. Then the audit
question: which of these decisions, if challenged in a year, could you
*reconstruct* from records? What's missing is the audit-log line item.

**Ethics protocol applied (the registrar dilemma above)** — walk all four
steps on the board with the position-paper conclusion: descope publicly +
document, and register the *secondary risk* (retro-fit cost) with an owner.

## Common misconceptions

| Misconception | Correction |
|---|---|
| "Ethics = legality." | Legal is the floor; the Code's values bind conduct the law leaves open (fairness, honesty in gray zones). |
| "The Code is for PMI members; I'm not certified." | The values are the profession's reasoning standard; employers and courts read conduct against them regardless of membership. |
| "Governance slows delivery." | *Ungoverned* delivery slows later — rework, disputes, audit failures; governance is pre-agreed speed (L20's CCB with teeth). |
| "Escalating means I failed." | Escalation is the designed route for decisions above your authority; sitting on them is the failure (and a Code violation when harm follows). |
| "Whistleblowing is the only ethical option under pressure." | The ladder is: raise → document → escalate → refuse to falsify → external channels last; most situations resolve at step 2 — knowing the ladder prevents both panic and martyrdom. |

## Classroom activities

1. **CS-39 dilemma workshop (40 min):** four written dilemmas (padded
   estimates under instruction; hidden defect found late; record-level data
   requested for convenience; favoritism in task assignment). Position
   papers ≤ 250 words each mapped to Code values + the four-step protocol.
2. **Governance design sprint (30 min):** capstone governance model using the
   worked-example table; peer audit: "could you reconstruct this decision in
   a year?"
3. **Red-flag drill (10 min):** six one-line scenarios; teams shout the
   violated value + the mandatory/aspirational call.

## Discussion questions

1. In the padding dilemma (CS-39), who is *more* ethical: the engineer who pads silently to protect the team, or the one who refuses and reports the pressure upward? Defend with the Code, then with consequences.
2. Which row of your governance model will be tested first this semester — and is the evidence column ready?
3. What is the difference between *loyalty to a sponsor* and *responsibility to stakeholders* — and where did that difference cost someone in L01's failure cases?

## Practical exercise

**In class:** CS-39 deliverable (position papers) + governance model
(capstone section). **Take home (25 min):** write the capstone's
governance + ethics section: governance table, the ethics protocol applied to
*your* project's most likely dilemma, and the AI-disclosure norms your team
adopts (links to the course's [integrity & AI policy](../../../docs/assessments/academic-integrity.md)).

## Formative assessment (exit ticket)

1. Name the four Code values; which two are *most* tested by the padding dilemma?
2. What four columns must a governance decision row have?
3. Step 1 of the ethics protocol is ___; the last-resort step is ___.

## Reading & references

- PMI. *Code of Ethics and Professional Conduct* — the four values,
  aspirational vs mandatory sections (free, pmi.org).
- PMI. (2021). *PMBOK Guide* (7th ed.) — stewardship principle; governance
  in the delivery system.
- ISO 21502:2020 — governance vocabulary (decision rights, gates).
- [Integrity & AI policy](../../../docs/assessments/academic-integrity.md) —
  the course-level contract students already operate under.

## Two-hour teaching plan

| Slot | Segment | Materials |
|---|---|---|
| 0:00–0:08 | Hook: the two-weeks-before-the-board fairness breach | — |
| 0:08–0:25 | Code values; aspirational vs mandatory; the escalation ladder | Code excerpt |
| 0:25–0:40 | Governance anatomy: rights/evidence/cadence/escalation | board table |
| 0:40–0:50 | Worked example: governance table + protocol walk | board |
| 0:50–1:00 | Break | |
| 1:00–1:40 | CS-39 workshop | dilemma sheets |
| 1:40–1:55 | Governance sprint + red-flag drill | audit checklist |
| 1:55–2:00 | Exit ticket | slips |

## Instructor preparation notes

- Prepare the four dilemma sheets with *no* embedded verdicts; your role is
  protocol enforcement, not moral verdicts — keep the class's disagreement
  productive by forcing the harm-analysis step.
- Write the red-flag scenarios so each clearly maps to one value; two are
  aspirational-layer, four mandatory-layer.
- CS-100 (privacy collision) is homework-lane: announce it as the DS track's
  extension of today (portfolio-eligible).

## Linked resources

- Lecture skeleton: [`docs/lectures/L28`](../../../docs/lectures/L28-28-ethics-governance.md)
- Case: [CS-39](../../../docs/cases/CS-39.md) · CS-100 (homework lane, [case directory](../../../docs/cases/index.md))
- Capstone: [charter & tracks](../../../docs/capstone/capstone-charter.md) — governance section
- Integrity: [academic integrity & AI](../../../docs/assessments/academic-integrity.md)
- Forward: [sustainability & benefits L29](../../../docs/lectures/L29-29-sustainability-benefits.md).
