# Landing page template

Section order from DESIGN-SYSTEM.md §9, composed from the component library.
Backgrounds alternate white and sky wash (`accent-5`); each section has one
clear action. The hero above section 1 is the finished custom build and is
not part of this composition.

Every section is the same shell:

```html
<!-- wp:group {"align":"full","backgroundColor":"<base|accent-5>","style":{"spacing":{"padding":{"top":"var:preset|spacing|70","bottom":"var:preset|spacing|70"},"blockGap":"var:preset|spacing|40"}},"layout":{"type":"constrained"}} -->
<div class="wp-block-group alignfull has-<base|accent-5>-background-color has-background" style="padding-top:var(--wp--preset--spacing--70);padding-bottom:var(--wp--preset--spacing--70)">
  … section header … content … one action …
</div>
<!-- /wp:group -->
```

The `blockGap` of 40 on the shell is the "title to content" gap; components
inside bring their own internal gaps (30 between cards, 20 inside a header).

| # | Section | Background | Components | Action | Notes |
|---|---|---|---|---|---|
| 1 | Intro | white | Section header (left-aligned, with Kalam tagline) + Paragraph, in Columns 2 with an Image (16:10, radius 16px) on the right | Link: "About WordCamp Mumbai" | Left column text, right column image; on phones the image stacks below. Heading is the page's first H2. |
| 2 | Key facts | sky wash | Info pill ×4 (date, venue, tickets, contributor day); pills use `base` background on this section | Primary button "Get tickets" | No header needed; the pills are the content. This is the section's one primary button. |
| 3 | Callout | white | Callout banner set to `base` | Primary "Apply to speak" (or "Become a sponsor" once the CfS closes) | The component ships sky wash; flip to white here to keep the rhythm. |
| 4 | Speakers | sky wash | Section header (centred) + Speaker card ×3 (cards on `base`) | Link under the grid: "All speakers" | Until announced: one placeholder card and the eyebrow "Speakers announced in January". |
| 5 | Schedule teaser | white | Section header (left) + Card ×3 (tracks / Contributor Day / after party) | Link in each card, plus one primary button "See the full schedule" | Cards on `accent-5`. |
| 6 | Sponsors | sky wash | Section header (centred) + Sponsor tier grid (logos in `base` boxes) | Secondary button "Sponsorship deck" + link "Become a sponsor" | No primary here; the callout in 3 already asks. |
| 7 | Venue | white | Section header (left) + Columns 2: Embed (map) left, Paragraphs + Info pills (address, nearest station) right | Link: "Travel and stay" | Embed block only; no iframe in Custom HTML. Map gets `radius 16px` via a `base` Group wrapper. |
| 8 | Community (optional) | sky wash | Section header (centred) + Gallery block (radius 16px, 3 columns) | Link: "Past WordCamps" | Drop if there are no photos yet; then 9 becomes sky wash. |
| 9 | Final CTA | white (sky wash if 8 is dropped) | Callout banner: H2 "See you in Mumbai", Buttons with primary "Get tickets" and secondary "Contact" | Primary "Get tickets" | The only section with two buttons. |

## Rhythm check

```
hero → 1 white → 2 sky → 3 white → 4 sky → 5 white → 6 sky → 7 white → 8 sky → 9 white
```

If a section is removed, flip the backgrounds of everything below it so no two
neighbours share a background.

## Assembly

1. Open the page, Options → Code editor.
2. Paste each section shell in order, then paste the component `block.html`
   contents inside it, replacing the placeholder text and image URLs.
3. Switch back to the visual editor; every block should show its preset
   colours and spacing with no "invalid block" notices.
4. Paste the CSS files that the components you used need into
   Appearance → Customize → Additional CSS, each under its own fence:
   `buttons.css`, `links.css`, `card.css`, `faq-details.css`. Reload and
   confirm the rules survived.
5. Run the quality bar from DESIGN-SYSTEM.md §8: 320, 390, 768, 1366, 1920,
   no horizontal scroll, one H1, header menu opens on a phone.
