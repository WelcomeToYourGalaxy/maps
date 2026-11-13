"""Round 16: take the researcher's voice out of the ten new cards.

Usage: python3 case-map-src/r16_fix_voice.py [--dry-run]
Idempotent in the sense that it reports what it cannot find: once applied, a second
run prints all 20 as "old text not found", which is the signal that it is already done.

The facts are unchanged. Only the voice changes: a public card does not say
"I downloaded", "during this check" or "the draft", and the 947 cards already on
the map almost never do. Where a sentence recorded round bookkeeping rather than
a fact about the case, it goes entirely — that belongs in the check log.

Every replacement is an exact match inside one named field of one named case, so
nothing else can shift. In particular the Ache card's reference to MICI's own
draft report, circulated 21 February 2012, is a fact about the panel and is left
alone.
"""
import json, os, sys

P = os.path.dirname(os.path.abspath(__file__)) + '/base.html'
s = open(P, encoding='utf8').read()
dec = json.JSONDecoder()
i = s.index('window.CASES = ') + 15
C, n = dec.raw_decode(s[i:])
byid = {c['id']: c for c in C}

# (case id, field path, old, new)
FIX = [
 ('tbilisi-rustavi-ponichala-sutip', 'confidence_note',
  "both of which I downloaded and read in full:",
  "both read in full:"),

 ('peshawar-landfill-ghari-faiz-ullah', 'confidence_note',
  "a 137-page document ADB published under the project; I read its main body, roughly the first 30 pages, in full and searched the annexes for each figure quoted here.",
  "a 137-page document ADB published under the project. Its main body, roughly the first 30 pages, was read in full, and the annexes were searched for each figure quoted here."),

 ('sahiwal-piciip-land-and-sewage', 'confidence_note',
  "The land half of this case is now sourced entirely to ADB's own documents, and the Devdiscourse summary the draft rested on has been removed.",
  "The land half of this case is sourced entirely to ADB's own documents."),
 ('sahiwal-piciip-land-and-sewage', 'confidence_note',
  "I downloaded the Panel report and read it in full, including both annexes.",
  "The Panel report was read in full, including both annexes."),

 ('batumi-bypass-land-valuation', 'confidence_note',
  "The draft's third source, a monitoring report filed under project 50064-001, was removed:",
  "One ADB monitoring report filed under project 50064-001 is not used here:"),
 ('batumi-bypass-land-valuation', 'confidence_note',
  "I read the Lessons Learned publication in full, about 7,300 words.",
  "The Lessons Learned publication was read in full, about 7,300 words."),

 ('kolkata-keiip-tranche2-vendors', 'confidence_note',
  "it has not been tested by the Panel or by any independent body, and the draft's description of it as 'not in dispute' has been removed.",
  "it has not been tested by the Panel or by any independent body."),
 ('kolkata-keiip-tranche2-vendors', 'confidence_note',
  "I downloaded the Panel report and read its body, paragraphs 1 to 70, in full, and searched its annexes, about 45,500 words in all, for every figure and quote used here.",
  "The Panel report's body, paragraphs 1 to 70, was read in full, and its annexes searched, about 45,500 words in all, for every figure and quote used here."),

 ('malolos-clark-railway-row-pampanga', 'confidence_note',
  "both of which I read in full.",
  "both read in full."),

 ('ache-finca-470-ruta-10', 'confidence_note',
  "The ABC Color article was listed as a source by the writer of the draft and was not opened during this check, so no figure here rests on it alone.",
  "The ABC Color article is listed as a source but was not opened, so no figure here rests on it alone."),

 ('polihali-lhwp-phase-ii', 'lenders[0].role',
  "none of those pages opened during this check, so that figure is not carried here.",
  "none of those pages opened, so that figure is not carried here."),
 ('polihali-lhwp-phase-ii', 'lenders[2].role',
  "because the news report that gave one did not open during this check.",
  "because the news report that gave one did not open."),
 ('polihali-lhwp-phase-ii', 'suppression',
  "no finding on them was found in the documents opened for this check.",
  "no finding on them appears in the documents opened."),
 ('polihali-lhwp-phase-ii', 'displaced_note',
  "No figure for households actually moved was found in any page opened for this check.",
  "No figure for households actually moved appears in any page opened."),
 ('polihali-lhwp-phase-ii', 'displaced_note',
  "A news report carrying the LHDA's own count of households relocated by April 2025 did not open during this check, so no number is given here.",
  "A news report carrying the LHDA's own count of households relocated by April 2025 did not open, so no number is given here."),
 ('polihali-lhwp-phase-ii', 'outcome',
  "the arithmetic note is this check's, not Public Eye's.",
  "the arithmetic is noted here, not by Public Eye."),

 ('nis-railway-bypass-min-holding-tenants', 'confidence_note',
  "That report is the lender's own factual record, not the complainant's allegation, and I opened it and checked each figure in it.",
  "That report is the lender's own factual record, not the complainant's allegation, and each figure in it was checked."),

 ('bogota-metro-line1-predios', 'confidence_note',
  "No source I read explains the gap, and the explanation is unsourced.",
  "No source found explains the gap, so the explanation is unsourced."),
 ('bogota-metro-line1-predios', 'confidence_note',
  "which had made no findings when I looked.",
  "which had not reported any findings."),
 ('bogota-metro-line1-predios', 'displaced_note',
  "publishes no count of them in the article I read, so no displaced figure is given here.",
  "publishes no count of them in that article, so no displaced figure is given here."),
]


def get_set(case, path, newval=None):
    """Read or write a field, supporting lenders[0].role style paths."""
    if '[' in path:
        arr, rest = path.split('[', 1)
        idx, field = rest.split('].')
        target = case[arr][int(idx)]
        if newval is None:
            return target[field]
        target[field] = newval
    else:
        if newval is None:
            return case.get(path)
        case[path] = newval


applied, failed = 0, []
for cid, path, old, new in FIX:
    c = byid.get(cid)
    if not c:
        failed.append((cid, path, 'no such case'))
        continue
    cur = get_set(c, path)
    if cur is None or old not in cur:
        failed.append((cid, path, 'old text not found'))
        continue
    if cur.count(old) != 1:
        failed.append((cid, path, 'old text appears %d times' % cur.count(old)))
        continue
    get_set(c, path, cur.replace(old, new))
    applied += 1

if failed:
    print('NOT APPLIED:')
    for f in failed:
        print('  ', f)

if '--dry-run' in sys.argv:
    print('dry run: %d of %d would apply' % (applied, len(FIX)))
    sys.exit(1 if failed else 0)

s = s[:i] + json.dumps(C, ensure_ascii=False, separators=(',', ':')) + s[i + n:]
open(P, 'w', encoding='utf8').write(s)
print('voice fixes applied: %d of %d' % (applied, len(FIX)))
sys.exit(1 if failed else 0)
