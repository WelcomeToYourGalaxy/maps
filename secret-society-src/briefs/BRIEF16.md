# Brief 16: high-throughput rounds, and the rebalance they have to serve

> **SUPERSEDED IN PART, 16 November 2026.** The rebalance this brief was written to
> serve is closed: `bk: company` is at 29.5 per cent against an estimated 30, and a
> company-shaped round now makes the map's shape *worse*. The throughput method below —
> one agent, one enumeration, mechanical validation first, batch source-checking, set
> `verified` as you write — is unchanged and still the method. **What has changed is the
> target the method is pointed at.** Read "THE STANDING GOAL" at the head of
> `HANDOFF.md` before briefing anyone: the cells to work are now a crime group or a
> political, religious or armed movement reaching a police force, army, intelligence
> service, court or cabinet ministry. Ignore point 1 below and the per-category table
> under "The rebalance, as numbers", both of which describe a gap that no longer exists.


Set on 14 November 2026, on two owner decisions:

1. **Prefer an accurately rounded selection over "biggest first."** BRIEF5 tells research agents to prioritise the largest and most consequential cases. That instruction did its job and has now bent the map: measured against `data/field_estimate.json`, which is the map's own estimate of the worldwide field and is deliberately not scaled from its sample, heads of state are over-represented elevenfold and international bodies eightfold, while infiltration of companies sits at 12 per cent of cases against an estimated 30. From now on, the shape of the selection matters as much as the size of the case. Keep adding big cases when they come; stop *steering* toward them.
2. **Keep the weighting toward the present.** 848 of 1,680 cases are from the 2020s and 77 per cent are post-2010. That is wanted: the map is a snapshot of where things stand now. Do not spend rounds on historical depth unless a historical case explains something still in force.

## The rebalance, as numbers

Rebalancing is by **addition only**. Nothing is removed to improve a ratio - that would be filtering the data, which the owner has ruled out, and removed cases go to `removed_records.json` with a reason or not at all. So a negative number below does not mean "delete"; it means "this category is full, and adding more makes the skew worse."

To reach the field estimate by addition, as of 14 November 2026:

| | map holds | share | estimate | add to reach it |
|---|---|---|---|---|
| Body reached is a **company** (state-owned included) | 209 | 12.4% | 30% | **+421** |
| Infiltrator is a **company or industry** | 531 | 31.6% | 45% | **+409** |
| Infiltrator is a **crime group** | 415 | 24.7% | 30% | +127 |
| Infiltrator is a **political or armed movement** | 103 | 6.1% | 10% | +72 |
| Body reached is a **court** | 79 | 4.7% | 5% | +5 |
| Infiltrator is a **foreign state or service** | 396 | 23.6% | 10% | full |
| Body reached is a **head of state or government** | 183 | 10.9% | 1% | full |
| Body reached is an **international body** | 72 | 4.3% | 0.5% | full |
| Body reached is a **finance ministry, central or state bank** | 101 | 6.0% | 2% | full |
| Infiltrator is a **lodge** | 76 | 4.5% | 1% | full |

The two binding numbers overlap almost entirely: a company paying the officers of a state-owned enterprise is `inf: corp, tgt: company`. So **roughly 420 new cases, nearly all of one shape - an outside party reaching inside a company - would land the map close to its own estimate of the field.** That is the target. Everything else is close enough.

At the historic rate of about 26 cases a round that is sixteen rounds. The rest of this brief is how to make it six.

## Where 420 company cases already exist, adjudicated and named

The throughput problem is not search. It is that a round spent one-case-at-a-time pays four to six searches per case and then a source check that, in the November rounds, corrected more than half of them. **Work source-dense enumerations instead: documents that carry twenty to forty named, adjudicated cases each, so the per-case search cost falls to under one and the source check is against a single document.**

Seams, richest first, all of them company-shaped:

- **The FCPA corpus by year.** Under ruling 12 a state-owned enterprise reached through its own officers is `tgt: company`, which is what most FCPA actions are. The map already matches 27 of the 30 largest sanction groups and 28 of 28 in the 2024 appendix, but the full corpus is several hundred actions. Work it backwards a year at a time. Each year's list is one page; each action has a published complaint or information naming the company, the country, the body and the decision.
- **Multilateral debarment lists** - World Bank, African Development Bank, Asian Development Bank, EBRD, Inter-American Development Bank. Ruling 5 says a debarment after the lender's own sanctions process is an adjudication, not an assertion, so it stays `established`. Hundreds of entries. Yield is mixed because many are collusion rather than an official reached: read the sanctions board decision, not the list row.
- **National leniency and settlement registers already benchmarked but not exhausted**: Brazil's CGU (33 of 37 matched), France's CJIPs (24 of 30), the Dutch hoge transacties, Switzerland's article 102 orders. Where a register is matched, its *earlier years* usually are not.
- **Port and terminal insider recruitment**: Belgian, Dutch and Spanish police reporting, and the Europol-style threat assessments. These give crime-into-company cases, which the map is also short of.
- **Bank insiders**: FATF and national FIU typology reports name the mechanism and sometimes the institution; Swiss, Singaporean and Baltic enforcement names the bank.
- **Procurement blacklists and audit-office reports** in countries whose insiders score severe, which is also where the thin-record hypothesis says to look.

## How to run the round

The limits, measured, and they are shared across every agent in the turn:

- **WebSearch: about 200 calls per turn.** Sixteen agents at once exhausted it within minutes and several saved almost nothing. Run four to six at a time and ration them explicitly: tell each agent its search budget in the prompt.
- **WebFetch: an hourly cap, also shared.** Five checkers at once reached it. It resets on the hour. A source-dense round is fetch-heavy rather than search-heavy, so stage the fetches: harvest the enumeration first, then fetch its underlying documents in batches.
- **Give every agent its own scratch folder.** Two agents once overwrote each other's `build.py` in a shared one.

The sequence that fits those limits:

1. **One agent, one enumeration.** Give each agent a single document or register - "the FCPA actions of 2019", "the World Bank sanctions board decisions of 2023-2024" - and a search ration of ten. Its job is to produce candidate records from that document, not to go looking.
2. **Shape the brief to the rebalance.** Tell the agent the target: an outside party reaching inside a company, including a state-owned one. Records that come out `tgt: gov` are still kept, but the agent should not go hunting for them.
3. **Mechanical validation before any reading.** Country names against `briefs/countries.txt`, org keys against `orgs.json`, duplicates by country plus title-word overlap against both `cases.json` and `removed_records.json`. This is a script, not a judgement, and it catches most of what used to be caught by hand.
4. **One agent applies BRIEF11 to the whole batch** - the test, not the sources - and reports keeps and drops with reasons.
5. **Source-check in batches against the one document**, not case by case against the web. This is where the old rounds lost their time: a batch drawn from a single enumeration can be checked in one or two fetches for the whole batch, because the document says what it says.
6. **Set `verified` on every record as it is written.** See the outcome-maintenance section of HANDOFF.md: an unstamped record is indistinguishable from an unchecked one, and the next round pays for it twice.

A round run this way should land 60 to 80 cases rather than 26, which puts the rebalance at six rounds rather than sixteen.

## What not to do for throughput

- **Do not loosen the test to raise the count.** BRIEF11 is what keeps the map defensible, and 23 of 253 candidates were dropped in one round by a reviewer applying it. A faster round with a looser test is not a faster round.
- **Do not add cases without the `inside` line.** It is the one sentence that makes a record usable to a reader, and writing it later never happens.
- **Do not let a big fan-out skip the duplicate check.** The map has at least one duplicate pair already (the two Trafigura records), which is cheap to create and expensive to find.
