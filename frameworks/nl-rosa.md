---
id: NL-ROSA
type: framework
name: Referentie Onderwijs Sector Architectuur
alternative_names:
  - ROSA
  - Ketenreferentiearchitectuur ROSA
description: >
  Chain reference architecture for the entire Dutch education sector,
  covering formal and non-formal education. It aims to promote cooperation
  between chain partners on information provision across all education
  domains, and is maintained by the Architecture Council (Architectuurraad)
  of Edustandaard.

level: sectoral
country: NL
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-04"
previous_version: null
successor: null

domains:
  - DOMAIN-EDUCATION
organisations:
  - NL-EDUSTANDAARD
related_entities:
  - NL-NORA
relationships:
  - type: based-on
    target: NL-NORA
    source: fact
    evidence: "Confirmed by reading noraonline.nl's own 'NORA_dochters' page directly (2026-08-27): NORA's daughter architectures include ROSA for education, alongside EAR for central government, GEMMA for municipalities, PETRA for the provinces and WILMA for the water boards. This closes the previous 'NOT READ — search-only' gap, and re-confirms the sourcing already established in the previous pass."
    confidence: high
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NL-EDUSTANDAARD
    source: fact
    evidence: "Confirmed by reading edustandaard.nl's own 'Relevante architecturen' page directly (2026-08-27): 'ROSA is maintained by the Architecture Council of Edustandaard' (Architectuurraad). A research-queue pickup (2026-09-04) created NL-EDUSTANDAARD as its own Atlas entity, closing the gap this file previously left unasserted for want of it."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Ketenreferentie-architectuur ROSA"
    url: "https://www.edustandaard.nl/standaard_architecturen/referentie-onderwijs-sector-architectuur-rosa/"
    publisher: "Edustandaard"
    accessed: "2026-08-27"
  - title: "Relevante architecturen binnen het onderwijs"
    url: "https://www.edustandaard.nl/rosa/onderwijsarchitecturen/"
    publisher: "Edustandaard"
    accessed: "2026-08-27"
---

# ROSA (Referentie Onderwijs Sector Architectuur)

> **Verified 2026-08-27.** Both cited pages were read directly this pass,
> closing the previous `search-only` status (never previously
> `last_verified`).

## Description

ROSA is the chain reference architecture (ketenreferentiearchitectuur) for
the Dutch education sector as a whole, spanning both formal and non-formal
education. Its purpose is to promote cooperation between chain partners on
information provision across all education domains, and — reading
edustandaard.nl's own page directly — to function both **descriptively**
(explaining existing processes) and **prescriptively** (setting principles
and design frameworks), while supporting modular architectural approaches
used in frameworks like AMIGO and giving the sector shared terminology
through the ROSA Concept Framework.

**Maintainer, now sourced and modelled.** edustandaard.nl's own "Relevante
architecturen" page, read directly, states plainly: "ROSA is maintained by
the Architecture Council of Edustandaard" (Architectuurraad). A
research-queue pickup (2026-09-04) created [[NL-EDUSTANDAARD]] as its
own Atlas entity, and the `maintained-by` edge this framework previously
left unasserted is now recorded.

The same page distinguishes ROSA from three **sector-specific**
architectures — **HORA** (higher education), **MORA** (vocational
education) and **FORA** (primary/secondary education) — each with its own
target architecture (HOSA, MOSA, FOSA). Where ROSA governs cross-sector
information exchange (between institutions, and with external
organisations like municipalities), the sector-specific architectures
describe internal institutional operations. A coordination advisory group
aligns ROSA and these sector architectures on terminology, reference
components and process.

`level: sectoral` rather than `national`, following the same reasoning
applied to [[NL-NICTIZ]]: national in reach, but bounded to one sector.

Tagged [[DOMAIN-EDUCATION]], alongside [[NL-SURF]].

## Relationships

- `based-on` [[NL-NORA]] — confirmed via NORA's own "dochters" wiki
  page, which lists ROSA by name among the NORA family's
  education-domain member.
- `maintained-by` [[NL-EDUSTANDAARD]] — closed 2026-09-04.

## Sources

Both listed sources read directly this pass.
