---
id: IE-NCSC
type: organisation
name: National Cyber Security Centre (Ireland)
alternative_names:
  - NCSC Ireland
  - NCSC-IE
description: >
  Ireland's national cyber security centre, which will act as lead authority
  for oversight and enforcement once the NIS2 Directive is transposed by the
  National Cyber Security Bill. It has published cyber governance guidance
  for management boards ahead of that implementation.

level: national
country: IE
region: EU

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
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - IE-NCS-BILL
  - EU-NIS2
relationships: []

sources:
  - title: "NCSC: NIS2"
    url: "https://www.ncsc.gov.ie/nis2/"
    publisher: "National Cyber Security Centre (Ireland)"
  - title: "NCSC: NIS2 FAQ"
    url: "https://www.ncsc.gov.ie/nis2/FAQ/"
    publisher: "National Cyber Security Centre (Ireland)"
  - title: "Irish NCSC Issues Cyber Governance Guidance for Management Boards Ahead of NIS2 Implementation"
    url: "https://www.globalpolicywatch.com/2026/07/irish-ncsc-issues-cyber-governance-guidance-for-management-boards-ahead-of-nis2-implementation/"
    publisher: "Covington — Global Policy Watch"
---

# National Cyber Security Centre (Ireland)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

Ireland's NCSC is the intended **lead authority for oversight and
enforcement** of NIS2 obligations once [[IE-NCS-BILL]] transposes
[[EU-NIS2]].

## An authority acting ahead of its own statute

The NCSC publishes NIS2 guidance, an FAQ, and cyber governance guidance for
management boards — while the Bill that would give it competent-authority
functions is **not yet enacted**.

That is a real and slightly odd state, and it shapes which edges exist.

**No relationship is asserted *from* this entity.** The Atlas cannot say the
NCSC is `governed-by` [[IE-NCS-BILL]], because the Bill is not law; nor that
it `applies-to` [[EU-NIS2]], because a directive binds the member state and
its competent authority is designated nationally. Both would describe an
arrangement that does not legally exist yet.

The edges run the other way. [[IE-NCS-BILL]] carries `applies-to` this
entity — the Bill *assigns competent-authority functions* to the NCSC and to
CSIRT-IE, which is a sourced fact about the Bill's **content** and true
whether or not it has been enacted — and `implements-requirement-from`
[[EU-NIS2]]. Both are at `confidence: low`, inherited from the Bill's
`status: proposed`.

## The Atlas's third naming collision on "NCSC"

Three countries in the Atlas now have a body called the National Cyber
Security Centre:

| ID | Country | Situation |
|---|---|---|
| [[GB-NCSC]] | GB | part of [[GB-GCHQ]]; explicitly **not** the NIS competent authority |
| **IE-NCSC** | IE | **will be** the NIS2 competent authority |
| [[CH-BACS]] | CH | renamed *from* NCSC; still publishes at `ncsc.admin.ch` |

The scoped ID convention keeps them apart, and the Netherlands has a fourth
NCSC that the Atlas still does not hold — logged since the Belgium batch as
the reason [[NL-CBW]] is a NIS2 act with no authority attached.

The UK/Ireland contrast is the useful one: same name, opposite answers on
the same question of whether the body is the NIS competent authority.

## Not modelled

- **CSIRT-IE**, which [[IE-NCS-BILL]] also designates.
- The **Department of the Environment, Climate and Communications**, the
  NCSC's parent.
- The **Cyber Fundamentals Framework (CyFun)** — see [[IE-NCS-BILL]].

## Sources

Listed in frontmatter.
