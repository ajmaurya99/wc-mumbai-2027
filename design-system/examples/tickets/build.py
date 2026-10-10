#!/usr/bin/env python3
"""Generate the Tickets page for WordCamp Mumbai 2027 as core-block markup.

Writes sections/NN-name.html and block.html (paste into the Tickets page's code
editor, page 14). Tickets are not on sale yet: section 3 holds the place of the
CampTix widget with an "on sale from 11 October 2026, 12:00 PM IST" card; see
camptix-widget.html and README.md for the swap. Helpers live in
design-system/tools/blocks.py. Run: python3 design-system/examples/tickets/build.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(HERE)), "tools"))
from blocks import *  # noqa: E402,F401

FILES = "https://mumbai.wordcamp.org/2027/files/"
PHOTO = FILES + "2026/10/75513602_2576447042392986_7977319273150283776_n-1024x683.jpg"
REGISTER = "https://login.wordpress.org/register"
EVENT_DATE = "13 February 2027"
SALE_DATE = "Sunday, 11 October 2026"
SALE_TIME = "12:00 PM IST"
ON_SALE = True          # False: the "on sale soon" page; True: the CampTix widget and live wording
EARLY_BIRD_PRICE = "₹650"


def tagline(text, align="left"):
    al = '"align":"%s",' % align if align != "left" else ""
    cls = "has-text-align-%s " % align if align != "left" else ""
    return ('<!-- wp:paragraph {%s"textColor":"accent-2","fontSize":"large","fontFamily":"kalam"} -->\n'
            '<p class="%shas-accent-2-color has-text-color has-large-font-size has-kalam-font-family">%s</p>\n<!-- /wp:paragraph -->' % (al, cls, text))


def details(q, paras):
    body = "\n\n".join(para(p) for p in paras)
    return ('<!-- wp:details {"className":"wcm-faq","style":{"border":{"radius":"16px"},"spacing":{"padding":{"top":"var:preset|spacing|40","bottom":"var:preset|spacing|40","left":"var:preset|spacing|40","right":"var:preset|spacing|40"}}},"backgroundColor":"accent-5"} -->\n'
            '<details class="wp-block-details wcm-faq has-accent-5-background-color has-background" style="border-radius:16px;padding-top:var(--wp--preset--spacing--40);padding-right:var(--wp--preset--spacing--40);padding-bottom:var(--wp--preset--spacing--40);padding-left:var(--wp--preset--spacing--40)"><summary>%s</summary>%s</details>\n<!-- /wp:details -->'
            % (q, body))


def point(n, title, text, bg="accent-5"):
    h3 = '<mark class="has-inline-color has-accent-1-color">%s</mark> %s' % (n, title)
    return column(group("\n\n".join([heading(h3, 3, "large"), para(text)]), bg=bg, radius="16px",
                        padding=(40, 40, 40, 40), gap=20, cls="wcm-card wcm-why", border_left=("accent-2", "4px")))


def included(title, text):
    return column(card([heading(title, 3, "large"), para(text)], bg="base", gap=20))


sections = []

# 1. intro -------------------------------------------------------------------
intro_left = "\n\n".join([
    group("\n\n".join([
        eyebrow("WordCamp Mumbai 2027 · %s" % EVENT_DATE),
        heading("Tickets", 1, "xx-large"),
        tagline("Early bird tickets are on sale now" if ON_SALE else "Early bird tickets go on sale soon"),
    ]), gap=20),
    para("Early bird tickets for WordCamp Mumbai 2027 are <strong>on sale now</strong>. Lock in the best price before rates go up, and guarantee your seat at one of the community's most anticipated events." if ON_SALE else
         "Mark your calendars! The countdown to WordCamp Mumbai 2027 has begun, and early bird tickets go live on <strong>%s at %s</strong>." % (SALE_DATE, SALE_TIME)),
    para("Join developers, designers, content creators and WordPress enthusiasts from across the community for a day of learning, networking, collaboration, food and fun."),
    buttons([button("Get your ticket", "#tickets") if ON_SALE else button("Get updates", "/2027/news/"), button("Explore the venue", "/2027/venue/", style="outline", color="accent-1")], justify="left"),
])
intro_right = image(PHOTO, "A speaker on stage at a past WordCamp Mumbai", ratio="4/3", radius="16px")
sections.append(("01-intro", section([
    columns([column(intro_left, "55%"), column(intro_right, "45%", valign="center")], valign="center"),
    columns([
        column(fact_card("fact-calendar", "Date", EVENT_DATE, "Saturday, one full day")),
        column(fact_card("fact-pin", "Venue", "ATLAS SkillTech University", "Off BKC, Kurla West, Mumbai")),
        column(fact_card("fact-ticket", "Early bird", EARLY_BIRD_PRICE, "Limited seats, the lowest price we will put on sale") if ON_SALE else
               fact_card("fact-ticket", "Tickets on sale", "11 October 2026", SALE_TIME + ", right here on this page")),
        column(fact_card("fact-ticket", "To buy", "WordPress.org account", "Log in to buy; creating one takes a minute") if ON_SALE else
               fact_card("fact-ticket", "Early bird", "Limited seats", "The lowest price we will put on sale")),
    ]),
], bg=None, bgimage=(PNG + "motif-gateway@2x.png", "320px auto", "100% 100%", "no-repeat"))))

sections.append(("02-sep-vadapav", separator("vadapav")))

# 3. the ticket widget slot ----------------------------------------------------
slot = group("\n\n".join([
    chip("Coming soon", tone="soon", bg="accent-5"),
    heading("Ticket sales open on %s at %s" % (SALE_DATE.split(", ")[1], SALE_TIME), 3, "large"),
    para("Early bird tickets for WordCamp Mumbai 2027 go on sale right here on %s at %s. Early bird spots are limited and tend to go fast, so bookmark this page and come back the moment they drop." % (SALE_DATE, SALE_TIME)),
    para("You will need a <strong>WordPress.org account</strong> to buy a ticket (the account for the official WordPress.org website, not your own WordPress site). Create one now so you are ready when sales open."),
    buttons([button("Create a WordPress.org account", REGISTER), button("Get updates", "/2027/news/", style="outline", color="accent-1")], justify="left"),
]), bg="base", radius="16px", padding=(50, 50, 50, 50), gap=30, cls="wcm-ticket-slot", border_left=("accent-2", "4px"))

# the CampTix widget: the shortcode on the site, a static stand-in for previews and the gate
fake_row = lambda name, price, left: '<tr><td>%s</td><td>%s</td><td>%s</td><td>0</td></tr>' % (name, price, left)
widget_preview = group("\n\n".join([
    para("Please <a href=\"#\">log in with your WordPress.org account</a> before choosing a ticket.", color="accent-4", size="small"),
    '<!-- wp:table --><figure class="wp-block-table"><table><thead><tr><th>Description</th><th>Price</th><th>Remaining</th><th>Quantity</th></tr></thead><tbody>%s</tbody></table></figure><!-- /wp:table -->' % fake_row("Early Bird", EARLY_BIRD_PRICE, "50"),
    buttons([button("Go to attendee information", "#")], justify="right"),
]), bg="base", radius="16px", padding=(50, 50, 50, 50), gap=30, cls="wcm-tix")
widget = ('<!-- ds:site-only -->\n%s\n<!-- /ds:site-only -->\n<!-- ds:preview-only -->\n%s\n<!-- /ds:preview-only -->'
          % (group('<!-- wp:shortcode -->\n[camptix]\n<!-- /wp:shortcode -->', bg="base", radius="16px", padding=(50, 50, 50, 50), gap=30, cls="wcm-tix"), widget_preview))

sections.append(("03-tickets", section([
    section_header("Tickets", "Choose your pass", "Early bird tickets are on sale now" if ON_SALE else "On sale from %s, %s" % (SALE_DATE, SALE_TIME)),
    widget if ON_SALE else slot,
    para("Each ticket admits one person. Your confirmation and receipt arrive by email, with a link to edit your details or pass the ticket on." if ON_SALE else
         "Ticket types and prices will be listed here when sales open. Each ticket admits one person.", align="center", size="small", color="accent-4"),
], bg="accent-5", bgimage=(PNG + "tile-lattice-light@2x.png", "120px auto", "0 0", "repeat"), anchor="tickets")))

# 4. why early -----------------------------------------------------------------
sections.append(("04-why-early", section([
    section_header("Early bird", "Why grab your ticket early?", "WordCamp Mumbai is one of the most awaited WordCamps across the community"),
    columns([
        point("01", "Lock in the best price", "Early bird is the lowest price we will put on sale. Rates go up once the first batch is gone."),
        point("02", "Guarantee your seat", "Seats are limited and the early batch tends to go fast. Booking early means you are in the room on %s." % EVENT_DATE),
        point("03", "Be the first to know", "Ticket holders get the speaker line-up, session tracks and schedule news as soon as they are announced."),
    ]),
], bg=None, bgimage=(PNG + "motif-palm@2x.png", "420px auto", "0 100%", "no-repeat"))))

# 5. what's included -------------------------------------------------------------
sections.append(("05-included", section([
    section_header("Your pass", "What's included in your ticket?", "Learning, networking, collaboration, food and fun"),
    columns([
        included("Full conference access", "Every talk and workshop on %s, plus the hallway track in between." % EVENT_DATE),
        included("Lunch, chai and snacks", "Lunch and refreshments through the day. Food is part of the fun."),
        included("Badge and swag", "Your attendee badge, lanyard and WordCamp Mumbai 2027 swag."),
        included("The community", "300+ developers, designers, creators, founders and WordPress users in one room."),
    ]),
], bg="accent-5", bgimage=(PNG + "tile-lattice-light@2x.png", "120px auto", "0 0", "repeat"))))

# 6. good to know --------------------------------------------------------------------
faqs = group("\n\n".join([
    details("Which tickets are on sale?", ["Early bird tickets are on sale now, <a href=\"#tickets\">on this page</a>. Early bird is a limited batch; regular tickets follow once it is gone."] if ON_SALE else
            ["Early bird tickets go on sale on %s at %s, on this page. Early bird is a limited batch; regular tickets follow once it is gone." % (SALE_DATE, SALE_TIME)]),
    details("How much does a ticket cost?", ["Early bird tickets are %s. WordCamp tickets are kept deliberately affordable; our <a href=\"/2027/call-for-sponsors/\">sponsors</a> cover most of what it takes to run the day." % EARLY_BIRD_PRICE] if ON_SALE else
            ["Prices will be listed here when sales open. WordCamp tickets are kept deliberately affordable; our <a href=\"/2027/call-for-sponsors/\">sponsors</a> cover most of what it takes to run the day."]),
    details("Do I need an account to buy a ticket?", ["Yes. Tickets are sold through WordCamp.org, so you log in with your WordPress.org account before choosing a ticket. This is the account for the official WordPress.org website, not your personal WordPress site. <a href=\"%s\">Create one here</a> if you do not have one yet." % REGISTER]),
    details("How can I pay?", ["We accept all major cards and UPI. Your confirmation and receipt arrive by email as soon as the payment goes through."]),
    details("Can I transfer my ticket or get a refund?", ["Each ticket admits one person. Attendee details can be edited from the link in your confirmation email, so a ticket can be passed on to someone else. Refund terms will be published alongside the tickets when sales open."]),
    details("What do I need on the day?", ["A digital copy of your confirmation email and a valid photo ID. Collect your badge at the registration desk and wear it throughout the event. By buying a ticket you agree to the <a href=\"/2027/code-of-conduct/\">Code of Conduct</a>."]),
]), gap=30)
sections.append(("06-good-to-know", section([
    columns([
        column("\n\n".join([
            section_header("Good to know", "Before you buy", align="left"),
            para("The short answers to the questions we get asked most. Anything else, <a href=\"/2027/contact/\">write to us</a> and we will get back to you."),
            para("Speaking, sponsoring or volunteering? The <a href=\"/2027/call-for-speakers/\">call for speakers</a> and the <a href=\"/2027/call-for-sponsors/\">call for sponsors</a> are open now."),
        ]), "40%"),
        column(faqs, "60%"),
    ]),
], bg=None, bgimage=(PNG + "tile-lattice-blue@2x.png", "120px auto", "0 0", "repeat"))))

# 7. gradient band ---------------------------------------------------------------------
band_inner = group("\n\n".join([
    eyebrow("Save the date", align="center", color="base"),
    heading(EVENT_DATE, 2, "x-large", align="center", color="base"),
    para("Don't wait: early bird spots are limited and tend to go fast. Grab yours before the price goes up. #WCMumbai" if ON_SALE else
         "Don't wait: early bird spots are limited and tend to go fast. Stay tuned for the sale and grab yours the moment it drops. #WCMumbai", align="center", color="base"),
    buttons([button("Get your ticket", "#tickets", bg="base", color="accent-3") if ON_SALE else button("Get updates", "/2027/news/", bg="base", color="accent-3"), button("Contact us", "/2027/contact/", style="outline", color="base")]),
]), layout="constrained", padding=(70, 70), gap=30)
sections.append(("07-save-the-date", group(band_inner, layout="constrained", align="full", gradient=GRADIENT, cls="wcm-band-gradient", gap=0)))

os.makedirs(os.path.join(HERE, "sections"), exist_ok=True)
for f in os.listdir(os.path.join(HERE, "sections")):
    os.remove(os.path.join(HERE, "sections", f))
for n, m in sections:
    with open(os.path.join(HERE, "sections", n + ".html"), "w") as fh:
        fh.write(m + "\n")
with open(os.path.join(HERE, "block.html"), "w") as fh:
    fh.write("\n\n".join(m for n, m in sections) + "\n")
with open(os.path.join(HERE, "camptix-widget.html"), "w") as fh:
    fh.write("<!-- wp:shortcode -->\n[camptix]\n<!-- /wp:shortcode -->\n")
print("wrote %d sections, block.html and camptix-widget.html" % len(sections))
