---
id: NL-EAR
type: framework
name: Enterprise Architectuur Rijksdienst
alternative_names:
  - EAR
description: >
  Enterprise architecture for the Dutch central government, addressing the
  organisation of information provision for the Concern Rijksdienst and
  describing both the current situation and the intended future arrangement.
  Succeeded from 2024 by the RijksOverheid Referentie Architectuur (RORA).

level: national
country: NL
region: null

status: superseded
confidence: low
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: NL-RORA

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-NORA
  - NL-RORA
relationships:
  - type: based-on
    target: NL-NORA
    source: fact
    evidence: "NORA has daughter architectures (NORA dochters) from government domains, including EAR for central government, GEMMA for municipalities, PETRA for the provinces and WILMA for the water boards, alongside domain and chain architectures such as ROSA for education, KARWEI for work and income and SRK for the criminal justice chain (noraonline.nl/wiki/NORA_dochters; noraonline.nl/wiki/Visie_op_dochters; nl.wikipedia.org 'Nederlandse Overheid Referentie Architectuur'). NOT READ — search-only. This entity is EAR, the central-government architecture, named in that list."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Wat is de Enterprise Architectuur Rijksdienst"
    url: "https://www.earonline.nl/index.php/Wat_is_de_Enterprise_Architectuur_Rijksdienst"
    publisher: "EAR Online"
  - title: "Beheermodel Enterprise Architectuur Rijksdienst"
    url: "https://www.earonline.nl/index.php/Beheermodel_Enterprise_Architectuur_Rijksdienst"
    publisher: "EAR Online"
---

# EAR (Enterprise Architectuur Rijksdienst)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The EAR addressed the organisation of information provision within the
Dutch central government, describing both the existing situation and the
intended future arrangement of information provision for the Concern
Rijksdienst. It sat alongside [[NL-GEMMA]] (municipalities) and
[[NL-PETRA]] (provinces) as the central-government member of the Dutch
reference-architecture family.

Search results state that since 2024 [[NL-RORA]] (RijksOverheid Referentie
Architectuur) has become the successor to the EAR. `status: superseded` is
recorded on that basis, with `successor` set accordingly.

`coverage: low`: the EAR's own content, its start date, and the exact date
and mechanism of the transition to RORA were not established. Note that
earonline.nl still appears to be live while roraonline.nl describes itself as
the EAR knowledge base — the relationship between the two sites is unclear
and is recorded in `discovery/unresolved.md`. Status here follows a
positive statement of succession, not an inference from site availability.

## Relationships

- Superseded by [[NL-RORA]] (recorded on that entity).
- Part of the reference-architecture family descending from [[NL-NORA]];
  the formal derivation was not sourced and is therefore not asserted.

## Sources

Listed in frontmatter.
