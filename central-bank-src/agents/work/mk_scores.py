#!/usr/bin/env python3
"""Emit agents/work/scores.json: the exposure score the page itself computes.

Why this exists. `check_scores.py` was written against a dump of RENDERED box
text and matched the panel heading "ULTERIOR INFLUENCE, ALL AROUND". That string
is gone -- the heading is now sentence case, and nothing in the repo has written
a boxes dump for several rounds, so the check silently reported "checked 0
country paragraphs" and passed. 189 country paragraphs quote a score; none of
them was being verified.

Rather than reimplement the scoring in Python and have the two drift, this runs
the page's OWN arithmetic: it lifts `const D` out of the built page and the pure
scoring block out of app.js, and evaluates them in Node. If app.js changes its
formula, this follows it automatically, which is the whole point.

The block lifted is app.js from `const uni =` to `function allScore`, which is
the self-contained scoring section. S is set to the layer defaults the paragraphs
were written against (alleged counted in, latest year).

    python3 agents/work/mk_scores.py
"""
import json, os, re, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CB   = os.path.dirname(os.path.dirname(HERE))
PAGE = os.path.join(CB, "dist", "central_bank_independence.html")
APP  = os.path.join(CB, "app.js")
OUT  = os.path.join(HERE, "scores.json")

def main():
    page = open(PAGE, encoding="utf-8").read()
    m = re.search(r"const D\s*=\s*\{", page)
    if not m:
        sys.exit("no `const D = {` in the built page")
    i = page.index("{", m.start()); depth = 0
    for j in range(i, len(page)):
        if page[j] == "{": depth += 1
        elif page[j] == "}":
            depth -= 1
            if depth == 0: end = j + 1; break
    else:
        sys.exit("unbalanced `const D`")
    data = page[i:end]

    app = open(APP, encoding="utf-8").read()
    a = app.index("const uni =")
    b = app.index("function allScore")
    b = app.index("\n", b)
    block = app[a:b]

    js = f"""
const D = {data};
const P = D.P, U = D.U, CUR = D.CUR;
const S = {{ alleged: true, latest: true, year: 2023 }};
const fmt = (v, n) => Number(v).toFixed(n);
{block}
// the percentile exactly as plainRank() computes it for the "all" layer:
// unrounded values, >=50% keeps the direction word, otherwise it flips.
const vals = [];
for (const p of Object.values(P)) {{ const a = allScore(p); if (a && a.v != null) vals.push(a.v); }}
const out = {{}};
for (const [iso, p] of Object.entries(P)) {{
  const a = allScore(p);
  if (!a) continue;
  const below = vals.filter((v) => v < a.v).length / vals.length;
  const above = vals.filter((v) => v > a.v).length / vals.length;
  const share = Math.round(100 * below);
  const dir = share >= 50 ? "more" : "less";
  const pct = share >= 50 ? share : Math.round(100 * above);
  out["p:" + iso] = {{ score: Math.round(a.v), groups: a.n,
                      pctl_dir: dir, pctl_share: pct, places: vals.length }};
}}
process.stdout.write(JSON.stringify(out));
"""
    with tempfile.TemporaryDirectory() as td:
        f = os.path.join(td, "s.js")
        open(f, "w", encoding="utf-8").write(js)
        r = subprocess.run(["node", f], capture_output=True, text=True)
    if r.returncode:
        sys.exit("node failed:\n" + r.stderr[-3000:])
    scores = json.loads(r.stdout)
    json.dump(scores, open(OUT, "w"), indent=1, sort_keys=True)
    print(f"wrote {len(scores)} scores to agents/work/scores.json")
    return 0

if __name__ == "__main__":
    sys.exit(main())
