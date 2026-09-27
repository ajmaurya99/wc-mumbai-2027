# Token → Twenty Twenty-Five preset map

How each token appears in the block editor's pickers, in saved block markup, and
as a class or CSS variable on the front end. Build with the pickers first; the
CSS column exists for the rare rule a picker cannot express.

Source: DESIGN-SYSTEM.md, verified against Styles on 27 Sep 2026. If the Site
Editor's Styles change, update DESIGN-SYSTEM.md first, then tokens.json, then
this file.

## Colour (Styles → Colors → Palette → Theme)

| Token | Hex | Picker label | Slug | Block JSON | Front-end class | CSS variable |
|---|---|---|---|---|---|---|
| color.base | `#FFFFFF` | Base | `base` | `"textColor":"base"` / `"backgroundColor":"base"` | `has-base-color` / `has-base-background-color` | `var(--wp--preset--color--base)` |
| color.contrast | `#0d1b2a` | Contrast | `contrast` | `"textColor":"contrast"` | `has-contrast-color` | `var(--wp--preset--color--contrast)` |
| color.accent-1 | `#0073aa` | Accent 1 | `accent-1` | `"backgroundColor":"accent-1"` | `has-accent-1-background-color` | `var(--wp--preset--color--accent-1)` |
| color.accent-2 | `#006b78` | Accent 2 | `accent-2` | `"textColor":"accent-2"` | `has-accent-2-color` | `var(--wp--preset--color--accent-2)` |
| color.accent-3 | `#6d28d9` | Accent 3 | `accent-3` | `"textColor":"accent-3"` | `has-accent-3-color` | `var(--wp--preset--color--accent-3)` |
| color.accent-4 | `#546776` | Accent 4 | `accent-4` | `"textColor":"accent-4"` | `has-accent-4-color` | `var(--wp--preset--color--accent-4)` |
| color.accent-5 | `#f2f7fa` | Accent 5 | `accent-5` | `"backgroundColor":"accent-5"` | `has-accent-5-background-color` | `var(--wp--preset--color--accent-5)` |
| color.festive.marigold | `#F6A21B` | none (custom) | – | `"style":{"color":{"background":"#F6A21B"}}` | `has-background` + inline style | literal hex only |
| color.festive.saffron | `#E0552D` | none (custom) | – | as above | as above | literal hex only |
| color.festive.gold | `#E8B93B` | none (custom) | – | as above | as above | literal hex only |

A colour set on a block also adds `has-text-color`, `has-background` or
`has-link-color` alongside the preset class. Link colour on a block:
`"style":{"elements":{"link":{"color":{"text":"var:preset|color|base"}}}}`.

Twenty Twenty-Five ships an `accent-6` slot too. It is not part of this system;
leave it unused.

## Typography (Styles → Typography)

| Token | Value | Picker | Slug | Block JSON | Front-end class | CSS variable |
|---|---|---|---|---|---|---|
| type.family.body | Newsreader | Font: Newsreader | `newsreader` | inherited; never set per block | `has-newsreader-font-family` | `var(--wp--preset--font-family--newsreader)` |
| type.family.accent | Kalam (700 only) | Font: Kalam | `kalam` | `"fontFamily":"kalam"` | `has-kalam-font-family` | `var(--wp--preset--font-family--kalam)` |
| type.size.small | `.875rem` | Size: S | `small` | `"fontSize":"small"` | `has-small-font-size` | `var(--wp--preset--font-size--small)` |
| type.size.medium | `1rem` | Size: M | `medium` | `"fontSize":"medium"` | `has-medium-font-size` | `var(--wp--preset--font-size--medium)` |
| type.size.large | `1.38rem` | Size: L | `large` | `"fontSize":"large"` | `has-large-font-size` | `var(--wp--preset--font-size--large)` |
| type.size.x-large | `1.75rem` | Size: XL | `x-large` | `"fontSize":"x-large"` | `has-x-large-font-size` | `var(--wp--preset--font-size--x-large)` |
| type.size.xx-large | `2.15rem` | Size: XXL | `xx-large` | `"fontSize":"xx-large"` | `has-xx-large-font-size` | `var(--wp--preset--font-size--xx-large)` |
| type.weight.bold | 700 | Appearance: Bold | – | `"style":{"typography":{"fontWeight":"700"}}` | inline `font-weight:700` | – |
| type.letterSpacing.eyebrow | `.08em` | Letter spacing | – | `"style":{"typography":{"letterSpacing":"0.08em","textTransform":"uppercase"}}` | inline | – |

Registered but unused, on purpose: Manrope (`manrope`), Fira Code (`fira-code`).
Do not pick them.

Body size (17px fluid to 14px) and heading weight, letter-spacing and line-height
are inherited from Styles. Do not set them per block.

## Spacing (Styles → Layout; spacing controls on Group, Columns, Buttons)

| Token | Value | Picker step | Slug | Block JSON | Front-end |
|---|---|---|---|---|---|
| spacing.20 | `10px` | 1 | `20` | `"var:preset\|spacing\|20"` | inline `var(--wp--preset--spacing--20)` |
| spacing.30 | `20px` | 2 | `30` | `"var:preset\|spacing\|30"` | `var(--wp--preset--spacing--30)` |
| spacing.40 | `30px` | 3 | `40` | `"var:preset\|spacing\|40"` | `var(--wp--preset--spacing--40)` |
| spacing.50 | `clamp(30px, 5vw, 50px)` | 4 | `50` | `"var:preset\|spacing\|50"` | `var(--wp--preset--spacing--50)` |
| spacing.60 | `clamp(30px, 7vw, 70px)` | 5 | `60` | `"var:preset\|spacing\|60"` | `var(--wp--preset--spacing--60)` |
| spacing.70 | `clamp(50px, 7vw, 90px)` | 6 | `70` | `"var:preset\|spacing\|70"` | `var(--wp--preset--spacing--70)` |
| spacing.80 | `clamp(70px, 10vw, 140px)` | 7 | `80` | `"var:preset\|spacing\|80"` | `var(--wp--preset--spacing--80)` |

Where each goes in block JSON:

```json
"style":{"spacing":{
  "padding":{"top":"var:preset|spacing|70","bottom":"var:preset|spacing|70"},
  "margin":{"top":"var:preset|spacing|40"},
  "blockGap":{"top":"var:preset|spacing|30","left":"var:preset|spacing|30"}
}}
```

Padding and margin serialise as inline styles on the block wrapper. `blockGap`
is emitted by WordPress at render time as a generated `wp-container-…` class,
so it never appears in the saved HTML; the preview builder reproduces it.

Layout: content width `800px`, wide `1340px`, root side padding preset 50.
A section is `"align":"full"` + `"layout":{"type":"constrained"}`; inner blocks
constrain to 800px, or 1340px with `"align":"wide"`.

## Radius and shadow

| Token | Value | Where | Block JSON |
|---|---|---|---|
| radius.pill | `999px` | Buttons, info pills | `"style":{"border":{"radius":"999px"}}` (Button: set once in Styles → Blocks → Button) |
| radius.card | `16px` | Cards, images | `"style":{"border":{"radius":"16px"}}` (Image: `"className":"is-style-rounded"` is NOT this; use the radius control) |
| radius.chip | `8px` | Chips | `"style":{"border":{"radius":"8px"}}` |
| shadow.cardHover | `0 12px 32px rgba(13, 27, 42, .12)` | Card hover only | No picker (the Shadow control applies at rest). Custom CSS: `.wcm-card:hover`. |

## Things only CSS can do here

The pickers cover colour, size, family, spacing, radius, alignment and layout.
Add a `wcm-` class and a fenced `/* ==== LANDING: <section> ==== */` block in
Additional CSS for:

* hover and focus states (button hover to accent-3, link underline, card shadow and lift),
* transitions (150–250ms) with the `prefers-reduced-motion` guard,
* festive accents on a child element,
* equal-height logo rows.

Remember the sanitiser: literal values, no `--custom: props`, no `will-change`.
