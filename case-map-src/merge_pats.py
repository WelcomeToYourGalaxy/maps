"""python3 merge_pats.py rounds/r44_graduate_checked.json [...] -- graduations and merges.

Written round 44. Applies three things to base.html, all or nothing:
  pats_add    [ {...} ]  new documented patterns. Each must carry the fields every existing
                         PATS entry has — id, title, kind, years, summary, implications,
                         countries — and its id must not already exist. A `counts` or
                         `computed` block is allowed but never required: only one of the
                         thirteen original patterns has one, so a graduated pattern does not
                         need a number to be a pattern.
  pats_edits  [ {"id","field","old","new"} ] or {"id","append_to","value"}
  hyps_edits  { "<hyps id>": {"status","graduated_to","edits":[{field,old,new}]} }

Every string edit must match exactly once. A near match is refused and nothing is written,
because an edit that silently misses leaves the old text on the page while the round reports
it changed. Run merge_hyps.py for story-only fixes; this script is for the structural moves.
"""
import json, sys, os, shutil, datetime, copy

S = os.path.dirname(os.path.abspath(__file__)) + "/"
P = S + "base.html"
s = open(P, encoding="utf-8").read()
dec = json.JSONDecoder()
ip = s.index("window.PATS = ") + 14
PA, np_ = dec.raw_decode(s[ip:])
ih = s.index("window.HYPS = ") + 14
HY, nh = dec.raw_decode(s[ih:])
ic = s.index("window.CASES = ") + 15
CA, _ = dec.raw_decode(s[ic:])
case_ids = {c["id"] for c in CA}
Pix = {p["id"]: p for p in PA}
Hix = {h["id"]: h for h in HY}
REQUIRED = ("id", "title", "kind", "years", "summary", "implications", "countries")

refused, added, pedits, hedits = [], [], 0, 0
snapshot = (copy.deepcopy(PA), copy.deepcopy(HY))

for path in sys.argv[1:]:
    R = json.load(open(path, encoding="utf-8"))

    for p in R.get("pats_add") or []:
        pid = p.get("id")
        ch = (p.get("check") or {}).get("verdict")
        if ch == "cut":
            refused.append((pid, "check verdict: cut")); continue
        if not pid or pid in Pix:
            refused.append((pid, "missing id or id already exists")); continue
        miss = [k for k in REQUIRED if not p.get(k)]
        if miss:
            refused.append((pid, "missing required field(s): %s" % miss)); continue
        bad = [c for c in (p.get("case_ids") or []) if c not in case_ids]
        if bad:
            refused.append((pid, "case_ids not on the map: %s" % bad)); continue
        p.pop("check", None)
        PA.append(p); Pix[pid] = p; added.append(pid)
        print("pats_add  %-34s countries=%d sources=%d%s" % (
            pid[:34], len(p.get("countries") or []), len(p.get("sources") or []),
            "  counts" if ("counts" in p or "computed" in p) else ""))

    for e in R.get("pats_edits") or []:
        pid = e.get("id")
        if pid not in Pix:
            refused.append((pid, "pats_edits: no such pattern")); continue
        rec = Pix[pid]
        if e.get("append_to"):
            f = e["append_to"]
            cur = rec.get(f)
            if cur is None:
                rec[f] = []
                cur = rec[f]
            if not isinstance(cur, list):
                refused.append((pid, "append_to %s is not a list" % f)); continue
            if e.get("value") not in cur:
                cur.append(e["value"]); pedits += 1
            continue
        f, old, new = e.get("field"), e.get("old"), e.get("new")
        cur = rec.get(f)
        if isinstance(cur, list):
            refused.append((pid, "field %s is a list — use append_to" % f)); continue
        cur = cur if isinstance(cur, str) else ("" if cur is None else str(cur))
        if old in (None, ""):
            if cur.strip():
                refused.append((pid, "%s: empty old on a non-empty field" % f)); continue
            rec[f] = new; pedits += 1; continue
        if cur.count(old) != 1:
            refused.append((pid, "%s: old matches %d times" % (f, cur.count(old)))); continue
        rec[f] = cur.replace(old, new); pedits += 1

    for k, v in (R.get("hyps_edits") or {}).items():
        if k not in Hix:
            refused.append((k, "hyps_edits: no such entry")); continue
        rec = Hix[k]
        ok = True
        for e in v.get("edits") or []:
            f, old, new = e.get("field"), e.get("old"), e.get("new")
            if f == "story":
                total = sum((p.count(old) if isinstance(p, str) else 0)
                            for p in rec.get("story") or [])
                hits = [i for i, p in enumerate(rec.get("story") or [])
                        if isinstance(p, str) and p.count(old) == 1]
                if total != 1 or len(hits) != 1:
                    refused.append((k, "story old matches %d times" % total)); ok = False; continue
                rec["story"][hits[0]] = rec["story"][hits[0]].replace(old, new)
            elif f in ("conviction", "title", "would_settle", "missing"):
                cur = rec.get(f) or ""
                if cur.count(old) != 1:
                    refused.append((k, "%s old matches %d times" % (f, cur.count(old))))
                    ok = False; continue
                rec[f] = cur.replace(old, new)
            else:
                refused.append((k, "field not editable: %s" % f)); ok = False
        if not ok:
            continue
        if v.get("status"):
            rec["status"] = v["status"]
        if v.get("graduated_to"):
            if v["graduated_to"] not in Pix:
                refused.append((k, "graduated_to names no pattern: %s" % v["graduated_to"]))
                continue
            rec["graduated_to"] = v["graduated_to"]
        hedits += 1
        print("hyps      %-34s status=%-11s -> %s" % (
            k[:34], rec.get("status", "-"), rec.get("graduated_to", "-")))

if refused:
    print("\nREFUSED %d — nothing written" % len(refused))
    for r in refused:
        print("  ", r)
    sys.exit(1)

shutil.copy(P, P + ".bak-" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
s = s[:ih] + json.dumps(HY, ensure_ascii=False, separators=(",", ":")) + s[ih + nh:]
s2 = open(P, encoding="utf-8").read()  # re-locate PATS after the HYPS splice
ip2 = s.index("window.PATS = ") + 14
_, np2 = dec.raw_decode(s[ip2:])
s = s[:ip2] + json.dumps(PA, ensure_ascii=False, separators=(",", ":")) + s[ip2 + np2:]
open(P, "w", encoding="utf-8").write(s)
print("\npatterns added %d %s" % (len(added), added))
print("pattern edits %d ; hyps entries touched %d" % (pedits, hedits))
print("PATS now %d ; HYPS now %d" % (len(PA), len(HY)))
