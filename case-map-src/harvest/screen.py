#!/usr/bin/env python3
"""Mechanical screen over the harvested text, before any agent is dispatched.

Round 21 established what separates a case from a drop: whether the works needed
a construction site people were living on. The project's own resettlement plan
usually says so in plain language, and five forms of that sentence were found by
hand across earlier rounds. This greps all of them, plus the relocation-count
patterns, over every harvested document.

The output is three buckets:

  drop_candidate  a null sentence, and no relocation count anywhere in any
                  document for that project. Recorded with the sentence and its
                  document and line, so the drop quotes a document.
  survivor        a relocation count, a demolition figure, or death or
                  compensation language that needs a reader.
  unscreened      neither, so nothing mechanical can decide it.

The screen narrows the queue; it does not filter it. A project with a framework
plus many subproject plans has no single sentence to grep, which is the known
limit, so a null sentence is only allowed to decide a drop when no count of any
kind appears anywhere for that project.
"""
import json, os, re, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, 'cache')

# Flatten runs of whitespace before matching: these sentences are broken across
# lines and padded by the layout of the source tables.
NULL_PATTERNS = [
    (r'no\s+physical\s+relocation\s+of\s+(?:the\s+)?households?\s+(?:is|are|will\s+be)\s+(?:required|needed|envisaged|expected|anticipated)', 'no physical relocation of households is required'),
    (r'no\s+(?:loss|losses)\s+of\s+primary\s+and\s+secondary\s+structures', 'no loss of primary and secondary structures'),
    (r'no\s+(?:physical\s+)?displacement\s*(?:/|or|and)?\s*(?:of\s+people\s*)?(?:re)?settlement\s+(?:is|are|will\s+be)\s+(?:required|needed|envisaged)', 'no displacement / resettlement is required'),
    (r'there\s+will\s+be\s+no\s+relocation\s+of\s+(?:people|persons|households|residents)', 'there will be no relocation of people'),
    (r'(?:none|no)\s+of\s+the\s+project[\s-]affected\s+(?:people|persons|households)\s+will\s+(?:be\s+severely\s+affected\s+or\s+)?(?:require|need)\s+relocation', 'none of the project affected people will require relocation'),
    (r'(?:did|does)\s+not\s+(?:have|involve|entail|require)\s+any\s+(?:house\s+)?demolition', 'did not have any house demolition'),
    (r'no\s+(?:house|housing|residential|building)\s+demolition\s+(?:is|was|will\s+be)?\s*(?:required|needed|involved|envisaged|necessary)?', 'no house demolition'),
    (r'no\s+(?:involuntary\s+)?(?:land\s+acquisition|resettlement)\s+(?:is|was|will\s+be)\s+(?:required|needed|involved|envisaged|anticipated|expected)', 'no land acquisition or resettlement is required'),
    (r'no\s+(?:physical|economic)?\s*(?:re)?settlement\s+impacts?', 'no resettlement impacts'),
    (r'(?:op|opn|bp)\s*/?\s*(?:bp)?\s*4\.12[^.]{0,80}not\s+(?:be\s+)?trigger', 'OP 4.12 not triggered'),
    (r'(?:policy\s+on\s+)?involuntary\s+resettlement[^.]{0,60}(?:is\s+)?not\s+(?:be\s+)?trigger', 'involuntary resettlement not triggered'),
    (r'no\s+(?:people|persons|households|families|residents)\s+(?:were|was|will\s+be|are)\s+(?:physically\s+)?(?:relocated|resettled|displaced|moved)', 'no people were relocated'),
    (r'no\s+(?:project[\s-]affected\s+)?(?:person|people|household)s?\s+(?:required|needed)\s+(?:physical\s+)?relocation', 'no people required relocation'),
]

# A count of people or households with a relocation verb attached, or a
# demolition figure, which round 20 ruled meets limb (b) without a count.
COUNT_PATTERNS = [
    (r'([\d][\d,\.]{0,12})\s+(?:households?|families|persons?|people|residents?|PAPs?|project[\s-]affected\s+(?:persons?|people|households?))\s+(?:were\s+|was\s+|have\s+been\s+|had\s+been\s+|are\s+|been\s+)?(?:physically\s+)?(?:relocated|resettled|rehoused|re-housed|displaced|moved|shifted|evicted)', 'count + relocation verb'),
    (r'(?:relocated|resettled|rehoused|re-housed|displaced|moved|shifted|evicted)\s+(?:a\s+total\s+of\s+)?([\d][\d,\.]{0,12})\s+(?:households?|families|persons?|people|residents?|PAPs?)', 'relocation verb + count'),
    (r'(?:number\s+of\s+)?(?:relocated|resettled)\s+households?', 'relocated-households column'),
    (r'([\d][\d,\.]{0,12})\s*(?:square\s+met(?:re|er)s?|m2|m²|sq\.?\s*m)\s+of\s+(?:hous|resident|build|private\s+hous)', 'demolished housing area'),
    (r'(?:house|housing|residential|building)\s+demolition[^.]{0,80}?([\d][\d,\.]{2,12})', 'house demolition with a figure'),
    (r'demolish(?:ed|ing)?\s+([\d][\d,\.]{0,12})\s*(?:square\s+met(?:re|er)s?|m2|m²|houses?|dwellings?|structures?|buildings?)', 'demolished count'),
    (r'([\d][\d,\.]{0,12})\s+(?:houses?|dwellings?|homes?)\s+(?:were\s+|was\s+)?(?:demolished|removed|dismantled|cleared)', 'houses demolished'),
]

# Harm language that earns a reader even with no relocation count: limb (b).
HARM_PATTERNS = [
    (r'fatalit|fatal\s+accident|(?:worker|workers|labourer|labourer|person|people)\s+(?:was|were)\s+killed|loss\s+of\s+life|death[s]?\s+(?:occurred|were\s+reported)', 'death language'),
    (r'compensation[^.]{0,70}(?:not\s+(?:yet\s+)?(?:been\s+)?paid|outstanding|in\s+arrears|unpaid|pending|delayed|withheld)', 'compensation arrears'),
    (r'(?:not\s+(?:yet\s+)?paid|outstanding|unpaid)[^.]{0,60}compensation', 'compensation arrears'),
    (r'replacement\s+cost', 'replacement cost'),
    (r'below\s+(?:the\s+)?(?:market|replacement)\s+(?:value|cost|rate)', 'below replacement cost'),
    (r'court\s+deposit|deposited\s+with\s+the\s+court|paid\s+into\s+court', 'court deposit'),
    (r'(?:livelihood|income)s?[^.]{0,60}not\s+(?:been\s+)?restored', 'livelihoods not restored'),
    (r'(?:did\s+not\s+(?:follow|comply)|non[\s-]?compliance|not\s+in\s+compliance)[^.]{0,60}(?:4\.12|resettlement)', 'resettlement non-compliance'),
    (r'(?:grievance|complaint)s?[^.]{0,40}(?:unresolved|outstanding|not\s+resolved)', 'unresolved grievances'),
    (r'arrest(?:ed)?|detain(?:ed)?|police', 'arrest or police'),
]

# The plan-reprint trap, which decided two drops in round 20.
TRAP_PATTERNS = [
    (r'envisaged', 'the appraisal\'s own word "envisaged"'),
    (r'will\s+be\s+(?:relocated|resettled)', 'a plan verb, "will be relocated"'),
]

# Staff statements, which are not documents.
STAFF_PATTERNS = [
    (r'informed\s+IEG', 'informed IEG'),
    (r'the\s+project\s+team\s+(?:provided|stated|clarified|informed|confirmed)', 'the project team provided'),
    (r'the\s+World\s+Bank\s+team\s+stated', 'the World Bank team stated'),
    (r'as\s+clarified\s+by\s+the\s+project\s+team', 'as clarified by the project team'),
]

WS = re.compile(r'[ \t ]+')


def load(path):
    try:
        return open(path, encoding='utf-8', errors='replace').read()
    except Exception:
        return ''


def scan_text(flat, pats):
    """Return [(label, matched text, position)] over whitespace-flattened text."""
    out = []
    for rx, label in pats:
        for m in re.finditer(rx, flat, re.I):
            out.append((label, m.group(0)[:200], m.start()))
    return out


def context(flat, pos, width=320):
    a = max(0, pos - width // 2)
    return flat[a:a + width].strip()


def main():
    man = sys.argv[1] if len(sys.argv) > 1 else 'harvest_manifest.json'
    outp = sys.argv[2] if len(sys.argv) > 2 else 'screen.json'
    M = json.load(open(os.path.join(HERE, man)))
    R = json.load(open(os.path.join(HERE, 'resolved.json')))

    # map each P-number (and sibling) back to its lead row
    rows_by_pid = defaultdict(list)
    for r in R:
        if 'pid' in r:
            rows_by_pid[r['pid']].append(r)
            for s in r.get('sibling_pids', []):
                rows_by_pid[s].append(r)

    results = {}
    for pid in sorted(M):
        docs = [d for d in M[pid].get('docs', [])
                if d.get('route') in ('txt', 'pdf', 'cached') and d.get('path')]
        rec = {'pid': pid, 'n_docs': len(docs), 'tags': sorted({d['tag'] for d in docs}),
               'nulls': [], 'counts': [], 'harm': [], 'traps': [], 'staff': [],
               'docs': [{'tag': d['tag'], 'docdt': d['docdt'], 'path': d['path'],
                         'title': d.get('title', '')[:140], 'bytes': d.get('bytes', 0)}
                        for d in docs]}
        for d in docs:
            p = os.path.join(HERE, d['path'])
            if not os.path.exists(p):
                continue
            raw = load(p)
            flat = WS.sub(' ', raw.replace('\n', ' '))
            where = f"{d['tag']} {d['docdt']}"
            for label, txt, pos in scan_text(flat, NULL_PATTERNS):
                rec['nulls'].append({'doc': where, 'file': d['path'], 'form': label,
                                     'text': txt, 'context': context(flat, pos)})
            for label, txt, pos in scan_text(flat, COUNT_PATTERNS):
                rec['counts'].append({'doc': where, 'file': d['path'], 'form': label,
                                      'text': txt, 'context': context(flat, pos)})
            for label, txt, pos in scan_text(flat, HARM_PATTERNS):
                rec['harm'].append({'doc': where, 'form': label, 'text': txt,
                                    'context': context(flat, pos)})
            for label, txt, pos in scan_text(flat, TRAP_PATTERNS):
                rec['traps'].append({'doc': where, 'form': label})
            for label, txt, pos in scan_text(flat, STAFF_PATTERNS):
                rec['staff'].append({'doc': where, 'form': label})

        # counts and harm that sit in an OUTCOME document decide more than a plan
        outcome_tags = {'ICR', 'ICRR', 'ICRX', 'PPAR'}
        rec['counts_in_outcome'] = [c for c in rec['counts']
                                    if c['doc'].split()[0] in outcome_tags]
        rec['harm_in_outcome'] = [h for h in rec['harm']
                                  if h['doc'].split()[0] in outcome_tags]
        has_outcome_doc = bool(outcome_tags & set(rec['tags']))

        # Order matters. The handoff's rule is that a null sentence in the
        # project's own resettlement plan plus no count anywhere is a drop, and
        # it does not require an outcome document, so that test comes first.
        if not rec['n_docs']:
            rec['bucket'] = 'no_documents'
        elif rec['nulls'] and not rec['counts']:
            rec['bucket'] = 'drop_candidate'
        elif not has_outcome_doc:
            rec['bucket'] = 'no_outcome_document'
        elif rec['counts_in_outcome'] or rec['harm_in_outcome']:
            rec['bucket'] = 'survivor'
        elif rec['counts']:
            rec['bucket'] = 'survivor_plan_only'
        else:
            rec['bucket'] = 'unscreened'

        rec['leads'] = [{'project': x['project'], 'approved': x['approved'],
                         'countries': x['countries'], 'displaced': x['displaced'],
                         'status': x['status'], 'complaint': x.get('complaint')}
                        for x in rows_by_pid.get(pid, [])]
        results[pid] = rec

    json.dump(results, open(os.path.join(HERE, outp), 'w'), indent=1)

    from collections import Counter
    b = Counter(r['bucket'] for r in results.values())
    print("buckets:", dict(b), file=sys.stderr)
    for name in ('drop_candidate', 'no_outcome_document', 'no_documents', 'unscreened'):
        pids = [p for p, r in results.items() if r['bucket'] == name]
        print(f"\n{name} ({len(pids)}):", file=sys.stderr)
        for p in pids[:40]:
            r = results[p]
            lead = r['leads'][0]['project'][:46] if r['leads'] else '?'
            extra = ''
            if r['nulls']:
                extra = ' | ' + r['nulls'][0]['form']
            print(f"  {p} {lead!r}{extra}", file=sys.stderr)


if __name__ == '__main__':
    main()
