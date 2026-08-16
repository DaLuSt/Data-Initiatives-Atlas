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
| Germany | DE | [`de/`](de/) |
| Belgium | BE | [`be/`](be/) |
| France | FR | [`fr/`](fr/) |

Adding a new country means creating its sub-folder with an anchor entity and
an index — the ontology requires no other change (README
§"Country-Neutral Architecture").

## That claim has now been tested

Germany was added as the second country after the Netherlands layer was
complete. What it required, in full:

- a new `de/` sub-folder with an anchor entity and an index;
- German entities added to the **existing flat type folders**, tagged
  `country: DE`;
- `applies-in` → `DE` relationships added to the EU instruments that
  already carried `applies-in` → `NL`.

What it did **not** require: any change to `metadata/schema.json`,
`metadata/ontology.md`, `metadata/taxonomy.md`,
`metadata/relationship-types.md`, the folder structure, or any validation
rule. No entity type, relationship type, status or level was added. No
`DE-EU-*` entity was created.

One genuine limitation surfaced, and it is a limitation of the model rather
than of the country-neutral design: the `level` vocabulary has no term
between `national` and `local`, so Germany's sixteen Länder cannot be
represented.

**Belgium, added third, confirmed the limitation is general and made it
worse.** In Germany no term fits; in Belgium the term that would fit is
already taken, because `level: regional` means *supra-national* in this
Atlas — it is what [[EU]] carries. A Belgian Region cannot even borrow the
word. The cost is concrete: **OSLO**, one of Europe's most developed
public-sector semantic interoperability programmes, is a Flemish product
and is therefore not modelled at all.

**France, added fourth, isolated the defect.** France is unitary, and it is
the first country whose addition raised **no new ontology question at all** —
every entity fitted an existing type, level, status and relationship type,
and nothing needed a caveat about what the Atlas could not express.

That negative result is what makes the finding precise. With only Germany
and Belgium it was unclear whether the model was federal-lossy or simply
Netherlands-shaped. A second unitary state separates the two: the ontology
is sound for unitary states and lossy for federal ones, and the loss is
confined to the `level` vocabulary.

No sub-national level has been invented, because doing so for one country
is exactly the country-specific change the model exists to prevent. See
`de/de.md`, `be/be.md`, `fr/fr.md` and `discovery/unresolved.md`.
