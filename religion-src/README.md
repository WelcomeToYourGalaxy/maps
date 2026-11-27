# religion.html — The Business of Belief

Source for `religion.html`, built on the engine of `school.html`.

- `story1.py`, `story2.py`, `story3.py` — chapter and slide text (`story3.py` is the current edition and reuses parts of the other two)
- `records.py`, `orgs.py`, `pages.py` — documented records, organisation directory, About and Method text
- `engine_patches.py` — changes made to the school.html engine
- `build.py` — assembles everything into `religion.html` (paths inside are those of the build machine and need adjusting)
- `pow_fetch.py`, `pow_process.py` — download OpenStreetMap places of worship through Overpass, remove schools and town halls, write the points that tippecanoe turns into `religion_pow.pmtiles`:
  `tippecanoe -o religion_pow.pmtiles -l pow -z9 -B9 --drop-densest-as-needed pow.geojsonl`
- `notes.md` — checked facts and their source links

Places of worship © OpenStreetMap contributors, ODbL.
