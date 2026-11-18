#!/usr/bin/env python3
import re, html, json, os, glob

CACHE = "/tmp/oecdw/cache"

LABELS = ["Date filed","Keywords","Countries of harm","Current status","Sector","Sectors","Status","NCP",
          "Allegations","Relevant OECD Guidelines","Outcome","More details","Defendant",
          "Company in violation","Other companies involved","Complainants","Affected people",
          "Date rejected / concluded","Documents","Related","Share this"]

def lines_of(path):
    s = open(path, encoding="utf-8", errors="replace").read()
    s = re.sub(r"(?s)<(script|style|noscript)[^>]*>.*?</\1>", " ", s)
    # keep the main article only, if identifiable
    s = re.sub(r"(?s)<[^>]+>", "\n", s)
    s = html.unescape(s)
    return [l.strip() for l in s.split("\n") if l.strip()]

def parse(path):
    L = lines_of(path)
    slug = os.path.basename(path)[:-5]
    # find the breadcrumb "Complaint" marker that precedes the title
    try:
        i = L.index("Complaints database")
    except ValueError:
        i = 0
    # title: the line after the breadcrumb trail, before "Complaint"
    try:
        j = L.index("Complaint", i)
        title = L[j + 1] if j + 1 < len(L) else ""
        sub = L[j + 2] if j + 2 < len(L) and L[j + 2] not in LABELS else ""
    except ValueError:
        title, sub = (L[i + 1] if i + 1 < len(L) else ""), ""
    d = {"slug": slug, "url": "https://oecdwatch.org/complaint/%s/" % slug,
         "title": title, "subtitle": sub}
    # label -> following lines until next label
    pos = {}
    for k, l in enumerate(L):
        if l in LABELS and l not in pos:
            pos[l] = k
    order = sorted(pos.items(), key=lambda kv: kv[1])
    for n, (lab, k) in enumerate(order):
        end = order[n + 1][1] if n + 1 < len(order) else len(L)
        vals = [x.rstrip(",") for x in L[k + 1:end]]
        d[lab] = vals
    return d

def one(d, lab, join=", "):
    v = d.get(lab) or []
    return join.join(v).strip()

out = []
for p in sorted(glob.glob(os.path.join(CACHE, "*.html"))):
    d = parse(p)
    rec = {
        "slug": d["slug"], "url": d["url"], "title": d["title"], "subtitle": d["subtitle"],
        "filed": one(d, "Date filed"),
        "keywords": d.get("Keywords") or [],
        "countries": d.get("Countries of harm") or [],
        "status": one(d, "Current status"),
        "sector": one(d, "Sector"),
        "ncp": one(d, "NCP"),
        "allegations": one(d, "Allegations", "\n"),
        "outcome": one(d, "Outcome", "\n"),
        "defendant": one(d, "Defendant"),
        "company_in_violation": one(d, "Company in violation"),
        "other_companies": d.get("Other companies involved") or [],
        "complainants": d.get("Complainants") or [],
        "affected": d.get("Affected people") or [],
        "concluded": one(d, "Date rejected / concluded"),
    }
    out.append(rec)

json.dump(out, open("/tmp/oecdw/oecdwatch_raw.json", "w"), indent=1, ensure_ascii=False)
print("parsed:", len(out))
import collections
for f in ["filed","countries","status","sector","allegations","outcome","defendant","keywords"]:
    n = sum(1 for r in out if r[f])
    print("  %-22s %d" % (f, n))
print("\nstatus spread:")
for k, v in collections.Counter(r["status"] for r in out).most_common(14):
    print("  %-40s %d" % (k[:40], v))
print("\ntop countries:")
cc = collections.Counter(c for r in out for c in r["countries"])
print("  distinct countries:", len(cc))
for k, v in cc.most_common(12):
    print("  %-28s %d" % (k, v))
