---
id: DE-CATENA-X
type: data-space
name: Catena-X Automotive Network
alternative_names:
  - Catena-X
description: >
  Open and collaborative data ecosystem for the automotive industry,
  launched in 2021. It is a distributed, Gaia-X-based data ecosystem built
  on European standards and following the International Data Spaces
  reference architecture, intended to guarantee the digital sovereignty of
  actors in the automotive industry and to enable secure, decentralised and
  standardised data exchange between vehicle manufacturers, suppliers and
  service providers along the automotive value chain.

level: sectoral
country: DE
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2021-01-01
end_date: null
last_verified: null
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - EU-GAIA-X
relationships:
  - type: based-on
    target: EU-GAIA-X
    source: fact
    evidence: "Catena-X creates a distributed GAIA-X-based data ecosystem built on European standards and is based on the technologies of GAIA-X; it follows the Gaia-X specifications and the reference architecture of the International Data Spaces from the outset (iff.fraunhofer.de; isst.fraunhofer.de; automotiveit.eu). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Offener und kollaborativer Datenraum für die Automobilindustrie (Projekt Catena-X)"
    url: "https://www.iff.fraunhofer.de/de/geschaeftsbereiche/logistik-fabriksysteme/catena-x.html"
    publisher: "Fraunhofer-Institut für Fabrikbetrieb und -automatisierung (IFF)"
  - title: "Catena-X Automotive Network — Alliance for secure and standardized data exchange"
    url: "https://www.isst.fraunhofer.de/en/departments/mobility-und-smart-cities/projects/CatenaX.html"
    publisher: "Fraunhofer-Institut für Software- und Systemtechnik (ISST)"
  - title: "Catena-X — Datenökosystem für die Autoindustrie"
    url: "https://www.automotiveit.eu/catena-x"
    publisher: "automotiveIT"
  - title: "Catena-X"
    url: "https://arena2036.de/en/catena-x/"
    publisher: "ARENA2036"
  - title: "Was ist Catena-X?"
    url: "https://www.springerprofessional.de/automobilwirtschaft/unternehmen---institutionen/was-ist-catena-x-/50174986"
    publisher: "Springer Professional"
---

# Catena-X Automotive Network

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

Catena-X was **launched in 2021** to develop an open, standardised data
ecosystem for the automotive industry. It is a **distributed
[[EU-GAIA-X]]-based data ecosystem built on European standards**, intended
to guarantee the digital sovereignty of all actors in the industry.

It is the data-centric platform on which vehicle manufacturers, suppliers
and service providers exchange information securely, and it follows the
Gaia-X specifications **and the reference architecture of the International
Data Spaces** from the outset. Its aim is standardised data and information
flows along the entire automotive value chain.

Its reach is not European-only: a Catena-X hub opened in Shanghai in 2024,
and a cooperation agreement with the Chinese automobile association CAAM in
April 2025 allows Chinese manufacturers to be integrated.

## ⚠ `country: DE` is the weakest field in this entity

Catena-X is recorded as German on the basis of German origin and German
institutional backing — the cited Fraunhofer institutes, ARENA2036, the
German automotive industry.

That is a thin basis, and it is the **same problem [[NL-ISHARE]] already
has**. iSHARE was recorded `country: NL` for its Dutch origin while
operating at ishare.eu in a European data-space context; its entity body
calls this "exactly the case the `country` field handles least well" and
flags it as provisional. Catena-X is the identical case in a second
country, with a Shanghai hub and a Chinese industry agreement making it
sharper still.

Two independent instances mean this is **a property of the model, not of
either entity**. The `country` field conflates three different things —
where an initiative originated, where it is governed, and where it
operates — and industry data spaces routinely differ on all three.

`level: sectoral` is recorded rather than `national`, which is at least
honest about the second axis. The `country` field is logged as an open
ontology question in `discovery/unresolved.md`, now with two supporting
cases rather than one.

## The IDS reference architecture is not an entity

Catena-X follows the **International Data Spaces reference architecture**,
and [[NL-ISHARE]] records that the IDSA incorporated the iSHARE agreement
system into the IDS architecture. Two entities in two countries now point
at the same missing node.

**Neither the IDSA nor the IDS-RAM is an Atlas entity**, and neither is
created here: both mentions are single clauses in sources about something
else, which is not enough to build an international standards body on.
This is now the best-evidenced gap in the Atlas's international layer —
two independent references from two national data spaces — and it is
queued in `discovery/research-queue.md` accordingly.

## Manufacturing-X and the wider family

Catena-X sits within a broader German industrial data-space family
including Manufacturing-X. **No other member is modelled**, and no
industry or manufacturing domain entity was created: `metadata/taxonomy.md`
§1 requires a domain to connect at least two entities, and Catena-X alone
does not meet the threshold. `domains: []` is therefore empty, which is
correct rather than an omission.

## Relationships

- `based-on` [[EU-GAIA-X]].

## Sources

Listed in frontmatter — two Fraunhofer institutes, a research campus and
two trade publications. **No catena-x.net source is cited**; none was
returned by search, so this entity describes Catena-X entirely through
third parties.
