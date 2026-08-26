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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - CZ
  - CZ-ZAKON-60-2026
  - CZ-DATA-GOV
relationships:
  - type: implements
    target: CZ-ZAKON-60-2026
    source: fact
    evidence: "Confirmed by reading dia.gov.cz's and isvs.cz's pages directly (2026-08-26): under the Act on data management and controlled access (No 60/2026 Sb.), DIA serves as Czechia's single information point and becomes a node for communication with European structures, connecting Czech data sources to the European data portal. isvs.cz further states DIA was the bill's own proposer — 'Předkladatelem zákona byla DIA' — and quotes DIA's director, Bohdan Urban, on the Act's aims."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: part-of
    target: CZ
    source: fact
    evidence: "Confirmed by reading cs.wikipedia.org's DIA article directly (2026-08-26): 'Agentura byla zřízena novelou 471/2022 Sb. zákona č. 12/2020 Sb., o právu na digitální služby k 1. lednu 2023 a plnou působnost přebrala od 1. dubna 2023' (the agency was established by amendment 471/2022 Sb. to Act No. 12/2020 Sb., on the right to digital services, with effect from 1 January 2023, and took over full authority from 1 April 2023) — matching this entity's existing claim exactly. Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Digitální a informační agentura"
    url: "https://www.dia.gov.cz/cs"
    publisher: "Digitální a informační agentura (DIA)"
    accessed: "2026-08-26"
  - title: "Zákon o správě dat a řízeném přístupu otevírá cestu státu k efektivnímu rozhodování"
    url: "https://www.dia.gov.cz/cs/aktuality/zakon-o-sprave-dat-a-rizenem-pristupu-otevira-cestu-statu-k-efektivnimu-rozhodovani"
    publisher: "Digitální a informační agentura (DIA)"
    accessed: "2026-08-26"
  - title: "Digitální a informační agentura"
    url: "https://cs.wikipedia.org/wiki/Digit%C3%A1ln%C3%AD_a_informa%C4%8Dn%C3%AD_agentura"
    publisher: "Wikipedie"
    accessed: "2026-08-26"
  - title: "DIA: Zákon o správě dat a řízeném přístupu otevírá cestu státu k efektivnímu rozhodování"
    url: "https://www.isvs.cz/dia-zakon-o-sprave-dat-a-rizenem-pristupu-otevira-cestu-statu-k-efektivnimu-rozhodovani/"
    publisher: "ISVS.CZ"
    accessed: "2026-08-26"
---

# Digitální a informační agentura

> **Verified 2026-08-26.** All four cited pages were read directly.
> isvs.cz revealed DIA was the sponsor of its own governing act, not
> merely the body it assigns a role to, and named DIA's director. A new
> `maintained-by` edge onto [[CZ-DATA-GOV]] closes a custodian gap
> found on the platform side this pass.

## Description

DIA is Czechia's **central administrative authority** for electronic
identification, trust services and public administration information
systems, headed by director **Bohdan Urban**. It was established by
**amendment 471/2022** to Act No 12/2020, effective **1 January 2023**,
and took full powers on **1 April 2023**. Confirmed by reading
cs.wikipedia.org directly, DIA also manages the basic-registers
information system, CzechPOINT, and the Portál občana citizen portal.

## The single information point — and the act's own author

Under [[CZ-ZAKON-60-2026]], DIA is Czechia's **single information point**
and the node connecting Czech data sources to the **European data portal**.
Confirmed by reading isvs.cz directly, DIA was also the bill's own
proposer ("Předkladatelem zákona byla DIA"), and its director is quoted
describing the Act's aims — DIA did not just receive this role, it
drafted the statute that assigns it.

That is a specific institutional design the Atlas has not seen before: one
named body, in statute, as the state's data interface both inward and
outward. Compare the Dutch arrangement, where [[NL-IBDS]] is a strategy and
[[NL-FDS]] a system, and no single act names a body in this role.

The edge is `implements`, not `governed-by`. The act does not constitute DIA
— amendment 471/2022 to Act No 12/2020 did, three years earlier — it assigns
it a role, which DIA operationalises. The same distinction the Atlas draws
for [[PL-ABW]] and [[PL-NASK]] under [[PL-KSC]].

## Also the custodian of data.gov.cz

DIA's own project page, read directly, names its work developing
[[CZ-DATA-GOV]] (NKOD) directly, and isvs.cz confirms DIA will formally
administer its 2028–2029 successor, the National Data Catalogue —
closing a custodian gap that entity had flagged since creation.

## Not modelled

- **Act No 12/2020** on the right to digital services, DIA's constituting
  statute.
- **Portál občana** and Czech electronic identification, though both are
  now named in this entity's own description.

## Relationships

- `implements` [[CZ-ZAKON-60-2026]].
- `part-of` [[CZ]] — an anchor edge.
- Operates [[CZ-DATA-GOV]] — the `maintained-by` edge lives on that
  entity, pointing here.

## Sources

Listed in frontmatter, all four read directly this pass.
