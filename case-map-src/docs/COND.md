# Tag each case by the type of condition attached to the money

Input: cond_in.json (946 cases: id, title, kind, lk lender keys, lenders, conditions text, levers, lever_why). The conditions text and lever_why are already sourced; you only classify what they say. Do not add anything they don't say.

For each case, list the condition types the text documents as attached to the money (a loan, grant, guarantee, investment deal or debt deal). A condition is something the funder required, or the deal's terms required, as the price of the money: a policy change, a law, a sale, a repayment term, a project rule.

Types (use these keys):
- priv: sell, lease or hand over a public firm, service or resource to companies
- prices: raise prices or remove subsidies (fuel, food, power, water tariffs)
- tax: raise or add taxes (VAT, excise, tolls)
- cuts: cut public spending, public pay or public jobs; budget targets
- deval: devalue or float the currency
- trade: cut tariffs, open imports, push exports or cash crops
- labour: change labour law, wage rules, unions
- land: change land or property law, title or make land available for the project
- fees: charge users for health care, schooling or other services
- invest: open the economy to foreign investors, investor protection, mining or investment codes
- law: another required change in the law or institutions, not covered above (say what in "why")
- repay: repayment terms that bind the borrower: collateral, resource-backed repayment, escrow accounts, priority repayment, cross-default
- tied: the money must be spent with the funder's own firms or goods
- safeguard: the lender's own project rules: resettlement plan, compensation, consultation, environmental plan (only if the text says such terms were attached)
- none: the text says there was no condition, or the money was the company's own

Rules:
- Only tag what the text supports. If a case has an outside lender but the text does not say what was required, give "ct": [] and "need_research": true.
- Cases with only foreign-company money and no condition stated: "ct": ["none"].
- For each tag give a short quote (under 20 words) from the case text in "why", keyed by type.

Output cond_out.json: {"<id>": {"ct": [...], "why": {"<type>": "quote"}, "need_research": bool}}. Every id. Validate with python (keys from the list only). Reply with counts per type and the number needing research.
