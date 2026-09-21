# Lab 3 Answer Key — Scope & WBS

## Model requirements (8–12 testable, MoSCoW; accept equivalents)

| Req | Testable sentence | MoSCoW |
|---|---|---|
| R-01 | Result publication completes within 48 h of ceremony end, verified in staging rehearsal | Must |
| R-02 | Portal p95 response ≤ 2.0 s with 3,000 concurrent users (load test, 3 runs) | Must |
| R-03 | Registration handles 3,000 concurrent users with zero deadlocks (peak replay) | Must |
| R-04 | LMS roster sync retries transient failures and dead-letters permanent ones; no silent loss | Must |
| R-05 | Fee challan reconciliation report matches finance ledger within tolerance X (student-defined, stated) | Should |
| R-06 | Analytics repo serves result-freshness queries ≤ 5 min p95 | Should |
| R-07 | Schema migration rollback completes ≤ 30 min (drill evidence) | Must |
| R-08 | Portal forms meet accessibility level the team defines and states | Could |
| R-09 | Historical results for 5 years queryable with era-consistent labels | Should |

**Exclusions (≥ 3 with destinations):** mobile app → other project; fee
payment gateway work → parking lot; full legacy archive (pre-2021) → never
(declared); department analytics → phase 2 parking lot.

## Model WBS (structure; students may vary level-3 composition)

```
1.0 CAMPUS-MEND
├── 1.1 Legacy audit & requirements sign-off (40/20/0/8)
│   ├── 1.1.1 Legacy data audit (20 dev)  ├── 1.1.2 Requirements workshops (20 dev)
│   └── 1.1.3 QA review of requirements evidence (20 QA)
├── 1.2 Database & schema design (80/20/40/8)
├── 1.3 Portal web app build (320/80/0/24) → 3 work packages by module
├── 1.4 Analytics repository (120/20/200/12) → 1.4.1 schema, 1.4.2 load jobs, 1.4.3 validation suite
├── 1.5 Streaming feature pipeline (120/20/120/12)
├── 1.6 LMS adapter build (120/40/0/16)
├── 1.7 System & performance testing (40/240/0/8)
├── 1.8 Rollout & SLA validation (24/40/8/8)
└── 1.9 Project management (0/0/0/96)
```

**100% audit (pass requires):** every level-2 sums to its §B hours; total
dev 864, QA 480, DE 368, PM 96 → labor total 1,808 h. PM = 96 h explicitly.
No misc nodes. Two packages marked rolling-wave with justification
(1.4/1.5 depend on discovery findings).

## Common wrong answers

| Error | Correction |
|---|---|
| WBS written as activities ("do testing") | deliverable nouns with acceptance hooks |
| Children don't sum to parents | 100% rule violation — the most common; usually missing PM or QA hours |
| "Testing" spread across every branch | testing is G's deliverable; per-package QA hours stay inside each package |
| Requirements with "fast", "user-friendly" | attach measure or delete |
| Exclusions with no destination | every exclusion names where the wish goes |

## Reflection guidance

1. Hardest testable: accessibility (R-08) — students must define the level
   themselves (data pack doesn't set it) — teach: unnamed standards are
   unnamed scope.
2. 130% children: missing overlap (two packages claiming same work = scope
   fix) vs sandbagged estimates (estimating fix). Which fix depends on
   whether hours disagree with scope or with reality.
3. 100% rule → auditable because every package has hours + acceptance; a
   percent claim maps to a finite, checkable basket of work.

## Preparation notes

Students need Lab 1's charter in hand. The hours worksheet CSV is the
machine-checkable part — run the checker before class to catch arithmetic
drift in student submissions fast.
