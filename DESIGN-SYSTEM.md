# WordCamp Mumbai 2027 — landing page design system

Brief for building the rest of https://mumbai.wordcamp.org/2027/ with WordPress core
blocks, matching the animated hero that already sits at the top of the page.

Read this whole file before designing anything. The "Platform constraints" section
explains why several normal WordPress techniques are unavailable here.

## 1. What already exists

* **The hero** fills the first screen: sky gradient, drifting clouds, the logo, a Kalam
  tagline, a blue date pill, the venue line, a plane towing a #WCMumbai banner, and an
  illustrated Mumbai skyline (CSMT, Rajabai, Sea Link, Gateway of India, Taj, a Ganpati
  pandal, Antilia, a local train, BEST bus, taxi, vada pav cart, dabbawala). Landmarks
  show tooltips on hover; the pandal gets a diya cursor and a marigold shower.
* **The header** is the theme's Header template part. On the home page only it floats
  over the hero with no background, its logo/date/venue hidden. Other pages show it
  normally. Menu items live in the header's Navigation block.
* **The footer** is the theme's Footer template part, in normal flow below the content.
* Source of truth: https://github.com/ajmaurya99/wc-mumbai-2027
  (`hero-block.html`, `hero.css`, SVG assets, `README.md`). The hero's CSS is pasted
  into Appearance → Customize → Additional CSS. Do not restyle anything prefixed `wcm-`.

Everything below the hero is yours to build.

## 2. Platform constraints (WordCamp.org, Twenty Twenty-Five)

These are enforced by the site, not preferences.

1. **No JavaScript.** `<script>` is stripped from content. Interactivity is CSS only
   (hover, focus, `<details>`), or whatever core blocks ship with (Navigation overlay,
   Details block, Cover block parallax is fine).
2. **Custom HTML blocks are sanitised** with `wp_kses_post`: no `<style>`, `<svg>`,
   `<input>`, `<iframe>`, no `autoplay`. `div/p/a/img/span/ul/details/summary/button`
   with `class`, `style`, `data-*` and `aria-*` attributes survive. Prefer core blocks.
3. **Additional CSS is sanitised** by CSSTidy. It strips **CSS custom properties**
   (`--x:` declarations and therefore `var(--x)` of your own), `will-change`, and
   container-query units. Use literal hex colours. Theme presets such as
   `var(--wp--preset--color--accent-1)` are fine to *reference*.
4. **SVG upload is blocked.** PNG/JPG/WebP go in the media library. SVGs live in the
   GitHub repo and are served by jsDelivr, pinned to a commit hash.
5. **Content width** is 800px, **wide** 1340px. Full-width blocks need the
   "Full width" alignment; a stray `100vw` trick fights the theme's constrained layout.
6. Prefer block settings (colour, spacing, typography pickers) over custom CSS. When
   CSS is needed, prefix classes with `wcm-`, keep it in a clearly fenced section of
   Additional CSS, and keep selectors simple.

## 3. Colour

Brand colours, pulled from the logo. Use these exact values in custom CSS; in the
block colour picker use the closest theme preset named in the right column.

| Role | Hex | Theme preset (block picker) | Use for |
|---|---|---|---|
| Blue (primary) | `#0A6CB5` | accent-1 `#0073aa` | Primary buttons, links, date pill, active states |
| Teal | `#1B7A78` | accent-2 `#006b78` | Tagline, secondary accents, section eyebrows |
| Purple | `#5B2DB8` | accent-3 `#6d28d9` | Button hover, focus rings, small highlights |
| Navy (text) | `#1A2447` | contrast `#0d1b2a` | Body text, headings, nav links |
| Sky | `#BFE3F7` → `#E4F2FB` | — | Hero sky gradient, light section tints |
| Sky wash | `#EAF5FC` | accent-5 `#f2f7fa` | Alternate section backgrounds, cards, the mobile menu overlay |
| White | `#FFFFFF` | base | Page ground, cards on tinted sections |

Warm accents used sparingly in the artwork, available for festive touches only
(badges, marigold dividers, the Ganpati section if any):
marigold `#F6A21B`, saffron `#E0552D`, gold `#E8B93B`, pandal maroon `#8E1B2E`.

Rules:
* Page ground is white; alternate sections in **sky wash** to create rhythm.
* One primary blue CTA per section. Secondary actions are outlined in blue or plain
  navy links with the underline treatment (see §6).
* Text on blue/purple/teal is white. Text on sky/white is navy. Keep AA contrast.
* Do not introduce new hues. Greens, reds and oranges belong to the illustration.

## 4. Typography

* **Body and headings: Manrope** (theme default; select it in the block typography
  picker, or leave inherit). Weights: 400 body, 500 nav/labels, 600 buttons, 700 headings.
* **Accent: Kalam** (theme preset `kalam`). Only for one-line flourishes such as a
  section tagline or a pull quote, in teal, 500 weight. Never for body text or buttons.
* Navy for all text; teal only for Kalam flourishes and eyebrows.

Scale (use clamp so it tracks the hero):

| Element | Size | Weight | Notes |
|---|---|---|---|
| Section title (H2) | `clamp(1.75rem, 3.2vw, 2.5rem)` | 700 | Centred on centred sections, else left |
| Eyebrow above H2 | `.85rem`, uppercase, letter-spacing `.08em` | 600 | Teal |
| Kalam tagline | `clamp(1.05rem, 1.6vw, 1.35rem)` | 500 | Teal, matches the hero |
| Card title (H3) | `1.25rem` | 700 | |
| Body | `1.05rem` | 400 | line-height 1.6, max 65ch |
| Small / meta | `.9rem` | 500 | navy at 70% opacity is fine |
| Buttons | `1.05rem` | 600 | |

## 5. Layout and spacing

* Sections are full-width Group blocks (alignment: Full width) with an inner
  constrained Group. Section padding: theme spacing preset **70** top and bottom
  (`clamp(50px, 7vw, 90px)`); **60** on phones if it feels tall.
* Inside sections use preset **40** (30px) between title and content, **30** (20px)
  between cards or list items.
* Grids: Columns block, 3 columns desktop, 2 tablet, 1 phone (stack on mobile on).
  Cards: white on sky-wash sections, sky-wash on white sections; radius **16px**;
  padding preset 40; no border; shadow `0 12px 32px rgba(26, 36, 71, .12)` on hover only.
* Corner radii: pills and buttons `999px`; cards and images `16px`; small chips `8px`.
* Keep the horizontal gutter the theme provides (root padding); never set negative margins.

## 6. Components

**Primary button** — Buttons block, style Fill, background blue `#0A6CB5`, text white,
radius 999px, padding `.6rem 1.5rem`, weight 600. Hover: purple `#5B2DB8`. This is the
hero's date pill and the old Contact button; keep it identical.

**Secondary button** — Buttons block, style Outline, border 2px blue, text blue,
radius 999px. Hover: fill blue, text white.

**Text link / nav-style link** — navy, no underline at rest, a 2px blue underline that
grows in from the centre on hover (`background-image` gradient trick, see the
`HERO NAV` section of `hero.css`). Minimum 44px tap height for anything tappable.

**Focus ring** — `outline: 2px solid #5B2DB8; outline-offset: 3px`. Always visible for
keyboard users.

**Eyebrow + title + Kalam line** — the section header pattern:
teal uppercase eyebrow, navy H2, optional Kalam teal line under it. Centre it on
symmetric sections (sponsors, speakers, CTA); left-align in two-column sections.

**Info pill** — white or sky-wash pill with a small icon and short text (e.g. date,
venue, "Tickets from ₹…"). Same shape as the date pill, navy text.

**Card** — see §5. Content order: image (16px radius, 16:10), H3, one or two lines,
optional link. Speaker cards: square photo, name H3, role in small/meta.

**Sponsor tier grid** — logos on white, greyscale off, equal-height rows,
tier heading as eyebrow. Never distort logos; use the Image block's contain scaling.

**Banner / callout** — full-width sky-wash strip with the eyebrow-title pattern and
one primary button, used for "Call for speakers", "Become a sponsor".

## 7. Motion

The hero moves; the rest of the page should be calm so the hero stays the event.

* Allowed: hover transitions of 150–250ms on colour, underline, shadow, and a
  4px lift (`transform: translateY(-4px)`) on cards. A single one-time fade-in on a
  section's title is fine (opacity only, ≤ .9s).
* Not allowed: looping animations below the hero, parallax on Cover blocks,
  auto-advancing carousels, anything that competes with the skyline.
* Wrap every animation in `@media (prefers-reduced-motion: reduce) { animation: none; transition: none; }`.
* Never animate `transform` on the header or its ancestors: the mobile menu overlay
  is `position: fixed` and a transformed ancestor traps it.

## 8. Imagery and Mumbai flavour

* Illustrated, flat, friendly: the skyline sets the tone. Photos are fine for
  speakers, venue and past-event galleries; keep them warm and daylight.
* Reuse hero motifs as small decorations, not repeats of the whole scene: a marigold
  row as a section divider, a single cloud shape as a card ornament, the plane's banner
  style for an announcement strip. Ask before reusing artwork so it can be exported as
  PNG from the SVG at the right size.
* Icons: simple line or flat icons in navy or blue, 24px, consistent stroke.
  Upload as PNG (SVG is blocked) at 2× size.

## 9. Accessibility and quality bar

* AA contrast everywhere; navy on sky wash and white on blue both pass.
* One H1 on the page (the hero's logo alt text acts as the page title; use H2 for sections).
* Every interactive element: 44px minimum target, visible focus, real link text
  (no "click here").
* Check at 320px, 390px, 768px portrait, 1366px and 1920px. Nothing scrolls
  horizontally; images never exceed their column.
* Test Additional CSS survives saving: if a rule disappears after save, it used a
  stripped feature (see §2.3). Rewrite it with literal values.

## 10. Landing page sections to build (suggested order)

1. Intro / "What is WordCamp Mumbai" — two columns: text left, illustration or photo right.
2. Key facts strip — three or four info pills: date, venue, tickets, contributor day.
3. Call for speakers / sponsors — banner callout.
4. Speakers (placeholder grid until announced).
5. Schedule teaser — link to the schedule page.
6. Sponsors by tier.
7. Venue — map embed is allowed (core Embed block) plus address and travel tips.
8. Community / past WordCamps — optional gallery.
9. Final CTA — "Get tickets" primary, "Contact" secondary.

Each section: eyebrow + H2 (+ optional Kalam line), one clear action, alternate
white / sky-wash backgrounds, preset-70 padding.

## 11. Hand-off checklist for the new session

* Work only in the block editor and Additional CSS. Do not edit `hero-block.html`,
  `hero.css` or the SVGs for landing-page work; raise hero changes separately.
* Add new CSS under a fenced comment, e.g. `/* ==== LANDING: <section> ==== */`,
  after the existing sections, so it can be found and removed independently.
* Prefix new classes with `wcm-`. Never reuse a `wcm-` class the hero already uses.
* Before pasting CSS, remove every `--custom-property` and `var(--custom)`.
* After each section, load the page on a phone and tap the header menu once.
