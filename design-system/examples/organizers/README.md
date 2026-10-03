# Organizers page: handover

Built 3 Oct 2026 for https://mumbai.wordcamp.org/2027/organizers/ (page 13)
from the Bengaluru and Rajasthan 2026 organizer pages, with core blocks only.
The twelve organizers come from the site itself (`wcb_organizer` posts), so the
page is generated, not hand-typed:

```sh
python3 design-system/examples/organizers/fetch.py   # site → organizers.json (keeps hand-filled links)
python3 design-system/examples/organizers/build.py   # organizers.json → sections/, block.html
python3 design-system/tools/preview.py design-system/examples/organizers
python3 design-system/report.py design-system/examples/organizers/block.html design-system/examples/organizers/organizers.css
design-system/tools/render.sh design-system/examples/organizers/preview.html
```

`organizers.json` is the editable middle: fill `links.linkedin`, `links.x` and
`links.website` per person (they ship as `#`), re-run `build.py`, re-paste.
`fetch.py` keeps those links when it refreshes names, bios and photos.

## Sections and rhythm

| # | Section | File | Background | Action |
|---|---|---|---|---|
| 1 | Intro: eyebrow, H1, Kalam tagline, two paragraphs, buttons, three stat tiles | `01-intro` | white, gateway motif | primary "Get tickets", outline "Contact the team" |
| 2 | Separator: marigold | `02-sep-marigold` | | |
| 3 | Team: section header + 4 rows × 3 organizer cards | `03-team` | sky wash, lattice tile | "Read profile" link per card |
| 4 | Volunteer callout | `04-volunteer` | white | primary "Contact the team", outline email |

The intro carries the page's H1, so the page needs a template **without** the
post title but **with** the site header and footer. Neither existing template
fits: "Pages" adds a centred post-title band above the content, and "Page No
Title" (the coming-soon template) has no header or footer at all. So the site
now has a third template, **Page, no title (header and footer)**
(`page-no-title-header-footer`, added 3 Oct 2026): header template part →
Post Content → footer template part, the same three blocks as the Front Page
template. The page is assigned to it; reuse it for other inner pages whose
intro carries the H1.

## Organizer card

`wcm-card wcm-organizer`: Group, Base, radius 16px, padding 40, gap 20.
Image (160px, aspect 1, cover, radius 999px, centred, `medium_large` size)
→ H3 name (large, centred) → bio clipped to 26 words (`wcm-organizer__bio`)
→ Social Links (WordPress.org profile, LinkedIn, X, website; Accent 1 on
sky wash, hover fills Accent 1) → "Read profile →" link to the organizer's
own page. The card is a flex column with the bio stretching, so the icons and
link sit on one line across a row. Ajay has no photo yet: a sky-wash
"Photo soon" placeholder from placehold.co until one is uploaded.

Choices between tokens: Base cards on the sky-wash section (brief §5);
icon circles use Accent 5 so the four icons read quieter than the one
primary button per section; the photo radius is the pill token (999px) for a
true circle, which both references use.

## Paste order

1. **CSS** (once). Appearance → Customize → Additional CSS. `organizers.css`
   is live under its fence since 3 Oct 2026, as are the cards and separators
   fences. Not live yet, checked the same day: the `buttons`, `links` and
   `fact cards and chips` fences from the home page handover, which is why
   primary buttons still render in the theme's navy rather than Accent 1.
2. **Page.** Organizers page → Options → Code editor → paste the output of
   `python3 design-system/tools/preview.py --site design-system/examples/organizers/block.html`.
   Page settings → Template → "Page, no title (header and footer)".
   (Done 3 Oct 2026: saved as a draft, not published.)
3. **Replace.** "Get tickets" goes to `#` until the Tickets page is published;
   the three `#` social links per person (edit `organizers.json`, rebuild);
   Ajay's photo (upload it on his organizer post and re-run `fetch.py`).
4. Check at 320, 390, 768, 1366 and 1920; open the header menu on a phone.

## Report

See `report.md` (PASS, 34 and 6 rows). Renders: `preview-390.png`,
`preview-1366.png`.
