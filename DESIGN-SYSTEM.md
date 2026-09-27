# WordCamp Mumbai 2027 — design system for the site

Brief for building https://mumbai.wordcamp.org/2027/ with WordPress core blocks on the
Twenty Twenty-Five theme. Everything below applies to the landing page and all inner
pages. Verified against the Site Editor's saved Styles on 27 Sep 2026.

The animated hero at the top of the home page is a separate custom build (a Custom
HTML block plus CSS prefixed `wcm-`). Treat it as finished: do not edit it, restyle it,
or reuse its classes. It shares the palette below, so anything you build will sit
naturally under it.

## 1. Platform constraints (WordCamp.org)

These are enforced by the platform, not preferences. Design around them.

1. **No JavaScript.** `<script>` is stripped from content. Use what core blocks provide
   (Navigation overlay, Details block, Embed block) and CSS hover/focus states.
2. **Custom HTML blocks are sanitised.** No `<style>`, `<svg>`, `<input>`, `<iframe>`.
   Build with core blocks; reach for Custom HTML only as a last resort.
3. **Additional CSS is sanitised.** CSS custom properties you define (`--x:`) and
   `will-change` are stripped. Use literal hex colours. Theme presets such as
   `var(--wp--preset--color--accent-1)` are fine to reference.
4. **SVG upload is blocked.** Use PNG or WebP at 2× size in the media library.
5. Prefer block settings (colour, spacing, typography pickers) over custom CSS.
   When CSS is needed, prefix classes with `wcm-`, add it to
   **Appearance → Customize → Additional CSS** under a fenced comment such as
   `/* ==== LANDING: <section> ==== */`. Leave the Site Editor's own Styles CSS box empty.
6. After saving CSS, reload and confirm the rule survived. If it vanished, it used a
   stripped feature; rewrite it with literal values.

## 2. Colour

Theme palette as saved in Styles → Colors. Use the presets from the block colour
picker; the hex values are for the rare custom CSS rule.

| Preset | Hex | Use for |
|---|---|---|
| Base | `#FFFFFF` | Page ground, cards on tinted sections |
| Contrast | `#0d1b2a` | Body text, headings |
| Accent 1 (blue) | `#0073aa` | Primary buttons, links, active states |
| Accent 2 (teal) | `#006b78` | Eyebrows, taglines, secondary accents |
| Accent 3 (purple) | `#6d28d9` | Button hover, focus rings, small highlights |
| Accent 4 (slate) | `#546776` | Meta text, captions, icons |
| Accent 5 (sky wash) | `#f2f7fa` | Alternate section backgrounds, cards, tints |

Festive accents, sparingly, for badges and dividers only: marigold `#F6A21B`,
saffron `#E0552D`, gold `#E8B93B`. Do not introduce other hues.

Rules: page ground is white; alternate sections in sky wash for rhythm. One primary
blue button per section. Text on blue, teal or purple is white; on white or sky wash
it is contrast. Keep AA contrast.

Bands (added 28 Sep 2026 for the home page): at most one **dark band** per screen,
Contrast background with Base text and a Base-filled button (text Contrast); and one
**gradient band** per page, `linear-gradient(135deg, #0073aa 0%, #6d28d9 100%)`
(Accent 1 to Accent 3) with Base text, a Base-filled button (text Accent 3) and a
Base outline button. No other gradients.

Decorative backgrounds: a section Group may carry one background image from
`design-system/assets/png` set in the block's Background control: a subtle tile
(`tile-lattice-*`, `tile-waves-*`, size 120px, repeat) or one corner motif
(`motif-*`, 320–420px, no-repeat, anchored to a corner). Tiles are white lines on
sky wash or Accent 1/2 at 7–8% on white; motifs are palette colours at 10%.

## 3. Typography

Set in Styles → Typography. Do not override fonts in CSS.

* **Body and headings: Newsreader** (serif). Body 400, 17px fluid to 14px on phones,
  line-height 1.6. Headings 700, letter-spacing -0.01em, line-height 1.2.
* **Accent: Kalam** (preset `kalam`, only the 700 face is installed so it always
  renders bold). One-line flourishes only: a section tagline or pull quote, in teal.
  Never for body text or buttons.
* Also registered but unused: Manrope, Fira Code. Leave them unused.

Size presets (typography picker): small `.875rem` · medium `1rem` · large `1.38rem` ·
x-large `1.75rem` · xx-large `2.15rem`.

| Element | Preset | Weight | Colour |
|---|---|---|---|
| Page title / hero-like H1 | xx-large | 700 | Contrast |
| Section title (H2) | x-large | 700 | Contrast |
| Eyebrow above H2 | small, uppercase, letter-spacing `.08em` | 700 | Accent 2 |
| Kalam tagline | large | 700 | Accent 2 |
| Card title (H3) | large | 700 | Contrast |
| Body | default | 400 | Contrast, max 65ch |
| Meta / captions | small | 400 | Accent 4 |
| Buttons | 16px (theme) | 700 | see §5 |

## 4. Layout and spacing

Saved layout: content width **800px**, wide **1340px**, root side padding preset 50,
root top padding 0.

Spacing presets: 20 = 10px · 30 = 20px · 40 = 30px · 50 = clamp(30px, 5vw, 50px) ·
60 = clamp(30px, 7vw, 70px) · 70 = clamp(50px, 7vw, 90px) · 80 = clamp(70px, 10vw, 140px).

* A section is a full-width Group (alignment Full width, background set in the
  colour picker) containing a constrained inner Group. Section padding preset **70**
  top and bottom.
* Preset **40** between a section title and its content, **30** between cards or
  list items.
* Grids: Columns block, 3 columns desktop, 2 tablet, 1 phone (Stack on mobile on).
* Radii: buttons and pills `999px`; cards and images `16px`; chips `8px`.
* Never set negative margins or `100vw` widths; use Full width alignment instead.

## 5. Components (all core blocks)

**Primary button** — Buttons block, Fill style. Set once in Styles → Blocks → Button:
background Accent 1, text Base, radius 999px, padding `.6rem 1.5rem`, weight 700.
Hover: background Accent 3. (The theme default is navy and square; override it.)

**Secondary button** — Buttons block, Outline style: 2px Accent 1 border, Accent 1
text, radius 999px. Hover: fill Accent 1, text Base.

**Links** — Contrast colour, no underline at rest, underline on hover in Accent 1.

**Focus ring** — `outline: 2px solid #6d28d9; outline-offset: 3px`, always visible.

**Section header** — Paragraph (eyebrow, small, uppercase, Accent 2) + Heading H2 +
optional Paragraph in Kalam, Accent 2. Centre on symmetric sections (sponsors,
speakers, CTA); left-align in two-column sections.

**Info pill** — Paragraph with Accent 5 background, radius 999px, padding 30 sides,
optional inline icon. Short facts: date, venue, ticket price.

**Card** — Group with 16px radius and padding 40. Base on sky-wash sections, Accent 5
on white sections. No border; shadow `0 12px 32px rgba(13, 27, 42, .12)` on hover only.
Order: Image (16px radius, 16:10) → H3 → one or two lines → link.
Speaker cards: square photo, name H3, role in meta style.

**Sponsor tier grid** — Image blocks in Columns, equal-height rows, tier name as an
eyebrow. Never distort logos.

**Callout banner** — Full-width Group in Accent 5 with a section header and one primary
button. For "Call for speakers", "Become a sponsor".

**Details block** — for FAQs; the only expand/collapse that works without JavaScript.

Added 28 Sep 2026, all in `design-system/components`:

**Fact card** — Group, flex, Accent 5 (Base on sky wash), radius 16px, 4px Accent 2 left
edge, 24px icon, small Accent 4 label, large bold value, optional note.

**Stat tile** — Card with the number in xx-large Accent 1, an uppercase small label in
Accent 4 and one line. Three or four per row.

**Separator** — Group, flex: Separator, Image (diamond-icon-diamond PNG, 200px),
Separator; CSS makes the separators a dashed 2px Accent 2 line.

**Pattern strip** — full-width Group with a 60px repeat-x background tile
(`strip-train`, `strip-toran`, `strip-waves`, `strip-kolam`) and a 60px Spacer.

**Status chip** — inside a card: Group, flex, Base, radius 8px, padding 20/30, small
700 text in Accent 2 (open) or Accent 4 (coming soon).

**Numbered point** — Group, flex, nowrap: Paragraph numeral (x-large, 700, Accent 1)
beside a Group with H3 and one line. Four points beside a 4:5 photo.

## 6. Motion

Keep everything calm; the hero is the only animated element on the site.

* Allowed: 150–250ms hover transitions on colour, underline and shadow, and a 4px
  lift on cards.
* Not allowed: looping animations, Cover block parallax, auto-advancing carousels.
* Wrap any animation or transition in
  `@media (prefers-reduced-motion: reduce) { animation: none; transition: none; }`.
* Never animate `transform` on the header; core's mobile menu overlay breaks inside a
  transformed ancestor.

## 7. Imagery

Artwork lives in `design-system/assets` as SVG sources and PNG at 2× (SVG upload is
blocked): six separator icons (marigold, local train, vada pav, cutting chai, taxi,
Gateway of India), four 24px fact icons, four pattern strips, four section tiles and
three corner motifs. Draw new pieces flat, in the palette, and rasterise with
`design-system/tools/rasterise.py`.

Flat, friendly, daylight. Photos for speakers, venue and past events; illustrations
in the palette above for everything else. Icons: simple line or flat, Contrast or
Accent 1, 24px, uploaded as PNG at 2×. Ask before reusing hero artwork; it can be
exported as PNG at the size needed.

## 8. Quality bar

* AA contrast everywhere.
* One H1 per page; sections start at H2.
* Every interactive element: 44px minimum target, visible focus, real link text.
* Check at 320px, 390px, 768px portrait, 1366px and 1920px. No horizontal scroll.
* After each section, load the page on a phone and open the header menu once.

## 9. Landing page sections (suggested order)

1. Intro — what WordCamp Mumbai is; two columns, text and image.
2. Key facts — three or four info pills: date, venue, tickets, contributor day.
3. Callout — call for speakers / sponsors.
4. Speakers grid (placeholder until announced).
5. Schedule teaser linking to the schedule page.
6. Sponsors by tier.
7. Venue — Embed block map, address, travel tips.
8. Community / past WordCamps gallery (optional).
9. Final CTA — "Get tickets" primary, "Contact" secondary.

Alternate white and sky-wash backgrounds; each section gets one clear action.
