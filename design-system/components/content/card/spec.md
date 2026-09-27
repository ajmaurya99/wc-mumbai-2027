# Card

**Group:** content · **Blocks:** Columns (wide) → Column → Group `wcm-card` → Image, Heading H3, Paragraph, Paragraph (link) · **CSS:** `card.css` (hover shadow, lift, equal heights, focus)

## Purpose

The unit for anything that comes in threes: what to expect, schedule teasers,
venue facts, past WordCamps. `block.html` ships a full three-card row because
that is how cards are always used; one card is one Column's contents.

## Anatomy

```
Columns (align wide, blockGap 30 rows and columns, Stack on mobile)
└── Column ×3
    └── Group .wcm-card (radius 16px, padding 40, Accent 5, flow)
        ├── Image     16:10, cover, radius 16px, size Large
        ├── Heading   H3, large
        ├── Paragraph one or two lines
        └── Paragraph link
```

Order is fixed: image, title, text, link. Gap inside the card is the theme
default block gap (not overridden). Card width follows the Columns block:
3 on desktop, 2 on tablet, 1 on phones.

## Variants

| Variant | How |
|---|---|
| On a white section (default) | card background `accent-5` |
| On a sky-wash section | card background `base` |
| No image | delete the Image block; the rest is unchanged |
| Two cards | Columns with two Columns; keep `align: wide` |
| Whole card clickable | not possible without JavaScript or Custom HTML; keep the text link |

## States

| State | Look | Where set |
|---|---|---|
| Rest | no border, no shadow | block settings |
| Hover | shadow `0 12px 32px rgba(13,27,42,.12)` and 4px lift | `card.css` |
| Link focus | 2px Accent 3 ring, 3px offset | `card.css` |
| Reduced motion | no transition, no lift | `card.css` |

Report note: `transition: transform` is flagged REVIEW by design; the 4px lift
is the one transform the brief allows, and it is on a card, never the header.

## Do

* Same image ratio on every card in a row (16:10, uploaded at 1600×1000).
* Titles of similar length so rows stay even; `height: 100%` covers the rest.
* One link per card, descriptive text.

## Don't

* No borders, no shadow at rest, no rounded-corner values other than 16px.
* No buttons inside cards; a text link is enough.
* No 4-column rows; three is the maximum.

## Presets used

`accent-5` (or `base`), spacing `30`, `40`, `large`, radius `16px`. CSS: the
hover shadow token, `#6d28d9`, 200ms.

## Report
### report: design-system/components/content/card/block.html

| Result | Category | Found | Token | Lines | Note |
|---|---|---|---|---|---|
| PASS | colour | `backgroundColor: accent-5` | color.accent-5 | 4, 24, 44 |  |
| PASS | colour | `has-accent-5-background-color` | color.accent-5 | 5, 25, 45 |  |
| PASS | font-size | `fontSize: large` | type.size.large | 9, 29, 49 |  |
| PASS | font-size | `has-large-font-size` | type.size.large | 10, 30, 50 |  |
| PASS | radius | `16px` | radius.card | 4, 5, 6, 24, 25 +4 |  |
| PASS | spacing | `var:preset\|spacing\|30` | spacing.30 | 1 |  |
| PASS | spacing | `var:preset\|spacing\|40` | spacing.40 | 4, 24, 44 |  |
| PASS | spacing | `padding-top: var(--wp--preset--spacing--40)` | spacing.40 | 5, 25, 45 |  |
| PASS | spacing | `padding-right: var(--wp--preset--spacing--40)` | spacing.40 | 5, 25, 45 |  |
| PASS | spacing | `padding-bottom: var(--wp--preset--spacing--40)` | spacing.40 | 5, 25, 45 |  |
| PASS | spacing | `padding-left: var(--wp--preset--spacing--40)` | spacing.40 | 5, 25, 45 |  |

**PASS** · 11 PASS · 0 REVIEW · 0 FAIL · 0 STRIP

### report: design-system/components/content/card/card.css

| Result | Category | Found | Token | Lines | Note |
|---|---|---|---|---|---|
| REVIEW | motion | `transition: transform` | motion.lift | 8 | transform transitions: cards only (4px lift); never on the header |
| PASS | colour | `#6d28d9` | color.accent-3 | 15 |  |
| PASS | motion | `transition: 200ms` | motion.duration | 8 |  |
| PASS | motion | `prefers-reduced-motion guard` | motion | 18 |  |
| PASS | shadow | `0 12px 32px rgba(13, 27, 42, .12)` | shadow.cardHover | 11 | hover only |

**REVIEW** · 4 PASS · 1 REVIEW · 0 FAIL · 0 STRIP

