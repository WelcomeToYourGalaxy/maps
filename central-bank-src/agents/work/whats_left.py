import json,re
UNION={"ECB":["AUT","BEL","BGR","HRV","CYP","EST","FIN","FRA","DEU","GRC","IRL","ITA","LVA","LTU","LUX","MLT","NLD","PRT","SVK","SVN","ESP"],
"BCEAO":["BEN","BFA","CIV","GNB","MLI","NER","SEN","TGO"],"BEAC":["CMR","CAF","TCD","COG","GNQ","GAB"],
"ECCB":["AIA","ATG","DMA","GRD","MSR","KNA","LCA","VCT"]}
MEM={m:u for u,ms in UNION.items() for m in ms}
txt=open('/tmp/cov45.txt').read()
rows={}
for m in re.finditer(r'  (.+?) — (\d+) to go\n    (.+?)\n',txt):
    rows[m.group(1)]=m.group(3).split()
print("%-34s %5s %6s %7s %7s" % ("Row","left","union","single","other"))
print("%-34s %5s %6s %7s %7s" % ("","", "members","records",""))
for k,v in rows.items():
    byu={}
    other=0
    for c in v:
        u=MEM.get(c)
        if u: byu.setdefault(u,[]).append(c)
        else: other+=1
    um=sum(len(x) for x in byu.values())
    print("%-34s %5d %6d %7d %7d" % (k,len(v),um,len(byu),other))
    if byu:
        for u,cs in sorted(byu.items()):
            print("        %-6s %d countries: %s" % (u,len(cs)," ".join(cs)))
