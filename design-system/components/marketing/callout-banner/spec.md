# Callout banner

**Group:** marketing · **Blocks:** Group (full, Accent 5, padding 70, constrained, blockGap 40) → Section header (no tagline) + body Paragraph + Buttons (one primary) · **CSS:** none (button hover from `buttons.css`)

## Purpose

A full-width ask with a single action: call for speakers, become a sponsor,
volunteer, get tickets. It is a complete section, so it goes straight between
two other sections and takes care of its own background rhythm.

## Anatomy

```
Group (align full, Accent 5, padding 70 top and bottom, constrained, blockGap 40)
├── Group (flow, blockGap 20)                       ← Section header
│   ├── Paragraph eyebrow  small, 700, uppercase, Accent 2, centred
│   ├── Heading H2         x-large, centred
│   └── Paragraph          one sentence, centred
└── Buttons (centred)
    └── Button             primary, one only
```

## Variants

| Variant | How |
|---|---|
| On a sky-wash neighbour | set the banner background to `base` (white) so the rhythm still alternates |
| Two actions | add a secondary Outline button ("Sponsorship deck") next to the primary; still one primary |
| With a deadline pill | put one Info pill under the paragraph |
| Left-aligned with image | Columns 2: header + button left, image right; only inside a two-column section |

## States

Static section. The button carries the hover and focus states from the
Buttons component.

## Do

* One ask per banner, one primary button.
* H2 as a question or a promise ("Have a story the WordPress community should hear?").
* Keep it under three lines of body copy on desktop.

## Don't

* No Kalam tagline here; the button is the flourish.
* No Cover block, no background image, no parallax.
* No second banner directly after the first.

## Presets used

`accent-5`, `accent-2`, `small`, `x-large`, spacing `20`, `40`, `70`.

## Report
### report: design-system/components/marketing/callout-banner/block.html

| Result | Category | Found | Token | Lines | Note |
|---|---|---|---|---|---|
| PASS | colour | `backgroundColor: accent-5` | color.accent-5 | 1 |  |
| PASS | colour | `has-accent-5-background-color` | color.accent-5 | 2 |  |
| PASS | colour | `textColor: accent-2` | color.accent-2 | 3 |  |
| PASS | colour | `has-accent-2-color` | color.accent-2 | 4 |  |
| PASS | font-size | `fontSize: small` | type.size.small | 3 |  |
| PASS | font-size | `has-small-font-size` | type.size.small | 4 |  |
| PASS | font-size | `fontSize: x-large` | type.size.x-large | 7 |  |
| PASS | font-size | `has-x-large-font-size` | type.size.x-large | 8 |  |
| PASS | spacing | `var:preset\|spacing\|70` | spacing.70 | 1 |  |
| PASS | spacing | `var:preset\|spacing\|40` | spacing.40 | 1 |  |
| PASS | spacing | `var:preset\|spacing\|20` | spacing.20 | 2 |  |
| PASS | spacing | `padding-top: var(--wp--preset--spacing--70)` | spacing.70 | 2 |  |
| PASS | spacing | `padding-bottom: var(--wp--preset--spacing--70)` | spacing.70 | 2 |  |

**PASS** · 13 PASS · 0 REVIEW · 0 FAIL · 0 STRIP

