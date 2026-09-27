# Stat tile

**Group:** content · **Blocks:** Columns (wide) → Column → Group `wcm-card` → Paragraph (number), Paragraph (label), Paragraph · **CSS:** reuses `card.css`

## Purpose

"By the numbers": attendees, speakers, tracks, Contributor Day. Three or four
tiles in a row, each one number, one label, one line.

## Anatomy

```
Columns (align wide, blockGap 30, Stack on mobile)
└── Column ×3–4
    └── Group .wcm-card (Base on sky wash / Accent 5 on white, radius 16px, padding 40, gap 20)
        ├── Paragraph number  xx-large, 700, Accent 1
        ├── Paragraph label   small, 700, uppercase, letter-spacing .08em, Accent 4
        └── Paragraph         one line
```

Numbers are Accent 1 on every tile; the reference site varies the colour per
tile but the brief keeps festive colours for badges and dividers.

## Variants

| Variant | How |
|---|---|
| Three tiles | three Columns |
| Without text | delete the last Paragraph |
| Placeholder | "XX+" until the number is known |

## States

Hover shadow and lift from `card.css`, like every card.

## Do

* Round numbers with a plus ("500+"), never exact until final.
* Labels of one or two words.

## Don't

* No icons inside the tile.
* No Kalam for the number.

## Presets used

`base` or `accent-5`, `accent-1`, `accent-4`, `xx-large`, `small`, spacing `20`, `30`, `40`, radius `16px`.

## Report
### report: design-system/components/content/stat-tile/block.html

| Result | Category | Found | Token | Lines | Note |
|---|---|---|---|---|---|
| PASS | colour | `backgroundColor: base` | color.base | 3, 19, 35, 51 |  |
| PASS | colour | `textColor: accent-1` | color.accent-1 | 4, 20, 36, 52 |  |
| PASS | colour | `has-base-background-color` | color.base | 4, 20, 36, 52 |  |
| PASS | colour | `has-accent-1-color` | color.accent-1 | 5, 21, 37, 53 |  |
| PASS | colour | `textColor: accent-4` | color.accent-4 | 8, 24, 40, 56 |  |
| PASS | colour | `has-accent-4-color` | color.accent-4 | 9, 25, 41, 57 |  |
| PASS | font-size | `fontSize: xx-large` | type.size.xx-large | 4, 20, 36, 52 |  |
| PASS | font-size | `has-xx-large-font-size` | type.size.xx-large | 5, 21, 37, 53 |  |
| PASS | font-size | `fontSize: small` | type.size.small | 8, 24, 40, 56 |  |
| PASS | font-size | `has-small-font-size` | type.size.small | 9, 25, 41, 57 |  |
| PASS | radius | `16px` | radius.card | 3, 4, 19, 20, 35 +3 |  |
| PASS | spacing | `var:preset\|spacing\|30` | spacing.30 | 1 |  |
| PASS | spacing | `var:preset\|spacing\|40` | spacing.40 | 3, 19, 35, 51 |  |
| PASS | spacing | `var:preset\|spacing\|20` | spacing.20 | 3, 19, 35, 51 |  |
| PASS | spacing | `padding-top: var(--wp--preset--spacing--40)` | spacing.40 | 4, 20, 36, 52 |  |
| PASS | spacing | `padding-bottom: var(--wp--preset--spacing--40)` | spacing.40 | 4, 20, 36, 52 |  |
| PASS | spacing | `padding-left: var(--wp--preset--spacing--40)` | spacing.40 | 4, 20, 36, 52 |  |
| PASS | spacing | `padding-right: var(--wp--preset--spacing--40)` | spacing.40 | 4, 20, 36, 52 |  |

**PASS** · 18 PASS · 0 REVIEW · 0 FAIL · 0 STRIP

### report: design-system/components/content/stat-tile/card.css

| Result | Category | Found | Token | Lines | Note |
|---|---|---|---|---|---|
| REVIEW | motion | `transition: transform` | motion.lift | 8 | transform transitions: cards only (4px lift); never on the header |
| PASS | colour | `#6d28d9` | color.accent-3 | 15 |  |
| PASS | motion | `transition: 200ms` | motion.duration | 8 |  |
| PASS | motion | `prefers-reduced-motion guard` | motion | 18 |  |
| PASS | shadow | `0 12px 32px rgba(13, 27, 42, .12)` | shadow.cardHover | 11 | hover only |

**REVIEW** · 4 PASS · 1 REVIEW · 0 FAIL · 0 STRIP

