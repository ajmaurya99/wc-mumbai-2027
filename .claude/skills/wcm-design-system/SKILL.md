---
name: wcm-design-system
description: WordCamp Mumbai 2027 design system. Use for any request to build, adapt or review a component, section or page for mumbai.wordcamp.org/2027 (WordPress Twenty Twenty-Five, core blocks only) from a screenshot, URL or description. Covers tokens, component library, platform constraints, the report.py gate and the reference-to-block-markup workflow.
---

# WordCamp Mumbai 2027 design system

You are producing on-brand WordPress block markup (plus CSS only when a block
picker cannot do the job) for https://mumbai.wordcamp.org/2027/. The system is
code-first and lives in `design-system/`. Read this file, then the index at
`design-system/README.md`, before touching anything.

## Where things live

| What | Path |
|---|---|
| Source of truth (palette, type, spacing, components, motion, constraints) | `DESIGN-SYSTEM.md` |
| Tokens, W3C DTCG | `design-system/tokens/tokens.json` |
| Tokens as literal-value CSS classes (`wcm-*`) | `design-system/tokens/tokens.css` |
| Token → Twenty Twenty-Five preset slug map | `design-system/tokens/theme-presets.md` |
| Components (`block.html`, `preview.html`, `spec.md`, `prompt.md`, optional `<name>.css`) | `design-system/components/<core|content|marketing>/<name>/` |
| Landing page composition | `design-system/templates/landing-page.md` |
| Gate script | `design-system/report.py` |
| Preview builder (block.html → preview.html) | `design-system/tools/preview.py` |
| Headless Chrome renderer (390px and 1366px) | `design-system/tools/render.sh` |
| Theme emulation for local previews only | `design-system/tools/theme-shim.css` |
| Worked example of the full loop | `design-system/examples/why-attend/` |
| The home page (generator, sections, handover) | `design-system/examples/home/` |
| Artwork: SVG sources and PNG at 2× | `design-system/assets/` (rasterise with `tools/rasterise.py`) |
| Reference analysis of other WordCamp sites | `design-system/references/` |

## Off limits

* `hero-block.html`, `hero.css`, `mumbai-panorama.svg`, `plane.svg`,
  `diya-cursor.png`: the hero is a finished custom build. Never edit, restyle
  or reuse its classes (`wcm-hero`, `wcm-spot`, `wcm-cloud`, …). `report.py`
  fails any file that references a hero class.
* No new colours, fonts or size steps. If the reference needs a value that is
  not in `DESIGN-SYSTEM.md`, ask before inventing it. Choosing between existing
  tokens is fine; state the choice in `spec.md`.

## Platform constraints (WordCamp.org, enforced, not preferences)

1. No JavaScript. `<script>` is stripped. Only core-block behaviour (Details,
   Navigation overlay, Embed) and CSS hover/focus.
2. Custom HTML blocks are sanitised through `wp_kses_post`: no `<style>`,
   `<svg>`, `<input>`, `<iframe>`, `<form>`. Build with core blocks; Custom HTML
   is a last resort.
3. Additional CSS goes through Jetpack CSSTidy: custom property definitions
   (`--x:`), `var(--x)` for anything but `--wp--preset--*`, `will-change` and
   `container-*` are silently dropped. Write literal values.
4. SVG upload is blocked. Raster at 2× (PNG/WebP).
5. Block settings first (colour, spacing, typography pickers). CSS only for
   hover, focus, transitions, festive accents, equal-height logo rows.
   Prefix classes `wcm-`; fence with `/* ==== LANDING: <section> ==== */`.

## Rules for every handover

* Run `python3 design-system/report.py <block.html> [<name>.css]` before
  handing anything over. Fix every FAIL and STRIP row. Resolve every REVIEW
  row, either by changing the value or by writing one line in `spec.md`
  explaining why it stays. Paste the final report table into `spec.md`.
* Render `preview.html` at 390px and 1366px with `render.sh` and look at both
  PNGs yourself before showing them. Check: no horizontal scroll, three
  columns → one column on the phone, text on colour is white, headings start
  at H2 inside a page.
* Alternate white and sky-wash (`accent-5`) section backgrounds. One primary
  blue button per section. Text on blue, teal or purple is Base. Bands: at
  most one dark (Contrast) band per screen and one gradient band per page
  (DESIGN-SYSTEM.md §2). Section backgrounds may carry one tile or one corner
  motif from `assets/png` via the Group's Background control.
* Artwork: no SVG on the site. Draw in `assets/svg`, run `rasterise.py`, commit
  the PNG, reference it by its jsDelivr URL
  (`https://cdn.jsdelivr.net/gh/ajmaurya99/wc-mumbai-2027@main/design-system/assets/png/<name>@2x.png`);
  previews rewrite that prefix to the local file.
* Dynamic blocks (Query Loop, Jetpack Subscriptions, Navigation, Social Links)
  render nothing in previews: wrap the real block in `<!-- ds:site-only -->`
  and a static stand-in in `<!-- ds:preview-only -->`; `preview.py --site`
  prints the paste-ready form.
* Section = Group, Full width, constrained layout, padding preset 70 top and
  bottom, background from the colour picker. Title-to-content gap preset 40;
  between cards preset 30. Grids = Columns 3/2/1, Stack on mobile on.

## Workflow for a reference request (screenshot, URL or description)

a. **Map it.** Read the reference. List which existing components it maps to
   (name each folder) and what, if anything, is new. Note any value that is
   not in the system; that is a question for the user, not a guess.
b. **Propose in words.** Describe the block tree top-down (section group →
   header → columns → cards …), the background rhythm, the one action, and
   which presets each part uses. Wait for the user's go-ahead before building.
c. **Build.** Create `design-system/components/<group>/<name>/` (or
   `design-system/examples/<name>/` for a one-off section) with `block.html`
   and, only if a picker cannot do it, `<name>.css`. Then:
   ```sh
   python3 design-system/tools/preview.py design-system/components/<group>/<name>
   python3 design-system/report.py design-system/components/<group>/<name>/block.html [<name>.css]
   ```
   Fix REVIEW and FAIL rows, re-run until the verdict line reads PASS (or
   REVIEW with each row justified in `spec.md`).
d. **Render.**
   ```sh
   design-system/tools/render.sh design-system/components/<group>/<name>/preview.html
   ```
   produces `preview-390.png` and `preview-1366.png` next to the preview.
   Open both with the Read tool, check them, then show the user the paths.
e. **Hand over.** Give the paste-ready `block.html` contents in a fenced
   `html` block (it goes into the page's code editor view, Options → Code
   editor). Only if a CSS file exists, add a second fenced `css` block headed
   "Appearance → Customize → Additional CSS", including its
   `/* ==== LANDING: … ==== */` fence. Tell the user what to edit after
   pasting (text, links, image IDs). Write `spec.md` and `prompt.md` for
   anything that becomes a reusable component.

## Writing block markup

* Use preset slugs in the block JSON, never literal values for colour, size or
  spacing: `"backgroundColor":"accent-5"`, `"fontSize":"small"`,
  `"var:preset|spacing|40"`. The matching classes and inline styles must
  appear in the HTML exactly as WordPress would save them; see
  `design-system/tokens/theme-presets.md` and copy patterns from an existing
  `block.html`.
* `blockGap` lives only in the JSON; WordPress emits it at render time.
  `preview.py` reproduces that, so do not add gap CSS.
* Placeholder images: `https://placehold.co/…` is fine for previews; say
  where the real image goes.
* One H1 per page; components start at H2 (H3 inside cards).
* Every link has real text; every interactive element is at least 44px tall.

## Commits

One conventional commit per component group or example, for example
`feat(ds): add content components (card, speaker-card, faq-details)`.
Never commit changes to the hero files.
