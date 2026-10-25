import csv, json, re, datetime, collections
W = "/home/claude/work/imfarch/"; DL = "/home/claude/dl/imfarch/"
def clean(s): return re.sub(r"-\s*\n\s*", "", s).replace("\n", " ").replace("\x0c", " ")
def load_docs(path):
    docs = [dict(zip(["c","d","t","k","cat","pdf"], r)) for r in list(csv.reader(open(path)))[1:]]
    for x in docs:
        x["id"] = x["pdf"].rsplit("/", 1)[1].split(".")[0]; x["d"] = datetime.date.fromisoformat(x["d"])
        try: x["T"] = re.sub(r"\s+", " ", clean(open(DL + x["id"] + ".txt", errors="ignore").read()))
        except FileNotFoundError: x["T"] = ""
    return docs
NUMP = re.compile(r"(?:(?<=\s)|^)(\d{1,2})\.\s+(?=[A-Z(\"'])")
def paras(seg):
    # split a stretch of text into its numbered paragraphs {n: text}; keeps the first run 1,2,3...
    ms = list(NUMP.finditer(seg)); out = {}; exp = 1
    for i, m in enumerate(ms):
        n = int(m.group(1))
        if n == 1 and exp > 3: break   # numbering starts again: a new document
        if n not in (exp, exp + 1): continue
        end = next((mm.start() for mm in ms[i+1:] if int(mm.group(1)) in (n + 1, n + 2)), len(seg))
        out[n] = seg[m.end():end]; exp = n + 1
    return out
ARR_HEAD = re.compile(r"Stand-?\s?By Arrangement\s*-\s*[A-Z]|Extended Arrangement\s*-\s*[A-Z]|STAND-?BY ARRANGEMENT\s*-?\s*[A-Z]{3}|Annexed hereto is a letter|Attached hereto is a letter|The attached letter", re.I)
TRIG = re.compile(r"reappraisal|situations? (?:should )?arises?|reach(?:es|ed)? the amount|not (?:being )?(?:observed|met|carried out|in effect|implemented|reached|maintained)|(?:are|is|been|be) exceeded|exceeds?|differs? from|falls? below|introduc\w+ .{0,60}restrictions|multiple currency", re.I)
SAL = re.compile(r"D\w?ear [^:]{2,30}:|Memorandum (?:of|on)|MEMORANDUM|Technical Memorandum")
OPEN = re.compile(r"D\w{2,5}g (?:any|the) p\S{1,8}d|If (?:\([a-z0-9]\) )?at any time|If \(i\)|in the event|whenever|If the data|(?:will|shall) not (?:make|request) (?:any )?purchases?", re.I)
SKIP = re.compile(r"Not later than|The rate of exchange|Repurchases|For a period of|[A-Z][\w ,.]{0,40} will remain in close consultation|[A-Z][\w ,.]{0,40} will pay charges", re.I)
BIND = re.compile(r"(?:prior to|before) (?:making |requesting )?(?:any )?further (?:drawings?|purchases?)|not (?:request|make) any (?:further )?drawings?|(?:will|shall) not (?:make|request|engage)|not (?:to )?request any purchase|purchases? [^.]{0,120}(?:suspended|not be made|interrupt)|without (?:the )?(?:prior )?(?:consent|approval) of the Fund[^.]{0,80}purchase|will not (?:make|request) (?:any )?(?:further )?purchases?", re.I)
MARK = re.compile(r"(?:(?<=[,;:])|(?<=\bor)|(?<=\bwhich)|(?<=\band)|(?<=\bthat)|(?<=\bif)|(?<=\bwhen))\s*\((\d{1,2}|[a-h]|i{1,3}|iv|vi{0,3})\)[\s,]")
def items(p):
    parts = MARK.split(p)
    if len(parts) < 4: return [p]
    return [parts[i + 1].strip(" ;,") for i in range(1, len(parts) - 1, 2)]
TAIL = re.compile(r",?\s*(?:the Government of )?[A-Z][\w'. ]{1,40} will not (?:request|make)\b.*$|,?\s*[A-Z][\w'. ]{1,40} will consult the Fund.*$", re.S)
def kind_of(clause, src, binding):
    if not binding: return "IB/SB"
    if re.search(r"limits?|ceilings?|exceed|fall below|minimum|maximum|targets?|standards?|goals?|net (?:foreign|international|domestic)", clause, re.I): return "QPC"
    if re.search(r"intentions?|measures|not carried out|not in effect|not implemented|restrictions|multiple currency|exchange practice|differs", clause, re.I): return "SPC"
    return "QPC" if quant(src) else "SPC"
CAT = [("EXT", r"foreign exchange|effective rates?|current account|per U\.?\s?S\.? dollar|deferments?|import payments|multiple currency|exchange rate|exchange (?:and trade|system|market|practice|transactions)|trade system|restrictions?|net (?:foreign|international) (?:assets|reserves)|reserves|bilateral payments|imports?|exports?|payments for current|deposits? requirement"),
       ("DEB", r"arrears|external (?:debt|borrowing|loans?|indebtedness|credits?)|foreign (?:debt|borrowing|loans?|indebtedness|credits?)|(?:contract|new) .{0,40}(?:loans?|debt|credits?) .{0,40}(?:abroad|foreign|maturit)|suppliers.? credits|maturities"),
       ("FP",  r"(?:credit|lending|financing) to the (?:government|public sector|treasury|central government)|net (?:credit|claims) .{0,40}(?:government|public sector|treasury)|budget|deficit|government (?:borrowing|expenditure|spending)|fiscal|treasury"),
       ("FIN", r"reserve requirements?|credit|domestic assets|money|central bank|banking system|rediscount|interest rate|banks?"),
       ("RTP", r"tax|revenue"), ("LAB", r"wages?|salar"), ("SOE", r"prices?|enterprises?|tariffs?|subsid")]
ORDER = ["DEB", "EXT", "FP", "RTP", "LAB", "SOE", "FIN"]
def cat(s):
    # the paragraph's opening sentences name its subject; check areas in a fixed order, banking last
    s = s[:350]
    if re.search(r"reserve requirements?", s, re.I) and not re.search(r"foreign exchange|exchange rate", s, re.I): return "FIN"
    for k in ORDER:
        if re.search(dict(CAT)[k], s, re.I): return k
    return "OTH"
def quant(s): return bool(re.search(r"ceiling|exceed|fall below|limit|million|minimum|maximum|not more than|not less than|per cent|percent|\$|SDR", s, re.I))

def code(arr_rows, docs, out_path):
    out = []
    for a in arr_rows:
        iso, c, fac, ap = a[0], a[1], a[2], datetime.date.fromisoformat(a[3])
        cand = [x for x in docs if x["c"] == c and -15 <= (ap - x["d"]).days <= 240]
        if not any(x["c"] == c for x in docs): continue
        rec = {"iso3": iso, "country": c, "facility": fac, "approved": a[3], "docs": [[x["d"].isoformat(), x["t"], x["pdf"]] for x in sorted(cand, key=lambda x: x["d"])]}
        found = None
        # prefer the final board text, then the latest request paper
        for x in sorted(cand, key=lambda x: (not re.search(r"REQUEST|MODIF|REVIS|CONSULT|REVIEW|PURCHASE", x["t"], re.I), x["d"]), reverse=True):
            T = x["T"]
            starts = [m.start() for m in ARR_HEAD.finditer(T)] + [m.start() for m in SAL.finditer(T)]
            for st in starts:
                P = paras(T[st:st + 60000])
                if len(P) < 4: continue
                trig = [(n, p) for n, p in P.items() if TRIG.search(p) and OPEN.search(p[:400]) and re.search(r"purchase|consult", p, re.I) and n > 2 and not SKIP.match(p.strip())]
                if trig: found = (x, P, trig, st); break
            if found: break
        if not found:
            # fallback: the clause written as a free-standing sentence, wherever it is
            CLX = re.compile(r"(?:D\w{2,5}g (?:any|the) p\S{1,8}d[^.]{0,160}?in which|If (?:at any time|\(i\)|\(1\)))(?:(?!\.\s+\d{1,2}\.\s).){20,2500}?(?:(?:will|shall) not (?:request|make|draw)|(?:will|shall) consult)[^.]{0,400}\.", re.I)
            for x in sorted(cand, key=lambda x: len(x["T"]), reverse=True):
                T = x["T"]; m = next((m for m in CLX.finditer(T) if TRIG.search(m.group(0))), None)
                if m:
                    P = {}
                    for pm in NUMP.finditer(T[:m.start()]): P[int(pm.group(1))] = T[pm.end():pm.end() + 1500]
                    found = (x, P, [(0, m.group(0))], m.start()); break
        if not found:
            alltxt = " ".join(x["T"] for x in cand)
            rec["status"] = ("No board papers found in the IMF Archives for this loan" if not cand else
                "No binding conditions: first credit tranche" if re.search(r"first credit tranche", alltxt, re.I) and not re.search(r"beyond the first credit tranche|upper credit tranche|second credit tranche", alltxt, re.I) else
                "No binding conditions: emergency assistance" if "Emergency" in fac else
                "No conditions listed: the agreement names no targets" if any(len(paras(x["T"][m.start():m.start() + 25000])) >= 4 for x in cand for m in ARR_HEAD.finditer(x["T"])) and not re.search(r"ceiling|limits? (?:on|specified)|performance criteri", alltxt, re.I) else
                "Papers found, but they set out no list of conditions this rule can count; read the papers")
            out.append(rec); continue
        x, P, trig, at = found
        # the letter and memorandum come before or after the arrangement; read their numbered paragraphs
        letters = []
        for y in sorted(cand, key=lambda y: (y is x, bool(re.search("REQUEST", y["t"], re.I)), y["d"]), reverse=True):
            for m in list(SAL.finditer(y["T"]))[:4]:
                L = paras(y["T"][m.start():m.start() + 60000])
                if len(L) >= 3: letters.append(L)
        conds = []
        for n, p in trig:
            binding = bool(BIND.search(p))
            for it in items(p):
                cut = TAIL.sub("", it); it = cut if TRIG.search(cut) else it
                if len(it.strip()) < 15 or re.search(r"suspend transactions|formal ineligibility", it, re.I): continue
                if not binding and (not re.search(r"criteri|targets?|limits?|ceilings?|standards?|goals?|paragraph", it, re.I) or re.search(r"believes that the policies", it, re.I)): continue
                refs = [int(r) for grp in re.findall(r"(?i:paragraphs?) ((?:\(?\d{1,2}\)?(?:\s*\([a-z]\))?(?:\s*(?:,|and|to|or)\s*)*)+)", it) for r in re.findall(r"\d{1,2}", re.sub(r"\([a-z]\)", "", grp))]
                own = not re.search(r"annexed|attached|memorandum|letter", it, re.I) and bool(re.search(r"above|below", it))
                if refs:
                    for r in refs:
                        src = (P.get(r, "") if own else "") or next((L.get(r) for L in letters if L.get(r)), "")
                        ctx = it + " " + src[:900]
                        k = cat(re.sub(r"paragraphs?[\s\d(),a-z]*|annexed|attached|letter|memorandum", " ", it)) if len(refs) == 1 else "OTH"
                        conds.append({"kind": kind_of(it, src, binding),
                                      "area": k if k != "OTH" else (cat(src) if src else cat(re.sub(r"paragraphs?[\s\d(),a-z]*|annexed|attached|letter|memorandum", " ", it))), "clause": it.strip()[:400], "paragraph": r, "text": src.strip()[:1500]})
                else:
                    conds.append({"kind": kind_of(it, "", binding), "area": cat(it), "clause": it.strip()[:400], "paragraph": None, "text": ""})
        seen = set(); conds = [c_ for c_ in conds if not ((c_["paragraph"], c_["kind"]) in seen and c_["paragraph"] is not None or seen.add((c_["paragraph"], c_["kind"])))]
        if not conds:
            rec["status"] = "Papers found, but they set out no list of conditions this rule can count; read the papers"; out.append(rec); continue
        rec.update(status="Coded", source=[x["d"].isoformat(), x["t"], x["pdf"]], clauses=[[n, ("binding" if BIND.search(p) else "consultation"), p.strip()[:2500]] for n, p in trig], conditions=conds)
        out.append(rec)
    json.dump(out, open(out_path, "w"), indent=1)
    return out
if __name__ == "__main__":
    docs = load_docs(W + "imf_pre1981_documents_part1.csv")
    arr = json.load(open("/tmp/claude-0/-home-claude/a1308dfa-f9cb-5e0e-8aa6-7a243eefa01e/scratchpad/pre80.json"))
    o = code(arr, docs, W + "pre80_coded.json")
    print(len(o), collections.Counter(r["status"] for r in o), sum(len(r.get("conditions", [])) for r in o))
    print(collections.Counter((c["kind"], c["area"]) for r in o for c in r.get("conditions", [])).most_common(20))
