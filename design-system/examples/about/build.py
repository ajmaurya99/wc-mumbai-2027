#!/usr/bin/env python3
"""Generate the About page for WordCamp Mumbai 2027 as core-block markup.

Writes sections/NN-name.html and block.html (paste into the About page's code
editor). Copy is the page's own, rearranged. Helpers live in
design-system/tools/blocks.py. Run: python3 design-system/examples/about/build.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(HERE)), "tools"))
from blocks import *  # noqa: E402,F401

FILES = "https://mumbai.wordcamp.org/2027/files/"
BOOTH = FILES + "2026/09/sponsor-area-1024x1024.png"
FORM = "https://forms.gle/aGj8NryWXTL9EQeU6"
EVENT_DATE = "13 February 2027"


def tagline(text):
    return ('<!-- wp:paragraph {"textColor":"accent-2","fontSize":"large","fontFamily":"kalam"} -->\n'
            '<p class="has-accent-2-color has-text-color has-large-font-size has-kalam-font-family">%s</p>\n<!-- /wp:paragraph -->' % text)


def details(q, paras):
    body = "\n\n".join(para(p) for p in paras)
    return ('<!-- wp:details {"className":"wcm-faq","style":{"border":{"radius":"16px"},"spacing":{"padding":{"top":"var:preset|spacing|40","bottom":"var:preset|spacing|40","left":"var:preset|spacing|40","right":"var:preset|spacing|40"}}},"backgroundColor":"accent-5"} -->\n'
            '<details class="wp-block-details wcm-faq has-accent-5-background-color has-background" style="border-radius:16px;padding-top:var(--wp--preset--spacing--40);padding-right:var(--wp--preset--spacing--40);padding-bottom:var(--wp--preset--spacing--40);padding-left:var(--wp--preset--spacing--40)"><summary>%s</summary>%s</details>\n<!-- /wp:details -->'
            % (q, body))


def stat(n, label, text):
    return column(card([
        para(n, size="xx-large", color="accent-1", weight=700),
        eyebrow(label, color="accent-4"),
        para(text),
    ], bg="accent-5", gap=20))


def pillar(n, title, text):
    h3 = '<mark class="has-inline-color has-accent-1-color">%s</mark> %s' % (n, title)
    return column(group("\n\n".join([heading(h3, 3, "large"), para(text)]), bg="base", radius="16px",
                        padding=(40, 40, 40, 40), gap=20, cls="wcm-card wcm-why", border_left=("accent-2", "4px")))


sections = []

intro_left = "\n\n".join([
    group("\n\n".join([
        eyebrow("WordCamp Mumbai 2027 · %s" % EVENT_DATE),
        heading("About Us", 1, "xx-large"),
        tagline("Aamchi Mumbai. Aapla WordPress."),
    ]), gap=20),
    para("WordCamp Mumbai 2027 is a community-driven gathering of WordPress enthusiasts, creators, developers, designers, entrepreneurs, educators, marketers and curious minds who come together to learn, share, connect and build."),
    para("It is not just an event. It is a celebration of the people who make the WordPress community what it is."),
    buttons([button("Meet the organizers", "/2027/organizers/"), button("Contact us", "/2027/contact/", style="outline", color="accent-1")], justify="left"),
])
intro_right = image(BOOTH, "Attendees talking at a sponsor booth at WordCamp Mumbai", ratio="1", radius="16px")
sections.append(("01-intro", section([
    columns([column(intro_left, "55%"), column(intro_right, "45%", valign="center")], valign="center"),
    columns([
        stat("300+", "Attendees", "Developers, designers, marketers, students and site owners."),
        stat("1", "Day", "%s at ATLAS SkillTech University, Kurla." % EVENT_DATE),
        stat("12", "Organizers", "Volunteers from the Mumbai WordPress community."),
        stat("100%", "Volunteer-run", "No one is paid. Everyone is invested."),
    ]),
], bg=None, bgimage=(PNG + "motif-gateway@2x.png", "320px auto", "100% 100%", "no-repeat"))))

sections.append(("02-sep-marigold", separator("marigold")))

sections.append(("03-city", section([
    section_header("The city", "A city of many worlds", "Fast, ambitious, diverse, creative and endlessly collaborative", body="Mumbai has always been a city of many worlds. WordCamp Mumbai brings that same spirit to the WordPress community: one day where the ideas, conversations, creativity and connections that make Mumbai and WordPress special come together."),
    columns([
        pillar("01", "Learn", "Talks and workshops from the people who build with WordPress every day, whether you are on your first theme or your hundredth client site."),
        pillar("02", "Share", "Bring what you know. Lightning talks, hallway conversations and Contributor Day are where the community teaches itself."),
    ]),
    columns([
        pillar("03", "Connect", "Freelancers, agencies, product teams, students and first-timers in one room. Meet the people who understand your world."),
        pillar("04", "Build", "Discover new tools, new collaborators and new opportunities, and leave with something to start on Monday."),
    ]),
], bg="accent-5", bgimage=(PNG + "tile-lattice-light@2x.png", "120px auto", "0 0", "repeat"))))

sections.append(("04-everyone", section([
    columns([
        column("\n\n".join([
            section_header("Who it is for", "There is a place for you here", align="left"),
            para("Whether you have been building with WordPress for years or are just getting started, come to learn something new, share what you know, meet people who understand your world, discover new opportunities and be part of a community that believes in open collaboration."),
            para("Developers, designers, content creators, marketers, agency owners, founders, educators, students and WordPress users: WordCamp Mumbai is built by this community, for this community."),
        ]), "50%", valign="center"),
        column(group("\n\n".join([
            details("What is a WordCamp?", ["WordCamps are informal, community-organised conferences about WordPress. They are affordable, welcoming to beginners and run by volunteers from the local community, with support from the global WordPress community programme."]),
            details("Who organises WordCamp Mumbai?", ["A team of twelve volunteers from the Mumbai WordPress meetup community, in their evenings and weekends. <a href=\"/2027/organizers/\">Meet them here</a>."]),
            details("How much does it cost to attend?", ["WordCamp tickets are kept deliberately affordable; sponsors cover most of what it takes to run the day. Ticket details and the on-sale date will be announced in the <a href=\"/2027/news/\">news</a>."]),
            details("How can I get involved?", ["Sponsor, speak, volunteer or simply attend. The <a href=\"/2027/call-for-sponsors/\">call for sponsors</a> is open now; the calls for speakers and volunteers follow soon."]),
        ]), gap=30), "50%"),
    ]),
], bg=None, bgimage=(PNG + "motif-palm@2x.png", "420px auto", "0 100%", "no-repeat"))))

band_inner = group("\n\n".join([
    heading("Be part of WordCamp Mumbai 2027", 2, "x-large", align="center", color="base"),
    para("Join us in bringing the WordPress community together in Mumbai. Sponsor the day, bring your team, or just come and say hello.", align="center", color="base"),
    buttons([button("Become a sponsor", FORM, bg="base", color="accent-3"), button("Contact us", "/2027/contact/", style="outline", color="base")]),
]), layout="constrained", padding=(70, 70), gap=30)
sections.append(("05-be-part", group(band_inner, layout="constrained", align="full", gradient=GRADIENT, cls="wcm-band-gradient", gap=0)))

os.makedirs(os.path.join(HERE, "sections"), exist_ok=True)
for f in os.listdir(os.path.join(HERE, "sections")):
    os.remove(os.path.join(HERE, "sections", f))
for n, m in sections:
    with open(os.path.join(HERE, "sections", n + ".html"), "w") as fh:
        fh.write(m + "\n")
with open(os.path.join(HERE, "block.html"), "w") as fh:
    fh.write("\n\n".join(m for n, m in sections) + "\n")
print("wrote %d sections and block.html" % len(sections))
