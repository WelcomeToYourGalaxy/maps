import json, urllib.request, sys, time
def get(series, cp="WLD"):
    out=[]; page=1
    while True:
        u=f"https://api.worldbank.org/v2/sources/6/country/all/series/{series}/counterpart-area/{cp}/time/all?format=json&per_page=20000&page={page}"
        for k in range(4):
            try: d=json.load(urllib.request.urlopen(u,timeout=300)); break
            except Exception as e: time.sleep(5); d=None
        if not d: break
        for r in d["source"]["data"]:
            v={x["concept"]:x["id"] for x in r["variable"]}; nm={x["concept"]:x["value"] for x in r["variable"]}
            if r["value"] is not None: out.append([v["Country"],nm["Country"],int(v["Time"][2:]),v["Counterpart-Area"],nm["Counterpart-Area"],r["value"]])
        if page>=int(d["pages"]): break
        page+=1
    return out, d.get("lastupdated") if d else None
res={}
for s in sys.argv[1:]:
    cp="all" if s.endswith(":all") else "WLD"; s=s.split(":")[0]
    rows,lu=get(s,cp); res[s+("" if cp=="WLD" else ":all")]={"rows":rows,"lastupdated":lu}
    print(s,cp,len(rows),lu, flush=True)
json.dump(res,open("ids_"+("_".join(a.replace(":","-") for a in sys.argv[1:2]))+".json","w"))
