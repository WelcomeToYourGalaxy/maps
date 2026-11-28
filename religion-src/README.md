# religion.html — The Business of Belief

Source for `religion.html`, built on the engine of `school.html`.

- `story1.py` to `story9.py` — chapter and slide text (`story9.py` is the current edition and reuses slides from the earlier ones)
- `records.py`, `orgs.py`, `pages.py` — documented records, organisation directory, About and Method text
- `engine_patches.py` — changes made to the school.html engine
- `build.py` — assembles everything into `religion.html` (paths inside are those of the build machine and need adjusting)
- `pow_fetch.py`, `pow_process.py` — download OpenStreetMap places of worship through Overpass, remove schools and town halls, write the points that tippecanoe turns into `religion_pow.pmtiles`:
  `tippecanoe -o religion_pow.pmtiles -l pow -z9 -B9 --drop-densest-as-needed pow.geojsonl`
- `notes.md` — checked facts and their source links

Places of worship © OpenStreetMap contributors, ODbL.

`ba_dioceses.json` holds the count of entries per United States diocese in the BishopAccountability.org Database of Accused, read on 27 November 2026, with the seat city of each diocese located through OpenStreetMap Nominatim. The tiles are now built in two passes (zooms 0-6 without names, zooms 7-9 with names) and merged.
