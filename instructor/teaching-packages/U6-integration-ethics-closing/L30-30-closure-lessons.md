# Lecture 30 — Closing Projects & Lessons Learned

> **Package for:** L30 · Week 15 · Unit U6 · CLO6 · Bloom: Evaluate · **Capstone master plan v2 due today**
> **Case anchor:** CS-41 (course retrospective as closure drill) · homework lane: CS-102 (closure failure audit), CS-103 (lessons-to-template)
> Companion: [`L30` skeleton](../../../docs/lectures/L30-30-closure-lessons.md) · [CS-41 brief](../../../docs/cases/CS-41.md)

## Learning objectives

1. Execute closure: acceptance verification, contract/administrative closure, resource release, archive.
2. Distinguish closure activities that protect the *product* (handover — L29) from those that protect the *organization* (records, lessons, re-use).
3. Run a structured retrospective (three formats) and convert findings into changed templates, not meeting notes.
4. Apply the closure checklist to the capstone — and defend its completion at the defense.

## Required prior knowledge

- L29 (handover package), L27 (the plan being closed), L20 (the baselines
  being verified).

## Teaching notes

Closure is the most-skipped phase in real projects and the least-taught in
most curricula. The teaching frame: **closure is a deliverable-producing
phase, not an ending.** Three products: (1) verified acceptance (against the
charter's success criteria — L06 returns for its final audit), (2) the
re-useable record (archive, lessons-learned → *template changes*), (3) clean
exits (people, contracts, access).

The lessons-learned failure mode gets special treatment: organizations run
retros that produce beautiful notes nobody reads. The re-use pipeline is the
fix: finding → owner → *template/checklist/checklist-row change* → next
project's phase-0. CS-103 (homework lane) designs exactly this pipeline;
today's closure checklist workshop practices the intake side.

The capstone's own closure runs as the worked exercise: teams complete the
checklist against *their* project (it becomes a defense artifact) — and the
session's final 40 minutes run the course's own retrospective (CS-41), which
doubles as live retro-format practice. Feed the course's findings into your
own lessons-to-template pipeline visibly (an LMS announcement listing template
changes made) — modeling the lecture's core idea.

## Definitions & concepts

- **Acceptance verification** — formal confirmation against success criteria
  (charter, L06) and acceptance criteria (WBS dictionary, L09); *signed*, not
  assumed.
- **Contract closure** — vendor deliverables verified, claims settled,
  contract formally closed (distinct from technical completion).
- **Administrative closure** — records archived per policy, access revoked or
  transferred, financials reconciled, team released with recognition.
- **Lessons learned (done right)** — finding → root cause → owner → *system
  change* (template/checklist/process) → adoption check at next project start.
- **Retrospective formats** — timeline walk, sailboat (wind/anchors),
  start/stop/continue; choice depends on team mood and event density.
- **Archive discipline** — findable, complete, *with* the context (decisions
  and why), or it is a junk drawer.

## Practical examples

**CS:** portal rewrite closure — acceptance: the SMART criteria from L06
(11 min → 4 min, ≥ 90% enrollments) verified from system logs, *signed by
registrar*; contract closure: the UX contractor's deliverables verified
against the SOW; administrative: old system access scheduled (2-week
parallel), archive includes decision log + change log (L20's CCB minutes) —
the archive that answers "why did we descope reports?" in 2029.

**DS:** churn model closure — acceptance: gate evidence + holdout results
signed by retention director; handover acceptance (L29) confirmed by ops
lead; lessons: "era-bound labels" finding becomes a *data-contract template
clause* for the next CRM-dependent project; archive includes the model card
and the experiment log (negative results included — they are the reusable
knowledge).

## Worked example

**Capstone closure checklist, fully populated (board):**

| # | Closure item | Evidence | Owner | Status at L30 |
|---|---|---|---|---|
| 1 | Acceptance vs charter criteria | criteria table (L06) + measurements | PM + sponsor | measured, signature pending defense |
| 2 | Work-package acceptance | WBS dictionary acceptance criteria (L09) | package owners | complete except spike #3 (documented) |
| 3 | Contract closure (if any vendor) | SOW checklist (L18) | PM | n/a — no vendors |
| 4 | Risk register final state | residuals + secondaries dispositioned | risk owners | done at last review |
| 5 | Change log completeness | CR decisions (L20) archived | PM | 7 CRs, all minuted |
| 6 | Archive package | repo, decision log, experiment log, model card | PM | in progress |
| 7 | Access & license transitions | access matrix (L04 RACI) | tech lead | pending handover date |
| 8 | Team release + recognition | individual memos (rubric), thanks | sponsor | at defense |
| 9 | Lessons → template change | ≥ 2 findings with system changes | team | drafted today |
| 10 | Benefits measurement plan live | benefits map owners notified (L29) | benefit owners | notified |

Teach the reading: items 1, 6, 9, 10 are the *organizational memory* half —
the half that survives the team; the rubric's "completeness" dimension reads
this table at the defense.

## Common misconceptions

| Misconception | Correction |
|---|---|
| "Closure = the last demo." | The demo is delivery; closure is verification, records, exits — a distinct, checklisted phase. |
| "Lessons learned is a meeting." | The meeting is intake; the *product* is a system change adopted by the next project — notes alone are archaeology. |
| "Archive means dumping the drive." | An archive without decision context is a junk drawer; the why-log is the artifact. |
| "Recognition is HR fluff." | Clean, recognized exits are how organizations get re-useable knowledge voluntarily next time. |
| "We can close while contracts/access are open." | Open access is a standing security exposure; closure *closes* it on a date. |

## Classroom activities

1. **Closure checklist workshop (30 min):** teams populate the checklist for
   their own capstone (evidence/owner/status per item); gaps become defense
   talking points, honestly framed.
2. **Course retrospective (CS-41, 35 min):** three formats in sequence —
   timeline walk (10), sailboat (15), start/stop/continue (10); output ≥ 3
   findings, each converted into a *template/course-structure change* with an
   owner (the instructor).
3. **Retro-anti-pattern drill (10 min):** given four retro transcripts, spot
   the failure (blame drift, no decisions, all-positives, no follow-up).

## Discussion questions

1. Which closure item for your capstone is *faked-able* — and what evidence would make faking it pointless?
2. Why do organizations keep running lessons-learned meetings that change nothing? What would you institutionalize instead? (CS-103's design.)
3. The course retrospective just produced a finding about *this course*. What should its "template change" be — and who verifies adoption next semester?

## Practical exercise

**In class:** checklist for capstone (item 10 above is the take-home from
L29, now verified) + retro output. **Take home (30 min, capstone):** lessons
memo — ≥ 2 findings from *your own project* converted into concrete system
changes (template clause, checklist row, process step) with owners. Attach to
the defense pack.

## Formative assessment (exit ticket)

1. Closure protects two different things — name them (product vs organization) with one activity each.
2. What converts a lesson into learning?
3. Which item on the checklist survives the team's dissolution? (The archive + benefits measurement.)

## Reading & references

- PMI. (2021). *PMBOK Guide* (7th ed.) — Project Work domain (closure
  practice); Delivery domain (acceptance).
- PMI. (2017). *PMBOK Guide* (6th ed.) — "Close Project or Phase" (the
  canonical closure process).
- [Capstone rubric](../../../docs/capstone/capstone-rubric.md) ·
  [defense format](../../../docs/capstone/defense-format.md) — the checklist
  feeds both.

## Two-hour teaching plan

| Slot | Segment | Materials |
|---|---|---|
| 0:00–0:10 | Hook: the project that "ended" and kept billing (CS-102 teaser) | — |
| 0:10–0:28 | Closure anatomy: acceptance/contract/administrative; archive discipline | board |
| 0:28–0:50 | Worked example: checklist + lessons-to-template pipeline | board table |
| 0:50–1:00 | Break | |
| 1:00–1:30 | Capstone checklist workshop | checklist template |
| 1:30–1:55 | Course retrospective (3 formats) | boards/sticky notes |
| 1:55–2:00 | Exit ticket + v2 sign-off queue | slips |

## Instructor preparation notes

- v2 sign-off logistics: collect master-plan submissions today; defense
  order publishes within 48 h (L32 planning depends on it).
- Retro facilitation: timebox ruthlessly (35 min total) — the formats are
  the *practice*, not the therapy; capture findings in writing live.
- Model the pipeline: commit to one visible course-structure change from the
  retro before L32 (an LMS post naming it) — credibility for the lesson.

## Linked resources

- Lecture skeleton: [`docs/lectures/L30`](../../../docs/lectures/L30-30-closure-lessons.md)
- Case: [CS-41](../../../docs/cases/CS-41.md) · CS-102/CS-103 (homework lane, [case directory](../../../docs/cases/index.md))
- Capstone: [rubric](../../../docs/capstone/capstone-rubric.md) ·
  [defense format](../../../docs/capstone/defense-format.md)
- Forward: [AI-assisted PM L31](../../../docs/lectures/L31-31-ai-assisted-pm.md) ·
  [defense L32](../../../docs/lectures/L32-32-capstone-synthesis.md).
