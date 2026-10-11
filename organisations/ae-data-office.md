---
id: AE-DATA-OFFICE
type: organisation
name: "UAE Data Office"
alternative_names:
  - "Data Office"
description: >
  The UAE's federal data regulator, affiliated with the UAE Cabinet and
  established by Federal Decree-Law No. 44 of 2021. Its operating status was
  not checked.

level: national
country: AE
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
  - AE
  - AE-PDPL-45-2021
  - AE-DECREE-LAW-44-2021
relationships:
  - type: part-of
    target: AE
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. The UAE Government's portal, read directly (2026-10-11): 'The UAE Data Office will act as the federal data regulator in the UAE' and 'is affiliated with the UAE Cabinet'."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: AE-DECREE-LAW-44-2021
    source: fact
    evidence: "The portal, read directly (2026-10-11), lists Federal Decree Law No. 44 of 2021 'on the establishment of the UAE Data Office'."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Data protection laws — The Official Portal of the UAE Government"
    url: "https://u.ae/en/about-the-uae/digital-uae/data/data-protection-laws"
    publisher: "UAE Government (u.ae)"
    accessed: "2026-10-11"
---

# UAE Data Office

> **Created 2026-10-11** (roadmap #475, United Arab Emirates). Known from the UAE Government's portal; the Office's own site was not found, and its operating status is not stated on the page read.

## Description

The portal says it "will act as the federal data regulator in the UAE" and is affiliated with the UAE Cabinet. It was established by [[AE-DECREE-LAW-44-2021]] and is the regulator under [[AE-PDPL-45-2021]]. The portal's wording is future ("will act"); how far it is operating today was not checked.

## Relationships

`part-of` [[AE]] (anchor edge); `governed-by` [[AE-DECREE-LAW-44-2021]].
