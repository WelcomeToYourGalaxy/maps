#!/usr/bin/env python3
"""Pull candidate records out of the COURT JUDGMENTS in the Romanian corpus.

    python3 score_judg.py cache/dna_ro.jsonl dna_judg.jsonl

About a third of the dna.ro archive by id is full court judgments published as
case law rather than press releases (measured: ~1,400 of 6,031 crawled). They
are worth a seam of their own for one reason the releases cannot match: they
carry the OUTCOME. A release almost always stops at "sent for trial", so the
map's `status` for a Romanian record is usually `indicted`; a judgment says
what the court decided and what sentence it passed.

Two costs. They average about 11,000 words, so the reader below extracts only
the sentencing lines and the facts passage. And they are anonymised to
initials, so ruling 11's named-individual is absent - but ruling 11 requires a
named BODY and a named DECISION, not a named person, and the bodies in these
texts are named in full.

Requires: a judgment marker, a corruption offence, a disposition verb that
decides guilt, and a body word. Appeal judgments that only rule on procedure
are dropped by the disposition test.
"""
import json,sys,re
JUDG=re.compile(r'(?i)(Dezbaterile au avut loc|încheierea de ședință|împotriva sentinței penale|TRIBUNALUL, Delib)')
OFF=re.compile(r'(?i)\b(luare de mit[ăa]|dare de mit[ăa]|trafic de influen[țt]|cump[ăa]rare de influen[țt]|abuz în serviciu|delapidare|[șs]antaj)')
# a disposition that decides guilt, not one that merely disposes of procedure
DISP=re.compile(r'(?i)(condamn[ăa]\s+(?:pe\s+)?inculpat|l-a condamnat|a condamnat (?:pe\s+)?inculpat|la pedeapsa de\s+\d|aplic[ăa]\s+inculpat\w*\s+pedeapsa|stabile[șs]te\s+pedeapsa)')
BODY=re.compile(r'(?i)\b(spital|primari|prim[ăa]ri[ae]|consiliul (?:jude[țt]ean|local)|ministerul|penitenciar|poli[țt]i[ae]|universit|inspectorat|direc[țt]ia|regia|compania na[țt]ional|administra[țt]ia na[țt]ional|agen[țt]ia na[țt]ional|tribunal|judec[ăa]tori[ae]|parchet|casa de asigur|serviciul public|aeroport|vam[ăa]|garda (?:de mediu|na[țt]ional))')
FACTS=re.compile(r'(?i)(stare de fapt|starea de fapt|situa[țt]ia de fapt)')
def main():
    cf,outf=sys.argv[1],sys.argv[2]
    held=set()
    R='/home/claude/repo/secret-society-src/'
    for f in ('data/cases.json','data/removed_records.json','data/candidates.json'):
        D=json.load(open(R+f))
        rows=D if isinstance(D,list) else (D.get('cases') or D.get('candidates') or [])
        for r in rows:
            m=re.search(r'id=(\d+)',r.get('url') or r.get('locator') or '')
            if m: held.add(int(m.group(1)))
    st={'total':0,'notjudg':0,'held':0,'nooff':0,'nodisp':0,'nobody':0,'nofacts':0,'kept':0}
    out=open(outf,'w')
    for l in open(cf,encoding='utf-8'):
        r=json.loads(l); st['total']+=1
        t=r.get('text') or ''
        if not JUDG.search(t[:3000]): st['notjudg']+=1; continue
        if r.get('id') in held: st['held']+=1; continue
        if not OFF.search(t): st['nooff']+=1; continue
        if not DISP.search(t): st['nodisp']+=1; continue
        if not BODY.search(t): st['nobody']+=1; continue
        if not FACTS.search(t): st['nofacts']+=1; continue
        st['kept']+=1
        out.write(json.dumps({'id':r['id'],'date':r.get('date'),
                              'words':len(t.split()),'text':t},ensure_ascii=False)+'\n')
    out.close(); print(st)
main()
