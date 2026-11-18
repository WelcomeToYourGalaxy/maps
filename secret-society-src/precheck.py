#!/usr/bin/env python3
"""Score each INCOMING candidate against every HELD record, before merging.

    python3 precheck.py /path/to/out_A.json [more...]

WHY. Agents check duplicates inside their own cell. A candidate that duplicates
a record coded into a different cell is invisible to that check, and rounds 12
and 13 each lost finished records to it after the merge rather than before.
This runs the dupsweep2 signals across the cell boundary, candidate vs held.
Prints every pair at or above the threshold and NAMES the held record, because a
bare verdict has been wrong often enough to cost real records.
"""
import json, os, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from flagleads import toks, figs, bodies, locs

RARE_FIG, RARE_BODY = 2, 3

def feats(c):
    blob = c.get('n','') + ' ' + (c.get('d') or '') + ' ' + str(c.get('undone') or '')
    return (toks(c.get('n','')), figs(blob),
            bodies(str(c.get('rank',''))) | bodies(c.get('n','')) | bodies((c.get('d') or '')[:400]),
            locs(str(c.get('url','')) + ' ' + str(c.get('cite',''))))

def main(paths, thresh=0.9):
    cs = json.load(open(os.path.join(HERE,'data','cases.json'), encoding='utf-8'))
    rm = json.load(open(os.path.join(HERE,'data','removed_records.json'), encoding='utf-8'))['cases']
    for c in rm: c['n'] = '[REMOVED: %s] %s' % (str(c.get('drop_reason',''))[:70], c.get('n',''))
    H = [(i,c)+feats(c) for i,c in enumerate(cs + rm)]
    dff, dfb = collections.Counter(), collections.Counter()
    for _,_,_,f,b,_ in H:
        for x in f: dff[x]+=1
        for x in b: dfb[x]+=1
    cand=[]
    for p in paths:
        d=json.load(open(p,encoding='utf-8'))
        r=d if isinstance(d,list) else d.get('cases',d.get('records'))
        for j,c in enumerate(r): cand.append((os.path.basename(p),j,c)+feats(c))
    hits=0
    for src,j,c,t,f,b,l in cand:
        best=[]
        for i,hc,ht,hf,hb,hl in H:
            s=0.0; why=[]
            ov=t&ht
            if t and ht:
                jac=len(ov)/len(t|ht)
                if jac>=0.3: s+=jac; why.append('title %.2f %s'%(jac,sorted(ov)[:4]))
            for x in f&hf:
                if dff[x]<=RARE_FIG: s+=0.9; why.append('fig %s (in %d)'%(x,dff[x]))
            for x in b&hb:
                if dfb[x]<=RARE_BODY: s+=0.8; why.append('body %s (in %d)'%(x,dfb[x]))
            for x in l&hl: s+=1.2; why.append('locator %s'%(x,))
            if c.get('y')==hc.get('y') and c.get('cn')==hc.get('cn') and s>0: s+=0.25; why.append('same year+country')
            if s>=thresh: best.append((s,i,hc,why))
        if best:
            best.sort(reverse=True); hits+=1
            s,i,hc,why=best[0]
            print('\n%s[%d] %.2f  %s' % (src,j,s,c.get('n','')[:95]))
            print('   HELD idx %d  %s' % (i, hc.get('n','')[:95]))
            print('   %s' % '; '.join(why[:5]))
            for s2,i2,hc2,w2 in best[1:3]:
                print('   also idx %d %.2f  %s' % (i2,s2,hc2.get('n','')[:80]))
    print('\n%d candidates, %d flagged at >= %.2f' % (len(cand),hits,thresh))

if __name__ == '__main__':
    main([a for a in sys.argv[1:] if not a.startswith('-')])
