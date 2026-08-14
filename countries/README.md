# countries/

One sub-folder per participating country, `countries/<iso2-lowercase>/`.
Each sub-folder holds exactly two things (`metadata/ontology.md` §3.1):

1. The `country` anchor entity itself, e.g. `nl/nl.md`.
2. A curated `index.md` of wikilinks into the flat type folders
   (`initiatives/`, `legislation/`, ...) for that country's key entities.

Country-scoped entities themselves (initiatives, legislation, organisations,
...) do **not** live here — they live in their type folder, tagged with
`country: <ISO2>`.

## Participating countries

| Country | Code | Folder |
|---|---|---|
| Netherlands | NL | [`nl/`](nl/) |

Adding a new country means creating its sub-folder with an anchor entity and
an index — the ontology requires no other change (README
§"Country-Neutral Architecture").
