---
id: BH-NCSC
type: organisation
name: "National Cyber Security Centre (Bahrain)"
alternative_names:
  - "NCSC"
  - "المركز الوطني للأمن السيبراني"
description: >
  A Bahraini body under the Ministry of Interior that, with the General Directorate of Anti-Corruption and Economic and Electronic
  Security, forms one of the two pillars of the Kingdom's cybersecurity strategy, per the National Portal. Its own site publishes
  the National Cyber Security Strategies, and sections on royal orders and decrees, standards and controls and executive
  decisions, and takes incident reports.

level: national
country: BH
region: null

status: active
organisation_role: executive
confidence: medium
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-11-01"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - BH
  - BH-NCSS-2025-2028
relationships:
  - type: part-of
    target: BH
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. The National Portal's Cyber Security page (read directly 2026-11-01): 'Two key entities under the Ministry of Interior form the pillars of Bahrain's cybersecurity strategy ... and the National Cyber Security Centre.'"
    confidence: high
    valid_from: null
    valid_until: null
  - type: produces
    target: BH-NCSS-2025-2028
    source: fact
    evidence: "The Centre's National Cybersecurity Strategies page (read directly 2026-11-01) lists 'Bahrain National Cyber Security Strategy 2025-2028' on the Centre's own site. The page does not state who authored it, so the edge is `medium` confidence."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Cyber Security — Bahrain National Portal"
    url: "https://www.bahrain.bh/wps/portal/en/BNP/ExploreBahrain/CyberSecurity"
    publisher: "Information & eGovernment Authority, Kingdom of Bahrain (National Portal)"
    accessed: "2026-11-01"
  - title: "National Cybersecurity Strategies — NCSC"
    url: "https://www.ncsc.gov.bh/en/national-strategy.html"
    publisher: "National Cyber Security Centre, Kingdom of Bahrain"
    accessed: "2026-11-01"
---

# National Cyber Security Centre (Bahrain)

> **Created 2026-11-01** (roadmap #480). The National Portal's cyber security page and the Centre's strategies page were read directly. The Centre's founding instrument and date, and the Ministry of Interior (not an Atlas entity), were not read.

## Relationships

Part of [[BH]]; publishes [[BH-NCSS-2025-2028]].
