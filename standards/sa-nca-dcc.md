---
id: SA-NCA-DCC
type: standard
name: "Data Cybersecurity Controls (DCC-1:2022)"
alternative_names:
  - "DCC"
  - "DCC-1:2022"
description: >
  Cybersecurity controls issued by Saudi Arabia's National Cybersecurity Authority (page dated 18 September 2022) that set the
  minimum cybersecurity requirements for organisations to protect their data through its whole life cycle, developed after a study
  of national and international standards, laws and incidents, as an extension to the Essential Cybersecurity Controls. An
  assessment and compliance tool is published with them. The document itself was not opened.

level: national
country: SA
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
  - DOMAIN-CYBERSECURITY
organisations:
  - SA-NCA
related_entities:
  - SA
  - SA-NCA
  - SA-NCA-ECC
relationships:
  - type: applies-in
    target: SA
    source: fact
    evidence: "The Authority's DCC page (read directly 2026-11-01): 'NCA has issued the Data Cybersecurity Controls (DCC-1:2022)'; 'These controls are an extension to the Essential Cybersecurity Controls (ECC).' To whom they apply was not read."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: based-on
    target: SA-NCA-ECC
    source: fact
    evidence: "The same page: 'These controls are an extension to the Essential Cybersecurity Controls (ECC).'"
    confidence: high
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: SA-NCA
    source: fact
    evidence: "The page is on the Authority's own site: 'NCA has issued the Data Cybersecurity Controls'."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Data Cybersecurity Controls — NCA"
    url: "https://nca.gov.sa/en/regulatory-documents/controls-list/dcc/"
    publisher: "National Cybersecurity Authority (NCA), Saudi Arabia"
    accessed: "2026-11-01"
---

# Data Cybersecurity Controls (DCC-1:2022)

> **Created 2026-11-01**. From the Authority's page only; `start_date` is empty: the page is dated 18 September 2022 but no effective date was read.

## Relationships

Applies in [[SA]]; based on [[SA-NCA-ECC]]; maintained by [[SA-NCA]].
