---
id: JM-OIC
type: organisation
name: "Office of the Information Commissioner"
alternative_names:
  - "OIC"
description: >
  Jamaica's independent data-protection authority, established in December
  2021 under the Data Protection Act 2020, which monitors compliance,
  advises the Minister and registers data controllers.

level: national
country: JM
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
  - JM
  - JM-DPA-2020
relationships:
  - type: part-of
    target: JM
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. The Office of the Prime Minister's page, read directly (2026-10-11), calls the Office of the Information Commissioner 'an independent governmental body established in December 2021 to protect the privacy and security of personal data'."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: JM-DPA-2020
    source: fact
    evidence: "The same page (read 2026-10-11): 'The OIC ensures adherence to the DPA, and any accompanying Regulations made under it.'"
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "The Office of the Information Commissioner — Office of the Prime Minister (Jamaica)"
    url: "https://opm.gov.jm/the-office-of-the-information-commissioner/"
    publisher: "Office of the Prime Minister, Government of Jamaica"
    accessed: "2026-10-11"
---

# Office of the Information Commissioner (Jamaica)

> **Created 2026-10-11** (roadmap #476, Jamaica). Read on the Office of the Prime Minister's page; the Office's own site `oic.gov.jm` was not reached. The date is the month the page gives.

## Description

"An independent governmental body established in December 2021 to protect the privacy and security of personal data." It ensures adherence to [[JM-DPA-2020]] and its Regulations, provides expert advice and recommendations to the Minister, may develop or direct the preparation of good-practice guidelines, and is required to raise public awareness about data protection. The page names the Information Commissioner as Miss Celia Barclay; the Atlas does not record people. Registration of data controllers began on 1 December 2023.

## Relationships

`part-of` [[JM]] (anchor edge); `governed-by` [[JM-DPA-2020]].
