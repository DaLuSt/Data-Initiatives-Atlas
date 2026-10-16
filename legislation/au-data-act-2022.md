---
id: AU-DATA-ACT-2022
type: act
name: "Data Availability and Transparency Act 2022"
alternative_names:
  - "DAT Act"
  - "DATA Act 2022"
description: >
  Australian Government act (No. 11 of 2022), made on 31 March 2022, that
  sets a scheme for sharing Australian Government data. Administered by the
  Department of Finance. The Federal Register's record shows it as in force
  now but with a scheduled status change: it is marked to cease on 1 April
  2027 as "Self Ceasing".

level: national
country: AU
region: null

status: active
confidence: high
coverage: low
verification: primary-source
start_date: 2022-03-31
end_date: null
last_verified: "2026-10-16"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - AU
  - AU-PRIVACY-ACT-1988
relationships:
  - type: applies-in
    target: AU
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. The Federal Register of Legislation (read 2026-10-16) lists the Data Availability and Transparency Act 2022, No. 11, 2022, as 'In force', administered by the Department of Finance."
    confidence: high
    valid_from: 2022-03-31
    valid_until: null
  - type: references
    target: AU-PRIVACY-ACT-1988
    source: fact
    evidence: "The register's version record for the Act's compilation C2024C00820 (11 December 2024) lists as its reason an amendment by 'sch 1 (items 45, 46) of the Privacy and Other Legislation Amendment Act 2024', an amending act that also amends the Privacy Act; the Act's text was not read."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Data Availability and Transparency Act 2022 — Federal Register of Legislation"
    url: "https://www.legislation.gov.au/C2022A00011/latest/text"
    publisher: "Federal Register of Legislation (Australian Government)"
    accessed: "2026-10-16"
    note: "Page read: No. 11 of 2022, in force, administered by the Department of Finance, latest compilation C2024C00820 (C04, 11 December 2024)."
  - title: "Data Availability and Transparency Act 2022 — title record (Federal Register API)"
    url: "https://api.prod.legislation.gov.au/v1/titles/C2022A00011"
    publisher: "Federal Register of Legislation (Australian Government)"
    accessed: "2026-10-16"
    note: "Making date 2022-03-31; status history lists a future status 'Ceased' on 2027-04-01 with the reason 'Self Ceasing'."
---

# Data Availability and Transparency Act 2022 (Australia)

> **Created 2026-10-16** (roadmap #479, Australia). Read on the Federal Register of Legislation and its API; the Act's sections were not read. `start_date` is the register's making date, 31 March 2022.

## The scheduled cessation

The register's API record for the title lists a future status **Ceased on 2027-04-01**, reason "Self Ceasing", and the current version (C2024C00820, compilation 4, 11 December 2024) runs to 2027-04-01. Secondary sources in search (law-firm notes, a South Australian law handbook; none read here) say this is the Act's sunset clause, with a statutory review due by 1 April 2026 on whether to extend it. **The review's outcome and any extension were not found**: finance.gov.au, which hosts the review page, answered with a 403. The status therefore stays `active`, with no end date (a date in the future is not recorded as `end_date`), and the next re-check belongs in the roadmap's "waiting on events" items (#502 and its successors).

## What is sourced

Title, number, making date, in-force status, administering department, latest compilation. Not read: the scheme itself, the National Data Commissioner's role, the data-sharing agreements.

## Relationships

Applies in [[AU]]; related to [[AU-PRIVACY-ACT-1988]] only through a shared 2024 amending act (low confidence).
