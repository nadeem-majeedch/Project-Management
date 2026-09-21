# Lecture 06 — Project Charter & Business Case

> **Package for:** L06 · Week 3 · Unit U2 · CLO1, CLO2 · Bloom: Apply
> **Case anchor:** CS-08 (one-page charter under pressure)
> Companion: [`L06` skeleton](../../../docs/lectures/L06-06-charter.md) · [CS-08 brief](../../../docs/cases/CS-08.md)

## Learning objectives

1. Write a one-page charter with objectives, success criteria, authority, and milestones.
2. Distinguish a business case from a charter and state what each answers.
3. Draft SMART success criteria for a software *and* a data project.
4. Peer-review a charter against a 10-point checklist.

## Required prior knowledge

- L02 (where charter objectives come from: portfolio intent).
- L04 (who signs what: sponsor accountability).

## Teaching notes

Students have written "project charters" before that were title pages plus
vibes. Today's bar is different: **a charter is a contract of intent between
sponsor and team** — it authorizes the PM to spend, sets measurable success,
and names decision authority. The business case asks *"is it worth it?"*; the
charter asks *"who is authorized to make what real?"* — keep the pair clean.

Structure: anatomy of the one-pager (12 minutes of template walk), then the
SMART criteria clinic — the heart of the session, because vague objectives are
the charter's most common disease — then CS-08 under a 40-minute clock with
peer review. The pressure is deliberate: messy briefs are the reality; the
skill is producing a defensible one-pager anyway.

Capstone hook: teams form at L08 and their first deliverable is exactly this
document — today's clinic is their rehearsal.

## Definitions & concepts

- **Business case** — problem, options (including do-nothing), expected
  benefits, costs, risks; the *investment* argument.
- **Charter** — objectives, success criteria, high-level scope, milestones,
  sponsor, PM authority, key assumptions; the *authorization* document.
- **SMART** — specific, measurable, achievable, relevant, time-bound (apply
  strictly to *success criteria*, not aspirations).
- **Do-nothing baseline** — the counterfactual every benefit claim must beat.
- **Assumption register seed** — charters carry assumptions that later become
  risks (first look; full treatment L15).

## Practical examples

**CS (CampusHub):** success criteria — "Reduce average course-registration
time from 11 min to under 4 min by the start of fall registration (Sep 7),
for ≥ 90% of undergraduate enrollments." Contrast with the vague original:
"Make registration faster and easier."

**DS (TelcoCare):** "Deploy a churn model achieving ≥ 0.25 lift on the top
decile against the live control, measured on a 6-week holdout, with a
fairness gap across age bands ≤ 5 percentage points, by Q3." — note the three
layers: performance, measurement window, fairness bound. Data charters fail
when the fairness/monitoring layer is missing (returns as a *model risk gate*
in L23).

## Worked example

**Business-case vs charter traceability chain (board exercise):**

> Portfolio intent: reduce first-year churn 10%.
> Benefit: 10% churn reduction ≈ retained revenue (finance supplies the
> number — the PM never invents it).
> Objective (charter): ship a churn-scoring service + retention playbook to
> the two highest-churn segments by Q3.
> Success criteria: the DS example's SMART triplet above.
> Authority: PO may reprioritize backlog within the two segments; scope
> beyond them needs sponsor sign-off.
> Milestones: M1 data audit complete (wk 4) · M2 model gate passed (wk 14) ·
> M3 controlled rollout (wk 20).

Then break it on purpose: remove the holdout window from the success
criterion and ask what happens (arguments forever; "lift" becomes
unmeasurable; gate collapses). **Lesson: the measurability clause is the
charter.**

## Common misconceptions

| Misconception | Correction |
|---|---|
| "The charter is a formality we fill in later." | It is the authorization contract; skipping it hands all negotiation to whoever is loudest later. |
| "Success criteria can be added at the end." | Criteria define the target *before* work; post-hoc criteria are moving goalposts (and an integrity issue). |
| "Business case = budget spreadsheet." | The case argues *benefits vs options*; money is one row. |
| "A signed charter means scope is frozen." | Charter fixes intent and authority; scope detail arrives via planning (L09) and changes via control (L20). |

## Classroom activities

1. **Criteria clinic (15 min):** rewrite four broken criteria ("user-friendly
   dashboard", "better data quality", "faster system", "actionable insights")
   into SMART form — pairs, then board critique.
2. **CS-08 charter sprint (40 min):** messy sponsor brief → one-page charter;
   hard clock, no extensions (that is the exercise).
3. **Peer review gauntlet (15 min):** swap charters, score against the
   10-point checklist, write the single most damaging question your peer's
   charter cannot answer.

## Discussion questions

1. Whose signature does your CS-08 charter actually need — and what happens if that person refuses?
2. For a DS charter, who must agree the fairness threshold before model work starts? What if they cannot?
3. Which is the bigger risk to a project: a weak business case or a vague charter? Why do they so often travel together?

## Practical exercise

**In class:** CS-08 deliverable (the charter, peer-scored). **Take home
(30 min):** draft the *success criteria block only* for your future capstone
team's project (teams form L08) — bring two copies: one software-flavored, one
data-flavored, for your team to choose between.

## Formative assessment (exit ticket)

1. Business case answers ___, charter answers ___.
2. Rewrite as SMART: "improve data quality" (one line).
3. Who authorizes the PM in a charter?

## Reading & references

- PMI. (2021). *PMBOK Guide* (7th ed.) — Planning domain; Stakeholders
  domain (sponsor role).
- ISO 21502:2020 — governance/authorization vocabulary.
- [Templates](../../../docs/resources/templates.md): charter skeleton (Lab 1
  uses it next week).

## Two-hour teaching plan

| Slot | Segment | Materials |
|---|---|---|
| 0:00–0:10 | Hook: the project that "succeeded" with no success criteria | — |
| 0:10–0:25 | Anatomy: business case → charter chain | one-pager template |
| 0:25–0:45 | SMART criteria clinic | broken-criteria sheet |
| 0:50–1:00 | Break (after clinic wrap) | |
| 1:00–1:40 | CS-08 charter sprint (hard clock) | CS-08 brief |
| 1:40–1:55 | Peer review gauntlet | 10-point checklist |
| 1:55–2:00 | Exit ticket | slips |

## Instructor preparation notes

- Prepare the messy sponsor brief (CS-08): include one contradictory
  requirement and one unnamed budget constraint — both are traps the checklist
  should catch.
- Print the 10-point checklist; peer scoring needs hard copies.
- Lab 1 (charter drafting) runs in the same week — coordinate: lab uses the
  team's own project, lecture used CS-08.

## Linked resources

- Lecture skeleton: [`docs/lectures/L06`](../../../docs/lectures/L06-06-charter.md)
- Case: [CS-08](../../../docs/cases/CS-08.md)
- Template: [charter skeleton](../../../docs/resources/templates.md) ·
  Lab 1: [labs index](../../../docs/labs/index.md)
- Forward: [capstone charter requirements](../../../docs/capstone/capstone-charter.md)
