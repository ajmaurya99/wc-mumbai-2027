# WordCamp Mumbai 2027 design system

Code-first design system for https://mumbai.wordcamp.org/2027/ (WordPress,
Twenty Twenty-Five, core blocks only, WordCamp.org sanitisers). The written
brief in `../DESIGN-SYSTEM.md` is the source of truth; everything here is
derived from it. No value in this folder was invented outside that brief;
where a choice between tokens was needed, the component's `spec.md` says so.

The hero (`../hero-block.html`, `../hero.css`, the SVGs) is a finished custom
build and is off limits. `report.py` fails anything that reuses its classes.

## Layout

```
design-system/
├── README.md                 this index
├── report.py                 the gate: grades a block.html or CSS file against the tokens
├── tokens/
│   ├── tokens.json           W3C DTCG tokens: colour, type, spacing, radius, shadow, motion
│   ├── tokens.css            the same as literal-value wcm-* classes for Additional CSS
│   └── theme-presets.md      token → Twenty Twenty-Five preset slug / class / CSS variable
├── tools/
│   ├── preview.py            block.html → preview.html, adding the classes WordPress adds at render
│   ├── render.sh             preview.html → preview-390.png and preview-1366.png (headless Chrome)
│   └── theme-shim.css        emulates the saved Styles for local previews only; never paste it
├── components/
│   ├── core/        buttons · links · section-header · info-pill
│   ├── content/     card · speaker-card · faq-details
│   └── marketing/   sponsor-tier-grid · callout-banner
├── templates/
│   └── landing-page.md       section order, backgrounds and actions, composed from the components
└── examples/
    └── why-attend/           worked example of the reference → component workflow
```

Each component folder holds:

| File | What |
|---|---|
| `block.html` | Block markup with `wp:` comments and preset slugs. Paste into a page's code editor view. |
| `preview.html` | Standalone preview built by `tools/preview.py`; open it locally. Regenerate after editing `block.html`. |
| `<name>.css` | Only where a picker cannot do it (hover, focus, transitions). Goes into Appearance → Customize → Additional CSS under its fence. |
| `spec.md` | Purpose, anatomy, variants, states, do and don't, presets used, and the `report.py` output. |
| `prompt.md` | The component in words, for regenerating or adapting it. |

Each group folder also has `preview.html` and the two rendered PNGs for the
whole group.

## Components

| Component | Folder | CSS | Report |
|---|---|---|---|
| Buttons (primary, secondary) | `components/core/buttons` | `buttons.css` | PASS |
| Links | `components/core/links` | `links.css` | PASS |
| Section header | `components/core/section-header` | none | PASS |
| Info pill | `components/core/info-pill` | none | PASS |
| Card | `components/content/card` | `card.css` | REVIEW (the allowed 4px lift; justified in spec) |
| Speaker card | `components/content/speaker-card` | reuses `card.css` | PASS |
| FAQ (Details) | `components/content/faq-details` | `faq-details.css` | PASS |
| Sponsor tier grid | `components/marketing/sponsor-tier-grid` | none | PASS |
| Callout banner | `components/marketing/callout-banner` | none | PASS |

The focus ring (2px `#6d28d9`, offset 3px) is not a separate component; it is
written into every CSS file that owns an interactive element.

## Workflow

The Claude Code skill at `../.claude/skills/wcm-design-system/SKILL.md` loads
in this repo and carries the full workflow. In short, for a new piece of work:

```sh
# 1. write design-system/components/<group>/<name>/block.html (+ <name>.css if needed)
python3 design-system/tools/preview.py design-system/components/<group>/<name>
python3 design-system/report.py design-system/components/<group>/<name>/block.html [<name>.css]
# 2. fix FAIL / STRIP / REVIEW rows, re-run until the verdict is PASS
design-system/tools/render.sh design-system/components/<group>/<name>/preview.html
# 3. look at preview-390.png and preview-1366.png, then hand over block.html (+ CSS)
```

Group preview of several components on one page:

```sh
python3 design-system/tools/preview.py --group design-system/components/core/preview.html design-system/components/core/*/
design-system/tools/render.sh design-system/components/core/preview.html
```

## Report verdicts

| Verdict | Meaning |
|---|---|
| PASS | exact token or a Twenty Twenty-Five preset reference |
| REVIEW | close to a token, or allowed only with care (festive colours, transform transitions, custom class names) |
| FAIL | off-system value, or a rule the brief forbids (negative margins, 100vw, hero classes, animations) |
| STRIP | the WordCamp sanitiser would remove it (custom properties, `will-change`, `container-*`, `<script>`, `<style>`, `<svg>`, `<input>`, `<iframe>`) |

Exit status 1 on FAIL or STRIP, so it can gate a commit hook.

## Platform constraints, in one place

No JavaScript. Custom HTML is sanitised (`wp_kses_post`). Additional CSS is
sanitised (custom properties, `will-change`, `container-*` dropped; theme
preset variables survive). SVG upload blocked. Block settings first; CSS only
for hover, focus, transitions, festive accents and equal-height rows, prefixed
`wcm-` and fenced `/* ==== LANDING: <section> ==== */`. Reload after saving
CSS and confirm it survived.

## Rendering notes

`render.sh` needs Google Chrome in `/Applications`. Headless Chrome will not
open a window narrower than 500px, so phone renders are made through a
390px iframe and cropped; `vw` units and media queries follow the iframe. Do
not add `--user-data-dir`: a fresh profile makes Chrome 153 hang on exit.
Previews load Newsreader and Kalam from Google Fonts; offline, the serif
fallback renders instead.
