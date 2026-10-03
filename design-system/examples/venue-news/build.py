#!/usr/bin/env python3
"""Generate the Venue page and the News (Blog Home template) for WordCamp Mumbai 2027.

Writes
    venue/sections/NN-name.html, venue/block.html     paste into the Venue page's code editor
    news/sections/NN-name.html,  news/block.html      the News body, for previews and the gate
    news/template.html                                 the whole Blog Home template (header part,
                                                       main, footer part) for the Site Editor
Helpers live in design-system/tools/blocks.py. Run: python3 design-system/examples/venue-news/build.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(HERE)), "tools"))
from blocks import *  # noqa: E402,F401

FILES = "https://mumbai.wordcamp.org/2027/files/"
POSTER = FILES + "2026/09/atlas-skilltech-venue-partner-featured-image-1024x536.png"
ATLAS_LOGO = FILES + "2026/09/4schoolatlas-trasnparent-1024x585.jpg"
RICKSHAW = FILES + "2026/10/3-768x512.png"
PHOTOS = [  # the four campus photos already in the media library
    (FILES + "2026/09/venue-1024x668.jpeg", "ATLAS SkillTech University campus"),
    (FILES + "2026/09/venue-2-1024x681.jpg", "Auditorium at ATLAS SkillTech University"),
    (FILES + "2026/09/venue-3-1024x681.jpg", "Seating inside the ATLAS campus"),
    (FILES + "2026/09/venue-4-1024x681.jpg", "Open space on the ATLAS campus"),
]
MAPS = "https://www.google.com/maps/dir/?api=1&destination=ATLAS+SkillTech+University+Equinox+Business+Park+Kurla+West+Mumbai"
POST = "/2027/venue-partner/"
EVENT_DATE = "13 February 2027"


def tagline(text, align="left"):
    al = '"align":"%s",' % align if align != "left" else ""
    cls = "has-text-align-%s " % align if align != "left" else ""
    return ('<!-- wp:paragraph {%s"textColor":"accent-2","fontSize":"large","fontFamily":"kalam"} -->\n'
            '<p class="%shas-accent-2-color has-text-color has-large-font-size has-kalam-font-family">%s</p>\n<!-- /wp:paragraph -->' % (al, cls, text))


def gallery(items):
    imgs = "\n\n".join(image(src, alt, ratio="4/3", radius="16px", size="large") for src, alt in items)
    return '<!-- wp:gallery {"columns":2,"linkTo":"none"} -->\n<figure class="wp-block-gallery has-nested-images columns-2 is-cropped">%s</figure>\n<!-- /wp:gallery -->' % imgs


# ------------------------------------------------------------------ venue --

venue = []

intro_left = "\n\n".join([
    group("\n\n".join([
        eyebrow("Venue"),
        heading("ATLAS SkillTech University", 1, "xx-large"),
        tagline("Off BKC, Kurla West"),
    ]), gap=20),
    para("WordCamp Mumbai 2027 happens on <strong>%s</strong> at ATLAS SkillTech University, a multidisciplinary campus off the Bandra Kurla Complex that brings together design, business, technology and law. Modern rooms for the talks and workshops, and plenty of space to meet, talk and network between them." % EVENT_DATE),
    buttons([button("Get directions", MAPS), button("About our venue partner", POST, style="outline", color="accent-1")], justify="left"),
])
intro_right = image(POSTER, "ATLAS SkillTech University, venue partner of WordCamp Mumbai 2027", ratio="16/9", radius="16px")
venue.append(("01-intro", section([
    columns([column(intro_left, "55%"), column(intro_right, "45%", valign="center")], valign="center"),
    columns([
        column(fact_card("fact-calendar", "Date", EVENT_DATE, "One day of talks, workshops and the hallway track")),
        column(fact_card("fact-pin", "Address", "Equinox Business Park", "Tower 2, off BKC, Kurla West, Mumbai 400070")),
        column(fact_card("fact-train", "Getting there", "Road, rail and metro", "Nearest stations and parking closer to the date")),
    ]),
], bg=None, bgimage=(PNG + "motif-gateway@2x.png", "320px auto", "100% 100%", "no-repeat"))))

venue.append(("02-sep-taxi", separator("taxi")))

space_left = "\n\n".join([
    section_header("The campus", "A space built for learning and connecting", align="left"),
    para("The campus has modern infrastructure and spacious facilities that suit a WordPress conference well: dedicated spaces for talks and workshops, and areas where attendees can meet, have conversations and network with fellow members of the community."),
    para("Whether you build sites for a living, exchange ideas with fellow designers, run an agency looking for collaborators or are attending your first WordCamp, the venue gives you plenty of room to connect."),
    tagline("The session may be 30 minutes. The hallway conversation could stay with you for years."),
])
venue.append(("03-campus", section([
    columns([column(space_left, "50%", valign="center"), column(gallery(PHOTOS), "50%")]),
], bg="accent-5", bgimage=(PNG + "tile-lattice-light@2x.png", "120px auto", "0 0", "repeat"))))

travel = group("\n\n".join([
    fact_card("fact-train", "By train", "Details closer to the date", "Nearest suburban railway station and the walk from it"),
    fact_card("fact-pin", "By metro", "Details closer to the date", "Nearest metro station and exit"),
    fact_card("fact-ticket", "By air", "Mumbai airport (BOM)", "About 30 minutes by road, traffic permitting"),
    fact_card("fact-calendar", "Parking", "Details closer to the date", "On-campus and nearby options"),
]), gap=30)
venue.append(("04-getting-there", section([
    columns([
        column("\n\n".join([section_header("Getting there", "Well connected by road, rail and metro", align="left", body="We will share detailed travel information, including the nearest railway and metro stations, closer to the date. Until then, the directions button above gets you to the gate."), travel]), "55%"),
        column(image(RICKSHAW, "Watercolour illustration of a Mumbai auto-rickshaw", radius="16px", size="medium_large"), "45%", valign="center"),
    ]),
], bg=None, bgimage=(PNG + "motif-palm@2x.png", "420px auto", "0 100%", "no-repeat"))))

venue.append(("05-thanks", section([
    columns([
        column(group(image(ATLAS_LOGO, "ATLAS SkillTech University: ISDI, ISME, uGDX, Law", radius="16px", size="large"), bg="base", radius="16px", padding=(40, 40, 40, 40), cls="wcm-card"), "40%", valign="center"),
        column("\n\n".join([
            section_header("Venue partner", "Thank you, ATLAS SkillTech University", align="left"),
            para("When we approached ATLAS, the response was warm and encouraging: the team was happy to welcome the WordPress community to their campus and supported us as we worked through the event and our venue requirements."),
            para("We are looking forward to seeing the campus filled with the energy of the Mumbai WordPress community."),
            buttons([button("Read the announcement", POST, style="outline", color="accent-1")], justify="left"),
        ]), "60%", valign="center"),
    ], valign="center"),
], bg="accent-5")))

# ------------------------------------------------------------------- news --

news = []

# subscribe card: Jetpack Subscriptions on the site, a static stand-in in previews
subscribe = '''<!-- ds:site-only -->
<!-- wp:jetpack/subscriptions {"buttonText":"Subscribe","submitButtonText":"Subscribe","buttonBackgroundColor":"accent-1","textColor":"base","borderRadius":999,"padding":12,"spacing":8} /-->
<!-- /ds:site-only -->
<!-- ds:preview-only -->
%s
<!-- /ds:preview-only -->''' % group("\n\n".join([
    group(para("you@example.com", color="accent-4"), layout="flex", bg="base", radius="999px", padding=(20, 20, 30, 30), gap=0, cls="wcm-fake-input"),
    buttons([button("Subscribe", "#")], justify="left"),
]), layout="flex", wrap="wrap", valign="center", gap=20)

subscribe_card = group("\n\n".join([
    group("\n\n".join([heading("Get updates in your inbox", 2, "large"), para("Speaker announcements, schedule and ticket news, the moment we publish them.")]), gap=20),
    subscribe,
]), bg="accent-5", radius="16px", padding=(40, 40, 40, 40), gap=30, cls="wcm-card")

news.append(("01-intro", section([
    columns([
        column("\n\n".join([
            group("\n\n".join([
                eyebrow("Latest news"),
                heading("News &amp; updates", 1, "xx-large"),
                tagline("Aamchi Mumbai, Aapla WordPress"),
            ]), gap=20),
            para("Announcements, behind-the-scenes notes and everything you need to know on the road to %s." % EVENT_DATE),
        ]), "55%", valign="center"),
        column(subscribe_card, "45%", valign="center"),
    ], valign="center"),
    columns([
        column(fact_card("fact-calendar", "Date", EVENT_DATE, "One day of talks, workshops and the hallway track")),
        column(fact_card("fact-pin", "Venue", "ATLAS SkillTech University", "Off BKC, Kurla West, Mumbai")),
        column(fact_card("fact-ticket", "Tickets", "Coming soon", "Follow the news for the on-sale date")),
    ]),
], bg=None, bgimage=(PNG + "motif-gateway@2x.png", "320px auto", "100% 100%", "no-repeat"))))

# one post per row: image 40% | category + date, title, excerpt with "Read more"
post_card = '''<!-- wp:group {"className":"wcm-card wcm-post","style":{"border":{"radius":"16px"},"spacing":{"padding":{"top":"var:preset|spacing|40","bottom":"var:preset|spacing|40","left":"var:preset|spacing|40","right":"var:preset|spacing|40"}}},"backgroundColor":"base","layout":{"type":"default"}} -->
<div class="wp-block-group wcm-card wcm-post has-base-background-color has-background" style="border-radius:16px;padding-top:var(--wp--preset--spacing--40);padding-right:var(--wp--preset--spacing--40);padding-bottom:var(--wp--preset--spacing--40);padding-left:var(--wp--preset--spacing--40)"><!-- wp:columns {"verticalAlignment":"center","style":{"spacing":{"blockGap":{"top":"var:preset|spacing|30","left":"var:preset|spacing|40"}}}} -->
<div class="wp-block-columns are-vertically-aligned-center"><!-- wp:column {"verticalAlignment":"center","width":"40%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:40%"><!-- wp:post-featured-image {"isLink":true,"aspectRatio":"16/9","style":{"border":{"radius":"16px"}}} /--></div>
<!-- /wp:column -->

<!-- wp:column {"verticalAlignment":"center","width":"60%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:60%"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|20"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|30"}},"layout":{"type":"flex","flexWrap":"wrap"}} -->
<div class="wp-block-group"><!-- wp:post-terms {"term":"category","style":{"typography":{"textTransform":"uppercase","letterSpacing":"0.08em","fontStyle":"normal","fontWeight":"700"}},"textColor":"accent-2","fontSize":"small"} /-->

<!-- wp:post-date {"textColor":"accent-4","fontSize":"small"} /--></div>
<!-- /wp:group -->

<!-- wp:post-title {"isLink":true,"fontSize":"large"} /-->

<!-- wp:post-excerpt {"moreText":"Read more →","excerptLength":30} /--></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></div>
<!-- /wp:group -->'''

query_site = '''<!-- wp:query {"queryId":38,"query":{"perPage":10,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","author":"","search":"","exclude":[],"sticky":"","inherit":true},"align":"wide","className":"wcm-news","layout":{"type":"default"}} -->
<div class="wp-block-query alignwide wcm-news"><!-- wp:post-template {"style":{"spacing":{"blockGap":"var:preset|spacing|30"}},"layout":{"type":"default"}} -->
%s
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph {"align":"center"} -->
<p class="has-text-align-center">No posts yet. The first announcements are on their way.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results -->

<!-- wp:query-pagination {"paginationArrow":"arrow","align":"wide","layout":{"type":"flex","justifyContent":"space-between"}} -->
<!-- wp:query-pagination-previous /-->

<!-- wp:query-pagination-numbers /-->

<!-- wp:query-pagination-next /-->
<!-- /wp:query-pagination --></div>
<!-- /wp:query -->''' % post_card


def fake_post(date, cat, title, text, img):
    return group(columns([
        column(image(img, "", ratio="16/9", radius="16px"), "40%", valign="center"),
        column(group("\n\n".join([
            group("\n\n".join([eyebrow(cat), para(date, color="accent-4", size="small")]), layout="flex", wrap="wrap", gap=30),
            heading('<a href="#">%s</a>' % title, 2, "large"),
            para(text + ' <a href="#">Read more →</a>'),
        ]), gap=20), "60%", valign="center"),
    ], align=None, gap=40, valign="center"), bg="base", radius="16px", padding=(40, 40, 40, 40), cls="wcm-card wcm-post")


query_preview = group("\n\n".join([
    fake_post("3 October 2026", "WordCamp Mumbai", "Call for Sponsors", "WordCamp Mumbai 2027 is bringing together the people who build, use, support and shape the web with WordPress. We are inviting organisations that believe in open source to join us as sponsors.", FILES + "2026/09/call-for-sponsors-featured-image-1024x536.png"),
    fake_post("16 September 2026", "WordCamp Mumbai", "Experience WordCamp Mumbai 2027 at ATLAS SkillTech University", "As one of the oldest WordPress community events in India, WordCamp Mumbai brings together developers, designers, agency owners, creators and enthusiasts from across Mumbai and beyond.", POSTER),
]), layout="constrained", align="wide", gap=30)

query = "<!-- ds:site-only -->\n%s\n<!-- /ds:site-only -->\n<!-- ds:preview-only -->\n%s\n<!-- /ds:preview-only -->" % (query_site, query_preview)

news.append(("02-posts", section([query], bg="accent-5", bgimage=(PNG + "tile-lattice-light@2x.png", "120px auto", "0 0", "repeat"))))

# ---------------------------------------------------------------- write --

def write(name, sections):
    d = os.path.join(HERE, name)
    os.makedirs(os.path.join(d, "sections"), exist_ok=True)
    for f in os.listdir(os.path.join(d, "sections")):
        os.remove(os.path.join(d, "sections", f))
    for n, m in sections:
        with open(os.path.join(d, "sections", n + ".html"), "w") as fh:
            fh.write(m + "\n")
    with open(os.path.join(d, "block.html"), "w") as fh:
        fh.write("\n\n".join(m for n, m in sections) + "\n")
    print("wrote %s: %d sections" % (name, len(sections)))

write("venue", venue)
write("news", news)

# the Blog Home template: header part, main (constrained, so full and wide sections work), footer part
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(HERE)), "tools"))
from preview import for_site  # noqa: E402
body = for_site("\n\n".join(m for n, m in news))
template = ('<!-- wp:template-part {"slug":"header","theme":"twentytwentyfive","area":"header"} /-->\n\n'
            '<!-- wp:group {"tagName":"main","style":{"spacing":{"margin":{"top":"0"},"blockGap":"0"}},"layout":{"type":"constrained"}} -->\n'
            '<main class="wp-block-group" style="margin-top:0">%s</main>\n<!-- /wp:group -->\n\n'
            '<!-- wp:template-part {"slug":"footer","theme":"twentytwentyfive","area":"footer"} /-->\n') % body
with open(os.path.join(HERE, "news", "template.html"), "w") as fh:
    fh.write(template)
print("wrote news/template.html")
