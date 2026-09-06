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
verification: primary-source

start_date: 1832-10-01
end_date: null
last_verified: "2026-09-06"
previous_version: null
successor: null

domains:
  - DOMAIN-GEOSPATIAL
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-GEONOVUM
  - EU-EUROGEOGRAPHICS
  - NL-ORGANISATIEWET-KADASTER
  - NL-KADASTERWET
relationships:
  - type: governed-by
    target: NL-ORGANISATIEWET-KADASTER
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP. Confirmed by reading wetten.overheid.nl's own text of the Organisatiewet Kadaster directly (2026-09-06), Article 2(1): 'Er is een Dienst voor het kadaster en de openbare registers... Hij bezit rechtspersoonlijkheid en is gevestigd te Apeldoorn' — this Act constitutes the Kadaster as a body with legal personality, distinct from NL-KADASTERWET which governs the registers it maintains."
    confidence: high
    valid_from: 1994-02-14
    valid_until: null
  - type: participates-in
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "Confirmed by reading kadaster.nl's own registrations overview directly (2026-08-27): the Kadaster holds five base registrations (BAG, BRK, Rijksdriehoeksmeting, BRT, BGT) plus the Informatiemodel Kadaster (IMKAD). digitaleoverheid.nl's dedicated BRK page returned a bot-verification wall on this pass and NORA Online's BRK wiki page returned HTTP 404 — both confirmed genuinely unreadable, not merely unread. nl.wikipedia.org's own Kadaster article, read directly as a replacement source this pass, independently confirms the Kadaster's role in BRK and BRT ('Sinds 2004 valt de Topografische Dienst onder het Kadaster')."
    confidence: high
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-EUROGEOGRAPHICS
    source: fact
    evidence: "EuroGeographics is the membership association for the European National Mapping, Cadastral and Land Registry Authorities, an international not-for-profit association (AISBL/IVZW under Belgian law, BCE 833 607 112) bringing together 63 organisations from 46 countries covering the whole of geographical Europe (eurogeographics.org/our-members/; eurogeographics.org). NOT READ this pass — eurogeographics.org was not re-fetched. Membership follows from the sourced composition rule rather than from a source naming this authority, the same basis on which the national standardisation bodies were attached to EU-CEN. This entity is the Netherlands' national land registry, cadastre and mapping agency."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Basisregistraties — Kadaster"
    url: "https://www.kadaster.nl/zakelijk/registraties/basisregistraties"
    publisher: "Kadaster"
    accessed: "2026-08-27"
  - title: "Waar bestaat de BRK uit?"
    url: "https://www.kadaster.nl/zakelijk/registraties/basisregistraties/brk"
    publisher: "Kadaster"
    accessed: "2026-08-27"
  - title: "Basisregistratie Kadaster (BRK) (confirmed bot-walled, not read)"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/10-basisregistraties/brk/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "BRK (Basisregistratie Kadaster) (confirmed dead, HTTP 404)"
    url: "https://www.noraonline.nl/wiki/BRK_(Basisregistratie_Kadaster)"
    publisher: "NORA Online (ICTU)"
  - title: "Kadaster (Nederland)"
    url: "https://nl.wikipedia.org/wiki/Kadaster_(Nederland)"
    publisher: "Wikipedia"
    accessed: "2026-08-27"
---

# Kadaster

> **Verified 2026-08-27.** Three of five cited pages read directly, with
> Wikipedia added as a replacement source for two confirmed-dead originals:
> digitaleoverheid.nl's BRK page is bot-walled and NORA Online's BRK wiki
> page returns HTTP 404. Wikipedia, read directly, adds the founding date
> (1 October 1832, as Dienst voor het kadaster en de openbare registers) and
> confirms zelfstandig-bestuursorgaan status since 1994, neither of which
> the entity carried before.
>
> **Closed 2026-09-06**: the 1994 autonomisation now has a primary
> statutory citation — [[NL-ORGANISATIEWET-KADASTER]], read directly on
> wetten.overheid.nl, giving this entity its first `governed-by` edge.

## Description

The Kadaster is the Dutch cadastre, land registry and mapping agency,
founded on **1 October 1832** as the Dienst voor het kadaster en de openbare
registers — confirmed by reading nl.wikipedia.org's own article directly
this pass — and a **zelfstandig bestuursorgaan** (independent administrative
body) since 1994. It holds the Basisregistratie Kadaster (BRK), one of the
registrations in the [[NL-BASISREGISTRATIES]]. The BRK comprises two
components: the cadastral registration and the cadastral map. The
registration covers cadastral objects (parcels and apartment rights),
ownership, mortgages, limited rights such as leasehold, superficies and
usufruct, and utility networks.

The Kadaster relates the BRK to other base registrations — the BAG
(addresses and buildings), the Handelsregister held by [[NL-KVK]], and the
BRP (persons) — which makes it a hub in the base-registry graph rather than
an isolated register holder.

It is also one of the funders of [[NL-GEONOVUM]]'s base programme,
connecting it to Dutch geo-standardisation.

## Relationships

- `governed-by` [[NL-ORGANISATIEWET-KADASTER]] — closed 2026-09-06.
- Participates in [[NL-BASISREGISTRATIES]] as holder of the BRK.
- Co-funder of [[NL-GEONOVUM]].

## Sources

Listed in frontmatter, three of five read directly this pass — the two
Kadaster registration pages and Wikipedia (added as a replacement source).
digitaleoverheid.nl's BRK page is confirmed genuinely bot-walled and NORA
Online's BRK wiki page is confirmed genuinely dead (HTTP 404); neither
was reachable this pass.
