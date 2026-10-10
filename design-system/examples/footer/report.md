### report: design-system/examples/footer/block.html

| Result | Category | Found | Token | Lines | Note |
|---|---|---|---|---|---|
| PASS | colour | `backgroundColor: base` | color.base | 1 |  |
| PASS | colour | `has-base-background-color` | color.base | 2 |  |
| PASS | colour | `textColor: accent-2` | color.accent-2 | 4, 45, 61, 74, 87 +2 |  |
| PASS | colour | `has-accent-2-color` | color.accent-2 | 5, 46, 62, 75, 88 +2 |  |
| PASS | colour | `textColor: accent-1` | color.accent-1 | 18 |  |
| PASS | colour | `has-accent-1-color` | color.accent-1 | 19 |  |
| PASS | colour | `backgroundColor: accent-5` | color.accent-5 | 24, 110, 143 |  |
| PASS | colour | `has-accent-5-color` | color.accent-5 | 25, 111 |  |
| PASS | colour | `has-accent-5-background-color` | color.accent-5 | 25, 111, 144 |  |
| PASS | colour | `textColor: accent-4` | color.accent-4 | 55, 144, 160, 164 |  |
| PASS | colour | `has-accent-4-color` | color.accent-4 | 56, 145, 161, 165 |  |
| PASS | colour | `has-accent-1-background-color` | color.accent-1 | 129 |  |
| PASS | colour | `has-base-color` | color.base | 129 |  |
| PASS | colour | `textColor: base` | color.base | 139 |  |
| PASS | font-family | `fontFamily: kalam` | type.family.accent | 45 |  |
| PASS | font-family | `has-kalam-font-family` | type.family.accent | 46 |  |
| PASS | font-size | `fontSize: small` | type.size.small | 4, 55, 61, 74, 87 +4 |  |
| PASS | font-size | `has-small-font-size` | type.size.small | 5, 56, 62, 75, 88 +4 |  |
| PASS | font-size | `fontSize: x-large` | type.size.x-large | 8 |  |
| PASS | font-size | `has-x-large-font-size` | type.size.x-large | 9 |  |
| PASS | font-size | `fontSize: large` | type.size.large | 41 |  |
| PASS | font-size | `has-large-font-size` | type.size.large | 42 |  |
| PASS | font-size | `0.875rem` | type.size.small | 129 |  |
| PASS | radius | `999px` | radius.pill | 129, 143, 144 |  |
| PASS | spacing | `var:preset\|spacing\|70` | spacing.70 | 1 |  |
| PASS | spacing | `var:preset\|spacing\|50` | spacing.50 | 1 |  |
| PASS | spacing | `var:preset\|spacing\|40` | spacing.40 | 1, 28, 114 |  |
| PASS | spacing | `var:preset\|spacing\|30` | spacing.30 | 2, 30, 115, 133, 143 |  |
| PASS | spacing | `padding-top: var(--wp--preset--spacing--70)` | spacing.70 | 2 |  |
| PASS | spacing | `padding-bottom: var(--wp--preset--spacing--50)` | spacing.50 | 2 |  |
| PASS | spacing | `var:preset\|spacing\|20` | spacing.20 | 3, 66, 79, 92, 98 +4 |  |
| PASS | spacing | `gap: var(--wp--preset--spacing--20)` | spacing.20 | 69, 82, 95, 129 |  |
| PASS | spacing | `padding-top: var(--wp--preset--spacing--20)` | spacing.20 | 144 |  |
| PASS | spacing | `padding-bottom: var(--wp--preset--spacing--20)` | spacing.20 | 144 |  |
| PASS | spacing | `padding-left: var(--wp--preset--spacing--30)` | spacing.30 | 144 |  |
| PASS | spacing | `padding-right: var(--wp--preset--spacing--30)` | spacing.30 | 144 |  |

**PASS** · 36 PASS · 0 REVIEW · 0 FAIL · 0 STRIP

### report: design-system/examples/footer/footer.css

| Result | Category | Found | Token | Lines | Note |
|---|---|---|---|---|---|
| FAIL | motion | `animation: wcm-open-pulse 2.4s ease-in-out infinite` | – | 56 | animations are not allowed outside the hero |
| PASS | colour | `#0d1b2a` | color.contrast | 9 |  |
| PASS | colour | `#0073aa` | color.accent-1 | 15 |  |
| PASS | colour | `#6d28d9` | color.accent-3 | 21 |  |
| PASS | colour | `#f2f7fa` | color.accent-5 | 30, 54, 68, 69 |  |
| PASS | colour | `#006b78` | color.accent-2 | 53 |  |
| PASS | font-size | `0.875rem` | type.size.small | 48 |  |
| PASS | motion | `transition: 200ms` | motion.duration | 11 |  |
| PASS | motion | `prefers-reduced-motion guard` | motion | 83 |  |
| PASS | radius | `999px` | radius.pill | 55 |  |
| PASS | spacing | `padding-left: var(--wp--preset--spacing--40)` | spacing.40 | 31 |  |
| PASS | spacing | `margin-left: var(--wp--preset--spacing--20)` | spacing.20 | 46 |  |
| PASS | spacing | `padding: var(--wp--preset--spacing--20)` | spacing.20 | 47 |  |

**FAIL** · 12 PASS · 0 REVIEW · 1 FAIL · 0 STRIP

