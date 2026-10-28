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
    a('<p>This map shows where people working for an outside group hold jobs inside governments, international bodies and companies, or where an outside group pays the people who do. The outside group can be another country\'s government or spy service, a drug cartel or mafia, a company, a bank, a lodge, a church, a policy club, an armed movement or a lender. The international bodies include Interpol, the World Health Organization, FIFA and the European Parliament.</p>')
    a('<p>Most of these arrangements are kept secret, so they become known in a few ways. Police find a membership list or a ledger in a raid. A court convicts someone and the evidence is read out. A parliament orders an organisation to hand over its members. A government admits what it had denied. A newsroom obtains leaked documents. In 1981 Italian police searching a businessman\'s factory near Arezzo found a list of 962 members of a Masonic lodge called P2. It included the heads of Italy\'s three intelligence services, three serving ministers and 44 members of parliament. In 2023 a New York jury convicted Genaro García Luna, who had run Mexico\'s federal police and then its public security ministry, of taking bribes from the Sinaloa Cartel while he held those posts.</p>')
    a('<p>Each diamond on the map is one such case. There are %d, in %d countries. By who was paying or placing people: %s.</p>' % (n_cases, n_cty, kinds))
    a('<h3>Proven and suspected</h3>')
    a('<p>Each case card says how sure we are. Proven means a court verdict, an official inquiry, a government designation, a settlement or an admission. Probable means someone has been charged, an official investigation is open, or reporting is backed by documents. Suspected means a named, credible source says it is happening and nobody has shown it yet; %d cases are in this group, and their diamonds are drawn faded. Disputed means the claim was overturned in court or is widely repeated without evidence; the card says what the evidence shows.</p>' % n_sus)
    a('<h3>What is current</h3>')
    a('<p>%d cases are still going on: the people are still in office, the trial is still running, or the ban is still in force. Another %d have ended but left something in place, such as a law, a debt, an agency run by the same people, or a crime nobody was punished for. The map opens on these two groups. Purely historical cases can be switched on in the key.</p>' % (n_now, n_leg))
    a('<h3>How to use it</h3>')
    a('<p>Click a country to read what is known about it, what it means for the people who live there, and the full list of its cases. Twenty-odd countries have no case yet; their cards give a best guess and say so.</p>')
    a('<p>Use the filters in the key to show one kind of outside group, only current cases, only proven cases, only the most serious ones, or only those that cross borders. The list of patterns in the bottom-left box changes with the filters.</p>')
    a('<p>Open a pattern to see one arrangement across many countries, such as cartels paying police commanders, or governments placing staff inside foreign phone companies. There are %d patterns. Opening one colours each country by its part in it.</p>' % n_pats)
    a('<p>The country colours come from the Global Organized Crime Index, which scores every country the same way: how often officials act for outside interests, and how weak the courts, police and watchdogs are. The colours show how much room an outside group would have. They are not a count of the cases. The second option in the menu shades countries by the cases instead, and follows the filters.</p>')
    a('<h3>Cautions</h3>')
    a('<p>Belonging to a lodge, a church, a club or a company is legal, and most members of every organisation here have done nothing wrong. A case is on the map because a court, an inquiry, a government or documented reporting found that particular people used an office for an outside group, or, where the card says so, because a credible source suspects it. Some findings were later overturned, and the card says when.</p>')
    a('<p>Countries with independent courts and a free press uncover more cases, so they can look worse than countries where nobody is allowed to investigate. A country with no cases may be one where nobody has looked.</p>')
    return '\n'.join(p)
