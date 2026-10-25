import json
t=open('/home/claude/work/template.html').read()
consts=open('/home/claude/work/part_consts.js').read()
bases=open('/home/claude/work/part_bases.js').read()
import gzip,base64
import math
def _c(x):
    if isinstance(x,float) and not math.isfinite(x): return None
    if isinstance(x,dict): return {k:_c(v) for k,v in x.items()}
    if isinstance(x,list): return [_c(v) for v in x]
    return x
DD=_c(json.load(open('/home/claude/work/data.json')))
MMF='loan-conditions-protests.json.gz'
mm=DD.pop('mm')
open('/home/claude/work/'+MMF,'wb').write(gzip.compress(json.dumps(mm,separators=(',',':'),allow_nan=False).encode(),9))
DD['mm_meta']={'n':len(mm['rows']),'file':MMF}
raw=json.dumps(DD,separators=(',',':'),allow_nan=False).encode()
data=base64.b64encode(gzip.compress(raw,9)).decode()
for k,v in [('/*__BASEMAP_CONST__*/',consts),('/*__BASES__*/',bases),('"/*__DATA__*/"','"'+data+'"')]:
    assert t.count(k)==1,k; t=t.replace(k,v)
open('/home/claude/work/loan-conditions.html','w').write(t)
print(len(t))
