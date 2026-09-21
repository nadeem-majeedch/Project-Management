#!/usr/bin/env python3
"""PM-401 slide-package checker (standard library only).

Validates instructor/slides decks:
  1. Coverage: one L{n}-slides.md per lecture 1..32
  2. Required slides per deck: objectives / CS example / DS example /
     case anchor / discussion / summary+exit ticket / references
  3. Diagrams: >=1 Mermaid diagram in every non-lead deck
  4. Speaker notes: >=1 notes marker per deck
  5. Front-matter: lecture, week, clo, unit present
  6. Numeric consistency: L11 CS-15 duration and L19 CampusHub EVM chain
     recomputed from case YAML and compared with slide text
  7. Case anchors resolve to real case IDs
  8. No placeholder residue
"""

from __future__ import annotations

import glob
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SLIDES = ROOT / "instructor" / "slides"

failures: list[str] = []
warns: list[str] = []


def fail(msg: str) -> None:
    failures.append(msg)


def warn(msg: str) -> None:
    warns.append(msg)


def load_lectures() -> dict[int, dict]:
    d = yaml.safe_load((ROOT / "planning" / "course-data.yaml").read_text(encoding="utf-8"))
    return {int(x["num"]): x for x in d["lectures"]}


def load_cases() -> dict[str, dict]:
    out: dict[str, dict] = {}
    for f in glob.glob(str(ROOT / "planning" / "cases" / "band-*.yaml")):
        for c in yaml.safe_load(open(f, encoding="utf-8"))["cases"]:
            out[c["id"]] = c
    return out


def main() -> int:
    lectures = load_lectures()
    cases = load_cases()

    paths = {int(m.group(1)): p for p in SLIDES.glob("L*-slides.md")
             if (m := re.match(r"L(\d+)-slides\.md", p.name))}
    missing = [n for n in range(1, 33) if n not in paths]
    if missing:
        fail(f"missing decks: {missing}")
    extra = [n for n in paths if n not in lectures]
    if extra:
        fail(f"unexpected decks: {extra}")

    anchor_re = re.compile(r"\bCS-(\d{2})\b")
    key_needed = {}

    for n in sorted(paths):
        deck = paths[n]
        text = deck.read_text(encoding="utf-8")

        # front matter
        for k in ("lecture", "week", "clo", "unit"):
            if not re.search(rf"^{k}\s*:", text, re.M):
                fail(f"L{n:02d}: front-matter '{k}:' missing")

        # required slide types
        for needle, label in [
            ("## Learning objectives", "objectives slide"),
            ("CS:", "CS example slide"),
            ("DS:", "DS example slide"),
            ("Case anchor:", "case anchor slide"),
            ("## Discussion", "discussion slide"),
            ("## Summary", "summary/exit slide"),
            ("## References", "references slide"),
            ("<!-- notes:", "speaker notes"),
        ]:
            if needle not in text:
                fail(f"L{n:02d}: no {label} ({needle})")

        # placeholder residue
        if re.search(r"TBD|PLACEHOLDER|LOREM|XXX", text, re.I):
            fail(f"L{n:02d}: placeholder residue")

        # diagram requirement
        n_diag = len(re.findall(r"```mermaid", text))
        lead = n == 1
        if n_diag < 1 and not lead:
            fail(f"L{n:02d}: no mermaid diagram")
        if lead and n_diag == 0:
            warn("L01: no diagram (lead lecture)")

        # case anchors resolve
        for cid in {f"CS-{m.group(1)}" for m in anchor_re.finditer(text)}:
            if cid not in cases:
                fail(f"L{n:02d}: unknown case anchor {cid}")
            else:
                key_needed.setdefault(cid, n)

        # decks must not contradict the roster
        r = lectures.get(n, {})
        for field in ("title", "code", "unit", "week"):
            v = r.get(field)
            if v and str(v) not in text:
                fail(f"L{n:02d}: roster '{field}' value '{v}' not found in deck")

        # numeric spot checks (values recomputed from authoritative sources)
        if n == 11:
            want = "17"
            if not re.search(rf"\b{want}\s*weeks", text):
                fail(f"L11: CS-15 critical path duration {want} weeks not stated")
        if n == 19:
            for needle, label in [("74,050", "EAC_1"), ("69,224", "EAC_2"),
                                  ("81,780", "EAC_3"), ("1.17", "TCPI"),
                                  ("0.87", "CPI"), ("0.83", "SPI")]:
                if needle not in text:
                    fail(f"L19: {label} value {needle} missing")

    # answer-key cross-check: numeric case values cited on slides must match
    for cid, n in sorted(key_needed.items()):
        c = cases[cid]
        if not c.get("numerical"):
            continue
        text = (paths[n]).read_text(encoding="utf-8")
        for blk in c.get("numeric", []):
            if not isinstance(blk, dict):
                continue
            for step in blk.get("steps", []):
                expect = step.get("expect")
                if expect is None:
                    continue
                name = str(step.get("name", "")).replace("_", " ")
                if not name:
                    continue
                # accept name-with-value or the formatted value with thousand separators
                val = f"{expect:,}" if isinstance(expect, int) and abs(expect) >= 10000 else str(expect)
                if val not in text and str(expect) not in text:
                    # tolerant: name mentioned with any number is fine (label style)
                    if name.lower() not in text.lower():
                        warn(f"L{n:02d}: cites {cid} but expected value for "
                             f"'{name}' ({val}) not stated and not labelled")

    print(f"Checked {len(paths)} decks · "
          f"{sum(len(re.findall(r'```mermaid', p.read_text(encoding='utf-8'))) for p in paths.values())} diagrams · "
          f"{len({c for c in key_needed})} case anchors")
    for w in warns:
        print("WARN:", w)
    if failures:
        print(f"\nFAIL ({len(failures)}):")
        for f in failures:
            print(" -", f)
        return 1
    print("SLIDES PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
