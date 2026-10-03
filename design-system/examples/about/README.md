# About page: handover

Built 4 Oct 2026 from the page's own copy, core blocks only. Live on page 678
(`/about-us/`, template "Page, no title (header and footer)") since 4 Oct; the
previous version is in the page's revisions.

```sh
python3 design-system/examples/about/build.py
python3 design-system/tools/preview.py design-system/examples/about
python3 design-system/report.py design-system/examples/about/block.html
design-system/tools/render.sh design-system/examples/about/preview.html
```

| # | Section | Background | Action |
|---|---|---|---|
| 1 | Intro, two columns: eyebrow, H1 "About Us", Kalam "Aamchi Mumbai. Aapla WordPress.", two paragraphs, buttons · the booth illustration (square) · four stat tiles (300+ attendees, 1 day, 12 organizers, 100% volunteer-run) | white, gateway motif | primary "Meet the organizers", outline "Contact us" |
| 2 | Separator: marigold | | |
| 3 | A city of many worlds: section header with the "fast, ambitious…" line as the tagline · four numbered cards, Learn / Share / Connect / Build (from the page's own "learn, share, connect and build") | sky wash, lattice | |
| 4 | There is a place for you here: the page's "whether you have been building…" copy · four Details: what is a WordCamp, who organises it, what it costs, how to get involved | white, palm motif | |
| 5 | Be part of WordCamp Mumbai 2027: gradient band | gradient | Base "Become a sponsor" (form), outline "Contact us" |

The numbered cards reuse the why-sponsor pattern (`wcm-why`, 4px Accent 2
edge, numeral as an inline Accent 1 highlight; the sponsors CSS fence clears
the `<mark>` background). The "12 organizers" tile is a literal count; change
it when the team grows.

Report: `report.md`, PASS.
