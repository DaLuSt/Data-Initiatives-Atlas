---
id: FR
type: country
name: France
alternative_names:
  - French Republic
  - République française
description: >
  Country anchor entity for France, the fourth national scope covered by
  the Data Initiatives Atlas. Used as the target of `country` fields and
  `applies-in` relationships for French-scoped entities.

level: national
country: FR
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains: []
organisations: []
related_entities: []
relationships: []

sources:
  - title: "FR — France (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:FR"
    publisher: "International Organization for Standardization (ISO)"
  - title: "LOI n° 2016-1321 du 7 octobre 2016 pour une République numérique"
    url: "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000033202746"
    publisher: "Légifrance (Direction de l'information légale et administrative)"
  - title: "La direction interministérielle du numérique (DINUM)"
    url: "https://www.numerique.gouv.fr/numerique-etat/dinum/"
    publisher: "DINUM — numerique.gouv.fr"
---

# France

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

France (ISO 3166-1 alpha-2: `FR`) is the **fourth country** populated in
the Data Initiatives Atlas, after [[NL]], [[DE]] and [[BE]].

French entities live in the same flat type folders as every other country's,
tagged `country: FR`. EU instruments that apply in France reference it via
an `applies-in` relationship — the same single entity that already carries
`applies-in` to three other countries.

## Why France, specifically

`progress/backlog.md` asked for this one by name:

> *A fourth country — a **unitary** one. All three tests so far have been
> the Netherlands plus two federal states. A second unitary country would
> show whether anything else in the model is Netherlands-shaped, which the
> two federal cases could not isolate.*

Germany and Belgium both strained the model in the same place — the missing
sub-national `level` — and that shared failure made it hard to tell whether
anything *else* was wrong. A second unitary state separates the two
questions.

**Result: nothing else broke.** France is the first country added that
raised **no new ontology question at all**. Every entity fits an existing
type, level, status and relationship type; nothing needed a caveat about
what the Atlas could not express.

That is a genuinely informative negative. Combined with the German and
Belgian batches it isolates the defect: the Atlas's ontology is sound for
unitary states and lossy for federal ones, and the loss is confined to the
`level` vocabulary rather than being a general country-shape problem.

## France is *more* centralised than the Netherlands, not less

The obvious worry with a second unitary country is that it would just
re-confirm the first. It does not, because France sits further along the
same axis:

- [[FR-DINUM]] is a service of the **Prime Minister**, setting the state's
  digital strategy across all ministries.
- [[FR-ETALAB]] is a **department inside DINUM**, not a separate body — so
  France's open-data function is one level *inside* its digital-government
  function.
- [[FR-RGI]] is a **legal obligation** under an ordonnance, not a
  comply-or-explain list like [[NL-PAS-TOE-OF-LEG-UIT]].

So the four countries now span a real range — France (centralised, binding),
the Netherlands (central, comply-or-explain), Belgium (federal, coordinated
by agreement), Germany (federal, Bund-Länder council) — and the model
carried all four without modification.

## The one thing France does that no other country here does

France implemented the GDPR by **amending a 1978 act rather than passing a
new one**, and the sources record that as a deliberate, symbolic choice.
See [[FR-LIL]]. The Atlas already had trouble with an amending act in
Germany ([[DE-NIS2UMSUCG]] → [[DE-BSIG]]); France shows the pattern is not
a German quirk, and — because the amended act keeps its own identity —
shows the case the Atlas models *well*.

## Relationships

See `countries/fr/index.md` for the curated index of French entities.

## Sources

Listed in frontmatter, including the ISO Online Browsing Platform entry —
the same citation [[DE]] and [[BE]] carry, and one the [[NL]] anchor still
lacks because Batch 0 composed its URLs from background knowledge.

**No `accessed` date and no `last_verified`** — nothing about this entity
has been checked against a source.
