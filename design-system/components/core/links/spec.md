# Links

**Group:** core · **Blocks:** any rich-text block (Paragraph, List, Heading) · **CSS:** `links.css`

## Purpose

Inline links in body copy and standalone "See the full schedule" links. They
read as text at rest and reveal themselves on hover, so paragraphs stay calm.

## Anatomy

Plain `<a href>` inside a Paragraph. No wrapper block, no class. A standalone
link is its own Paragraph so it gets its own line and 44px of hit area with
the line-height.

## Variants

| Variant | How |
|---|---|
| Inline | link inside running text |
| Standalone | a Paragraph whose whole text is the link |
| On a coloured section (Accent 1/2/3 background) | set the section Group's link colour to Base in the colour picker (`elements.link`), so the text stays white; hover underline stays Accent 1 |

## States

| State | Look | Where set |
|---|---|---|
| Rest | Contrast, no underline | `links.css` (or Styles → Colors → Link) |
| Hover | underline in Accent 1 | `links.css` |
| Focus | 2px Accent 3 ring, 3px offset | `links.css` |
| Transition | 200ms colour and underline colour | `links.css`, reduced-motion guard |

`links.css` scopes to `.entry-content` so header and footer navigation keep
their own styling; buttons are excluded with `:not(.wp-element-button)`.

## Do

* Real link text that says where it goes ("See the full schedule").
* One idea per link; avoid three links in one sentence.

## Don't

* No "click here", no bare URLs as text.
* No colour or weight overrides on individual links.
* No underline at rest; do not re-add it in Styles.

## Presets used

None in the markup. CSS: `#0d1b2a`, `#0073aa`, `#6d28d9`, 200ms.

## Report
### report: design-system/components/core/links/block.html

(no gradeable values found)

**PASS** · 0 PASS · 0 REVIEW · 0 FAIL · 0 STRIP

### report: design-system/components/core/links/links.css

| Result | Category | Found | Token | Lines | Note |
|---|---|---|---|---|---|
| PASS | colour | `#0d1b2a` | color.contrast | 6 |  |
| PASS | colour | `#0073aa` | color.accent-1 | 12 |  |
| PASS | colour | `#6d28d9` | color.accent-3 | 15 |  |
| PASS | motion | `transition: 200ms` | motion.duration | 8 |  |
| PASS | motion | `prefers-reduced-motion guard` | motion | 18 |  |

**PASS** · 5 PASS · 0 REVIEW · 0 FAIL · 0 STRIP

