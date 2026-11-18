#!/usr/bin/env python3
"""Harvest OECD Watch's complaint register into a lead list."""
import re, html, json, os, sys, subprocess, concurrent.futures as cf

CACHE = "/tmp/oecdw/cache"
SM = "/tmp/oecdw/cs.xml"

def slugs():
    s = open(SM, encoding="utf-8").read()
    out = []
    for u in re.findall(r"<loc>([^<]*)</loc>", s):
        u = u.strip()
        m = re.match(r"https://oecdwatch\.org/complaint/([^/]+)/?$", u)
        if m:
            out.append((m.group(1), u))
    return out

def fetch(args):
    slug, url = args
    p = os.path.join(CACHE, slug + ".html")
    if os.path.exists(p) and os.path.getsize(p) > 20000:
        return slug, "cached"
    r = subprocess.run(["curl", "-sSL", "-m", "90", "-o", p, "-w", "%{http_code}", url],
                       capture_output=True, text=True)
    return slug, r.stdout.strip()

if __name__ == "__main__":
    sl = slugs()
    print("complaints in sitemap:", len(sl))
    ok = bad = 0
    with cf.ThreadPoolExecutor(max_workers=8) as ex:
        for i, (slug, code) in enumerate(ex.map(fetch, sl)):
            if code in ("200", "cached"):
                ok += 1
            else:
                bad += 1
                print("  FAIL", slug, code)
            if (i + 1) % 100 == 0:
                print(" ", i + 1, "done")
    print("fetched ok:", ok, "failed:", bad)
