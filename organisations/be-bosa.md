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
last_verified: "2026-08-27"
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
    accessed: "2026-08-26"
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
  - title: "Koninklijk besluit van 22 februari 2017 houdende oprichting van de Federale Overheidsdienst Beleid en Ondersteuning"
    url: "https://etaamb.openjustice.be/nl/koninklijk-besluit-van-22-februari-2017_n2017010836.html"
    publisher: "etaamb / OpenJustice (Belgisch Staatsblad)"
    accessed: "2026-08-26"
---

# FOD BOSA — Federale Overheidsdienst Beleid en Ondersteuning

> **Re-checked 2026-08-27, still `search-only`.** All three `bosa.belgium.be`
> pages and the `news.belgium.be` page remain genuinely bot-walled
> (CAPTCHA/403) even with an honest User-Agent. This pass tried three
> further routes to BOSA's own voice — `dtservices.bosa.be` (301-redirects
> to a blocked `bosa.belgium.be` search page), `fedweb.belgium.be`
> (301-redirects to the same blocked domain), and `digitall.be` (403) —
> all dead ends, confirming the block is comprehensive rather than
> page-specific. Two of six is still not a majority, so this entity stays
> `search-only` despite genuine additional effort this pass.

## Description

BOSA is the Belgian federal public service for policy and support,
**established on 1 March 2017**, by **Royal Decree of 22 February 2017** —
confirmed by reading the decree's own text directly this pass. It provides
the federal government's supporting services — HR, ICT, communication,
budget and accounting — and supports its users and policymakers across five
domains: working in the public sector, **digital government and
administrative simplification**, budget and accounting, public procurement,
and strategic support.

Its **Directorate-General for Digital Transformation (DG DT)** is the part
within the Atlas's scope — confirmed as one of six directorates-general
under Article 4 of the founding decree. DG DT runs the federal ICT
framework contracts and operates [[BE-DATA-GOV-BE]], the federal open data
portal, including its metadata integration services.

The founding decree itself confirms BOSA was formed by merging **FOD
Personeel en Organisatie, FOD Budget en Beheerscontrole and Fedict**, with
**Selor and Empreva**'s functions integrated too — a fuller and slightly
different list of predecessors than Wikipedia gives, which names all five
but frames the merger loosely. The decree's Article 2 lists 35 functions
across personnel, budget, digital transformation, procurement and
health-and-safety — corroborating the "five domains" framing without using
that exact structure.

The **Dienst Administratieve Vereenvoudiging** (administrative
simplification service) was integrated into BOSA, and **Nido** is its
innovation lab — neither confirmed independently this pass.

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

Two of six read directly this pass (both from the prior pass) — Wikipedia
and the founding Royal Decree of 22 February 2017 at
etaamb.openjustice.be. All three `bosa.belgium.be` pages and the
`news.belgium.be` page returned CAPTCHA challenges rather than content;
the same wall was found on `ccb.belgium.be`, `data.gov.be`,
`financien.belgium.be` and `statbel.fgov.be` across this batch.
`dtservices.bosa.be` and `fedweb.belgium.be` both 301-redirect into the
same blocked `bosa.belgium.be` domain, and `digitall.be` returned 403 —
three further routes tried this pass, none successful.
