#!/usr/bin/env python3
"""Post-build link & path validator for the PM-401 site.

Checks every generated HTML page in site/ for:
  1. Relative links (href/src) that resolve to a real file
  2. Root-absolute links ("/...") — allowed ONLY in 404.html, where
     MkDocs Material deliberately emits site_url-prefixed paths (which are
     correct under the GitHub Pages project subpath). Anywhere else they
     fail the check.
  3. Local filesystem paths leaking into output ("file://", drive letters
     not preceded by a letter, so https:// is not a false positive)

Usage: python tools/check_links.py [--site site]
Exit 0 = clean, 1 = problems found.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r'(?:href|src)="([^"]+)"')
SKIP_PREFIXES = ("http://", "https://", "#", "mailto:", "data:", "tel:", "javascript:")
# drive letter not preceded by a letter (https:// must not match)
DRIVE_RE = re.compile(r"(?<![a-z0-9])[a-z]:[\\/]", re.I)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", default=str(ROOT / "site"))
    args = parser.parse_args()
    site = Path(args.site)
    if not site.exists():
        print(f"site/ not found at {site} — run mkdocs build first")
        return 1

    pages = list(site.rglob("*.html"))
    checked = 0
    abs_links: list[tuple[str, str]] = []
    broken: list[tuple[str, str]] = []
    fs_leaks: list[str] = []

    for p in pages:
        rel = p.relative_to(site)
        text = p.read_text(encoding="utf-8", errors="replace")
        if "file://" in text.lower() or DRIVE_RE.search(text):
            fs_leaks.append(str(rel))
        for m in LINK_RE.finditer(text):
            u = m.group(1)
            checked += 1
            if u.startswith(SKIP_PREFIXES) or u.startswith("//"):
                continue
            if u.startswith("/"):
                # 404.html is special-cased by mkdocs-material: it emits
                # site_url-prefixed absolute links, correct for the subpath.
                if rel.name == "404.html" and u.startswith("/Project-Management/"):
                    continue
                abs_links.append((str(rel), u))
                continue
            path = u.split("#", 1)[0].split("?", 1)[0]
            if not path:
                continue
            target = (site / rel.parent / path)
            if not target.exists():
                # extensionless markdown-style links resolve to .html in the
                # built site (e.g. ../lectures/L01-01-x -> ../lectures/L01-01-x.html)
                if Path(str(target) + ".html").exists():
                    continue
                broken.append((str(rel), u))

    print(f"checked {checked} href/src attributes across {len(pages)} HTML pages")
    print(f"root-absolute links: {len(abs_links)}")
    for r, u in abs_links[:10]:
        print("  ABS", r, "->", u)
    print(f"broken relative links: {len(broken)}")
    for r, u in broken[:20]:
        print("  BROKEN", r, "->", u)
    print(f"filesystem-path leaks: {len(fs_leaks)}")
    for r in fs_leaks[:10]:
        print("  LEAK", r)

    if abs_links or broken or fs_leaks:
        print("LINK CHECK: FAIL")
        return 1
    print("LINK CHECK: PASS — all internal links resolve, no absolute paths, no fs leaks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
