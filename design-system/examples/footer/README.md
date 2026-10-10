# Footer: handover

Built 11 Oct 2026 after the WordCamp Bengaluru 2026 footer, core blocks only,
and written to the **Footer template part** through the REST API the same day
(the previous footer is in the template part's revisions). The three menus
are Navigation posts created for it:

| Menu | Post | Items |
|---|---|---|
| Footer: Event | 1353 | About · News · Organizers · Code of Conduct |
| Footer: Get Involved | 1354 | Call for Sponsors (`wcm-nav-open`) · Call for Speakers (`wcm-nav-open`) · Tickets |
| Footer: Community | 1355 | Mumbai Meetup (meetup.com/wordpress-mumbai, opens in a new tab) · Contact |

```sh
python3 design-system/examples/footer/build.py
python3 design-system/tools/preview.py design-system/examples/footer
python3 design-system/report.py design-system/examples/footer/block.html design-system/examples/footer/footer.css
design-system/tools/render.sh design-system/examples/footer/preview.html
```

| # | Row | What |
|---|---|---|
| 1 | Columns 37 / 21 / 21 / 21 | brand lockup (Site Logo 64px, name, Kalam tagline), one-line blurb, venue link · Event menu · Get Involved menu · Community menu + "Write to us" email |
| 2 | Rule | wide Separator, Accent 5 |
| 3 | Follow and subscribe | "Follow" + Social Links (X, Instagram, LinkedIn, Facebook, the site's accounts) · "Get updates in your inbox" + Jetpack Subscriptions |
| 4 | Credit | "© 2027 WordCamp Mumbai · Organised by the Mumbai WordPress community" · Code of Conduct · Proudly powered by WordPress |

White background (the pages above it end on a tinted or gradient band), Base
text, Accent 2 eyebrows. The Navigation blocks render nothing in previews, so
`block.html` carries static stand-ins behind the `ds:` markers; `preview.py
--site` strips them.

## CSS (`footer.css`, fence `LANDING: footer`)

Column dividers (2px Accent 5), quiet menu links that turn Accent 1 and
underline on hover, the focus ring, the inline subscribe form, and the
**"Open" label**: a Navigation link with the class `wcm-nav-open` gets an
uppercase Accent 2 pill after its text through `::after`, pulsing in opacity
every 2.4s. That pulse is the one looping animation outside the hero, asked
for explicitly on 11 Oct 2026; `report.py` flags it as the single FAIL row and
it stops under `prefers-reduced-motion`. To mark a call closed, remove the
class from its menu item (Appearance → Editor → Navigation → the menu → the
item → Advanced → Additional CSS class). Live in Additional CSS since 11 Oct.

## To check or change

* The Mumbai Meetup URL (`https://www.meetup.com/wordpress-mumbai/`) could not
  be verified from here; confirm it opens the right group.
* The closing call-to-action row ("Come spend a day with us." with two
  buttons) was built and then removed the same day at the user's request;
  `cta` still exists in `build.py` if it is wanted back.
* The subscribe form is Jetpack Subscriptions, as on the News page.

Report: `report.md`, block.html PASS; footer.css one FAIL (the pulse, see above).
