#!/usr/bin/env python3
"""Pre-extract the decisive sentences, one brief per project.

This is step 3 of the compression plan and the part that is safe: it decides
nothing, it hands a writer candidate sentences with their document so the writer
verifies and judges instead of searching, which is where most of the per-case
time goes.

The one piece of real mechanical work here is the plan-reprint trap. Round 20
dropped Xining and Inner Mongolia on it and round 22 found a sharper version
sitting in the completion report's own results annex: the appraisal's figure
reprinted where a reader takes it for an outcome. The standing instruction is to
grep the appraisal for any resettlement figure the completion report gives. That
is mechanical, so it is done here for every project: every figure that appears in
a resettlement context in an outcome document is checked against the appraisal
and the resettlement plan, and flagged when it appears in both.

Nothing in a brief is a conclusion. A null sentence is listed as a caution
because the screen was measured and found to drop about one real case in nine
when it was allowed to decide; see the round notes.
"""
import json, os, re, sys
from collections import defaultdict, Counter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'briefs')
os.makedirs(OUT, exist_ok=True)
WS = re.compile(r'[ \t ]+')

OUTCOME = {'ICR', 'ICRR', 'ICRX', 'PPAR'}
PLAN = {'PAD', 'SAR', 'PP', 'SDR', 'RP', 'RAP', 'IPP'}

# The Bank files implementation reports, mission reports and monitoring reports
# under docty "Resettlement Plan". Round 31's West Africa writer found two of
# them inside P129713's 22 RP-tagged documents — a June 2021 Kananga
# implementation report recording one household paid and moved, and a February
# 2019 Kolwezi mission report — and the brief had therefore reported
# relocation_counts_in_outcome_doc as 0 for a row that had them. So the
# plan/outcome split cannot rest on docty alone; the title and the opening of
# the document decide it too.
OUTCOME_TITLE = re.compile(
    r'implementation\s+report|progress\s+report|monitoring\s+report|'
    r'completion\s+report|mission\s+report|rapport\s+de\s+mission|'
    r'mise\s+en\s+\u0153uvre|rapport\s+de\s+suivi|rapport\s+d.?ex\u00e9cution|'
    r'audit\s+report|ex[\s-]?post', re.I)


def effective_tag(tag, title, head=''):
    """Treat a plan-tagged document as an outcome document when it is one."""
    if tag in PLAN and (OUTCOME_TITLE.search(title or '')
                        or OUTCOME_TITLE.search(head or '')):
        return 'RP-OUTCOME'
    return tag

RELOC = (r'relocat|resettl|rehous|re-hous|displac|demolish|demolit|evict|'
         r'expropriat|compensat|land acquisition|shifted|moved')

# Core phrases only. Context is sliced in Python rather than padded into the
# regex: a padded pattern such as [^.]{0,160} backtracks badly over text that
# has been flattened to one line, and made this pass about ten times slower.
PAT = {
 'count with a relocation verb': [
   r'\b\d[\d,\.]{0,12}\s+(?:households?|families|persons?|people|residents?|PAPs?|project[\s-]affected\s+(?:persons?|people|households?))\s+(?:were\s+|was\s+|have\s+been\s+|had\s+been\s+|are\s+|been\s+)?(?:physically\s+)?(?:relocated|resettled|rehoused|re-housed|displaced|moved|shifted|evicted)',
   r'(?:relocated|resettled|rehoused|re-housed|displaced|moved|shifted|evicted)\s+(?:a\s+total\s+of\s+)?\d[\d,\.]{0,12}\s+(?:households?|families|persons?|people|residents?|PAPs?)',
 ],
 'affected, NOT a relocation count': [
   r'\b\d[\d,\.]{0,12}\s+(?:households?|families|persons?|people|PAPs?|project[\s-]affected\s+(?:persons?|people|households?))\s+(?:were\s+|was\s+|are\s+)?affected',
   r'\baffected\s+\d[\d,\.]{0,12}\s+(?:households?|families|persons?|people)',
 ],
 'demolished housing': [
   r'\b\d[\d,\.]{0,12}\s*(?:square\s+met(?:re|er)s?|m2|m\u00b2|sq\.?\s*m|mu)\s+of\s+(?:hous|resident|build|private\s+hous)',
   r'\b\d[\d,\.]{0,12}\s+(?:houses?|dwellings?|homes?|structures?)\s+(?:were\s+|was\s+)?(?:demolished|removed|dismantled|cleared)',
   r'(?:house|housing|residential|building)\s+demolition',
 ],
 'death, with any cause given': [
   r'\bfatalit(?:y|ies)\b', r'\bfatal\s+accident', r'\b(?:was|were)\s+killed\b',
   r'\bloss\s+of\s+life\b', r'\bworkers?\s+died\b',
 ],
 'compensation unpaid or late': [
   r'compensation[^.]{0,60}?(?:not\s+(?:yet\s+)?(?:been\s+)?paid|outstanding|in\s+arrears|unpaid|pending|delayed|withheld)',
   r'(?:not\s+(?:yet\s+)?paid|outstanding|unpaid|arrears)[^.]{0,60}?compensation',
 ],
 'replacement cost': [r'replacement\s+cost'],
 'paid into court': [r'court\s+deposit', r'deposited\s+with\s+the\s+court', r'paid\s+into\s+court', r'revenue\s+deposit'],
 'livelihoods not restored': [r'(?:livelihood|income)s?[^.]{0,60}?not\s+(?:been\s+)?restored'],
 'resettlement non-compliance': [
   r'(?:did\s+not\s+(?:follow|comply\s+with)|non[\s-]?compliance\s+with|not\s+in\s+compliance\s+with)[^.]{0,70}?(?:4\.12|resettlement|safeguard)',
 ],
 'arrests, police or force': [r'\barrested\b', r'\bdetained\b', r'armed\s+police', r'\bbulldozer'],
 # Three gaps the round 31 writers found by hand. Each decided a case.
 'eviction, or people never traced': [
   r'\bevict(?:ed|ion|ions)\b', r'\bexpelled\b',
   r'(?:could\s+not\s+be|never|not)\s+(?:be\s+)?(?:traced|located|reached|found)',
   r'\buntraced\b', r'remain(?:ed|s)?\s+unpaid',
 ],
 'household-loss table label (incl. French)': [
   r'[Nn]ombre\s+de\s+m\u00e9nages[^.\n]{0,70}',
   r'(?:number|no\.)\s+of\s+(?:households?|families|persons?)\s+(?:losing|who\s+lost|that\s+lost|displaced|relocated|resettled|affected)',
   r'm\u00e9nages\s+(?:ayant|qui\s+ont)\s+perdu',
   r'personnes?\s+(?:affect\u00e9|d\u00e9plac\u00e9|recas\u00e9)[a-z\u00e9s]*',
 ],
 'borrower\'s own account, not the Bank\'s': [
   r"[Bb]orrower'?s?\s+(?:own\s+)?(?:ICR|completion\s+report|report|comments|annex)",
   r'Annex\s+\d+[^.\n]{0,40}Borrower',
   r'Comments\s+on\s+Draft\s+ICR',
   r'rapport\s+de\s+(?:mission|mise\s+en\s+\u0153uvre|suivi)',
 ],
 'PLAN VERB \u2014 the reprint trap': [
   r'\benvisaged\b', r'will\s+be\s+(?:relocated|resettled|displaced|acquired)',
   r'are\s+to\s+be\s+(?:relocated|resettled)',
 ],
 'STAFF STATEMENT \u2014 not a document': [
   r'informed\s+IEG', r'the\s+project\s+team\s+(?:provided|stated|clarified|informed|confirmed)',
   r'the\s+World\s+Bank\s+team\s+stated', r'as\s+clarified\s+by\s+the\s+project\s+team',
 ],
 'CAUTION \u2014 null sentence (does NOT decide a drop)': [
   r'no\s+(?:physical\s+)?relocation\s+of\s+(?:the\s+)?households?',
   r'no\s+(?:involuntary\s+)?(?:land\s+acquisition|resettlement|displacement)\s+(?:is|was|will\s+be)\s+(?:required|needed|involved|envisaged|anticipated|expected)',
   r'there\s+will\s+be\s+no\s+relocation\s+of\s+(?:people|persons|households|residents)',
   r'(?:did|does)\s+not\s+(?:have|involve|entail|require)\s+any\s+(?:house\s+)?demolition',
   r'4\.12[^.]{0,60}?not\s+(?:be\s+)?trigger',
 ],
}
PRE, POST = 170, 260
COMPILED = {k: [re.compile(p, re.I) for p in v] for k, v in PAT.items()}

NUM = re.compile(r'\b\d[\d,]{1,12}(?:\.\d+)?\b')


def load(p):
    try:
        return open(p, encoding='utf-8', errors='replace').read()
    except Exception:
        return ''


def flat(s):
    return WS.sub(' ', s.replace('\n', ' '))


RELOC_RX = re.compile(RELOC, re.I)

# A resettlement figure is a number tied to a unit of people or housing, not any
# number that happens to sit near the word "resettlement". Without this, the
# reprint check fills up with transmission voltages, line lengths, years and page
# numbers, because a project's technical specs sit next to its land acquisition.
UNIT_AFTER = re.compile(
    r'\s{0,3}(?:households?|families|persons?|people|residents?|PAPs?|'
    r'project[\s-]affected\s+(?:persons?|people|households?)|houses?|dwellings?|'
    r'homes?|structures?|shops?|enterprises?|square\s+met(?:re|er)s?|m2|m\u00b2|'
    r'sq\.?\s*m|mu|hectares?|ha\b|acres?)', re.I)
VERB_BEFORE = re.compile(
    r'(?:relocat|resettl|rehous|re-hous|displac|demolish|demolit|evict|'
    r'expropriat|acquir|compensat)[a-z]*\W{0,24}$', re.I)


def resettlement_figures(text):
    """Figures carrying a people-or-housing unit in a resettlement context."""
    found = {}
    for n in NUM.finditer(text):
        raw = n.group()
        v = raw.rstrip('.').replace(',', '')
        try:
            f = float(v)
        except ValueError:
            continue
        if f < 4 or f > 5e8:
            continue
        tail = text[n.end():n.end() + 60]
        head = text[max(0, n.start() - 60):n.start()]
        has_unit = bool(UNIT_AFTER.match(tail))
        has_verb = bool(VERB_BEFORE.search(head))
        if not (has_unit or has_verb):
            continue
        # a bare year with no unit is a date, not a count
        if not has_unit and 1900 <= f <= 2100 and '.' not in v:
            continue
        # require the surrounding text to be about resettlement at all
        ctx_a = max(0, n.start() - 300)
        ctx = text[ctx_a:n.end() + 300]
        if not RELOC_RX.search(ctx):
            continue
        if v in found:
            continue
        a = max(0, n.start() - 160)
        found[v] = text[a:n.end() + 180].strip()[:320]
    return found


def main():
    M = json.load(open(os.path.join(HERE, 'harvest_manifest.json')))
    S = json.load(open(os.path.join(HERE, 'screen.json')))
    R = json.load(open(os.path.join(HERE, 'resolved.json')))
    try:
        NOTES = json.load(open(os.path.join(HERE, 'icr_notes.json')))
    except Exception:
        NOTES = {'own_recovered': {}, 'parent_candidates': {}}

    index = []
    for rec in R:
        if 'pid' not in rec:
            continue
        pids = [rec['pid']] + rec.get('sibling_pids', [])
        docs = []
        for p in pids:
            for d in M.get(p, {}).get('docs', []):
                if d.get('route') in ('txt', 'pdf', 'cached') and d.get('path'):
                    dd = dict(d); dd['pid'] = p
                    docs.append(dd)
        slug = re.sub(r'[^a-z0-9]+', '-', rec['project'].lower()).strip('-')[:48]
        name = f"{rec['pid']}_{slug or 'project'}.md"

        texts = {}
        for d in docs:
            fp = os.path.join(HERE, d['path'])
            if os.path.exists(fp):
                texts[d['path']] = flat(load(fp))

        # the plan-reprint trap, mechanised
        out_nums, plan_nums = {}, {}
        for d in docs:
            t = texts.get(d['path'], '')
            if not t:
                continue
            got = resettlement_figures(t)
            eff = effective_tag(d['tag'], d.get('title', ''), t[:3000])
            tgt = (out_nums if (d['tag'] in OUTCOME or eff == 'RP-OUTCOME')
                   else (plan_nums if d['tag'] in PLAN else None))
            if tgt is None:
                continue
            for v, ctx in got.items():
                tgt.setdefault(v, []).append((f"{d['tag']} {d['docdt']}", ctx))
        reprinted = sorted(set(out_nums) & set(plan_nums),
                           key=lambda v: -float(v.replace(',', '')))

        L = []
        A = L.append
        A(f"# {rec['project']}\n")
        A(f"**Bank project:** {rec['pid']}" +
          (f" (also filed as {', '.join(rec.get('sibling_pids', []))})" if rec.get('sibling_pids') else ""))
        A(f"**ICIJ row:** approved {rec['approved']}, {', '.join(rec['countries'])}, "
          f"cost {rec['cost']}, ICIJ status {rec['status']}, "
          f"ICIJ complaint flag {rec.get('complaint')}")
        A(f"**ICIJ's displacement estimate:** {rec['displaced']} — this is ICIJ's count of "
          f"project-affected people and must never be put in `displaced`. "
          f"See \"The ICIJ figures\" in the handoff.")
        if rec.get('match_note'):
            A(f"**On the match:** {rec['match_note']}")
        A("")
        A("## Documents harvested (read these from disk; do not re-fetch)\n")
        if not docs:
            A("None. The wds API returned no documents for this number. Check the parent and "
              "sibling numbers and try a `qterm` title search before concluding anything.\n")
        for d in sorted(docs, key=lambda x: (x['tag'], x['docdt'])):
            eff = effective_tag(d['tag'], d.get('title', ''),
                                texts.get(d['path'], '')[:3000])
            mark = ('  **<- filed as a plan but reads as an outcome document; '
                    'treat its figures as outcomes**' if eff == 'RP-OUTCOME' else '')
            A(f"- `{d['path']}` — **{d['tag']}** {d['docdt']} — {d.get('title', '')[:120]}{mark}")
        A("")
        tags_here = {d['tag'] for d in docs}
        if rec['pid'] in NOTES.get('own_recovered', {}):
            A("**Route note:** " + ', '.join(NOTES['own_recovered'][rec['pid']]) +
              " for this project is filed under its own number but `wds?projectid=` "
              "did not return it; a `qterm` title search did. It is in the list above. "
              "Add that to the reasons a report that looks undisclosed is not.\n")
        if not (tags_here & OUTCOME):
            A("## No completion report or assessment report is reachable\n")
            A("`wds?projectid=` returned none, and a `qterm` title search on the project "
              "name returned none filed under this number. Before writing that the report "
              "is undisclosed, check the parent and sibling numbers yourself. Where the "
              "report genuinely is undisclosed, the Evaluation Group's review, which cites "
              "it by paragraph, is the only route, and the card must say so.\n")
            cands = NOTES.get('parent_candidates', {}).get(rec['pid'], [])
            if cands:
                A("Candidate parent or sibling projects. These are country-checked name "
                  "matches and nothing more: **verify each against the documents before "
                  "using it, and never treat one as this project's own report.** A "
                  "mechanical token match put Benin's Transport Infrastructure "
                  "Rehabilitation and Maintenance Project against Uruguay's Transport "
                  "Infrastructure Maintenance and Rural Access on two shared words.\n")
                for c in cands:
                    A(f"- `{c['pid']}` — {str(c.get('title'))[:120]} "
                      f"({c.get('docty')}, {c.get('docdt')}) — shared words: "
                      f"{', '.join(c.get('shared_words', []))}")
                A("")
        sc = S.get(rec['pid'], {})
        A(f"**Screen bucket:** {sc.get('bucket', '?')} "
          f"(ranking only — the screen was measured and drops about one real case in nine "
          f"when allowed to decide, so it decides nothing here)\n")

        if reprinted:
            A("## The plan-reprint trap — figures appearing in BOTH an outcome document and a plan\n")
            A("Round 20 dropped two projects on this and round 22 found it inside the completion "
              "report's own results annex. Each figure below sits in a resettlement context in an "
              "outcome document **and** in the appraisal or resettlement plan. That does not make "
              "the project a drop; it means that figure may be a plan reprinted as an outcome, and "
              "the verb usually gives it away. Check the verb before using any of them.\n")
            for v in reprinted[:14]:
                A(f"- **{v}**")
                for where, ctx in out_nums[v][:1]:
                    A(f"    - outcome ({where}): …{ctx[:230]}…")
                for where, ctx in plan_nums[v][:1]:
                    A(f"    - plan ({where}): …{ctx[:230]}…")
            A("")

        A("## Candidate sentences, by kind\n")
        A("Each is a grep hit, not a finding. Verify every one against the document named before "
          "using it, and read the whole paragraph it sits in — selective quotation is the fault "
          "that has decided more drops on this map than any other.\n")
        A("**Where this extraction is known to be thin, from round 31's writers.** Four of ten "
          "cases in one batch turned on a passage no candidate sentence surfaced, and the misses "
          "ran to a pattern: text inside footnotes, compensation-status tables dated after the "
          "closing date, counts sitting in a table's row label rather than in a sentence, and the "
          "borrower's own annex to the completion report, which sometimes contradicts the Bank's "
          "main text. Patterns for the first three were added after that round; the borrower's "
          "annex is flagged but not parsed. **Read the completion report's footnotes and its "
          "borrower annex yourself.**\n")
        total_hits = 0
        for kind, pats in COMPILED.items():
            hits = []
            seen = set()
            for d in sorted(docs, key=lambda x: (x['tag'] not in OUTCOME, x['tag'], x['docdt'])):
                t = texts.get(d['path'], '')
                if not t:
                    continue
                for rx in pats:
                    for m in rx.finditer(t):
                        a = max(0, m.start() - PRE)
                        txt = ' '.join(t[a:m.end() + POST].split())[:460]
                        key = ' '.join(m.group(0).split()).lower()[:70]
                        if key in seen:
                            continue
                        seen.add(key)
                        hits.append((f"{d['tag']} {d['docdt']}", d['path'], txt))
                        if len(hits) > 400:
                            break
            if not hits:
                continue
            total_hits += len(hits)
            A(f"### {kind}  ({len(hits)})\n")
            for where, path, txt in hits[:16]:
                A(f"- **[{where}]** …{txt}…")
            if len(hits) > 16:
                A(f"- _…and {len(hits) - 16} more of this kind; grep the files for the rest._")
            A("")

        A("## What to decide\n")
        A("Apply the forward rule in the handoff, item 9 of \"What is actually open\": a case needs "
          "either (a) a document counting people or households actually **relocated**, or (b) a "
          "specific documented harm to identifiable people — deaths with a stated cause, injuries, "
          "arrests, land taken, compensation unpaid or below replacement cost, livelihoods not "
          "restored. Neither limb is a drop, and a card whose entire content is a count of people "
          "\"affected\" is a drop. Where a document records housing actually demolished, in a table "
          "with a separate enterprise column, limb (b) is met without a household count.\n")
        open(os.path.join(OUT, name), 'w').write('\n'.join(L))
        index.append({'pid': rec['pid'], 'file': name, 'project': rec['project'],
                      'countries': rec['countries'], 'approved': rec['approved'],
                      'displaced': rec['displaced'], 'status': rec['status'],
                      'bucket': sc.get('bucket', '?'), 'n_docs': len(docs),
                      'tags': sorted({d['tag'] for d in docs}),
                      'n_reprinted': len(reprinted), 'n_hits': total_hits,
                      'complaint': rec.get('complaint'),
                      'sibling_pids': rec.get('sibling_pids', [])})

    json.dump(index, open(os.path.join(HERE, 'brief_index.json'), 'w'), indent=1)
    print(f"briefs written: {len(index)}", file=sys.stderr)
    print("buckets:", dict(Counter(i['bucket'] for i in index)), file=sys.stderr)
    print("with a reprint-trap flag:", sum(1 for i in index if i['n_reprinted']), file=sys.stderr)
    print("no documents at all:", [i['pid'] for i in index if not i['n_docs']], file=sys.stderr)
    print("median candidate hits:",
          sorted(i['n_hits'] for i in index)[len(index) // 2], file=sys.stderr)


if __name__ == '__main__':
    main()
