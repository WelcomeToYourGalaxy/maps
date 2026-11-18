"""python3 merge_hyps.py rounds/r43_hypfix_checked.json [...] -- applies checked edits to window.HYPS.

Written round 43, for fixing suspected-pattern cards rather than cases. Each record is keyed by the
entry's id and may carry:
  edits        [{"field": "story"|"conviction"|"title", "old": "...", "new": "..."}]
               story edits match against any one paragraph; an `old` must occur exactly once across
               the whole entry, or the edit is refused and nothing in that entry is written.
  sources_add  [{...}]  deduped on url
  case_ids_add ["id", ...]  each must exist in window.CASES, or it is refused
  check        {"verdict": ...}  a record whose verdict is "cut" is skipped

It refuses an edit rather than applying a near match, because a silent miss leaves the defect on the
page while the round reports it fixed. It prints every refusal and writes nothing unless every edit
in the file can be applied.
"""
import json, sys, os, shutil, datetime, copy

S = os.path.dirname(os.path.abspath(__file__)) + "/"
P = S + "base.html"
s = open(P, encoding="utf-8").read()
dec = json.JSONDecoder()
ih = s.index("window.HYPS = ") + 14
H, nh = dec.raw_decode(s[ih:])
ic = s.index("window.CASES = ") + 15
C, _ = dec.raw_decode(s[ic:])
case_ids = {c["id"] for c in C}
B = {h["id"]: h for h in H}

refused, applied, touched = [], 0, []
for path in sys.argv[1:]:
    R = json.load(open(path, encoding="utf-8"))
    for k, v in R.items():
        if not isinstance(v, dict):
            continue
        if (v.get("check") or {}).get("verdict") == "cut":
            refused.append((k, "check verdict: cut"))
            continue
        if k not in B:
            refused.append((k, "no such HYPS entry"))
            continue
        rec = B[k]
        before = copy.deepcopy(rec)
        ok = True
        for e in v.get("edits") or []:
            f, old, new = e.get("field"), e.get("old"), e.get("new")
            if f == "story":
                hits = [i for i, p in enumerate(rec.get("story") or [])
                        if isinstance(p, str) and p.count(old) == 1]
                total = sum((p.count(old) if isinstance(p, str) else 0)
                            for p in rec.get("story") or [])
                if total != 1 or len(hits) != 1:
                    refused.append((k, "story old matches %d times" % total)); ok = False; continue
                i = hits[0]
                rec["story"][i] = rec["story"][i].replace(old, new)
            elif f in ("conviction", "title", "would_settle", "missing"):
                cur = rec.get(f) or ""
                if cur.count(old) != 1:
                    refused.append((k, "%s old matches %d times" % (f, cur.count(old)))); ok = False; continue
                rec[f] = cur.replace(old, new)
            else:
                refused.append((k, "field not editable here: %s" % f)); ok = False
        for x in v.get("sources_add") or []:
            if x.get("url") and not any(y.get("url") == x.get("url")
                                        for y in rec.get("sources") or []):
                rec.setdefault("sources", []).append(x)
        for cid in v.get("case_ids_add") or []:
            if cid not in case_ids:
                refused.append((k, "case_ids_add: no such case %s" % cid)); ok = False; continue
            if cid not in (rec.get("case_ids") or []):
                rec.setdefault("case_ids", []).append(cid)
        if not ok:
            B[k].clear(); B[k].update(before)
            continue
        applied += 1
        touched.append(k)
        words = sum(len(p.split()) for p in (rec.get("story") or []) if isinstance(p, str))
        print("%-42s edits=%-3d sources+%-2d words=%d" % (
            k[:42], len(v.get("edits") or []), len(v.get("sources_add") or []), words))

if refused:
    print("\nREFUSED %d — nothing written" % len(refused))
    for r in refused:
        print("  ", r)
    sys.exit(1)

shutil.copy(P, P + ".bak-" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
s = s[:ih] + json.dumps(H, ensure_ascii=False, separators=(",", ":")) + s[ih + nh:]
open(P, "w", encoding="utf-8").write(s)
print("\nentries applied", applied, touched)
