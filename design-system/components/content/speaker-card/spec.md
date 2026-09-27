# Speaker card

**Group:** content · **Blocks:** Columns (wide) → Column → Group `wcm-card` → Image (square), Heading H3, Paragraph (meta) · **CSS:** reuses `card.css`

## Purpose

The speakers grid, and by extension organisers and volunteers. A square photo,
a name, a role. The card treatment is identical to Card so the two can share a
page without looking like two systems.

## Anatomy

```
Columns (align wide, blockGap 30, Stack on mobile)
└── Column ×3
    └── Group .wcm-card (radius 16px, padding 40, Accent 5, blockGap 20)
        ├── Image     1:1, cover, radius 16px, alt = the name
        ├── Heading   H3, large: name
        └── Paragraph small, Accent 4: role, company
```

Gap choice: blockGap preset 20 inside the card keeps the name and role
together under the photo; Card uses the theme default because it has a body
paragraph.

## Variants

| Variant | How |
|---|---|
| With talk title | add a Paragraph (default size) between name and role |
| Linked name | wrap the name in a link to the speaker page; link hover applies |
| Placeholder until announced | one card with the image replaced by a `base`-background Group of the same ratio and the text "Speakers announced in January" |
| Organisers | same card, eyebrow above the grid says "Organisers" |

## States

Same as Card: hover shadow and lift from `card.css`; the photo itself does
not change.

## Do

* Square photos, same crop style, uploaded at 1200×1200.
* Role line under 40 characters.

## Don't

* No social icons row inside the card (no SVG on this platform; keep links on the speaker page).
* No Kalam for names.

## Presets used

`accent-5`, `accent-4` (role text), spacing `20`, `30`, `40`, `large`, `small`, radius `16px`.

## Report
### report: design-system/components/content/speaker-card/block.html

| Result | Category | Found | Token | Lines | Note |
|---|---|---|---|---|---|
| PASS | colour | `backgroundColor: accent-5` | color.accent-5 | 4, 20, 36 |  |
| PASS | colour | `has-accent-5-background-color` | color.accent-5 | 5, 21, 37 |  |
| PASS | colour | `textColor: accent-4` | color.accent-4 | 13, 29, 45 |  |
| PASS | colour | `has-accent-4-color` | color.accent-4 | 14, 30, 46 |  |
| PASS | font-size | `fontSize: large` | type.size.large | 9, 25, 41 |  |
| PASS | font-size | `has-large-font-size` | type.size.large | 10, 26, 42 |  |
| PASS | font-size | `fontSize: small` | type.size.small | 13, 29, 45 |  |
| PASS | font-size | `has-small-font-size` | type.size.small | 14, 30, 46 |  |
| PASS | radius | `16px` | radius.card | 4, 5, 6, 20, 21 +4 |  |
| PASS | spacing | `var:preset\|spacing\|30` | spacing.30 | 1 |  |
| PASS | spacing | `var:preset\|spacing\|40` | spacing.40 | 4, 20, 36 |  |
| PASS | spacing | `var:preset\|spacing\|20` | spacing.20 | 4, 20, 36 |  |
| PASS | spacing | `padding-top: var(--wp--preset--spacing--40)` | spacing.40 | 5, 21, 37 |  |
| PASS | spacing | `padding-right: var(--wp--preset--spacing--40)` | spacing.40 | 5, 21, 37 |  |
| PASS | spacing | `padding-bottom: var(--wp--preset--spacing--40)` | spacing.40 | 5, 21, 37 |  |
| PASS | spacing | `padding-left: var(--wp--preset--spacing--40)` | spacing.40 | 5, 21, 37 |  |

**PASS** · 16 PASS · 0 REVIEW · 0 FAIL · 0 STRIP

### report: design-system/components/content/card/card.css

| Result | Category | Found | Token | Lines | Note |
|---|---|---|---|---|---|
| REVIEW | motion | `transition: transform` | motion.lift | 8 | transform transitions: cards only (4px lift); never on the header |
| PASS | colour | `#6d28d9` | color.accent-3 | 15 |  |
| PASS | motion | `transition: 200ms` | motion.duration | 8 |  |
| PASS | motion | `prefers-reduced-motion guard` | motion | 18 |  |
| PASS | shadow | `0 12px 32px rgba(13, 27, 42, .12)` | shadow.cardHover | 11 | hover only |

**REVIEW** · 4 PASS · 1 REVIEW · 0 FAIL · 0 STRIP

