---
id: INTL-OECS
type: organisation
name: "Organisation of Eastern Caribbean States (OECS)"
alternative_names:
  - "OECS"
  - "OECS Commission"
description: >
  The international inter-governmental organisation for regional integration in the Eastern Caribbean: seven full
  Member States in an economic union under the Revised Treaty of Basseterre (2010), plus associate members. Its
  Commission runs the Regional Data Governance Council and the regional statistics strategy.

level: regional
country: null
region: null

status: active
organisation_role: executive
confidence: high
coverage: low
verification: primary-source
start_date: 1981-06-18
end_date: null
last_verified: "2026-10-23"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - INTL-OECS-REVISED-TREATY
  - INTL-OECS-RDGC
  - INTL-OECS-RSDS
relationships:
  - type: governed-by
    target: INTL-OECS-REVISED-TREATY
    source: fact
    evidence: "The About page (read directly 2026-10-23): 'The 1981 Treaty was replaced in 2010 with a Revised Treaty of Basseterre, creating an economic union'."
    confidence: high
    valid_from: null
    valid_until: null
  - type: related-to
    target: INTL-OECS-RDGC
    source: fact
    evidence: "The OECS media release of 17 October 2023 (read directly 2026-10-23): 'The Organisation of Eastern Caribbean States (OECS) Commission officially launched the OECS Regional Data Governance Council (RDGC) on October 11, 2023, in Saint Lucia.'"
    confidence: high
    valid_from: null
    valid_until: null
  - type: related-to
    target: INTL-OECS-RSDS
    source: fact
    evidence: "The same release: the RDGC 'will also contribute to the implementation of the OECS Regional Strategy for the Development of Statistics (RSDS) - (2017-2030)'."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "About the OECS"
    url: "https://www.oecs.int/en/who-we-are/about-us"
    publisher: "Organisation of Eastern Caribbean States"
    accessed: "2026-10-23"
  - title: "OECS Regional Data Governance Council Officially Launched! (17 October 2023)"
    url: "https://pressroom.oecs.int/oecs-regional-data-governance-council-officially-launched"
    publisher: "Organisation of Eastern Caribbean States"
    accessed: "2026-10-23"
---

# Organisation of Eastern Caribbean States (OECS)

> **Created 2026-10-23** (roadmap #547, the Caribbean's regional bodies). From the OECS's own About page and media releases, read directly. The Treaty texts were not read.

## Description

"The Organisation of Eastern Caribbean States came into being on June 18th 1981, when seven Eastern Caribbean countries signed a treaty" (the Treaty of Basseterre), replaced on 18 June 2010 by the Revised Treaty of Basseterre. Full Member States: Antigua and Barbuda, Dominica, Grenada, Montserrat, Saint Kitts and Nevis, Saint Lucia and Saint Vincent and the Grenadines; associate members: the British Virgin Islands, Anguilla, Martinique, Guadeloupe and Saint Martin. **None of these has a country anchor in the Atlas**, so the OECS has no country edges. Its Director General (Dr Didacus Jules in 2023 and 2026) opened the data governance council meetings.

## Relationships

`governed-by` [[INTL-OECS-REVISED-TREATY]]; `related-to` [[INTL-OECS-RDGC]] and [[INTL-OECS-RSDS]].

## Sources

Listed in frontmatter, read directly.
