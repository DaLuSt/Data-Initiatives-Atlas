---
id: FI-DVV
type: organisation
name: Digital and Population Data Services Agency
alternative_names:
  - DVV
  - Digi- ja vaestotietovirasto
  - Digi- ja väestötietovirasto
  - Myndigheten for digitalisering och befolkningsdata
description: >
  Finnish agency whose tasks include maintenance of the Population
  Information System, the development of solutions for electronic
  identification, and the development and maintenance of the centralised
  support services for e-services - the Suomi.fi Web Service, Suomi.fi
  Messages and Suomi.fi e-Authorization. It has over 800 employees and
  operates at multiple locations across Finland.

level: national
country: FI
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
  - FI
  - FI-SUOMI-FI
  - FI-PALVELUVAYLA
relationships:
  - type: part-of
    target: FI
    source: fact
    evidence: "Confirmed by reading dvv.fi's own 'About the agency' page directly (2026-08-26): 'Digital and Population Data Services Agency promotes the digitalisation of society, secures the availability of information, and provides services related to customers' life events' — anchor edge under metadata/relationship-types.md §2.3, asserting no more than national scope."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Digital and Population Data Services Agency"
    url: "https://dvv.fi/en/digital-and-population-data-services-agency"
    publisher: "Digital and Population Data Services Agency (DVV)"
    accessed: "2026-08-26"
  - title: "About the agency"
    url: "https://dvv.fi/en/about-the-agency"
    publisher: "Digital and Population Data Services Agency (DVV)"
    accessed: "2026-08-26"
---

# Digital and Population Data Services Agency

> **Verified 2026-08-26.** Both cited pages were read directly. The
> "over 800 employees" figure is confirmed verbatim, and DVV's own site
> names a project this entity did not previously carry: piloting the
> European Digital Identity Wallet under the revised eIDAS Regulation.

## Description

Finland's digital government and population data agency, and the other
half of the X-Road story the Atlas began with Estonia. Confirmed by
reading dvv.fi directly: "Our agency has over 800 employees and we
operate in 12 towns all over Finland" — matching this entity's existing
claim exactly, now in DVV's own words rather than unread.

## One agency for identity, population data and e-services

DVV holds three things that in most Atlas countries sit in different
bodies: the **Population Information System**, **electronic
identification**, and the **shared e-service support services**.

In the Netherlands those are [[NL-RVIG]], [[NL-LOGIUS]] and the [[NL-GDI]]
respectively. The Finnish consolidation is worth recording because the
Atlas's organisation layer otherwise implies that separation is the norm.

## A queued eIDAS2 connection

DVV's own site lists "European digital identity wallet — Piloting of
the European Digital Identity Wallet" and "What is the revised eIDAS
Regulation?" among its current projects. No page read this pass states
DVV's role under [[EU-EIDAS2]] in enough detail to assert a
relationship, so none is added — this is the same eIDAS2 gap
[[FR-FRANCECONNECT]] flagged as queued across every Atlas country, now
observed here too rather than asserted.

## Relationships

- `part-of` [[FI]] (anchor edge).
- Maintains [[FI-SUOMI-FI]] and [[FI-PALVELUVAYLA]].

## Sources

Listed in frontmatter, both read directly this pass.
