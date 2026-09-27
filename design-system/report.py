#!/usr/bin/env python3
"""WCM design system report: grade block markup or CSS against tokens.json.

    report.py <file.html|file.css> [...] [--summary] [--strict]

For each file it lists every colour, font-size, font-family, spacing, radius,
shadow and motion value it finds, resolves it to the nearest token and prints:

    PASS    exact token (or a Twenty Twenty-Five preset reference)
    REVIEW  close to a token, or allowed only with care; look at it
    FAIL    off-system value, or a rule DESIGN-SYSTEM.md forbids
    STRIP   the WordCamp.org sanitiser would remove it (custom properties,
            will-change, container-*, <script>, <style>, <svg>, <input>, ...)

Output is a Markdown table so it can be pasted into spec.md. Exit status is
1 when any FAIL or STRIP row exists (also for REVIEW with --strict).
Values are read from ../tokens/tokens.json; hero class names are read from
the repo's hero.css and hero-block.html so reusing them fails the gate.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
TOKENS_PATH = os.path.join(HERE, "tokens", "tokens.json")

# ----------------------------------------------------------------- tokens ----

def load_tokens():
    t = json.load(open(TOKENS_PATH))
    colours = {}
    for name, node in t["color"].items():
        if name.startswith("$"):
            continue
        if "$value" in node:
            colours[name] = node["$value"]
        else:
            for sub, subnode in node.items():
                if not sub.startswith("$"):
                    colours[name + "." + sub] = subnode["$value"]
    sizes = {k: v["$value"] for k, v in t["type"]["size"].items() if not k.startswith("$")}
    spacing = {k: v["$value"] for k, v in t["spacing"].items() if not k.startswith("$")}
    radius = {k: v["$value"] for k, v in t["radius"].items() if not k.startswith("$")}
    shadow = t["shadow"]["cardHover"]["$extensions"]["org.wordcamp.mumbai"]["css"]
    families = {k: v["$extensions"]["org.wordcamp.mumbai"]["preset"] for k, v in t["type"]["family"].items() if not k.startswith("$")}
    return {
        "colours": colours,
        "sizes": sizes,
        "spacing": spacing,
        "radius": radius,
        "shadow": shadow,
        "families": families,
        "button_padding": t["button"]["padding"]["$value"],
        "button_font": t["button"]["fontSize"]["$value"],
        "durations": (150, 250),
        "focus_offset": t["focus"]["offset"]["$value"],
        "border_button": t["border"]["button"]["$value"],
        "lift": t["motion"]["lift"]["$value"],
    }

TOK = load_tokens()
PRESET_COLOURS = {k for k in TOK["colours"] if "." not in k}
PRESET_SIZES = set(TOK["sizes"])
PRESET_SPACING = set(TOK["spacing"])
PRESET_FAMILIES = set(TOK["families"].values())
UNUSED_FAMILIES = {"manrope", "fira-code"}


def hero_classes():
    names = set()
    for f in ("hero.css", "hero-block.html"):
        p = os.path.join(REPO, f)
        if os.path.exists(p):
            txt = open(p, errors="replace").read()
            # the FOOTER SCENE fence in hero.css styles the site footer, not the hero: its class is reusable
            txt = re.sub(r"/\* ==== FOOTER SCENE: start ====.*?FOOTER SCENE: end ==== \*/", "", txt, flags=re.S)
            names.update(re.findall(r"\.(wcm-[\w-]+)", txt))
            names.update(re.findall(r'class="([^"]*)"', txt) and [c for m in re.findall(r'class="([^"]*)"', txt) for c in m.split() if c.startswith("wcm-")])
            names.update(re.findall(r'id="(wcm-[\w-]+)"', txt))
    return names

HERO_CLASSES = hero_classes()

# ------------------------------------------------------------------ utils ----

def hex_to_rgb(h):
    h = h.lstrip("#")
    if len(h) in (3, 4):
        h = "".join(c * 2 for c in h[:3])
    h = h[:6]
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def parse_colour(s):
    """Return (rgb, alpha) for #hex / rgb() / rgba() strings, else None."""
    s = s.strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", s)
    if m:
        h = m.group(1)
        alpha = 1.0
        if len(h) == 4:
            alpha = int(h[3] * 2, 16) / 255
        if len(h) == 8:
            alpha = int(h[6:8], 16) / 255
        return hex_to_rgb(h), alpha
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*([0-9.]+)\s*)?\)", s)
    if m:
        return (int(m.group(1)), int(m.group(2)), int(m.group(3))), float(m.group(4) or 1)
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s+(\d+)\s+(\d+)\s*(?:/\s*([0-9.]+%?)\s*)?\)", s)
    if m:
        a = m.group(4)
        alpha = 1.0 if a is None else (float(a[:-1]) / 100 if a.endswith("%") else float(a))
        return (int(m.group(1)), int(m.group(2)), int(m.group(3))), alpha
    return None


def nearest_colour(rgb):
    best, dist = None, 1e9
    for name, hx in TOK["colours"].items():
        r = hex_to_rgb(hx)
        d = sum((a - b) ** 2 for a, b in zip(rgb, r)) ** 0.5
        if d < dist:
            best, dist = name, d
    return best, dist


def to_px(value):
    """'1.38rem' -> 22.08, '16px' -> 16.0, else None (clamp, %, auto...)."""
    m = re.fullmatch(r"(-?[0-9]*\.?[0-9]+)(px|rem|em)", value.strip())
    if not m:
        if value.strip() in ("0", "0px", "0rem"):
            return 0.0
        return None
    n = float(m.group(1))
    return n if m.group(2) == "px" else n * 16


def norm(s):
    return re.sub(r"\s+", " ", s.strip().lower()).replace(", ", ",").replace(" ,", ",")


def nearest_dimension(value, table):
    """Return (token, kind) where kind in exact/close/none for a length."""
    v = norm(value)
    for name, tv in table.items():
        if norm(tv) == v or norm(tv).replace(" ", "") == v.replace(" ", ""):
            return name, "exact"
    px = to_px(value)
    if px is None:
        return None, "none"
    best, bestd = None, 1e9
    for name, tv in table.items():
        tpx = to_px(tv)
        if tpx is None:
            continue
        d = abs(tpx - px)
        if d < bestd:
            best, bestd = name, d
    if best is None:
        return None, "none"
    if bestd <= 0.1:
        return best, "exact"
    tpx = to_px(table[best])
    if tpx and bestd / tpx <= 0.15:
        return best, "close"
    return best, "none"


# ------------------------------------------------------------- scanning ----

class Report:
    def __init__(self, path):
        self.path = path
        self.rows = {}  # (category, found) -> dict(token, result, lines, note)

    def add(self, line, category, found, token, result, note=""):
        key = (category, found, result)
        r = self.rows.setdefault(key, {"token": token, "result": result, "lines": [], "note": note})
        if line not in r["lines"]:
            r["lines"].append(line)

    # colour ---------------------------------------------------------------
    def colour_literal(self, line, raw):
        parsed = parse_colour(raw)
        if not parsed:
            return
        rgb, alpha = parsed
        name, dist = nearest_colour(rgb)
        tok = "color." + name
        if dist < 0.5 and alpha >= 0.999:
            if name.startswith("festive."):
                self.add(line, "colour", raw, tok, "REVIEW", "festive: badges and dividers only")
            else:
                self.add(line, "colour", raw, tok, "PASS")
        elif dist < 0.5:
            self.add(line, "colour", raw, tok, "REVIEW", "token colour with alpha %.2f" % alpha)
        elif dist < 40:
            self.add(line, "colour", raw, tok + " (Δ%.0f)" % dist, "REVIEW", "close but not exact: use %s" % TOK["colours"][name])
        else:
            self.add(line, "colour", raw, tok + " (Δ%.0f)" % dist, "FAIL", "off-palette")

    def colour_slug(self, line, slug, found):
        if slug in PRESET_COLOURS:
            self.add(line, "colour", found, "color." + slug, "PASS")
        else:
            self.add(line, "colour", found, "–", "FAIL", "not a system preset")

    # font-size ------------------------------------------------------------
    def size_literal(self, line, value):
        v = value.strip()
        if v in ("inherit", "initial"):
            return
        if norm(v) == norm(TOK["button_font"]) or to_px(v) == 16.0:
            self.add(line, "font-size", v, "type.size.medium / button.fontSize", "PASS")
            return
        name, kind = nearest_dimension(v, TOK["sizes"])
        if kind == "exact":
            self.add(line, "font-size", v, "type.size." + name, "PASS")
        elif kind == "close":
            self.add(line, "font-size", v, "type.size." + name, "REVIEW", "use preset %s (%s)" % (name, TOK["sizes"][name]))
        else:
            self.add(line, "font-size", v, "–", "FAIL", "not a size preset")

    def size_slug(self, line, slug, found):
        if slug in PRESET_SIZES:
            self.add(line, "font-size", found, "type.size." + slug, "PASS")
        else:
            self.add(line, "font-size", found, "–", "FAIL", "not a size preset")

    # font-family ----------------------------------------------------------
    def family_literal(self, line, value):
        v = value.strip().lower()
        if v in ("inherit",):
            return
        m = re.search(r"--wp--preset--font-family--([\w-]+)", v)
        if m:
            self.family_slug(line, m.group(1), value.strip())
            return
        if "newsreader" in v:
            self.add(line, "font-family", value.strip(), "type.family.body", "REVIEW", "fonts come from Styles; do not set in CSS")
        elif "kalam" in v:
            self.add(line, "font-family", value.strip(), "type.family.accent", "REVIEW", "prefer the has-kalam-font-family preset")
        else:
            self.add(line, "font-family", value.strip(), "–", "FAIL", "not a system font")

    def family_slug(self, line, slug, found):
        if slug in PRESET_FAMILIES:
            self.add(line, "font-family", found, "type.family." + ("body" if slug == "newsreader" else "accent"), "PASS")
        elif slug in UNUSED_FAMILIES:
            self.add(line, "font-family", found, "–", "FAIL", "registered but unused on purpose")
        else:
            self.add(line, "font-family", found, "–", "FAIL", "not a system font")

    # spacing --------------------------------------------------------------
    def spacing_value(self, line, prop, value):
        v = value.strip()
        if v in ("auto", "inherit", "initial", "unset", "normal"):
            return
        if prop.startswith("padding") and norm(v) == norm(TOK["button_padding"]):
            self.add(line, "spacing", "%s: %s" % (prop, v), "button.padding", "PASS")
            return
        if prop.startswith("margin") and re.search(r"-\s*[0-9.]+(px|rem|em|vw|%)", v):
            self.add(line, "layout", "%s: %s" % (prop, v), "–", "FAIL", "negative margins are not allowed; use Full width alignment")
            return
        parts = re.findall(r"var\(--wp--preset--spacing--(\d+)\)|[-0-9.]+(?:px|rem|em|vw|vh|%)|clamp\([^)]*\)|\b0\b|calc\([^)]*\)", v)
        for token_hit in re.finditer(r"var\(--wp--preset--spacing--(\d+)\)", v):
            slug = token_hit.group(1)
            if slug in PRESET_SPACING:
                self.add(line, "spacing", "%s: %s" % (prop, token_hit.group(0)), "spacing." + slug, "PASS")
            else:
                self.add(line, "spacing", "%s: %s" % (prop, token_hit.group(0)), "–", "FAIL", "not a spacing preset")
        stripped = re.sub(r"var\([^)]*\)", "", v)
        for lit in re.finditer(r"clamp\([^)]*\)|-?[0-9]*\.?[0-9]+(?:px|rem|em|vw|vh)|(?<![\w.])0(?![\w.])", stripped):
            lit_s = lit.group(0)
            if lit_s == "0":
                continue
            if lit_s.endswith("%"):
                continue
            name, kind = nearest_dimension(lit_s, TOK["spacing"])
            found = "%s: %s" % (prop, lit_s)
            if re.search(r"(vw|vh)$", lit_s):
                self.add(line, "spacing", found, "–", "REVIEW", "viewport-relative spacing: only for image-tied offsets; justify in spec")
                continue
            if kind == "exact":
                self.add(line, "spacing", found, "spacing." + name, "PASS", "prefer the preset var")
            elif kind == "close":
                self.add(line, "spacing", found, "spacing." + name, "REVIEW", "use preset %s (%s)" % (name, TOK["spacing"][name]))
            else:
                self.add(line, "spacing", found, "–", "FAIL", "not a spacing preset")

    def spacing_slug(self, line, slug, found):
        if slug in PRESET_SPACING:
            self.add(line, "spacing", found, "spacing." + slug, "PASS")
        else:
            self.add(line, "spacing", found, "–", "FAIL", "not a spacing preset")

    # radius ---------------------------------------------------------------
    def radius_value(self, line, value):
        v = value.strip()
        for lit in re.findall(r"[0-9]*\.?[0-9]+(?:px|rem|em|%)|\b0\b", v):
            if lit == "0":
                continue
            if lit.endswith("%"):
                self.add(line, "radius", lit, "–", "FAIL", "percent radii are off-system (use 999px for pills)")
                continue
            name, kind = nearest_dimension(lit, TOK["radius"])
            if kind == "exact":
                self.add(line, "radius", lit, "radius." + name, "PASS")
            elif kind == "close" or (to_px(lit) or 0) >= 100:
                tok = "radius.pill" if (to_px(lit) or 0) >= 100 else "radius." + name
                self.add(line, "radius", lit, tok, "REVIEW", "use %s" % (TOK["radius"]["pill"] if tok.endswith("pill") else TOK["radius"][name]))
            else:
                self.add(line, "radius", lit, "–", "FAIL", "not 8px, 16px or 999px")

    # shadow ---------------------------------------------------------------
    def shadow_value(self, line, value):
        v = norm(value).replace("0.12", ".12")
        if v in ("none",):
            return
        if v == norm(TOK["shadow"]).replace("0.12", ".12"):
            self.add(line, "shadow", value.strip(), "shadow.cardHover", "PASS", "hover only")
        else:
            self.add(line, "shadow", value.strip(), "shadow.cardHover", "FAIL", "the only shadow is %s" % TOK["shadow"])

    # motion ---------------------------------------------------------------
    def motion_value(self, line, prop, value):
        v = value.strip()
        if prop == "animation" and v not in ("none",):
            self.add(line, "motion", "%s: %s" % (prop, v), "–", "FAIL", "animations are not allowed outside the hero")
            return
        for d in re.findall(r"([0-9.]+)(ms|s)\b", v):
            ms = float(d[0]) * (1000 if d[1] == "s" else 1)
            lo, hi = TOK["durations"]
            found = "%s: %s%s" % (prop, d[0], d[1])
            if lo <= ms <= hi:
                self.add(line, "motion", found, "motion.duration", "PASS")
            elif ms == 0:
                continue
            else:
                self.add(line, "motion", found, "motion.duration", "FAIL", "hover transitions are 150–250ms")
        if "transform" in v and prop.startswith("transition"):
            self.add(line, "motion", "%s: transform" % prop, "motion.lift", "REVIEW", "transform transitions: cards only (4px lift); never on the header")

    # sanitiser -----------------------------------------------------------
    def strip(self, line, found, why):
        self.add(line, "sanitiser", found, "–", "STRIP", why)

    # ----------------------------------------------------------------------
    def scan(self):
        text = open(self.path, errors="replace").read()
        is_css = self.path.lower().endswith(".css")
        if is_css:
            # blank /* comments */ but keep the newlines so line numbers hold
            text = re.sub(r"/\*.*?\*/", lambda m: re.sub(r"[^\n]", " ", m.group(0)), text, flags=re.S)
        for i, raw_line in enumerate(text.splitlines(), 1):
            line = raw_line
            low = line.lower()

            # -- sanitiser: tags (in HTML files) and stripped CSS features
            for tag in ("script", "style", "svg", "input", "iframe", "link", "form", "textarea", "object", "embed", "select"):
                if re.search(r"<\s*%s\b" % tag, low):
                    if tag == "embed" and "wp:embed" in low:
                        continue
                    self.strip(i, "<%s>" % tag, "removed by wp_kses_post / the Custom HTML sanitiser")
            if is_css or 'style="' in low or "{" in low:
                for m in re.finditer(r"(?<![\w-])(--[a-z][\w-]*)\s*:", low):
                    self.strip(i, m.group(1) + ":", "custom property definitions are stripped")
                for m in re.finditer(r"var\((--[\w-]+)", low):
                    if not m.group(1).startswith("--wp--"):
                        self.strip(i, "var(%s)" % m.group(1), "only theme preset variables survive")
                for kw in ("will-change", "container-type", "container-name"):
                    if kw in low:
                        self.strip(i, kw, "stripped by the CSS sanitiser")
                if re.search(r"\bcontainer\s*:", low):
                    self.strip(i, "container:", "stripped by the CSS sanitiser")
                if "@import" in low:
                    self.strip(i, "@import", "stripped by the CSS sanitiser")
                if "expression(" in low or "javascript:" in low:
                    self.strip(i, "expression()/javascript:", "blocked")
                if "@container" in low:
                    self.strip(i, "@container", "container queries are stripped")
            if "100vw" in low:
                self.add(i, "layout", "100vw", "–", "FAIL", "never set 100vw widths; use Full width alignment")
            if "onclick" in low or re.search(r"\son\w+=", low):
                self.strip(i, "on*= handler", "event handlers are stripped")

            # -- hero classes
            for cls in re.findall(r"wcm-[\w-]+", line):
                if cls in HERO_CLASSES:
                    self.add(i, "hero", cls, "–", "FAIL", "hero class: off limits")

            # -- block JSON attributes
            for m in re.finditer(r'"textColor"\s*:\s*"([\w-]+)"', line):
                self.colour_slug(i, m.group(1), 'textColor: %s' % m.group(1))
            for m in re.finditer(r'"backgroundColor"\s*:\s*"([\w-]+)"', line):
                self.colour_slug(i, m.group(1), 'backgroundColor: %s' % m.group(1))
            for m in re.finditer(r'"fontSize"\s*:\s*"([\w-]+)"', line):
                self.size_slug(i, m.group(1), 'fontSize: %s' % m.group(1))
            for m in re.finditer(r'"fontFamily"\s*:\s*"([\w-]+)"', line):
                self.family_slug(i, m.group(1), 'fontFamily: %s' % m.group(1))
            for m in re.finditer(r'var:preset\|color\|([\w-]+)', line):
                self.colour_slug(i, m.group(1), m.group(0))
            for m in re.finditer(r'var:preset\|spacing\|([\w-]+)', line):
                self.spacing_slug(i, m.group(1), m.group(0))
            for m in re.finditer(r'var:preset\|font-size\|([\w-]+)', line):
                self.size_slug(i, m.group(1), m.group(0))
            for m in re.finditer(r'"(padding|margin|blockGap)"\s*:\s*(\{[^}]*\}|"[^"]*")', line):
                prop = "gap" if m.group(1) == "blockGap" else m.group(1)
                for v in re.findall(r'"([^"]+)"\s*(?=,|\}|$)', m.group(2).strip("{}") if m.group(2).startswith("{") else m.group(2)):
                    if v.startswith("var:") or v in ("top", "bottom", "left", "right"):
                        continue
                    self.spacing_value(i, prop, v)
            for m in re.finditer(r'"radius"\s*:\s*"([^"]+)"', line):
                self.radius_value(i, m.group(1))
            for m in re.finditer(r'"radius"\s*:\s*\{([^}]*)\}', line):
                for v in re.findall(r'"([^"]+)"\s*(?=,|$)', m.group(1)):
                    self.radius_value(i, v)
            for m in re.finditer(r'"(?:text|background)"\s*:\s*"(#[0-9a-fA-F]{3,8})"', line):
                self.colour_literal(i, m.group(1))

            # -- preset classes
            for m in re.finditer(r"has-([\w-]+?)-(background-color|color)\b", line):
                slug = m.group(1)
                if slug in ("text", "link", "background", "icon", "icon-background"):
                    continue
                self.colour_slug(i, slug, m.group(0))
            for m in re.finditer(r"has-([\w-]+?)-font-size\b", line):
                self.size_slug(i, m.group(1), m.group(0))
            for m in re.finditer(r"has-([\w-]+?)-font-family\b", line):
                self.family_slug(i, m.group(1), m.group(0))

            # -- CSS declarations (in CSS files and inline style="")
            decl_text = line
            if not is_css:
                decl_text = "; ".join(re.findall(r'style="([^"]*)"', line))
            # shadows first, then blank them so their rgba is not re-read as a colour
            for m in re.finditer(r"box-shadow\s*:\s*([^;\"}]+)", decl_text):
                self.shadow_value(i, m.group(1))
            decl_text = re.sub(r"box-shadow\s*:\s*[^;\"}]+", "", decl_text)
            for m in re.finditer(r"(?<![\w-])(padding(?:-[a-z]+)*|margin(?:-[a-z]+)*|gap|row-gap|column-gap|inset(?:-[a-z]+)*)\s*:\s*([^;\"}]+)", decl_text):
                self.spacing_value(i, m.group(1), m.group(2))
            for m in re.finditer(r"border(?:-[a-z]+)*-radius\s*:\s*([^;\"}]+)", decl_text):
                self.radius_value(i, m.group(1))
            for m in re.finditer(r"(?<![\w-])font-size\s*:\s*([^;\"}]+)", decl_text):
                v = m.group(1)
                pm = re.search(r"--wp--preset--font-size--([\w-]+)", v)
                if pm:
                    self.size_slug(i, pm.group(1), v.strip())
                else:
                    self.size_literal(i, v)
            for m in re.finditer(r"(?<![\w-])font-family\s*:\s*([^;\"}]+)", decl_text):
                self.family_literal(i, m.group(1))
            for m in re.finditer(r"(?<![\w-])(transition(?:-[a-z]+)*|animation(?:-[a-z]+)*)\s*:\s*([^;\"}]+)", decl_text):
                self.motion_value(i, m.group(1), m.group(2))
            for m in re.finditer(r"--wp--preset--color--([\w-]+)", decl_text):
                self.colour_slug(i, m.group(1), "var(%s)" % m.group(0))
            # literal colours anywhere in declarations (and in JSON handled above)
            colour_scope = decl_text
            for m in re.finditer(r"#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)|hsla?\([^)]*\)", colour_scope):
                if m.group(0).startswith("hsl"):
                    self.add(i, "colour", m.group(0), "–", "FAIL", "use the palette hex")
                    continue
                if not is_css and re.search(r'"(?:text|background)"\s*:\s*"%s"' % re.escape(m.group(0)), line):
                    continue
                self.colour_literal(i, m.group(0))
            if is_css:
                for m in re.finditer(r"(?<![\w-])(color|background(?:-color)?|border(?:-[a-z]+)*-color|outline(?:-color)?|fill|stroke|text-decoration-color)\s*:\s*([^;}]+)", low):
                    v = m.group(2).strip()
                    if v in ("white",):
                        self.add(i, "colour", "white", "color.base", "REVIEW", "write #FFFFFF so the gate can grade it")
                    elif v in ("black",):
                        self.add(i, "colour", "black", "–", "FAIL", "use contrast #0d1b2a")
                    elif re.fullmatch(r"[a-z]+", v) and v not in ("transparent", "currentcolor", "inherit", "initial", "none", "unset", "solid", "dashed", "dotted"):
                        self.add(i, "colour", v, "–", "FAIL", "named colour is off-palette")
                # custom class prefix
                for m in re.finditer(r"\.([a-zA-Z_][\w-]*)", re.sub(r"\{[^}]*\}", "", line)):
                    c = m.group(1)
                    if re.match(r"(wcm-|wp-|has-|is-|align|entry-|site-|home\b|ds-)", c):
                        continue
                    if re.match(r"^\d", c):
                        continue
                    self.add(i, "naming", "." + c, "–", "REVIEW", "custom classes should be prefixed wcm-")
                if "@media (prefers-reduced-motion" in low:
                    self.add(i, "motion", "prefers-reduced-motion guard", "motion", "PASS")
        if is_css:
            has_motion = any(k[0] == "motion" and k[1] != "prefers-reduced-motion guard" for k in self.rows)
            has_guard = any(k[1] == "prefers-reduced-motion guard" for k in self.rows)
            if has_motion and not has_guard:
                self.add(0, "motion", "no prefers-reduced-motion guard", "motion", "FAIL", "wrap transitions in @media (prefers-reduced-motion: reduce)")
        return self

    # ----------------------------------------------------------------------
    def table(self):
        order = {"STRIP": 0, "FAIL": 1, "REVIEW": 2, "PASS": 3}
        rows = sorted(self.rows.items(), key=lambda kv: (order[kv[1]["result"]], kv[0][0], kv[1]["lines"][0]))
        out = ["| Result | Category | Found | Token | Lines | Note |", "|---|---|---|---|---|---|"]
        for (cat, found, _res), r in rows:
            lines = r["lines"]
            ls = ", ".join(str(l) for l in lines[:5]) + (" +%d" % (len(lines) - 5) if len(lines) > 5 else "")
            out.append("| %s | %s | `%s` | %s | %s | %s |" % (r["result"], cat, found.replace("|", "\\|"), r["token"], ls, r["note"]))
        return "\n".join(out)

    def counts(self):
        c = {"PASS": 0, "REVIEW": 0, "FAIL": 0, "STRIP": 0}
        for r in self.rows.values():
            c[r["result"]] += 1
        return c


def main(argv):
    summary_only = "--summary" in argv
    strict = "--strict" in argv
    files = [a for a in argv if not a.startswith("--")]
    if not files:
        print(__doc__)
        return 2
    worst = 0
    for f in files:
        rep = Report(f).scan()
        c = rep.counts()
        rel = os.path.relpath(f, REPO)
        if rel.startswith(".."):
            rel = f
        print("### report: %s" % rel)
        print()
        if not summary_only:
            if rep.rows:
                print(rep.table())
            else:
                print("(no gradeable values found)")
            print()
        verdict = "FAIL" if (c["FAIL"] or c["STRIP"]) else ("REVIEW" if c["REVIEW"] else "PASS")
        print("**%s** · %d PASS · %d REVIEW · %d FAIL · %d STRIP" % (verdict, c["PASS"], c["REVIEW"], c["FAIL"], c["STRIP"]))
        print()
        if c["FAIL"] or c["STRIP"]:
            worst = max(worst, 1)
        elif strict and c["REVIEW"]:
            worst = max(worst, 1)
    return worst


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
