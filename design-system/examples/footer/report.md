### report: design-system/examples/footer/block.html

| Result | Category | Found | Token | Lines | Note |
|---|---|---|---|---|---|
| PASS | colour | `backgroundColor: base` | color.base | 1 |  |
| PASS | colour | `has-base-background-color` | color.base | 2 |  |
| PASS | colour | `textColor: accent-2` | color.accent-2 | 19, 35, 48, 61, 73 +1 |  |
| PASS | colour | `has-accent-2-color` | color.accent-2 | 20, 36, 49, 62, 74 +1 |  |
| PASS | colour | `textColor: accent-4` | color.accent-4 | 29, 118, 134, 138 |  |
| PASS | colour | `has-accent-4-color` | color.accent-4 | 30, 119, 135, 139 |  |
| PASS | colour | `backgroundColor: accent-5` | color.accent-5 | 84, 117 |  |
| PASS | colour | `has-accent-5-color` | color.accent-5 | 85 |  |
| PASS | colour | `has-accent-5-background-color` | color.accent-5 | 85, 118 |  |
| PASS | colour | `has-accent-1-background-color` | color.accent-1 | 103 |  |
| PASS | colour | `has-base-color` | color.base | 103 |  |
| PASS | colour | `textColor: base` | color.base | 113 |  |
| PASS | font-family | `fontFamily: kalam` | type.family.accent | 19 |  |
| PASS | font-family | `has-kalam-font-family` | type.family.accent | 20 |  |
| PASS | font-size | `fontSize: large` | type.size.large | 15 |  |
| PASS | font-size | `has-large-font-size` | type.size.large | 16 |  |
| PASS | font-size | `fontSize: small` | type.size.small | 29, 35, 48, 61, 73 +3 |  |
| PASS | font-size | `has-small-font-size` | type.size.small | 30, 36, 49, 62, 74 +3 |  |
| PASS | font-size | `0.875rem` | type.size.small | 103 |  |
| PASS | radius | `999px` | radius.pill | 103, 117, 118 |  |
| PASS | spacing | `var:preset\|spacing\|70` | spacing.70 | 1 |  |
| PASS | spacing | `var:preset\|spacing\|50` | spacing.50 | 1 |  |
| PASS | spacing | `var:preset\|spacing\|40` | spacing.40 | 1, 2, 88 |  |
| PASS | spacing | `padding-top: var(--wp--preset--spacing--70)` | spacing.70 | 2 |  |
| PASS | spacing | `padding-bottom: var(--wp--preset--spacing--50)` | spacing.50 | 2 |  |
| PASS | spacing | `var:preset\|spacing\|30` | spacing.30 | 4, 89, 107, 117 |  |
| PASS | spacing | `var:preset\|spacing\|20` | spacing.20 | 40, 53, 66, 72, 95 +3 |  |
| PASS | spacing | `gap: var(--wp--preset--spacing--20)` | spacing.20 | 43, 56, 69, 103 |  |
| PASS | spacing | `padding-top: var(--wp--preset--spacing--20)` | spacing.20 | 118 |  |
| PASS | spacing | `padding-bottom: var(--wp--preset--spacing--20)` | spacing.20 | 118 |  |
| PASS | spacing | `padding-left: var(--wp--preset--spacing--30)` | spacing.30 | 118 |  |
| PASS | spacing | `padding-right: var(--wp--preset--spacing--30)` | spacing.30 | 118 |  |

**PASS** · 32 PASS · 0 REVIEW · 0 FAIL · 0 STRIP

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

