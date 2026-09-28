#!/usr/bin/env python3
"""Generate the WordCamp Mumbai 2027 home page (sample A: blue rhythm) as core-block markup.

Writes sections/NN-name.html, block.html (paste into the home page's code editor)
and footer.html (paste into the Footer template part). Helpers live in
design-system/tools/blocks.py. Run: python3 design-system/examples/home/build.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(HERE)), "tools"))
from blocks import *  # noqa: E402,F401

# ------------------------------------------------------------- sections --

PLACEHOLDER = "https://placehold.co/%s/%s/%s.png?text=%s"

sections = []

# 01 pattern strip under the hero
sections.append(("01-strip-train", strip("train")))

# 02 key facts, two columns, white, gateway motif
left = [
    section_header("Key facts", "Mumbai becomes a meeting point for the WordPress community", "Aamchi Mumbai, Aapla WordPress", align="left"),
    para("On <strong>13 February 2027</strong>, Mumbai brings together developers, designers, creators, agencies, entrepreneurs, product builders, educators and business owners for one day of WordPress."),
    para("Whether you build sites for a living, run a business on WordPress or are just getting started, there is a place for you here."),
    buttons([button("About the event", "#", style="outline", color="accent-1")], justify="left"),
]
right = group("\n\n".join([
    fact_card("fact-calendar", "Sponsor applications close", "DD Mon 2026"),
    fact_card("fact-ticket", "Call for speakers opens", "DD Mon 2026"),
    fact_card("fact-train", "Tickets go on sale", "DD Mon 2026"),
]), gap=30)
sections.append(("02-key-facts", section([
    columns([column("\n\n".join(left), "55%"), column(right, "45%", valign="center")], valign="center")
], bg="base", bgimage=(PNG + "motif-gateway@2x.png", "320px auto", "100% 100%", "no-repeat"))))

# S separator marigold
sections.append(("03-sep-marigold", separator("marigold")))

# 04 why attend: numbered points left, photo right, sky wash lattice
def point(n, title, text):
    return group("\n\n".join([
        para(n, size="x-large", color="accent-1", weight=700),
        group("\n\n".join([heading(title, 3, "large"), para(text)]), gap=20),
    ]), layout="flex", wrap="nowrap", valign="top", gap=30, cls="wcm-point")

points = [
    point("01", "Learn from the people who build it", "Two tracks of talks and workshops, from your first theme to contributing to core."),
    point("02", "Meet the Mumbai WordPress community", "Freelancers, agencies, product teams and first-timers in one room. The hallway track is half the value."),
    point("03", "Get hired, or hire", "Agencies and product companies from across the city come looking for people who know WordPress."),
    point("04", "Give something back", "Contributor Day the day before: mentors from every team, no experience needed."),
]
left = [section_header("Why attend", "Four reasons you will be glad you came", align="left"), group("\n\n".join(points), gap=40)]
right = image(PLACEHOLDER % ("960x1200", "0073aa", "ffffff", "Photo+4:5"), "Attendees at the previous Mumbai WordPress meetup", ratio="4/5", radius="16px")
sections.append(("04-why-attend", section([
    columns([column("\n\n".join(left), "55%"), column(right, "45%", valign="center")])
], bg="accent-5", bgimage=(PNG + "tile-lattice-light@2x.png", "120px auto", "0 0", "repeat"))))

sections.append(("05-sep-train", separator("train")))

# 06 get involved, white
def involve(state, title, text, meta, btn):
    return column(card([
        chip("Open" if state == "open" else "Coming soon", state),
        heading(title, 3, "large"),
        para(text),
        para(meta, color="accent-4", size="small"),
        buttons([button(btn, "#", style="outline", color="accent-1", width=100)], justify="left"),
    ], gap=20))

sections.append(("06-get-involved", section([
    section_header("Get involved", "Help make WordCamp Mumbai happen"),
    columns([
        involve("open", "Sponsor", "Support the event and meet the community.", "Closes DD Mon", "Become a sponsor"),
        involve("soon", "Speak", "Share what you know with WordPress people.", "Opens DD Mon", "Call for speakers"),
        involve("soon", "Volunteer", "Help run the day and make new friends.", "Opens DD Mon", "Call for volunteers"),
        involve("soon", "Media partner", "Help spread the word about WordCamp Mumbai.", "Opens DD Mon", "Call for media"),
    ]),
], bg="base")))

sections.append(("07-sep-vadapav", separator("vadapav")))

# 08 by the numbers + dark strip, sky wash waves
def stat(n, label, text):
    return column(card([
        para(n, size="xx-large", color="accent-1", weight=700),
        eyebrow(label, color="accent-4"),
        para(text),
    ], bg="base", gap=20))

dark = group("\n\n".join([
    group("\n\n".join([heading("Where the city meets the web", 3, "large", color="base"),
                       para("Experience Mumbai like never before: a city where deep-rooted heritage meets the cutting edge.", color="base")]), gap=20),
    buttons([button("Explore Mumbai", "#", bg="base", color="contrast")], justify="right"),
]), layout="flex", justify="space-between", wrap="wrap", valign="center", align="wide", bg="contrast", radius="16px",
    padding=(40, 40, 40, 40), gap=40, cls="wcm-band")
sections.append(("08-numbers", section([
    section_header("By the numbers", "One day, a whole community"),
    columns([
        stat("500+", "Attendees", "Developers, designers, marketers, students and site owners."),
        stat("20+", "Speakers", "Voices from Mumbai, India and the global WordPress community."),
        stat("2", "Tracks", "Technical depth on one side, bold creative thinking on the other."),
        stat("1", "Contributor Day", "A day of giving back to the open source project that powers the web."),
    ]),
    dark,
], bg="accent-5", bgimage=(PNG + "tile-waves-light@2x.png", "120px auto", "0 100%", "repeat-x"))))

# 09 sponsors, white, palm motif
def logo(name, colour):
    return column(group(image(PLACEHOLDER % ("600x400", "ffffff", colour, name), name.replace("+", " "), ratio="3/2", scale="contain", link="#"),
                        bg="accent-5", radius="16px", padding=(40, 40, 40, 40), cls="wcm-card"))

sections.append(("09-sponsors", section([
    section_header("Sponsors", "Made possible by our sponsors", body="WordCamp Mumbai runs on the generosity of the WordPress ecosystem. Here are the partners making 2027 happen."),
    group("\n\n".join([
        eyebrow("Blockbuster Sponsor – Platinum", "center"),
        columns([logo("Sponsor+one", "0073aa"), logo("Sponsor+two", "006b78"), logo("Sponsor+three", "546776")]),
    ]), layout="constrained", align="wide", gap=30),
    buttons([button("Become a sponsor", "#"), button("View sponsorship tiers", "#", style="outline", color="accent-1")]),
], bg="base", bgimage=(PNG + "motif-palm@2x.png", "420px auto", "0 100%", "no-repeat"))))

# 10 venue, sky wash
gallery_imgs = "\n\n".join(image(PLACEHOLDER % ("800x600", "546776", "ffffff", "Venue+%d" % i), "ATLAS SkillTech University, view %d" % i, ratio="4/3", radius="16px", size="large") for i in range(1, 5))
gallery = ('<!-- wp:gallery {"columns":2,"linkTo":"none"} -->\n<figure class="wp-block-gallery has-nested-images columns-2 is-cropped">%s</figure>\n<!-- /wp:gallery -->' % gallery_imgs)
facts = group("\n\n".join([
    fact_card("fact-calendar", "Date", "13 February 2027", "Contributor Day on 12 February", bg="base"),
    fact_card("fact-pin", "Venue", "ATLAS SkillTech University", "Equinox Business Park, Kurla West, Mumbai 400070", bg="base"),
    fact_card("fact-train", "Getting there", "Kurla station, 10 minutes by auto", "Metro and parking details closer to the date", bg="base"),
]), gap=30)
map_img = image(PLACEHOLDER % ("1600x600", "f2f7fa", "546776", "Map+placeholder"), "Map showing ATLAS SkillTech University, Kurla West", ratio="16/6", radius="16px", link="https://maps.google.com/?q=ATLAS+SkillTech+University+Mumbai", cls="wcm-map")
sections.append(("10-venue", section([
    section_header("Venue", "When and where we gather", "Kurla, Mumbai"),
    columns([column(facts, "45%", valign="center"), column(gallery, "55%")]),
    group(map_img, layout="constrained", align="wide"),
    buttons([button("Explore the venue", "#"), button("Get directions", "https://maps.google.com/?q=ATLAS+SkillTech+University+Mumbai", style="outline", color="accent-1")]),
], bg="accent-5")))

sections.append(("11-sep-chai", separator("chai")))

# 12 updates + stay in touch, white lattice
def post_card(date, cat, title, text):
    return column(card([
        image(PLACEHOLDER % ("1200x675", "0073aa", "ffffff", "Featured+image"), "", ratio="16/9", radius="16px"),
        para("%s · %s" % (date, cat), color="accent-4", size="small"),
        heading('<a href="#">%s</a>' % title, 3, "large"),
        para(text),
    ], gap=20))

query = '''<!-- ds:site-only -->
<!-- wp:query {"queryId":1,"query":{"perPage":3,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","author":"","search":"","exclude":[],"sticky":"exclude","inherit":false},"align":"wide","layout":{"type":"default"}} -->
<div class="wp-block-query alignwide"><!-- wp:post-template {"style":{"spacing":{"blockGap":"var:preset|spacing|30"}},"layout":{"type":"grid","columnCount":3}} -->
<!-- wp:group {"className":"wcm-card","style":{"border":{"radius":"16px"},"spacing":{"padding":{"top":"var:preset|spacing|40","bottom":"var:preset|spacing|40","left":"var:preset|spacing|40","right":"var:preset|spacing|40"},"blockGap":"var:preset|spacing|20"}},"backgroundColor":"accent-5","layout":{"type":"default"}} -->
<div class="wp-block-group wcm-card has-accent-5-background-color has-background" style="border-radius:16px;padding-top:var(--wp--preset--spacing--40);padding-right:var(--wp--preset--spacing--40);padding-bottom:var(--wp--preset--spacing--40);padding-left:var(--wp--preset--spacing--40)"><!-- wp:post-featured-image {"aspectRatio":"16/9","style":{"border":{"radius":"16px"}}} /-->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|20"}},"layout":{"type":"flex","flexWrap":"nowrap"}} -->
<div class="wp-block-group"><!-- wp:post-date {"textColor":"accent-4","fontSize":"small"} /-->

<!-- wp:post-terms {"term":"category","textColor":"accent-4","fontSize":"small"} /--></div>
<!-- /wp:group -->

<!-- wp:post-title {"level":3,"isLink":true,"fontSize":"large"} /-->

<!-- wp:post-excerpt {"excerptLength":20} /--></div>
<!-- /wp:group -->
<!-- /wp:post-template --></div>
<!-- /wp:query -->
<!-- /ds:site-only -->
<!-- ds:preview-only -->
%s
<!-- /ds:preview-only -->''' % columns([
    post_card("24 Sep 2026", "Sponsors", "Call for sponsors is now open", "Applications for WordCamp Mumbai 2027 sponsorships are open. Here is how to take part."),
    post_card("20 Sep 2026", "Announcements", "WordCamp Mumbai 2027 is happening on 13 February", "Save the date: the WordPress community meets at ATLAS SkillTech University."),
    post_card("18 Sep 2026", "Announcements", "Meet the organising team", "Say hello to the volunteers from the Mumbai WordPress community who are putting this together."),
])

subscribe = '''<!-- ds:site-only -->
<!-- wp:jetpack/subscriptions {"buttonText":"Subscribe","submitButtonText":"Subscribe","buttonBackgroundColor":"accent-1","textColor":"base","borderRadius":999,"padding":12,"spacing":8} /-->
<!-- /ds:site-only -->
<!-- ds:preview-only -->
%s
<!-- /ds:preview-only -->''' % group("\n\n".join([
    group(para("you@example.com", color="accent-4"), layout="flex", bg="base", radius="999px", padding=(20, 20, 30, 30), gap=0, cls="wcm-fake-input"),
    buttons([button("Subscribe", "#")], justify="left"),
]), layout="flex", wrap="wrap", valign="center", gap=20)

header_row = group("\n\n".join([
    section_header("Latest news", "Updates from the team", align="left"),
    para('<a href="#">All updates</a>', weight=700),
]), layout="flex", justify="space-between", wrap="wrap", valign="bottom", align="wide", gap=30)

stay = group(columns([
    column(group("\n\n".join([heading("Stay in touch", 3, "x-large"), para("Speaker announcements, schedule and ticket news, straight to your inbox.")]), gap=20), "50%", valign="center"),
    column(subscribe, "50%", valign="center"),
], align=None, valign="center"), layout="constrained", align="wide", bg="accent-5", radius="16px", padding=(40, 40, 40, 40), cls="wcm-card")

sections.append(("12-updates", section([header_row, query, stay], bg="base",
                                         bgimage=(PNG + "tile-lattice-blue@2x.png", "120px auto", "0 0", "repeat"))))

# 13 be part: gradient band, logo, toran strip
bepart_inner = columns([
    column("\n\n".join([
        eyebrow("Be part of it", color="base"),
        heading("Be part of WordCamp Mumbai 2027", 2, "xx-large", color="base"),
        para("Join us in bringing the WordPress community together in Mumbai. Tell us you are interested and the team will get back to you.", color="base"),
        buttons([button("I am interested", "#", bg="base", color="accent-3"), button("mumbai@wordcamp.org", "mailto:mumbai@wordcamp.org", style="outline", color="base")], justify="left"),
    ]), "60%", valign="center"),
    column(group(image(LOGO, "WordCamp Mumbai 2027", width="220px"), layout="flex", justify="center", bg="base", radius="999px", padding=(40, 40, 40, 40), cls="wcm-logo-disc"), "40%", valign="center"),
], valign="center")
bepart = group("\n\n".join([
    group(bepart_inner, layout="constrained", padding=(70, 70), gap=40),
    strip("toran"),
]), layout="constrained", align="full", gradient=GRADIENT, cls="wcm-bepart", gap=0)
sections.append(("13-be-part", bepart))

# ------------------------------------------------------------- footer --

nav_site = '<!-- wp:navigation {"overlayMenu":"never","textColor":"contrast","style":{"typography":{"fontWeight":"700"}},"layout":{"type":"flex","justifyContent":"center"}} /-->'
nav_preview = ('<!-- ds:preview-only -->\n<nav class="wp-block-navigation" style="font-weight:700"><ul>%s</ul></nav>\n<!-- /ds:preview-only -->'
               % "".join('<li><a href="#">%s</a></li>' % t for t in ("About", "Schedule", "Sponsors", "Speakers", "Venue", "Contact")))
social_site = ('<!-- wp:social-links {"iconColor":"base","iconColorValue":"#FFFFFF","iconBackgroundColor":"accent-1","iconBackgroundColorValue":"#0073aa","size":"has-normal-icon-size","layout":{"type":"flex","justifyContent":"center"}} -->\n'
               '<ul class="wp-block-social-links has-normal-icon-size has-icon-color has-icon-background-color">'
               '<!-- wp:social-link {"url":"#","service":"x"} /-->\n<!-- wp:social-link {"url":"#","service":"instagram"} /-->\n<!-- wp:social-link {"url":"#","service":"linkedin"} /-->\n<!-- wp:social-link {"url":"#","service":"youtube"} /-->'
               '</ul>\n<!-- /wp:social-links -->')
social_preview = ('<!-- ds:preview-only -->\n<ul class="wp-block-social-links is-layout-flex is-content-justification-center">%s</ul>\n<!-- /ds:preview-only -->'
                  % "".join('<li class="wp-social-link has-accent-1-background-color has-base-color" style="font-weight:700;font-size:14px"><a href="#">%s</a></li>' % t for t in ("X", "In", "Li", "Yt")))

footer_inner = group("\n\n".join([
    '<!-- ds:site-only -->\n' + nav_site + '\n<!-- /ds:site-only -->', nav_preview,
    '<!-- ds:site-only -->\n' + social_site + '\n<!-- /ds:site-only -->', social_preview,
    para('WordCamp Mumbai 2027 · <a href="#">Code of conduct</a> · <a href="#">Privacy</a> · Proudly powered by <a href="https://wordpress.org/">WordPress</a>', align="center", color="accent-4", size="small"),
]), layout="constrained", gap=30, padding=(50,))

# Footer: a full-width Group with the scene as its block background (Cover size, centre
# bottom), exactly as the live site does it. The class wcm-footer-scene is styled by the
# FOOTER SCENE fence already in hero.css (bottom padding clamp(300px, 42vw, 620px) and a
# portrait crop on phones), so no new CSS is needed.
footer = group(footer_inner, layout="constrained", align="full", cls="wcm-footer-scene", gap=0,
               bgimage=(CDN + "img/footer-stage.jpg", "cover", "50% 100%", "no-repeat"))

# --------------------------------------------------------------- write --

os.makedirs(os.path.join(HERE, "sections"), exist_ok=True)
for f in os.listdir(os.path.join(HERE, "sections")):
    os.remove(os.path.join(HERE, "sections", f))
for name, markup in sections:
    with open(os.path.join(HERE, "sections", name + ".html"), "w") as fh:
        fh.write(markup + "\n")
with open(os.path.join(HERE, "block.html"), "w") as fh:
    fh.write("\n\n".join("<!-- ==== %s ==== -->\n%s" % (n, m) for n, m in sections) + "\n")
with open(os.path.join(HERE, "footer.html"), "w") as fh:
    fh.write(footer + "\n")
# the page preview includes the footer so the whole home page renders in one go
with open(os.path.join(HERE, "page-with-footer.html"), "w") as fh:
    fh.write(open(os.path.join(HERE, "block.html")).read() + "\n<!-- ==== footer (template part) ==== -->\n" + footer + "\n")
print("wrote %d sections, block.html, footer.html" % len(sections))
