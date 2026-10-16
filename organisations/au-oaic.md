---
id: AU-OAIC
type: organisation
name: "Office of the Australian Information Commissioner"
alternative_names:
  - "OAIC"
description: >
  Australia's independent national regulator for privacy and freedom of
  information, an independent agency within the Attorney-General's
  portfolio. Its functions include investigations, reviews of decisions,
  complaints, guidance and advice, and it also handles privacy matters under
  the Consumer Data Right.

level: national
country: AU
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
  - AU
  - AU-PRIVACY-ACT-1988
relationships:
  - type: part-of
    target: AU
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. The Office's About page (read 2026-10-16): 'We are an independent agency within the Attorney-General's portfolio. Our primary functions are privacy, freedom of information and government information policy.'"
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: AU-PRIVACY-ACT-1988
    source: fact
    evidence: "The Office's home page (read 2026-10-16) calls it 'the independent national regulator for privacy and freedom of information' and offers privacy complaints and data-breach reports; the Privacy Act's own table of contents (read 2026-10-16 on the Federal Register) has a Part IV, 'Functions of the Information Commissioner'. Neither OAIC page read names the Act in the sentence on its role, so confidence is medium."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "About the OAIC"
    url: "https://www.oaic.gov.au/about-the-OAIC"
    publisher: "Office of the Australian Information Commissioner"
    accessed: "2026-10-16"
  - title: "OAIC — home page"
    url: "https://www.oaic.gov.au/"
    publisher: "Office of the Australian Information Commissioner"
    accessed: "2026-10-16"
---

# Office of the Australian Information Commissioner

> **Created 2026-10-16** (roadmap #479, Australia). Read on the Office's own site. No founding date is recorded: neither page gives one.

## What the pages say

"We're the independent national regulator for privacy and freedom of information. We promote and uphold your rights to access government-held information and have your personal information protected." The home page offers a privacy complaint, a data-breach report, Information Commissioner review of freedom-of-information decisions, and guides on privacy, freedom of information and the Consumer Data Right (including Privacy Safeguard Guidelines). The About page lists conducting investigations, reviewing decisions, handling complaints and providing guidance and advice.

## Relationships

Part of [[AU]]; `governed-by` [[AU-PRIVACY-ACT-1988]] (medium confidence, see the evidence note).
