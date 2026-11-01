---
id: INTL-SPC-PDH
type: platform
name: "Pacific Data Hub"
alternative_names:
  - "PDH"
  - "pacificdata.org"
description: >
  The Pacific Community's data hub, listed on spc.int under Resources and Pacific Databases (Pacific Ocean Catalogue, PDH.STAT,
  Pacific Ocean Portal and others). Known here only from that menu: pacificdata.org answers a Cloudflare challenge to the agent
  and to the fetch tool, so its purpose, licence and holdings were not read.

level: regional
country: null
region: null

status: active
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
  - DOMAIN-DIGITAL-INFRASTRUCTURE
organisations:
  - INTL-SPC
related_entities:
  - INTL-SPC
  - INTL-SPC-PDH-STAT
relationships:
  - type: maintained-by
    target: INTL-SPC
    source: fact
    evidence: "The Pacific Community's home page (read directly 2026-11-01) lists 'Pacific Data Hub' (linking to https://pacificdata.org/) under its Resources menu, with 'PDH.STAT (Dev Indicators)' among 'Pacific Databases and Specialist Resources'. The page does not say who runs it, so this edge is `medium` confidence."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "The Pacific Community — home page"
    url: "https://www.spc.int/"
    publisher: "Pacific Community (SPC)"
    accessed: "2026-11-01"
---

# Pacific Data Hub

> **Created 2026-11-01** (roadmap #559-#561). Known only from SPC's menu; the Hub itself was not opened. `status: active` rests on the live menu entry.

## Relationships

Maintained by [[INTL-SPC]] (medium confidence); related to [[INTL-SPC-PDH-STAT]].
