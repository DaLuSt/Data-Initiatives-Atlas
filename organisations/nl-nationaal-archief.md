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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
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
    evidence: "Confirmed by reading nationaalarchief.nl's own Archiefwet page directly (2026-08-27): government organisations must, in principle, transfer permanently valuable records to the Nationaal Archief (or a local/regional archive service) within twenty years. rijksoverheid.nl's own page, also read directly, states the same rule: 'Daar kan iedereen deze documenten doorzoeken en inzien' (everyone can search and view these documents there) once transferred. nationaalarchief.nl's wet-en-regelgeving page, also read directly, names the Archiefbesluit 1995 and the Archiefregeling as the implementing decree and regulation beneath the Act."
    confidence: high
    valid_from: null
    valid_until: 2027-01-01

sources:
  - title: "Archiefwet — Kennisbank"
    url: "https://www.nationaalarchief.nl/archiveren/kennisbank/archiefwet"
    publisher: "Nationaal Archief"
    accessed: "2026-08-27"
  - title: "Wet- en regelgeving — Kennisbank"
    url: "https://www.nationaalarchief.nl/archiveren/kennisbank/wet-en-regelgeving"
    publisher: "Nationaal Archief"
    accessed: "2026-08-27"
  - title: "Archieven van de overheid"
    url: "https://www.rijksoverheid.nl/themas/overheid-en-democratie/archieven/archieven-van-de-overheid"
    publisher: "Rijksoverheid"
    accessed: "2026-08-27"
---

# Nationaal Archief

> **Verified 2026-08-27.** All three cited pages read directly. Both add a
> detail not previously recorded: the **Inspectie Overheidsinformatie en
> Erfgoed** monitors national-government compliance with archive rules
> (rijksoverheid.nl), and the twenty-year transfer regime sits beneath an
> Archiefbesluit 1995 and Archiefregeling that the entity's prior text did
> not name (nationaalarchief.nl).

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
[[NL-ARCHIEFWET-2026]], which shortens the transfer period from twenty years
to ten. Its status is more concrete than a "planned" bill this pass: reading
the Staatsblad directly (for [[NL-ARCHIEFWET-2026]] this pass) confirms the
Act was signed 13 May 2026 and published as Stb. 2026, 149 on 19 June
2026 — enacted, with entry into force still set by royal decree, expected
1 January 2027 per nationaalarchief.nl's own knowledge base.

## Relationships

- Governed by [[NL-ARCHIEFWET-1995]], with `valid_until: 2027-01-01`
  recording that this relationship is time-bounded.
- [[NL-ARCHIEFWET-2026]] will govern it from 1 January 2027. That
  relationship is deliberately **not** yet asserted as current: the
  `valid_until` on the existing one, plus the successor chain between the
  two acts, already expresses the transition without claiming a governing
  relationship that has not yet commenced.

## Sources

Listed in frontmatter, all three read directly this pass — the Nationaal
Archief's own Archiefwet and wet-en-regelgeving pages, and rijksoverheid.nl's
overview page.
