import json,re
UNION={"ECB":["AUT","BEL","BGR","HRV","CYP","EST","FIN","FRA","DEU","GRC","IRL","ITA","LVA","LTU","LUX","MLT","NLD","PRT","SVK","SVN","ESP"],
"BCEAO":["BEN","BFA","CIV","GNB","MLI","NER","SEN","TGO"],"BEAC":["CMR","CAF","TCD","COG","GNQ","GAB"],
"ECCB":["AIA","ATG","DMA","GRD","MSR","KNA","LCA","VCT"]}
MEM={m:u for u,ms in UNION.items() for m in ms}
# NEVER read a cached absent list. At round 49 this script parsed a stale /tmp/cov45.txt and sent an
# agent to research union printer ties that had been on the map since round 45, and the stale figures
# reached the user: they were told 17 union records would close 143 cells when the live number was 11
# records and 98 cells. The round-49 handoff recorded that this was fixed; it was not -- the fix was
# lost with its session, the same way merge_links.py and check_scores.py were. Fixed again at round 56.
# Run coverage.py in the same session, every time.
import subprocess, os, sys
_here = os.path.dirname(os.path.abspath(__file__))
_cov = os.path.join(_here, 'coverage.py')
_r = subprocess.run([sys.executable, _cov], capture_output=True, text=True)
if _r.returncode != 0:
    sys.exit("coverage.py failed:\n" + _r.stderr)
txt = _r.stdout
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
