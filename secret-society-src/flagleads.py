#!/usr/bin/env python3
"""Flag the banked leads against the records the map already holds and has removed.

Run after every merge:  python3 flagleads.py

WHY THIS EXISTS, AND WHY IT IS BUILT THIS WAY. Leads are filed by agents whose
own cells were barred, so they are filed by precisely the agents with no reason
to read the cell they land in. The bank therefore accumulates leads that
duplicate records the map already holds. Measured at 41 per cent contamination
across the bank, and higher in some cells.

Three attempts taught the design:

  1. A flag that states a verdict will be wrong often enough to cost records.
     Two agents lost the most valuable leads in their files to flags that fired
     on a round figure. So every lead now NAMES THE CLOSEST HELD RECORD with a
     score and the reason, and the agent reads that record rather than trusting
     a label.

  2. Every signal has to be weighted by how rare it is on the map. The figure
     10,000 appears in 77 held records and means nothing; a figure in one or two
     records is strong. The body "ministry of defence" appears in 17 and means
     nothing; "ASP Trapani" identifies one case.

  3. Titles alone miss the commonest duplicate. An agent measured 0 of 25
     records from this bank because lead titles paraphrase held titles with no
     shared figure: "a none flag on an Italian health lead means nothing; the
     body name is the tell". Hence the third signal.

NOTHING IS EVER REMOVED FROM THE BANK. A flag an agent disproves is a real lead.
"""
import json, re, os, sys, collections, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
D = lambda n: os.path.join(HERE, 'data', n)
RARE_FIG, RARE_BODY = 2, 3

BW = (r'(?:ASL|ASP|AOU|Policlinico|Azienda|Ospedal\w*|Hospital|Comune|Municipality|Council'
      r'|Ministry|Ministero|Directorate|Inspectorate|Guard|Customs|Politia|Police|Prefect\w*'
      r'|Authority|Agency|Agentia|Compania|Posta|Romsilva|Port|Terminal|Penitenciar\w*'
      r'|Universit\w*|Tribunal\w*|Procura|Commission|Comisia|Institut\w*|Bureau|Oficiu'
      r'|Departament\w*|Serviciu|Spital\w*|Casa)')
SINGLE = [(r'comunicat\.xhtml\?id=(\d+)', 'dna release'), (r'case_profile/(\d+)', 'OSP case'),
          (r'/node/(\d{4,})', 'node id')]
STOP = {'the','and','for','with','from','that','this','over','into','its','his','her','their',
        'paid','took','bribe','bribes','charged','convicted','accused','officials','official',
        'police','court','state','company','firm','firms','money','cash','said','says'}


def _n(s):
    s = unicodedata.normalize('NFKD', str(s or '')).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9 ]', ' ', s)


def toks(s):
    return {w for w in _n(s).split() if len(w) > 3 and w not in STOP}


def figs(s):
    out = set()
    for m in re.findall(r'\d[\d.,]*', str(s or '')):
        g = m.strip('.,').replace(',', '').replace('.', '')
        if g.isdigit() and len(g) >= 5 and not (1900 <= int(g) <= 2100 and len(g) == 4):
            out.add(g)
    return out


def bodies(s):
    out = set()
    for m in re.finditer(BW + r"(?:\s+(?:di|de|of|for|and|del|della|din|du|da|the))?(?:\s+[A-ZÀ-Ý][\w'-]+){0,3}",
                         str(s or '')):
        t = ' '.join(w for w in _n(m.group(0)).split() if len(w) > 2)
        if len(t.split()) >= 2:
            out.add(t)
    return out


def rare_tokens(df, s, cap=3):
    """Words that appear in very few records. The generalisation of the figure and
    body rules: rarity is the signal, whatever kind of token it is. A pair of
    records sharing "overflight" is a likelier duplicate than one sharing "police".
    """
    return {w for w in toks(s) if 0 < df.get(w, 0) <= cap}


def locs(s):
    out = set()
    for p, lab in SINGLE:
        for m in re.findall(p, str(s or '')):
            out.add((lab, m))
    return out


def main():
    cases = json.load(open(D('cases.json'), encoding='utf-8'))
    rm = json.load(open(D('removed_records.json'), encoding='utf-8'))['cases']
    bankf = D('candidates_flagged.json')
    src = bankf if os.path.exists(bankf) else D('candidates.json')
    bank = json.load(open(src, encoding='utf-8'))['candidates']
    bank = [b for b in bank if b.get('status') == 'apparently_qualifying' or 'DUP_FLAG' in b]

    dff, dfb = collections.Counter(), collections.Counter()
    H = []
    for i, c in enumerate(cases):
        blob = c.get('n', '') + ' ' + (c.get('d') or '') + ' ' + str(c.get('undone') or '')
        f = figs(blob)
        b = bodies(str(c.get('rank', ''))) | bodies(c.get('n', '')) | bodies((c.get('d') or '')[:400])
        H.append((i, c['n'], toks(c.get('n', '')), f, b,
                  locs(str(c.get('url', '')) + ' ' + str(c.get('cite', ''))), c.get('c')))
        for x in f: dff[x] += 1
        for x in b: dfb[x] += 1

    R = []
    for c in rm:
        blob = c.get('n', '') + ' ' + str(c.get('d') or '')
        R.append((c.get('n', ''), c.get('drop_reason') or c.get('why') or '(no reason recorded)',
                  figs(blob), toks(c.get('n', '')), bodies(blob), c.get('c')))

    out = collections.Counter()
    seen = {}
    for lead in bank:
        t = lead.get('title') or lead.get('n') or ''
        ex = str(lead.get('excerpt', ''))
        lc = lead.get('country') or lead.get('c')
        lt, lf = toks(t), figs(t + ' ' + ex)
        lb = bodies(t) | bodies(ex[:500])
        ll = locs(str(lead.get('symbol') or lead.get('locator') or lead.get('url') or ''))
        for k in ('DUP_HELD_IDX', 'DUP_NOTE'):
            lead.pop(k, None)

        key = (frozenset(sorted(lt)[:6]), lc)
        if key in seen:
            lead['DUP_FLAG'] = 'internal'
            lead['DUP_NOTE'] = 'the same item is already banked as: %s' % seen[key][:70]
            out['internal'] += 1
            continue
        seen[key] = t

        # a deliberately removed record is the strongest signal there is
        hit = None
        for rn, why, rf, rt, rb, rc in R:
            if lc and rc and lc != rc:
                continue
            tj = len(lt & rt) / max(1, len(lt | rt))
            sf = {x for x in (lf & rf) if dff.get(x, 0) <= RARE_FIG}
            sb = {x for x in (lb & rb) if dfb.get(x, 0) <= RARE_BODY}
            if sf:
                hit = (rn, why, 'shares the rare figure %s' % sorted(sf)[0]); break
            if tj >= 0.50:
                hit = (rn, why, 'title overlap %.2f' % tj); break
            if sb and tj >= 0.20:
                hit = (rn, why, 'both name "%s" and the titles overlap %.2f'
                       % (sorted(sb, key=len, reverse=True)[0], tj)); break
        if hit:
            lead['DUP_FLAG'] = 'REMOVED'
            lead['DUP_NOTE'] = ('MATCHES A DELIBERATELY REMOVED RECORD: "%s" (%s). READ THE REASON: %s'
                                % (hit[0][:70], hit[2], ' '.join(str(hit[1]).split())[:200]))
            out['REMOVED'] += 1
            continue

        best = (0.0, None, '')
        for i, hn, ht, hf, hb, hl, hc in H:
            if lc and hc and lc != hc:
                continue
            s, why = 0.0, []
            if ll & hl:
                k = sorted(ll & hl)[0]
                s += 1.0; why.append('same %s %s, one locator is one prosecution' % k)
            tj = len(lt & ht) / max(1, len(lt | ht))
            if tj > 0:
                s += tj; why.append('title overlap %.2f' % tj)
            for v in (lf & hf):
                n = dff.get(v, 0)
                s += 0.6 if n <= RARE_FIG else (0.25 if n <= 8 else 0.05)
                why.append('figure %s (in %d records)' % (v, n))
            for v in (lb & hb):
                n = dfb.get(v, 0)
                if n <= RARE_BODY:
                    s += 0.7; why.append('both name "%s", a body in only %d record(s)' % (v, n))
            if s > best[0]:
                best = (s, i, '; '.join(why[:3]))
        sc, i, why = best
        if i is None:
            lead['DUP_FLAG'] = 'none'; out['none'] += 1; continue
        lead['DUP_FLAG'] = 'high' if sc >= 0.85 else ('check' if sc >= 0.40 else 'none')
        lead['DUP_HELD_IDX'] = i
        lead['DUP_NOTE'] = ('closest held record is %d: "%s" (score %.2f — %s)'
                            % (i, cases[i]['n'][:68], sc, why))
        out[lead['DUP_FLAG']] += 1

    json.dump({'note': __doc__, 'candidates': bank},
              open(bankf, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('flags:', dict(out))
    write_cells(bank)
    return bank


HEADER = '''# %d banked leads for inf=%s bk=%s, cleanest first.
# Every lead names the CLOSEST held record, with a score and the reason, so you always have
# something specific to compare against rather than a bare verdict.
#   none    - nothing on the map is close. Work these first.
#   check   - something is close. Read the named record before spending a fetch.
#   high    - almost certainly already held. Skip the fetch.
#   REMOVED - matches a record deliberately removed from the map. READ THE REASON:
#             "Duplicate of the kept record..." means find the kept record instead;
#             any other reason means the case SHAPE fails the test and a new one will too.
#   internal- the same lead was filed twice. Write it once.
#
# Three signals, each weighted by how rare it is on the map, because a common one carries no
# information: a shared figure (10,000 is in 77 held records; a figure in one or two is strong),
# a shared NAMED BODY ("ministry of defence" is in 17; "ASP Trapani" identifies one case), and an
# identical single-case locator (one DNA release or case profile is one prosecution).
#
# The body signal exists because an agent measured 0 of 25 records from this bank: lead titles
# paraphrase held titles with no shared figure, so title matching missed every one of them.
# Its words: "a none flag on an Italian health lead means nothing; the body name is the tell."
#
# AND READ data/removed_records.json's DROP REASONS BEFORE THIS FILE. Only a handful of banked
# leads match a removed record, but about 75 removed cases sit in crime+legis/court alone, and
# the reasons are a specification for what not to write at all. Two agents withdrew finished
# records against that list, and both found the collisions by discovery, not from this bank.
#
# NOTHING has been removed from this bank. A flag you disprove is a real lead.

'''


def write_cells(bank, outdir='/home/claude/work/b5/leads2'):
    os.makedirs(outdir, exist_ok=True)
    for fn in os.listdir(outdir):
        os.remove(os.path.join(outdir, fn))
    cells = collections.defaultdict(list)
    for c in bank:
        cells[(c.get('inf'), c.get('bk'))].append(c)
    order = {'none': 0, 'check': 1, 'internal': 2, 'high': 3, 'REMOVED': 4}
    for (i, b), rows in cells.items():
        if not i or not b:
            continue
        rows.sort(key=lambda r: order.get(r.get('DUP_FLAG', 'none'), 0))
        with open(os.path.join(outdir, '%s_%s.txt' % (i, b)), 'w', encoding='utf-8') as f:
            f.write(HEADER % (len(rows), i, b))
            for c in rows:
                f.write('FLAG: %s\n' % c.get('DUP_FLAG'))
                if c.get('DUP_NOTE'):
                    f.write('  %s\n' % c['DUP_NOTE'])
                f.write('TITLE: %s\nCOUNTRY: %s\nLOCATOR: %s\n'
                        % (c.get('title') or c.get('n', ''), c.get('country') or c.get('c', ''),
                           c.get('symbol') or c.get('locator') or c.get('url', '')))
                f.write('EXCERPT: %s\nNOTE: %s\n\n'
                        % (str(c.get('excerpt', ''))[:420], str(c.get('note', ''))[:200]))
    print('wrote %d per-cell lead files to %s' % (len(os.listdir(outdir)), outdir))


if __name__ == '__main__':
    main()
