#!/usr/bin/env python3
"""Home page sample B: the same sections as sample A, warmer and more colourful.

Differences from sample A (design-system/examples/home):
* section tints from the proposed wash tokens (marigold, teal, purple) and one
  full teal band (venue); the numbers strip is purple, the Be part band runs
  teal to purple;
* festive colours where AA allows: saffron for Kalam taglines and xx-large
  numerals, gold on teal, marigold chips; eyebrows stay teal or purple;
* a pattern or motif on every section; separators in four line colours;
* toran strip under the hero, kolam strip before the footer.
Run: python3 design-system/examples/home-b/build.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(HERE)), "tools"))
from blocks import *  # noqa: E402,F401

WASH_MARIGOLD, WASH_TEAL, WASH_PURPLE = "#FFF6E3", "#E8F3F4", "#F1ECFB"
GRADIENT_B = "linear-gradient(135deg,#006b78 0%,#6d28d9 100%)"
PLACEHOLDER = "https://placehold.co/%s/%s/%s.png?text=%s"


def section_c(inner, color, bgimage=None, cls=None, gap=40, padding=(70, 70)):
    """Section shell with a custom (wash) background colour."""
    import json
    j = {"align": "full", "style": {"color": {"background": color}, "spacing": {"padding": {"top": SPJ(padding[0]), "bottom": SPJ(padding[1])}, "blockGap": SPJ(gap)}}, "layout": {"type": "constrained"}}
    if cls:
        j["className"] = cls
    if bgimage:
        url, size, pos, rep = bgimage
        j["style"]["background"] = {"backgroundImage": {"url": url, "source": "file"}, "backgroundSize": size, "backgroundPosition": pos, "backgroundRepeat": rep}
    return '<!-- wp:group %s -->\n<div class="wp-block-group alignfull%s has-background" style="background-color:%s;padding-top:%s;padding-bottom:%s">%s</div>\n<!-- /wp:group -->' % (
        json.dumps(j, separators=(",", ":")), (" " + cls) if cls else "", color, SP(padding[0]), SP(padding[1]), "\n\n".join(inner))


def tagline(text, color_hex, align="center"):
    """Kalam tagline in a festive colour (large bold = AA large text)."""
    al = '"align":"%s",' % align if align != "left" else ""
    cls = "has-text-align-%s " % align if align != "left" else ""
    return ('<!-- wp:paragraph {%s"style":{"color":{"text":"%s"}},"fontSize":"large","fontFamily":"kalam"} -->\n'
            '<p class="%shas-text-color has-large-font-size has-kalam-font-family" style="color:%s">%s</p>\n<!-- /wp:paragraph -->') % (al, color_hex, cls, color_hex, text)


def header_b(eye, h2, tag=None, align="center", eye_color="accent-2", h_color=None, tag_color="#E0552D", body=None, body_color=None):
    parts = [eyebrow(eye, align, eye_color), heading(h2, 2, "x-large", align, h_color)]
    if tag:
        parts.append(tagline(tag, tag_color, align))
    if body:
        parts.append(para(body, align, color=body_color))
    return group("\n\n".join(parts), gap=20)


def fact_b(icon, label, value, edge, note=None, bg="base"):
    text = [para(label, color="accent-4", size="small"), para(value, size="large", weight=700)]
    if note:
        text.append(para(note, color="accent-4", size="small"))
    return group("\n\n".join([image(PNG + icon + "@2x.png", "", width="24px"), group("\n\n".join(text), gap=0)]),
                 layout="flex", wrap="nowrap", valign="center", bg=bg, radius="16px", cls="wcm-fact",
                 padding=(30, 30, 40, 40), gap=30, border_left=(edge, "4px"))


def chip_b(text, tone):
    import json
    if tone == "open":
        return ('<!-- wp:group {"className":"wcm-chip","style":{"color":{"background":"%s"},"border":{"radius":"8px"},"spacing":{"padding":{"top":"var:preset|spacing|20","bottom":"var:preset|spacing|20","left":"var:preset|spacing|30","right":"var:preset|spacing|30"}},"spacing":{"blockGap":"0"}},"layout":{"type":"flex"}} -->\n'
                '<div class="wp-block-group wcm-chip has-background" style="background-color:%s;border-radius:8px;padding-top:%s;padding-right:%s;padding-bottom:%s;padding-left:%s">%s</div>\n<!-- /wp:group -->') % (
            WASH_MARIGOLD, WASH_MARIGOLD, SP(20), SP(30), SP(20), SP(30), para(text, size="small", color="accent-3", weight=700))
    return chip(text, "soon")


def sep_b(icon, tone):
    s = separator(icon)
    return s.replace('"className":"wcm-sep"', '"className":"wcm-sep wcm-sep--%s"' % tone).replace('class="wp-block-group alignwide wcm-sep"', 'class="wp-block-group alignwide wcm-sep wcm-sep--%s"' % tone)


sections = []

# 01 strip: toran (marigold garland) straight under the hero
sections.append(("01-strip-toran", strip("toran")))

# 02 key facts on marigold wash, marigold dots tile, cards with three edge colours
left = [
    header_b("Key facts", "Mumbai becomes a meeting point for the WordPress community", "Aamchi Mumbai, Aapla WordPress", align="left", eye_color="accent-3"),
    para("On <strong>13 February 2027</strong>, Mumbai brings together developers, designers, creators, agencies, entrepreneurs, product builders, educators and business owners for one day of WordPress."),
    para("Whether you build sites for a living, run a business on WordPress or are just getting started, there is a place for you here."),
    buttons([button("About the event", "#")], justify="left"),
]
right = group("\n\n".join([
    fact_b("fact-calendar", "Sponsor applications close", "DD Mon 2026", "accent-1"),
    fact_b("fact-ticket", "Call for speakers opens", "DD Mon 2026", "accent-2"),
    fact_b("fact-train", "Tickets go on sale", "DD Mon 2026", "accent-3"),
]), gap=30)
sections.append(("02-key-facts", section_c([
    columns([column("\n\n".join(left), "55%"), column(right, "45%", valign="center")], valign="center")
], WASH_MARIGOLD, bgimage=(PNG + "tile-dots-marigold@2x.png", "120px auto", "0 0", "repeat"))))

sections.append(("03-sep-marigold", sep_b("marigold", "saffron")))

# 04 why attend on teal wash with white lattice; numerals in four colours
def point_c(n, colour, title, text):
    return group("\n\n".join([para(n, size="x-large", color=colour, weight=700),
                              group("\n\n".join([heading(title, 3, "large"), para(text)]), gap=20)]),
                 layout="flex", wrap="nowrap", valign="top", gap=30, cls="wcm-point")

points = [
    point_c("01", "accent-1", "Learn from the people who build it", "Two tracks of talks and workshops, from your first theme to contributing to core."),
    point_c("02", "accent-2", "Meet the Mumbai WordPress community", "Freelancers, agencies, product teams and first-timers in one room. The hallway track is half the value."),
    point_c("03", "accent-3", "Get hired, or hire", "Agencies and product companies from across the city come looking for people who know WordPress."),
    point_c("04", "accent-4", "Give something back", "Contributor Day the day before: mentors from every team, no experience needed."),
]
left = [header_b("Why attend", "Four reasons you will be glad you came", "Learn, connect, contribute", align="left"), group("\n\n".join(points), gap=40)]
right = image(PLACEHOLDER % ("960x1200", "006b78", "ffffff", "Photo+4:5"), "Attendees at the previous Mumbai WordPress meetup", ratio="4/5", radius="16px")
sections.append(("04-why-attend", section_c([
    columns([column("\n\n".join(left), "55%"), column(right, "45%", valign="center")])
], WASH_TEAL, bgimage=(PNG + "tile-lattice-light@2x.png", "120px auto", "0 0", "repeat"))))

sections.append(("05-sep-train", sep_b("train", "purple")))

# 06 get involved on white with the kolam tile; open chip in marigold
def involve(state, title, text, meta, btn):
    return column(card([
        chip_b("Open" if state == "open" else "Coming soon", state),
        heading(title, 3, "large"),
        para(text),
        para(meta, color="accent-4", size="small"),
        buttons([button(btn, "#", style="outline", color="accent-1", width=100)], justify="left"),
    ], gap=20))

sections.append(("06-get-involved", section([
    header_b("Get involved", "Help make WordCamp Mumbai happen", "Sponsor, speak, volunteer", eye_color="accent-3"),
    columns([
        involve("open", "Sponsor", "Support the event and meet the community.", "Closes DD Mon", "Become a sponsor"),
        involve("soon", "Speak", "Share what you know with WordPress people.", "Opens DD Mon", "Call for speakers"),
        involve("soon", "Volunteer", "Help run the day and make new friends.", "Opens DD Mon", "Call for volunteers"),
        involve("soon", "Media partner", "Help spread the word about WordCamp Mumbai.", "Opens DD Mon", "Call for media"),
    ]),
], bg="base", bgimage=(PNG + "tile-kolam-purple@2x.png", "120px auto", "0 0", "repeat"))))

sections.append(("07-sep-vadapav", sep_b("vadapav", "gold")))

# 08 numbers on purple wash; numerals in four colours; purple band
def stat_c(n, colour_hex_or_slug, label, text):
    if colour_hex_or_slug.startswith("#"):
        num = ('<!-- wp:paragraph {"style":{"color":{"text":"%s"},"typography":{"fontWeight":"700"}},"fontSize":"xx-large"} -->\n'
               '<p class="has-text-color has-xx-large-font-size" style="color:%s;font-weight:700">%s</p>\n<!-- /wp:paragraph -->') % (colour_hex_or_slug, colour_hex_or_slug, n)
    else:
        num = para(n, size="xx-large", color=colour_hex_or_slug, weight=700)
    return column(card([num, eyebrow(label, color="accent-4"), para(text)], bg="base", gap=20))

band = group("\n\n".join([
    group("\n\n".join([heading("Where the city meets the web", 3, "large", color="base"),
                       para("Experience Mumbai like never before: a city where deep-rooted heritage meets the cutting edge.", color="base")]), gap=20),
    buttons([button("Explore Mumbai", "#", bg="base", color="accent-3")], justify="right"),
]), layout="flex", justify="space-between", wrap="wrap", valign="center", align="wide", bg="accent-3", radius="16px",
    padding=(40, 40, 40, 40), gap=40, cls="wcm-band")
sections.append(("08-numbers", section_c([
    header_b("By the numbers", "One day, a whole community", eye_color="accent-3"),
    columns([
        stat_c("500+", "accent-1", "Attendees", "Developers, designers, marketers, students and site owners."),
        stat_c("20+", "accent-2", "Speakers", "Voices from Mumbai, India and the global WordPress community."),
        stat_c("2", "#E0552D", "Tracks", "Technical depth on one side, bold creative thinking on the other."),
        stat_c("1", "accent-3", "Contributor Day", "A day of giving back to the open source project that powers the web."),
    ]),
    band,
], WASH_PURPLE, bgimage=(PNG + "tile-waves-light@2x.png", "120px auto", "0 100%", "repeat-x"))))

# 09 sponsors on white with a marigold motif; logos on marigold-wash cards
def logo(name, colour):
    import json
    inner = image(PLACEHOLDER % ("600x400", "ffffff", colour, name), name.replace("+", " "), ratio="3/2", scale="contain", link="#")
    return column('<!-- wp:group {"className":"wcm-card","style":{"color":{"background":"%s"},"border":{"radius":"16px"},"spacing":{"padding":{"top":"var:preset|spacing|40","bottom":"var:preset|spacing|40","left":"var:preset|spacing|40","right":"var:preset|spacing|40"}}},"layout":{"type":"flow"}} -->\n<div class="wp-block-group wcm-card has-background" style="background-color:%s;border-radius:16px;padding-top:%s;padding-right:%s;padding-bottom:%s;padding-left:%s">%s</div>\n<!-- /wp:group -->' % (WASH_MARIGOLD, WASH_MARIGOLD, SP(40), SP(40), SP(40), SP(40), inner))

sections.append(("09-sponsors", section([
    header_b("Sponsors", "Made possible by our sponsors", body="WordCamp Mumbai runs on the generosity of the WordPress ecosystem. Here are the partners making 2027 happen."),
    group("\n\n".join([eyebrow("Blockbuster Sponsor – Platinum", "center", "accent-3"),
                       columns([logo("Sponsor+one", "0073aa"), logo("Sponsor+two", "006b78"), logo("Sponsor+three", "6d28d9")])]),
          layout="constrained", align="wide", gap=30),
    buttons([button("Become a sponsor", "#"), button("View sponsorship tiers", "#", style="outline", color="accent-1")]),
], bg="base", bgimage=(PNG + "motif-marigold@2x.png", "420px auto", "100% 0", "no-repeat"))))

# 10 venue on a full teal band, gold Kalam, base cards, base buttons
gallery_imgs = "\n\n".join(image(PLACEHOLDER % ("800x600", "0d1b2a", "ffffff", "Venue+%d" % i), "ATLAS SkillTech University, view %d" % i, ratio="4/3", radius="16px", size="large") for i in range(1, 5))
gallery = ('<!-- wp:gallery {"columns":2,"linkTo":"none"} -->\n<figure class="wp-block-gallery has-nested-images columns-2 is-cropped">%s</figure>\n<!-- /wp:gallery -->' % gallery_imgs)
facts = group("\n\n".join([
    fact_b("fact-calendar", "Date", "13 February 2027", "accent-1", "Contributor Day on 12 February"),
    fact_b("fact-pin", "Venue", "ATLAS SkillTech University", "accent-3", "Equinox Business Park, Kurla West, Mumbai 400070"),
    fact_b("fact-train", "Getting there", "Kurla station, 10 minutes by auto", "accent-1", "Metro and parking details closer to the date"),
]), gap=30)
map_img = image(PLACEHOLDER % ("1600x600", "E8F3F4", "546776", "Map+placeholder"), "Map showing ATLAS SkillTech University, Kurla West", ratio="16/6", radius="16px", link="https://maps.google.com/?q=ATLAS+SkillTech+University+Mumbai", cls="wcm-map")
sections.append(("10-venue", section([
    header_b("Venue", "When and where we gather", "Kurla, Mumbai", eye_color="base", h_color="base", tag_color="#E8B93B"),
    columns([column(facts, "45%", valign="center"), column(gallery, "55%")]),
    group(map_img, layout="constrained", align="wide"),
    buttons([button("Explore the venue", "#", bg="base", color="accent-2"), button("Get directions", "https://maps.google.com/?q=ATLAS+SkillTech+University+Mumbai", style="outline", color="base")]),
], bg="accent-2", bgimage=(PNG + "tile-waves-light@2x.png", "120px auto", "0 0", "repeat"), cls="wcm-teal-band")))

sections.append(("11-sep-chai", sep_b("chai", "saffron")))

# 12 updates on marigold wash with the white lattice
def post_card(date, cat, title, text):
    return column(card([
        image(PLACEHOLDER % ("1200x675", "6d28d9", "ffffff", "Featured+image"), "", ratio="16/9", radius="16px"),
        para("%s · %s" % (date, cat), color="accent-4", size="small"),
        heading('<a href="#">%s</a>' % title, 3, "large"),
        para(text),
    ], bg="base", gap=20))

query_site = open(os.path.join(os.path.dirname(HERE), "home", "sections", "12-updates.html")).read()
start = query_site.index("<!-- ds:site-only -->\n<!-- wp:query"); end = query_site.index("<!-- /ds:site-only -->", start) + len("<!-- /ds:site-only -->")
query = query_site[start:end].replace('"backgroundColor":"accent-5"', '"backgroundColor":"base"').replace("has-accent-5-background-color", "has-base-background-color") + "\n<!-- ds:preview-only -->\n%s\n<!-- /ds:preview-only -->" % columns([
    post_card("24 Sep 2026", "Sponsors", "Call for sponsors is now open", "Applications for WordCamp Mumbai 2027 sponsorships are open. Here is how to take part."),
    post_card("20 Sep 2026", "Announcements", "WordCamp Mumbai 2027 is happening on 13 February", "Save the date: the WordPress community meets at ATLAS SkillTech University."),
    post_card("18 Sep 2026", "Announcements", "Meet the organising team", "Say hello to the volunteers from the Mumbai WordPress community who are putting this together."),
])
subscribe = '''<!-- ds:site-only -->
<!-- wp:jetpack/subscriptions {"buttonText":"Subscribe","submitButtonText":"Subscribe","buttonBackgroundColor":"accent-3","textColor":"base","borderRadius":999,"padding":12,"spacing":8} /-->
<!-- /ds:site-only -->
<!-- ds:preview-only -->
%s
<!-- /ds:preview-only -->''' % group("\n\n".join([
    group(para("you@example.com", color="accent-4"), layout="flex", bg="accent-5", radius="999px", padding=(20, 20, 30, 30), gap=0, cls="wcm-fake-input"),
    buttons([button("Subscribe", "#", bg="accent-3", color="base")], justify="left"),
]), layout="flex", wrap="wrap", valign="center", gap=20)
header_row = group("\n\n".join([header_b("Latest news", "Updates from the team", align="left", eye_color="accent-3"), para('<a href="#">All updates</a>', weight=700)]),
                   layout="flex", justify="space-between", wrap="wrap", valign="bottom", align="wide", gap=30)
stay = group(columns([
    column(group("\n\n".join([heading("Stay in touch", 3, "x-large"), para("Speaker announcements, schedule and ticket news, straight to your inbox.")]), gap=20), "50%", valign="center"),
    column(subscribe, "50%", valign="center"),
], align=None, valign="center"), layout="constrained", align="wide", bg="base", radius="16px", padding=(40, 40, 40, 40), cls="wcm-card")
sections.append(("12-updates", section_c([header_row, query, stay], WASH_MARIGOLD, bgimage=(PNG + "tile-lattice-light@2x.png", "120px auto", "0 0", "repeat"))))

# 13 be part: teal-to-purple gradient, gold eyebrow, marigold garland, kolam strip after
bepart_inner = columns([
    column("\n\n".join([
        '<!-- wp:paragraph {"style":{"color":{"text":"#E8B93B"},"typography":{"textTransform":"uppercase","letterSpacing":"0.08em","fontStyle":"normal","fontWeight":"700"}},"fontSize":"small"} -->\n<p class="has-text-color has-small-font-size" style="color:#E8B93B;font-style:normal;font-weight:700;letter-spacing:0.08em;text-transform:uppercase">Be part of it</p>\n<!-- /wp:paragraph -->',
        heading("Be part of WordCamp Mumbai 2027", 2, "xx-large", color="base"),
        para("Join us in bringing the WordPress community together in Mumbai. Tell us you are interested and the team will get back to you.", color="base"),
        buttons([button("I am interested", "#", bg="base", color="accent-3"), button("mumbai@wordcamp.org", "mailto:mumbai@wordcamp.org", style="outline", color="base")], justify="left"),
    ]), "60%", valign="center"),
    column(group(image(LOGO, "WordCamp Mumbai 2027", width="220px"), layout="flex", justify="center", bg="base", radius="999px", padding=(40, 40, 40, 40), cls="wcm-logo-disc"), "40%", valign="center"),
], valign="center")
sections.append(("13-be-part", group("\n\n".join([group(bepart_inner, layout="constrained", padding=(70, 70), gap=40), strip("toran")]),
                                     layout="constrained", align="full", gradient=GRADIENT_B, cls="wcm-bepart", gap=0)))
sections.append(("14-strip-kolam", strip("kolam")))

# footer: identical to sample A
footer = open(os.path.join(os.path.dirname(HERE), "home", "footer.html")).read().rstrip("\n")

os.makedirs(os.path.join(HERE, "sections"), exist_ok=True)
for f in os.listdir(os.path.join(HERE, "sections")):
    os.remove(os.path.join(HERE, "sections", f))
for name, markup in sections:
    open(os.path.join(HERE, "sections", name + ".html"), "w").write(markup + "\n")
open(os.path.join(HERE, "block.html"), "w").write("\n\n".join("<!-- ==== %s ==== -->\n%s" % (n, m) for n, m in sections) + "\n")
open(os.path.join(HERE, "footer.html"), "w").write(footer + "\n")
open(os.path.join(HERE, "page-with-footer.html"), "w").write(open(os.path.join(HERE, "block.html")).read() + "\n<!-- ==== footer (template part) ==== -->\n" + footer + "\n")
print("wrote %d sections, block.html, footer.html" % len(sections))
