### report: design-system/examples/why-attend/block.html

| Result | Category | Found | Token | Lines | Note |
|---|---|---|---|---|---|
| PASS | colour | `backgroundColor: accent-5` | color.accent-5 | 1 |  |
| PASS | colour | `has-accent-5-background-color` | color.accent-5 | 2 |  |
| PASS | colour | `textColor: accent-2` | color.accent-2 | 3, 11 |  |
| PASS | colour | `has-accent-2-color` | color.accent-2 | 4, 12 |  |
| PASS | colour | `backgroundColor: base` | color.base | 19, 35, 51 |  |
| PASS | colour | `has-base-background-color` | color.base | 20, 36, 52 |  |
| PASS | font-family | `fontFamily: kalam` | type.family.accent | 11 |  |
| PASS | font-family | `has-kalam-font-family` | type.family.accent | 12 |  |
| PASS | font-size | `fontSize: small` | type.size.small | 3 |  |
| PASS | font-size | `has-small-font-size` | type.size.small | 4 |  |
| PASS | font-size | `fontSize: x-large` | type.size.x-large | 7 |  |
| PASS | font-size | `has-x-large-font-size` | type.size.x-large | 8 |  |
| PASS | font-size | `fontSize: large` | type.size.large | 11, 24, 40, 56 |  |
| PASS | font-size | `has-large-font-size` | type.size.large | 12, 25, 41, 57 |  |
| PASS | radius | `16px` | radius.card | 19, 20, 21, 35, 36 +4 |  |
| PASS | spacing | `var:preset\|spacing\|70` | spacing.70 | 1 |  |
| PASS | spacing | `var:preset\|spacing\|40` | spacing.40 | 1, 19, 35, 51 |  |
| PASS | spacing | `var:preset\|spacing\|20` | spacing.20 | 2 |  |
| PASS | spacing | `padding-top: var(--wp--preset--spacing--70)` | spacing.70 | 2 |  |
| PASS | spacing | `padding-bottom: var(--wp--preset--spacing--70)` | spacing.70 | 2 |  |
| PASS | spacing | `var:preset\|spacing\|30` | spacing.30 | 16 |  |
| PASS | spacing | `padding-top: var(--wp--preset--spacing--40)` | spacing.40 | 20, 36, 52 |  |
| PASS | spacing | `padding-right: var(--wp--preset--spacing--40)` | spacing.40 | 20, 36, 52 |  |
| PASS | spacing | `padding-bottom: var(--wp--preset--spacing--40)` | spacing.40 | 20, 36, 52 |  |
| PASS | spacing | `padding-left: var(--wp--preset--spacing--40)` | spacing.40 | 20, 36, 52 |  |

**PASS** · 25 PASS · 0 REVIEW · 0 FAIL · 0 STRIP

### report: design-system/examples/why-attend/card.css

| Result | Category | Found | Token | Lines | Note |
|---|---|---|---|---|---|
| REVIEW | motion | `transition: transform` | motion.lift | 8 | transform transitions: cards only (4px lift); never on the header |
| PASS | colour | `#6d28d9` | color.accent-3 | 15 |  |
| PASS | motion | `transition: 200ms` | motion.duration | 8 |  |
| PASS | motion | `prefers-reduced-motion guard` | motion | 18 |  |
| PASS | shadow | `0 12px 32px rgba(13, 27, 42, .12)` | shadow.cardHover | 11 | hover only |

**REVIEW** · 4 PASS · 1 REVIEW · 0 FAIL · 0 STRIP

### report: design-system/examples/why-attend/buttons.css

| Result | Category | Found | Token | Lines | Note |
|---|---|---|---|---|---|
| PASS | colour | `#6d28d9` | color.accent-3 | 10, 19 |  |
| PASS | colour | `#FFFFFF` | color.base | 11, 16 |  |
| PASS | colour | `#0073aa` | color.accent-1 | 15 |  |
| PASS | motion | `transition: 200ms` | motion.duration | 7 |  |
| PASS | motion | `prefers-reduced-motion guard` | motion | 22 |  |

**PASS** · 5 PASS · 0 REVIEW · 0 FAIL · 0 STRIP

