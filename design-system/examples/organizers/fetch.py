#!/usr/bin/env python3
"""Pull the published organisers from the site into organizers.json.

Reads the public REST endpoint (no login needed), keeps any links you have
filled in by hand (linkedin, x, website) for a person already in the file,
and writes the list back sorted by name. Run, then python3 build.py.
"""
import json
import os
import re
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "organizers.json")
API = "https://mumbai.wordcamp.org/2027/wp-json/wp/v2/organizers?per_page=100&_embed=wp:featuredmedia&orderby=title&order=asc"


def text(html):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)).replace("&#8217;", "’").replace("&#8211;", "–").replace("&amp;", "&").strip()


def main():
    old = {}
    if os.path.exists(OUT):
        old = {o["slug"]: o for o in json.load(open(OUT))}
    req = urllib.request.Request(API, headers={"User-Agent": "wcm-design-system fetch.py"})
    data = json.load(urllib.request.urlopen(req))
    people = []
    for o in data:
        media = (o.get("_embedded", {}).get("wp:featuredmedia") or [None])[0]
        photo = None
        if media and media.get("media_details", {}).get("sizes"):
            sizes = media["media_details"]["sizes"]
            pick = sizes.get("medium_large") or sizes.get("large") or sizes.get("full") or sizes.get("medium")
            photo = {"id": media["id"], "url": pick["source_url"], "alt": media.get("alt_text") or ""}
        prev = old.get(o["slug"], {})
        people.append({
            "id": o["id"],
            "name": text(o["title"]["rendered"]),
            "slug": o["slug"],
            "profile": o["link"],
            "wporg": o.get("meta", {}).get("_wcpt_user_name", ""),
            "bio": text(o["content"]["rendered"]),
            "photo": photo,
            "links": prev.get("links", {"linkedin": "#", "x": "#", "website": "#"}),
        })
    people.sort(key=lambda p: p["name"].lower())
    with open(OUT, "w") as fh:
        json.dump(people, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    print("wrote %d organisers to %s" % (len(people), os.path.relpath(OUT)))


if __name__ == "__main__":
    main()
