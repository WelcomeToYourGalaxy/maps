import sys,json;import os;sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)));from sparql import q
tops={'hos':'Q48352','hog':'Q2285706','min':'Q83307','cbg':'Q107363151'}
allp={}
for k,t in tops.items():
    r=q(f'''SELECT DISTINCT ?pos ?j ?jt WHERE {{ ?pos wdt:P279* wd:{t}. OPTIONAL {{ ?pos wdt:P1001 ?j. OPTIONAL {{ ?j wdt:P31 ?jt. }} }} }}''')
    for b in r:
        p=b['pos'].rsplit('/',1)[1]; e=allp.setdefault(p,{'k':set(),'j':{}})
        e['k'].add(k)
        if 'j' in b:
            j=b['j'].rsplit('/',1)[1]; e['j'].setdefault(j,set())
            if 'jt' in b: e['j'][j].add(b['jt'].rsplit('/',1)[1])
    print(k,len(r),file=sys.stderr)
json.dump({p:{'k':sorted(v['k']),'j':{j:sorted(t) for j,t in v['j'].items()}} for p,v in allp.items()},open('data/positions_raw.json','w'))
print(len(allp))
