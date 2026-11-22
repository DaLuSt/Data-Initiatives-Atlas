---
id: CZ-DIA
type: organisation
name: Digitální a informační agentura
name_en: "Digital and Information Agency"
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
last_verified: "2026-11-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - CZ
  - CZ-ZAKON-60-2026
  - CZ-ZAKON-12-2020
  - CZ-DATA-GOV
relationships:
  - type: governed-by
    target: CZ-ZAKON-12-2020
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP (discovery/unresolved.md row #185). Act No. 12/2020 Sb., as amended by Act No. 471/2022 Sb., read directly 2026-11-22 on zakonyprolidi.cz: § 2a(1) establishes the Agency and § 2a(3) gives it its tasks, among them 'a) plní koordinační úlohu v oblasti digitálních služeb a digitálních úkonů podle tohoto zákona' and 'c) plní koordinační úlohu v oblasti evidence a sdílení dat'. The original 2020 Act is [[CZ-ZAKON-12-2020]], read via psp.cz's legislative record (2026-09-12); amendment 471/2022 is not separately modelled. Replaces an encyclopedia citation (roadmap #767)."
    confidence: high
    valid_from: 2023-01-01
    valid_until: null
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
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. Act No. 12/2020 Sb., § 2a, read directly 2026-11-22 on zakonyprolidi.cz: '(1) Zřizuje se Digitální a informační agentura (dále jen „Agentura“) se sídlem v Praze. (2) Agentura je ústředním správním úřadem pro elektronickou identifikaci a služby vytvářející důvěru a pro informační systémy veřejné správy.' A central administrative authority of the Czech State. The transitional provisions of amendment 471/2022 Sb., on the same page, say the Ministry of the Interior exercised its competences until 31 March 2023. The 1 January 2023 effective date came from an encyclopedia article and is not relied on (roadmap #767)."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Zákon č. 12/2020 Sb., o právu na digitální služby, § 2a and the transitional provisions of 471/2022 Sb. (zakonyprolidi.cz)"
    url: "https://www.zakonyprolidi.cz/cs/2020-12"
    publisher: "zakonyprolidi.cz (AION CS), text of the Sbírka zákonů"
    accessed: "2026-11-22"
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
>
> **Updated 2026-09-12**: Act No 12/2020, DIA's own constituting statute,
> is now [[CZ-ZAKON-12-2020]], closing `discovery/unresolved.md` row #185.

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

- **Portál občana** and Czech electronic identification, though both are
  now named in this entity's own description.

## Relationships

- `governed-by` [[CZ-ZAKON-12-2020]] — its constituting statute, added
  2026-09-12, closing row #185. Amendment 471/2022 to that Act, which
  actually inserted DIA's founding provisions, is not separately modelled.
- `implements` [[CZ-ZAKON-60-2026]].
- `part-of` [[CZ]] — an anchor edge.
- Operates [[CZ-DATA-GOV]] — the `maintained-by` edge lives on that
  entity, pointing here.

## Sources

Listed in frontmatter, all four read directly this pass.
