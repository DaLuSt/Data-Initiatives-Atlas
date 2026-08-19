---
id: NL-BRK
type: platform
name: Basisregistratie Kadaster
alternative_names:
  - BRK
  - Cadastral Base Registry
description: >
  The Dutch cadastral base registry, held by the Kadaster, and one of the
  ten registrations in the stelsel van basisregistraties. It records
  ownership of real property, and within the geo base registries it is the
  registration that answers the ownership question, alongside the
  topographic registries for shape and dimensions, the address and buildings
  registry for location, the property-value registry for value and the
  subsurface registry for what lies beneath. Its products increasingly carry
  the KvK number of organisations, linking it to the trade register, and the
  Kadaster relates it to the address, trade and persons registries.

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
  - DOMAIN-GOVERNMENT
  - DOMAIN-GEOSPATIAL
organisations:
  - NL-KADASTER
related_entities:
  - NL-KADASTERWET
  - NL-BASISREGISTRATIES
  - NL-KADASTER
  - NL-NHR
  - NL-BAG
  - NL-BRP
relationships:
  - type: governed-by
    target: NL-KADASTERWET
    source: fact
    evidence: "The Kadasterwet of 3 May 1989 contains rules on the public registers for registered property and on the cadastre; the cadastral base registration and the topographic base registration are maintained under it as authentic data, with database rights reserved to the Dienst voor het kadaster en de openbare registers (wetten.overheid.nl/BWBR0004541). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: part-of
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "The ten base registrations are the BRP, HR, BAG, BRT, BRK (Basisregistratie Kadaster), BRV, BRI, WOZ, BGT and BRO (digitaleoverheid.nl '10 basisregistraties'; data.overheid.nl; noraonline.nl). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NL-KADASTER
    source: fact
    evidence: "The Kadaster describes the BRK among the basisregistraties it holds, publishes the BRK catalogue, and connects the BRK with the Handelsregister of the KvK, increasingly providing KvK numbers in BRK products for organisations (kadaster.nl 'Waar bestaat de BRK uit?'; kadaster.nl 'Overzicht registraties'; catalogus.kadaster.nl/brk). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Waar bestaat de BRK uit? — Kadaster"
    url: "https://www.kadaster.nl/zakelijk/registraties/basisregistraties/brk"
    publisher: "Kadaster"
  - title: "Overzicht registraties — Kadaster"
    url: "https://www.kadaster.nl/zakelijk/registraties"
    publisher: "Kadaster"
  - title: "Handelsregister | Basisregistratie Kadaster (BRK)"
    url: "https://catalogus.kadaster.nl/brk/nl/page/Handelsregister"
    publisher: "Kadaster"
  - title: "Basisregistraties | Geobasisregistraties"
    url: "https://www.geobasisregistraties.nl/basisregistraties"
    publisher: "Geobasisregistraties (Ministerie van BZK)"
---

# BRK — Basisregistratie Kadaster

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The BRK is the Dutch cadastral base registry, held by [[NL-KADASTER]]. In
the division of labour among the geo base registries it is the one that
answers **ownership**.

The geobasisregistraties material sets out that division explicitly, and it
is the clearest statement of why these registers are a system:

| Question | Register |
|---|---|
| Where — the address | [[NL-BAG]] |
| What is there — function and shape | [[NL-BRT]], [[NL-BGT]] |
| **Who owns it** | **BRK** |
| What is it worth | [[NL-WOZ]] |
| What is underneath | [[NL-BRO]] |

Each register answers one question about the same physical object, which is
the stelsel's organising idea applied to land.

## The KvK number is a real, sourced key-sharing link

The Kadaster's own BRK catalogue has a page for the *Handelsregister*, and
records that BRK products increasingly carry the **KvK number** for
organisations. That is a concrete instance of two base registries sharing an
identifier, sourced from the register's own catalogue rather than inferred.

**It is still not asserted as a relationship.** The Atlas has no type for
"carries the identifier of", and the candidates all misstate it:
`references` implies a document citation, `depends-on` implies operational
dependency, `derived-from` is plainly wrong.

This is the fourth time in three batches that a real, well-sourced
connection has been left unmodelled for want of a relationship type — the
UN batch found two (the UNESCO agreement and the EU voluntary review), the
Belastingdienst's WOZ consumption is a third, and this is a fourth. See
`discovery/unresolved.md`.

## Relationships

- `part-of` [[NL-BASISREGISTRATIES]].
- `maintained-by` [[NL-KADASTER]].

## Sources

Listed in frontmatter.
