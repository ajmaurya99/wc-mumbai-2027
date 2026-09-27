# Section header

**Group:** core · **Blocks:** Group → Paragraph (eyebrow), Heading H2, Paragraph (Kalam tagline) · **CSS:** none

## Purpose

Opens every section: a small teal eyebrow naming the topic, the H2 that makes
the point, and optionally one line in Kalam for warmth. Gives the page a
consistent rhythm so sections are scannable.

## Anatomy

```
Group (flow, blockGap preset 20)
├── Paragraph   eyebrow: small, 700, uppercase, letter-spacing .08em, Accent 2
├── Heading H2  x-large, Contrast (weight, line-height from Styles)
└── Paragraph   optional tagline: Kalam, large, Accent 2, one line
```

Gap choice: the brief fixes 40 between a header and its content but not the
gap inside the header; preset 20 (10px) was chosen so the eyebrow sits on the
title. The 40 belongs on the parent section's blockGap, not here.

## Variants

| Variant | How |
|---|---|
| Centred (default) | as in `block.html`; for symmetric sections: sponsors, speakers, CTA |
| Left-aligned | remove `"align":"center"` / `"textAlign":"center"` and the `has-text-align-center` classes; for two-column sections |
| No tagline | delete the Kalam paragraph; most sections |
| On Accent 5 background | unchanged; teal and contrast keep AA on sky wash |

## States

Static. No hover, no motion.

## Do

* Eyebrow: one or two words ("Speakers", "Venue", "Call for sponsors").
* H2 that says something ("Voices from the WordPress community"), 3 to 8 words.
* Tagline: one line, no full stop, teal only.

## Don't

* No Kalam anywhere except the tagline; never for the H2.
* No H1 here; the page title is the only H1.
* No manual bold or size on the H2; the preset carries it.

## Presets used

`accent-2` (text), `small`, `x-large`, `large`, `kalam`, spacing `20`.

## Report
### report: design-system/components/core/section-header/block.html

| Result | Category | Found | Token | Lines | Note |
|---|---|---|---|---|---|
| PASS | colour | `textColor: accent-2` | color.accent-2 | 2, 10 |  |
| PASS | colour | `has-accent-2-color` | color.accent-2 | 3, 11 |  |
| PASS | font-family | `fontFamily: kalam` | type.family.accent | 10 |  |
| PASS | font-family | `has-kalam-font-family` | type.family.accent | 11 |  |
| PASS | font-size | `fontSize: small` | type.size.small | 2 |  |
| PASS | font-size | `has-small-font-size` | type.size.small | 3 |  |
| PASS | font-size | `fontSize: x-large` | type.size.x-large | 6 |  |
| PASS | font-size | `has-x-large-font-size` | type.size.x-large | 7 |  |
| PASS | font-size | `fontSize: large` | type.size.large | 10 |  |
| PASS | font-size | `has-large-font-size` | type.size.large | 11 |  |
| PASS | spacing | `var:preset\|spacing\|20` | spacing.20 | 1 |  |

**PASS** · 11 PASS · 0 REVIEW · 0 FAIL · 0 STRIP

