# Reference: four WordCamp 2026 home pages

Captured 27 Sep 2026 at 1459px wide. Section order, backgrounds and patterns
per site, then the patterns that recur and how each maps to our components.
Colours and fonts here are the reference sites' own; ours stay as in
DESIGN-SYSTEM.md.

## Delhi · https://delhi.wordcamp.org/2026/

Poppins body, Yatra One display headings. Cream and navy. Two tones of cream
alternate; navy for the schedule band. ~6,250px tall.

| # | Section | Background | Pattern |
|---|---|---|---|
| 1 | Hero | cream, illustrated skyline at the foot, birds | Stacked title, two fact pills (date, venue) with icons, tagline, two buttons |
| 2 | Marquee strip | navy | Scrolling text ticker of topics (JavaScript; not possible for us) |
| 3 | Stats row | light cream | Four big numbers with labels (20+ speakers, 2 days, 500+ attendees, 20+ sponsors) |
| 4 | About | cream | Two columns: heading + three paragraphs + button left, group photo right |
| 5 | Schedule at a glance | navy | Two columns, one per day, time + title + room rows, one button |
| 6 | Speakers | light cream | Four-up cards, name + role, mostly "To be announced", outline button "Apply to become speaker" |
| 7 | Sponsors | cream | Heading, tier pill "Platinum Sponsors", four logo cards with thin border, two buttons |
| 8 | Latest updates | light cream | Three post cards with "Read more" links, one button |
| 9 | When and where | light cream | Fact cards left (date, venue, address), embedded map right |
| 10 | Footer | navy | Newsletter subscribe, links |

## Kathmandu · https://kathmandu.wordcamp.org/2026/

Bricolage Grotesque body, **Kalam for headings** (the only site using our
accent font, and it uses it everywhere). White, warm off-white cards, an
orange accent. Very long page (~11,000px).

| # | Section | Background | Pattern |
|---|---|---|---|
| 1 | Hero | white, brown skyline silhouette and mandala corners | Two-tone title, Kalam tagline, four-column fact row (contributor day, conference day, venue, hashtag), two buttons |
| 2 | Why attend | white | Four cards: Learn & Grow, Connect, Contribute, Explore; title + paragraph, no icons |
| 3 | Culture mural | white | Full-width illustrated photo with orange frame |
| 4 | Ways to take part | cream cards | Two wide cards: Sponsor, Attendee, each with a button |
| 5 | Programme | white | Eyebrow "PROGRAMME", H2 "Two Days. Two Stages.", two large day cards |
| 6 | Speakers | pale peach | Four-up circular photos with flag badges, name, talk title, topic chips; very long |
| 7 | Contributor Day | white | Team grid, eleven images |
| 8 | Sponsors | patterned background | Logo grid, "View All Sponsors" |
| 9 | Latest news | white | Three post cards with date |
| 10 | Newsletter | pale peach | "Stay informed", one button |

## Bengaluru · https://bengaluru.wordcamp.org/2026/

Hanken Grotesk body, Fraunces serif headings, monospace "// section_name"
eyebrows and a fake terminal strip at the top. Warm beige ground, dark red
accents, botanical line illustrations in the margins. ~7,700px.

| # | Section | Background | Pattern |
|---|---|---|---|
| 1 | Hero | beige, big "6" watermark | Two columns: huge serif title left; right, a "ticket" card listing the two days with badges, two stacked buttons and "how the two days work" notes |
| 2 | Ticker | dark red | Repeating text strip (JavaScript) |
| 3 | About | beige | Two columns: story left with two links, photo right; facts table under it (weekend, room, run by) |
| 4 | By the numbers | beige | Four stat cards (400+, 20+, 2, 1) with label and one line |
| 5 | CTA strip | dark red | Single-row banner: heading + line left, button right |
| 6 | Get involved | beige | Five numbered cards: Speak (closed), Sponsor, Media partner (closed), Volunteer, Lead a table; each with deadline and link; a lotus divider under it |
| 7 | Sponsors | beige | Eyebrow, H2 "Proudly supported by", logo grid, "View packages" |
| 8 | Venue | lighter beige | Two columns: address facts and getting-there left, embedded map right, two direction buttons |
| 9 | Stay in the loop | beige | Post cards |
| 10 | Newsletter | beige | Subscribe form |

## Rajasthan · https://rajasthan.wordcamp.org/2026/

Poppins body, **Newsreader headings** (same heading font as ours), with an
italic terracotta word inside each H2. Off-white and deep maroon bands
alternate. Woven textile strip between hero and content. ~9,250px. Page
uses a smooth-scroll script.

| # | Section | Background | Pattern |
|---|---|---|---|
| 1 | Hero | off-white, photo of the venue right | Devanagari eyebrow, H1 with italic second line, paragraph, two buttons, date and venue facts under a rule |
| 2 | Textile divider | pattern | Decorative strip |
| 3 | The event | off-white | Eyebrow + H2 left, two stat cards right (600+, 15+, 2 days) |
| 4 | Four reasons | maroon | Four numbered cards (01 to 04), title + paragraph, faint building watermark |
| 5 | Who you'll meet | off-white | Five small persona cards, then a maroon single-row banner with button "See who's coming" |
| 6 | Speakers | maroon | Three-up cards: round photo, name, role in accent, one line, "INTERNATIONAL" badge; two buttons under |
| 7 | Conversations | off-white | Chip cloud of talk topics, some filled, some outlined |
| 8 | Venue | off-white | H2, paragraph, four photo tiles with captions, two buttons |
| 9 | Community power | off-white | H2, three stats in a row with rules, three group photos |
| 10 | Cities | maroon | Cities list and a button |
| 11 | Sponsors | off-white | Logo grid, two buttons |

## What recurs across all four

| Pattern | Seen on | Our component | Gap |
|---|---|---|---|
| Fact pills or fact row under the hero (date, venue, hashtag) | all four | Info pill | none |
| Stats row: 3 or 4 big numbers with a label | Delhi, Bengaluru, Rajasthan | none | **new: stat tile** (number xx-large in Accent 1, label small Accent 4) |
| "Why attend" / "Four reasons" numbered feature cards | Kathmandu, Rajasthan | Card, no-link variant (`examples/why-attend`) | optional "01" numeral eyebrow |
| About in two columns, text + photo | Delhi, Bengaluru | Section header (left) + Columns + Image | landing template section 1 |
| Ways to take part: Speak, Sponsor, Volunteer cards with deadline and status | Bengaluru, Kathmandu | Card + Info pill for the deadline | a "closed" badge could be a festive chip |
| Speakers grid: photo, name, role, sometimes a badge or chips | all four | Speaker card | round photo variant would need a value (we use 16px radius) |
| Sponsors by tier, logos in bordered or white boxes | all four | Sponsor tier grid | none |
| Single-row CTA strip: heading left, button right | Bengaluru, Rajasthan | Callout banner (left-aligned variant) | none |
| Venue: facts left, map right | Delhi, Bengaluru | Columns + Embed + Info pill | landing template section 7 |
| Latest news: three post cards | Delhi, Kathmandu, Bengaluru | Card, or the Query Loop block | Query Loop keeps it automatic |
| Newsletter block | Delhi, Kathmandu, Bengaluru | none | WordCamp.org has no newsletter form without Jetpack; skip or link out |
| Scrolling text ticker | Delhi, Bengaluru | none | JavaScript; not possible. A static Info pill row is the equivalent |
| Topic chip cloud | Rajasthan | Info pill with radius 8px (chip) | none |
| Decorative divider strip between sections | Rajasthan, Bengaluru | none | festive colours are allowed for dividers; a 2× PNG strip would work |
| Alternating light and dark bands | Delhi, Rajasthan | our system alternates white and sky wash only | a Contrast (navy) band is in the palette but the brief says page ground is white; ask before using dark bands |

## Notes for our home page

* Every site puts date, venue and the ticket button in the first screen.
  Our hero already does that; the pills under it are then for the second
  screen (contributor day, tickets price, hashtag).
* Three of four open with a stats row or fact row right after the hero.
* "Why attend" style cards appear early, before speakers.
* Speakers, sponsors and venue always come in that order in the lower half.
* Kathmandu is the closest to our type system (Kalam), Rajasthan to our
  heading font (Newsreader). Neither uses a serif for body; we do.
