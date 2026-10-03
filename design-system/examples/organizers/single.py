#!/usr/bin/env python3
"""Generate the single organizer template (single-wcb_organizer) for the Site Editor.

Writes single-template.html (the whole template: header part → main → footer part)
and single-preview/block.html (a static stand-in for previews and the gate).
Run: python3 design-system/examples/organizers/single.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(HERE)), "tools"))
from blocks import *  # noqa: E402,F401

PLACEHOLDER = "https://placehold.co/480x480/f2f7fa/546776.png?text=Photo"

# -------------------------------------------------------- site blocks --

back = para('<a href="/2027/organizers/">← All organizers</a>', size="small", weight=700)

# round photo with the 4px Accent 2 ring, as on the organizers grid (Post Featured Image → Border)
photo_site = '<!-- wp:post-featured-image {"aspectRatio":"1","width":"240px","height":"240px","scale":"cover","align":"center","style":{"border":{"radius":"999px","width":"4px"}},"borderColor":"accent-2","className":"wcm-organizer__photo"} /-->'
photo_preview = ('<!-- wp:image {"align":"center","width":"240px","height":"240px","aspectRatio":"1","scale":"cover","sizeSlug":"medium_large","linkDestination":"none","style":{"border":{"radius":"999px","width":"4px"}},"borderColor":"accent-2"} -->\n'
                 '<figure class="wp-block-image aligncenter size-medium_large is-resized has-custom-border"><img src="%s" alt="Organizer" class="has-border-color has-accent-2-border-color" style="border-width:4px;border-radius:999px;aspect-ratio:1;object-fit:cover;width:240px;height:240px"/></figure>\n<!-- /wp:image -->' % PLACEHOLDER)
photo = "<!-- ds:site-only -->\n%s\n<!-- /ds:site-only -->\n<!-- ds:preview-only -->\n%s\n<!-- /ds:preview-only -->" % (photo_site, photo_preview)

title_site = '<!-- wp:post-title {"level":1,"fontSize":"xx-large"} /-->'
title_preview = heading("Organizer Name", 1, "xx-large")
title = "<!-- ds:site-only -->\n%s\n<!-- /ds:site-only -->\n<!-- ds:preview-only -->\n%s\n<!-- /ds:preview-only -->" % (title_site, title_preview)

# team taxonomy, when set; renders nothing otherwise
team_site = '<!-- wp:post-terms {"term":"wcb_organizer_team","prefix":"Team: ","textColor":"accent-4","fontSize":"small"} /-->'
team_preview = para("Team: Technology", color="accent-4", size="small")
team = "<!-- ds:site-only -->\n%s\n<!-- /ds:site-only -->\n<!-- ds:preview-only -->\n%s\n<!-- /ds:preview-only -->" % (team_site, team_preview)

content_site = '<!-- wp:post-content {"layout":{"type":"constrained"}} /-->'
content_preview = "\n\n".join([
    para("Organizer Name is an Enterprise Project Manager who believes that good project management is as much about people as it is about plans, processes and deadlines."),
    para("A WordCamp speaker and longtime WordPress contributor, she has been part of the community for over eight years, organising meetups, contributing to releases and helping bring Contributor Days together."),
])
content = "<!-- ds:site-only -->\n%s\n<!-- /ds:site-only -->\n<!-- ds:preview-only -->\n%s\n<!-- /ds:preview-only -->" % (content_site, content_preview)

# ------------------------------------------------------------ sections --

hero = section([
    back,
    columns([
        column(photo, "30%", valign="center"),
        column(group("\n\n".join([
            eyebrow("Organizer · WordCamp Mumbai 2027"),
            title,
            tagline_kalam := ('<!-- wp:paragraph {"textColor":"accent-2","fontSize":"large","fontFamily":"kalam"} -->\n'
                              '<p class="has-accent-2-color has-text-color has-large-font-size has-kalam-font-family">Aamchi Mumbai, Aapla WordPress</p>\n<!-- /wp:paragraph -->'),
            team,
        ]), gap=20), "70%", valign="center"),
    ], valign="center"),
], bg=None, bgimage=(PNG + "motif-gateway@2x.png", "320px auto", "100% 100%", "no-repeat"), gap=40)

bio = section([
    group("\n\n".join([eyebrow("Bio"), content]), gap=30),
], bg="accent-5", bgimage=(PNG + "tile-lattice-light@2x.png", "120px auto", "0 0", "repeat"))

more = section([
    section_header("The team", "Meet the rest of the organising team", body="Twelve volunteers from the Mumbai WordPress community. Say hello when you see them at the venue."),
    buttons([button("All organizers", "/2027/organizers/"), button("Contact the team", "/2027/contact/", style="outline", color="accent-1")]),
], bg=None)

sections = [("01-hero", hero), ("02-bio", bio), ("03-more", more)]

# ----------------------------------------------------------------- write --

out = os.path.join(HERE, "single-preview")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "block.html"), "w") as fh:
    fh.write("\n\n".join(m for n, m in sections) + "\n")

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(HERE)), "tools"))
from preview import for_site  # noqa: E402
body = for_site("\n\n".join(m for n, m in sections))
template = ('<!-- wp:template-part {"slug":"header","theme":"twentytwentyfive","area":"header"} /-->\n\n'
            '<!-- wp:group {"tagName":"main","style":{"spacing":{"margin":{"top":"0"},"blockGap":"0"}},"layout":{"type":"constrained"}} -->\n'
            '<main class="wp-block-group" style="margin-top:0">%s</main>\n<!-- /wp:group -->\n\n'
            '<!-- wp:template-part {"slug":"footer","theme":"twentytwentyfive","area":"footer"} /-->\n') % body
with open(os.path.join(HERE, "single-template.html"), "w") as fh:
    fh.write(template)
print("wrote single-preview/block.html and single-template.html")
