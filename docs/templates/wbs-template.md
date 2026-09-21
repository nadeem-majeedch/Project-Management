<!--
Template: WBS (Lab 3; feeds A2, capstone)
Rules: 100% rule (children sum to parent — every package, no gaps, no
overlaps); deliverable-oriented (name nouns, not "do planning"); work-package
level = one owner, estimable, ≤ 80 hours or one reporting period; numbered
1, 1.1, 1.1.1 so the dictionary and hours CSVs can reference it.
-->

# Work Breakdown Structure — [Project name]

**Decomposition depth:** [levels used] · **Work-package size rule:** [≤ 80 h / 1 sprint / other]

## WBS tree (indented or fenced diagram)

```
1.0 [Project name]
├── 1.1 [Major deliverable]
│   ├── 1.1.1 [Work package]   (owner: __  est: __ h)
│   └── 1.1.2 [Work package]   (owner: __  est: __ h)
├── 1.2 [Major deliverable]
│   ├── 1.2.1 [Work package]
│   └── 1.2.2 [Work package]
└── 1.3 [Project management]   ← keep PM as a real, sized work package
    └── 1.3.1 [Coordination, reporting, change control]  (owner: __  est: __ h)
```

*(example — delete)* For CAMPUS-MEND, packages A–H in `data-pack.md` §A are
the level-2 spine: e.g. `1.4 Analytics repository` decomposes into
1.4.1 warehouse schema, 1.4.2 load jobs, 1.4.3 validation suite.

## 100%-rule audit (do this before submitting)
| Check | Result |
|---|---|
| Every parent = sum of children (hours and scope) | ☐ |
| Every leaf is a work package (owner + estimate + acceptance) | ☐ |
| No "miscellaneous"/"etc." nodes | ☐ |
| PM work explicitly sized | ☐ |
| Traceability: each deliverable D1..Dn appears in exactly one branch | ☐ |

## Horizon note
State which levels are fully decomposed now vs rolling-wave (planned to
decompose by [milestone/date]) — and why that is the right cut for this life
cycle.
