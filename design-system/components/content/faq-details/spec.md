# FAQ (Details)

**Group:** content · **Blocks:** Group (flow, blockGap 30) → Details `wcm-faq` ×n → Paragraph · **CSS:** `faq-details.css`

## Purpose

Questions and answers that expand in place. The Details block is the only
expand/collapse on WordCamp.org that works without JavaScript, so it is the
FAQ, the "what is included" list and the travel tips.

## Anatomy

```
Group (flow, blockGap 30)
└── Details .wcm-faq ×n  (Accent 5, radius 16px, padding 40)
    ├── summary   the question (bold via CSS)
    └── Paragraph the answer (any blocks allowed)
```

The item uses the Card tokens (Accent 5, 16px, padding 40) so FAQ items and
cards share one visual language. On a sky-wash section, set the item
background to `base`.

## Variants

| Variant | How |
|---|---|
| Open by default | Details → "Open by default" (adds `open` to the tag) |
| Rich answer | put a List or a Buttons block inside the Details after the Paragraph |
| Two columns of FAQs | Columns → two Columns, each with its own Group of Details |

## States

| State | Look | Where set |
|---|---|---|
| Closed | question with an Accent 1 marker | `faq-details.css` |
| Open | answer revealed, preset 30 below the question | native `<details>`, `faq-details.css` |
| Focus on the question | 2px Accent 3 ring, 3px offset | `faq-details.css` |
| Hover | pointer cursor only; no colour change | `faq-details.css` |

Note: `faq-details.css` references `var(--wp--preset--spacing--30)`; theme
preset variables survive the sanitiser (only custom `--x` definitions are
stripped) and `report.py` grades them PASS.

## Do

* Question as a real question, under 70 characters.
* Answer in one or two short paragraphs; link out for detail.
* Six to eight items at most; split by topic beyond that.

## Don't

* No nested Details.
* No Custom HTML accordion; it would be stripped or need JavaScript.
* No heading blocks inside the summary.

## Presets used

`accent-5`, spacing `30`, `40`, radius `16px`. CSS: `#0073aa`, `#6d28d9`.

## Report
### report: design-system/components/content/faq-details/block.html

| Result | Category | Found | Token | Lines | Note |
|---|---|---|---|---|---|
| PASS | colour | `backgroundColor: accent-5` | color.accent-5 | 3, 9, 15 |  |
| PASS | colour | `has-accent-5-background-color` | color.accent-5 | 4, 10, 16 |  |
| PASS | radius | `16px` | radius.card | 3, 4, 9, 10, 15 +1 |  |
| PASS | spacing | `var:preset\|spacing\|30` | spacing.30 | 1 |  |
| PASS | spacing | `var:preset\|spacing\|40` | spacing.40 | 3, 9, 15 |  |
| PASS | spacing | `padding-top: var(--wp--preset--spacing--40)` | spacing.40 | 4, 10, 16 |  |
| PASS | spacing | `padding-right: var(--wp--preset--spacing--40)` | spacing.40 | 4, 10, 16 |  |
| PASS | spacing | `padding-bottom: var(--wp--preset--spacing--40)` | spacing.40 | 4, 10, 16 |  |
| PASS | spacing | `padding-left: var(--wp--preset--spacing--40)` | spacing.40 | 4, 10, 16 |  |

**PASS** · 9 PASS · 0 REVIEW · 0 FAIL · 0 STRIP

### report: design-system/components/content/faq-details/faq-details.css

| Result | Category | Found | Token | Lines | Note |
|---|---|---|---|---|---|
| PASS | colour | `#0073aa` | color.accent-1 | 11 |  |
| PASS | colour | `#6d28d9` | color.accent-3 | 14 |  |
| PASS | spacing | `margin-bottom: var(--wp--preset--spacing--30)` | spacing.30 | 18 |  |

**PASS** · 3 PASS · 0 REVIEW · 0 FAIL · 0 STRIP

