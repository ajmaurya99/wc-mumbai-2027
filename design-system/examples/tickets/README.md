# Tickets page: handover

Built 10 Oct 2026 from the Delhi and Bengaluru 2026 tickets pages and the early
bird announcement copy, core blocks only. Pasted into **page 14** (the site's
default Tickets page, which held only the `[camptix]` shortcode), now titled
Tickets with the slug `tickets`, template "Page, no title (header and footer)",
still a **draft**. Tickets are not on sale yet (CampTix has no ticket types and
renders "Sorry, but there are currently no tickets for sale"), so section 3
reserves the widget's place with an on-sale notice.

```sh
python3 design-system/examples/tickets/build.py
python3 design-system/tools/preview.py design-system/examples/tickets
python3 design-system/report.py design-system/examples/tickets/block.html
design-system/tools/render.sh design-system/examples/tickets/preview.html
```

| # | Section | Background | Action |
|---|---|---|---|
| 1 | Intro, two columns: eyebrow, H1 "Tickets", Kalam "Early bird tickets go on sale soon", two paragraphs, buttons · past-WordCamp speaker photo (attachment 1200, 4:3) · four fact cards (date, venue, tickets on sale 11 October 2026, early bird limited seats) | white, gateway motif | primary "Get updates" (news), outline "Explore the venue" |
| 2 | Separator: vada pav | | |
| 3 | Choose your pass (`#tickets`): section header · **the widget slot**: a Base card with the "Coming soon" chip, "Ticket sales open on 11 October 2026 at 12:00 PM IST", the WordPress.org-account note and buttons · one meta line | sky wash, lattice | primary "Create a WordPress.org account", outline "Get updates" |
| 4 | Why grab your ticket early: three numbered cards (best price, guaranteed seat, first to know) | white, palm motif | |
| 5 | What's included: four cards (conference access, lunch chai and snacks, badge and swag, the community) | sky wash, lattice | |
| 6 | Before you buy: intro beside six Details (on-sale date, price, WordPress.org account, payment, transfer or refund, on the day) | white, blue lattice | |
| 7 | Save the date: gradient band | gradient (the one per page) | Base "Get updates", outline "Contact us" |

## When tickets go on sale (11 October 2026, 12:00 PM IST)

1. Create the ticket types in Tickets → Tickets (CampTix) first.
2. In page 14's code editor, replace the `wcm-ticket-slot` Group (the card in
   section 3, from `<!-- wp:group {"className":"wcm-ticket-slot"` to its
   `<!-- /wp:group -->`) with the contents of `camptix-widget.html`
   (`[camptix]` in a Shortcode block). Keep the section header above it.
3. Update the copy that says "on sale soon": the intro tagline and first
   paragraph, the "Tickets on sale" fact card, the "Coming soon" tone, the
   section 3 tagline and the first two FAQs. Add the prices to "How much does
   a ticket cost?" and the refund terms to "Can I transfer my ticket".
4. Do not change the slug after sales start: receipt emails link to it.

`build.py` has `SALE_DATE` and `SALE_TIME` at the top if the date moves.

## Notes

* Nothing new in the CSS: the page uses the live buttons, links, cards, fact
  cards and chips, separators, faq, bands and sponsors fences (the last one
  clears the `<mark>` background on the numbered cards).
* `wcm-ticket-slot` is a plain class name with no CSS; it marks the card to
  swap.
* `tools/blocks.py`: `chip()` gained a `bg` argument (the chip sits on a Base
  card here, so it is Accent 5).
* The draft " Early Bird Ticket" (page 1287) is a teammate's; it was not
  touched.

Report: `report.md`, PASS (53 PASS, 0 REVIEW, 0 FAIL, 0 STRIP).
