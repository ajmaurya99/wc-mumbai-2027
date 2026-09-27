# Worked example: "Why attend" feature section

The end-to-end test of the skill workflow. The reference was an imagined
screenshot: a three-column feature section headed "Why attend", each column
with an illustration, a short title and two lines, and one button below.
Each stage below is what the session says or does at that step.

## a. Map the reference

Maps to existing components, no new component needed:

| In the reference | Component | Folder |
|---|---|---|
| Sky-wash band with generous padding | section shell from the landing template | `templates/landing-page.md` |
| Small teal label, big title, handwritten line | Section header (centred, with Kalam tagline) | `components/core/section-header` |
| Three columns: picture, title, two lines | Card ×3, white on sky wash, **no per-card link** | `components/content/card` |
| One blue button under the columns | Buttons, primary only | `components/core/buttons` |

Values not in the system: the reference's icons looked about 56px. The brief
defines icons at 24px and illustrations in the card's 16:10 slot, nothing in
between. **Question for the user:** 24px icons, or the 16:10 illustration
slot? This run assumed the illustration slot (fully in-system); in a live
session the build waits for the answer.

## b. Proposal (waits for go-ahead)

> Section Group: full width, Accent 5, padding 70, constrained, blockGap 40.
> Inside: Section header centred with eyebrow "Why attend", H2, Kalam line.
> Then Columns, wide, gap 30, three Cards on Base (radius 16, padding 40),
> each with a 16:10 illustration, H3 large, one paragraph, no link because
> the section's action is the button. Then Buttons centred, one primary
> "Get tickets". CSS needed: `card.css` (hover) and `buttons.css` (hover,
> focus), both already in Additional CSS if the library is installed.
> Sits as section 2 of the landing page (white intro above, white callout
> below). Go ahead?

## c. Build and gate

```sh
python3 design-system/tools/preview.py design-system/examples/why-attend
python3 design-system/report.py design-system/examples/why-attend/block.html card.css buttons.css
```

Result (full table in `report.md`): block.html PASS with 25 PASS rows;
card.css REVIEW on `transition: transform` (the allowed 4px lift, justified
in the Card spec); buttons.css PASS. Nothing to fix.

## d. Render

```sh
design-system/tools/render.sh design-system/examples/why-attend/preview.html
```

`preview-1366.png`: three cards in a wide row, header centred, one button.
`preview-390.png`: cards stack to one column, title wraps to two lines, no
horizontal scroll, button stays 44px tall.

## e. Handover

Paste `block.html` into the page's code editor view at the position of the
section. Replace the three placeholder image URLs with media library
illustrations (1600×1000 PNG or WebP), and the ticket link if it differs.
CSS: `card.css` and `buttons.css` under their fences in Appearance →
Customize → Additional CSS, once per site, not per section. Reload and
confirm the hover shadow appears on a card.

Files in this folder: `block.html` (paste-ready), `card.css` and
`buttons.css` (copies of the library CSS, for the preview), `preview.html`,
`report.md`, `preview-390.png`, `preview-1366.png`.
