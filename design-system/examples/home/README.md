# Home page: handover

> Chosen 28 Sep 2026 over sample B (`../home-b/`, kept for reference).

Built 28 Sep 2026 from the references in `../../references/` and the sample
artifact, with core blocks only. Regenerate with `python3 build.py`; the
generator is the source, `sections/*.html`, `block.html` and `footer.html` are
outputs.

## Order and rhythm

| # | Section | File | Background | Action |
|---|---|---|---|---|
| 0 | Hero | existing, untouched | | |
| 1 | Pattern strip: local train | `01-strip-train` | strip | |
| 2 | Key facts, two columns | `02-key-facts` | white, gateway motif | outline "About the event" |
| 3 | Separator: marigold | `03-sep-marigold` | | |
| 4 | Why attend: four numbered points + 4:5 photo | `04-why-attend` | sky wash, lattice tile | none (the points are the content) |
| 5 | Separator: local train | `05-sep-train` | | |
| 6 | Get involved: four cards, Sponsor open | `06-get-involved` | white | four outline buttons, one per card |
| 7 | Separator: vada pav | `07-sep-vadapav` | | |
| 8 | By the numbers + dark strip | `08-numbers` | sky wash, waves tile at the foot | Base button on the dark strip |
| 9 | Sponsors: Blockbuster – Platinum, three logos | `09-sponsors` | white, palm motif | primary "Become a sponsor" |
| 10 | Venue: facts, gallery, map, buttons | `10-venue` | sky wash | primary "Explore the venue" |
| 11 | Separator: cutting chai | `11-sep-chai` | | |
| 12 | Updates (Query Loop) + Stay in touch (Jetpack) | `12-updates` | white, lattice tile | "All updates" link, Subscribe |
| 13 | Be part: gradient band, logo disc, garland strip | `13-be-part` | gradient | Base "I am interested" + outline email |
| F | Footer scene | `footer.html` | illustration | slim menu, social links, credit |

## Paste order

1. **Assets first.** The page references PNGs by jsDelivr URL
   (`https://cdn.jsdelivr.net/gh/ajmaurya99/wc-mumbai-2027@main/design-system/assets/…`).
   They resolve once this repo is pushed to GitHub `main`; jsDelivr caches
   `@main` for up to 12 hours, so pin a commit hash in `build.py` (`CDN`) for
   production, as the hero does. Alternative: upload `assets/png/*.png` and
   `assets/img/footer-stage.jpg` to the media library and replace the URLs.
2. **CSS.** Appearance → Customize → Additional CSS, once per site, each
   under its fence: `buttons.css`, `links.css`, `card.css` (from the library)
   and `home.css` (separators, fact cards and chips, bands). The footer fence
   is already live in hero.css; `footer-live.css` is a preview copy, do not
   paste it. Reload and confirm the rules survived.
3. **Page.** Home page → Options → Code editor → paste the output of
   `python3 ../../tools/preview.py --site block.html` after the hero block.
   (`block.html` also works as-is; the `ds:` marker comments and the
   preview-only stand-ins are harmless but untidy.)
4. **Footer.** Appearance → Editor → Patterns → Footer template part → Code
   editor → replace with the output of `preview.py --site footer.html`. Then
   pick the menu in the Navigation block and set the four Social Links URLs.
5. **Replace placeholders.** Every `placehold.co` image, every `DD Mon 2026`,
   every `#` link, the four numbers, the sponsor logos, the venue address line.
6. Check at 320, 390, 768, 1366 and 1920; open the header menu on a phone.

## Things to know

* **Map.** The Custom HTML block on WordCamp.org strips `<iframe>`, so the
  venue section ships a static map image linked to Google Maps. To try an
  embed anyway, add a Custom HTML block under the map image with
  `<iframe src="https://www.google.com/maps/embed?pb=…" width="100%" height="400" style="border:0;border-radius:16px" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>`
  and reload the page: if it survives, delete the image; if it vanishes,
  keep the image, or use the Jetpack Map block.
* **Updates** is a Query Loop: latest three posts, featured image 16:9, date,
  category, title, excerpt. It fills itself; the preview shows stand-ins.
* **Stay in touch** is the Jetpack Subscriptions block (used by other
  WordCamp sites). Its colours are set in the block JSON.
* **Get involved**: only Sponsor is "Open"; the other three say "Coming soon"
  and still link to `#` until the calls open. Change a chip by editing its
  text and text colour (Accent 2 open, Accent 4 coming soon).
* **Footer** reuses the live `wcm-footer-scene` approach: a full-width Group
  with the scene as a Cover-sized, bottom-anchored background image, and the
  bottom padding and phone crop from the FOOTER SCENE fence in hero.css. The
  phone crop image is on the live site only, so the 390px preview shows the
  menu on a plain background.
* **New values** introduced for this page and recorded in DESIGN-SYSTEM.md:
  the gradient band, the dark band, the 4px accent edge, decorative
  background tiles and motifs, and the 4:5 photo ratio in Why attend.

## Files

`build.py` generator · `sections/` one file per section · `block.html` page ·
`footer.html` template part · `home.css` page CSS · `buttons.css`,
`links.css`, `card.css` library copies · `footer-live.css` preview copy ·
`preview.html`, `page-with-footer.preview.html` previews ·
`page-with-footer.preview-390.png`, `page-with-footer.preview-1366.png` renders.
