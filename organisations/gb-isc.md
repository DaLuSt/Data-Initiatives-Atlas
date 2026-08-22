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
verification: primary-source
start_date: "2013-06-25"
end_date: null
last_verified: "2026-08-22"
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
    evidence: "Confirmed by reading the JSA 2013 statute text at legislation.gov.uk (2026-08-22), § 1(1)-(2): 'There is to be a body known as the Intelligence and Security Committee of Parliament ... The ISC is to consist of nine members who are to be drawn both from the members of the House of Commons and from the members of the House of Lords', enacted 25 April 2013."
    confidence: medium
    valid_from: 2013-01-01
    valid_until: null
  - type: applies-to
    target: GB-MI5
    source: fact
    evidence: "Confirmed by reading the JSA 2013 statute text at legislation.gov.uk (2026-08-22), § 2(1): 'The ISC may examine or otherwise oversee the expenditure, administration, policy and operations of— (a) the Security Service, (b) the Secret Intelligence Service, and (c) the Government Communications Headquarters.'"
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: GB-SIS
    source: fact
    evidence: "Confirmed by reading the JSA 2013 statute text at legislation.gov.uk (2026-08-22), § 2(1): 'The ISC may examine or otherwise oversee the expenditure, administration, policy and operations of— (a) the Security Service, (b) the Secret Intelligence Service, and (c) the Government Communications Headquarters.'"
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: GB-GCHQ
    source: fact
    evidence: "Confirmed by reading the JSA 2013 statute text at legislation.gov.uk (2026-08-22), § 2(1): 'The ISC may examine or otherwise oversee the expenditure, administration, policy and operations of— (a) the Security Service, (b) the Secret Intelligence Service, and (c) the Government Communications Headquarters.'"
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Justice and Security Act 2013 — explanatory notes"
    url: "https://www.legislation.gov.uk/ukpga/2013/18/notes/division/3/2/data.htm"
    publisher: "The National Archives (legislation.gov.uk)"
    accessed: "2026-08-22"
  - title: "Justice and Security Act 2013"
    url: "https://en.wikipedia.org/wiki/Justice_and_Security_Act_2013"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
  - title: "Oversight and where we fit in"
    url: "https://investigatorypowerstribunal.org.uk/oversight-and-where-we-fit-in/"
    publisher: "Investigatory Powers Tribunal"
    accessed: "2026-08-22"
---

# Intelligence and Security Committee of Parliament (ISC)

> **Verified 2026-08-22.** The JSA 2013 statute text at legislation.gov.uk
> was read directly and confirmed §§ 1–2 below, along with a more precise
> founding date than previously recorded.

## Description

Confirmed directly on legislation.gov.uk (2026-08-22), § 2(1): "The ISC may
examine or otherwise oversee the expenditure, administration, policy and
operations of— (a) the Security Service, (b) the Secret Intelligence
Service, and (c) the Government Communications Headquarters." The ISC is
the UK's **parliamentary** oversight body for the intelligence
services, on a statutory footing under Part 1 of [[GB-JSA-2013]]. Its remit
covers **expenditure, administration, policy and operations** — and other
government activities relating to intelligence or security.

`start_date` is now **25 June 2013**, not the placeholder 1 January
previously recorded: the statute's own commencement information shows § 1
(establishing the ISC) came into force on that date by S.I. 2013/1482,
two months after the Act's Royal Assent on 25 April 2013.

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
