---
id: NL-WET-BRP
type: law
name: Wet basisregistratie personen
alternative_names:
  - Wet BRP
description: >
  Dutch act forming the basis for the registration of personal data in the
  Basisregistratie Personen. In force since 6 January 2014, it replaced the
  municipal GBA registrations with a single central national registration
  and sets out the requirements on managers and users of the BRP.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2014-01-06
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-BASISREGISTRATIES
relationships:
  - type: applies-to
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "The Wet BRP has formed the basis for registering personal data in the Basisregistratie Personen since 2014; the BRP is one of the ten basisregistraties (rvig.nl; digitaleoverheid.nl BRP page). NOT READ — search-only."
    confidence: medium
    valid_from: 2014-01-06
    valid_until: null

sources:
  - title: "Wetgeving Basisregistratie Personen"
    url: "https://www.rvig.nl/wetgeving-basisregistratie-personen"
    publisher: "Rijksdienst voor Identiteitsgegevens (RvIG)"
  - title: "BRP — Stelsel van basisregistraties"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/10-basisregistraties/brp/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "Basisregistratie Personen (BRP)"
    url: "https://www.rijksoverheid.nl/onderwerpen/privacy-en-persoonsgegevens/basisregistratie-personen-brp"
    publisher: "Rijksoverheid"
---

# Wet basisregistratie personen (Wet BRP)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The Wet BRP has formed the basis for the registration of personal data in
the Basisregistratie Personen since it came into effect on 6 January 2014.
It created the foundation for a single central national database of personal
data, replacing the local Gemeentelijke Basisadministraties (GBA). The act
sets out the requirements that managers and users of the BRP must meet, and
the purposes for which BRP information may be used.

Data recorded includes at least: name and first names; date, place and
country of birth; data on parents, marriage or registered partnership, and
children; nationality and, where applicable, residence rights; address; and
the burgerservicenummer (BSN).

BRP personal data are not public. Only organisations performing a societal
task may obtain data from it, and where an organisation does so, that fact
remains visible for twenty years.

The BRP is administered by the Rijksdienst voor Identiteitsgegevens (RvIG),
which is not yet an Atlas entity and is queued in
`discovery/research-queue.md`.

## Relationships

- Governs the BRP, one of the registrations within
  [[NL-BASISREGISTRATIES]].
- Interacts with [[NL-UAVG]] and [[EU-GDPR]], since BRP data are personal
  data; no relationship is asserted, as none was sourced.

## Sources

Listed in frontmatter.
