#!/usr/bin/env python3
"""Generate the site footer (the Footer template part) for WordCamp Mumbai 2027.

Modelled on the WordCamp Bengaluru 2026 footer: a closing call to action, a
brand column beside three link columns (Event, Get Involved, Community), a
follow + subscribe row and the credit line. Core blocks only. The three menus
are Navigation posts on the site (Footer: Event 1353, Footer: Get Involved
1354, Footer: Community 1355); previews show static stand-ins. Writes
block.html (paste into Appearance → Editor → Patterns → Footer → code editor).
Run: python3 design-system/examples/footer/build.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(HERE)), "tools"))
from blocks import *  # noqa: E402,F401

EVENT_DATE = "13 February 2027"
EMAIL = "mumbai@wordcamp.org"
MENUS = {"event": 1353, "involved": 1354, "community": 1355}
SOCIAL = [("x", "https://x.com/wcmumbai"), ("instagram", "https://www.instagram.com/wpmumbai/"),
          ("linkedin", "https://www.linkedin.com/company/wpmumbai/"), ("facebook", "https://www.facebook.com/WPMumbai.org/")]
PREVIEW_LINKS = {
    "event": [("About", "/2027/about-us/"), ("News", "/2027/news/"), ("Organizers", "/2027/organizers/"), ("Code of Conduct", "/2027/code-of-conduct/")],
    "involved": [("Call for Sponsors", "/2027/call-for-sponsors/", "wcm-nav-open"), ("Call for Speakers", "/2027/call-for-speakers/", "wcm-nav-open"), ("Tickets", "/2027/tickets/")],
    "community": [("Mumbai Meetup", "https://www.meetup.com/wordpress-mumbai/"), ("Contact", "/2027/contact/")],
}


def site_only(site, preview):
    return "<!-- ds:site-only -->\n%s\n<!-- /ds:site-only -->\n<!-- ds:preview-only -->\n%s\n<!-- /ds:preview-only -->" % (site, preview)


def menu(key):
    site = ('<!-- wp:navigation {"ref":%d,"overlayMenu":"never","className":"wcm-footer-nav","style":{"spacing":{"blockGap":"var:preset|spacing|20"}},"layout":{"type":"flex","orientation":"vertical"}} /-->' % MENUS[key])
    items = "".join('<li class="wp-block-navigation-item wp-block-navigation-link%s"><a class="wp-block-navigation-item__content" href="%s">%s</a></li>'
                    % ((" " + l[2]) if len(l) > 2 else "", l[1], l[0]) for l in PREVIEW_LINKS[key])
    preview = '<nav class="wp-block-navigation wcm-footer-nav is-vertical is-layout-flex" style="flex-direction:column;align-items:flex-start;gap:var(--wp--preset--spacing--20)"><ul class="wp-block-navigation__container is-vertical" style="display:flex;flex-direction:column;align-items:flex-start;gap:var(--wp--preset--spacing--20);list-style:none;margin:0;padding:0">%s</ul></nav>' % items
    return site_only(site, preview)


def rule():
    return '<!-- wp:separator {"align":"wide","className":"is-style-wide wcm-footer-rule","backgroundColor":"accent-5"} -->\n<hr class="wp-block-separator alignwide has-text-color has-accent-5-color has-alpha-channel-opacity has-accent-5-background-color has-background is-style-wide wcm-footer-rule"/>\n<!-- /wp:separator -->'


def tagline(text):
    return ('<!-- wp:paragraph {"textColor":"accent-2","fontFamily":"kalam"} -->\n'
            '<p class="has-accent-2-color has-text-color has-kalam-font-family">%s</p>\n<!-- /wp:paragraph -->' % text)


# 1. closing call to action ---------------------------------------------------
cta = group("\n\n".join([
    group("\n\n".join([eyebrow("%s · Mumbai" % EVENT_DATE), heading("Come spend a day with us.", 2, "x-large")]), gap=20),
    buttons([button("Get your ticket", "/2027/tickets/"), button("Get involved", "/2027/call-for-speakers/", style="outline", color="accent-1")], justify="right"),
]), layout="flex", wrap="wrap", justify="space-between", valign="center", align="wide", cls="wcm-footer-cta", gap=30)

# 2. brand and the three link columns -----------------------------------------------
logo_site = '<!-- wp:site-logo {"width":64,"shouldSyncIcon":false} /-->'
logo_preview = image(LOGO, "WordCamp Mumbai 2027", width="64px")
brand = "\n\n".join([
    group("\n\n".join([
        site_only(logo_site, logo_preview),
        group("\n\n".join([para("WordCamp Mumbai 2027", size="large", weight=700), tagline("Aamchi Mumbai, Aapla WordPress")]), gap=0),
    ]), layout="flex", wrap="nowrap", valign="center", gap=30, cls="wcm-footer-lockup"),
    para("The Mumbai WordPress community's own gathering: a day of talks, workshops, food and the hallway track."),
    para('<a href="/2027/venue/">ATLAS SkillTech University, Kurla West</a>', size="small", color="accent-4"),
])
col_event = "\n\n".join([eyebrow("Event"), menu("event")])
col_involved = "\n\n".join([eyebrow("Get involved"), menu("involved")])
col_community = "\n\n".join([
    eyebrow("Community"), menu("community"),
    group("\n\n".join([eyebrow("Write to us"), para('<a href="mailto:%s">%s</a>' % (EMAIL, EMAIL))]), gap=20),
])
cols = columns([column(brand, "37%"), column(col_event, "21%"), column(col_involved, "21%"), column(col_community, "21%")], cls="wcm-footer-cols", gap=40)

# 3. follow and subscribe ------------------------------------------------------------
social_site = ('<!-- wp:social-links {"iconColor":"base","iconColorValue":"#FFFFFF","iconBackgroundColor":"accent-1","iconBackgroundColorValue":"#0073aa","size":"has-normal-icon-size","style":{"spacing":{"blockGap":"var:preset|spacing|20"}},"layout":{"type":"flex"}} -->\n'
               '<ul class="wp-block-social-links has-normal-icon-size has-icon-color has-icon-background-color">%s</ul>\n<!-- /wp:social-links -->'
               % "\n".join('<!-- wp:social-link {"url":"%s","service":"%s"} /-->' % (u, s) for s, u in SOCIAL))
social_preview = '<ul class="wp-block-social-links is-layout-flex" style="display:flex;gap:var(--wp--preset--spacing--20);list-style:none;margin:0;padding:0">%s</ul>' % "".join(
    '<li class="wp-social-link has-accent-1-background-color has-base-color" style="width:36px;height:36px;border-radius:999px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:0.875rem"><a href="%s" style="color:inherit">%s</a></li>' % (u, s[:2].title()) for s, u in SOCIAL)
follow = group("\n\n".join([eyebrow("Follow"), site_only(social_site, social_preview)]), layout="flex", wrap="wrap", valign="center", gap=30, cls="wcm-footer-follow")

subscribe_site = '<!-- wp:jetpack/subscriptions {"buttonText":"Subscribe","submitButtonText":"Subscribe","buttonBackgroundColor":"accent-1","textColor":"base","borderRadius":999,"padding":12,"spacing":8} /-->'
subscribe_preview = group("\n\n".join([
    group(para("you@example.com", color="accent-4"), layout="flex", bg="accent-5", radius="999px", padding=(20, 20, 30, 30), gap=0, cls="wcm-fake-input"),
    buttons([button("Subscribe", "#")], justify="left"),
]), layout="flex", wrap="wrap", valign="center", gap=20)
subscribe = group("\n\n".join([para("Get updates in your inbox", weight=700), site_only(subscribe_site, subscribe_preview)]), layout="flex", wrap="wrap", valign="center", gap=30, cls="wcm-footer-subscribe")
follow_row = group("\n\n".join([follow, subscribe]), layout="flex", wrap="wrap", justify="space-between", valign="center", align="wide", gap=40)

# 4. credit line --------------------------------------------------------------------------
credit = group("\n\n".join([
    para("© 2027 WordCamp Mumbai · Organised by the Mumbai WordPress community", size="small", color="accent-4"),
    para('<a href="/2027/code-of-conduct/">Code of Conduct</a> · Proudly powered by <a href="https://wordpress.org/">WordPress</a>', size="small", color="accent-4"),
]), layout="flex", wrap="wrap", justify="space-between", align="wide", gap=20, cls="wcm-footer-credit")

footer = group("\n\n".join([cta, rule(), cols, rule(), follow_row, credit]),
               layout="constrained", align="full", bg="base", cls="wcm-footer", gap=40, padding=(70, 50))

with open(os.path.join(HERE, "block.html"), "w") as fh:
    fh.write(footer + "\n")
print("wrote block.html")
