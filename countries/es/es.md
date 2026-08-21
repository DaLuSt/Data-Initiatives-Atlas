---
id: ES
type: country
name: Spain
alternative_names:
  - Kingdom of Spain
  - España
  - Reino de España
description: >
  Country anchor entity for Spain, the fifth national scope covered by the
  Data Initiatives Atlas and the first outside the founding-six /
  Benelux-DACH group. Used as the target of `country` fields and
  `applies-in` relationships for Spanish-scoped entities.

level: national
country: ES
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-20"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - EU
relationships:
  - type: part-of
    target: EU
    source: fact
    evidence: "Spain is one of the 27 member states of the European Union, having acceded on 1 January 1986; the Union's own list of EU countries records its accession date together with its Schengen and euro status (european-union.europa.eu 'EU countries'). Anchor edge under metadata/relationship-types.md §2.3: it records EU membership and asserts no more than that. Added in the European country batch so that all fifty anchors carry the same membership edge."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "EU countries"
    url: "https://european-union.europa.eu/principles-countries-history/eu-countries_en"
    publisher: "European Union"
    accessed: "2026-08-20"
  - title: "ES — Spain (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:ES"
    publisher: "International Organization for Standardization (ISO)"
    accessed: "2026-08-20"
  - title: "España Digital 2026"
    url: "https://digital.gob.es/ministerio/programas/programas-avance-digital/espana-digital-2026"
    publisher: "Ministerio para la Transformación Digital y de la Función Pública"
    accessed: "2026-08-20"
  - title: "Real Decreto 1118/2024, de 5 de noviembre, por el que se aprueba el Estatuto de la Agencia Estatal de Administración Digital"
    url: "https://www.boe.es/buscar/doc.php?id=BOE-A-2024-22929"
    publisher: "Boletín Oficial del Estado (BOE)"
    accessed: "2026-08-20"
---

# Spain

> **Verified 2026-08-20.** Every cited source was read and confirmed to
> support what this entity says, including its accession date.
> `verification: primary-source`.

## Description

Spain (ISO 3166-1 alpha-2: `ES`) is the **fifth country** populated in the
Data Initiatives Atlas, after [[NL]], [[DE]], [[BE]] and [[FR]].

Spanish entities live in the same flat type folders as every other
country's, tagged `country: ES`. EU instruments that apply in Spain
reference it via an `applies-in` relationship — the same single entity that
already carries `applies-in` to four other countries.

## Why Spain, specifically

`progress/backlog.md` asked for this one by name:

> *A fifth country outside the founding-six / Benelux-DACH group. All four
> so far are neighbouring western European states with similar
> administrative traditions. A Nordic, southern or central European state
> (Ireland, Spain, Poland, Estonia) would test whether the model is
> **western-European**-shaped rather than merely country-neutral — a
> question four similar countries cannot answer.*

Spain answers it. The first four countries share a border with at least one
other; Spain is southern European, joined the EU in a later enlargement than
any of them, and organises its state on a constitutional principle none of
the others use.

**The model held again**, with no schema, ontology, taxonomy,
relationship-type, folder, validation or generator change, and no `ES-EU-*`
entity. Whatever the Atlas's ontology is shaped like, it is not shaped like
the six founding members.

## What Spain did change: the federal gap now has a *third* shape

Spain is neither unitary like France and the Netherlands nor federal like
Germany and Belgium. It is a **State of Autonomies** — seventeen Comunidades
Autónomas holding devolved competences of differing scope, a constitutional
form deliberately built to be neither.

The Atlas cannot express any of it, for the same single reason as before:
there is no `level` term between `national` and `local`.

The cost is measurable rather than theoretical here:

- the autonomous communities operate **seventeen open data portals** —
  eleven with roughly 5,000 datasets in 2013, seventeen with over 14,000 by
  2019 — none of which is representable;
- they manage **more than 35 % of consolidated public spending**;
- [[ES-ESPANA-DIGITAL-2026]] adds *cogobernanza del Estado y las
  Comunidades Autónomas* as one of two new cross-cutting axes, so
  state–regional co-governance is an explicit, named element of the
  national digital strategy — and the Atlas can model the state half only.

Germany's Länder, Belgium's Regions and Spain's Comunidades Autónomas are
three constitutionally distinct things. **The Atlas fails on all three
identically**, which is the strongest available evidence that the defect is
in the `level` vocabulary rather than in any one country's shape.

Three of five countries are now affected. No sub-national level has been
invented, because doing so for one country is exactly the country-specific
change the model exists to prevent.

## What Spain adds that no earlier country did

- **[[ES-AESIA]] — the first AI supervisory agency in the European Union**,
  created in 2023, before the AI Act applied. It gives the Atlas its first
  sourced national link to [[EU-AI-ACT]].
- **[[ES-LEY-37-2007]] — the Open Data Directive transposition**, which
  Belgium and France both failed to produce. The gap that had spread across
  two countries closes on the third attempt.
- **[[ES-AEAD]] superseding [[ES-SGAD]]** — the Atlas's first modelled
  *organisational* succession, as opposed to a succession between documents.
- **[[ES-INE]] → [[EU-EUROSTAT]]** — the first edge of any kind in the
  statistics cluster, after five refusals across four countries.

## Relationships

See `countries/es/index.md` for the curated index of Spanish entities.

## Sources

Listed in frontmatter, including the ISO Online Browsing Platform entry —
the same citation [[DE]], [[BE]] and [[FR]] carry, and one the [[NL]] anchor
still lacks because Batch 0 composed its URLs from background knowledge.

**No `accessed` date and no `last_verified`** — nothing about this entity
has been checked against a source.
