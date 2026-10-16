#!/usr/bin/env python3
"""Generate countdown.svg: a self-ticking countdown to WordCamp Mumbai 2027 with no JavaScript.
Each digit is a vertical strip of glyphs moved by a CSS steps() animation whose negative delay
aligns it to the exact remaining time at generation. Regenerated on a schedule by GitHub Actions."""
import datetime as dt, sys, pathlib
EVENT = dt.datetime(2027, 2, 13, 9, 0, tzinfo=dt.timezone(dt.timedelta(hours=5, minutes=30)))  # 13 Feb 2027, 09:00 IST
now = dt.datetime.now(dt.timezone.utc)
R = int((EVENT - now).total_seconds())
out = pathlib.Path(__file__).parent.parent / 'site' / 'countdown.svg'
out.parent.mkdir(exist_ok=True)

W, H = 400, 120
NAVY, BLUE, PURPLE, LIGHT = '#1A2447', '#0A6CB5', '#5B2DB8', '#AFC0D4'
FONT = "font-family=\"'Figtree','Segoe UI',system-ui,Arial,sans-serif\""

def strip(x, y, glyphs, cls, w):
    """A clipped window showing one glyph at a time from a vertical strip."""
    gh = 54
    cid = f'c{cls}'
    g = f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="{w}" height="{gh}" rx="8"/></clipPath>'
    g += f'<rect x="{x}" y="{y}" width="{w}" height="{gh}" rx="8" fill="#FFFFFF"/>'
    g += f'<g clip-path="url(#{cid})"><g class="{cls}">'
    for i, t in enumerate(glyphs):
        g += f'<text x="{x + w/2}" y="{y + i*gh + 40}" text-anchor="middle" font-size="40" font-weight="800" fill="{NAVY}" {FONT}>{t}</text>'
    g += '</g></g>'
    return g

if R <= 0:
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"><rect width="{W}" height="{H}" rx="20" fill="#FFFFFF" fill-opacity=".85"/><text x="{W/2}" y="70" text-anchor="middle" font-size="40" font-weight="800" fill="{BLUE}" {FONT}>WordCamp Mumbai is today!</text></svg>'''
else:
    days = R // 86400; r_day = R % 86400
    hours = (R // 3600) % 24; r_hour = R % 3600
    mins = (R // 60) % 60; r_min = R % 60
    secs = R % 60
    css = []
    parts = []
    gh = 54
    # DAYS: non-cyclic strip from `days` down to 0, one step per day, stops at 0
    x = 20
    glyphs = [str(d) for d in range(days, -1, -1)]
    parts.append(strip(x, 16, glyphs, 'd', 118))
    if days > 0:
        css.append(f'.d{{animation:ad {days*86400}s steps({days},end) forwards;animation-delay:-{86400 - r_day - 1}s}}@keyframes ad{{from{{transform:translateY(0)}}to{{transform:translateY(-{days*gh}px)}}}}')
    # HOURS: cyclic 23..00 (two-digit), one step per hour
    x += 118 + 34
    hg = [f'{h:02d}' for h in range(23, -1, -1)] + ['23']
    parts.append(strip(x, 16, hg, 'h', 84))
    k = 23 - hours
    css.append(f'.h{{animation:ah 86400s steps(24,end) infinite;animation-delay:-{k*3600 + (3600 - r_hour - 1)}s}}@keyframes ah{{from{{transform:translateY(0)}}to{{transform:translateY(-{24*gh}px)}}}}')
    # MINUTES: tens (5..0) and units (9..0)
    x += 84 + 34
    mt, mu = mins // 10, mins % 10
    parts.append(strip(x, 16, [str(v) for v in range(5, -1, -1)] + ['5'], 'mt', 40))
    parts.append(strip(x + 44, 16, [str(v) for v in range(9, -1, -1)] + ['9'], 'mu', 40))
    css.append(f'.mt{{animation:amt 3600s steps(6,end) infinite;animation-delay:-{(5-mt)*600 + (600 - (R % 600) - 1)}s}}@keyframes amt{{from{{transform:translateY(0)}}to{{transform:translateY(-{6*gh}px)}}}}')
    css.append(f'.mu{{animation:amu 600s steps(10,end) infinite;animation-delay:-{(9-mu)*60 + (60 - r_min - 1)}s}}@keyframes amu{{from{{transform:translateY(0)}}to{{transform:translateY(-{10*gh}px)}}}}')
    labels = [(20+59, 'DAYS'), (20+118+34+42, 'HOURS'), (20+118+34+84+34+42, 'MINUTES')]
    lab = ''.join(f'<text x="{lx}" y="98" text-anchor="middle" font-size="13" font-weight="700" letter-spacing="2" fill="{BLUE}" {FONT}>{t}</text>' for lx, t in labels)
    colons = ''.join(f'<g fill="{PURPLE}"><circle cx="{cx}" cy="34" r="4"/><circle cx="{cx}" cy="54" r="4"/></g>' for cx in (20+118+17, 20+118+34+84+17))
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{days} days, {hours} hours and {mins} minutes to WordCamp Mumbai 2027">'
           f'<style>{"".join(css)}@media (prefers-reduced-motion:reduce){{.d,.h,.mt,.mu{{animation-play-state:paused}}}}</style>'
           f'<defs></defs>{"".join(parts)}{colons}{lab}</svg>')
out.write_text(svg)
print(f'R={R}s  {days}d {hours:02d}:{mins:02d}  -> {out.name} ({len(svg)} bytes)')
