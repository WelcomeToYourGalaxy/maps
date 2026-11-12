import json,os,glob,collections,sys
SRC="/home/claude/welcometoyourgalaxy/executive-map"
OUT="/home/claude/maps/contacts"
SZ=2
KIND={'townhall':'t','govoffice':'g','ministry':'m','police':'p',
      'firestation':'f','prison':'r','diplomatic':'d'}
def clean(v):
    if not isinstance(v,str): return ""
    v=v.strip()
    return "" if v in ("","-","?") else v
cells=collections.defaultdict(list)
counts=collections.Counter()
for k,code in KIND.items():
    f=os.path.join(SRC,"execmap_local_%s.json"%k)
    if not os.path.exists(f): print("missing",f); continue
    for r in json.load(open(f)):
        if len(r)<3: continue
        try: lat=float(r[0]); lon=float(r[1])
        except (TypeError,ValueError): continue
        if not(-90<=lat<=90 and -180<=lon<=180): continue
        name=clean(r[2])
        if not name: continue
        site  = clean(r[3]) if len(r)>3 else ""
        oper  = clean(r[4]) if len(r)>4 else ""
        addr  = clean(r[5]) if len(r)>5 else ""
        phone = clean(r[7]) if len(r)>7 else ""
        email = clean(r[8]) if len(r)>8 else ""
        rec=[round(lat,5),round(lon,5),name,code,site,phone,email,addr,oper]
        while len(rec)>4 and rec[-1]=="": rec.pop()
        cells[(int((lon+180)//SZ),int((lat+90)//SZ))].append(rec)
        counts[code]+=1
os.makedirs(OUT,exist_ok=True)
for old in glob.glob(os.path.join(OUT,"*.json")): os.remove(old)
idx=[]
for (x,y),rs in cells.items():
    p=os.path.join(OUT,"%d_%d.json"%(x,y))
    json.dump(rs,open(p,"w"),ensure_ascii=False,separators=(",",":"))
    idx.append("%d_%d"%(x,y))
json.dump({"size":SZ,"cells":sorted(idx),
  "kinds":{"t":"town hall","g":"government office","m":"ministry or department",
           "p":"police","f":"fire station","r":"prison","d":"diplomatic"},
  "fields":["lat","lon","name","kind","website","phone","email","address","operator"],
  "source":"OpenStreetMap via WelcomeToYourGalaxy/executive-map"},
  open(os.path.join(OUT,"index.json"),"w"),separators=(",",":"))
tot=sum(len(v) for v in cells.values())
print("records:",tot,dict(counts))
print("cells:",len(cells))
sz=sum(os.path.getsize(os.path.join(OUT,f)) for f in os.listdir(OUT))
print("total bytes: %.1f MB"%(sz/1e6))
big=sorted(((os.path.getsize(os.path.join(OUT,f)),f) for f in os.listdir(OUT)),reverse=True)[:3]
print("largest:",[(f,"%.0f KB"%(b/1000)) for b,f in big])
