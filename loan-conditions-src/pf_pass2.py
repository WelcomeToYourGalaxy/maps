import json,re,time,sys
sys.path.insert(0,'/home/claude/work')
exec(open('/home/claude/work/pf_build.py').read().split('# 1. OSM features')[0])  # helpers: get, cache, UA
import urllib.parse
P=json.load(open('/home/claude/work/pf_rows.json'))
cases={c['id']:c for c in json.load(open(DIR+'pf_all.json'))}
cty={c['address']['country_code'].upper():[float(c['lon']),float(c['lat']),c['name']] for c in json.load(open(DIR+'countries.json')) if c.get('address',{}).get('country_code')}
def q(name,cc):
    key="S2|"+(cc or "")+"|"+name
    if key in cache: return cache[key]
    p={"q":name,"format":"json","limit":1}
    if cc:p["countrycodes"]=cc.lower()
    r=get("https://nominatim.openstreetmap.org/search?"+urllib.parse.urlencode(p)); time.sleep(1.1)
    v=[float(r[0]["lon"]),float(r[0]["lat"])] if r else None
    cache[key]=v; return v
exec(open('/home/claude/work/pf_build.py').read().split('def cls')[1].split('rows, unplaced')[0].join(['def cls','']))
still=[]
for u in P['unplaced']:
    c=cases[u['id']]; name=(u['place'] or '').strip().strip('"'); cc=u['cc']
    xy=None; how=1
    if name:
        base=re.sub(r'\([^)]*\)','',name).strip()
        cands=[base]+[x.strip() for x in re.split(r',| and | et | & |\+|-|/', base) if x.strip()]
        for cand in cands:
            cand=re.sub(r'^(City of|Greater|Borough of|Municipalities of|Provincia( de)?|Comunidad|Federal State of|region of)\s+','',cand,flags=re.I).strip(' .')
            if len(cand)<3: continue
            xy=q(cand,cc)
            if xy: break
    if not xy and cc in cty: xy=cty[cc][:2]; how=2
    if not xy: still.append(u); continue
    loc=c['location']; J=lambda l:"; ".join(str(v) for v in l)
    yi=cls(c,"implementation-year"); yd=cls(c,"decision-year")
    services=[]
    for s in c["services"]:
        sv=svcs.get(s["serviceId"])
        if sv: services.append(sv["name"]+(" ("+secs[sv["sectorId"]]["name"]+")" if sv.get("sectorId") in secs else ""))
    P['rows'].append([round(xy[0],5),round(xy[1],5),cc,(loc.get('altName') or '').strip(),yi[0] if yi else None,yd[0] if yd else None,J(cls(c,"deprivatisation-type")),J(services),J(cls(c,"previous-provider")),J(cls(c,"current-provider")),J(cls(c,"ownership")),J(cls(c,"actors")),J(cls(c,"actions")),J(cls(c,"governance")),J(cls(c,"organisation")),J(cls(c,"motivation")),how,c['id'],loc.get('population'),c.get('summary') or '',J(cls(c,"outcome"))])
json.dump(cache,open(CACHE,'w'))
P['unplaced']=still
P['rows'].sort(key=lambda r:r[17])
json.dump(P,open('/home/claude/work/pf_rows.json','w'))
import collections
print(len(P['rows']),'placed',collections.Counter(r[16] for r in P['rows']),'still unplaced',still)
