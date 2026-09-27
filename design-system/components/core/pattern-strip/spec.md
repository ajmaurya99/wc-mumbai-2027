# Pattern strip

**Group:** core · **Blocks:** Group (full, background image repeat-x) → Spacer 60px · **CSS:** none

## Purpose

A full-width decorative band, like the woven textile strip on the Rajasthan
site: under the hero, at the foot of the "Be part" band, or between two
sections that need a hard break instead of an ornament.

## Anatomy

```
Group .wcm-strip (align full, constrained, background image: strip-<name>@2x.png,
                  size auto 60px, position centre, repeat-x)
└── Spacer 60px
```

The Group's Background image control (WordPress 6.5+) sets all of this in
the block; no CSS. Strips tile at 240×60 (PNG at 480×120):

| Name | Motif | Colours |
|---|---|---|
| `train` | local train side, windows | gold, purple, contrast |
| `toran` | marigold garland on a string | marigold, saffron, gold, teal |
| `waves` | three wave bands | blue, teal, purple, marigold dots |
| `kolam` | diamond lattice | purple, teal, marigold, blue |

## Variants

| Variant | How |
|---|---|
| Thinner | Spacer 40px and background size `auto 40px` |
| Inside a coloured band | remove `align: full`; the parent band's width applies (see Be part) |

## Do

* One strip after the hero; one at most elsewhere.
* Keep the Spacer height equal to the background-size height.

## Don't

* No text inside the strip.
* No stretching: always `auto 60px`, never `cover`.

## Presets used

None. Assets: `design-system/assets/png/strip-*@2x.png`.

## Report
### report: design-system/components/core/pattern-strip/block.html

(no gradeable values found)

**PASS** · 0 PASS · 0 REVIEW · 0 FAIL · 0 STRIP

