import json, re, datetime, csv, collections, os, subprocess
from code_v2 import code
W = "/home/claude/work/imfarch/"; DL = "/home/claude/dl/imfarch/"
N = {"Afghanistan":["Afghanistan"],"Argentina":["Argentina"],"Australia":["Australia"],"Bangladesh":["Bangladesh"],"Belgium":["Belgium"],"Bolivia":["Bolivia"],"Brazil":["Brazil"],"Burundi":["Burundi"],"Chad":["Chad"],"Chile":["Chile"],"Colombia":["Colombia"],"Congo, Dem. Rep.":["Zaire","Democratic Republic of (?:the )?Congo","Congo \\(Kinshasa\\)","Republic of the Congo \\(Kinshasa\\)"],"Congo, Rep.":["People's Republic of (?:the )?Congo","Congo \\(Brazzaville\\)"],"Costa Rica":["Costa Rica"],"Cuba":["Cuba"],"Dominica":["Dominica(?!n)"],"Dominican Republic":["Dominican Republic"],"Ecuador":["Ecuador"],"Egypt, Arab Rep.":["Egypt","United Arab Republic"],"El Salvador":["El Salvador"],"Fiji":["Fiji"],"Finland":["Finland"],"France":["France"],"Gabon":["Gabon"],"Gambia, The":["Gambia"],"Ghana":["Ghana"],"Grenada":["Grenada"],"Guatemala":["Guatemala"],"Guyana":["Guyana"],"Haiti":["Haiti"],"Honduras":["Honduras"],"Iceland":["Iceland"],"India":["India(?!n)"],"Indonesia":["Indonesia"],"Iran, Islamic Rep.":["Iran"],"Israel":["Israel"],"Italy":["Italy"],"Jamaica":["Jamaica"],"Japan":["Japan"],"Kenya":["Kenya"],"Korea, Rep.":["Korea"],"Liberia":["Liberia"],"Madagascar":["Madagascar","Malagasy"],"Malawi":["Malawi"],"Mali":["Mali(?!an)"],"Mauritania":["Mauritania"],"Mauritius":["Mauritius"],"Mexico":["Mexico"],"Morocco":["Morocco"],"Myanmar":["Burma"],"Nepal":["Nepal"],"Netherlands":["Netherlands"],"New Zealand":["New Zealand"],"Nicaragua":["Nicaragua"],"Pakistan":["Pakistan"],"Panama":["Panama"],"Paraguay":["Paraguay"],"Peru":["Peru"],"Philippines":["Philippines"],"Portugal":["Portugal"],"Romania":["Romania"],"Rwanda":["Rwanda"],"Samoa":["Western Samoa"],"Senegal":["Senegal"],"Sierra Leone":["Sierra Leone"],"Somalia, Fed. Rep.":["Somalia"],"South Africa":["South Africa"],"Spain":["Spain"],"Sri Lanka":["Sri Lanka","Ceylon"],"Sudan":["Sudan"],"Syrian Arab Republic":["Syria(?:n Arab Republic)?"],"Tanzania":["Tanzania"],"Thailand":["Thailand"],"Togo":["Togo"],"Tunisia":["Tunisia"],"Turkiye":["Turkey"],"Uganda":["Uganda"],"United Kingdom":["United Kingdom"],"United States":["United States"],"Uruguay":["Uruguay"],"Venezuela, RB":["Venezuela"],"Yugoslavia (SFR)":["Yugoslavia"],"Zambia":["Zambia"]}
B = "https://stoprdcom01e2.blob.core.windows.net/allfiles/IG/Production%20Hosting/Adlib/Public%20Documents/EB/"
S = json.load(open(W + "subjects.json"))
REL = re.compile(r"stand.{0,3}[bB3]y|extended (?:arrangement|fund)|emergency assistance|use o\S{0,2}\W{0,3}(?:the\W{0,2})?f\w{2,3}d|renewal|purchase|drawing", re.I)
rows = []
for k, v in S.items():
    s = v["subject"]
    if not v["date"] or not (1950 <= int(v["date"][:4]) <= 1981): continue
    head = re.sub(r"\s+", " ", open(DL + "p1/" + k + ".txt", errors="ignore").read()[:1500])
    if not (REL.search(s) or (len(s) < 12 and REL.search(head))): continue
    if not any(re.search(r"\b" + n + r"\b", s, re.I) for ns in N.values() for n in ns): s = (s + " " + head)[:400]
    # the country named earliest in the subject line
    hits = [(m.start(), -len(m.group(0)), c) for c, ns in N.items() for n in ns for m in [re.search(r"\b" + n + r"\b", s, re.I)] if m]
    if hits: c = min(hits)[2]; rows.append([c, v["date"], s, "", B + k + ".PDF", k])
# add the 17 countries' catalog finds (their titles are cleaner) where the subject parse missed them
have = {r[5] for r in rows}
for r in list(csv.reader(open(W + "imf_pre1981_documents_part1.csv")))[1:]:
    k = r[5].rsplit("/", 1)[1].split(".")[0]
    if k not in have: rows.append([r[0], r[1], r[2], "", r[5], k])
print("documents:", len(rows), "countries:", len({r[0] for r in rows}))
# full text for every matched document
for r in rows:
    t = DL + r[5] + ".txt"
    if not os.path.exists(t) and os.path.exists(DL + r[5] + ".pdf"): subprocess.run(["pdftotext", "-layout", DL + r[5] + ".pdf", t], stderr=subprocess.DEVNULL)
with open(W + "imf_pre1981_documents.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["Country", "Date", "Title (as the IMF catalog gives it)", "Kind of document", "Catalog page", "PDF"])
    for r in sorted(rows): w.writerow([r[0], r[1], r[2], ("Request (staff paper with the government's letter)" if re.search(r"request", r[2], re.I) else "Board decision or arrangement text" if re.search(r"^[^-]+-\s*(?:stand-?by|extended) arrangement\s*$", r[2], re.I) else "Other paper on the arrangement"), "", r[4]])
from code_v2 import load_docs
docs = load_docs(W + "imf_pre1981_documents.csv")
arr = json.load(open("/tmp/claude-0/-home-claude/a1308dfa-f9cb-5e0e-8aa6-7a243eefa01e/scratchpad/pre80.json"))
o = code(arr, docs, W + "pre80_coded_all.json")
print(len(o), collections.Counter(r["status"] for r in o), sum(len(r.get("conditions", [])) for r in o))
