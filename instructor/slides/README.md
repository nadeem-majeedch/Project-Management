# PM-401 Lecture Slide Decks

One deck per lecture (L01–L32), Marp-flavored Markdown, built to
self-contained HTML by `tools/build_slides.py` (standard library only).

## Layout

- `L{n}-slides.md` — the decks (student-visible content + `<!-- notes: -->` speaker notes)
- `assets/pm401.css` — shared theme (WCAG-AA checked palette; `@theme pm401` for Marp CLI)
- `build/` — generated HTML (`index.html` + `L{n}.html`); do not edit by hand

## Deck conventions (checked by `tools/check_slides.py`)

- Front matter: `lecture`, `week`, `unit`, `clo`
- Required slides: learning objectives · CS example · DS example · case anchor ·
  discussion · summary & exit ticket · references
- At least one Mermaid diagram per deck (L01 lead deck exempt)
- Speaker notes on at least one slide per deck (`<!-- notes: ... -->`)
- Numeric values must match the verified answer keys (spot-checked: L11 CS-15
  duration, L19 CampusHub EVM chain)

## Build

```bash
python tools/build_slides.py          # -> instructor/slides/build/
python tools/check_slides.py          # structure + consistency gates
```

The HTML output embeds the theme, renders Mermaid via CDN (diagram source text
stays visible offline), and prints speaker notes automatically
(File → Print → PDF).

## Marp CLI (optional PPTX/PDF)

```bash
npx @marp-team/marp-cli @latest instructor/slides/L19-slides.md \
  --theme instructor/slides/assets/pm401.css -o L19.pptx
```

The same sources build with Marp; `<!-- _class: lead -->` and
`<!-- notes: ... -->` are Marp-compatible conventions (notes via `<!-- notes: -->`
map to Marp presenter notes when using `--notes`-capable workflows; HTML build
treats them as embedded notes regardless).

## Status

All 32 decks authored and validated. Numbers on calculation slides are
checker-verified against `instructor/answer-keys/` and `tools/check_answers.py` /
`tools/check_cases.py`.
