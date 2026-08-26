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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-26"
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
    evidence: "Confirmed by reading data.gouv.fr's own organisation page for Etalab directly (2026-08-26): 'Etalab est un département de la direction interministérielle du numérique (DINUM)' which 'administre' the portal — corroborated by data.gouv.fr's own homepage, read directly, which describes the platform as 'La plateforme des données publiques françaises' (the French public-data platform), 'Utilisez, partagez et améliorez les données publiques' (use, share and improve public data), matching this entity's description. fr.wikipedia.org's Etalab page, read independently, confirms the same administering relationship."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "data.gouv.fr — plateforme ouverte des données publiques françaises"
    url: "https://www.data.gouv.fr/"
    publisher: "Etalab / DINUM"
    accessed: "2026-08-26"
  - title: "Organisation — Etalab | data.gouv.fr"
    url: "https://www.data.gouv.fr/organizations/etalab/datasets"
    publisher: "data.gouv.fr"
    accessed: "2026-08-26"
  - title: "Etalab"
    url: "https://fr.wikipedia.org/wiki/Etalab"
    publisher: "Wikipédia"
    accessed: "2026-08-26"
  - title: "Chronologie juridique de l'open data"
    url: "https://guides.data.gouv.fr/guides/guide-juridique/chronologie-de-lopen-data"
    publisher: "data.gouv.fr"
    accessed: "2026-08-26"
---

# data.gouv.fr

> **Verified 2026-08-26.** All four cited pages were read directly.
> data.gouv.fr's own homepage confirms its identity verbatim, and its
> Etalab organisation page confirms the `maintained-by` edge directly.

## Description

Confirmed by reading data.gouv.fr directly (2026-08-26): "La plateforme
des données publiques françaises. Utilisez, partagez et améliorez les
données publiques" (the French public-data platform; use, share and
improve public data) — the interministerial portal for downloading,
sharing and reusing the data of the state and of territorial
authorities.

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

- **No DCAT profile — and searching for one has now been done.** France has
  no `FR-DCAT-AP-FR` entity, unlike the Dutch, German and Belgian layers.
  The third research-queue batch went looking, and the finding is negative:
  what the sources describe is France being measured on **conformity with
  DCAT-AP itself** — the European profile — and data.gouv.fr supporting
  DCAT harvesting, not a French application profile sitting between the two.
  The DCAT fork stays at three national children plus Spain's, which is
  folded into [[ES-NTI-RISP]] rather than standing alone. The queue item is
  closed as "no such profile found", not carried.
- **No relationship to [[FR-LRN]]**, though the 2016 act's open-data
  obligations are what much of this portal carries. Same call as
  [[DE-GOVDATA]]/[[DE-DNG]] and [[BE-DATA-GOV-BE]]/[[BE-HERGEBRUIK-WET]]:
  obviously related, nowhere stated.

## Relationships

- Maintained by [[FR-ETALAB]].

## Sources

Listed in frontmatter, all four read directly this pass.
