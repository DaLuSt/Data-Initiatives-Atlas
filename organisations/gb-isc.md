---
id: GB-ISC
type: organisation
name: Intelligence and Security Committee of Parliament
alternative_names:
  - ISC
  - Intelligence and Security Committee
description: >
  Statutory committee of parliamentarians established under Part 1 of the
  Justice and Security Act 2013, responsible for oversight of the
  expenditure, administration, policy and operations of the UK intelligence
  services and of other government activities relating to intelligence or
  security matters.

level: national
country: GB
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2013-01-01
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - GB-JSA-2013
  - GB-ISA-1994
  - GB-MI5
  - GB-SIS
  - GB-GCHQ
  - GB-IPCO
relationships:
  - type: governed-by
    target: GB-JSA-2013
    source: fact
    evidence: "The Intelligence and Security Committee of Parliament is a statutory Committee (see Part 1 of the Justice and Security Act 2013) comprising parliamentarians who have responsibility for the oversight of the expenditure, administration, policy and operations of the intelligence services and other activities of HMG in relation to intelligence or security matters (legislation.gov.uk ukpga/2013/18 explanatory notes; en.wikipedia.org 'Justice and Security Act 2013'; investigatorypowerstribunal.org.uk 'Oversight and where we fit in'). NOT READ — search-only."
    confidence: medium
    valid_from: 2013-01-01
    valid_until: null
  - type: applies-to
    target: GB-MI5
    source: fact
    evidence: "The Justice and Security Act 2013 provides for oversight of the Security Service, the Secret Intelligence Service, the Government Communications Headquarters and other activities relating to intelligence or security matters (legislation.gov.uk ukpga/2013/18 explanatory notes; en.wikipedia.org 'Justice and Security Act 2013'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: GB-SIS
    source: fact
    evidence: "The Justice and Security Act 2013 provides for oversight of the Security Service, the Secret Intelligence Service and the Government Communications Headquarters (legislation.gov.uk ukpga/2013/18 explanatory notes). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: GB-GCHQ
    source: fact
    evidence: "The Justice and Security Act 2013 provides for oversight of the Security Service, the Secret Intelligence Service and the Government Communications Headquarters (legislation.gov.uk ukpga/2013/18 explanatory notes). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Justice and Security Act 2013 — explanatory notes"
    url: "https://www.legislation.gov.uk/ukpga/2013/18/notes/division/3/2/data.htm"
    publisher: "The National Archives (legislation.gov.uk)"
  - title: "Justice and Security Act 2013"
    url: "https://en.wikipedia.org/wiki/Justice_and_Security_Act_2013"
    publisher: "Wikipedia"
  - title: "Oversight and where we fit in"
    url: "https://investigatorypowerstribunal.org.uk/oversight-and-where-we-fit-in/"
    publisher: "Investigatory Powers Tribunal"
---

# Intelligence and Security Committee of Parliament (ISC)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

The ISC is the UK's **parliamentary** oversight body for the intelligence
services, on a statutory footing under Part 1 of [[GB-JSA-2013]]. Its remit
covers **expenditure, administration, policy and operations** — and other
government activities relating to intelligence or security.

## An oversight body that was re-founded, not created

The ISC first existed under [[GB-ISA-1994]], which established a committee
of parliamentarians examining the agencies' **expenditure, administration
and policy**. [[GB-JSA-2013]] re-founded it with the word *operations* added
to that list.

That single word is the change. A committee that may examine expenditure,
administration and policy scrutinises how an agency is *run*; one that may
examine operations scrutinises what it *does*.

The Atlas models the current basis — `governed-by` [[GB-JSA-2013]] — and
records the 1994 origin on [[GB-ISA-1994]] rather than asserting a second,
superseded edge.

## Two overseers, split by question

The UK runs the same pair as Germany:

| | Parliamentary | Independent / legality |
|---|---|---|
| UK | **ISC** ([[GB-JSA-2013]]) | [[GB-IPCO]] ([[GB-IPA-2016]]) |
| Germany | [[DE-PKGR]] ([[DE-PKGRG]]) | [[DE-UKR]] |
| Poland | [[PL-KSS]] (Sejm standing orders) | *not held* |

The ISC asks whether the agencies are doing the right things; [[GB-IPCO]]
asks whether particular uses of particular powers were lawful.

## Relationships

- `governed-by` [[GB-JSA-2013]].
- `applies-to` [[GB-MI5]], [[GB-SIS]] and [[GB-GCHQ]].

## Sources

Listed in frontmatter.
