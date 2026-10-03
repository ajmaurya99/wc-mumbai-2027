#!/usr/bin/env python3
"""Generate the WordCamp Mumbai 2027 organizers page as core-block markup.

Reads organizers.json (refresh it with fetch.py) and writes sections/NN-name.html
and block.html (paste into the Organizers page's code editor). Helpers live in
design-system/tools/blocks.py. Run: python3 design-system/examples/organizers/build.py
"""
import html
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(HERE)), "tools"))
from blocks import *  # noqa: E402,F401

PEOPLE = json.load(open(os.path.join(HERE, "organizers.json")))
BIO_WORDS = 26
PLACEHOLDER = "https://placehold.co/320x320/f2f7fa/546776.png?text=Photo+soon"
EVENT_DATE = "13 February 2027"
VENUE = "ATLAS SkillTech University, Kurla"
CONTACT = "/2027/contact/"
TICKETS = "#"  # tickets page is still a draft; replace when it goes live


def esc(s):
    return html.escape(s, quote=False)


def clip(bio):
    """First ~BIO_WORDS words of the bio, cut at a word boundary, with an ellipsis."""
    if not bio:
        return "Part of the WordCamp Mumbai 2027 organizing team."
    words = bio.split()
    if len(words) <= BIO_WORDS:
        return esc(bio)
    cut = " ".join(words[:BIO_WORDS]).rstrip(",;:.–-")
    return esc(cut) + "…"


# ------------------------------------------------------------- atoms --

def avatar(person):
    """Round 160px photo: Image block, aspect 1, cover, radius 999px, centred."""
    photo = person.get("photo")
    src = photo["url"] if photo else PLACEHOLDER
    alt = esc(person["name"])
    j = {"align": "center", "width": "160px", "height": "160px", "aspectRatio": "1", "scale": "cover",
         "sizeSlug": "medium_large" if photo else "full", "linkDestination": "none",
         "style": {"border": {"radius": "999px"}}}
    return ('<!-- wp:image %s -->\n<figure class="wp-block-image aligncenter size-%s is-resized has-custom-border">'
            '<img src="%s" alt="%s" style="border-radius:999px;aspect-ratio:1;object-fit:cover;width:160px;height:160px"/></figure>\n<!-- /wp:image -->'
            % (json.dumps(j, separators=(",", ":")), j["sizeSlug"], src, alt))


def social(person):
    """Social Links block (dynamic on the site) with a static stand-in for previews."""
    name = esc(person["name"])
    links = person.get("links", {})
    items = [("wordpress", "https://profiles.wordpress.org/%s/" % person["wporg"], "%s on WordPress.org" % name)] if person.get("wporg") else []
    items += [("linkedin", links.get("linkedin", "#"), "%s on LinkedIn" % name),
              ("x", links.get("x", "#"), "%s on X" % name),
              ("chain", links.get("website", "#"), "%s's website" % name)]
    site = ('<!-- wp:social-links {"iconColor":"accent-1","iconColorValue":"#0073aa","iconBackgroundColor":"accent-5","iconBackgroundColorValue":"#f2f7fa","className":"wcm-social","layout":{"type":"flex","justifyContent":"center"}} -->\n'
            '<ul class="wp-block-social-links has-icon-color has-icon-background-color wcm-social">%s</ul>\n<!-- /wp:social-links -->'
            % "\n".join('<!-- wp:social-link {"url":"%s","service":"%s","label":"%s"} /-->' % (url, svc, label) for svc, url, label in items))
    glyph = {"wordpress": "W", "linkedin": "in", "x": "X", "chain": "↗"}
    preview = ('<ul class="wp-block-social-links has-icon-color has-icon-background-color wcm-social is-layout-flex is-content-justification-center">%s</ul>'
               % "".join('<li class="wp-social-link wp-social-link-%s wp-block-social-link has-accent-1-color has-accent-5-background-color"><a class="wp-block-social-link-anchor" href="%s" aria-label="%s">%s</a></li>'
                         % (svc, url, label, glyph[svc]) for svc, url, label in items))
    return "<!-- ds:site-only -->\n%s\n<!-- /ds:site-only -->\n<!-- ds:preview-only -->\n%s\n<!-- /ds:preview-only -->" % (site, preview)


def person_card(person):
    return card([
        avatar(person),
        heading(esc(person["name"]), 3, "large", align="center"),
        '<!-- wp:paragraph {"align":"center","className":"wcm-organizer__bio"} -->\n<p class="has-text-align-center wcm-organizer__bio">%s</p>\n<!-- /wp:paragraph -->' % clip(person["bio"]),
        social(person),
        para('<a href="%s">Read profile →</a>' % person["profile"], align="center", weight=700),
    ], bg="base", gap=20, cls="wcm-card wcm-organizer")


def stat(n, label, text):
    return column(card([
        para(n, size="xx-large", color="accent-1", weight=700),
        eyebrow(label, color="accent-4"),
        para(text),
    ], bg="accent-5", gap=20))


# ---------------------------------------------------------- sections --

sections = []

# 01 intro: eyebrow, H1, Kalam tagline, two paragraphs, buttons; stat tiles; white, gateway motif
intro = group("\n\n".join([
    eyebrow("Organizers"),
    heading("The people behind WordCamp Mumbai 2027", 1, "xx-large"),
    '<!-- wp:paragraph {"textColor":"accent-2","fontSize":"large","fontFamily":"kalam"} -->\n<p class="has-accent-2-color has-text-color has-large-font-size has-kalam-font-family">Aamchi Mumbai, Aapla WordPress</p>\n<!-- /wp:paragraph -->',
]), gap=20)
sections.append(("01-intro", section([
    intro,
    para("WordCamp Mumbai is planned and run entirely by volunteers from the Mumbai WordPress community. Developers, designers, marketers, educators and business owners who give their evenings and weekends so the community can meet for a day."),
    para("Say hello when you see them at the venue. They are the friendly faces making %s happen." % EVENT_DATE),
    buttons([button("Get tickets", TICKETS), button("Contact the team", CONTACT, style="outline", color="accent-1")], justify="left"),
    columns([
        stat(str(len(PEOPLE)), "Organizers", "Volunteers from the Mumbai WordPress community."),
        stat("1", "Day", "%s at %s." % (EVENT_DATE, VENUE)),
        stat("100%", "Volunteer-run", "No one is paid. Everyone is invested."),
    ]),
], bg=None, bgimage=(PNG + "motif-gateway@2x.png", "320px auto", "100% 100%", "no-repeat"))))
# bg=None: the page ground is already white, and a Base background here would sit flush
# under the Header template part and paint over its box-shadow (the shadow shows on
# /about-us because nothing opaque follows the header).

# 02 separator marigold
sections.append(("02-sep-marigold", separator("marigold")))

# 03 team grid: three cards per row, sky wash, lattice tile
rows = [PEOPLE[i:i + 3] for i in range(0, len(PEOPLE), 3)]
grid = group("\n\n".join(columns([column(person_card(p)) for p in row]) for row in rows),
             layout="constrained", align="wide", gap=30)
sections.append(("03-team", section([
    section_header("Organizing team", "Meet the team", body="%s people, one WordCamp. Say hello when you see them." % ("Twelve" if len(PEOPLE) == 12 else str(len(PEOPLE)))),
    grid,
], bg="accent-5", bgimage=(PNG + "tile-lattice-light@2x.png", "120px auto", "0 0", "repeat"))))

# 04 callout: volunteer, white
sections.append(("04-volunteer", section([
    section_header("Volunteers", "Want to help on the day?", body="Volunteers run registration, look after speakers and keep the day moving. The call for volunteers opens soon; write to us if you would like to be on the list."),
    buttons([button("Contact the team", CONTACT), button("mumbai@wordcamp.org", "mailto:mumbai@wordcamp.org", style="outline", color="accent-1")]),
], bg="base")))

# --------------------------------------------------------------- write --

os.makedirs(os.path.join(HERE, "sections"), exist_ok=True)
for f in os.listdir(os.path.join(HERE, "sections")):
    os.remove(os.path.join(HERE, "sections", f))
for name, markup in sections:
    with open(os.path.join(HERE, "sections", name + ".html"), "w") as fh:
        fh.write(markup + "\n")
with open(os.path.join(HERE, "block.html"), "w") as fh:
    fh.write("\n\n".join("<!-- ==== %s ==== -->\n%s" % (n, m) for n, m in sections) + "\n")
print("wrote %d sections and block.html for %d organizers" % (len(sections), len(PEOPLE)))
