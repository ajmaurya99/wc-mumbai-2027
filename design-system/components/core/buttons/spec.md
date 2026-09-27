# Buttons

**Group:** core · **Blocks:** Buttons → Button · **CSS:** `buttons.css` (hover, focus, outline hover)

## Purpose

The one action a section offers. Primary (fill) for the main action, secondary
(outline) beside it only when a genuinely different second action exists
("Get tickets" + "Contact"). One primary blue button per section.

## Anatomy

```
Buttons (flex, justify centre)
├── Button                         primary: Fill style, theme defaults
└── Button (is-style-outline)      secondary: Outline style, text Accent 1
```

The resting look is not in the markup. It is set once in **Styles → Blocks →
Button**: background Accent 1, text Base, radius 999px, padding `.6rem 1.5rem`,
weight 700, size 16px. The theme default is navy and square; if a pasted button
looks like that, those Styles have not been saved yet.

## Variants

| Variant | How | Notes |
|---|---|---|
| Primary | Button, Fill style (default) | Accent 1 on Base |
| Secondary | Button, Outline style, text colour Accent 1 | core's outline style draws a 2px border in `currentColor`, so the text colour sets the border too |
| Left-aligned pair | Buttons → Justification: Left | for two-column sections |
| Full-width on phones | Button → Width: 100% | optional, for CTA sections |

## States

| State | Primary | Secondary | Where set |
|---|---|---|---|
| Rest | Accent 1 / Base | transparent, 2px Accent 1, text Accent 1 | Styles + block picker |
| Hover | Accent 3 / Base | Accent 1 / Base | `buttons.css` |
| Focus | 2px Accent 3 ring, 3px offset | same | `buttons.css` |
| Transition | 200ms on colour, background, border | same | `buttons.css`, reduced-motion guard |

## Do

* Real verb labels: "Get tickets", "Apply to speak", "Become a sponsor".
* Keep at least 44px tall (the padding and 16px size give this).
* Link to a page, not `#`.

## Don't

* No third button style, no Kalam, no icons inside buttons.
* No two primary buttons in one section.
* No custom colours on individual buttons.

## Presets used

`accent-1` (text colour on the outline variant only); everything else inherits
from Styles → Blocks → Button. CSS: `#6d28d9`, `#0073aa`, `#FFFFFF`, 200ms.

## Report
### report: design-system/components/core/buttons/block.html

| Result | Category | Found | Token | Lines | Note |
|---|---|---|---|---|---|
| PASS | colour | `textColor: accent-1` | color.accent-1 | 6 |  |
| PASS | colour | `has-accent-1-color` | color.accent-1 | 7 |  |

**PASS** · 2 PASS · 0 REVIEW · 0 FAIL · 0 STRIP

### report: design-system/components/core/buttons/buttons.css

| Result | Category | Found | Token | Lines | Note |
|---|---|---|---|---|---|
| PASS | colour | `#6d28d9` | color.accent-3 | 10, 19 |  |
| PASS | colour | `#FFFFFF` | color.base | 11, 16 |  |
| PASS | colour | `#0073aa` | color.accent-1 | 15 |  |
| PASS | motion | `transition: 200ms` | motion.duration | 7 |  |
| PASS | motion | `prefers-reduced-motion guard` | motion | 22 |  |

**PASS** · 5 PASS · 0 REVIEW · 0 FAIL · 0 STRIP

