#!/usr/bin/env python3
"""Pull COURT-cell candidates out of the Romanian corpus.

    python3 score_court.py cache/dna_ro.jsonl dna_court.jsonl

Ruling 17 puts a court, tribunal, prosecution office or judicial officer in
`court`. In DNA releases the post words below name the officer; the sentencing
court appears instead as "Tribunalul ... cu propunere", "Curtea de Apel ... a
dispus" and similar, which do not use these post words, so the filter does not
pick up the court that is merely hearing the case.
"""
import json,sys,re
POST=re.compile(r'(?i)\b(judec[ăa]tor(?:ul|ului|i|ilor)?|procuror(?:ul|ului|i|ilor)?|grefier\w*|executor judec[ăa]toresc|magistrat\w*|pre[șs]edinte al (?:Judec[ăa]toriei|Tribunalului|Cur[țt]ii)|consilier de probatiune|consilier de proba[țt]iune)\b')
# The post must be a DEFENDANT'S, not the judge hearing the case. Measured on
# this corpus: a loose "inculpat ... judecator" window matched 411 documents,
# almost all of them court judgments whose procedural boilerplate names the
# deciding court. A third of the dna.ro archive by id is court judgments, not
# press releases (measured: ~1,400 of 6,031, averaging 11,000 words), and only
# the releases put the defendant's name in CAPITALS followed by the post. So
# anchor on that format instead.
DEF=re.compile(r'\b([A-ZĂÂÎȘȚ][A-ZĂÂÎȘȚ\-]+\s+){1,4}[,]?\s*(?:la data faptelor\s+|fost\s+|în prezent\s+)*'
               r'(judec[ăa]tor|procuror|grefier|executor judec[ăa]toresc|magistrat|pre[șs]edinte al (?:Judec[ăa]toriei|Tribunalului))')
JUDGMENT=re.compile(r'(?i)(Dezbaterile au avut loc|încheierea de ședință|împotriva sentinței penale)')
BRIBE=re.compile(r'(?i)\b(mit[ăa]|luare de mit|dare de mit|trafic de influen|cumparare de influen|cump[ăa]rare de influen)')
FACTS=re.compile(r'(?i)(stare de fapt|starea de fapt)')
SKIPDOC=re.compile(r'(?i)(bilan[țt]|raport de activitate|comunicat de pres[ăa] privind activitatea)')
def main():
    cf,outf=sys.argv[1],sys.argv[2]
    held=set()
    R='/home/claude/repo/secret-society-src/'
    for f in ('data/cases.json','data/removed_records.json','data/candidates.json'):
        D=json.load(open(R+f))
        rows=D if isinstance(D,list) else (D.get('cases') or D.get('candidates') or [])
        for r in rows:
            u=r.get('url') or r.get('locator') or ''
            m=re.search(r'id=(\d+)',u)
            if m: held.add(int(m.group(1)))
    st={'total':0,'held':0,'skipdoc':0,'nobribe':0,'notice':0,'nodef':0,'kept':0}
    out=open(outf,'w')
    for l in open(cf,encoding='utf-8'):
        r=json.loads(l); st['total']+=1
        t=r.get('text') or ''
        if r.get('id') in held: st['held']+=1; continue
        if SKIPDOC.search(t[:400]) or JUDGMENT.search(t[:3000]):
            st['skipdoc']+=1; continue
        if not BRIBE.search(t): st['nobribe']+=1; continue
        if not FACTS.search(t): st['notice']+=1; continue
        if not DEF.search(t): st['nodef']+=1; continue
        st['kept']+=1
        out.write(json.dumps({'id':r['id'],'date':r.get('date'),'words':len(t.split()),
                              'text':t},ensure_ascii=False)+'\n')
    out.close(); print(st)
main()
