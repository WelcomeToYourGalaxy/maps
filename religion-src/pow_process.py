import glob, json, re, collections, datetime, sys
SRC = "/home/claude/pow/tiles3/*.tsv"
BAD_B = {"school", "kindergarten", "college", "university", "townhall"}
BAD_N = re.compile(r"\b(school|kindergarten|town ?hall|city ?hall|village hall)\b", re.I)
seen = set(); kept = 0; drop = collections.Counter(); rel = collections.Counter(); bad = 0
out = open("/home/claude/pow/pow.geojsonl", "w", encoding="utf-8")
for fn in sorted(glob.glob(SRC)):
    for line in open(fn, encoding="utf-8", errors="replace"):
        c = line.rstrip("\n").split("\t")
        if len(c) < 9: bad += 1; continue
        t, i, lat, lon, name, r, d, b, en = c[:9]
        key = t[:1] + i
        if key in seen: continue
        seen.add(key)
        try: lat = float(lat); lon = float(lon)
        except ValueError: bad += 1; continue
        if b.lower() in BAD_B: drop["tagged " + b.lower()] += 1; continue
        if BAD_N.search(name) or BAD_N.search(en): drop["name"] += 1; continue
        p = {}
        nm = name or en
        if nm: p["n"] = nm[:90]
        if r: p["r"] = r[:30]; 
        if d: p["d"] = d[:40]
        rel[r or "(not recorded)"] += 1
        out.write(json.dumps({"type": "Feature", "geometry": {"type": "Point", "coordinates": [round(lon, 5), round(lat, 5)]}, "properties": p}, ensure_ascii=False, separators=(",", ":")) + "\n"); kept += 1
out.close()
meta = {"file": "religion_pow.pmtiles", "total": kept, "dropped": sum(drop.values()), "drop": dict(drop), "rel": rel.most_common(12), "date": datetime.date.today().strftime("%-d %B %Y"), "bad": bad}
json.dump(meta, open("/home/claude/pow/pow_stats.json", "w"), indent=1); print(json.dumps(meta, indent=1))
