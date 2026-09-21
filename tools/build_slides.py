#!/usr/bin/env python3
"""PM-401 slide build pipeline (standard library only).

Reads Marp-flavored Markdown decks from instructor/slides/L{n}-slides.md,
writes self-contained HTML to instructor/slides/build/L{n}.html.

- Mermaid blocks are passed through to the Mermaid CDN renderer (see index page);
  offline, the raw diagram text remains visible as a styled panel.
- Speaker notes are embedded as <details class="speaker-notes"> (collapsed,
  printer-visible via CSS) so the same file works for live projection,
  independent review, and printing.
- The shared theme (assets/pm401.css) is inlined into every page; the file
  itself stays authoritative for Marp CLI users.

Usage: python tools/build_slides.py [--out DIR]
"""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLIDES_DIR = ROOT / "instructor" / "slides"
THEME = SLIDES_DIR / "assets" / "pm401.css"

MERMAID_SRC = "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs"


def esc(s: str) -> str:
    return html.escape(s, quote=False)


# --------------------------------------------------------------------------
# Markdown-lite rendering
# --------------------------------------------------------------------------

def _inline(md: str) -> str:
    s = esc(md)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(
        r"\[([^\]]+)\]\(([^)\s]+)\)",
        lambda m: '<a href="%s">%s</a>' % (html.escape(m.group(2), quote=True), m.group(1)),
        s,
    )
    return s


def _table_html(rows: list[list[str]]) -> str:
    out = ["<table>"]
    for i, row in enumerate(rows):
        tag = "th" if i == 0 else "td"
        cells = "".join(f"<{tag}>{_inline(c)}</{tag}>" for c in row)
        out.append(f"<tr>{cells}</tr>")
    out.append("</table>")
    return "".join(out)


def render_blocks(lines: list[str]) -> tuple[str, int]:
    """Render slide body lines to HTML; return (html, mermaid_diagram_count)."""
    out: list[str] = []
    para: list[str] = []
    diagrams = 0
    i, n = 0, len(lines)

    def flush_para() -> None:
        if para:
            out.append(f"<p>{_inline(' '.join(para))}</p>")
            para.clear()

    while i < n:
        line = lines[i]
        stripped = line.strip()

        # fenced code / mermaid
        if stripped.startswith("```"):
            flush_para()
            lang = stripped[3:].strip().lower()
            body: list[str] = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                body.append(lines[i])
                i += 1
            i += 1  # closing fence
            code = "\n".join(body)
            if lang == "mermaid":
                diagrams += 1
                out.append(f'<div class="mermaid">\n{esc(code)}\n</div>')
            else:
                out.append(f"<pre><code>{esc(code)}</code></pre>")
            continue

        # table: header row + separator row
        if (
            stripped.startswith("|")
            and i + 1 < n
            and re.match(r"^\|[\s:|-]+\|$", lines[i + 1].strip())
        ):
            flush_para()
            rows: list[list[str]] = []
            header = [c.strip() for c in stripped.strip("|").split("|")]
            rows.append(header)
            i += 2
            while i < n and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            out.append(_table_html(rows))
            continue

        # headings
        m = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if m:
            flush_para()
            level = len(m.group(1))
            out.append(f"<h{level}>{_inline(m.group(2))}</h{level}>")
            i += 1
            continue

        # blockquote
        if stripped.startswith(">"):
            flush_para()
            quote: list[str] = []
            while i < n and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip().lstrip(">").strip())
                i += 1
            out.append(f"<blockquote>{_inline(' '.join(quote))}</blockquote>")
            continue

        # lists (two levels by indentation)
        m = re.match(r"^(\s*)(?:[-*]|\d+[.)])\s+(.*)$", line)
        if m:
            flush_para()
            items: list[tuple[int, str]] = []
            while i < n:
                mm = re.match(r"^(\s*)(?:[-*]|\d+[.)])\s+(.*)$", lines[i])
                if not mm:
                    break
                items.append((len(mm.group(1)), mm.group(2)))
                i += 1
            out.append(_list_html(items))
            continue

        if not stripped:
            flush_para()
            i += 1
            continue

        para.append(stripped)
        i += 1

    flush_para()
    return "\n".join(out), diagrams


def _list_html(items: list[tuple[int, str]]) -> str:
    out: list[str] = []
    depth = 0
    for indent, text in items:
        level = 1 if indent >= 2 else 0
        if level > depth:
            out.append("<ul>")
            depth = level
        elif level < depth:
            out.append("</ul>")
            depth = level
        elif out and out[-1] not in ("<ul>",):
            pass
        out.append(f"<li>{_inline(text)}</li>")
    while depth >= 0:
        out.append("</ul>")
        depth -= 1
    return "".join(out)


# --------------------------------------------------------------------------
# Deck parsing
# --------------------------------------------------------------------------

def parse_deck(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    meta: dict[str, str] = {}
    body = raw
    if raw.startswith("---"):
        end = raw.find("\n---", 3)
        if end != -1:
            for ln in raw[3:end].splitlines():
                if ":" in ln:
                    k, v = ln.split(":", 1)
                    meta[k.strip()] = v.strip()
            body = raw[end + 4:]

    # split slides on standalone --- lines
    chunks, cur = [], []
    for line in body.splitlines():
        if line.strip() == "---":
            chunks.append(cur)
            cur = []
        else:
            cur.append(line)
    chunks.append(cur)

    slides = []
    for chunk in chunks:
        cls, notes, content = None, [], []
        i = 0
        while i < len(chunk):
            line = chunk[i]
            s = line.strip()
            if s.startswith("<!--"):
                comment = [s]
                while "-->" not in comment[-1]:
                    i += 1
                    comment.append(chunk[i].strip())
                joined = " ".join(comment)
                inner = joined[4:joined.index("-->")].strip()
                if inner.startswith("_class:"):
                    cls = inner.split(":", 1)[1].strip()
                elif inner.startswith("notes:"):
                    notes.append(inner.split(":", 1)[1].strip())
                i += 1
                continue
            content.append(line)
            i += 1

        html_body, diagrams = render_blocks(content)
        title_m = re.search(r"<h1>(.*?)</h1>", html_body)
        slides.append(
            {
                "class": cls,
                "notes": "\n".join(x for x in notes if x),
                "html": html_body,
                "title": re.sub(r"<[^>]+>", "", title_m.group(1)) if title_m else "",
                "diagrams": diagrams,
            }
        )

    num_m = re.match(r"L(\d+)-slides\.md", path.name)
    return {
        "num": int(num_m.group(1)) if num_m else 0,
        "path": path,
        "meta": meta,
        "slides": slides,
        "diagrams": sum(s["diagrams"] for s in slides),
        "title": meta.get("title") or next(
            (s["title"] for s in slides if s["title"]), path.stem
        ),
    }


def iter_decks() -> list[dict]:
    decks = []
    for p in sorted(SLIDES_DIR.glob("L*-slides.md")):
        m = re.match(r"L(\d+)-slides\.md", p.name)
        if m:
            decks.append(parse_deck(p))
    decks.sort(key=lambda d: d["num"])
    return decks


# --------------------------------------------------------------------------
# HTML output
# --------------------------------------------------------------------------

LAYOUT_CSS = """
body { margin: 0; background: #2b3240; }
main { display: flex; flex-direction: column; align-items: center; gap: 28px; padding: 28px 0; }
section.slide { width: 960px; max-width: 96vw; min-height: 540px; box-shadow: 0 2px 12px rgba(0,0,0,.4); box-sizing: border-box; position: relative; }
section.slide.lead { display: flex; flex-direction: column; justify-content: center; }
code { background: var(--c-panel); padding: 0 5px; border-radius: 4px; font-family: Consolas, "Courier New", monospace; font-size: 0.88em; }
pre code { display: block; padding: 10px 14px; }
.mermaid { min-height: 2em; }
details.speaker-notes { margin-top: 18px; border-top: 2px dashed var(--c-line); padding-top: 8px; font-size: 0.72em; color: var(--c-note); }
details.speaker-notes summary { cursor: pointer; font-weight: 600; color: var(--c-accent); }
details.speaker-notes div { white-space: pre-line; }
.index-card { width: 960px; max-width: 96vw; background: #fff; color: var(--c-ink); padding: 40px 56px; box-sizing: border-box; box-shadow: 0 2px 12px rgba(0,0,0,.4); font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif; }
@media print {
  body { background: #fff; }
  main { gap: 0; padding: 0; }
  section.slide { box-shadow: none; width: 100%; max-width: none; min-height: auto; page-break-after: always; }
  details.speaker-notes { display: block !important; }
  .index-card { box-shadow: none; }
}
"""

MATTER = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>__TITLE__</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
__THEME__
{LAYOUT_CSS}
</style>
</head>
<body>
<main>
'''

MATTER_END = f"""</main>
<script type="module">
import mermaid from "{MERMAID_SRC}";
mermaid.initialize({{ startOnLoad: true, theme: "neutral", securityLevel: "loose",
  fontFamily: "Segoe UI, Helvetica Neue, Arial, sans-serif" }});
</script>
</body>
</html>
"""


def slide_html(slide: dict, idx: int, total: int) -> str:
    cls = f' class="slide {esc(slide["class"])}"' if slide["class"] else ' class="slide"'
    notes = ""
    if slide["notes"]:
        notes = (
            '<details class="speaker-notes"><summary>Speaker notes</summary>'
            f"<div>{esc(slide['notes'])}</div></details>"
        )
    return (
        f'<section{cls} id="s{idx:02d}" data-pagination="{idx} / {total}">\n'
        f'{slide["html"]}\n{notes}\n</section>'
    )


def deck_page(deck: dict, theme_css: str) -> str:
    head_title = f"PM-401 · {deck['title']} (slides)"
    parts = [MATTER.replace("__TITLE__", esc(head_title)).replace("__THEME__", theme_css)]
    total = len(deck["slides"])
    for i, s in enumerate(deck["slides"], 1):
        parts.append(slide_html(s, i, total))
    parts.append(MATTER_END)
    return "".join(parts)


def index_page(decks: list[dict], theme_css: str) -> str:
    rows = []
    for d in decks:
        n_notes = sum(1 for s in d["slides"] if s["notes"])
        rows.append(
            f"<tr><td><a href='L{d['num']:02d}.html'>L{d['num']:02d}</a></td>"
            f"<td>{esc(d['title'])}</td>"
            f"<td style='text-align:center'>{len(d['slides'])}</td>"
            f"<td style='text-align:center'>{d['diagrams']}</td>"
            f"<td style='text-align:center'>{n_notes}/{len(d['slides'])}</td></tr>"
        )
    body = f"""<div class="index-card">
<h1>PM-401 Lecture Slide Decks</h1>
<p>One HTML deck per lecture, built from <code>instructor/slides/L&lt;n&gt;-slides.md</code>
by <code>tools/build_slides.py</code> (standard library only).</p>
<ul>
<li><strong>Navigation:</strong> scroll; each slide is a &lt;section&gt; with a page number.</li>
<li><strong>Speaker notes:</strong> collapsed per slide — click to open; they print automatically (File → Print → PDF).</li>
<li><strong>Diagrams:</strong> rendered by the Mermaid CDN; offline, the diagram source text remains visible in a styled panel.</li>
<li><strong>Marp CLI:</strong> the same Markdown sources build to PPTX/PDF with <code>assets/pm401.css</code> as the theme.</li>
</ul>
<table>
<tr><th>Deck</th><th>Title</th><th>Slides</th><th>Diagrams</th><th>Notes</th></tr>
{"".join(rows)}
</table>
</div>"""
    page = MATTER.replace("__TITLE__", "PM-401 · Slide deck index").replace("__THEME__", theme_css)
    # index page needs no mermaid script
    return page + body + "</main>\n</body>\n</html>\n"


def main() -> int:
    out = SLIDES_DIR / "build"
    argv = sys.argv[1:]
    if "--out" in argv:
        out = Path(argv[argv.index("--out") + 1])
    out.mkdir(parents=True, exist_ok=True)
    theme_css = THEME.read_text(encoding="utf-8") if THEME.exists() else ""

    decks = iter_decks()
    if not decks:
        print("No decks found in", SLIDES_DIR)
        return 1
    for d in decks:
        page = deck_page(d, theme_css)
        target = out / f"L{d['num']:02d}.html"
        target.write_text(page, encoding="utf-8")
        n_notes = sum(1 for s in d["slides"] if s["notes"])
        print(
            f"L{d['num']:02d}  {len(d['slides']):2d} slides · "
            f"{d['diagrams']} diagrams · notes {n_notes}/{len(d['slides'])}"
            f"  -> {target.relative_to(ROOT)}"
        )
    (out / "index.html").write_text(index_page(decks, theme_css), encoding="utf-8")
    print(f"Built {len(decks)} decks + index -> {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
