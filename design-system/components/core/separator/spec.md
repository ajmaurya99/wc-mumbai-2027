# Separator (ornament)

**Group:** core · **Blocks:** Group (flex, nowrap, centred, wide) → Separator, Image, Separator · **CSS:** `separator.css`

## Purpose

A breathing space between sections with a Mumbai motif in the middle: a
dashed teal line, two purple diamonds and one icon. Used where two sections
share a background, or where the page changes topic.

## Anatomy

```
Group .wcm-sep (flex, nowrap, justify centre, align wide, gap 30, padding 40 top and bottom)
├── Separator .wcm-sep__line (Accent 2)     → becomes the dashed line
├── Image  sep-<icon>@2x.png at 200px wide  → diamonds + icon in one PNG
└── Separator .wcm-sep__line
```

The diamonds live inside the artwork so no pseudo-elements are needed; the
sanitiser cannot break it. Icons: `marigold`, `train`, `vadapav`, `chai`,
`taxi`, `gateway` (`design-system/assets/png/sep-*.png`, sources in
`assets/svg`).

## Variants

| Variant | How |
|---|---|
| Icon | swap the image file; keep 200px width |
| Tighter | padding 30 instead of 40 |
| Line colour | Separator colour picker: Accent 2 (default) or Accent 4 |

## States

Static.

## Do

* Use a different icon each time down the page; never the same twice in a row.
* Keep at most one separator between two sections.

## Don't

* No separators inside a section or between a header and its content.
* No new icons outside the palette; draw in `assets/svg` and rasterise.

## Presets used

`accent-2`, spacing `30`, `40`. CSS: `#006b78`.

## Report
### report: design-system/components/core/separator/block.html

| Result | Category | Found | Token | Lines | Note |
|---|---|---|---|---|---|
| PASS | colour | `backgroundColor: accent-2` | color.accent-2 | 2, 10, 16, 24, 30 +1 |  |
| PASS | colour | `has-accent-2-color` | color.accent-2 | 3, 11, 17, 25, 31 +1 |  |
| PASS | colour | `has-accent-2-background-color` | color.accent-2 | 3, 11, 17, 25, 31 +1 |  |
| PASS | spacing | `var:preset\|spacing\|40` | spacing.40 | 1, 15, 29 |  |
| PASS | spacing | `var:preset\|spacing\|30` | spacing.30 | 1, 15, 29 |  |
| PASS | spacing | `padding-top: var(--wp--preset--spacing--40)` | spacing.40 | 2, 16, 30 |  |
| PASS | spacing | `padding-bottom: var(--wp--preset--spacing--40)` | spacing.40 | 2, 16, 30 |  |

**PASS** · 7 PASS · 0 REVIEW · 0 FAIL · 0 STRIP

### report: design-system/components/core/separator/separator.css

| Result | Category | Found | Token | Lines | Note |
|---|---|---|---|---|---|
| PASS | colour | `#006b78` | color.accent-2 | 12 |  |

**PASS** · 1 PASS · 0 REVIEW · 0 FAIL · 0 STRIP

