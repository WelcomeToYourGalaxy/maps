#!/usr/bin/env python3
"""Filter the Romanian DNA corpus to candidate infiltration records.

    python3 score_dna.py cache/dna_ro.jsonl out.jsonl

DNA releases put the defendant's name in CAPITALS followed by the post held,
which makes the named-body test of ruling 11 mechanical: a release that names
no post names no body. Requires a bribery offence, a post inside a named body,
and a capitalised defendant. Drops releases already cited by a held record.
"""
import json,sys,re,os

SRC=os.path.join(os.path.dirname(os.path.abspath(__file__)),'data')

PAY=re.compile(r'(?i)luare de mit|dare de mit|trafic de influen|cump[ăa]rare de influen|'
 r'[îi]nc[ăa]lcarea.{0,40}mit|folosirea.{0,30}func[țt]i|abuz [îi]n serviciu|'
 r'[șs]pag|remitere.{0,20}bani|sum[ăa] de bani|mit[ăa]')
POST=re.compile(r'(?i)\b(primar|viceprimar|consilier local|consilier jude[țt]ean|'
 r'pre[șs]edinte al consiliului jude[țt]ean|prefect|subprefect|ministru|'
 r'secretar de stat|deputat|senator|director(?: general| executiv| adjunct)?|'
 r'manager(?:ul)? (?:al )?spitalului|[șs]ef(?: de)? serviciu|[șs]ef birou|'
 r'inspector(?: [șs]ef| principal)?|comisar|poli[țt]ist|agent de poli[țt]ie|'
 r'ofi[țt]er|procuror|judec[ăa]tor|vame[șs]|lucr[ăa]tor vamal|'
 r'medic|asistent medical|rector|decan|inspector [șs]colar|'
 r'administrator public|secretar(?:ul)? (?:al )?(?:unit[ăa][țt]ii|prim[ăa]riei)|'
 r'func[țt]ionar public|expert|arhitect [șs]ef|comandant)\b')
BODY=re.compile(r'(?i)\b(prim[ăa]ria|consiliul (?:local|jude[țt]ean)|spitalul|'
 r'inspectoratul|direc[țt]ia|agen[țt]ia|autoritatea|ministerul|'
 r'poli[țt]ia|inspectoratul de poli[țt]ie|garda (?:de mediu|financiar)|'
 r'vama|birou(?:l)? vamal|administra[țt]ia|institutul|universitatea|'
 r'compania na[țt]ional|regia (?:autonom|na[țt]ional)|societatea na[țt]ional|'
 r'casa (?:de asigur|na[țt]ional)|tribunalul|judec[ăa]toria|parchetul|'
 r'serviciul (?:public|de)|oficiul|comisariatul)\b')
NAME=re.compile(r'\b[A-ZĂÂÎȘȚ]{3,}(?:[\s\-][A-ZĂÂÎȘȚ]{2,}){1,3}\b')
# A release must CHARGE a bribery or influence offence: abuse of office alone
# names no payer and fails BRIEF11 limb 1. Measured: 259 of 389.
BRIBE=re.compile(r'(?i)luare de mit|dare de mit|trafic de influen|cump[ăa]rare de influen|mituire')
# A release with no facts section is a sentencing notice whose facts were
# published earlier: an UPDATE to a held record, not a new record. 130 of 259.
FACTS=re.compile(r'(?i)(stare de fapt|starea de fapt)')
SKIPDOC=re.compile(r'(?i)bilan[țt]ul de activitate|raport(?:ul)? (?:anual|de activitate)|'
 r'situa[țt]ia statistic|comunicat de pres[ăa] privind participarea')

def main():
    cf,outf=sys.argv[1],sys.argv[2]
    held=json.load(open(os.path.join(SRC,'cases.json'),encoding='utf-8'))
    rm=json.load(open(os.path.join(SRC,'removed_records.json'),encoding='utf-8'))['cases']
    usedids=set()
    for x in held+rm:
        for m in re.finditer(r'dna\.ro/comunicat\.xhtml\?id=(\d+)',str(x.get('url',''))):
            usedids.add(int(m.group(1)))
    st={'total':0,'held':0,'skipdoc':0,'toolong':0,'nopay':0,'nobody':0,
        'nobribe':0,'notice':0,'kept':0}
    out=[]
    for line in open(cf,encoding='utf-8'):
        r=json.loads(line); st['total']+=1
        if r['id'] in usedids: st['held']+=1; continue
        t=r['text']
        if SKIPDOC.search(t[:600]): st['skipdoc']+=1; continue
        if r['words']>2500: st['toolong']+=1; continue
        if not PAY.search(t): st['nopay']+=1; continue
        if not (POST.search(t) and BODY.search(t)): st['nobody']+=1; continue
        if not BRIBE.search(t[:2600]): st['nobribe']=st.get('nobribe',0)+1; continue
        if not FACTS.search(t): st['notice']=st.get('notice',0)+1; continue
        names=sorted(set(NAME.findall(t[:2200])))[:6]
        out.append({'id':r['id'],'url':r['url'],'date':r['date'],'year':r['year'],
                    'words':r['words'],'names':names,'text':t})
        st['kept']+=1
    out.sort(key=lambda r:-r['year'])
    with open(outf,'w',encoding='utf-8') as f:
        for r in out: f.write(json.dumps(r,ensure_ascii=False)+'\n')
    print(st)
main()
