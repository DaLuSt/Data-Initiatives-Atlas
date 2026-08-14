---
id: NL-KADASTER
type: organisation
name: Kadaster
alternative_names:
  - Dienst voor het kadaster en de openbare registers
  - Netherlands' Cadastre, Land Registry and Mapping Agency
description: >
  Dutch cadastre, land registry and mapping agency. It holds and maintains
  the Basisregistratie Kadaster (BRK) and is involved in other geospatial
  base registrations, making it one of the principal holders of
  authoritative spatial data in the Netherlands.

level: national
country: NL
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
  - DOMAIN-GEOSPATIAL
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-GEONOVUM
relationships:
  - type: participates-in
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "Kadaster holds the BRK, one of the ten basisregistraties; kadaster.nl documents its basisregistraties role. NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Basisregistraties — Kadaster"
    url: "https://www.kadaster.nl/zakelijk/registraties/basisregistraties"
    publisher: "Kadaster"
  - title: "Waar bestaat de BRK uit?"
    url: "https://www.kadaster.nl/zakelijk/registraties/basisregistraties/brk"
    publisher: "Kadaster"
  - title: "Basisregistratie Kadaster (BRK)"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/10-basisregistraties/brk/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "BRK (Basisregistratie Kadaster)"
    url: "https://www.noraonline.nl/wiki/BRK_(Basisregistratie_Kadaster)"
    publisher: "NORA Online (ICTU)"
---

# Kadaster

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The Kadaster is the Dutch cadastre, land registry and mapping agency. It
holds the Basisregistratie Kadaster (BRK), one of the registrations in the
[[NL-BASISREGISTRATIES]]. The BRK comprises two components: the cadastral
registration and the cadastral map. The registration covers cadastral
objects (parcels and apartment rights), ownership, mortgages, limited rights
such as leasehold, superficies and usufruct, and utility networks.

The Kadaster relates the BRK to other base registrations — the BAG
(addresses and buildings), the Handelsregister held by [[NL-KVK]], and the
BRP (persons) — which makes it a hub in the base-registry graph rather than
an isolated register holder.

It is also one of the funders of [[NL-GEONOVUM]]'s base programme,
connecting it to Dutch geo-standardisation.

## Relationships

- Participates in [[NL-BASISREGISTRATIES]] as holder of the BRK.
- Co-funder of [[NL-GEONOVUM]].

## Sources

Listed in frontmatter.
