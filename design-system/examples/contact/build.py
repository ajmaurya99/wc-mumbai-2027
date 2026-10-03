#!/usr/bin/env python3
"""Generate the Contact page for WordCamp Mumbai 2027 as core-block markup.

Writes sections/NN-name.html and block.html (paste into the Contact page's code
editor). The form is the site's existing Jetpack Form block (it already sends to
mumbai@wordcamp.org); previews show a static stand-in. Helpers live in
design-system/tools/blocks.py. Run: python3 design-system/examples/contact/build.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(HERE)), "tools"))
from blocks import *  # noqa: E402,F401

EMAIL = "mumbai@wordcamp.org"
LINKS = [
    ("Email", EMAIL, "mailto:" + EMAIL),
    ("Facebook", "WPMumbai.org", "https://www.facebook.com/WPMumbai.org/"),
    ("X", "@wcmumbai", "https://x.com/wcmumbai"),
    ("LinkedIn", "WPMumbai", "https://www.linkedin.com/company/wpmumbai/"),
    ("Instagram", "@wpmumbai", "https://www.instagram.com/wpmumbai/"),
]
SOCIAL = [("facebook", "https://www.facebook.com/WPMumbai.org/"), ("x", "https://x.com/wcmumbai"),
          ("linkedin", "https://www.linkedin.com/company/wpmumbai/"), ("instagram", "https://www.instagram.com/wpmumbai/")]


def tagline(text):
    return ('<!-- wp:paragraph {"textColor":"accent-2","fontSize":"large","fontFamily":"kalam"} -->\n'
            '<p class="has-accent-2-color has-text-color has-large-font-size has-kalam-font-family">%s</p>\n<!-- /wp:paragraph -->' % text)


# the site's Jetpack Form block, as saved on the current Contact page, with the button on the palette
FORM_SITE = '''<!-- wp:jetpack/contact-form {"subject":"WordCamp Contact Request","to":"%s","jetpackCRM":false,"salesforceData":{"organizationId":"","sendToSalesforce":false},"mailpoet":{"listId":null,"listName":null,"enabledForForm":false}} -->
<div class="wp-block-jetpack-contact-form"><!-- wp:jetpack/field-name {"id":"","required":true,"fieldVariant":"name"} -->
<div><!-- wp:jetpack/label {"label":"Name"} /-->

<!-- wp:jetpack/input {"style":{"border":{"style":"solid"}}} /--></div>
<!-- /wp:jetpack/field-name -->

<!-- wp:jetpack/field-email {"id":"","required":true} -->
<div><!-- wp:jetpack/label {"label":"Email"} /-->

<!-- wp:jetpack/input {"style":{"border":{"style":"solid"}}} /--></div>
<!-- /wp:jetpack/field-email -->

<!-- wp:jetpack/field-textarea {"id":"","required":true} -->
<div><!-- wp:jetpack/label {"label":"What would you like to ask or tell us?"} /-->

<!-- wp:jetpack/input {"type":"textarea","style":{"border":{"style":"solid"}}} /--></div>
<!-- /wp:jetpack/field-textarea -->

<!-- wp:jetpack/button {"element":"button","text":"Send message","backgroundColor":"accent-1","textColor":"base","borderRadius":999,"lock":{"move":false,"remove":true}} /--></div>
<!-- /wp:jetpack/contact-form -->''' % EMAIL


def fake_field(label, tall=False):
    return group("\n\n".join([
        para(label, size="small", color="accent-4"),
        group(para("&nbsp;"), layout="flex", bg="accent-5", radius="8px", padding=(40, 40, 30, 30) if tall else (20, 20, 30, 30), gap=0, cls="wcm-fake-input"),
    ]), gap=20)


FORM_PREVIEW = group("\n\n".join([
    fake_field("Name"), fake_field("Email"), fake_field("What would you like to ask or tell us?", tall=True),
    buttons([button("Send message", "#")], justify="left"),
]), gap=30)

form = "<!-- ds:site-only -->\n%s\n<!-- /ds:site-only -->\n<!-- ds:preview-only -->\n%s\n<!-- /ds:preview-only -->" % (FORM_SITE, FORM_PREVIEW)

form_card = group("\n\n".join([
    group("\n\n".join([heading("Send us a message", 2, "large"), para("Everything goes to one inbox and the whole organising team reads it, so there is no wrong way to reach us.")]), gap=20),
    form,
]), bg="base", radius="16px", padding=(40, 40, 40, 40), gap=40, cls="wcm-card wcm-form")

# other ways: label + link pairs, then the icons
ways = [group("\n\n".join([eyebrow(label, color="accent-4"), para('<a href="%s">%s</a>' % (href, text), weight=700)]), gap=0) for label, text, href in LINKS]
social_site = ('<!-- wp:social-links {"iconColor":"accent-1","iconColorValue":"#0073aa","iconBackgroundColor":"accent-5","iconBackgroundColorValue":"#f2f7fa","className":"wcm-social","layout":{"type":"flex","justifyContent":"left"}} -->\n'
               '<ul class="wp-block-social-links has-icon-color has-icon-background-color wcm-social">%s</ul>\n<!-- /wp:social-links -->'
               % "\n".join('<!-- wp:social-link {"url":"%s","service":"%s","label":"WordCamp Mumbai on %s"} /-->' % (u, s, s.capitalize()) for s, u in SOCIAL))
social_preview = ('<ul class="wp-block-social-links has-icon-color has-icon-background-color wcm-social is-layout-flex">%s</ul>'
                  % "".join('<li class="wp-social-link wp-social-link-%s wp-block-social-link has-accent-1-color has-accent-5-background-color"><a class="wp-block-social-link-anchor" href="%s">%s</a></li>' % (s, u, {"facebook": "f", "x": "X", "linkedin": "in", "instagram": "ig"}[s]) for s, u in SOCIAL))
social = "<!-- ds:site-only -->\n%s\n<!-- /ds:site-only -->\n<!-- ds:preview-only -->\n%s\n<!-- /ds:preview-only -->" % (social_site, social_preview)

ways_card = group("\n\n".join([
    heading("Other ways to reach us", 2, "large"),
    group("\n\n".join(ways), gap=30),
    social,
]), bg="base", radius="16px", padding=(40, 40, 40, 40), gap=30, cls="wcm-card")

sections = []

sections.append(("01-intro", section([
    group("\n\n".join([
        eyebrow("WordCamp Mumbai 2027 · 13 February 2027"),
        heading("Contact Us", 1, "xx-large"),
        tagline("Namaskar! Say hello"),
    ]), gap=20),
    para("Questions about the event, speaking, sponsoring, volunteering or getting involved? Write to us and it lands with the organising team."),
], bg=None, bgimage=(PNG + "motif-gateway@2x.png", "320px auto", "100% 100%", "no-repeat"))))

sections.append(("02-form", section([
    columns([column(form_card, "58%"), column(ways_card, "42%")]),
], bg="accent-5", bgimage=(PNG + "tile-lattice-light@2x.png", "120px auto", "0 0", "repeat"))))

sections.append(("03-sep-chai", separator("chai")))

def quick(title, text, label, href):
    return column(card([heading(title, 3, "large"), para(text), para('<a href="%s">%s →</a>' % (href, label), weight=700)], bg="accent-5", gap=20))

sections.append(("04-quick", section([
    section_header("Looking for something specific?", "Most questions are answered here"),
    columns([
        quick("Sponsoring", "Tiers, benefits and the application form.", "Call for sponsors", "/2027/call-for-sponsors/"),
        quick("Getting there", "The venue, the address and how to reach it.", "Venue", "/2027/venue/"),
        quick("The team", "The volunteers organising WordCamp Mumbai 2027.", "Organizers", "/2027/organizers/"),
    ]),
], bg=None, bgimage=(PNG + "motif-palm@2x.png", "420px auto", "0 100%", "no-repeat"))))

os.makedirs(os.path.join(HERE, "sections"), exist_ok=True)
for f in os.listdir(os.path.join(HERE, "sections")):
    os.remove(os.path.join(HERE, "sections", f))
for n, m in sections:
    with open(os.path.join(HERE, "sections", n + ".html"), "w") as fh:
        fh.write(m + "\n")
with open(os.path.join(HERE, "block.html"), "w") as fh:
    fh.write("\n\n".join(m for n, m in sections) + "\n")
print("wrote %d sections and block.html" % len(sections))
