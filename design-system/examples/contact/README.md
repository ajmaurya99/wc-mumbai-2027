# Contact page: handover

Built 3 Oct 2026 from bengaluru.wordcamp.org/2026/contact, core blocks plus the
site's own Jetpack Form block. Live on page 18 (`/contact/`, template "Page,
no title (header and footer)") since 3 Oct; the previous version is in the
page's revisions.

```sh
python3 design-system/examples/contact/build.py
python3 design-system/tools/preview.py design-system/examples/contact
python3 design-system/report.py design-system/examples/contact/block.html
design-system/tools/render.sh design-system/examples/contact/preview.html
```

| # | Section | Background |
|---|---|---|
| 1 | Intro: eyebrow, H1 "Contact Us" (the page title), Kalam "Namaskar! Say hello", one line | white, gateway motif |
| 2 | Two cards: "Send us a message" with the Jetpack Form (name, email, message; sends to mumbai@wordcamp.org, subject "WordCamp Contact Request"; button on Accent 1, pill) · "Other ways to reach us": email, Facebook, X, LinkedIn, Instagram as label + link, then the Social Links icons | sky wash, lattice |
| 3 | Separator: cutting chai | |
| 4 | Quick links: Sponsoring → call for sponsors · Getting there → venue · The team → organizers | white, palm motif |

The form block is the one the page already had (same `to` and subject), so
Jetpack keeps the same responses list. Previews show a static stand-in for it.
The "Venue" quick link points at `/2027/venue/`, which is a draft until
published.

Links used: facebook.com/WPMumbai.org, x.com/wcmumbai,
linkedin.com/company/wpmumbai, instagram.com/wpmumbai, mumbai@wordcamp.org.

Report: `report.md`, PASS.
