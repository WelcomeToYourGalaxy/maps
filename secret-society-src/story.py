"""'About this map': the story of the map, told plainly for a reader who is new to all of it.
Present tense where things are still going on. Counts are filled in at build time."""


def story(data):
    cases = data['cases']
    n_cases = len(cases)
    n_orgs = len(data['entities'])
    n_pats = len(data['patterns'])
    n_now = sum(1 for c in cases if c.get('rel') == 'now')
    n_leg = sum(1 for c in cases if c.get('rel') == 'legacy')
    n_sus = sum(1 for c in cases if c.get('lik') == 'possible')
    n_cty = len({c['c'] for c in cases})
    by = {}
    for c in cases:
        by[c.get('inf')] = by.get(c.get('inf'), 0) + 1
    lab = {x['k']: x['label'].lower() for x in data['inf']}
    kinds = ', '.join('%s (%d)' % (lab[k], by[k]) for k in sorted(by, key=lambda k: -by[k]) if k in lab)
    p = []
    a = p.append
    a('<h2>About this map</h2>')
    a('<p>Every government has the part you can see: the elections, the ministers on television, the laws with their names on them. This map is about the part you usually cannot see — the moments when someone from outside gets a hand on the controls. It might be another country\'s spy service, a drug cartel, a company that wants a rule changed, a bank, a private lodge, a church with a plan for public office, or a club where ministers meet bankers off the record. And it is not only governments. The same thing happens to international bodies like Interpol and the World Health Organization, and to companies: a spy agency that secretly owns a firm, a cartel with a bank\'s branch staff on its payroll.</p>')
    a('<p>Most of the time none of this is visible. A minister does not announce that he answers to someone else, and a foreign government does not sign the cheques it sends. So how does anyone know? Usually by accident. In March 1981 Italian police, looking into a banker\'s fraud, opened a safe at a businessman\'s factory near Arezzo and found a list of 962 names. On it were the heads of all three of Italy\'s intelligence services, the chief of the armed forces, three serving ministers and 44 members of parliament. They all belonged to one private Masonic lodge, called P2. When the list was published two months later, the government fell. In 2023 a jury in New York found that Genaro García Luna, who had run Mexico\'s federal police and then its whole public security ministry, had taken bribes from the Sinaloa Cartel while he held those posts.</p>')
    a('<p>That is the kind of moment this map is built from: a list found in a raid, a court verdict, a parliament forcing an organisation to hand over its members, a government admitting what it had denied. Each diamond on the map is one of those moments — %d of them, in %d countries. By who was reaching in: %s.</p>' % (n_cases, n_cty, kinds))
    a('<h3>Proven, and only suspected</h3>')
    a('<p>Not everything here has been proven, and the map says which is which. Some cases ended in a conviction or an official finding. Others are charges not yet tested, or careful reporting with documents behind it. %d are only suspected: a named, credible source — an intelligence service\'s public report, a UN panel, an investigative newsroom — says it is happening, and nobody has shown it yet. Those diamonds are drawn faded. A few claims are widely repeated but fall apart when you look at the evidence; they are marked disputed, and their cards say why.</p>' % n_sus)
    a('<h3>Why it matters now</h3>')
    a('<p>It is tempting to treat this as history — the Cold War, the lodges of old Italy. Most of the map is not. %d cases are still going on: people still in office, cases still in court, bans still in force. Another %d are over but left something behind that still shapes life today — a law, a debt, a captured agency, a crime that went unpunished. The map opens on those two kinds. You can switch on the purely historical ones in the key.</p>' % (n_now, n_leg))
    a('<p>The method is worth knowing because it is simple, whoever uses it. You do not need to win an election if you can place your people where decisions are prepared: in the ministry that drafts the law, the police unit that decides what to investigate, the court that decides how a case ends, the regulator that decides what is safe. You do not need to break the law if you can host the conversation where the decision is really made. And you do not need to stay hidden forever, only long enough.</p>')
    a('<h3>How to read it</h3>')
    a('<p>Start with a country. Click it and you get its story: who is known to have reached inside, how, and what it means for the people who live there. Some countries have a long record; others have none yet, and for those the map gives its best guess, clearly marked as a guess.</p>')
    a('<p>Then use the filters in the key. You can show only one kind of infiltrator — only organised crime, say, or only foreign governments — or only what is happening now, or only what has been proven, or only the most severe cases, or only the ones whose reach is worldwide. The country colours change with the filters, so the map becomes a picture of where that particular kind of infiltration reaches.</p>')
    a('<p>Then open a pattern, in the box at the bottom left. There are %d. Each one follows an arrangement that keeps repeating — the same banks carrying money for intelligence services, the same kind of lodge turning up inside police forces, the same playbook used by different governments to recruit officials abroad. Opening a pattern colours the whole map by the part each country plays in it.</p>' % n_pats)
    a('<p>The country colours are a score from 0 to 10. Half of it is the record on this map, with recent, proven and severe cases counting most. Three-tenths is how many of the %d organisations and networks tracked here have a footing in the country. The last fifth is how easily officials there can be bent, from an independent index of organised crime. Method and sources, in the button beside this one, explains every part.</p>' % n_orgs)
    a('<h3>A word of caution</h3>')
    a('<p>Belonging to a lodge, a church, a club or a company is not a crime, and most members of every organisation here have done nothing wrong. A case is on the map because a court, an inquiry, a government or serious reporting found that someone, through particular people, reached into an office that was meant to serve the public — or, where the card says so plainly, because a credible source suspects it. Some findings were later overturned; the map keeps them, with what happened next.</p>')
    a('<p>And the record is lopsided. Countries with free courts and a nosy press find more, so they look worse. A country with no cases on this map may simply be one where nobody has been allowed to look.</p>')
    return '\n'.join(p)
