#!/usr/bin/env python3
"""Mechanical checks on a batch of candidate records, before anyone reads them.

Across the four rounds of 15 November 2026 this flagged 16 problems in 183
candidates and nothing false, so it is cheaper than a reading pass and catches
a different class of fault. It makes no judgements: field presence, enum
values, country names, org keys, coordinate and year sanity, word counts, and
duplicates against both cases.json and removed_records.json.

Its one blind spot, found on 15 November: it compared titles only within a
country, so the same banker written up twice under two different countries
(Krull, as Switzerland and as Venezuela) went through. The person-name check
below closes that - capitalised multi-word names in a title are compared
across the whole map, not just inside one country.

    python3 validate_batch.py candidates.json
"""
import json, sys, os, re, collections

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, 'data')

REQ = ['n','c','city','lat','lng','y','bk','tgt','inf','who','rank','status',
       'lik','rel','int','wide','d','inside','cite','url']
ENUM = {
 'bk':  {'exec','cabinet','legis','court','security','finance','intl','company'},
 'tgt': {'gov','intl','company'},
 'inf': {'state','crime','corp','money','lodge','faith','elite','movement','lender'},
 'status': {'investigation','alleged','convicted','inquiry','acknowledged',
            'designated','settled','indicted','reported','annulled','acquitted'},
 'lik': {'established','probable','possible','contested'},
 'rel': {'now','legacy','past'},
}
STOP = set('the a an and or of in at on for to from with by its his her their '
           'who was were is are be been has had have not no over under into '
           'paid pay pays bought buy case cases two three four five'.split())

def words(s): return len(str(s).split())

def toks(title):
    return {w for w in re.findall(r"[a-z']+", title.lower()) if len(w) > 3 and w not in STOP}

def names(title):
    """Capitalised two-or-more-word runs: person names, mostly."""
    out = set()
    for m in re.finditer(r"\b([A-Z][\w'À-ɏ-]+(?:\s+(?:van|de|den|der|bin|al|el)\s+|\s+)"
                         r"[A-Z][\w'À-ɏ-]+)\b", title):
        s = m.group(1)
        if len(s.split()) <= 4:
            out.add(s.lower())
    return out

def figures(s):
    """The significant digits of each figure in a string.

    Compared as digit prefixes, not as text, because the same figure is written
    many ways across a record: a title saying Rp310bn against a description
    saying Rp310,118,271,000, or 680m dong against 680 million dong. Units are
    ignored for the same reason. Loose on purpose: this is a note to check, and
    under-flagging is better than crying wolf on every notation difference.
    """
    out = set()
    for m in re.finditer(r"\d[\d.,]*", str(s)):
        digits = m.group(0).replace(',', '').replace('.', '').lstrip('0')
        if len(digits) >= 2:
            out.add(digits[:3])
    return out


def main(path):
    cands = json.load(open(path, encoding='utf-8'))
    cases = json.load(open(os.path.join(D,'cases.json'), encoding='utf-8'))
    removed = json.load(open(os.path.join(D,'removed_records.json'), encoding='utf-8'))['cases']
    orgkeys = {o['k'] for o in json.load(open(os.path.join(D,'orgs.json'), encoding='utf-8'))['orgs']}
    countries = {l.strip() for l in open(os.path.join(HERE,'briefs','countries.txt'),
                                         encoding='utf-8') if l.strip()}

    by_country = collections.defaultdict(list)
    for src, pool in (('map',cases),('removed',removed)):
        for c in pool:
            by_country[c.get('c','')].append((src, c.get('n',''), toks(c.get('n','')),
                                              (c.get('city') or '').strip().lower()))
    name_index = collections.defaultdict(list)
    for src, pool in (('map',cases),('removed',removed)):
        for c in pool:
            for nm in names(c.get('n','')):
                name_index[nm].append((src, c.get('c',''), c.get('n','')))

    problems = []
    notes = []
    def bad(i, kind, msg): problems.append((i, kind, msg))

    seen_titles = {}
    for i, r in enumerate(cands):
        t = r.get('n','')
        for f in REQ:
            if f not in r or r[f] in (None,''):
                bad(i,'missing',f'field {f}')
        if r.get('bk') or r.get('tgt'):
            for f, allowed in ENUM.items():
                if f in r and r[f] not in allowed:
                    bad(i,'enum',f'{f}={r[f]!r}')
        if r.get('c') not in countries:
            bad(i,'country',f'{r.get("c")!r} not in countries.txt')
        org = r.get('org','')
        if org and org not in orgkeys:
            bad(i,'org',f'{org!r} not an existing org key')
        if org and r.get('org_label'):
            bad(i,'org',"both org and org_label set")
        if not org and not r.get('org_label'):
            bad(i,'org',"neither org nor org_label")
        try:
            lat,lng = float(r.get('lat')), float(r.get('lng'))
            if not (-90<=lat<=90 and -180<=lng<=180): bad(i,'coord','out of range')
            if abs(lat)<0.02 and abs(lng)<0.02: bad(i,'coord','null island')
        except Exception: bad(i,'coord','not numeric')
        try:
            y=int(r.get('y'))
            if not (1600<=y<=2026): bad(i,'year',f'{y}')
        except Exception: bad(i,'year','not an integer')
        for f in ('int','wide'):
            try:
                v=int(r.get(f))
                if not 1<=v<=5: bad(i,f,f'{f}={v}')
            except Exception: bad(i,f,f'{f} not 1-5')
        # BRIEF5 says 60-130 words. The looser 45-150 this used to allow is why 188
        # records on the map are over the cap; new ones are held to the brief.
        if not 60 <= words(r.get('d','')) <= 130:
            bad(i,'length',f'd is {words(r.get("d",""))} words, brief says 60-130')
        if not 10 <= words(r.get('inside','')) <= 40:
            bad(i,'length',f'inside is {words(r.get("inside",""))} words')
        if len(t) > 85: bad(i,'title',f'{len(t)} chars')
        # A figure that only the title or the inside line carries, with nothing in the
        # description to support it, is how a figure travels between two cases. The fifth
        # round had one: an AIC record claimed a 40 per cent mark-up in its title and its
        # inside line, and the figure belonged to a different AIC case.
        indesc = figures(r.get('d',''))
        loose = sorted(f for f in (figures(r.get('inside','')) | figures(t))
                       if not any(f.startswith(g) or g.startswith(f) for g in indesc))
        if loose:
            notes.append((i,'figure',f'in the title or inside line but not in d: {loose} '
                                     f'(a figure spelled out in d will show here too)'))
        if not str(r.get('url','')).startswith('http'): bad(i,'url','not a url')

        k = (r.get('c',''), t.lower())
        if k in seen_titles: bad(i,'dup-batch',f'same title as candidate {seen_titles[k]}')
        seen_titles[k] = i

        ct = toks(t)
        rcity = (r.get('city') or '').strip().lower()
        if ct:
            for src, on, ot, ocity in by_country.get(r.get('c',''), []):
                if not ot: continue
                ov = len(ct & ot) / max(1, min(len(ct), len(ot)))
                if ov < 0.6:
                    continue
                # A case sits in the city of the body it reached, so a different city is a
                # different body and not a duplicate. Both title-overlap flags of the fifth
                # round were this: one company's near-identical records across provinces
                # (Viet A across Vietnam's provincial disease centres, the CBI's mule-account
                # cases across Indian branches). Still reported, as a note to check rather
                # than a problem to fix.
                kind = 'dup' if (rcity and ocity and rcity == ocity) or not (rcity and ocity) else 'note'
                if kind == 'dup':
                    bad(i,f'dup-{src}',f'{int(ov*100)}% title overlap with: {on[:70]}')
                else:
                    notes.append((i,f'near-{src}',
                                  f'{int(ov*100)}% title overlap but a different city '
                                  f'({rcity} vs {ocity}): {on[:52]}'))
        # A person named in two countries' records is worth a hard look: it is how the
        # same banker was written up twice, as Switzerland and as Venezuela. But it is
        # also legitimate - Trinh Xuan Thanh appears in Vietnam for a villa bought by a
        # contractor and in Slovakia for the plane used in his abduction, two events. So
        # this is a note to check, not a problem to fix.
        for nm in names(t):
            for src, oc, on in name_index.get(nm,[]):
                if oc != r.get('c'):
                    notes.append((i,'name-'+src,
                                  f'"{nm}" is also on the map under {oc}: {on[:56]}'))

    print(f'{len(cands)} candidates, {len(problems)} problems, {len(notes)} to check')
    for i, kind, msg in problems:
        print(f'  [{i}] {kind:11s} {msg}')
        print(f'       {cands[i].get("c","?")} / {cands[i].get("n","?")[:70]}')
    for i, kind, msg in notes:
        print(f'  [{i}] {kind:11s} {msg}')
        print(f'       {cands[i].get("c","?")} / {cands[i].get("n","?")[:70]}')
    return 1 if problems else 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
