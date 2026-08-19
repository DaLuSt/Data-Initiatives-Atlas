---
id: CZ-DIA
type: organisation
name: Digitální a informační agentura
alternative_names:
  - DIA
  - Digital and Information Agency
description: >
  Czech central administrative authority for electronic identification,
  trust services and public administration information systems, established
  by amendment 471/2022 to Act No 12/2020 with effect from 1 January 2023 and
  assuming full powers on 1 April 2023. Under the Act on data management and
  controlled access it is Czechia's single information point and the node
  connecting Czech data sources to the European data portal.

level: national
country: CZ
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - CZ
  - CZ-ZAKON-60-2026
relationships:
  - type: implements
    target: CZ-ZAKON-60-2026
    source: fact
    evidence: "Under the Act on data management and controlled access (No 60/2026 Sb.), a norm modernising Czech eGovernment, DIA serves as the single information point in the Czech Republic and becomes a node for communication with European structures, ensuring the connection of Czech data sources with the European data portal (dia.gov.cz 'Zákon o správě dat a řízeném přístupu otevírá cestu státu k efektivnímu rozhodování'; isvs.cz). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: part-of
    target: CZ
    source: fact
    evidence: "The Digitální a informační agentura is a Czech central administrative authority for electronic identification, trust-creating services and public administration information systems; it was established by amendment 471/2022 of Act No 12/2020 with effect from 1 January 2023 and assumed full powers on 1 April 2023 (dia.gov.cz; cs.wikipedia.org 'Digitální a informační agentura'). NOT READ — search-only. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Digitální a informační agentura"
    url: "https://www.dia.gov.cz/cs"
    publisher: "Digitální a informační agentura (DIA)"
  - title: "Zákon o správě dat a řízeném přístupu otevírá cestu státu k efektivnímu rozhodování"
    url: "https://www.dia.gov.cz/cs/aktuality/zakon-o-sprave-dat-a-rizenem-pristupu-otevira-cestu-statu-k-efektivnimu-rozhodovani"
    publisher: "Digitální a informační agentura (DIA)"
  - title: "Digitální a informační agentura"
    url: "https://cs.wikipedia.org/wiki/Digit%C3%A1ln%C3%AD_a_informa%C4%8Dn%C3%AD_agentura"
    publisher: "Wikipedie"
---

# Digitální a informační agentura

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

DIA is Czechia's **central administrative authority** for electronic
identification, trust services and public administration information
systems. It was established by **amendment 471/2022** to Act No 12/2020,
effective **1 January 2023**, and took full powers on **1 April 2023**.

## The single information point

Under [[CZ-ZAKON-60-2026]], DIA is Czechia's **single information point**
and the node connecting Czech data sources to the **European data portal**.

That is a specific institutional design the Atlas has not seen before: one
named body, in statute, as the state's data interface both inward and
outward. Compare the Dutch arrangement, where [[NL-IBDS]] is a strategy and
[[NL-FDS]] a system, and no single act names a body in this role.

The edge is `implements`, not `governed-by`. The act does not constitute DIA
— amendment 471/2022 to Act No 12/2020 did, three years earlier — it assigns
it a role, which DIA operationalises. The same distinction the Atlas draws
for [[PL-ABW]] and [[PL-NASK]] under [[PL-KSC]].

## Not modelled

- **Act No 12/2020** on the right to digital services, DIA's constituting
  statute.
- **Portál občana** and Czech electronic identification.

## Relationships

- `implements` [[CZ-ZAKON-60-2026]].
- `part-of` [[CZ]] — an anchor edge.

## Sources

Listed in frontmatter.
