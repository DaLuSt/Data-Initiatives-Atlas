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
last_verified: "2026-09-18"
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
  - title: "Les différents types de moissonneurs (harvesting/DCAT documentation)"
    url: "https://guides.data.gouv.fr/moissonnage/comprendre-le-moissonnage/les-differents-type-de-moissonneurs"
    publisher: "data.gouv.fr"
    accessed: "2026-09-06"
  - title: "Quelles sont les obligations ? (legal guide for data producers)"
    url: "https://guides.data.gouv.fr/guides/guide-juridique/producteurs-de-donnees/quelles-sont-les-obligations"
    publisher: "data.gouv.fr"
    accessed: "2026-09-18"
---

# data.gouv.fr

> **Verified 2026-08-26; DCAT-profile negative independently corroborated
> 2026-09-06.** All four originally-cited pages were read directly.
> data.gouv.fr's own homepage confirms its identity verbatim, and its
> Etalab organisation page confirms the `maintained-by` edge directly.
>
> **Closed 2026-09-18** (`discovery/unresolved.md` row #76): the
> "obviously related, nowhere stated" question about [[FR-LRN]] is
> answered, but not as expected — see "The LRN link, refined rather than
> confirmed" below.

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
  closed as "no such profile found", not carried. **Independently
  corroborated 2026-09-06**: guides.data.gouv.fr's own harvesting
  documentation, read directly, names only "DCAT et... l'extension DCAT-AP
  publiée par la Commission européenne" plus GeoDCAT-AP for geographic
  data — no French-specific profile. This directly contradicts an
  uncorroborated askem.eu blog claim (found by search, not read from a
  primary page) that "France has its own derived profile" adding
  SIREN/administrative-nomenclature fields; that claim is not adopted.
- ~~No relationship to [[FR-LRN]]~~ — refined 2026-09-18, see below.

## The LRN link, refined rather than confirmed — 2026-09-18

`discovery/unresolved.md` row #76 asked the same question already asked
of [[DE-GOVDATA]]/[[DE-DNG]] and [[BE-DATA-GOV-BE]]/[[BE-HERGEBRUIK-WET]]:
the portal and the national open-data act look obviously related, but
nowhere was it stated.

data.gouv.fr's own legal guide for data producers, "Quelles sont les
obligations ?", read directly, answers it — and corrects the assumption
behind the question rather than confirming it. The platform's own
designation as *"portail unique interministériel destiné à rassembler et
à mettre à disposition les informations publiques"* rests on **Article
R. 321-8 of the Code des relations entre le public et l'administration
(CRPA)**, plus circulars of 26 May 2011 and 27 April 2021 — not on
[[FR-LRN]] itself. [[FR-LRN]]'s own file already independently sourced
its open-data obligations to a *different* article of the same code,
**L312-1-1 et seq. of the CRPA** (via decideo.fr).

So the two are related, but not directly: both sit inside the CRPA, at
different articles serving different functions — L312-1-1 imposes the
open-data-by-default obligation on public bodies, R. 321-8 designates
this platform as where reference data is made available. No source
states that the LRN itself designates data.gouv.fr, so no
`implements-requirement-from` or similar edge is added — the same
caution [[FR-LRN]]'s own file already applies (Nor is any edge asserted
to [[FR-DATA-GOUV]]). What has changed is that "obviously related,
nowhere stated" is now "related through a shared code at two distinct
articles, neither stating the other."

## Relationships

- Maintained by [[FR-ETALAB]].

## Sources

Listed in frontmatter. The first four read directly in the 2026-08-26
pass; the legal-obligations guide, added 2026-09-18, read directly.
