import os, re, json, datetime
P = "/home/claude/dl/imfarch/p1/"
MON = "January|February|March|April|May|June|July|August|September|October|November|December"
out = {}
for f in os.listdir(P):
    t = open(P + f, errors="ignore").read()
    m = re.search(r"Subj\w*\s*[:;.]?\s*\n?\s*(.+?)(?:\n\s*\n|\n[A-Z][a-z]+ |\n\s*Attached|\n\s*The )", t, re.S)
    subj = re.sub(r"\s+", " ", m.group(1)).strip() if m else ""
    d = re.search(r"(%s)\s+(\d{1,2})\s*,\s*(19[4-8]\d)" % MON, t[:1500])
    dt = None
    if d:
        try: dt = datetime.datetime.strptime(f"{d.group(1)} {d.group(2)} {d.group(3)}", "%B %d %Y").date().isoformat()
        except ValueError: pass
    ref = re.search(r"\b(EBS|EBD|SM|EBM|EBAP|EB)/\s?(\d{2})/\s?(\d+)", t[:800])
    out[f[:-4]] = {"subject": subj[:300], "date": dt, "ref": ref.group(0) if ref else ""}
json.dump(out, open("/home/claude/work/imfarch/subjects.json", "w"))
hit = {k: v for k, v in out.items() if re.search(r"stand.?-?by|extended (?:arrangement|fund)|emergency assistance|compensatory|use of fund", v["subject"], re.I)}
print(len(out), "with subject:", sum(1 for v in out.values() if v["subject"]), "arrangement-related:", len(hit))
