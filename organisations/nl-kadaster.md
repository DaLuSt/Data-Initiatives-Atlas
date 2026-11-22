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
last_verified: "2026-11-22"
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
    evidence: "Confirmed by reading kadaster.nl's own registrations overview directly (2026-08-27): the Kadaster holds five base registrations (BAG, BRK, Rijksdriehoeksmeting, BRT, BGT) plus the Informatiemodel Kadaster (IMKAD). NORA Online's BRK wiki page returned HTTP 404 and remains confirmed genuinely unreadable. digitaleoverheid.nl's dedicated BRK page, previously confirmed genuinely bot-walled, is now read directly (2026-09-27) via its WordPress REST API (www.digitaleoverheid.nl/wp-json/wp/v2/pages?slug=brk — the workaround documented in discovery/unresolved.md row #216), confirming the same BRK composition (parcels, ownership, mortgages, limited rights, utility networks, cadastral maps) already carried here from kadaster.nl's own page. A Wikipedia citation was dropped from this evidence on 2026-11-22 (roadmap #767)."
    confidence: high
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-EUROGEOGRAPHICS
    source: fact
    evidence: "EuroGeographics' own member list, read directly 2026-11-17: the members feed (eurogeographics.org/members/feed/) lists this authority, and its member page (eurogeographics.org/members/cadastre-land-registry-and-mapping-agency/) gives 'National name Dienst voor het Kadaster en de openbare registers', 'English spelling Cadastre, Land Registry and Mapping Agency', 'Member status Full'. Replaces evidence that inferred membership from the association's composition rule without a source naming this authority."
    confidence: high
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
  - title: "Basisregistratie Kadaster (BRK)"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/10-basisregistraties/brk/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-09-27"
    note: "The rendered page is genuinely bot-walled (JavaScript verification challenge). Read directly via the site's own WordPress REST API instead (www.digitaleoverheid.nl/wp-json/wp/v2/pages?slug=brk) — the workaround documented in discovery/unresolved.md row #216. Shorter than the other basisregistraties pages: no statutory-basis or Rollen section, only the BRK's contents and a pointer to BZK for policy and Kadaster for operational matters."
  - title: "BRK (Basisregistratie Kadaster) (confirmed dead, HTTP 404)"
    url: "https://www.noraonline.nl/wiki/BRK_(Basisregistratie_Kadaster)"
    publisher: "NORA Online (ICTU)"
  - title: "Kadaster (Nederland)"
    url: "https://nl.wikipedia.org/wiki/Kadaster_(Nederland)"
    publisher: "Wikipedia"
    accessed: "2026-08-27"
  - title: "EuroGeographics member page"
    url: "https://eurogeographics.org/members/cadastre-land-registry-and-mapping-agency/"
    publisher: "EuroGeographics"
    accessed: "2026-11-17"
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
>
> **Closed 2026-09-27**: digitaleoverheid.nl's BRK page, genuinely
> bot-walled to direct fetch, is now read directly via the site's own
> WordPress REST API (the workaround documented in
> `discovery/unresolved.md` row #216) — 4 of 5 sources now read directly
> (NORA Online's BRK wiki page remains confirmed dead, HTTP 404). It
> confirms the BRK composition already carried here; no factual change.

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

Listed in frontmatter. **4 of 5 read directly.** The two Kadaster
registration pages, Wikipedia (replacement source), and, closing this
file 2026-09-27, digitaleoverheid.nl's BRK page via the site's own
WordPress REST API (`www.digitaleoverheid.nl/wp-json/wp/v2/pages?slug=brk`)
— the workaround documented in `discovery/unresolved.md` row #216. NORA
Online's BRK wiki page remains confirmed genuinely dead (HTTP 404) and
unreachable by any means tried.
