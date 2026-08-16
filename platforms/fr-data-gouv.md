---
id: FR-DATA-GOUV
type: platform
name: data.gouv.fr
alternative_names:
  - Plateforme ouverte des données publiques françaises
description: >
  France's open data platform, the interministerial portal for downloading,
  sharing and reusing the data of the state and territorial authorities. It
  is administered by Etalab and intended to gather and freely provide the
  public information of the state, its public establishments, and — where
  they wish — territorial authorities and bodies charged with a public
  service mission.

level: national
country: FR
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
organisations:
  - FR-ETALAB
related_entities:
  - FR-LRN
  - NL-DATA-OVERHEID
  - DE-GOVDATA
  - BE-DATA-GOV-BE
relationships:
  - type: maintained-by
    target: FR-ETALAB
    source: fact
    evidence: "Etalab administers the interministerial portal data.gouv.fr, intended to gather and freely provide all public information of the state, its public establishments and, if they wish, territorial authorities and public or private law bodies charged with a public service mission (fr.wikipedia.org 'Etalab'; data.gouv.fr organisation pages). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "data.gouv.fr — plateforme ouverte des données publiques françaises"
    url: "https://www.data.gouv.fr/"
    publisher: "Etalab / DINUM"
  - title: "Organisation — Etalab | data.gouv.fr"
    url: "https://www.data.gouv.fr/organizations/etalab/datasets"
    publisher: "data.gouv.fr"
  - title: "Chronologie juridique de l'open data"
    url: "https://guides.data.gouv.fr/guides/guide-juridique/chronologie-de-lopen-data"
    publisher: "data.gouv.fr"
  - title: "Etalab"
    url: "https://fr.wikipedia.org/wiki/Etalab"
    publisher: "Wikipédia"
---

# data.gouv.fr

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

data.gouv.fr is the French open data platform — the interministerial portal
for downloading, sharing and reusing the data of the state and of
territorial authorities.

[[FR-ETALAB]] administers it. Its intended scope is the public information
of **the state, its public establishments**, and — **where they wish** —
territorial authorities and public or private bodies charged with a public
service mission.

That "where they wish" is worth noticing: even in the Atlas's most
centralised country, the national portal's reach into sub-national
government is **voluntary**.

## Four national open data portals

| Country | Portal | Institutional basis | Custodian |
|---|---|---|---|
| France | **data.gouv.fr** | administered by a **department of** the central digital body | [[FR-ETALAB]] |
| Belgium | [[BE-DATA-GOV-BE]] | managed by a federal support service | [[BE-BOSA]] |
| Germany | [[DE-GOVDATA]] | a **Verwaltungsvereinbarung** signed by the federation and all sixteen Länder | [[DE-FITKO]] |
| Netherlands | [[NL-DATA-OVERHEID]] | an ordinary central government service | **none modelled** |

The German entity observed that the same function needs an interstate
agreement in one country and a plain government service in another. With
four countries the pattern is clearer: **the institutional weight of the
portal tracks the constitutional structure of the state**, from a
department inside a Prime Minister's directorate (France) to a treaty-like
agreement among seventeen governments (Germany).

That is a real comparative finding, and it is only visible because the
Atlas records four countries against one shared ontology. **No relationship
between the four portals is asserted.**

The Dutch cell is a gap rather than a finding — see [[FR-ETALAB]].

## What is not recorded

- **No DCAT profile.** France has no `FR-DCAT-AP-FR` entity, unlike the
  Dutch, German and Belgian layers, because **no source read establishes
  one**. data.gouv.fr certainly exposes DCAT — the European portal harvests
  it — but the Atlas does not record what it has not seen stated. This
  breaks the three-way DCAT fork at three rather than four, and is queued.
- **No relationship to [[FR-LRN]]**, though the 2016 act's open-data
  obligations are what much of this portal carries. Same call as
  [[DE-GOVDATA]]/[[DE-DNG]] and [[BE-DATA-GOV-BE]]/[[BE-HERGEBRUIK-WET]]:
  obviously related, nowhere stated.

## Relationships

- Maintained by [[FR-ETALAB]].

## Sources

Listed in frontmatter.
