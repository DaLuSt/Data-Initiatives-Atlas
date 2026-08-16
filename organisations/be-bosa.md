---
id: BE-BOSA
type: organisation
name: FOD Beleid en Ondersteuning
alternative_names:
  - BOSA
  - SPF Stratégie et Appui
  - FOD BOSA
  - DG Digitale Transformatie
description: >
  Belgian federal public service for policy and support, established on
  1 March 2017, responsible for the federal government's supporting
  services including HR, ICT, communication, budget and accounting. Its
  Directorate-General for Digital Transformation carries federal digital
  government and administrative simplification, and it operates the federal
  open data portal.

level: national
country: BE
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2017-03-01
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - BE-DATA-GOV-BE
relationships: []

sources:
  - title: "Federale Overheidsdienst Beleid en Ondersteuning"
    url: "https://nl.wikipedia.org/wiki/Federale_Overheidsdienst_Beleid_en_Ondersteuning"
    publisher: "Wikipedia"
  - title: "Federale open data portaal"
    url: "https://bosa.belgium.be/nl/applications/federale-open-data-portaal"
    publisher: "FOD Beleid en Ondersteuning (BOSA)"
  - title: "Federale open data portaal: integratie metadata"
    url: "https://bosa.belgium.be/nl/services/federale-open-data-portaal-integratie-metadata"
    publisher: "FOD Beleid en Ondersteuning (BOSA)"
  - title: "Integratie Metadata | DG DT"
    url: "https://dtservices.bosa.be/nl/services/open-data/integratie-metadata"
    publisher: "FOD BOSA — DG Digitale Transformatie"
  - title: "Integratie van de Dienst Administratieve Vereenvoudiging (DAV) in de FOD Beleid en Ondersteuning (BOSA)"
    url: "https://news.belgium.be/nl/integratie-van-de-dienst-administratieve-vereenvoudiging-dav-de-fod-beleid-en-ondersteuning-bosa"
    publisher: "news.belgium.be (Belgian federal government)"
---

# FOD BOSA — Federale Overheidsdienst Beleid en Ondersteuning

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

BOSA is the Belgian federal public service for policy and support,
**established on 1 March 2017**. It provides the federal government's
supporting services — HR, ICT, communication, budget and accounting — and
supports its users and policymakers across five domains: working in the
public sector, **digital government and administrative simplification**,
budget and accounting, public procurement, and strategic support.

Its **Directorate-General for Digital Transformation (DG DT)** is the part
within the Atlas's scope. DG DT runs the federal ICT framework contracts
and operates [[BE-DATA-GOV-BE]], the federal open data portal, including
its metadata integration services.

The **Dienst Administratieve Vereenvoudiging** (administrative
simplification service) was integrated into BOSA, and **Nido** is its
innovation lab.

## The federal counterpart to two entities elsewhere in the Atlas

BOSA occupies roughly the position [[NL-LOGIUS]] holds in the Dutch layer
and [[DE-BMDS]] in the German one: the central body running government
digital services and the open data portal. **No relationship to either is
asserted** — the resemblance is functional, and the three are constituted
very differently (a Dutch executive agency, a German ministry, a Belgian
horizontal support service).

## ⚠ Scope caveat: this is the *federal* service only

BOSA is a **federal** public service. It does not act for the Regions or
Communities, which run their own digital administrations — Digitaal
Vlaanderen, the Agence du Numérique, Paradigm — none of which is an Atlas
entity, because the `level` vocabulary has no term for them.

A reader seeing `country: BE` plus "central digital government body" would
over-read this entity's reach. The same caveat applies to [[DE-BFDI]] in
Germany, and the Belgian case is sharper: see `countries/be/be.md`.

## Relationships

**None asserted from this entity.** It is reached from
[[BE-DATA-GOV-BE]], which is `maintained-by` BOSA.

A `produces` link to [[BE-BELGIF]] was considered and **refused**: BELGIF
is sourced as a collaborative effort of the federal state, the Regions and
the Communities with several public administrations, which is precisely
*not* something BOSA owns.

## Sources

Listed in frontmatter. Note the first is Wikipedia — it carries the
establishment date and the five domains, which no bosa.belgium.be page
returned by search stated directly.
