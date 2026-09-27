# Sponsor tier grid

**Group:** marketing · **Blocks:** Group (wide, constrained, blockGap 40) → per tier: Paragraph (eyebrow) + Columns (wide) → Column → Image (linked) · **CSS:** none

## Purpose

Sponsors by tier on the landing page and the sponsors page. Logos are the
sponsor's asset, so the component's whole job is to give every logo the same
box, keep proportions and link out.

## Anatomy

```
Group (align wide, constrained, blockGap 40)
├── Paragraph  tier eyebrow: small, 700, uppercase, Accent 2, centred
├── Columns (align wide, blockGap 30, Stack on mobile)
│   └── Column ×3
│       └── Image  3:2 box, scale Contain, linked, alt = sponsor name
├── Paragraph  next tier eyebrow
└── Columns …
```

The wrapper is wide so the Columns can be wide; a plain Group would cap them
at the 800px content width. Each tier is one eyebrow plus one Columns row;
add more rows for more logos, three per row.

The Image block's Scale: Contain writes `object-fit: contain` inline, and the
fixed 3:2 aspect ratio makes every logo box the same height, so rows are equal
and nothing is stretched. Upload logos as PNG or WebP at 2× (at least
1200×800 with the mark centred on a transparent or white background).

## Variants

| Variant | How |
|---|---|
| Tier weight | Gold three per row; Silver and Bronze also three per row, just more rows. Do not shrink boxes per tier; use more rows instead |
| On a sky-wash section | wrap each Image in a `base` Group with radius 16px and padding 40 (the Card container) so logos sit on white |
| Community partners | same grid, eyebrow "Community partners", unlinked images allowed |
| Empty tier | one card with a text link "Become a sponsor"; see Callout banner |

## States

Static. Linked logos get the link focus ring from the theme; no hover effect
on logos.

## Do

* `alt` = sponsor name, every time.
* `rel="sponsored"` on logo links.
* Tier names as eyebrows, never as H2s (the section's H2 is "Sponsors").

## Don't

* No cropping (Scale: Cover) on logos.
* No greyscale filters or opacity changes.
* No mixed ratios in one row.

## Presets used

`accent-2`, `small`, spacing `30`, `40`.

## Report
### report: design-system/components/marketing/sponsor-tier-grid/block.html

| Result | Category | Found | Token | Lines | Note |
|---|---|---|---|---|---|
| PASS | colour | `textColor: accent-2` | color.accent-2 | 3, 27 |  |
| PASS | colour | `has-accent-2-color` | color.accent-2 | 4, 28 |  |
| PASS | font-size | `fontSize: small` | type.size.small | 3, 27 |  |
| PASS | font-size | `has-small-font-size` | type.size.small | 4, 28 |  |
| PASS | spacing | `var:preset\|spacing\|40` | spacing.40 | 1 |  |
| PASS | spacing | `var:preset\|spacing\|30` | spacing.30 | 7, 31 |  |

**PASS** · 6 PASS · 0 REVIEW · 0 FAIL · 0 STRIP

