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
| Spain | ES | [`es/`](es/) |

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

**Spain, added fifth, answered the remaining question and gave the defect a
third shape.** The first four countries are neighbours with similar
administrative traditions, so a reasonable objection was that the ontology
might be *western-European*-shaped rather than country-neutral. Spain is
southern European, joined the EU in a later enlargement, and organises its
state on a constitutional principle none of the others use — and it too
required no ontology, schema, folder, validation or generator change.

It also sharpened the `level` finding rather than repeating it. Spain is a
**State of Autonomies**: seventeen Comunidades Autónomas with devolved
competences of differing scope, which is neither a federation nor a unitary
state. Germany's Länder, Belgium's Regions and Spain's Comunidades Autónomas
are three constitutionally distinct things, and **the Atlas fails on all
three identically**. That is the strongest available evidence that the
defect sits in the `level` vocabulary rather than in any one country's
constitutional shape.

Three of five countries are now affected, and the cost is measurable: in
Spain it hides seventeen regional open data portals and half of a named
axis of the national digital strategy.

No sub-national level has been invented, because doing so for one country
is exactly the country-specific change the model exists to prevent. See
`de/de.md`, `be/be.md`, `fr/fr.md`, `es/es.md` and
`discovery/unresolved.md`.
