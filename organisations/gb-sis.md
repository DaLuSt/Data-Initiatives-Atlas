---
id: GB-SIS
type: organisation
name: Secret Intelligence Service
alternative_names:
  - SIS
  - MI6
description: >
  The United Kingdom's foreign intelligence service. The Intelligence
  Services Act 1994 established and regulated it on a statutory basis
  alongside GCHQ, providing for accountability and legal oversight. Its use
  of investigatory powers is governed by the Investigatory Powers Act 2016
  and overseen by IPCO.

level: national
country: GB
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - GB-ISA-1994
  - GB-IPA-2016
  - GB-DPA-2018
  - GB-MI5
  - GB-GCHQ
  - GB-IPCO
  - GB-ISC
relationships:
  - type: governed-by
    target: GB-DPA-2018
    source: fact
    evidence: "Part 4 of the Data Protection Act 2018 is separate from the UK GDPR regime and sets out a data protection regime for intelligence services processing; the intelligence services are the Security Service (MI5), the Secret Intelligence Service (MI6) and GCHQ, and all processing of personal data they undertake is governed by Part 4 (ico.org.uk 'Guide to Intelligence Services Processing' and 'Scope and key definitions'; assets.publishing.service.gov.uk 'Data Protection Act 2018 Factsheet — Intelligence services processing'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: GB-ISA-1994
    source: fact
    evidence: "The Intelligence Services Act 1994 establishes and regulates the United Kingdom's intelligence services, specifically the Secret Intelligence Service (MI6) and the Government Communications Headquarters (GCHQ), providing a statutory basis for their activities and ensuring accountability and legal oversight (legislation.gov.uk ukpga/1994/13; en.wikipedia.org 'Intelligence Services Act 1994'; lexisnexis.co.uk). NOT READ — search-only."
    confidence: medium
    valid_from: 1994-01-01
    valid_until: null
  - type: governed-by
    target: GB-IPA-2016
    source: fact
    evidence: "The Investigatory Powers Act 2016 provides a modernised framework to govern the use and oversight of investigatory powers by law enforcement and the security and intelligence agencies (legislation.gov.uk ukpga/2016/25; ipco.org.uk 'Investigatory Powers'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Intelligence Services Act 1994"
    url: "https://www.legislation.gov.uk/ukpga/1994/13"
    publisher: "The National Archives (legislation.gov.uk)"
  - title: "Intelligence Services Act 1994"
    url: "https://en.wikipedia.org/wiki/Intelligence_Services_Act_1994"
    publisher: "Wikipedia"
  - title: "Roles and Responsibilities of the Security Service and Secret Intelligence Service"
    url: "https://tile.loc.gov/storage-services/service/ll/llglrd/2024555215/2024555215.pdf"
    publisher: "Law Library of Congress"
---

# Secret Intelligence Service (SIS / MI6)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

SIS is the UK's **foreign** intelligence service, put on a statutory footing
by [[GB-ISA-1994]] together with [[GB-GCHQ]].

## Two services, one act — and the reason it matters here

[[GB-ISA-1994]] covers **both** SIS and GCHQ. That makes the UK a hybrid of
the two patterns in this batch: [[GB-MI5]] has an act to itself
([[GB-SSA-1989]]), while the other two share one.

The pairing is not arbitrary. Both are foreign-facing services answering to
the Foreign Secretary, where MI5 is domestic and answers to the Home
Secretary. The statute follows the ministerial line, not the discipline —
human intelligence and signals intelligence sit in the same act because they
sit under the same minister.

## The 1994 act created the ISC, and 2013 replaced that provision

[[GB-ISA-1994]] also established the **Intelligence and Security
Committee** — a body of parliamentarians examining the agencies'
expenditure, administration and policy.

[[GB-JSA-2013]] then re-founded the ISC on a new statutory basis with a
wider remit including **operations**. The modern [[GB-ISC]] therefore takes
its `governed-by` edge to the 2013 act, not to the 1994 one, and the 1994
act's oversight provision is recorded on [[GB-ISA-1994]] as superseded
rather than modelled as a live relationship.

## Relationships

- `governed-by` [[GB-ISA-1994]], [[GB-IPA-2016]] and [[GB-DPA-2018]] (Part 4).

## Sources

Listed in frontmatter.
