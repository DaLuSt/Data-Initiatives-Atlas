---
id: EU-DORA
type: regulation
name: Digital Operational Resilience Act
alternative_names:
  - DORA
  - Regulation (EU) 2022/2554
description: >
  Regulation (EU) 2022/2554 of 14 December 2022 on digital operational resilience for the financial sector, published
  in OJ L 333 of 27 December 2022. It sets uniform requirements for the security of the network and information systems
  of financial entities: ICT risk management, incident reporting, resilience testing, third-party risk, and an oversight
  framework for critical ICT third-party service providers run by the European Supervisory Authorities. It has applied
  since 17 January 2025.

level: regional
country: null
region: EU

status: active
rank: ordinary
confidence: high
coverage: medium
verification: primary-source

start_date: 2025-01-17
end_date: null
last_verified: "2026-11-14"
previous_version: null
successor: null

domains:
  - DOMAIN-FINANCE
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - EU-NIS2
  - EU-PSD2
  - FR-NIS2-LOI
relationships:
  - type: applies-in
    target: EU
    source: fact
    evidence: "The Regulation's text, read directly 2026-11-14 from the Publications Office (CELEX 32022R2554): Article 64, it enters into force on the twentieth day after publication, 'shall apply from 17 January 2025' and is 'binding in its entirety and directly applicable in all Member States'."
    confidence: high
    valid_from: 2025-01-17
    valid_until: null
  - type: references
    target: EU-NIS2
    source: fact
    evidence: "Article 1(2): 'In relation to financial entities identified as essential or important entities pursuant to national rules transposing Article 3 of Directive (EU) 2022/2555, this Regulation shall be considered a sector-specific Union legal act for the purposes of Article 4 of that Directive.' Read directly 2026-11-14."
    confidence: high
    valid_from: null
    valid_until: null
  - type: references
    target: EU-PSD2
    source: fact
    evidence: "Article 2(1)(b): the Regulation applies to 'payment institutions, including payment institutions exempted pursuant to Directive (EU) 2015/2366'. Read directly 2026-11-14."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Regulation (EU) 2022/2554 (Digital Operational Resilience Act), Official Journal text"
    url: "https://publications.europa.eu/resource/celex/32022R2554"
    publisher: "Publications Office of the European Union"
    accessed: "2026-11-14"
---

# Digital Operational Resilience Act (Regulation (EU) 2022/2554)

> **Created 2026-11-14** (roadmap #771). The Official Journal text was downloaded from the Publications Office and read
> directly: the title, Articles 1, 2(1) (points a to t), 31(1), 46 (opening) and 64. The rest was not read.

## What the text says

- **Title and dates.** "Regulation (EU) 2022/2554 of the European Parliament and of the Council of 14 December 2022 on
  digital operational resilience for the financial sector and amending Regulations (EC) No 1060/2009, (EU) No 648/2012,
  (EU) No 600/2014, (EU) No 909/2014 and (EU) 2016/1011", OJ L 333, 27.12.2022, p. 1. It applies from **17 January 2025**
  (Article 64).
- **Content** (Article 1(1)): requirements for financial entities on ICT risk management, the reporting of major
  ICT-related incidents, digital operational resilience testing, information sharing on cyber threats and the management
  of ICT third-party risk; requirements for contracts with ICT third-party service providers; an Oversight Framework for
  critical ICT third-party service providers; and rules on cooperation and enforcement by competent authorities.
- **Relation to NIS2** (Article 1(2)): for financial entities that are essential or important entities under the
  national rules transposing [[EU-NIS2]], this Regulation counts as the sector-specific Union act.
- **Who is covered** (Article 2(1)): credit institutions, payment institutions, account information service providers,
  electronic money institutions, investment firms, crypto-asset service providers, central securities depositories,
  central counterparties, trading venues, insurance and reinsurance undertakings, credit rating agencies and others in
  the list.
- **Oversight** (Article 31): the European Supervisory Authorities, through their Joint Committee, designate the ICT
  third-party service providers that are critical for financial entities and appoint a Lead Overseer for each.

## A note on the French bill

[[FR-NIS2-LOI]]'s description says the French bill transposes NIS2 "together with the Critical Entities Resilience
Directive and DORA". This Regulation is directly applicable and is not itself transposed; what exactly the French bill
does in relation to it was not read for this entity, so no edge is drawn between them.

## Not modelled

- The **European Supervisory Authorities** (EBA, EIOPA, ESMA) and the national financial supervisors are not Atlas
  entities.
- The five regulations it amends are not Atlas entities.

## Sources

Listed in frontmatter, read directly.
