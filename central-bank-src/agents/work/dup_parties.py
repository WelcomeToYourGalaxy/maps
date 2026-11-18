#!/usr/bin/env python3
"""Find two spellings of one party anywhere on the map.

WHY THIS EXISTS. merge_links.py folds an incoming entity name before comparing
it, but it compares against what is already on the map FOR THAT CENTRAL BANK.
A firm arriving under a new spelling, for a country that holds no record of it,
is not a duplicate by that test -- so the script passes it and the map gains a
second diamond for one firm. Round 49 carried the World Bank's reserve-advisory
programme under five names, a party with 24 ties rendering as five parties.
Round 59 took three more spellings the same way: Oberthur Fiduciaire S.A.S.
beside Oberthur Fiduciaire, G+D Currency Development GmbH beside
Giesecke+Devrient, and two further spellings of Papierfabrik Louisenthal.

Until now the only check was grepping networks.json by hand for a distinctive
word before adding a party. This does that comparison for the whole map at once.

It reads the node list out of a BUILT page, not out of one data file, because
NET.nodes is much larger than networks.json's link entities: it also holds every
party from corruption.json cases and revolving-door records, via parties.json.
Deriving the live set from one data file is what deleted 1,218 writeups at
round 49.

    python3 agents/work/dup_parties.py dist/central_bank_independence.html

Exits 1 if it finds anything, so it can gate a push. Three tests, loosest last:

  fold      identical under merge_links.py's own fold (accents, case,
            punctuation and legal-form filler removed) AND in the same word
            order -- always a duplicate
  reorder   the same words in another order. That fold sorts the words, so a
            permutation folds alike: this was reported as certain until round
            62, when it put "City National Bank" beside "National City Bank"
            and "Canada" beside "Bank of Canada". Read these
  subset    one name's folded words are a subset of the other's and the
            shorter has at least two words -- "oberthur fiduciaire" inside
            "oberthur fiduciaire sas"; usually a duplicate
  token     the two share a distinctive token (a word of 5+ characters that
            appears in fewer than four parties on the whole map, and is not a
            place name or a generic institutional word) -- worth a look, often
            a parent and a subsidiary that are genuinely separate. People are
            left out of this test: two people share a surname without being
            one party, and a misspelled name is caught by the two tests above.

A parent and its subsidiary are NOT a duplicate: the map deliberately keeps
World Bank Treasury separate from the RAMP programme, because one record is a
Treasury cooperation agreement that does not mention RAMP. So read the groups
rather than folding them automatically.
"""
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict

FILLER = {'the', 'of', 'and', 'bank', 'banknote', 'printing', 'works', 'ltd', 'limited',
          'plc', 'sa', 'ag', 'nv', 'inc', 'llc', 'gmbh', 'co', 'company', 'group',
          'holding', 'holdings', 'doo', 'srl', 'spa', 'as', 'ab', 'oy', 'kk', 'pte',
          'sas', 'sarl', 'aps', 'bv', 'dd', 'ad', 'jsc', 'ojsc', 'pjsc', 'llp'}


def words(s):
    s = unicodedata.normalize('NFKD', s or '').encode('ascii', 'ignore').decode().lower()
    return [w for w in re.findall(r'[a-z0-9]+', s) if w not in FILLER]


def fold(s):
    return ' '.join(sorted(words(s)))


def ordered_fold(s):
    """fold() without the sort, to tell a permutation from a filler difference."""
    return ' '.join(words(s))


def fold_de(s):
    """The same fold with German transliterations collapsed.

    NFKD plus an ASCII strip turns 'ü' into 'u', never into 'ue', so the two
    ordinary spellings of a German name do not collide: round 61 found the map
    drawing Orell Fuessli, Orell Fussli and Orell Fuessli Security Printing Ltd
    as three parties for one banknote printer, four ties between them. This is a
    SEPARATE test rather than a change to fold(), because collapsing 'ue' into
    'u' in general would also merge genuinely different names.
    """
    out = []
    for w in words(s):
        for a, b in (('ue', 'u'), ('oe', 'o'), ('ae', 'a')):
            w = w.replace(a, b)
        out.append(w)
    return ' '.join(sorted(out))


def fold_ar(s):
    """The same fold with common Arabic-to-English romanisation variants collapsed.

    Round 73 found the map drawing Yemen's former president as TWO person nodes --
    'Abd-Rabbu Mansour Hadi' and 'Abd Rabbuh Mansur Hadi', one tie each, from two
    events whose sources romanised the name differently. Neither the plain fold nor
    fold_de catches it: 'ou' against 'u' and a trailing 'h' are not accent
    differences, and step 3's distinctive-token test SKIPS person nodes, so nothing
    looked. A third spelling, 'Abdrabbuh Mansur Hadi', sits in corruption.json.

    SEPARATE test for the same reason fold_de is separate: collapsing 'ou' into 'u'
    everywhere would merge genuinely different names, and stripping a trailing 'h'
    certainly would. This is advisory output a human reads, like the rest, so a false
    pair here costs a glance and a missed duplicate costs a wrong node on the map.
    """
    out = []
    for w in words(s):
        for x, y in (('ou', 'u'), ('oo', 'u'), ('ee', 'i'), ('aa', 'a')):
            w = w.replace(x, y)
        if len(w) > 3 and w.endswith('h'):
            w = w[:-1]
        # A doubled consonant is the commonest romanisation difference of all and it is
        # on this map twice over: Mohammed against Mohamed, Hammam against Hamam, which
        # are the two spellings of the Yemeni central bank head in the sources. Collapse
        # runs of the same letter rather than a fixed list, so no pair is special-cased.
        w = re.sub(r'([bcdfghjklmnpqrstvwxyz])\1+', r'\1', w)
        out.append(w)
    return ' '.join(sorted(out))


# Generic words that carry no identity on their own. A shared one says only that
# two bodies are both public, or both in the same country -- "Government of
# Zimbabwe" and "Ministry of Finance of Zimbabwe" are two bodies, not two
# spellings. Test 3 counted a word distinctive when it appeared in two or three
# parties map-wide, and a country that holds two or three parties made its own
# name distinctive by that measure: the test returned 579 groups, which is more
# than anyone reads, and real duplicates (uniBank beside uniBank Ghana) sat in
# the middle of them. Geography is taken from the map's own data rather than a
# hand list, so it stays right as places and parties are added.
GENERIC = {
    'government', 'ministry', 'ministerio', 'ministere', 'national', 'nacional',
    'nationale', 'state', 'federal', 'republic', 'republica', 'republique',
    'central', 'office', 'oficina', 'bureau', 'department', 'authority',
    'agency', 'commission', 'commissioner', 'committee', 'council', 'conseil',
    'consejo', 'board', 'court', 'tribunal', 'supreme', 'parliament',
    'parlement', 'assembly', 'congress', 'senate', 'president', 'presidency',
    'prime', 'minister', 'cabinet', 'secretariat', 'general', 'generale',
    'auditor', 'audit', 'accounts', 'accounting', 'finance', 'financial',
    'financiera', 'treasury', 'tesoro', 'revenue', 'customs', 'public',
    'publico', 'publique', 'service', 'services', 'institute', 'instituto',
    'institution', 'fund', 'fondo', 'fonds', 'pension', 'pensions', 'provident',
    'superannuation', 'insurance', 'assurance', 'assicurazioni', 'seguros',
    'savings', 'risparmio', 'investment', 'investments', 'capital', 'trust',
    'exchange', 'stock', 'securities', 'valores', 'market', 'development',
    'economic', 'economics', 'economy', 'monetary', 'money', 'currency',
    'reserve', 'reserves', 'commercial', 'international', 'union', 'unity',
    'association', 'federation', 'chamber', 'corporation', 'enterprise',
    'management', 'partnership', 'programme', 'program', 'project', 'telephone',
    'communications', 'media', 'mediaworks', 'vault', 'vaults', 'domestic',
    'head', 'main', 'branch', 'first', 'interstate', 'people', 'peoples',
    'popular', 'certified', 'chartered', 'accountants', 'advisors', 'advisory',
    'partners', 'consulting', 'anticorruption', 'oversight', 'ombudsman',
    'prosecutor', 'attorney', 'justice', 'police', 'enforcement', 'control',
    'supervision', 'supervisory', 'regulatory', 'regulation', 'deposit',
    'insurance', 'guarantee', 'housing', 'agricultural', 'agriculture',
    'industrial', 'industry', 'trade', 'trading', 'import', 'export',
    'petroleum', 'mining', 'energy', 'power', 'water', 'transport', 'post',
    'postal', 'university', 'college', 'school', 'foundation', 'fondazione',
    'fondation', 'society', 'cooperative', 'cassa', 'caisse', 'banca', 'banco',
    'banque', 'bancaria', 'bancario', 'sparkasse', 'raiffeisen',
    # non-English corporate forms and sector words that survive the FILLER list
    'sociedad', 'societa', 'societe', 'sociedade', 'cooperativa', 'credito',
    'credit', 'kredit', 'genossenschaft', 'aktiengesellschaft', 'anonima',
    'anonyme', 'responsabilidad', 'limitada', 'mutua', 'mutual', 'asociados',
    'asociacion', 'participacoes', 'beteiligungs', 'verwaltung',
    # nationality and regional adjectives: shared nationality is not identity
    'swiss', 'suisse', 'schweizerische', 'french', 'francaise', 'german',
    'deutsche', 'italian', 'italiana', 'spanish', 'espanola', 'portuguese',
    'portuguesa', 'dutch', 'nederlandsche', 'belgian', 'austrian',
    'oesterreichische', 'danish', 'danmarks', 'swedish', 'sveriges',
    'norwegian', 'norges', 'finnish', 'suomen', 'polish', 'polski',
    'narodowy', 'czech', 'slovak', 'slovenska', 'hungarian', 'magyar',
    'romanian', 'romana', 'bulgarian', 'balgarska', 'greek', 'turkish',
    'turkiye', 'russian', 'rossii', 'ukrainian', 'lithuanian', 'latvian',
    'estonian', 'canadian', 'australian', 'american', 'british', 'english',
    'scottish', 'irish', 'japanese', 'nippon', 'chinese', 'korean', 'indian',
    'pakistani', 'bangladeshi', 'indonesian', 'malaysian', 'filipino',
    'philippine', 'thai', 'vietnamese', 'cambodian', 'nigerian', 'ghanaian',
    'kenyan', 'tanzanian', 'ugandan', 'zambian', 'zimbabwean', 'sudanese',
    'egyptian', 'moroccan', 'tunisian', 'algerian', 'lebanese', 'jordanian',
    'saudi', 'emirati', 'qatari', 'kuwaiti', 'bahraini', 'omani', 'yemeni',
    'iraqi', 'iranian', 'israeli', 'brazilian', 'argentine', 'argentina',
    'chilean', 'peruvian', 'colombian', 'mexican', 'cuban', 'jamaican',
    'sammarinese', 'maltese', 'cypriot', 'icelandic', 'islandsbanki',
    # bare qualifiers: two unrelated bodies share these constantly
    'royal', 'rural', 'urban', 'special', 'specialised', 'specialized',
    'southern', 'northern', 'eastern', 'western', 'north', 'south', 'east',
    'west', 'upper', 'lower', 'alta', 'bassa', 'grand', 'petit', 'nuevo',
    'nueva', 'santa', 'santo', 'saint', 'subsidiary', 'subsidiaries',
    'aggregate', 'shareholders', 'shareholder', 'holders', 'other', 'others',
    'private', 'privada', 'global', 'world', 'universal', 'unified',
    'metropolitan', 'provincial', 'regional', 'district', 'county', 'city',
    'municipal', 'village', 'community', 'secretary', 'secretario',
}


def stoplist(D):
    """GENERIC plus every place and city name the map itself carries."""
    stop = set(GENERIC)
    for v in D.get('P', {}).values():
        if isinstance(v, dict) and v.get('n'):
            stop.update(words(v['n']))
    for n in D.get('NET', {}).get('nodes', []):
        if n.get('city'):
            stop.update(words(n['city']))
    return stop


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'dist/central_bank_independence.html'
    m = re.search(r'const D = (\{.*?\});\n', open(path, encoding='utf-8').read(), re.S)
    if not m:
        print('could not find const D in ' + path)
        return 2
    D = json.loads(m.group(1))
    nodes = D['NET']['nodes']
    ties = Counter(l['n'] for l in D['NET']['links'] if l.get('n') is not None)
    ties.update(l['tn'] for l in D['NET']['links'] if l.get('tn') is not None)
    name = {i: n['name'] for i, n in enumerate(nodes)}
    ws = {i: set(words(n['name'])) for i, n in enumerate(nodes)}

    def show(label, groups):
        if not groups:
            return 0
        print('\n' + label)
        for g in groups:
            print('  ' + ' | '.join('%s (%d ties)' % (name[i], ties.get(i, 0)) for i in g))
        return len(groups)

    # 1. identical under the fold, split by whether the word order also matches
    byfold = defaultdict(list)
    for i, n in enumerate(nodes):
        byfold[fold(n['name'])].append(i)
    same, reordered = [], []
    for k, v in byfold.items():
        if not k or len(v) < 2:
            continue
        # fold() sorts the words, so a permutation folds the same. "City
        # National Bank" and "National City Bank" are two banks; "Bank of
        # Canada" and "Canada" differ only by stripped filler and are one.
        # A name that reduces to ONE substantive word collides promiscuously,
        # because the filler list strips the rest: "Crane Bank" (Uganda) and
        # "Crane AB" (the banknote printer) both reduce to "crane", and so do
        # "Canada" and "Bank of Canada", "First Bank" and "First Bank SA",
        # "Bank of the Commonwealth" and "Commonwealth Bank Limited". Every
        # one of those is two parties. Two or more words surviving the fold is
        # what makes a match certain.
        if len(k.split()) >= 2 and len({ordered_fold(name[i]) for i in v}) == 1:
            same.append(sorted(v))
        else:
            reordered.append(sorted(v))

    # 1b. identical once German transliterations are collapsed
    byde = defaultdict(list)
    for i, n in enumerate(nodes):
        byde[fold_de(n['name'])].append(i)
    seen0 = {frozenset(g) for g in same} | {frozenset(g) for g in reordered}
    same_de = [sorted(v) for k, v in byde.items()
               if k and len(v) > 1 and frozenset(v) not in seen0]

    # 1c. identical once Arabic romanisation variants are collapsed (round 73)
    byar = defaultdict(list)
    for i, n in enumerate(nodes):
        byar[fold_ar(n['name'])].append(i)
    seen0b = seen0 | {frozenset(g) for g in same_de}
    same_ar = [sorted(v) for k, v in byar.items()
               if k and len(v) > 1 and frozenset(v) not in seen0b]

    # 2. one folded word set inside another
    seen = ({frozenset(g) for g in same} | {frozenset(g) for g in reordered}
            | {frozenset(g) for g in same_de} | {frozenset(g) for g in same_ar})
    subset = []
    items = [(i, ws[i]) for i in range(len(nodes)) if len(ws[i]) >= 2]
    for a, wa in items:
        for b, wb in items:
            if a < b and wa != wb and (wa <= wb or wb <= wa):
                if frozenset((a, b)) not in seen:
                    subset.append((a, b))
                    seen.add(frozenset((a, b)))

    # 3. a distinctive token shared by two parties
    stop = stoplist(D)
    tok = defaultdict(set)
    for i in range(len(nodes)):
        if nodes[i].get('type') == 'person':
            continue
        for w in ws[i]:
            if len(w) >= 5 and w not in stop:
                tok[w].add(i)
    token = []
    for w, ids in sorted(tok.items()):
        if 2 <= len(ids) <= 3:
            ids = sorted(ids)
            for a in range(len(ids)):
                for b in range(a + 1, len(ids)):
                    k = frozenset((ids[a], ids[b]))
                    if k not in seen:
                        token.append((ids[a], ids[b]))
                        seen.add(k)

    n = 0
    n += show('Identical under the fold, same word order -- one party, two names:', same)
    n += show('Fold alike but NOT certain -- read these. Either the words are in '
              'another order ("City National Bank" is not "National City Bank"), '
              'or the name reduces to one word ("Crane Bank" is not "Crane AB"):',
              reordered)
    n += show('Identical once German ue/oe/ae are collapsed -- one party, two spellings:', same_de)
    n += show('Identical once Arabic romanisation is collapsed -- one party, two spellings:',
              same_ar)
    n += show('One name inside the other -- almost always one party:', subset)
    n += show('Share a distinctive word -- read these, a parent and a subsidiary are not a duplicate:', token)
    print('\n%d parties, %d groups to read' % (len(nodes), n))
    if n:
        print('Fold a duplicate into the name already carrying the most ties, keep the')
        print("source's own wording in name_as_stated, and migrate any writeup key the")
        print('rename orphans rather than deleting it.')
    return 1 if n else 0


if __name__ == '__main__':
    sys.exit(main())
