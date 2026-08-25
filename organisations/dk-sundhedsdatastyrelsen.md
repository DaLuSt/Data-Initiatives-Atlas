---
id: DK-SUNDHEDSDATASTYRELSEN
type: organisation
name: Sundhedsdatastyrelsen
alternative_names:
  - Danish Health Data Authority
description: >
  Danish authority responsible for the national health registers, which hold
  data on the health of the entire Danish population and on the services of
  the healthcare system. It was established in November 2015 and is part of
  the Ministry of the Interior and Health. Its Research Services provide access
  to register data through the Secure Research Platform, which gives remote
  online access in a controlled environment. The National Patient Register is
  the largest collection of healthcare data in Denmark, covering examinations
  and treatments in Danish hospitals over the last forty years.

level: national
country: DK
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2015-11-01
end_date: null
last_verified: "2026-08-25"
previous_version: null
successor: null

domains:
  - DOMAIN-HEALTH
organisations: []
related_entities:
  - DK
  - EU-EHDS
relationships:
  - type: part-of
    target: DK
    source: fact
    evidence: "Confirmed verbatim by reading english.sundhedsdatastyrelsen.dk directly (2026-08-25): 'The Danish Health Data Authority is a part of the Ministry of the Interior and Health and was established in November 2015,' and, on its national-health-registers page, 'The Danish Health Data Authority is responsible for the national health registers that contain data related to the health of the entire Danish population and the services of the healthcare system' — matching this entity's evidence word for word."
    confidence: medium
    valid_from: 2015-11-01
    valid_until: null

sources:
  - title: "About the Danish Health Data Authority"
    url: "https://english.sundhedsdatastyrelsen.dk/about-us"
    publisher: "Sundhedsdatastyrelsen — Danish Health Data Authority"
    accessed: "2026-08-25"
  - title: "National health registers"
    url: "https://english.sundhedsdatastyrelsen.dk/health-data-and-registers/national-health-registers"
    publisher: "Sundhedsdatastyrelsen — Danish Health Data Authority"
    accessed: "2026-08-25"
  - title: "Research Services"
    url: "https://english.sundhedsdatastyrelsen.dk/health-data-and-registers/research-services"
    publisher: "Sundhedsdatastyrelsen — Danish Health Data Authority"
    accessed: "2026-08-25"
---

# Sundhedsdatastyrelsen

> **Verified 2026-08-25.** All three cited pages were read directly and
> confirm the authority's identity, its November 2015 establishment,
> and its role over the national health registers word for word.

## Description

The Danish authority responsible for the **national health registers**,
established **November 2015** and part of the **Ministry of the Interior and
Health**. Health data is registered at the GP, the hospital, the specialist,
the pharmacy and the municipality, and is collected in those registers.

The **National Patient Register** is the largest collection of healthcare data
in Denmark, covering examinations and treatments in Danish hospitals over the
last **forty years**.

**Research Services** provides access through the **Secure Research
Platform** — remote online access to register data in a controlled
environment.

## The custodian model

Denmark is the third of the three shapes described on
[[FR-HEALTH-DATA-HUB]]: the authority **holds the registers itself** and
provides researchers a controlled environment to work inside, rather than
pooling members ([[FR-HEALTH-DATA-HUB]]) or licensing access to data others
hold ([[FI-FINDATA]]).

It also fits the pattern [[DK]] already shows elsewhere in the Atlas.
`discovery/research-queue.md` records that Klimadatastyrelsen operates
[[DK-DATAFORDELER]] as *"the single channel through which all Danish basic
data is distributed"* — *"the Danish counterpart of the ten Dutch register
holders collapsed into one body"*. Danish data governance concentrates where
the Dutch distributes, and health is the second instance of it.

## Relationships

- `part-of` [[DK]] — anchor edge, and literally true: the authority is part
  of a ministry.

## What is not modelled

The **National Patient Register** and the **Secure Research Platform** are
both named here without entities. The register is the more significant
omission — it is the largest health dataset in the country and the Atlas
models ten Dutch basisregistraties individually.

## Sources

Listed in frontmatter — three pages of the authority's own English
site, all read directly this pass.
