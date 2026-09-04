---
id: BE-DIGITAAL-VLAANDEREN
type: organisation
name: Digitaal Vlaanderen
alternative_names:
  - Agentschap Digitaal Vlaanderen
  - Informatie Vlaanderen
  - Flanders Digital Agency
description: >
  Flemish government agency for digital transformation and ICT policy
  support, an "intern verzelfstandigd agentschap" (internally autonomous
  agency without legal personality) established by Besluit van de
  Vlaamse Regering of 18 March 2016 under the name Informatie
  Vlaanderen. In early 2021 it merged with the ICT department of Het
  Facilitair Bedrijf and was renamed Digitaal Vlaanderen, employing
  around 640 staff. It supports digitalisation policy, builds and
  operates shared digital and ICT solutions for the Flemish public
  sector, and maintains OSLO, the Flemish semantic interoperability
  standard.

level: subnational
country: BE
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2016-03-18
end_date: null
last_verified: "2026-09-04"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - BE
  - BE-OSLO
relationships:
  - type: part-of
    target: BE
    source: fact
    evidence: "Confirmed by reading codex.vlaanderen.be's own consolidated text of the founding Besluit van de Vlaamse Regering directly (2026-09-04): Article 2 establishes an internally autonomous agency 'opgericht onder de benaming Digitaal Vlaanderen' (established under the name Digitaal Vlaanderen), with Article 3 giving it a mandate to support digitalisation policy and provide scalable digital and ICT solutions for public-sector service delivery. Anchor edge under metadata/relationship-types.md §2.3, asserting Flemish sub-federal scope via `level: subnational`."
    confidence: medium
    valid_from: 2016-03-18
    valid_until: null

sources:
  - title: "Besluit van de Vlaamse Regering houdende de oprichting van het intern verzelfstandigd agentschap Digitaal Vlaanderen"
    url: "https://codex.vlaanderen.be/PrintDocument.ashx?id=1026864&datum=&geannoteerd=false&print=false"
    publisher: "Vlaamse Codex (Vlaamse overheid)"
    accessed: "2026-09-04"
  - title: "Digitaal Vlaanderen — Vlaanderen.be"
    url: "https://www.vlaanderen.be/en"
    publisher: "Vlaamse overheid"
    accessed: "2026-09-04"
---

# Digitaal Vlaanderen

> **Added 2026-09-04, `verification: primary-source` from creation.**
> `discovery/research-queue.md` had recorded Digitaal Vlaanderen as
> entirely unmodelled, blocked (it said) on the Atlas having no `level`
> term for a Belgian Region. `level: subnational` closed that blocker on
> 2026-08-21; this is one of the first entities to use it for an
> organisation rather than a sub-federal act. `codex.vlaanderen.be`'s own
> consolidated founding decree was read directly this pass.

## Description

Digitaal Vlaanderen is the Flemish government's digital-transformation
and ICT-policy agency. It is an **intern verzelfstandigd agentschap
zonder rechtspersoonlijkheid** (internally autonomous agency without
legal personality), established by **Besluit van de Vlaamse Regering of
18 March 2016**, read directly on `codex.vlaanderen.be` — the agency's
own consolidated legal text, still in force under a decree amended in
place to carry its current name, the same pattern the Atlas has already
recorded for [[IT-CAD]].

## One founding decree, two names

The agency was originally established under the name **Informatie
Vlaanderen**. In **early 2021** it merged with the ICT department of
**Het Facilitair Bedrijf** (the Flemish government's facilities agency)
and was renamed **Digitaal Vlaanderen**, now employing around 640 staff
— confirmed by secondary reporting on the merger, not independently
re-verified against a government announcement this pass. The founding
decree's own consolidated text, read directly, already carries the
post-2021 name throughout, which is why its date (18 March 2016) is
recorded as this entity's `start_date` rather than the later rename
date: the legal person is continuous, and the Atlas already gives the
same treatment to [[DE-BMV]]'s BMDV lineage.

## Maintains OSLO

Digitaal Vlaanderen's GitHub organisation, `github.com/Informatievlaanderen`
— still carrying the pre-2021 name — publishes and maintains
[[BE-OSLO]], the Flemish semantic-interoperability standard. See that
entity for OSLO's own two-phase history.

## Not modelled

- **Het Facilitair Bedrijf**, the agency Digitaal Vlaanderen partly
  absorbed in 2021. Named here in prose only.
- A specific relationship to [[BE-BELGIF]], the federal Belgian
  interoperability framework. No source read this pass connects the two
  directly.

## Relationships

- `part-of` [[BE]] (anchor edge, `level: subnational`).

## Sources

Listed in frontmatter, both read directly this pass.
