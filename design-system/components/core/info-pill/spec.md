# Info pill

**Group:** core · **Blocks:** Group (flex, wrap) → Paragraph × n · **CSS:** none

## Purpose

Short facts at a glance: date, venue, ticket price, contributor day. A row of
pills under the intro or inside a callout, never a paragraph in disguise.

## Anatomy

```
Group (flex, wrap, justify centre, blockGap preset 30)
└── Paragraph  Accent 5 background, radius 999px,
               padding 20 top/bottom, 30 sides,
               <strong>Label</strong> value, optional inline 24px image first
```

Padding choice: the brief fixes "padding 30 sides" and leaves top/bottom open;
preset 20 (10px) was chosen so the pill stays a pill and not a card. Line
height 1.6 plus 10px each side keeps it above 44px tall.

## Variants

| Variant | How |
|---|---|
| Text only | `<strong>Date</strong> 13 February 2027` |
| With icon | inline image 24px (PNG at 2×, 48px file) before the label, `alt=""` |
| On Accent 5 section | change the pill background to `base` so it still reads as a pill |
| Left-aligned row | Group → Justification: Left |
| Linked pill | wrap the value in a link; the link component's hover applies |

## States

Static. If a pill links somewhere, the link hover underline applies to the
text; the pill itself does not change.

## Do

* Three or four pills, each under about 30 characters.
* Bold label, plain value.

## Don't

* No sentences, no wrapping text inside a pill.
* No festive colours as pill backgrounds; sky wash or white only.
* No custom padding or radius values.

## Presets used

`accent-5` (background), spacing `20`, `30`, radius `999px`.

## Report
### report: design-system/components/core/info-pill/block.html

| Result | Category | Found | Token | Lines | Note |
|---|---|---|---|---|---|
| PASS | colour | `backgroundColor: accent-5` | color.accent-5 | 2, 6, 10 |  |
| PASS | colour | `has-accent-5-background-color` | color.accent-5 | 3, 7, 11 |  |
| PASS | radius | `999px` | radius.pill | 2, 3, 6, 7, 10 +1 |  |
| PASS | spacing | `var:preset\|spacing\|30` | spacing.30 | 1, 2, 6, 10 |  |
| PASS | spacing | `var:preset\|spacing\|20` | spacing.20 | 2, 6, 10 |  |
| PASS | spacing | `padding-top: var(--wp--preset--spacing--20)` | spacing.20 | 3, 7, 11 |  |
| PASS | spacing | `padding-right: var(--wp--preset--spacing--30)` | spacing.30 | 3, 7, 11 |  |
| PASS | spacing | `padding-bottom: var(--wp--preset--spacing--20)` | spacing.20 | 3, 7, 11 |  |
| PASS | spacing | `padding-left: var(--wp--preset--spacing--30)` | spacing.30 | 3, 7, 11 |  |

**PASS** · 9 PASS · 0 REVIEW · 0 FAIL · 0 STRIP

