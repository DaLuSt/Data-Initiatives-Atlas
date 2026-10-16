---
id: NG-NDPC
type: organisation
name: "Nigeria Data Protection Commission"
alternative_names:
  - "NDPC"
description: >
  Nigeria's data protection authority, established by the Nigeria Data
  Protection Act 2023 to oversee its implementation. Its site offers
  registration of data controllers and processors of major importance,
  licensing of data protection compliance organisations (DPCOs) and
  privacy-breach reporting.

level: national
country: NG
region: null

status: active
organisation_role: regulatory
confidence: high
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-10-16"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NG
  - NG-NDPA-2023
  - NG-NDPA-GAID-2025
relationships:
  - type: part-of
    target: NG
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. The Commission's About page (read 2026-10-16): the Federal Government of Nigeria signed the Act into law and 'the Act established the Nigeria Data Protection Commission'."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: NG-NDPA-2023
    source: fact
    evidence: "The same page (read 2026-10-16): the Commission's mandate is 'to oversee the implementation of the Nigeria Data Protection Act'; its home page says it is 'established under the Nigeria Data Protection Act 2023'."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "About Us — Nigeria Data Protection Commission"
    url: "https://ndpc.gov.ng/about-us/"
    publisher: "Nigeria Data Protection Commission"
    accessed: "2026-10-16"
  - title: "Nigeria Data Protection Commission — home page"
    url: "https://ndpc.gov.ng/"
    publisher: "Nigeria Data Protection Commission"
    accessed: "2026-10-16"
---

# Nigeria Data Protection Commission

> **Created 2026-10-16** (roadmap #475, Nigeria). Read on the Commission's own site. The earlier runner attempt (2026-10-11) got a 403 from ndpc.gov.ng; the site answered with a 200 to the agent on 2026-10-16. No founding date is recorded: the pages say the Act established the Commission but do not date the Commission itself.

## What the site says

Mandate: to oversee implementation of [[NG-NDPA-2023]] and complement other statutory institutions in safeguarding natural persons' privacy; collaborate with stakeholders to safeguard data-privacy rights, promote secure processing and strengthen the legal foundations of the digital economy. The home page's services: data controller/processor registration, DPCO registration and a list of licensed DPCOs, privacy-breach reporting. The head of the Commission signs the 2025 directive as "National Commissioner/CEO" ([[NG-NDPA-GAID-2025]]).

## Relationships

Part of [[NG]]; `governed-by` [[NG-NDPA-2023]].
