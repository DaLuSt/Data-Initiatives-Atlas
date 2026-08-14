---
id: NL-GDI
type: platform
name: Generieke Digitale Infrastructuur
alternative_names:
  - GDI
description: >
  The Netherlands' generic digital infrastructure: the set of shared digital
  facilities, standards and services used across government and by
  organisations with a public task. Services within it are operated by
  Logius; its modernisation is programmed through MIDO.

level: national
country: NL
region: null

status: active
confidence: low
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-LOGIUS
  - NL-BZK
related_entities:
  - NL-MIDO
relationships:
  - type: maintained-by
    target: NL-LOGIUS
    source: fact
    evidence: "GDI services are described as managed by Logius; from 2023 several moved to central BZK budget (logius.nl, rijksfinancien.nl). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Facturatie GDI-diensten 2023 is veranderd"
    url: "https://www.logius.nl/actueel/facturatie-gdi-diensten-2023-veranderd"
    publisher: "Logius"
  - title: "Stelsel van het heden (Stelseldiensten ter ondersteuning)"
    url: "https://www.noraonline.nl/wiki/Stelsel_van_het_heden_(Stelseldiensten_ter_ondersteuning)"
    publisher: "NORA Online (ICTU)"
  - title: "Wat is het MIDO?"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/mido/wat-is-het-mido/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
---

# Generieke Digitale Infrastructuur (GDI)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The GDI is the Netherlands' generic digital infrastructure: shared digital
facilities, standards and services reused across government rather than
rebuilt per organisation. Services commonly named as part of it include
DigiD, DigiD Machtigen and MijnOverheid, operated by [[NL-LOGIUS]]. From
2023 the funding model for several of these changed, with the services
moving to a central budget managed by [[NL-BZK]] instead of being invoiced
to using organisations.

Its modernisation is programmed through [[NL-MIDO]].

`coverage: low`: the individual GDI services are not yet Atlas entities, and
the boundary of what counts as "in" the GDI has not been established from a
source. The expansion of "GDI" also needs checking — search results rendered
it both as *Generieke* and as *Gezamenlijke* Digitale Infrastructuur, which
may reflect a genuine change in terminology or simply inconsistent
secondary sources. Recorded in `discovery/unresolved.md`.

The typing as `platform` is an Atlas judgement: the GDI is a collection of
systems and agreements rather than a single system, so `platform` and
`framework` are both partly apt. Flagged for review.

## Relationships

- Services operated by [[NL-LOGIUS]]; funded/steered via [[NL-BZK]].
- Modernised through [[NL-MIDO]].

## Atlas interpretation

Entity typing and the scope boundary of the GDI are Atlas interpretations.

## Sources

Listed in frontmatter.
