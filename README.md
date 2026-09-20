# WordCamp Mumbai 2027 hero — WordPress (no unfiltered_html) setup

WordCamp.org accounts can't save `<style>`, `<link>` or inline `<svg>` in a
Custom HTML block: the content is sanitised on save. This build splits the hero
into three parts that each go where they're allowed.

## 1. Host the two SVGs (once)

This folder is the repo root of https://github.com/ajmaurya99/wc-mumbai-2027.
Once pushed, jsDelivr serves the files with the right MIME type:

* https://cdn.jsdelivr.net/gh/ajmaurya99/wc-mumbai-2027@main/mumbai-panorama.svg
* https://cdn.jsdelivr.net/gh/ajmaurya99/wc-mumbai-2027@main/plane.svg
* https://cdn.jsdelivr.net/gh/ajmaurya99/wc-mumbai-2027@main/hero.css

`hero-block.html` already points at the first two.

jsDelivr caches `@main` for up to 12 hours. After changing an SVG, either wait,
purge at https://www.jsdelivr.com/tools/purge, or reference a commit hash
instead of `@main`.

Any other static host that serves `image/svg+xml` also works (Netlify, GitHub Pages, S3).

## 2. CSS

Paste `hero.css` into **Appearance → Customize → Additional CSS**.

WordCamp.org runs Additional CSS and Remote CSS through Jetpack's CSSTidy
sanitiser, which silently drops CSS custom properties (`--x` / `var()`),
`will-change` and `container-type`. `hero.css` is written without them and
was verified against that sanitiser: every declaration survives. Keep it that
way when editing (use literal colours, not variables).
WordCamp.org also offers **Appearance → Remote CSS**, which can pull
`hero.css` straight from this GitHub repo and keep it in sync:
`https://github.com/ajmaurya99/wc-mumbai-2027/blob/main/hero.css`.

## 3. The block

Paste `hero-block.html` into a **Custom HTML** block. It contains only
`div`, `p`, `a`, `img` and `span` with class/data/style attributes, all of
which survive `wp_kses_post` (verified against WordPress core's sanitiser).

Edit in the block: the Contact link (`/2027/contact/`), date, venue, tooltip
text (`data-tip` on each hotspot).

## Notes

* The hero is full-screen (`100dvh`) and breaks out of the content column by
  itself. If you place it inside a full-width Group block, delete the two
  lines `width: 100vw; margin-left: calc(50% - 50vw);` from `#wcm-hero`.
* Figtree loads only if the theme already has it; otherwise the system font
  is used. Google Fonts `<link>` tags are stripped by the sanitiser.
* Inside an `<img>` the SVG's own animations (train, bus, taxi, ferry, waves)
  still run, but nothing inside it can be hovered. Hover tooltips are
  therefore HTML hotspots layered over the image; they cover the fixed
  landmarks and props, not the moving vehicles.

## Diya cursor + flower shower (pandal hover)

Added in one commit on top of the tag `before-diya`. To remove it:

* CSS: delete everything between `/* ==== DIYA + FLOWER SHOWER: start ==== */`
  and `/* ==== end ==== */` in Additional CSS.
* Block: restore the pandal hotspot to its original single line:
  `<span class="wcm-spot" data-tip="Ganpati Bappa Morya!" style="…"></span>`
  (drop the `wcm-spot--pandal` class and the fourteen `<i class="wcm-petal …">` children).
* Or in git: `git revert <commit>` / `git checkout before-diya -- hero.css hero-block.html`.
* `diya-cursor.png` can stay or go; nothing else references it.

## Hero navigation (the theme header, floated over the hero)

On the home page only (`body.home`), the `HERO NAV` section of `hero.css` takes the
site's normal Header template part and:

* floats it over the top of the hero with no background or shadow,
* hides its logo and date/venue (the hero already shows them),
* centres the Navigation block on desktop and puts the hamburger top-right on phones,
* restyles the dropdowns and core's mobile overlay to match the hero.

Editor setup: add the **Header** (and Footer) template parts to the home page
template. Nothing else: no extra Navigation block, no CSS classes. Menu items and
sub-items are managed in the header's Navigation block, once, for the whole site.

Rules to keep:

* Never animate `transform` on the header or nav. Core's mobile overlay is
  `position: fixed` and a transformed ancestor would trap it inside the header.
* The header's outer Group has padding and a shadow set in its block settings
  (inline styles), so the home overrides for those need `!important`.
* The overlay rules use long selectors and `!important` on two colours on purpose:
  core sets those with CSS variables, which WordCamp's sanitiser strips from our file.
* If the header's structure changes (for example the logo group is moved), recheck
  the `display: none` rule that hides the logo group.

Rollback: `git checkout before-core-nav -- hero.css hero-block.html` restores the
hand-built About / Venue / Contact links inside the block.
