#!/usr/bin/env python3
"""Pull COURT-cell and LEGIS-cell candidates out of the clustered DOJ corpus.

    python3 score_cl.py groups2.json cl_cand.jsonl

Ruling 17 puts a court, tribunal, prosecution office or judicial officer in
`court`, and an elected assembly in `legis`. In the DOJ corpus those read as
judges, magistrates, court clerks, probation and pretrial officers, district
attorneys, and on the other side council members, state representatives,
senators, aldermen, supervisors and commissioners who sit on an elected body.
Requires the body word and a payment word in the same release.
"""
import json,sys,re
# 'pretrial', 'courthouse' and 'prosecutor' appear in DOJ boilerplate on every
# release, so they flag corrections and police cases as court cases. The post
# words below only appear when a judicial officer is actually a party.
COURT=re.compile(r'(?i)\b(a |the |former |sitting |state |county |circuit |district |municipal |superior |immigration )(judge|magistrate|justice of the peace|court clerk|clerk of court|court administrator)\b|(?<!District )(?<!Honorable )(?<!before )\b(magistrate|court clerk|clerk of court|probation officer|court administrator|justice of the peace)\s+[A-Z][a-z]+|\bbrib\w+ (a|the) (federal |state |sitting |former )?(judge|magistrate)\b|\bjudge (accepted|solicited|took|received)\b|\bjudicial (bribery|corruption)\b')
LEGIS=re.compile(r'(?i)\b(state senator|state representative|state rep\.|city council|council ?member|councilman|councilwoman|alderman|alderwoman|board of supervisors|county commissioner|borough council|town council|legislator|house of representatives|general assembly|state house|state legislature)\b')
PAY=re.compile(r'(?i)\b(bribe|bribery|kickback|cash payment|in exchange for|in return for|gratuit|extort|pay(?:ments?|off|offs)?\s+(?:to|from|of)|accepted\b.{0,24}\b(?:cash|money|payments?)|honest services)\b')
def main():
    gf,outf=sys.argv[1],sys.argv[2]
    G=json.load(open(gf))
    cand=[json.loads(l) for l in open('cand2.jsonl',encoding='utf-8')]
    groups=[[cand[i] for i in grp] for grp in G['groups'].values()]
    done=set(json.load(open('done_urls.json')))
    R='/home/claude/repo/secret-society-src/'
    for f in ('data/cases.json','data/removed_records.json','data/candidates.json'):
        try:
            D=json.load(open(R+f))
            rows=D if isinstance(D,list) else (D.get('cases') or D.get('candidates') or [])
            for r in rows:
                u=r.get('url') or r.get('locator') or ''
                if u: done.add(u.rstrip('/').rsplit('/',1)[-1])
        except Exception as e: print('warn',f,e)
    skip=set()
    for f in ('skips.json',):
        try: skip={k for k in json.load(open(f))}
        except Exception: pass
    st={'total':0,'done':0,'nopay':0,'nobody':0,'court':0,'legis':0}
    out=open(outf,'w')
    for g in groups:
        st['total']+=1
        urls=[r.get('url','') for r in g]
        slugs=[u.rstrip('/').rsplit('/',1)[-1] for u in urls]
        if any(s0 in done or any(s0.startswith(d0) for d0 in done if len(d0)>24) for s0 in slugs):
            st['done']+=1; continue
        txt=' '.join((r.get('title','')+' '+' '.join(r.get('hits',[])))[:9000] for r in g)
        if not PAY.search(txt): st['nopay']+=1; continue
        c=bool(COURT.search(txt)); l=bool(LEGIS.search(txt))
        if not (c or l): st['nobody']+=1; continue
        cell='legis' if l else 'court'
        st[cell]+=1
        out.write(json.dumps({'cell':cell,'urls':urls,
            'titles':[r.get('title','') for r in g],
            'text':txt[:14000]},ensure_ascii=False)+'\n')
    out.close(); print(st)
main()
