import json,math,io,urllib.request,ssl
from shapely.geometry import shape,mapping,box,Polygon,MultiPolygon,LineString
from shapely.ops import unary_union
from shapely import make_valid,set_precision
def rd(p):return json.load(open(p))
hs=unary_union([make_valid(shape(f['geometry'])) for f in rd('high_seas.geojson')['features']])
print('hs',hs.is_valid,hs.area)
land=unary_union([make_valid(shape(f['geometry'])) for f in rd('ne_50m_land.geojson')['features']])
hs_s=make_valid(hs.simplify(.18)).buffer(0)
world=box(-180,-85.05,180,85.05)
eez=make_valid(world.difference(hs_s).difference(land.buffer(0)))
south=box(-180,-85.05,180,-60)
eez=eez.difference(south)        # Antarctic Treaty area drawn on its own
hs_noS=hs_s.difference(south)
arc=hs_noS.intersection(box(-180,60,180,90))
open_=hs_noS.difference(box(-180,60,180,90))
south_sea=hs_s.intersection(south)
def clean(g,tol=.08):
    g=make_valid(g.simplify(tol)).buffer(0)
    polys=[p for p in (g.geoms if hasattr(g,'geoms') else [g]) if p.area>0.02]
    return MultiPolygon(polys)
def rr(o):
    if isinstance(o,(list,tuple)):return [rr(x) for x in o]
    return round(o,2)
fc=[]
def add(zid,g,**k):
    m=mapping(g);fc.append({"type":"Feature","properties":dict(zone=zid,**k),"geometry":{"type":m['type'],"coordinates":rr(m['coordinates'])}})
add('high-seas',clean(open_))
add('central-arctic',clean(arc))
add('eez-shelf',clean(eez,.12))
# Antarctic sectors (treaty claims; longitudes per the claimants' declarations)
def wedge(a,b,lat0=-60,lat1=-85.05):
    pts=[(x,lat0) for x in [a+(b-a)*i/40 for i in range(41)]]+[(x,lat1) for x in [b-(b-a)*i/40 for i in range(41)]]
    return Polygon(pts)
SEC=[('Norway (Queen Maud Land)',-20,44.633),('Australia (western part)',44.633,136.183),('France (Adélie Land)',136.183,142.033),('Australia (eastern part)',142.033,160),('New Zealand (Ross Dependency)',160,180),('New Zealand (Ross Dependency)',-180,-150)]
for n,a,b in SEC: add('antarctica-claimed',wedge(a,b),label=n)
add('antarctica-claimed',wedge(-80,-20),label='Overlapping claims: UK, Argentina, Chile (UK 20–80°W, Argentina 25–74°W, Chile 53–90°W)')
add('antarctica-claimed',wedge(-90,-80),label='Chile')
add('antarctica-unclaimed',wedge(-150,-90),label='Marie Byrd Land: the only unclaimed sector')
cc=rd('ccz.geojson')['features']
ccz=unary_union([make_valid(shape(f['geometry'])) for f in cc]).simplify(.1)
add('deep-seabed-area',ccz,label='Clarion-Clipperton Zone (ISA management area)')
print(len(fc),{f['properties']['zone'] for f in fc})
json.dump({"type":"FeatureCollection","features":fc},open('../data/zones.geojson','w'),separators=(',',':'))
d=rd('nedisp.geojson')
for f in d['features']:
    n=f['properties'].get('NAME') or ''
    if n=='Bir Tawil': add('terra-nullius-land',shape(f['geometry']),label='Bir Tawil')
    if n in('Spratly Is.','Paracel Is.','Scarborough Reef'):
        add('disputed-islands',shape(f['geometry']).buffer(.12),label=n)
s=rd('siga.json')[0]['geojson']
from shapely.geometry import shape as _s
add('terra-nullius-land',_s(s).buffer(.01),label='Gornja Siga (Liberland)')
fc.append({"type":"Feature","properties":{"zone":"geo","label":"Geostationary belt: 35,786 km straight above this line"},"geometry":{"type":"LineString","coordinates":[[x,0] for x in range(-180,181,4)]}})
json.dump({"type":"FeatureCollection","features":fc},open('../data/zones.geojson','w'),separators=(',',':'))
print(len(fc))
