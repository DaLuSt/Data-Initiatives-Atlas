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
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
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
    evidence: "Confirmed by reading the DPA 2018 statute text at legislation.gov.uk (2026-08-22), Part 4, § 82(2): 'In this Part, \"intelligence service\" means— (a) the Security Service; (b) the Secret Intelligence Service; (c) the Government Communications Headquarters.'"
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: GB-ISA-1994
    source: fact
    evidence: "Confirmed by reading the ISA 1994 statute text at legislation.gov.uk (2026-08-22): the long title covers 'the Secret Intelligence Service and the Government Communications Headquarters', enacted 26 May 1994; § 1(1) sets out SIS's functions, exercisable 'in the interests of national security, with particular reference to the defence and foreign policies of Her Majesty's Government'."
    confidence: medium
    valid_from: 1994-01-01
    valid_until: null
  - type: governed-by
    target: GB-IPA-2016
    source: fact
    evidence: "Confirmed by reading the IPA 2016 statute text at legislation.gov.uk (2026-08-22): the Act's long title covers 'the interception of communications, equipment interference and the acquisition and retention of communications data, bulk personal datasets and other information', enacted 29 November 2016."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Intelligence Services Act 1994"
    url: "https://www.legislation.gov.uk/ukpga/1994/13"
    publisher: "The National Archives (legislation.gov.uk)"
    accessed: "2026-08-22"
  - title: "Intelligence Services Act 1994"
    url: "https://en.wikipedia.org/wiki/Intelligence_Services_Act_1994"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
  - title: "Roles and Responsibilities of the Security Service and Secret Intelligence Service"
    url: "https://tile.loc.gov/storage-services/service/ll/llglrd/2024555215/2024555215.pdf"
    publisher: "Law Library of Congress"
    accessed: "2026-08-22"
---

# Secret Intelligence Service (SIS / MI6)

> **Verified 2026-08-22.** The ISA 1994, IPA 2016 and DPA 2018 statute
> texts at legislation.gov.uk were read directly and confirmed the claims
> below, including § 1 ISA 1994 on SIS's own functions.

## Description

Confirmed directly on legislation.gov.uk (2026-08-22), § 1(1) ISA 1994: the
Secret Intelligence Service's functions are exercisable "in the interests
of national security, with particular reference to the defence and foreign
policies of Her Majesty's Government in the United Kingdom". SIS is the UK's **foreign** intelligence service, put on a statutory footing
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
