---
id: PK-DATA-GOVERNANCE-POLICY-2026
type: policy
name: "Data Governance Policy 2026"
alternative_names:
  - "National Data Governance Policy"
  - "DNP-D.001 POL"
description: >
  Pakistan's draft national policy for the governance of public-sector
  data, issued as a draft by the Ministry of Information Technology and
  Telecommunication in June 2026 (listed 26 June 2026). It sets the State's
  position on data sovereignty and residency, open data, sharing, personal
  data, citizen data rights, cross-border transfer, AI and the data
  economy, and an institutional framework run by the Pakistan Digital
  Authority.

level: national
country: PK
region: null

status: proposed
confidence: high
coverage: medium
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-10-16"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - PK-PDA
  - PK-MOITT
related_entities:
  - PK
  - PK-PDA
  - PK-MOITT
relationships:
  - type: applies-in
    target: PK
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. Clause 1 of the draft (read 2026-10-16): the Policy 'establishes the binding national direction for the governance of public-sector data in the Islamic Republic of Pakistan' and applies to all federal public bodies and their contractors, processors and partners (clause 7)."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: PK-PDA
    source: fact
    evidence: "Clause 16.1 (read 2026-10-16): the Pakistan Digital Authority is 'responsible for the issuance, oversight, and assurance of this Policy and its supporting instruments'."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Data Governance Policy 2026 (draft, June 2026)"
    url: "https://www.moitt.gov.pk/SiteImage/Policies/Data%20Governance%20Policy%20June%202026.pdf"
    publisher: "Ministry of Information Technology and Telecommunication (Pakistan)"
    accessed: "2026-10-16"
    note: "Read in full text: 25 pages. Listed as a Draft on the Ministry's Policies page."
  - title: "Policies — MoITT"
    url: "https://www.moitt.gov.pk/Policies"
    publisher: "Ministry of Information Technology and Telecommunication (Pakistan)"
    accessed: "2026-10-16"
---

# Data Governance Policy 2026 (Pakistan)

> **Created 2026-10-16** (roadmap #476, Pakistan). The whole text (25 pages) was read from the Ministry's PDF. It is a **draft**: the Ministry's Policies page lists it as "Draft", dated 26 June 2026, and the policy itself says it takes effect "on the date of its formal issuance by PDA, following Cabinet approval and Gazette notification"; its machine-readable block carries `"maturityLevel": "PROPOSED"`, `"dateApproved": "2026-05-XX"` and `"gazetteReference": "[Pending Cabinet approval and SRO assignment]"`. Hence `status: proposed` and no start date.

## What the text says

- **Scope (cl. 1, 7).** The primary national instrument for governing *public-sector* data across its lifecycle; it does not govern personal data held outside the public sector.
- **Sovereignty and residency (cl. 8).** The Government asserts sovereign control over Government data, with tiered residency (the top tier for restricted, confidential and personal data to be hosted, stored and processed in Pakistan). Cross-border transfer (cl. 13) is allowed only where lawful, justified, governed and safeguarded, through approval pathways by classification and recipient jurisdiction.
- **Personal data (cl. 11-12).** Lawful, fair and transparent processing by public bodies under Article 14 of the Constitution; data-subject rights "as provided by applicable law". The Policy says that where a Personal Data Protection Law is enacted it will be updated to align: so no such law existed when it was written.
- **Institutions (cl. 16).** See [[PK-PDA]]: a National Chief Data Officer, an Agency Chief Data Officer in every public body, a National Data Governance Council.
- **Anchors (Annex I).** The Constitution, the Right of Access to Information Act 2017, the Electronic Transactions Ordinance 2002, the Prevention of Electronic Crimes Act 2016 and the Digital Nation Pakistan Act 2025. None of these was read.
- **Review (Annex III).** At least every three years.

## Relationships

Applies in [[PK]]; `governed-by` [[PK-PDA]]; issued under [[PK-MOITT]].
