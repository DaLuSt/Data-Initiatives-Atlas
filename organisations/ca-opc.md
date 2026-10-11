---
id: CA-OPC
type: organisation
name: "Office of the Privacy Commissioner of Canada"
alternative_names:
  - "OPC"
  - "Bureau du commissaire à la protection de la vie privée du Canada"
description: >
  Canada's federal privacy regulator, established in 1983 under the Privacy
  Act and responsible since 2001 also for PIPEDA. The Privacy Commissioner
  is independent of government and reports to Parliament.

level: national
country: CA
region: null

status: active
organisation_role: regulatory
confidence: high
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
  - CA
  - CA-PRIVACY-ACT
  - CA-PIPEDA
relationships:
  - type: part-of
    target: CA
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. priv.gc.ca, read directly (2026-10-11): 'The mission of the OPC is to protect and promote the privacy rights of individuals'; the Privacy Commissioner 'is independent of government and reports to Parliament'."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: CA-PRIVACY-ACT
    source: fact
    evidence: "priv.gc.ca, read directly (2026-10-11): the OPC 'was established in 1983 following the passage of the' Privacy Act, which governs how federal departments and agencies handle personal information."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: CA-PIPEDA
    source: fact
    evidence: "priv.gc.ca, read directly (2026-10-11): 'In 2001, the duties of the OPC were extended to include private sector businesses'; PIPEDA is Canada's federal private-sector privacy law."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Who we are — Office of the Privacy Commissioner of Canada"
    url: "https://www.priv.gc.ca/en/about-the-opc/who-we-are/"
    publisher: "Office of the Privacy Commissioner of Canada"
    accessed: "2026-10-11"
---

# Office of the Privacy Commissioner of Canada (OPC)

> **Created 2026-10-11** (roadmap #472, Canada). The OPC's "who we are" page was read directly.

## Description

The OPC checks that federal departments and agencies and private businesses follow the privacy laws it oversees, [[CA-PRIVACY-ACT]] and [[CA-PIPEDA]]. It "was established in 1983 following the passage of the" Privacy Act; "in 2001, the duties of the OPC were extended to include private sector businesses". The Privacy Commissioner is independent of government and reports to Parliament. The 1983 date is the establishment year as the page gives it; the day is not stated.

## Relationships

`part-of` [[CA]] (anchor edge); `governed-by` [[CA-PRIVACY-ACT]] and [[CA-PIPEDA]].
