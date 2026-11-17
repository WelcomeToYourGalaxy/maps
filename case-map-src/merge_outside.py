"""python3 merge_outside.py rounds/r40_x_checked.json [...] -- applies an outside-sourcing round.

Built for round 40. Each record is keyed by case id and may carry:
  confidence         "documented" | "contested"   (set only where the check allows it)
  confidence_note    replacement string, or null to keep the existing one
  sources_add        [{title, publisher, year, url}]  (deduped on url)
  field_changes      {"<top-level field or path>": <new value>}
  check              {"verdict": ...}  -- a record whose verdict is "cut" is skipped

It refuses to promote a card to `documented` unless the record carries at least one added source,
because a promotion with no outside source is the thing this round exists not to do. It prints every
change it makes and every one it refuses.
"""
import json, re, sys, os, shutil, datetime

S = os.path.dirname(os.path.abspath(__file__)) + "/"
P = S + "base.html"
shutil.copy(P, P + ".bak-" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
s = open(P, encoding="utf-8").read()
dec = json.JSONDecoder()
i = s.index("window.CASES = ") + 15
C, n = dec.raw_decode(s[i:])
B = {c["id"]: c for c in C}

def walk(obj, path):
    parts = re.findall(r"[^.\[\]]+|\[\d+\]", path)
    for p in parts[:-1]:
        obj = obj[int(p[1:-1])] if p.startswith("[") else obj[p]
    last = parts[-1]
    return obj, (int(last[1:-1]) if last.startswith("[") else last)

applied, refused, promoted = 0, [], []
for path in sys.argv[1:]:
    R = json.load(open(path, encoding="utf-8"))
    for k, v in R.items():
        if not isinstance(v, dict):
            continue
        chk = v.get("check") or {}
        if chk.get("verdict") == "cut":
            refused.append((k, "check verdict: cut"))
            continue
        if k not in B:
            refused.append((k, "no such case"))
            continue
        rec = B[k]
        adds = [x for x in (v.get("sources_add") or [])
                if x.get("url") and not any(
                    y.get("url") == x.get("url") for y in rec.get("sources") or [])]
        want = v.get("confidence")
        if want == "documented" and rec.get("confidence") != "documented":
            if not (v.get("sources_add") or []):
                refused.append((k, "promotion to documented with no added source"))
                want = None
            else:
                promoted.append(k)
        if want in ("documented", "contested"):
            rec["confidence"] = want
        if v.get("confidence_note"):
            rec["confidence_note"] = v["confidence_note"]
        for x in adds:
            rec.setdefault("sources", []).append(x)
        for f, nv in (v.get("field_changes") or {}).items():
            try:
                o, key = walk(rec, f)
                if isinstance(o, dict):
                    o[key] = nv
                else:
                    o[key] = nv
            except Exception as e:
                refused.append((k, "field_changes %s: %s" % (f, e)))
        applied += 1
        print("%-52s %-10s +%d sources%s" % (
            k[:52], rec.get("confidence"), len(adds),
            "  " + ", ".join((v.get("field_changes") or {}).keys())
            if v.get("field_changes") else ""))

s = s[:i] + json.dumps(C, ensure_ascii=False, separators=(",", ":")) + s[i + n:]
open(P, "w", encoding="utf-8").write(s)
print("\nrecords applied", applied, "; promoted to documented", len(promoted), promoted)
print("refused", len(refused))
for r in refused:
    print("  ", r)
conf = {}
for c in C:
    conf[c.get("confidence")] = conf.get(c.get("confidence"), 0) + 1
print("confidence now:", conf)
