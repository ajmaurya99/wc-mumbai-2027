# Home page sample B: warm and colourful (not chosen)

> Decision 28 Sep 2026: sample A (`../home/`) is the home page. This sample
> is kept for reference only. Its proposed wash tokens and second gradient were
> withdrawn from tokens.json; the values below stay documented here.

Same thirteen sections and footer as sample A (`../home/`), rebuilt with more
colour. Compare `page-with-footer.preview-1366.png` here with the one in
`../home/`. Regenerate with `python3 build.py`; paste instructions are the
same as in `../home/README.md` (the CSS adds one fence, separator colours).

## What changed, section by section

| # | Section | Sample A | Sample B |
|---|---|---|---|
| 1 | Strip under the hero | local train | marigold garland (toran) |
| 2 | Key facts | white, gateway motif, teal edges | **marigold wash**, marigold dots tile, edges in blue, teal and purple, saffron Kalam line, primary button |
| 3 | Separator | teal dashed | **saffron** dashed |
| 4 | Why attend | sky wash, lattice | **teal wash**, white lattice, numerals in blue, teal, purple and slate, saffron Kalam line |
| 5 | Separator | teal | **purple** |
| 6 | Get involved | white | white with **purple kolam tile**; "Open" chip on marigold wash |
| 7 | Separator | teal | **gold** |
| 8 | Numbers | sky wash, navy strip | **purple wash**, numerals in blue, teal, saffron and purple; **purple strip** |
| 9 | Sponsors | white, palm motif, sky-wash cards | white with a **marigold flower motif**, marigold-wash logo cards |
| 10 | Venue | sky wash | **full teal band**, white waves tile, gold Kalam line, white cards, white buttons |
| 11 | Separator | teal | saffron |
| 12 | Updates | white, lattice | **marigold wash**, white lattice, white cards, purple Subscribe |
| 13 | Be part | blue → purple gradient | **teal → purple** gradient, gold eyebrow |
| 14 | Strip before footer | none | **kolam** strip |

## New values this sample proposes

Recorded in `tokens.json` as `status: proposed`; adopt or drop when you pick:

| Token | Value | Derived from |
|---|---|---|
| color.wash.marigold | `#FFF6E3` | marigold at ~12% on white |
| color.wash.teal | `#E8F3F4` | Accent 2 at ~10% on white |
| color.wash.purple | `#F1ECFB` | Accent 3 at ~8% on white |
| gradient.bandB | teal → purple | Accent 2 to Accent 3 |

Washes are not theme presets, so they are custom background colours in the
block JSON. If sample B wins, add them to Styles → Colors → Custom so they
appear in the picker, and DESIGN-SYSTEM.md §2 gets a "washes" row.

Festive colours as text: the brief limits marigold, saffron and gold to badges
and dividers. This sample uses saffron for Kalam taglines and one xx-large
numeral, and gold for a Kalam line and an eyebrow on teal and on the
gradient. All are large or bold text, so they clear AA for large text; the
report flags them REVIEW on purpose so the decision is visible.

## Report

block.html: 58 PASS, 2 REVIEW (the festive text uses above), 0 FAIL.
home.css: 2 PASS, 2 REVIEW (separator line colours), 0 FAIL.
