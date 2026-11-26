# -*- coding: utf-8 -*-
import json, re, pickle, collections, math
NE0='/home/claude/data/ne110.geojson'; NE1='/home/claude/ne/adm1.geojson'
def ring_area_centroid(ring):
    a=cx=cy=0.0
    for i in range(len(ring)-1):
        x0,y0=ring[i][0],ring[i][1]; x1,y1=ring[i+1][0],ring[i+1][1]
        f=x0*y1-x1*y0; a+=f; cx+=(x0+x1)*f; cy+=(y0+y1)*f
    if abs(a)<1e-12:
        xs=[p[0] for p in ring]; ys=[p[1] for p in ring]
        return (sum(xs)/len(xs), sum(ys)/len(ys), 0.0)
    a*=0.5
    return (cx/(6*a), cy/(6*a), abs(a))
def biggest_centroid(geom):
    polys=[geom['coordinates']] if geom['type']=='Polygon' else geom['coordinates']
    best=None
    for poly in polys:
        x,y,ar=ring_area_centroid(poly[0])
        if best is None or ar>best[2]: best=(x,y,ar)
    return best
# ---- countries, by the largest landmass so distant territories do not drag the point
CC={}
for f in json.load(open(NE0))['features']:
    p=f['properties']
    iso=(p.get('ISO_A2') or '').strip()
    if not iso or iso=='-99' or len(iso)!=2: iso=(p.get('ISO_A2_EH') or '').strip()
    iso=iso.lower()
    if not iso or iso=='-99' or len(iso)!=2: continue
    x,y,_=biggest_centroid(f['geometry']); CC[iso]=(round(y,5),round(x,5))
# ---- subdivisions
A2_OF_A3={'USA':'us','BRA':'br','RUS':'ru','CAN':'ca','IND':'in','IDN':'id','CHN':'cn','AUS':'au','ZAF':'za'}
SUB={}; SUBNAME={}
for f in json.load(open(NE1))['features']:
    p=f['properties']; cc=A2_OF_A3.get(p.get('adm0_a3'))
    if not cc: continue
    x,y,_=biggest_centroid(f['geometry']); pt=(round(y,5),round(x,5))
    code=(p.get('postal') or '').strip().upper()
    nm=(p.get('name') or '').strip().lower()
    if code: SUB[(cc,code)]=pt
    if nm: SUBNAME[(cc,nm)]=pt
print('countries %d  subdivisions %d (%d by name)'%(len(CC),len(SUB),len(SUBNAME)))
print('US country point ->',CC.get('us'),' BR ->',CC.get('br'))
print('US-KY ->',SUB.get(('us','KY')),' BR-MA ->',SUB.get(('br','MA')))
json.dump({'cc':{k:list(v) for k,v in CC.items()},
           'sub':{k[0]+'|'+k[1]:list(v) for k,v in SUB.items()},
           'subname':{k[0]+'|'+k[1]:list(v) for k,v in SUBNAME.items()}},
          open('/home/claude/data/centroids.json','w'))
print('saved')
