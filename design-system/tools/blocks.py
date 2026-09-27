import json
import os
"""Core-block markup helpers shared by the page generators.

Every helper returns saved block markup (the <!-- wp:… --> form you paste into
the code editor) with preset slugs from tokens.json. Import from a generator:

    from blocks import *
"""

CDN = "https://cdn.jsdelivr.net/gh/ajmaurya99/wc-mumbai-2027@main/design-system/assets/"
PNG = CDN + "png/"
LOGO = "https://mumbai.wordcamp.org/2027/files/2026/09/wc_mumbai_logo_transparent.png"
GRADIENT = "linear-gradient(135deg,#0073aa 0%,#6d28d9 100%)"

SP = lambda n: "var(--wp--preset--spacing--%s)" % n
SPJ = lambda n: "var:preset|spacing|%s" % n


def pad(top=None, bottom=None, left=None, right=None):
    """(json, style) for a padding set."""
    j, s = {}, []
    for k, v in (("top", top), ("bottom", bottom), ("left", left), ("right", right)):
        if v is not None:
            j[k] = SPJ(v)
            s.append("padding-%s:%s" % (k, SP(v)))
    return j, s


# ------------------------------------------------------------------ atoms --

def eyebrow(text, align="left", color="accent-2"):
    al = ' "align":"%s",' % align if align != "left" else ""
    cls = " has-text-align-%s" % align if align != "left" else ""
    return ('<!-- wp:paragraph {%s"style":{"typography":{"textTransform":"uppercase","letterSpacing":"0.08em","fontStyle":"normal","fontWeight":"700"}},"textColor":"%s","fontSize":"small"} -->\n'
            '<p class="%s has-%s-color has-text-color has-small-font-size" style="font-style:normal;font-weight:700;letter-spacing:0.08em;text-transform:uppercase">%s</p>\n'
            '<!-- /wp:paragraph -->') % (al.strip() + (" " if al else ""), color, cls.strip() or "", color, text)


def heading(text, level=2, size="x-large", align="left", color=None):
    j = {"level": level} if level != 2 else {}
    if align != "left":
        j["textAlign"] = align
    if color:
        j["textColor"] = color
    j["fontSize"] = size
    cls = ["wp-block-heading"]
    if align != "left":
        cls.append("has-text-align-" + align)
    if color:
        cls += ["has-%s-color" % color, "has-text-color"]
    cls.append("has-%s-font-size" % size)
    import json
    return '<!-- wp:heading %s -->\n<h%d class="%s">%s</h%d>\n<!-- /wp:heading -->' % (json.dumps(j, separators=(",", ":")), level, " ".join(cls), text, level)


def para(text, align="left", size=None, color=None, weight=None, extra_json=None):
    import json
    j = {}
    cls = []
    if align != "left":
        j["align"] = align
        cls.append("has-text-align-" + align)
    style = {}
    if weight:
        style["typography"] = {"fontWeight": str(weight)}
    if style:
        j["style"] = style
    if color:
        j["textColor"] = color
        cls += ["has-%s-color" % color, "has-text-color"]
    if size:
        j["fontSize"] = size
        cls.append("has-%s-font-size" % size)
    if extra_json:
        j.update(extra_json)
    attrs = (" " + json.dumps(j, separators=(",", ":"))) if j else ""
    c = ' class="%s"' % " ".join(cls) if cls else ""
    st = ' style="font-weight:%s"' % weight if weight else ""
    return '<!-- wp:paragraph%s -->\n<p%s%s>%s</p>\n<!-- /wp:paragraph -->' % (attrs, c, st, text)


def image(src, alt="", width=None, ratio=None, radius=None, link=None, scale="cover", size="large", cls=""):
    import json
    j = {}
    if ratio:
        j["aspectRatio"] = ratio
        j["scale"] = scale
    if width:
        j["width"] = width
    j["sizeSlug"] = "full" if width else size
    if link:
        j["linkDestination"] = "custom"
    if radius:
        j["style"] = {"border": {"radius": radius}}
    if cls:
        j["className"] = cls
    fcls = ["wp-block-image", "size-" + j["sizeSlug"]]
    if width:
        fcls.append("is-resized")
    if radius:
        fcls.append("has-custom-border")
    if cls:
        fcls.append(cls)
    st = []
    if radius:
        st.append("border-radius:%s" % radius)
    if ratio:
        st += ["aspect-ratio:%s" % ratio, "object-fit:%s" % scale]
    if width:
        st.append("width:%s" % width)
    img = '<img src="%s" alt="%s"%s/>' % (src, alt, (' style="%s"' % ";".join(st)) if st else "")
    if link:
        img = '<a href="%s">%s</a>' % (link, img)
    return '<!-- wp:image %s -->\n<figure class="%s">%s</figure>\n<!-- /wp:image -->' % (json.dumps(j, separators=(",", ":")), " ".join(fcls), img)


def button(text, href="#", style=None, width=None, bg=None, color=None):
    import json
    j = {}
    cls = ["wp-block-button"]
    acls = ["wp-block-button__link"]
    if bg:
        j["backgroundColor"] = bg
    if color:
        j["textColor"] = color
        acls += ["has-%s-color" % color]
    if bg:
        acls += ["has-%s-background-color" % bg]
    if color:
        acls.append("has-text-color")
    if bg:
        acls.append("has-background")
    if width:
        j["width"] = width
        cls += ["has-custom-width", "wp-block-button__width-%d" % width]
    if style:
        j["className"] = "is-style-" + style
        cls.append("is-style-" + style)
    acls.append("wp-element-button")
    attrs = (" " + json.dumps(j, separators=(",", ":"))) if j else ""
    return '<!-- wp:button%s -->\n<div class="%s"><a class="%s" href="%s">%s</a></div>\n<!-- /wp:button -->' % (attrs, " ".join(cls), " ".join(acls), href, text)


def buttons(items, justify="center"):
    return ('<!-- wp:buttons {"layout":{"type":"flex","justifyContent":"%s"}} -->\n<div class="wp-block-buttons">%s</div>\n<!-- /wp:buttons -->' % (justify, "\n\n".join(items)))


def group(inner, layout="flow", align=None, bg=None, gradient=None, padding=None, gap=None, radius=None, cls=None,
          justify=None, wrap=None, valign=None, orientation=None, bgimage=None, border_left=None, extra_style=None):
    import json
    j = {}
    if align:
        j["align"] = align
    if cls:
        j["className"] = cls
    style = {}
    st = []
    if border_left:
        style.setdefault("border", {})["left"] = {"color": "var:preset|color|" + border_left[0], "width": border_left[1]}
        st += ["border-left-color:var(--wp--preset--color--%s)" % border_left[0], "border-left-width:%s" % border_left[1], "border-left-style:solid"]
    if radius:
        style.setdefault("border", {})["radius"] = radius
        st.append("border-radius:%s" % radius)
    sp = {}
    if padding:
        pj, ps = pad(*padding)
        sp["padding"] = pj
        st += ps
    if gap is not None:
        sp["blockGap"] = SPJ(gap) if gap else "0"
    if sp:
        style["spacing"] = sp
    if gradient:
        style["color"] = {"gradient": gradient}
        st.append("background:%s" % gradient)
    if bgimage:
        url, size, pos, rep = bgimage
        style["background"] = {"backgroundImage": {"url": url, "source": "file"}, "backgroundSize": size, "backgroundPosition": pos, "backgroundRepeat": rep}
    if extra_style:
        st.append(extra_style)
    if style:
        j["style"] = style
    if bg:
        j["backgroundColor"] = bg
    lay = {"type": layout}
    if justify:
        lay["justifyContent"] = justify
    if wrap:
        lay["flexWrap"] = wrap
    if valign:
        lay["verticalAlignment"] = valign
    if orientation:
        lay["orientation"] = orientation
    j["layout"] = lay
    cl = ["wp-block-group"]
    if align:
        cl.append("align" + align)
    if cls:
        cl.append(cls)
    if bg:
        cl += ["has-%s-background-color" % bg, "has-background"]
    elif gradient:
        cl.append("has-background")
    stt = (' style="%s"' % ";".join(st)) if st else ""
    return '<!-- wp:group %s -->\n<div class="%s"%s>%s</div>\n<!-- /wp:group -->' % (json.dumps(j, separators=(",", ":")), " ".join(cl), stt, inner)


def columns(cols, align="wide", gap=30, valign=None, cls=None):
    import json
    j = {}
    if valign:
        j["verticalAlignment"] = valign
    if align:
        j["align"] = align
    if cls:
        j["className"] = cls
    j["style"] = {"spacing": {"blockGap": {"top": SPJ(gap), "left": SPJ(gap)}}}
    cl = ["wp-block-columns"]
    if valign:
        cl.append("are-vertically-aligned-" + valign)
    if align:
        cl.append("align" + align)
    if cls:
        cl.append(cls)
    return '<!-- wp:columns %s -->\n<div class="%s">%s</div>\n<!-- /wp:columns -->' % (json.dumps(j, separators=(",", ":")), " ".join(cl), "\n\n".join(cols))


def column(inner, width=None, valign=None):
    import json
    j = {}
    cl = ["wp-block-column"]
    if valign:
        j["verticalAlignment"] = valign
        cl.append("is-vertically-aligned-" + valign)
    if width:
        j["width"] = width
    attrs = (" " + json.dumps(j, separators=(",", ":"))) if j else ""
    st = ' style="flex-basis:%s"' % width if width else ""
    return '<!-- wp:column%s -->\n<div class="%s"%s>%s</div>\n<!-- /wp:column -->' % (attrs, " ".join(cl), st, inner)


def spacer(h):
    return '<!-- wp:spacer {"height":"%s"} -->\n<div style="height:%s" aria-hidden="true" class="wp-block-spacer"></div>\n<!-- /wp:spacer -->' % (h, h)


# ------------------------------------------------------------ molecules --

def section_header(eye, h2, tagline=None, align="center", body=None):
    parts = [eyebrow(eye, align), heading(h2, 2, "x-large", align)]
    if tagline:
        parts.append(('<!-- wp:paragraph {%s"textColor":"accent-2","fontSize":"large","fontFamily":"kalam"} -->\n'
                      '<p class="%shas-accent-2-color has-text-color has-large-font-size has-kalam-font-family">%s</p>\n<!-- /wp:paragraph -->')
                     % ('"align":"%s",' % align if align != "left" else "", "has-text-align-%s " % align if align != "left" else "", tagline))
    if body:
        parts.append(para(body, align))
    return group("\n\n".join(parts), gap=20)


def section(inner, bg="base", align="full", bgimage=None, cls=None, gap=40, padding=(70, 70)):
    return group("\n\n".join(inner), layout="constrained", align=align, bg=bg, padding=padding, gap=gap, bgimage=bgimage, cls=cls)


def card(inner, bg="accent-5", gap=None, cls="wcm-card"):
    return group("\n\n".join(inner), bg=bg, padding=(40, 40, 40, 40), radius="16px", cls=cls, gap=gap)


def fact_card(icon, label, value, note=None, bg="accent-5"):
    text = [para(label, color="accent-4", size="small"), para(value, size="large", weight=700)]
    if note:
        text.append(para(note, color="accent-4", size="small"))
    return group("\n\n".join([image(PNG + icon + "@2x.png", "", width="24px"),
                              group("\n\n".join(text), gap=0)]),
                 layout="flex", wrap="nowrap", valign="center", bg=bg, radius="16px", cls="wcm-fact",
                 padding=(30, 30, 40, 40), gap=30, border_left=("accent-2", "4px"))


def chip(text, tone="open"):
    color = "accent-2" if tone == "open" else "accent-4"
    return group(para(text, size="small", color=color, weight=700), layout="flex", bg="base", radius="8px",
                 padding=(20, 20, 30, 30), gap=0, cls="wcm-chip")


def separator(icon):
    line = '<!-- wp:separator {"className":"wcm-sep__line","backgroundColor":"accent-2"} -->\n<hr class="wp-block-separator has-text-color has-accent-2-color has-alpha-channel-opacity has-accent-2-background-color has-background wcm-sep__line"/>\n<!-- /wp:separator -->'
    return group("\n\n".join([line, image(PNG + "sep-" + icon + "@2x.png", "", width="200px"), line]),
                 layout="flex", wrap="nowrap", justify="center", valign="center", align="wide", cls="wcm-sep", gap=30,
                 padding=(40, 40))


def strip(name):
    return group(spacer("60px"), layout="constrained", align="full", cls="wcm-strip",
                 bgimage=(PNG + "strip-" + name + "@2x.png", "auto 60px", "50% 50%", "repeat-x"))


