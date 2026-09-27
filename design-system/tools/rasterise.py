#!/usr/bin/env python3
"""Rasterise SVG artwork to PNG at 2× with headless Chrome.

    rasterise.py <in.svg> [<in.svg> ...] [--out DIR] [--scale 2]

The SVG's width/height attributes (or viewBox) give the 1× size; the PNG is
written at scale× with a transparent background as <name>@2x.png. WordCamp.org
blocks SVG uploads, so this is how every icon, pattern tile and motif reaches
the media library or the CDN.
"""
import os
import re
import subprocess
import sys

CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")


def size_of(svg):
    m = re.search(r'viewBox="\s*[-\d.]+\s+[-\d.]+\s+([\d.]+)\s+([\d.]+)', svg)
    w = re.search(r'<svg[^>]*\swidth="([\d.]+)', svg)
    h = re.search(r'<svg[^>]*\sheight="([\d.]+)', svg)
    if w and h:
        return float(w.group(1)), float(h.group(1))
    if m:
        return float(m.group(1)), float(m.group(2))
    sys.exit("no size in svg")


def main(argv):
    out_dir = None
    scale = 2
    files = []
    i = 0
    while i < len(argv):
        if argv[i] == "--out":
            out_dir = argv[i + 1]; i += 2; continue
        if argv[i] == "--scale":
            scale = float(argv[i + 1]); i += 2; continue
        files.append(argv[i]); i += 1
    if not files:
        print(__doc__); return 2
    for f in files:
        svg = open(f).read()
        w, h = size_of(svg)
        W, H = int(round(w * scale)), int(round(h * scale))
        name = os.path.splitext(os.path.basename(f))[0]
        od = out_dir or os.path.dirname(os.path.abspath(f))
        os.makedirs(od, exist_ok=True)
        out = os.path.join(od, "%s@%gx.png" % (name, scale))
        wrap = os.path.join(od, ".raster-%s.html" % name)
        with open(wrap, "w") as fh:
            fh.write('<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;background:transparent}svg{display:block;width:%dpx;height:%dpx}</style></head><body>%s</body></html>' % (W, H, svg))
        # Chrome will not open a window narrower than 500px: render wider, then crop from the centre with sips.
        win_w = max(W, 520)
        wrap_html = open(wrap).read().replace("<body>", '<body style="display:flex;justify-content:center">')
        open(wrap, "w").write(wrap_html)
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--default-background-color=00000000",
                        "--window-size=%d,%d" % (win_w, H), "--screenshot=%s" % out, "file://" + os.path.abspath(wrap)],
                       capture_output=True)
        if win_w != W:
            subprocess.run(["sips", "-c", str(H), str(W), out, "--out", out], capture_output=True)
        os.remove(wrap)
        print("%s (%dx%d)" % (out, W, H))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
