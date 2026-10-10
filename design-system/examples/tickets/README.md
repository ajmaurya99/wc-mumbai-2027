# Tickets page: handover

Built 10 Oct 2026 from the Delhi and Bengaluru 2026 tickets pages and the early
bird announcement copy, core blocks only. Lives on **page 14** (the site's
default Tickets page, which held only the `[camptix]` shortcode), titled Tickets,
slug `tickets`, template "Page, no title (header and footer)". **Published on
10 Oct 2026 with the password `WCMumbaiOnly`** so the team can review the
on-sale state before Sunday; remove the password (Visibility → Public) to go
live.

`build.py` has two states, switched by `ON_SALE` at the top:

* `ON_SALE = False`: the countdown page, with an on-sale notice card
  (`wcm-ticket-slot`) in the widget's place.
* `ON_SALE = True` (what is on the site): the `[camptix]` shortcode inside a
  Base card (`wcm-tix`), live wording, the early bird price (`EARLY_BIRD_PRICE`,
  ₹650) in a fact card and the FAQ. The preview and the gate get a static
  stand-in table through the `ds:site-only` / `ds:preview-only` markers.

```sh
python3 design-system/examples/tickets/build.py
python3 design-system/tools/preview.py design-system/examples/tickets
python3 design-system/report.py design-system/examples/tickets/block.html
design-system/tools/render.sh design-system/examples/tickets/preview.html
```

| # | Section | Background | Action |
|---|---|---|---|
| 1 | Intro, two columns: eyebrow, H1 "Tickets", Kalam "Early bird tickets go on sale soon", two paragraphs, buttons · past-WordCamp speaker photo (attachment 1200, 4:3) · three fact cards (date, venue, early bird ₹650) | white, gateway motif | primary "Get updates" (news), outline "Explore the venue" |
| 2 | Separator: vada pav | | |
| 3 | Choose your pass (`#tickets`): section header · the CampTix widget in a Base card (`wcm-tix`) · one meta line. Before `ON_SALE`: a notice card with the "Coming soon" chip and the WordPress.org-account note instead | sky wash, lattice | CampTix "Register →" |
| 4 | Why grab your ticket early: three numbered cards (best price, guaranteed seat, first to know) | white, palm motif | |
| 5 | What's included: four cards (conference access, lunch chai and snacks, badge and swag, the community) | sky wash, lattice | |
| 6 | Before you buy: intro beside six Details (on-sale date, price, WordPress.org account, payment, transfer or refund, on the day) | white, blue lattice | |
| 7 | Save the date: gradient band | gradient (the one per page) | Base "Get updates", outline "Contact us" |

## CampTix on the page (`tickets.css`, fence `LANDING: tickets`)

CampTix brings its own markup and a thin stylesheet. The fence restyles it
with the system's tokens: the ticket table (uppercase Accent 2 column heads,
large bold ticket title, 44px select), inputs as filled Accent 5 fields with
an Accent 1 focus border, the submit as the primary button, notices as
left-edged Accent 5 cards, and a phone layout where the attendee form stacks
label over field. On the checkout steps (`?tix_action=attendee_info`,
payment, receipt, edit) CampTix replaces the whole page content with `#tix`,
so `.entry-content > #tix` gives those steps an 800px frame and page padding.

Live in Appearance → Customize → Additional CSS since 10 Oct 2026 (added
through the Customizer; every declaration survived the sanitiser, including
`accent-color`, `:focus-visible` and the media queries).

## Going live on 11 October 2026, 12:00 PM IST

1. Tickets → Setup → Payment: take CampTix out of **sandbox mode**.
2. Page 14: Visibility → Public (drop the password), Update.
3. Do not change the slug after sales start: receipt emails link to it.
4. Refund terms: the "Can I transfer my ticket" FAQ still says they will be
   published; replace that line once the policy is decided.

## The Early Bird ticket (CampTix ticket 1314, published)

₹650, quantity 50, no start or end date. Custom questions, in order after
name and email: WordPress.org Profile (text) · X/Twitter Handle (username
only, without the @ or a link) (Twitter) · LinkedIn (URL) · Your Website (URL)
· How would you describe yourself? (checkbox, 12 options). WordCamp.org adds
its own fixed questions after them, including "Will this be your first time
attending a WordPress event?", so the custom copy of that question that was
added on 10 Oct was removed again the same day.

## Notes

* Besides `tickets.css` the page uses the live buttons, links, cards, fact
  cards and chips, separators, faq, bands and sponsors fences (the last one
  clears the `<mark>` background on the numbered cards).
* `wcm-ticket-slot` (countdown state) and `wcm-tix` (on-sale state) are
  markers; only `wcm-tix` has CSS.
* `report.md`: the block markup passes; `tickets.css` has REVIEW rows only,
  all for CampTix's own `.tix-*` class names (third-party markup, cannot be
  prefixed) and one `#E0552D` saffron left edge on error notices (a divider
  use, allowed by the brief).
* `tools/blocks.py`: `chip()` gained a `bg` argument (the chip sits on a Base
  card here, so it is Accent 5).
* The draft " Early Bird Ticket" (page 1287) is a teammate's; it was not
  touched.

Report: `report.md`, block.html PASS; tickets.css REVIEW (see Notes).
