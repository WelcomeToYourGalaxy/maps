# Round 15: new cases where outside lending is tied to documented harm

Follow /tmp/claude-0/-home-claude/e2ccd99e-7ec4-5ac8-a52a-ceacb7081fb1/scratchpad/w/BRIEF13.md (and the BRIEF.md and BRIEF2.md it points to) for the rules, the three tests and the case shape. Existing cases: /tmp/claude-0/-home-claude/e2ccd99e-7ec4-5ac8-a52a-ceacb7081fb1/scratchpad/w/cases.json (750; do not repeat an episode; use "extend" for an existing one).

Workplace pay or dismissal disputes alone are not cases. Product-supplier or buyer links alone are not cases (the outside party must have lent, invested, insured, or set the loan condition).

Find 20–30 new, well-documented cases. Priority order:
1. Projects financed by the IFC, MIGA, World Bank, ADB, AIIB, AfDB, EBRD, EIB, IDB or bilateral development financiers (FMO, DEG, Proparco, BII/CDC, Norfund, DFC/OPIC, JBIC/JICA, KfW) where harm on the ground is documented by the lender's own complaint office, a court, a UN body, or field research by credible NGOs or journalists. Good lead lists: Accountability Counsel's case list, Inclusive Development International (including IFC financial-intermediary cases), Bank Information Center, Human Rights Watch and Amnesty reports since 2015, Global Witness, Forest Peoples Programme, Coalition for Human Rights in Development ("Uncalculated Risks"), Recourse, Urgewald, Both ENDS.
2. Chinese state-financed projects (China Exim, CDB, Sinosure) with documented harm (AidData records, court rulings, credible reporting).
3. IMF or World Bank policy-loan conditions since 2015 that led to documented harm not yet on the map (price, tax, pay or job cuts; privatizations; required law changes), with the condition shown in the lender's own documents.

Check each candidate against cases.json by place, project and years before writing it. Output {"cases": [...], "extend": [...], "dropped": [{"candidate", "reason"}]} to /tmp/claude-0/-home-claude/e2ccd99e-7ec4-5ac8-a52a-ceacb7081fb1/scratchpad/w/r15_new.json. Validate with python (keys, valid lk/rg/levers/mechanism values, unique ids not in cases.json, coordinates on land at the named place). Reply with counts, one line per kept case, and anything contested.
