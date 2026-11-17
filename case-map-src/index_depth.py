#!/usr/bin/env python3
"""How deep is a national judgment index on this map's own subject?

Round 40 found that the eleven peachjam indexes serve the same route and are
nothing like the same depth, and that depth on one phrase predicts whether an
outside-sourcing round will yield in that country. Run this before committing a
round to a country, not after.

  python3 case-map-src/index_depth.py            # the standing phrase set
  python3 case-map-src/index_depth.py "<phrase>" # one phrase
"""
import json, re, sys, time, urllib.request, urllib.parse, html

UA = {"User-Agent": "Mozilla/5.0 (research; welcometoyourgalaxy maps)"}
HOSTS = ["kenyalaw.org", "tanzlii.org", "ulii.org", "ghalii.org", "zambialii.org",
         "malawilii.org", "lesotholii.org", "nigerialii.org", "zimlii.org",
         "namiblii.org", "sierralii.org", "africanlii.org"]
PHRASES = sys.argv[1:] or ["Resettlement Action Plan", "compulsory acquisition compensation",
                           "World Bank", "Land Acquisition Tribunal"]

def q(host, phrase):
    u = ("https://%s/search/api/documents/?search=%s"
         % (host, urllib.parse.quote('"%s"' % phrase)))
    d = json.load(urllib.request.urlopen(
        urllib.request.Request(u, headers=UA), timeout=45))
    hits = []
    for href, t in re.findall(r'href="(/akn/[^"]+)"[^>]*>(.*?)</a>',
                              d.get("results_html", ""), re.S):
        t = re.sub(r"\s+", " ", html.unescape(re.sub("<[^>]+>", "", t))).strip()
        if t and t.lower() not in ("download", "pdf") and not t.startswith("Page"):
            hits.append({"url": "https://%s%s" % (host, href), "title": t[:200]})
    return d["count"], hits[:5]

out = {}
for host in HOSTS:
    out[host] = {}
    for p in PHRASES:
        try:
            c, h = q(host, p)
            out[host][p] = {"count": c, "sample": h}
            print("%-15s %-40s %s" % (host, p[:40], c), flush=True)
        except Exception as e:
            out[host][p] = {"error": "%s: %s" % (type(e).__name__, e)}
            print("%-15s %-40s FAIL %s" % (host, p[:40], type(e).__name__), flush=True)
        time.sleep(1)
json.dump(out, open("case-map-src/docs/index_depth.json", "w"), indent=1,
          ensure_ascii=False)
print("\nwrote case-map-src/docs/index_depth.json")
print("Quote the phrase. Unquoted these searches are relevance-ranked and capped "
      "at 10,000, which says nothing about depth.")
