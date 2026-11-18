#!/usr/bin/env python3
"""Filter and score cached releases into readable candidates.

    python3 score.py cache/doj.jsonl out.jsonl [--min 2]

Drops: already-held/removed URLs, stings, releases with no payment+role pair.
The sting filter is not optional -- it kills about a third of the
prison-contraband family and those releases are indistinguishable by title.
"""
import json, sys, re, os

SRC = '/home/claude/repo/secret-society-src/data'

# Ruling 15 bars private commercial bribery with no public body and no official.
# The Anti-Kickback Statute / False Claims Act healthcare families are almost
# entirely that shape: a lab or pharmacy paying physicians, marketers or
# patients for referrals. Measured as about a fifth of the "Kickback" family.
RULING15 = re.compile(r'(?i)anti-?kickback statute|False Claims Act|'
 r'medically unnecessary|Medicare|Medicaid|TRICARE|beneficiar\w+|'
 r'physician referral|patient referrals?|pharmac\w+|laborator\w+|'
 r'durable medical equipment|telemedicine|genetic testing')
PUBLIC = re.compile(r'(?i)\b(public official|government official|city |county |state |federal official|'
 r'police|correctional|customs|border|inspector|examiner|councilman|councilwoman|'
 r'council member|mayor|commissioner|senator|judge|army|navy|air force|'
 r'contracting officer|school district|housing authorit\w+|municipal)\b')
STING = re.compile(r'(?i)undercover|posing as|fictitious|purported|represented to contain|'
                   r'sting operation|cooperating witness posing|FBI agent posing|'
                   r'what (?:he|she|they) believed to be|sham |fake (?:bribe|payment)')
PAY = re.compile(r'(?i)\bbrib\w+|kickback|payoff|paid (?:him|her|them|cash|a total|\$)|'
                 r'in (?:exchange|return) for (?:cash|money|payments?|\$)|'
                 r'accept(?:ed|ing) (?:cash|money|payments?|bribes?|things of value)|'
                 r'corrupt(?:ly)? (?:accept|receiv|demand|solicit)|honest services')
ROLE = re.compile(r'(?i)\b(correctional officer|corrections officer|detention officer|'
                  r'prison guard|jail(?:er| officer| sergeant)|police officer|detective|'
                  r'sergeant|lieutenant|deputy sheriff|sheriff|state trooper|'
                  r'border patrol agent|customs(?: and border protection)? officer|'
                  r'immigration (?:officer|services officer)|special agent|'
                  r'contracting officer|contracting official|building inspector|'
                  r'safety inspector|inspector|examiner|city council\w*|councilman|'
                  r'councilwoman|county commissioner|mayor|housing (?:official|authority)|'
                  r'army (?:officer|official|sergeant)|navy (?:officer|official)|'
                  r'air force|chief|administrator|supervisor|warden|officer)\b')
AMT = re.compile(r'\$[\d,]{3,}|\$[\d.]+ (?:million|billion)')
OUT = re.compile(r'(?i)pleaded guilty|plead guilty|was sentenced|sentenced to|convicted|'
                 r'found guilty|indicted|charged|was arrested|jury convicted')

def sent(t):
    return re.split(r'(?<=[.!?])\s+', t)

def main():
    cf, outf = sys.argv[1], sys.argv[2]
    held = json.load(open(os.path.join(SRC,'cases.json'), encoding='utf-8'))
    rm = json.load(open(os.path.join(SRC,'removed_records.json'), encoding='utf-8'))['cases']
    seen = set()
    for x in held + rm:
        u = str(x.get('url','')).strip().rstrip('/')
        if u: seen.add(u)
    # held person-name tokens, for a soft duplicate warning
    heldblob = ' '.join((x.get('n','')+' '+str(x.get('who','')))
                        for x in held+rm).lower()
    rows, stats = [], {'total':0,'held':0,'sting':0,'nopay':0,'kept':0}
    for line in open(cf, encoding='utf-8'):
        try: r = json.loads(line)
        except Exception: continue
        stats['total'] += 1
        u = r['url'].strip().rstrip('/')
        if u in seen: stats['held'] += 1; continue
        t = r['text']
        if STING.search(t): stats['sting'] += 1; continue
        if RULING15.search(t) and not PUBLIC.search(t):
            stats['ruling15'] = stats.get('ruling15', 0) + 1; continue
        hits = [s.strip() for s in sent(t) if PAY.search(s) and ROLE.search(s)]
        if not hits: stats['nopay'] += 1; continue
        amts = AMT.findall(t)
        outc = OUT.findall(t)
        # soft dup: any capitalised 2-word name in title present in held blob
        nm = re.findall(r"\b[A-Z][a-z']{2,}\s+[A-Z][a-z']{2,}\b", r['title'])
        dup = [n for n in nm if n.lower() in heldblob]
        rows.append({'url':r['url'],'title':r['title'],'date':r['date'],
                     'component':r['component'],'q':r['q'],
                     'hits':hits[:6],'amts':amts[:4],'outcome':sorted(set(o.lower() for o in outc))[:3],
                     'dupwarn':dup,'len':len(t.split())})
        stats['kept'] += 1
    rows.sort(key=lambda x: (-len(x['hits']), x['title']))
    with open(outf,'w',encoding='utf-8') as f:
        for r in rows: f.write(json.dumps(r,ensure_ascii=False)+"\n")
    print(stats)
main()
