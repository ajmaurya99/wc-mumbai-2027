# Fact card

**Group:** core · **Blocks:** Group (flex, nowrap, centred) → Image 24px, Group (label, value, note) · **CSS:** `fact-card.css`

## Purpose

A labelled fact with an icon and a teal left edge: key dates, date and venue,
getting there. The stacked cousin of the Info pill, for when the fact has a
label and a value rather than one line.

## Anatomy

```
Group .wcm-fact (flex, nowrap, vertical centre, Accent 5, radius 16px,
                 border left 4px Accent 2, padding 30 top/bottom and 40 sides, gap 30)
├── Image  fact-<icon>@2x.png at 24px (calendar, pin, train, ticket)
└── Group (flow, gap 0)
    ├── Paragraph label  small, Accent 4
    ├── Paragraph value  large, 700
    └── Paragraph note   small, Accent 4 (optional)
```

The left edge is the Group's Border control (left side only, 4px, Accent 2),
which saves as inline styles. The 4px width is a new token (`border.accent`).

## Variants

| Variant | How |
|---|---|
| On a sky-wash section | card background `base` |
| No icon | delete the Image block; the text group stays |
| Stack | wrap several in a Group with blockGap 30 |

## States

Static.

## Do

* Label under 30 characters, value under 40.
* Same icon size on every card in a stack.

## Don't

* No buttons inside; put the action under the stack.
* No other edge colours: Accent 2 only.

## Presets used

`accent-5` or `base`, `accent-2` (edge), `accent-4`, `small`, `large`, spacing `30`, `40`, radius `16px`.

## Report
### report: design-system/components/core/fact-card/block.html

| Result | Category | Found | Token | Lines | Note |
|---|---|---|---|---|---|
| PASS | colour | `backgroundColor: accent-5` | color.accent-5 | 2, 22, 42 |  |
| PASS | colour | `var:preset\|color\|accent-2` | color.accent-2 | 2, 22, 42 |  |
| PASS | colour | `has-accent-5-background-color` | color.accent-5 | 3, 23, 43 |  |
| PASS | colour | `var(--wp--preset--color--accent-2)` | color.accent-2 | 3, 23, 43 |  |
| PASS | colour | `textColor: accent-4` | color.accent-4 | 8, 16, 28, 36, 48 |  |
| PASS | colour | `has-accent-4-color` | color.accent-4 | 9, 17, 29, 37, 49 |  |
| PASS | font-size | `fontSize: small` | type.size.small | 8, 16, 28, 36, 48 |  |
| PASS | font-size | `has-small-font-size` | type.size.small | 9, 17, 29, 37, 49 |  |
| PASS | font-size | `fontSize: large` | type.size.large | 12, 32, 52 |  |
| PASS | font-size | `has-large-font-size` | type.size.large | 13, 33, 53 |  |
| PASS | radius | `16px` | radius.card | 2, 3, 22, 23, 42 +1 |  |
| PASS | spacing | `var:preset\|spacing\|30` | spacing.30 | 1, 2, 22, 42 |  |
| PASS | spacing | `var:preset\|spacing\|40` | spacing.40 | 2, 22, 42 |  |
| PASS | spacing | `padding-top: var(--wp--preset--spacing--30)` | spacing.30 | 3, 23, 43 |  |
| PASS | spacing | `padding-bottom: var(--wp--preset--spacing--30)` | spacing.30 | 3, 23, 43 |  |
| PASS | spacing | `padding-left: var(--wp--preset--spacing--40)` | spacing.40 | 3, 23, 43 |  |
| PASS | spacing | `padding-right: var(--wp--preset--spacing--40)` | spacing.40 | 3, 23, 43 |  |

**PASS** · 17 PASS · 0 REVIEW · 0 FAIL · 0 STRIP

### report: design-system/components/core/fact-card/fact-card.css

(no gradeable values found)

**PASS** · 0 PASS · 0 REVIEW · 0 FAIL · 0 STRIP

