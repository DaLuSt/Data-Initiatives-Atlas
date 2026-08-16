---
id: DE-DESTATIS
type: organisation
name: Statistisches Bundesamt
alternative_names:
  - Destatis
  - StBA
  - Federal Statistical Office of Germany
description: >
  German federal statistical office, in the business area of the Federal
  Ministry of the Interior. Its tasks are set by the Bundesstatistikgesetz:
  continuously collecting, compiling, processing, presenting and analysing
  data on mass phenomena under principles of neutrality, objectivity and
  professional independence, and publishing results in open-data-compliant,
  machine-readable formats.

level: national
country: DE
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

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - DE-BMI
  - DE-BSTATG
relationships:
  - type: part-of
    target: DE-BMI
    source: fact
    evidence: "The Statistisches Bundesamt is a German federal authority in the business area (Geschäftsbereich) of the Federal Ministry of the Interior (de.wikipedia.org 'Statistisches Bundesamt'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: DE-BSTATG
    source: fact
    evidence: "The tasks of the Statistisches Bundesamt are legally established in the Bundesstatistikgesetz; under § 1 BStatG they lie in continuously collecting, compiling, processing, presenting and analysing data on mass phenomena (destatis.de 'Gesetzliche Grundlagen'; destatis.de 'Aufgaben'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

  - type: part-of
    target: EU-ESS
    source: fact
    evidence: "The European Statistical System is the partnership between the Community statistical authority, which is the Commission (Eurostat), and the national statistical institutes and other national authorities responsible in each member state for the development, production and dissemination of European statistics; the ESS Committee is composed of NSI representatives and chaired by Eurostat (ec.europa.eu/eurostat/web/european-statistical-system; EUR-Lex CELEX 32009R0223; cso.ie European Statistical System page). Destatis is the German NSI. NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
sources:
  - title: "Aufgaben — Statistisches Bundesamt"
    url: "https://www.destatis.de/DE/Ueber-uns/Aufgaben/_inhalt.html"
    publisher: "Statistisches Bundesamt (Destatis)"
  - title: "Gesetzliche Grundlagen — Statistisches Bundesamt"
    url: "https://www.destatis.de/DE/Ueber-uns/Aufgaben/gesetze.html"
    publisher: "Statistisches Bundesamt (Destatis)"
  - title: "Statistisches Bundesamt"
    url: "https://de.wikipedia.org/wiki/Statistisches_Bundesamt"
    publisher: "Wikipedia"
  - title: "Statistisches Bundesamt/Statistische Landesämter"
    url: "https://www.bpb.de/kurz-knapp/lexika/handwoerterbuch-politisches-system/202188/statistisches-bundesamt-statistische-landesaemter/"
    publisher: "Bundeszentrale für politische Bildung (bpb)"
  - title: "Statistisches Bundesamt"
    url: "https://www.service.bund.de/Content/DE/DEBehoerden/S/StBA/Statistisches-Bundesamt.html?nn=4641496"
    publisher: "service.bund.de (Bundesverwaltungsamt)"
---

# Statistisches Bundesamt (Destatis)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

Destatis is Germany's federal statistical office, in the Geschäftsbereich
of [[DE-BMI]]. Its tasks are established in [[DE-BSTATG]]: under § 1
BStatG, continuously collecting, compiling, processing, presenting and
analysing data on mass phenomena.

Principles of **neutrality, objectivity and professional independence**
apply, and data is obtained using scientific knowledge and appropriate
methods and information technologies.

Two aspects matter for the Atlas specifically:

- **Open data by default in the output.** The office prepares federal
  statistics methodically and technically, compiles results for the federal
  government from data supplied by the Länder, and publishes them in
  **open-data-compliant, machine-readable formats**.
- **The European and international layer.** Destatis has the particular
  task of cooperating in the preparation of statistical programmes and
  regulations, and in the methodological and technical preparation and
  harmonisation of statistics for the purposes of the European Union and
  international organisations.

It is bound to comply with data protection and to maintain statistical
confidentiality of the individual data it collects.

## The link to Eurostat that is not asserted

That second point is tantalisingly close to the connection the Atlas most
needs. Batch 15 recorded that **the UN layer connects to nothing outside
itself** and that the two links which would close most of the gap —
[[UN-UNSD]] → [[EU-EUROSTAT]] and [[UN-FPOS]] → [[NL-WET-CBS]] — were
refused for want of a source.

Destatis offers a third candidate of the same shape: a national statistical
office whose sourced remit explicitly includes harmonising statistics for
EU purposes. **It is refused on the same grounds.** "Cooperating in the
preparation of statistical programmes and regulations ... for the purposes
of the European Union" does not name [[EU-EUROSTAT]], and the European
Statistical System is not mentioned in any source read.

Adding it would close a structural gap the Atlas has flagged twice and
would be, as the Final Quality Gate put it about the earlier pair, *"plainly
true in substance"*. It would also be unsourced. The gap stays open; the
candidate is logged in `discovery/unresolved.md` alongside the other two,
where a single reading of three pages would probably close all three at once.

## Relationships

- `part-of` [[DE-BMI]].
- `governed-by` [[DE-BSTATG]].

## Sources

Listed in frontmatter.
