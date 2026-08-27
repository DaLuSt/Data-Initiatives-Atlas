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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
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
    evidence: "Confirmed by reading wetten.overheid.nl's own text of BWBR0004541 directly (2026-08-27): 'Wet van 3 mei 1989, houdende regelen met betrekking tot de openbare registers voor registergoederen, alsmede met betrekking tot het kadaster.' Article 1a establishes 'een basisregistratie kadaster, bestaande uit administratieve gegevens met betrekking tot onroerende zaken en de landelijke kadastrale kaart' and, in the same article, 'een basisregistratie topografie' — confirming both this register's statutory basis and the BRT's, and assigning both to the Dienst voor het kadaster en de openbare registers."
    confidence: high
    valid_from: null
    valid_until: null
  - type: part-of
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "Confirmed by reading data.overheid.nl's basisregistraties_10 group listing directly (2026-08-27), which names 'Basisregistratie: Kadaster (BRK)' among the ten, and geobasisregistraties.nl's own overview page, also read directly, which places the BRK's ownership question ('wie is de eigenaar') alongside the address, function/dimension, value and subsurface registers as one of the coordinated geo base registrations."
    confidence: high
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NL-KADASTER
    source: fact
    evidence: "Confirmed by reading kadaster.nl's own BRK page directly (2026-08-27): the BRK comprises cadastral registration, the cadastral map, and registered utility networks. catalogus.kadaster.nl's BRK catalogue page, also read directly, confirms the KvK-number link: 'in steeds meer van onze BRK-producten leveren wij voortaan bij organisaties...het KVK-nummer mee' (increasingly, our BRK products now include the KvK number for organisations), naming six specific products including Eigendomsinformatie and BRK Levering."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Waar bestaat de BRK uit? — Kadaster"
    url: "https://www.kadaster.nl/zakelijk/registraties/basisregistraties/brk"
    publisher: "Kadaster"
    accessed: "2026-08-27"
  - title: "Overzicht registraties — Kadaster"
    url: "https://www.kadaster.nl/zakelijk/registraties"
    publisher: "Kadaster"
    accessed: "2026-08-27"
  - title: "Handelsregister | Basisregistratie Kadaster (BRK)"
    url: "https://catalogus.kadaster.nl/brk/nl/page/Handelsregister"
    publisher: "Kadaster"
    accessed: "2026-08-27"
  - title: "Basisregistraties | Geobasisregistraties"
    url: "https://www.geobasisregistraties.nl/basisregistraties"
    publisher: "Geobasisregistraties (Ministerie van BZK)"
    accessed: "2026-08-27"
  - title: "Kadasterwet — official text"
    url: "https://wetten.overheid.nl/BWBR0004541"
    publisher: "Overheid.nl (Basiswettenbestand)"
    accessed: "2026-08-27"
---

# BRK — Basisregistratie Kadaster

> **Verified 2026-08-27.** All five cited pages read directly, including the
> Kadasterwet's own official text added as a new source: it confirms the
> BRK's statutory basis in Article 1a, in the same sentence that establishes
> the BRT — the two registers genuinely share one statute.

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

Listed in frontmatter, all five read directly this pass — the two Kadaster
pages, the BRK catalogue's Handelsregister page, the geobasisregistraties.nl
overview, and the Kadasterwet's own official text (added this pass, shared
with [[NL-BRT]]).
