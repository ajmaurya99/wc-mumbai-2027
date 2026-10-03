# Venue page and News template: handover

Built 3 Oct 2026 from the Bengaluru and Rajasthan 2026 news pages and the
site's own venue announcement (post 748), core blocks only.

```sh
python3 design-system/examples/venue-news/build.py     # → venue/, news/ (block.html, sections/, news/template.html)
python3 design-system/tools/preview.py design-system/examples/venue-news/venue
python3 design-system/tools/preview.py design-system/examples/venue-news/news
python3 design-system/report.py design-system/examples/venue-news/<page>/block.html
design-system/tools/render.sh design-system/examples/venue-news/<page>/preview.html
```

## Venue (`venue/`, page 12 at `/venue/`, **draft**)

| # | Section | Background | Action |
|---|---|---|---|
| 1 | Intro, two columns: eyebrow, H1 "ATLAS SkillTech University", tagline, paragraph, buttons · the venue poster · three fact cards (date, address, getting there) | white, gateway motif | primary "Get directions" (Google Maps), outline "About our venue partner" → post 748 |
| 2 | Separator: taxi | | |
| 3 | The campus: copy from the post, Kalam pull quote · 2×2 gallery of the four campus photos already in the media library | sky wash, lattice | |
| 4 | Getting there: four fact cards (train, metro, air, parking; three say "Details closer to the date") · the auto-rickshaw illustration | white, palm motif | |
| 5 | Thank you, ATLAS: logo card · copy · outline "Read the announcement" | sky wash | |

Page 12 was the empty "Location" draft; it is now titled Venue with the slug
`venue`, on the "Page, no title (header and footer)" template. The nav's
"Venue" item still points at post 748 (`/venue-partner/`): switch it to page
12 when the page is published. The rickshaw illustration was uploaded to the
media library (attachment 1132, `files/2026/10/3.png`) and is kept in
`assets/img/auto-rickshaw.png`.

## News (`news/`, the **Blog Home** template)

`/news/` is the Posts page (Settings → Reading), so it has no content of its
own: the layout is the theme's **Blog Home** template. `news/template.html`
is the whole template: header part → main (constrained) → footer part, with:

| # | Section | Background |
|---|---|---|
| 1 | Intro: eyebrow "Latest news", H1 "News & updates", tagline, one line | white, gateway motif |
| 2 | Query Loop (inherits the main query, 10 per page): one post per row as a `wcm-card` — featured image 16:9 (40%) · category + date, title, excerpt with "Read more →" (60%) · numbered pagination · a no-results line | sky wash, lattice |
| 3 | Stay in touch: the home page's subscribe card (Jetpack Subscriptions) | white |

The panorama Cover banner the old template had is dropped (decided 3 Oct).
Templates have no draft state, and the Site Editor write was blocked for
Claude, so **paste it yourself**: Appearance → Editor → Templates → Blog Home
→ ⋮ → Code editor → replace everything with `news/template.html` → Save.
The previous version stays in the template's revisions.

`news/block.html` is the body only, with a static stand-in for the Query
Loop so the preview and the gate have something to render.

## Reports

`venue/report.md`, `news/report.md`: PASS. The template file passes too
(`report.py news/template.html`).
