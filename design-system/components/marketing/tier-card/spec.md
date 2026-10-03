# Tier card

**Group:** marketing · **Blocks:** Columns (wide) → Column → Group `wcm-card wcm-tier` → Image, Group (eyebrow + H3), Group (price + meta), Paragraph, List `wcm-check`, Paragraph, Buttons · **CSS:** `tier-card.css` (plus `card.css`)

## Purpose

A sponsorship package: the tier icon, level and name, price, who it is for,
what it includes, and one action. Three in a row on the call-for-sponsors
page (short version) and on the sponsorship-tiers page (every benefit).

## Anatomy

```
Columns (align wide, blockGap 30, Stack on mobile)
└── Column ×3
    └── Group .wcm-card.wcm-tier (Accent 5 on white / Base on sky wash, radius 16px, padding 40, gap 20)
        ├── Image            tier icon, 96px, radius 16px
        ├── Group (gap 0)    eyebrow "Platinum" (small, 700, uppercase, Accent 2) + H3 name (large)
        ├── Group (gap 0)    Paragraph price xx-large 700 Accent 1 + Paragraph "about $850" small Accent 4
        ├── Paragraph        one line: who the tier is for
        ├── List .wcm-check  benefits (four headline ones, or all of them)
        ├── Paragraph        short: link "All <tier> benefits →" · full: "Best for: …" small Accent 4
        └── Buttons          one outline button, full width
```

The headline tier adds `wcm-tier--featured` and a 2px Accent 1 border
(Group → Border, colour preset accent-1).

## Variants

| Variant | How |
|---|---|
| Short (teaser) | four headline benefits + "All … benefits →" link to the full card's anchor |
| Full | every benefit + "Best for" line; the Group carries an HTML anchor (`id="blockbuster"`) |
| Featured | 2px Accent 1 border on the Group |

## States

Hover shadow and lift from `card.css`. Checklist ticks are Accent 2.
The card is a flex column with the list stretching, so buttons line up
across a row whatever the list length.

## Do

* One primary button per section: the cards carry outline buttons, the
  section's primary button sits below the row.
* Prices in rupees as the number; dollars as a meta line.

## Don't

* No festive colours on the price.
* No more than four bullets in the short version.

## Presets used

`accent-5` or `base`, `accent-1`, `accent-2`, `accent-4`, `xx-large`,
`large`, `small`, spacing `20`, `30`, `40`, radius `16px`.

## Choices and the one REVIEW row

The tick indent is `padding-left: 1.6em` (REVIEW: not a spacing preset).
It is text-relative on purpose so the tick and the first line stay aligned at
every font size; a pixel preset would drift on phones.

## Report
### report: design-system/components/marketing/tier-card/block.html

| Result | Category | Found | Token | Lines | Note |
|---|---|---|---|---|---|
| PASS | colour | `backgroundColor: accent-5` | color.accent-5 | 3, 57, 111, 166 |  |
| PASS | colour | `has-accent-1-border-color` | color.accent-1 | 4 |  |
| PASS | colour | `has-accent-5-background-color` | color.accent-5 | 4, 58, 112, 167 |  |
| PASS | colour | `textColor: accent-2` | color.accent-2 | 9, 63, 117, 172 |  |
| PASS | colour | `has-accent-2-color` | color.accent-2 | 10, 64, 118, 173 |  |
| PASS | colour | `textColor: accent-1` | color.accent-1 | 19, 49, 73, 103, 127 +3 |  |
| PASS | colour | `has-accent-1-color` | color.accent-1 | 20, 50, 74, 104, 128 +3 |  |
| PASS | colour | `textColor: accent-4` | color.accent-4 | 23, 77, 131, 186, 221 |  |
| PASS | colour | `has-accent-4-color` | color.accent-4 | 24, 78, 132, 187, 222 |  |
| PASS | font-size | `fontSize: small` | type.size.small | 9, 23, 63, 77, 117 +4 |  |
| PASS | font-size | `has-small-font-size` | type.size.small | 10, 24, 64, 78, 118 +4 |  |
| PASS | font-size | `fontSize: large` | type.size.large | 13, 67, 121, 176 |  |
| PASS | font-size | `has-large-font-size` | type.size.large | 14, 68, 122, 177 |  |
| PASS | font-size | `fontSize: xx-large` | type.size.xx-large | 19, 73, 127, 182 |  |
| PASS | font-size | `has-xx-large-font-size` | type.size.xx-large | 20, 74, 128, 183 |  |
| PASS | radius | `16px` | radius.card | 3, 4, 5, 57, 58 +7 |  |
| PASS | spacing | `var:preset\|spacing\|30` | spacing.30 | 1 |  |
| PASS | spacing | `var:preset\|spacing\|40` | spacing.40 | 3, 57, 111, 166 |  |
| PASS | spacing | `var:preset\|spacing\|20` | spacing.20 | 3, 57, 111, 166 |  |
| PASS | spacing | `padding-top: var(--wp--preset--spacing--40)` | spacing.40 | 4, 58, 112, 167 |  |
| PASS | spacing | `padding-right: var(--wp--preset--spacing--40)` | spacing.40 | 4, 58, 112, 167 |  |
| PASS | spacing | `padding-bottom: var(--wp--preset--spacing--40)` | spacing.40 | 4, 58, 112, 167 |  |
| PASS | spacing | `padding-left: var(--wp--preset--spacing--40)` | spacing.40 | 4, 58, 112, 167 |  |

**PASS** · 23 PASS · 0 REVIEW · 0 FAIL · 0 STRIP

### report: design-system/components/marketing/tier-card/tier-card.css

| Result | Category | Found | Token | Lines | Note |
|---|---|---|---|---|---|
| REVIEW | spacing | `padding-left: 1.6em` | spacing.40 | 10 | use preset 40 (30px) |
| PASS | colour | `#006b78` | color.accent-2 | 17 |  |

**REVIEW** · 1 PASS · 1 REVIEW · 0 FAIL · 0 STRIP

