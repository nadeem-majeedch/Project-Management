---
title: "Lab 1 — Project Charter (CAMPUS-MEND Kickoff)"
lab: 1
week: 3
lecture: 6
time: "2 hours in-lab + 1 hour refinement"
deliverable: "One-page project charter (Markdown), draft v0.9"
submitted: "LMS, within one week"
---

# Lab 1 — Project Charter

## 1. Objectives
By the end of this lab you can:
1. Translate a messy sponsor request ([data pack](data-pack.md)) into a one-page charter with SMART objectives.
2. Separate scope (in/out lists) from success criteria (verifiable acceptance evidence).
3. Draft an authority table that names what the PM may decide alone vs must escalate.

## 2. Background & scenario
You are the newly appointed PM of CAMPUS-MEND at Northlake University. The
registrar's charter request arrived as a corridor conversation: *"Fix the
portal before January results, keep the vendor happy, and don't embarrass us
again."* Your job is to convert that into a charter precise enough to be
signed. Everything you are allowed to assume is in the [data pack](data-pack.md);
anything not there must appear in your charter as a stated assumption or an
explicit open question.

## 3. Required tools
- [Charter template](../templates/charter-template.md)
- [Data pack](data-pack.md) (story + constraints sections)
- No other tools; this is a judgment lab, not a calculation lab.

## 4. Step-by-step instructions
1. **Read the data pack story twice** (10 min). List every hard constraint you find — you should locate at least four (deadline, staffing, SOW cap, external dependencies).
2. **Draft objectives (20 min).** 2–3 SMART objectives. Each needs a measure, a target, and a deadline. "Improve the portal" is not an objective; "p95 response ≤ 2.0 s at 3,000 concurrent users by rollout" is.
3. **Scope in/out (20 min).** In-scope = what the data pack names. Out-scope = at least three things a stakeholder will *assume* are included (hint: think about what the legacy system does that nobody mentioned).
4. **Success criteria (20 min).** Convert the [data pack §G quality targets](data-pack.md#g-quality-and-measurement-targets-labs-8-13) into acceptance rows: criterion, verification method, verifier.
5. **Risks & milestones (15 min).** Two high-level risks (cause → event → effect) and 3–4 milestone rows with weeks.
6. **Authority table (15 min).** Fill the charter's roles section: sponsor, PM, teams — one line each on what they may decide alone.
7. **Refine (out of lab, 1 h).** Cut to one page. Every sentence either traces to the data pack or is labeled as your assumption.

## 5. Your tasks (checklist)
- [ ] ≥ 4 constraints identified from the story
- [ ] 2–3 SMART objectives with measures and dates
- [ ] In/out scope with ≥ 3 explicit exclusions
- [ ] ≥ 3 success criteria, each with verification method + verifier
- [ ] 2 cause→event→effect risks; 3–4 dated milestones
- [ ] Authority limits stated for PM (decide-alone vs escalate)
- [ ] ≤ 1 page + assumptions footer

## 6. Expected outputs
`charter.md` (from the template, all bracketed fields filled), ≤ 1 page,
plus an assumptions list. Submit via LMS within one week.

## 7. Reflection questions (answer in 3–5 lines, submit with the charter)
1. Which single charter line would have prevented the 2018 portal's failure mode?
2. What did you *want* to promise that the data pack does not let you? Where did you park it?
3. Who must sign this charter for it to actually bind anyone — and what does their signature mean?

## 8. Assessment rubric (graded pass / refine)
| Dimension | Pass looks like | Refine looks like |
|---|---|---|
| Objectives | measurable, dated, traceable | adjectives without numbers |
| Scope | explicit in AND out lists | out-scope missing or vague |
| Success criteria | each has verification method + verifier | restatement of objectives |
| Authority | decide-alone vs escalate is concrete | titles without limits |
| Traceability | every claim cites pack or is flagged | unsourced precision |

## 9. Related material
[Lecture 6 — Charter](../lectures/L06-06-charter.md) ·
[Case CS-04](../cases/CS-04.md) ·
[Capstone charter requirements](../capstone/capstone-charter.md) (this lab is a dry run)
