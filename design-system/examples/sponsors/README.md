# Sponsor pages: handover

Built 3 Oct 2026 for the Call for Sponsors and Sponsorship Tiers pages from
the Rajasthan and Bengaluru 2026 call-for-sponsors pages, core blocks only.
Both pages come from one generator and one data file:

```sh
python3 design-system/examples/sponsors/build.py        # tiers.json → call-for-sponsors/, sponsorship-tiers/, components/marketing/tier-card/block.html
python3 design-system/tools/preview.py design-system/examples/sponsors/call-for-sponsors
python3 design-system/tools/preview.py design-system/examples/sponsors/sponsorship-tiers
python3 design-system/report.py design-system/examples/sponsors/<page>/block.html design-system/examples/sponsors/sponsors.css design-system/components/marketing/tier-card/tier-card.css
design-system/tools/render.sh design-system/examples/sponsors/<page>/preview.html
```

`tiers.json` holds the form link, the email, the two images already in the
media library, the three tiers (price, headline benefits, full benefits,
"best for"), the comparison rows and the FAQ. Change a price or a benefit
there, rebuild, re-paste both pages.

## Call for Sponsors (`call-for-sponsors/`)

| # | Section | Background | Action |
|---|---|---|---|
| 1 | Intro, two columns: eyebrow, H1, tagline, two paragraphs, buttons · poster image · four stat tiles | white (no colour set, so the header shadow shows), gateway motif | primary "Become a sponsor" (form), outline "See the tiers" |
| 2 | Separator: local train | | |
| 3 | Why sponsor: six cards | sky wash, lattice | |
| 4 | The tiers: three short tier cards | white, palm motif | primary "Become a sponsor", outline "Compare the tiers" |
| 5 | How it works: three numbered points beside the booth illustration | sky wash | |
| 6 | FAQ: eight Details blocks | white, blue lattice | |
| 7 | Ready to partner: gradient band | gradient (the one per page) | Base "Become a sponsor", outline email |

## Sponsorship Tiers (`sponsorship-tiers/`)

| # | Section | Background | Action |
|---|---|---|---|
| 1 | Intro: eyebrow, H1 "Pick your tier", tagline, paragraph, buttons | white, gateway motif | primary "Become a sponsor", outline "Compare the tiers" (#compare) |
| 2 | The tiers: three full tier cards, Blockbuster with the Accent 1 border; anchors `#blockbuster` `#megahit` `#superhit` | sky wash, lattice | outline button per card |
| 3 | Compare (`#compare`): the 20-row table from the old Compare the Tiers page, Table block, stripes style | white | |
| 4 | Good to know: four fact cards, 2 × 2 | sky wash | |
| 5 | Not sure which tier: section header + buttons | white | primary "Become a sponsor", outline email |

## New in the library

`components/marketing/tier-card` (spec, prompt, `tier-card.css`: checklist
ticks and the flex column). `tools/blocks.py` gained an `anchor` argument on
`group()` and `section()`.

## Paste order

1. **CSS** (once). Appearance → Customize → Additional CSS: add the
   `tier cards` fence (`components/marketing/tier-card/tier-card.css`) and
   the `sponsors` fence (`sponsors.css`, the comparison table). The faq fence
   (`components/content/faq-details/faq-details.css`) is needed too if it is
   not live yet. Reload and confirm.
2. **Pages.** Both are new draft pages on the "Page, no title (header and
   footer)" template, pasted 3 Oct 2026 for review. The existing
   `/call-for-sponsors/` is a blog **post** (post 5), so the new page's slug
   is provisional until the post is renamed; `/sponsorship-tiers/` (page 841)
   stays live until the new one replaces it; `/compare-the-tiers/` (page 843)
   stays as it is, just unlinked.
3. **Replace.** Nothing is placeholder: the form link, images, prices and FAQ
   are the site's own. Two table rows still say TBD (booth size, sponsor
   dinner), as they did before.
4. Check at 320, 390, 768, 1366 and 1920. The comparison table scrolls
   sideways inside its figure on phones.

## Reports

`call-for-sponsors/report.md`, `sponsorship-tiers/report.md`: PASS for both
pages and for `sponsors.css`; `tier-card.css` has the one REVIEW row
(`padding-left: 1.6em` on the tick, text-relative on purpose; see the
component spec).
