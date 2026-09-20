---
id: DE-PLATTFORM-INDUSTRIE-4-0
type: organisation
name: Plattform Industrie 4.0
alternative_names:
  - Platform Industrie 4.0
  - Plattform Industrie 4.0 (PI4.0)
description: >
  German government-industry platform providing coordinated support for
  the digital transformation of manufacturing ("Industrie 4.0"), jointly
  chaired by the Federal Ministry for Economic Affairs and the Federal
  Ministry of Education and Research alongside representatives from
  business, trade unions and academia. It organises its work through a
  Steering Committee, a Strategy Committee, an Academic Advisory Board
  and five thematic Working Groups (reference architectures/standards,
  research and innovation, security of networked systems, legal
  framework, and work/education/training), each chaired by a named
  representative from industry or the trade union IG Metall. The concept
  base for the Manufacturing-X family of data-space initiatives.

level: national
country: DE
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-20"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - DE-MANUFACTURING-X
  - DE-CATENA-X
relationships:
  - type: related-to
    target: DE-MANUFACTURING-X
    source: fact
    evidence: "PARTIALLY CLOSES discovery/unresolved.md row #131. Confirmed by reading Fraunhofer ISST's own Manufacturing-X page directly (already cited on [[DE-MANUFACTURING-X]]): Manufacturing-X 'builds upon and incorporates Catena-X principles' and Plattform Industrie 4.0 concepts, and the Manufacturing-X Council Germany is described there as coordinating the national cooperation of the initiative alongside the platform. Its own presentation deck (Geschäftsstelle Plattform Industrie 4.0, 'Digital Transformation \"Made in Germany\"', authored by the platform's own project office, dated 29 June 2016, read directly 2026-09-20 as a local PDF since the live site returns a bot-verification challenge) describes the platform as 'the moderator of and catalyst for the exchange amongst all societal actors in the pre-competitive phase' of Industrie 4.0 — the concept and coordination layer the Manufacturing-X family of data spaces was built on top of, rather than a data space itself. `related-to` rather than a more specific type: no source read states Manufacturing-X is organisationally part of or governed by the platform, only that it builds on its concepts and coordinates through a shared Council."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Plattform Industrie 4.0: Digital Transformation \"Made in Germany\""
    url: "https://ec.europa.eu/information_society/newsroom/image/document/2016-27/10__pi40_diemer_16494.pdf"
    publisher: "Geschäftsstelle Plattform Industrie 4.0 (project office)"
    accessed: "2026-09-20"
  - title: "Plattform Industrie 4.0"
    url: "https://www.ifm.com/us/en/shared/company/consortia-and-alliances/platform-industry-4.0"
    publisher: "ifm electronic (secondary corroboration)"
    accessed: "2026-09-20"
---

# Plattform Industrie 4.0

> **Created 2026-09-20**, partially closing `discovery/unresolved.md` row
> #131 ("Plattform Industrie 4.0 not modelled" — the row's final
> remaining item after Factory-X, Aerospace-X, Construct-X and
> HealthTrack-X closed earlier the same batch). Sourced primarily from
> the platform's own 2016 presentation deck, authored by its own project
> office ("Geschäftsstelle Plattform Industrie 4.0") and hosted on an EU
> Commission newsroom mirror — read directly as a local PDF since the
> platform's own live site (`plattform-i40.de`) and its parent ministry's
> site (`bundeswirtschaftsministerium.de`) both return a Radware
> bot-verification challenge, the same block already documented on
> [[DE-MANUFACTURING-X]]. A secondary source (ifm.com) corroborates the
> joint-ministry leadership and working-group structure independently.

## Description

Plattform Industrie 4.0 is Germany's government-industry platform
coordinating the digital transformation of manufacturing. Its own 2016
deck states its purpose directly: *"The Platform Industrie 4.0 provides
support for the coordinated and organised transition into the digital
economy in Germany"* and describes itself as *"the moderator of and
catalyst for the exchange amongst all societal actors in the
pre-competitive phase."*

## Structure, read directly from the platform's own org chart

The 2016 deck's own structure slide gives a precise picture:

- **Chair**: at the time, Federal Ministers **Sigmar Gabriel** (Economic
  Affairs) and **Johanna Wanka** (Education and Research) — named
  directly as "Ministers Gabriel, Wanka" — with representatives from
  business, trade unions and academia for political integration.
- **Steering Committee** (business-led, with BMWi/BMBF participation):
  technical/practical competences, industrial-strategy decision-making.
- **Strategy Committee** (chaired by two Secretaries of State — Machnig
  and Schütze — with representatives from federal and state governments,
  industry associations VDMA/ZVEI/BITCOM/BDI/VDA/BDEW, the trade union IG
  Metall, and the Fraunhofer-Gesellschaft): political direction,
  agenda-setting.
- An **Academic Advisory Board**.
- A **Project office** providing network coordination and communication.

## Five Working Groups, each with a named chair

Confirmed directly from the same deck — "the heart of the platform,"
open to qualified representatives from businesses and works councils:

| Working Group | Chair | Organisation |
|---|---|---|
| Reference architectures, standards and norms | Dr. Peter Adolphs | Pepperl+Fuchs |
| Research and innovation | Johannes Diemer | Hewlett Packard Enterprise |
| Security of networked systems | Michael Jochem | Robert Bosch GmbH |
| Legal framework | Dr. Hans-Jürgen Schlinkert | ThyssenKrupp |
| Work, education and training | Dr. Constanze Kurz | IG Metall |

## The concept base for Manufacturing-X

[[DE-MANUFACTURING-X]]'s own entity already records, via Fraunhofer ISST's
page, that Manufacturing-X's concepts build on this platform and that the
Manufacturing-X Council Germany coordinates alongside it. No source read
this pass states a formal organisational relationship (part-of,
governed-by) between the two — Plattform Industrie 4.0 is the broader,
older coordination platform (Industrie 4.0 dates to the German
government's 2011 high-tech strategy, per English Wikipedia's own
"Industry 4.0" article, read directly, though that article does not
describe the platform's own founding date), and Manufacturing-X is one
initiative that grew out of it. `related-to` is recorded rather than a
more specific type.

## Not modelled

- The platform's **exact founding date** — not confirmed by any source
  read directly this pass; a 2013-launch/2015-relaunch date appears only
  in unread search snippets and is not recorded here.
- **Industrial consortia and initiatives** and **international
  standardisation** activities, the platform's own org chart's third
  column — not independently researched.
- The **Testbed network Industrie 4.0** and the **i4kmu.de** SME funding
  programme, both described in the same deck.
- **Ministers Gabriel and Wanka** as individuals, or their successors in
  the chair role today — this entity records the 2016 leadership as
  sourced, not the platform's current officeholders.

## Relationships

- `related-to` [[DE-MANUFACTURING-X]] — `confidence: medium`.

## Sources

Listed in frontmatter. The platform's own 2016 presentation deck was
read directly as a local PDF; ifm.com's page was read directly as
secondary corroboration for the joint-ministry leadership and
working-group structure, though its own founding-date/member-count
claims could not be independently confirmed.
