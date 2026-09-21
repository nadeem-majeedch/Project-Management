# Lecture 04 — Roles, Competencies & the PM Profession

> **Package for:** L04 · Week 2 · Unit U1 · CLO1 · Bloom: Remember
> **Case anchor:** CS-05 (RACI for the CampusHub portal team) · **Quiz 1 today (L01–L04)**
> Companion: [`L04` skeleton](../../../docs/lectures/L04-04-roles-profession.md) · [CS-05 brief](../../../docs/cases/CS-05.md)

## Learning objectives

1. Name the roles on a technical project (sponsor, PM, product owner, scrum master, tech/data lead) and their core accountabilities.
2. Build a RACI matrix and flag ambiguities where accountability is unclear.
3. Describe the PMI Talent Triangle and locate their own development on it.
4. Distinguish certification signals (CAPM, PMP, PMI-ACP) without confusing them with competence.

## Required prior knowledge

- L01–L03 vocabulary (domains, roles encountered informally).
- Students' own project experience (they will mine it today).

## Teaching notes

Careful with this lecture: it can collapse into a boring taxonomy. Make it
personal and contentious instead — the *hard* truth is that role confusion,
not ignorance, causes most governance failures. The session's spine:
(1) roles via a war story of a decision nobody owned; (2) RACI as the repair
tool — built live; (3) competence as more than title (Talent Triangle);
(4) honest framing of certifications: they open doors, they don't make
judgment.

Run **Quiz 1 (10–15 min) at the start** covering L01–L04 reading; keep the
post-quiz time protected for CS-05 — it is the densest activity of U1.

Watch the CS/DS symmetry: data projects add roles students haven't met —
data steward, model risk owner — preview them here (full treatment in the DS
spine, L14/L23).

## Definitions & concepts

- **Sponsor** — owns the benefit and the money; authorizes the project;
  resolves escalations. Not a figurehead.
- **Project manager** — integrates scope, schedule, risk, communication; runs
  the management system (whatever the life cycle).
- **Product owner** — owns the *what and why* of the product backlog
  (Scrum accountability; Scrum Guide 2020).
- **Scrum master** — owns the *process health and team effectiveness*, not
  people management.
- **Tech lead / data lead** — owns technical decisions and quality bar.
- **Data steward / model risk owner** (DS track) — accountable for a
  dataset's fitness and for the model-release evidence respectively
  (see [glossary](../../../docs/resources/glossary.md)).
- **RACI** — Responsible (does it), Accountable (owns the outcome — exactly
  one A per activity), Consulted (two-way input), Informed (one-way update).
- **PMI Talent Triangle** — ways of working; power skills; business acumen.

## Practical examples

**CS:** CampusHub — sponsor: registrar (owns the service outcome); PO:
student-services lead; tech lead: senior developer; PM: integrator. RACI the
"exam-timetable publishing" activity: registrar A, services team R, PM
consulted, students informed.

**DS:** churn model — sponsor: VP marketing (owns retention benefit); PO:
retention manager; data lead: senior DS; **data steward**: CRM data owner
(consulted on any new customer attribute); model risk owner: analytics QA
(approves the release gate). RACI "approve model go-live": risk owner A,
data lead R, PO consulted, legal informed.

## Worked example

**RACI construction, live, on a 6-activity slice:**

| Activity | Sponsor | PM | PO | Devs | Data steward |
|---|---|---|---|---|---|
| Approve charter | **A** | R | C | I | I |
| Write backlog | I | C | **A/R** | C | I |
| Build ingestion pipeline | I | C | I | **A/R** | C |
| Approve data access rules | I | I | C | C | **A** |
| Run UAT | I | R | **A** | C | I |
| Publish go/no-go | **A** | R | C | I | I |

Teach three checks: exactly one A per row; every role has R somewhere (or
explain why not); consulted-vs-informed is a *time* decision — C costs
meetings, I costs only reading. Then the classic pathology: two A's on "build
ingestion" (tech lead *and* PM) — walk what actually happens (slowed
decisions, shadow PM, blame diffusion).

## Common misconceptions

| Misconception | Correction |
|---|---|
| "The PM is the boss of everyone." | The PM integrates; authority comes from the sponsor and the plan, not rank over engineers. |
| "RACI is HR paperwork." | It is a decision-rights contract; its absence shows up as duplicate work and dropped balls. |
| "Scrum master = junior PM." | Different accountability: process health vs delivery integration. |
| "PMP = competent PM." | Certification signals vocabulary and process knowledge; the triangle's other two sides carry the judgment. |

## Classroom activities

1. **Quiz 1 (15 min):** L01–L04 items; collect, peer-mark in session if time allows.
2. **CS-05 RACI workshop (35 min):** 12 activities × 6 roles; teams flag two
   ambiguities and write the escalation they would raise.
3. **Talent-triangle self-assessment (10 min):** students place themselves and
   name the side they will strengthen this semester.
4. **Title sort (5 min):** given twelve real job-ad titles, guess the underlying
   accountability — lively and revealing.

## Discussion questions

1. In CS-05, who should be A for "decide tech stack" — tech lead or PM? Defend with consequences, not titles.
2. What goes wrong when the sponsor is also the PO? When is that actually fine?
3. Which side of your talent triangle does this course stretch least — and what will you do about it?

## Practical exercise

**In class (part of CS-05):** complete the RACI for your Unit-1 case team's
own project (each member takes 2 activities). **Take home:** add a
*decision-rights* column ("who decides" vs "who informs") to your two rows —
RACI and decision rights are related but not identical (see glossary).

## Formative assessment (exit ticket)

1. What is the maximum number of A's per activity, and why?
2. Your sponsor asks for weekly written status. Which triangle side is that testing?
3. One role from today you had never heard of — and what it owns.

## Reading & references

- PMI. (2021). *PMBOK Guide* (7th ed.) — Team and Stakeholders domains.
- PMI. *Talent Triangle* materials — pmi.org (free overview).
- Scrum Guide 2020 — accountabilities section (free, scrum.org).

## Two-hour teaching plan

| Slot | Segment | Materials |
|---|---|---|
| 0:00–0:15 | **Quiz 1** (L01–L04) | quiz papers |
| 0:15–0:35 | Roles anatomy; the un-owned decision story | role cards |
| 0:35–0:50 | RACI construction + one-A rule | board table |
| 0:50–1:00 | Break | |
| 1:00–1:35 | CS-05 RACI workshop | CS-05 briefs |
| 1:35–1:50 | Talent triangle self-assessment | triangle sheets |
| 1:50–1:57 | Certification landscape Q&A (honest framing) | — |
| 1:57–2:00 | Exit ticket | slips |

## Instructor preparation notes

- Print quiz papers; arrange peer-marking logistics in advance.
- Pre-check CS-05's twelve activities for ambiguity traps you want surfaced.
- Have the job-ad titles ready (paste a dozen from a real job board the week
  before — authentic and citable as "retrieved from …" in class only).

## Linked resources

- Lecture skeleton: [`docs/lectures/L04`](../../../docs/lectures/L04-04-roles-profession.md)
- Case: [CS-05](../../../docs/cases/CS-05.md)
- Quiz 1 shell: [exam bank](../../exam-bank/README.md) — populate before delivery
- Roles & governance terms: [glossary](../../../docs/resources/glossary.md)
- Forward: capstone team formation (L08) uses today's role clarity.
