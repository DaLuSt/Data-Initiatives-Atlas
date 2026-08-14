---
id: NL-NATIONAAL-ARCHIEF
type: organisation
name: Nationaal Archief
alternative_names:
  - National Archives of the Netherlands
description: >
  The national archive of the Netherlands. It receives government records
  transferred under the Archiefwet and acts as the national expertise centre
  on sustainable accessibility of information, for central government and
  for other public bodies and archival institutions.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: low
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
  - NL-ARCHIEFWET-1995
  - NL-ARCHIEFWET-2026
relationships:
  - type: governed-by
    target: NL-ARCHIEFWET-1995
    source: fact
    evidence: "Government organisations must in principle transfer records after twenty years to the Nationaal Archief or a local/regional archive service under the Archiefwet (nationaalarchief.nl kennisbank). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: 2027-01-01

sources:
  - title: "Archiefwet — Kennisbank"
    url: "https://www.nationaalarchief.nl/archiveren/kennisbank/archiefwet"
    publisher: "Nationaal Archief"
  - title: "Wet- en regelgeving — Kennisbank"
    url: "https://www.nationaalarchief.nl/archiveren/kennisbank/wet-en-regelgeving"
    publisher: "Nationaal Archief"
  - title: "Archieven van de overheid"
    url: "https://www.rijksoverheid.nl/themas/overheid-en-democratie/archieven/archieven-van-de-overheid"
    publisher: "Rijksoverheid"
---

# Nationaal Archief

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The Nationaal Archief is the national archive of the Netherlands. It enters
the Atlas through information management (informatiehuishouding) rather than
cultural heritage: it acts as the national expertise centre on sustainable
accessibility of information, serving central government as well as other
public bodies and archival institutions.

Its operational role derives from the Archiefwet, which requires every
government organisation to make and keep information sustainably accessible
and to destroy it once retention periods expire. Government organisations
must in principle transfer records after twenty years to the Nationaal
Archief or to a local or regional archive service.

Batch 3 added both the current [[NL-ARCHIEFWET-1995]] and its successor
[[NL-ARCHIEFWET-2026]], which takes effect on 1 January 2027 and shortens
the transfer period from twenty years to ten — a change that bears directly
on this organisation's intake.

## Relationships

- Governed by [[NL-ARCHIEFWET-1995]], with `valid_until: 2027-01-01`
  recording that this relationship is time-bounded.
- [[NL-ARCHIEFWET-2026]] will govern it from 1 January 2027. That
  relationship is deliberately **not** yet asserted as current: the
  `valid_until` on the existing one, plus the successor chain between the
  two acts, already expresses the transition without claiming a governing
  relationship that has not yet commenced.

## Sources

Listed in frontmatter.
