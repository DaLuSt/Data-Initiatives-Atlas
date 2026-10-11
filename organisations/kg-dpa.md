---
id: KG-DPA
type: organisation
name: "State Agency for Personal Data Protection"
alternative_names:
  - "DPA Kyrgyzstan"
description: >
  Kyrgyzstan's authorized state body for personal data under Law No. 58 of
  2008. The Atlas knows it from its register site and from secondary
  sources; its own pages were not read.

level: national
country: KG
region: null

status: active
organisation_role: regulatory
confidence: medium
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-10-11"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - KG
  - KG-LAW-58-2008
relationships:
  - type: part-of
    target: KG
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. The register at reestr.dpa.gov.kg (read 2026-10-11), on a .gov.kg domain, publishes the personal-data law and calls the body in Article 3 'the authorized state body for personal data'; the name 'State Agency for Personal Data Protection' comes from secondary sources (DLA Piper) and is not on the page read."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: KG-LAW-58-2008
    source: fact
    evidence: "Article 3 of the law, read on the agency's own register (2026-10-11), defines 'The authorized state body for personal data (hereinafter referred to as the authorized state body)'."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Law of the Kyrgyz Republic No. 58 of April 14, 2008 'On personal data' (as amended by Laws No. 129 of 2017 and No. 142 of 2021) — register of normative acts"
    url: "https://reestr.dpa.gov.kg/en/npa/4"
    publisher: "State Agency for Personal Data Protection (Kyrgyz Republic), reestr.dpa.gov.kg"
    accessed: "2026-10-11"
---

# State Agency for Personal Data Protection (Kyrgyz Republic)

> **Created 2026-10-11** (roadmap #474, Kyrgyzstan). The agency is identified through the register at `reestr.dpa.gov.kg`, which hosts the law; its own pages and its place in government (secondary sources say under the Cabinet of Ministers) were not read, and the main site `dpa.gov.kg/en/npa/4` returned 404.

## Description

The "authorized state body for personal data" of [[KG-LAW-58-2008]]. Secondary sources describe it as the State Agency for Personal Data Protection and say that data arrays and their holders must register with it (Article 30); that was not read.

## Relationships

`part-of` [[KG]] (anchor edge); `governed-by` [[KG-LAW-58-2008]].
