#!/usr/bin/env python3
"""Generate the WordCamp Mumbai 2027 sponsor pages as core-block markup.

Reads tiers.json (prices, benefits, comparison rows, FAQ, links) and writes
    call-for-sponsors/sections/NN-name.html, call-for-sponsors/block.html
    sponsorship-tiers/sections/NN-name.html, sponsorship-tiers/block.html
Helpers live in design-system/tools/blocks.py.
Run: python3 design-system/examples/sponsors/build.py
"""
import html
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(HERE)), "tools"))
from blocks import *  # noqa: E402,F401

D = json.load(open(os.path.join(HERE, "tiers.json")))
FORM, EMAIL = D["form"], D["email"]
EVENT_DATE = "13 February 2027"


def esc(s):
    return html.escape(s, quote=False)


# ------------------------------------------------------------- atoms --

def tagline(text):
    return ('<!-- wp:paragraph {"textColor":"accent-2","fontSize":"large","fontFamily":"kalam"} -->\n'
            '<p class="has-accent-2-color has-text-color has-large-font-size has-kalam-font-family">%s</p>\n<!-- /wp:paragraph -->' % text)


def checklist(items):
    """Core List block; the class wcm-check swaps the bullet for a teal tick (sponsors.css)."""
    return ('<!-- wp:list {"className":"wcm-check"} -->\n<ul class="wp-block-list wcm-check">%s</ul>\n<!-- /wp:list -->'
            % "".join('<!-- wp:list-item -->\n<li>%s</li>\n<!-- /wp:list-item -->' % i for i in items))  # items may carry <strong>


def details(q, paras):
    body = "\n\n".join(para(p) for p in paras)
    return ('<!-- wp:details {"className":"wcm-faq","style":{"border":{"radius":"16px"},"spacing":{"padding":{"top":"var:preset|spacing|40","bottom":"var:preset|spacing|40","left":"var:preset|spacing|40","right":"var:preset|spacing|40"}}},"backgroundColor":"accent-5"} -->\n'
            '<details class="wp-block-details wcm-faq has-accent-5-background-color has-background" style="border-radius:16px;padding-top:var(--wp--preset--spacing--40);padding-right:var(--wp--preset--spacing--40);padding-bottom:var(--wp--preset--spacing--40);padding-left:var(--wp--preset--spacing--40)"><summary>%s</summary>%s</details>\n<!-- /wp:details -->'
            % (esc(q), body))


def table(head, rows):
    th = "".join("<th>%s</th>" % esc(h) for h in head)
    tr = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % esc(c) for c in r) for r in rows)
    return ('<!-- wp:table {"align":"wide","className":"is-style-stripes wcm-compare"} -->\n'
            '<figure class="wp-block-table alignwide is-style-stripes wcm-compare"><table class="has-fixed-layout"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></figure>\n<!-- /wp:table -->' % (th, tr))


def point(n, title, text):
    return group("\n\n".join([
        para(n, size="x-large", color="accent-1", weight=700),
        group("\n\n".join([heading(title, 3, "large"), para(text)]), gap=20),
    ]), layout="flex", wrap="nowrap", valign="top", gap=30, cls="wcm-point")


def stat(n, label, text):
    return column(card([
        para(n, size="xx-large", color="accent-1", weight=700),
        eyebrow(label, color="accent-4"),
        para(text),
    ], bg="accent-5", gap=20))


def tier_card(t, full, bg):
    """Tier card: icon, eyebrow (level), H3 (name), price, $ meta, line, checklist, best-for, button.
    full=True lists every benefit (tiers page); False lists the four headline ones plus a link."""
    inner = [
        image(t["icon"], "%s – %s sponsor" % (t["name"], t["level"]), width="96px", radius="16px"),
        group("\n\n".join([
            eyebrow(t["level"]),
            heading(esc(t["name"]), 3, "large"),
        ]), gap=0),
        para("%s (%s)" % (t["inr"], t["usd"]), size="xx-large", color="accent-1", weight=700),
        para(esc(t["line"])),
        checklist(t["benefits"] if full else t["headline"]),
    ]
    if full:
        inner.append(para("<strong>Best for:</strong> " + esc(t["best_for"]), size="small", color="accent-4"))
    else:
        inner.append(para('<a href="%s#%s">All %s benefits →</a>' % (D["tiers_page"], t["slug"], t["name"]), weight=700))
    inner.append(buttons([button("Become a sponsor", FORM, style="outline", color="accent-1", width=100)], justify="left"))
    cls = "wcm-card wcm-tier" + (" wcm-tier--featured" if t["featured"] else "")
    j = {"className": cls, "style": {"border": {"radius": "16px"}, "spacing": {"padding": {k: SPJ(40) for k in ("top", "bottom", "left", "right")}, "blockGap": SPJ(20)}}, "backgroundColor": bg, "layout": {"type": "default"}}
    st = ["border-radius:16px"] + ["padding-%s:%s" % (k, SP(40)) for k in ("top", "right", "bottom", "left")]
    cl = ["wp-block-group", cls, "has-%s-background-color" % bg, "has-background"]
    if t["featured"]:
        # 2px Accent 1 border for the headline tier (Group → Border in the editor)
        j["style"]["border"]["width"] = "2px"
        j["borderColor"] = "accent-1"
        st.insert(0, "border-width:2px")
        cl.insert(2, "has-border-color")
        cl.insert(3, "has-accent-1-border-color")
    anchor = ' id="%s"' % t["slug"] if full else ""
    if full:
        j["anchor"] = t["slug"]
    return '<!-- wp:group %s -->\n<div class="%s"%s style="%s">%s</div>\n<!-- /wp:group -->' % (
        json.dumps(j, separators=(",", ":"), ensure_ascii=False), " ".join(cl), anchor, ";".join(st), "\n\n".join(inner))


def tier_row(full, bg):
    return columns([column(tier_card(t, full, bg)) for t in D["tiers"]])


def gradient_band(h2, text, primary, secondary):
    inner = group("\n\n".join([
        heading(h2, 2, "x-large", align="center", color="base"),
        para(text, align="center", color="base"),
        buttons([button(primary[0], primary[1], bg="base", color="accent-3"), button(secondary[0], secondary[1], style="outline", color="base")]),
    ]), layout="constrained", padding=(70, 70), gap=30)
    return group(inner, layout="constrained", align="full", gradient=GRADIENT, cls="wcm-band-gradient", gap=0)


# ------------------------------------------------- call for sponsors --

cfs = []

intro_left = "\n\n".join([
    group("\n\n".join([
        # H1 matches the page title ("Call for Sponsors") for search; the old headline becomes the tagline
        eyebrow("WordCamp Mumbai 2027 · %s" % EVENT_DATE),
        heading("Call for Sponsors", 1, "xx-large"),
        tagline("Help build what comes next in WordPress"),
    ]), gap=20),
    para("On <strong>%s</strong>, Mumbai becomes a meeting point for developers, designers, creators, agencies, entrepreneurs, product builders, educators and business owners who build, use, support and shape the web with WordPress." % EVENT_DATE),
    para("We are inviting organisations that believe in open source, community and the people building the future of the web to join us as sponsors."),
    buttons([button("Become a sponsor", FORM), button("See the tiers", D["tiers_page"], style="outline", color="accent-1")], justify="left"),
])
intro_right = image(D["poster"], "Call for sponsors: WordCamp Mumbai 2027, %s, ATLAS SkillTech University" % EVENT_DATE, ratio="16/9", radius="16px")
cfs.append(("01-intro", section([
    columns([column(intro_left, "55%"), column(intro_right, "45%", valign="center")], valign="center"),
    columns([
        stat("300+", "Attendees", "Developers, designers, marketers, students and site owners."),
        stat("1", "Day", "%s at ATLAS SkillTech University, Kurla." % EVENT_DATE),
        stat("100%", "Volunteer-run", "No one is paid. Sponsors cover what tickets don’t."),
        stat("43%", "Of the web", "Runs on WordPress. The people in this room keep it that way."),
    ]),
], bg=None, bgimage=(PNG + "motif-gateway@2x.png", "320px auto", "100% 100%", "no-repeat"))))

cfs.append(("02-sep-train", separator("train")))

def why(n, title, text):
    """Why-sponsor card: Base card with the fact-card's 4px Accent 2 left edge; the numeral
    sits inside the H3 as an inline Accent 1 highlight (the editor's Highlight format)."""
    # the editor's Highlight format also writes style="background-color:rgba(0, 0, 0, 0)", which
    # WordCamp's sanitiser strips on save, so sponsors.css clears the <mark> background instead
    h3 = '<mark class="has-inline-color has-accent-1-color">%s</mark> %s' % (n, title)
    return column(group("\n\n".join([heading(h3, 3, "large"), para(text)]), bg="base", radius="16px",
                        padding=(40, 40, 40, 40), gap=20, cls="wcm-card wcm-why", border_left=("accent-2", "4px")))

WHY = [
    ("01", "High-impact brand visibility", "Showcase your tools and services throughout the single-day main conference."),
    ("02", "Direct lead generation", "Engage users and decision-makers through booth interactions, demonstrations and networking."),
    ("03", "Access to top-tier talent", "Connect with WordPress engineering and product talent across enterprise, plugins and modern workflows."),
    ("04", "Community leadership", "Support open-source education and collaboration through a volunteer-led initiative."),
    ("05", "Limited availability", "Packages are structured for focused visibility and are available first-come, first-served."),
    ("06", "Early advantage", "Secure a preferred tier early to maximise promotional runway and pre-event digital benefits."),
]
cfs.append(("03-why", section([
    section_header("Why sponsor", "Why sponsor WordCamp Mumbai 2027?", body="WordCamps are non-commercial and volunteer-run. Tickets cover a fraction of the cost; sponsors cover the rest, and get the room’s attention for it."),
    columns([why(*w) for w in WHY[:3]]),
    columns([why(*w) for w in WHY[3:]]),
], bg="accent-5", bgimage=(PNG + "tile-lattice-light@2x.png", "120px auto", "0 0", "repeat"))))

cfs.append(("04-tiers", section([
    section_header("The tiers", "Blockbuster, Megahit, Superhit", "Three ways to be on the bill", body="Every tier includes sponsor space, passes for your team, your logo and link on the website and swag in the attendee kit. The full benefit lists and a side-by-side table are on the tiers page."),
    tier_row(full=False, bg="accent-5"),
    buttons([button("Become a sponsor", FORM), button("Compare the tiers", D["tiers_page"] + "#compare", style="outline", color="accent-1")]),
], bg=None, bgimage=(PNG + "motif-palm@2x.png", "420px auto", "0 100%", "no-repeat"))))

steps = group("\n\n".join([
    point("01", "Tell us your tier", "Fill in the sponsorship form with your company details and the package you have in mind. Not sure? Say so; we will help you choose."),
    point("02", "WordCamp Central invoices you", "Sponsorship payments go through WordCamp Central’s official process, never through the organisers or personal channels."),
    point("03", "Send us your logo", "We add you to the website, the signage and the announcements, and confirm your passes and sponsor space."),
]), gap=40)
cfs.append(("05-how", section([
    columns([
        column("\n\n".join([section_header("How it works", "Three steps to being on the banner", align="left"), steps]), "55%"),
        column(image(D["booth"], "A sponsor booth at WordCamp Mumbai, with attendees talking to the team", ratio="1", radius="16px"), "45%", valign="center"),
    ]),
], bg="accent-5")))

cfs.append(("06-faq", section([
    section_header("FAQ", "Questions sponsors ask", body="If yours is not here, the sponsor team is one email away."),
    group("\n\n".join(details(q, ps) for q, ps in D["faq"]), gap=30),
], bg=None, bgimage=(PNG + "tile-lattice-blue@2x.png", "120px auto", "0 0", "repeat"))))

cfs.append(("07-ready", gradient_band("Ready to partner with us?", "Fill in the short sponsor application and the team will get back to you within two working days.",
                                      ("Become a sponsor", FORM), (EMAIL, "mailto:" + EMAIL))))

# ------------------------------------------------- sponsorship tiers --

tiers = []

tiers.append(("01-intro", section([
    group("\n\n".join([
        eyebrow("WordCamp Mumbai 2027 · %s" % EVENT_DATE),
        heading("Sponsorship Tiers", 1, "xx-large"),
        tagline("Blockbuster, Megahit, Superhit"),
    ]), gap=20),
    para("Three tiers, named the way Mumbai names its hits. Every tier includes sponsor space at the event, passes for your team, your logo and link on the website and swag in the attendee kit. Payments are handled by WordCamp Central."),
    buttons([button("Become a sponsor", FORM), button("Compare the tiers", "#compare", style="outline", color="accent-1")], justify="left"),
], bg=None, bgimage=(PNG + "motif-gateway@2x.png", "320px auto", "100% 100%", "no-repeat"))))

tiers.append(("02-tiers", section([
    section_header("The tiers", "Everything each tier includes"),
    tier_row(full=True, bg="base"),
], bg="accent-5", bgimage=(PNG + "tile-lattice-light@2x.png", "120px auto", "0 0", "repeat"))))

tiers.append(("03-compare", section([
    section_header("Compare", "The tiers, side by side", body="The quick version is above; this is the full picture."),
    table(["What you get", "Blockbuster · Platinum", "Megahit · Gold", "Superhit · Silver"], D["compare"]),
], bg=None, anchor="compare")))

facts = "\n\n".join([
    columns([
        column(fact_card("fact-ticket", "Payment", "Through WordCamp Central", "Never through the organisers or personal channels", bg="base")),
        column(fact_card("fact-calendar", "Speaking", "Not part of any tier", "Talks are selected on merit through the call for speakers", bg="base")),
    ]),
    columns([
        column(fact_card("fact-pin", "In kind", "Products and services welcome", "We agree a value and match it with benefits", bg="base")),
        column(fact_card("fact-train", "Leads", "Conversations, not lists", "We never share attendee contact details", bg="base")),
    ]),
])
tiers.append(("04-good-to-know", section([
    section_header("Good to know", "Before you choose"),
    facts,
], bg="accent-5")))

tiers.append(("05-callout", section([
    section_header("Not sure which tier?", "The sponsor team will help you choose", body="Tell us what you want from the day, hiring, visibility or simply backing the community, and we will suggest a fit."),
    buttons([button("Become a sponsor", FORM), button("Write to " + EMAIL, "mailto:" + EMAIL, style="outline", color="accent-1")]),
], bg=None)))

# --------------------------------------------------------------- write --

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

write("call-for-sponsors", cfs)
write("sponsorship-tiers", tiers)

# the library component: three teaser cards on sky wash, one full card on white
comp = os.path.join(os.path.dirname(os.path.dirname(HERE)), "components", "marketing", "tier-card")
with open(os.path.join(comp, "block.html"), "w") as fh:
    fh.write(tier_row(full=False, bg="accent-5") + "\n\n" + group(tier_card(D["tiers"][2], True, "accent-5"), layout="constrained") + "\n")
print("wrote components/marketing/tier-card/block.html")
