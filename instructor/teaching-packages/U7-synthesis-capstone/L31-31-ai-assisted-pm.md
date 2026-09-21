# Lecture 31 — AI-Assisted Project Management

> **Package for:** L31 · Week 16 · Unit U7 · CLO6 · Bloom: Evaluate/Create
> **Case anchor:** CS-42 (AI-drafted risk register critique)
> Companion: [`L31` skeleton](../../../docs/lectures/L31-31-ai-assisted-pm.md) · [CS-42 brief](../../../docs/cases/CS-42.md)

## Learning objectives

1. Map where AI tools genuinely help PM work (drafting, pattern-mining, rehearsal) vs where they mislead (invented references, confident wrong arithmetic).
2. Run a verification protocol on AI-generated PM artifacts (risk register, status summary) against the course's quality checklists.
3. Co-create and commit to the team's AI-use norms consistent with the course's integrity policy.
4. Defend an AI-assisted work product in a Q&A setting, including its limitations.

## Required prior knowledge

- L15 (risk register quality bar — the audit standard), L26 (honest
  communication), the [integrity & AI policy](../../../docs/assessments/academic-integrity.md)
  (the contract being extended to tools).

## Teaching notes

This lecture closes the course's integrity arc by *operationalizing* it: the
five-clause AI contract from the policy page becomes working practice. The
frame that keeps it honest: **AI is a powerful, over-confident junior
collaborator — brilliant at breadth, unaccountable for truth.** The skill
taught is *verification leadership*: using the tool for speed while owning
every fact that leaves your desk.

The session's engine is CS-42: an AI-drafted risk register for GRIDSENSE,
audited by teams against the exact quality bars the course taught —
normalization (cause-risk-effect), P×I evidence, family coverage (data risks
present?), duplicates, vague triggers. The finding pattern is stable across
years of such tools: fluent, plausible, structurally decent, *and* subtly
wrong — duplicated causes, orphaned effects, missing the data-family risks a
veteran would seed. Students discover that critique requires the very
judgment the course built — which is the lecture's thesis.

The norms co-creation (20 minutes) has teams write their *capstone AI norms*:
what tools for what tasks, disclosure line format (per policy), verification
duties per artifact. Norms get attached to the defense pack — the L32 Q&A
may probe them.

## Definitions & concepts

- **AI-assisted drafting** — first-pass structure/content generation;
  *verified* by the human author before it counts.
- **Verification protocol (course form)** — (1) provenance: what did the tool
  claim vs what can be traced; (2) quality bars: run the artifact through the
  course's checklist for that artifact type; (3) adversarial probe: ask the
  tool to attack its own output, then verify the attack; (4) human
  ownership: name what you changed and why.
- **Pattern-mining** — tools extracting candidate risks/insights from text
  corpora (status reports, tickets); output is *candidate*, not found fact.
- **Disclosure norm** — the policy's one-line template, applied per
  submission; disclosure ≠ confession, it is provenance hygiene.
- **Skill shift** — judgment, framing, stakeholder trust remain human; the
  tool leverages them, never replaces the accountability.

## Practical examples

**CS:** AI-drafted status report for the portal — strong: structure, neutral
tone, readable summary; failure mode: the "next steps" list contains a task
nobody decided (invented continuity); verification catches it against the
CR log (L20). Lesson: AI interpolates *plausible continuity*; your decision
log is the ground truth.

**DS:** AI-assisted churn-model risk mining (CS-42's actual case) — the tool
produces 22 risks; audit finds: 3 duplicates of one cause; 6 non-normalized
statements ("data quality concerns"); missing family: privacy/consent risks
absent entirely; one invented vendor (not in the case world). Verified yield:
~12 usable after normalization + family patch — faster than cold-start, and
*only* because the team could audit at the course's quality bar.

## Worked example

**CS-42 audit protocol, fully worked (board):**

| Audit check | Result on the AI draft |
|---|---|
| Normalization (cause→event→effect) | 14/22 pass; 6 have effect missing or generic ("delays") |
| Duplicate causes | 3 pairs merge → 19 distinct candidates |
| P×I evidence | none provided — probabilities uncited; scores must be re-derived (L15 discipline) |
| Family coverage | technical 11, vendor 3, people 2, **data-family 1** (a churn project needs ≥ 4: availability, label quality, drift, privacy) |
| Fabrication probe | "VendorSync" appears — not in the case world; deleted |
| **Verified yield** | **12 normalized risks, re-scored with evidence** — a starting register, not a register |

The workflow that emerges: *AI drafts → checklist audits → humans normalize
and evidence → register v1*. Speed-up ≈ 40% of the cold-start time, bought
with the audit discipline the course already taught — that is the honest
value proposition, and it is why the critique skill, not the tool, is the
learning objective.

## Common misconceptions

| Misconception | Correction |
|---|---|
| "AI output = analysis." | It is draft text with confident tone; analysis requires evidence and verification — which the tool cannot supply. |
| "Disclosure means I'm admitting to cheating." | The policy defines permitted use *with* disclosure; the violation is unverified fabrication, not tool use. Undisclosed use is the offense. |
| "AI will replace PM roles." | It automates artifact *drafting*; accountability, stakeholder trust, and judgment under ambiguity remain human — that is where this course's value lives. |
| "Popular tools are verified by popularity." | Verification is per-artifact, per-use; tool reputation is not a QA process. |
| "The register the AI wrote is faster to accept than to fix." | Accepting unaudited drafts moves the cost downstream — to your defense Q&A (L32) or your project's blind spots (L15's whole point). |

## Classroom activities

1. **CS-42 audit protocol (40 min):** teams audit the AI register with the
   six checks; annotated critique + corrected register v1 (the deliverable).
2. **Norms co-creation (25 min):** team AI norms sheet — tools/tasks matrix,
   disclosure line, verification duties per artifact; attached to defense
   pack.
3. **Own-register stress test (10 min):** teams run the audit checklist
   against *their own* A3 register — did human-authored work pass the same
   bar? (Usually a humbling 2–3 findings.)
4. **Probe drill (10 min):** three AI-drafted status snippets; find the
   invented continuity.

## Discussion questions

1. Which audit check found the most problems — and does that surprise you given the tool's fluency? What does fluency mask?
2. Your teammate used an AI tool for their case portfolio analysis *without* disclosure, and the analysis is excellent. What do the course norms require of you — and why does "it was excellent" not answer the question?
3. Where in *your* capstone would AI assistance be irresponsible even with disclosure? (Think: fairness evidence, acceptance criteria, anything feeding a governance decision.)

## Practical exercise

**In class:** CS-42 deliverable (critique + corrected register). **Take home
(20 min):** apply the verification protocol to one artifact of your capstone
(a register section or status summary drafted with AI assistance), attach the
disclosure line per policy, and note what you changed — defense-pack ready.

## Formative assessment (exit ticket)

1. Name four checks in the verification protocol.
2. Per the course policy, when is AI use a violation — tool use, or something else?
3. What did the fabrication probe catch in the worked example, and how?

## Reading & references

- Course policy: [Academic integrity & responsible AI](../../../docs/assessments/academic-integrity.md)
  — the five-clause contract, disclosure template.
- PMI. (2021). *PMBOK Guide* (7th ed.) — Uncertainty and Measurement domains
  (the quality bars the audit applies).
- [Case CS-42](../../../docs/cases/CS-42.md) — the AI-drafted register under audit.

## Two-hour teaching plan

| Slot | Segment | Materials |
|---|---|---|
| 0:00–0:10 | Hook: the beautifully written, entirely wrong status report | — |
| 0:10–0:25 | Value map: where AI helps/fails; skill shift | board |
| 0:25–0:50 | Worked example: the six-check audit protocol | board table |
| 0:50–1:00 | Break | |
| 1:00–1:40 | CS-42 audit + norms co-creation | CS-42 brief, norms sheet |
| 1:40–1:50 | Own-register stress test | own artifacts |
| 1:50–1:57 | Defense-week logistics (L32 order, rehearsal slots) | — |
| 1:57–2:00 | Exit ticket | slips |

## Instructor preparation notes

- Prepare the AI-drafted register (CS-42's artifact) in advance with the
  planted flaws listed in the worked example — regeneration per semester
  keeps it current; record the flaw key in the
  [answer keys](../../answer-keys/README.md) area.
- Norms co-creation needs a template sheet; collect per team today (defense
  pack item).
- If your institution has specific AI guidance, reconcile the course norms
  with it before this session and say so explicitly.

## Linked resources

- Lecture skeleton: [`docs/lectures/L31`](../../../docs/lectures/L31-31-ai-assisted-pm.md)
- Case: [CS-42](../../../docs/cases/CS-42.md)
- Policy: [integrity & AI](../../../docs/assessments/academic-integrity.md)
- Forward: [capstone defense L32](../../../docs/lectures/L32-32-capstone-synthesis.md) —
  AI norms and verified artifacts join the defense pack.
