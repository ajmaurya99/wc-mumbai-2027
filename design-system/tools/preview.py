#!/usr/bin/env python3
"""Build preview.html from block.html the way WordPress renders it.

Saved block markup (what you paste into the code editor) is not what the
front end serves: at render time WordPress adds layout classes
(is-layout-constrained, is-layout-flex, has-global-padding, justification
classes) and emits a generated stylesheet for blockGap, grid columns and
custom content widths. This script reproduces that step, then wraps the
result in a standalone page that loads tools/theme-shim.css (emulating the
Twenty Twenty-Five saved Styles) and tokens/tokens.css, plus any *.css that
sits next to block.html.

Usage:
  preview.py <component-dir> [...]      write <dir>/preview.html for each dir
  preview.py <file.html>                 write <file>.preview.html (CSS from its folder)
  preview.py --group <out.html> <dir>...  one page stacking several components
  preview.py --stdin < block.html         print the rendered fragment only
  preview.py --site block.html            print the paste-ready markup (see markers)

Markers inside block.html:
  <!-- ds:preview-only --> … <!-- /ds:preview-only -->  shown in previews only
      (stand-ins for dynamic blocks such as Query Loop or Jetpack forms)
  <!-- ds:site-only --> … <!-- /ds:site-only -->        pasted to the site only
Asset URLs under https://cdn.jsdelivr.net/gh/ajmaurya99/wc-mumbai-2027@main/
are rewritten to local repo paths in previews.

It never modifies block.html.
"""
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DS_ROOT = os.path.dirname(HERE)
REPO = os.path.dirname(DS_ROOT)
# Assets are committed to the repo and served by jsDelivr on the live site
# (the hero already does this). Previews load the same files from disk.
CDN_PREFIX = "https://cdn.jsdelivr.net/gh/ajmaurya99/wc-mumbai-2027@main/"
PREVIEW_ONLY = re.compile(r"<!--\s*ds:preview-only\s*-->(.*?)<!--\s*/ds:preview-only\s*-->", re.S)
SITE_ONLY = re.compile(r"<!--\s*ds:site-only\s*-->(.*?)<!--\s*/ds:site-only\s*-->", re.S)

BLOCK_OPEN = re.compile(r"<!--\s*wp:([a-z0-9/_-]+)(\s+(\{.*?\}))?\s*(/)?-->", re.S)
TAG_OPEN = re.compile(r"<([a-zA-Z][a-zA-Z0-9-]*)((?:\s+[^\s=>/]+(?:=(?:\"[^\"]*\"|'[^']*'|[^\s>]+))?)*)\s*(/?)>")

# blocks whose wrapper gets layout classes, and their default layout type
LAYOUT_BLOCKS = {
    "core/group": "flow",
    "core/columns": "flex",
    "core/column": "flow",
    "core/buttons": "flex",
    "core/post-content": "flow",
    "core/cover": "flow",
}


def background_style(attrs):
    """Inline background declarations WordPress adds at render for style.background."""
    bg = (attrs.get("style") or {}).get("background") or {}
    decls = []
    img = bg.get("backgroundImage")
    if isinstance(img, dict) and img.get("url"):
        decls.append("background-image:url('%s')" % img["url"])
        decls.append("background-size:%s" % bg.get("backgroundSize", "cover"))
        if bg.get("backgroundPosition"):
            decls.append("background-position:%s" % bg["backgroundPosition"])
        decls.append("background-repeat:%s" % bg.get("backgroundRepeat", "no-repeat"))
        if bg.get("backgroundAttachment"):
            decls.append("background-attachment:%s" % bg["backgroundAttachment"])
    return ";".join(decls)


def for_site(markup):
    """Handover form: drop preview-only parts, unwrap site-only markers."""
    markup = PREVIEW_ONLY.sub("", markup)
    return SITE_ONLY.sub(lambda m: m.group(1), markup)


def for_preview(markup):
    markup = SITE_ONLY.sub("", markup)
    markup = PREVIEW_ONLY.sub(lambda m: m.group(1), markup)
    return markup


def preset_to_css(value):
    """'var:preset|spacing|30' -> 'var(--wp--preset--spacing--30)'"""
    if isinstance(value, str) and value.startswith("var:"):
        parts = value.split(":", 1)[1].split("|")
        return "var(--wp--" + "--".join(parts) + ")"
    return value


def gap_css(block_gap):
    """Return (row, column) gap strings, or None."""
    if block_gap is None:
        return None
    if isinstance(block_gap, dict):
        top = preset_to_css(block_gap.get("top", block_gap.get("left", "var(--wp--style--block-gap)")))
        left = preset_to_css(block_gap.get("left", top))
        return top, left
    v = preset_to_css(block_gap)
    return v, v


class Renderer:
    def __init__(self, cdn_local=None):
        self.counter = 0
        self.styles = []
        self.cdn_local = cdn_local

    def next_id(self, block):
        self.counter += 1
        short = block.split("/")[-1]
        return "wp-container-core-%s-is-layout-%d" % (short, self.counter)

    def layout_classes(self, block, attrs):
        classes = []
        layout = attrs.get("layout") or {}
        ltype = layout.get("type") or LAYOUT_BLOCKS.get(block, "flow")
        if ltype == "default":
            ltype = "flow"  # saved as "default", rendered as is-layout-flow
        if block == "core/columns":
            ltype = "flex"
        short = block.split("/")[-1]
        classes.append("is-layout-" + ltype)

        if ltype == "flex":
            jc = layout.get("justifyContent")
            if jc:
                classes.append("is-content-justification-" + jc)
            if layout.get("orientation") == "vertical":
                classes.append("is-vertical")
            elif "orientation" in layout:
                classes.append("is-horizontal")
            if layout.get("flexWrap") == "nowrap":
                classes.append("is-nowrap")
        if ltype == "constrained":
            classes.append("has-global-padding")

        rules = []
        gap = gap_css((attrs.get("style") or {}).get("spacing", {}).get("blockGap"))
        if ltype in ("flex", "grid") and gap:
            rules.append("gap: %s %s;" % gap)
        if ltype in ("flow", "constrained") and gap:
            rules.append("> * { margin-block-start: 0; margin-block-end: 0; } > * + * { margin-block-start: %s; margin-block-end: 0; }" % gap[0])
        if ltype == "constrained":
            cs = layout.get("contentSize")
            ws = layout.get("wideSize") or cs
            if cs:
                rules.append("> :where(:not(.alignleft):not(.alignright):not(.alignfull)) { max-width: %s; }" % cs)
            if ws:
                rules.append("> .alignwide { max-width: %s; }" % ws)
            jc = layout.get("justifyContent")
            if jc == "left":
                rules.append("> :where(:not(.alignleft):not(.alignright):not(.alignfull)) { margin-left: 0 !important; margin-right: auto !important; }")
            if jc == "right":
                rules.append("> :where(:not(.alignleft):not(.alignright):not(.alignfull)) { margin-left: auto !important; margin-right: 0 !important; }")
        if ltype == "grid":
            if layout.get("columnCount"):
                rules.append("grid-template-columns: repeat(%s, minmax(0, 1fr));" % layout["columnCount"])
            else:
                mw = layout.get("minimumColumnWidth", "12rem")
                rules.append("grid-template-columns: repeat(auto-fill, minmax(min(%s, 100%%), 1fr));" % mw)

        if rules:
            cid = self.next_id(block)
            classes.append(cid)
            for r in rules:
                if r.startswith(">"):
                    # nested selectors: split "> a {..} > b {..}"
                    for m in re.finditer(r"(>[^{]+)\{([^}]*)\}", r):
                        self.styles.append(".%s %s{%s}" % (cid, m.group(1).strip(), m.group(2).strip()))
                else:
                    self.styles.append(".%s { %s }" % (cid, r))
        classes.append("wp-block-%s-is-layout-%s" % (short, ltype))
        return classes

    def render(self, markup):
        markup = for_preview(markup)
        markup = markup.replace(CDN_PREFIX, self.cdn_local or CDN_PREFIX)
        # cover: WordPress puts the layout classes on the inner container
        markup = re.sub(r'class="wp-block-cover__inner-container"', 'class="wp-block-cover__inner-container is-layout-constrained wp-block-cover-is-layout-constrained"', markup)
        out = []
        pos = 0
        for m in BLOCK_OPEN.finditer(markup):
            block = m.group(1)
            if "/" not in block:
                block = "core/" + block
            attrs = {}
            if m.group(3):
                try:
                    attrs = json.loads(m.group(3))
                except json.JSONDecodeError as e:
                    sys.exit("bad block JSON at offset %d: %s" % (m.start(), e))
            out.append(markup[pos:m.end()])
            pos = m.end()
            if block not in LAYOUT_BLOCKS or m.group(4):
                continue
            tag = TAG_OPEN.search(markup, pos)
            if not tag:
                continue
            between = markup[pos:tag.start()]
            if between.strip():
                continue  # something other than whitespace before the wrapper: leave it
            new_classes = self.layout_classes(block, attrs)
            if block == "core/cover":
                new_classes = []  # cover's layout classes go on its inner container (handled below)
            tag_text = tag.group(0)
            if new_classes:
                if re.search(r'\sclass="', tag_text):
                    tag_text = re.sub(r'(\sclass=")([^"]*)"', lambda mm: '%s%s %s"' % (mm.group(1), mm.group(2), " ".join(new_classes)), tag_text, count=1)
                else:
                    tag_text = tag_text[: len(tag.group(1)) + 1] + ' class="%s"' % " ".join(new_classes) + tag_text[len(tag.group(1)) + 1:]
            extra_style = background_style(attrs)
            if extra_style:
                if re.search(r'\sstyle="', tag_text):
                    tag_text = re.sub(r'(\sstyle=")([^"]*)"', lambda mm: '%s%s;%s"' % (mm.group(1), mm.group(2), extra_style), tag_text, count=1)
                else:
                    tag_text = tag_text[: len(tag.group(1)) + 1] + ' style="%s"' % extra_style + tag_text[len(tag.group(1)) + 1:]
            out.append(between)
            out.append(tag_text)
            pos = tag.end()
        out.append(markup[pos:])
        return "".join(out)


def rel(from_dir, target):
    return os.path.relpath(target, from_dir).replace(os.sep, "/")


PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:wght@400;700&family=Kalam:wght@700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{shim}">
<link rel="stylesheet" href="{tokens}">
{component_css}
<style>
/* generated by preview.py: what WordPress emits for blockGap / layout at render time */
{generated}
/* preview chrome (not part of the component) */
.wp-site-blocks {{ padding-top: 40px; padding-bottom: 40px; }}
.ds-preview-label {{ font: 700 12px/1 ui-monospace, Menlo, monospace; letter-spacing: .06em; text-transform: uppercase; color: #546776; padding: 12px clamp(30px, 5vw, 50px); background: #FFFFFF; border-top: 1px dashed #546776; border-bottom: 1px dashed #546776; margin-top: 40px !important; margin-bottom: 0 !important; }}
.ds-preview-label:first-child {{ margin-top: 0 !important; }}
</style>
</head>
<body>
<div class="wp-site-blocks">
<main class="wp-block-group alignfull has-global-padding is-layout-constrained wp-block-group-is-layout-constrained">
{body}
</main>
</div>
</body>
</html>
"""


def build_page(sections, out_path, title):
    """sections: list of (label or None, block_html, [css paths])"""
    out_dir = os.path.dirname(os.path.abspath(out_path))
    r = Renderer(cdn_local=rel(out_dir, REPO) + "/")
    body_parts = []
    css_links = []
    for label, markup, css_files in sections:
        if label:
            body_parts.append('<p class="ds-preview-label alignfull">%s</p>' % html.escape(label))
        body_parts.append(r.render(markup))
        for c in css_files:
            link = '<link rel="stylesheet" href="%s">' % rel(out_dir, c)
            if link not in css_links:
                css_links.append(link)
    page = PAGE.format(
        title=html.escape(title),
        shim=rel(out_dir, os.path.join(HERE, "theme-shim.css")),
        tokens=rel(out_dir, os.path.join(DS_ROOT, "tokens", "tokens.css")),
        component_css="\n".join(css_links),
        generated="\n".join(r.styles),
        body="\n".join(body_parts),
    )
    with open(out_path, "w") as f:
        f.write(page)
    return out_path


def component_inputs(d):
    d = os.path.abspath(d)
    if os.path.isfile(d):
        block = d
        d = os.path.dirname(d)
        css = sorted(os.path.join(d, f) for f in os.listdir(d) if f.endswith(".css"))
        return open(block).read(), css
    block = os.path.join(d, "block.html")
    if not os.path.exists(block):
        sys.exit("no block.html in %s" % d)
    css = sorted(os.path.join(d, f) for f in os.listdir(d) if f.endswith(".css"))
    return open(block).read(), css


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if argv[0] == "--stdin":
        print(Renderer().render(sys.stdin.read()))
        return 0
    if argv[0] == "--site":
        # print the paste-ready form of a block.html (preview-only parts removed)
        sys.stdout.write(for_site(open(argv[1]).read()))
        return 0
    if argv[0] == "--group":
        out = argv[1]
        dirs = argv[2:]
        sections = []
        for d in dirs:
            markup, css = component_inputs(d)
            label = os.path.relpath(d, os.path.join(DS_ROOT, "components")).strip("./")
            sections.append((label, markup, css))
        build_page(sections, out, "WCM design system: " + os.path.basename(os.path.dirname(os.path.abspath(out))))
        print("wrote", out)
        return 0
    for d in argv:
        markup, css = component_inputs(d)
        if os.path.isfile(d):
            stem = os.path.splitext(os.path.basename(d))[0]
            out = os.path.join(os.path.dirname(os.path.abspath(d)), stem + ".preview.html")
            name = stem
        else:
            out = os.path.join(os.path.abspath(d), "preview.html")
            name = os.path.basename(os.path.abspath(d))
        build_page([(None, markup, css)], out, "WCM component: " + name)
        print("wrote", out)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
