---
id: IE-NCSC
type: organisation
name: National Cyber Security Centre
alternative_names:
  - NCSC Ireland
description: >
  Ireland's national cyber security centre, founded in 2011, which will act
  as lead authority for oversight and enforcement once the NIS2 Directive
  is transposed by the National Cyber Security Bill. It has published
  cyber governance guidance for management boards ahead of that
  implementation.

level: national
country: IE
region: EU

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
    accessed: "2026-08-22"
  - title: "NCSC: NIS2 FAQ"
    url: "https://www.ncsc.gov.ie/nis2/FAQ/"
    publisher: "National Cyber Security Centre (Ireland)"
    accessed: "2026-08-22"
  - title: "Irish NCSC Issues Cyber Governance Guidance for Management Boards Ahead of NIS2 Implementation"
    url: "https://www.globalpolicywatch.com/2026/07/irish-ncsc-issues-cyber-governance-guidance-for-management-boards-ahead-of-nis2-implementation/"
    publisher: "Covington — Global Policy Watch"
    accessed: "2026-08-22"
  - title: "NCSC: National Cyber Security Centre"
    url: "https://www.ncsc.gov.ie/"
    publisher: "National Cyber Security Centre (Ireland)"
    accessed: "2026-08-22"
---

# National Cyber Security Centre (IE-NCSC)

> **Verified 2026-08-22.** All four cited pages were read directly and
> confirmed the claims below, verbatim in places. The `name` field has
> been changed from "National Cyber Security Centre (Ireland)" — a
> disambiguation not attested on any source — to "National Cyber Security
> Centre," matching how [[GB-NCSC]] carries the same name: the scoped ID
> (`IE-NCSC`), not the display name, does the disambiguating.

## Description

Confirmed by reading globalpolicywatch.com directly (2026-08-22): "On
July 7, 2026, the Irish National Cyber Security Centre ('NCSC') published
guidance for management boards and senior executives of organizations
subject to the EU's Network and Information Security Directive ('NIS2')."
Ireland's NCSC is the **current designated national competent authority**
for digital service providers under the still-unamended NIS1 regime —
confirmed on the European Commission's own tracker — and is expected to
take on a wider lead-authority role once [[IE-NCS-BILL]] transposes
[[EU-NIS2]].

## An authority acting ahead of its own statute

The NCSC publishes NIS2 guidance, an FAQ ("Once the legislation is
implemented, both the NIS2 registration portal and the NIS2 incident
reporting portal will be available for use" — confirmed verbatim on
ncsc.gov.ie), and cyber governance guidance for management boards — while
the Bill that would give it its full competent-authority functions is
**not yet enacted**.

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

## A finding worth flagging: the NCSC's own parent department has changed

Confirmed verbatim on ncsc.gov.ie (2026-08-22): "The National Cyber
Security Centre (NCSC) was founded in **2011** and is an operational arm
of the **Department of the Justice, Home Affairs and Migration**." The
Atlas's earlier sourcing (via the European Commission's tracker, still
current for the DSP competent-authority role) names the Department of
Communications, Climate Action & Environment as the contact department.
Both may be correct for different functions, or a machinery-of-government
move may have happened since the tracker page was last updated (7 July
2025) — this was not resolved this pass, and no `organisations:` entry is
asserted for either department on that basis.

## Not modelled

- **CSIRT-IE** as a separate entity — see [[IE-NCS-BILL]] for the same
  caveat on whether the Bill's own text, as opposed to the current
  regime, designates it.
- The NCSC's parent department — see the finding above.
- The **Cyber Fundamentals Framework (CyFun)** — see [[IE-NCS-BILL]].

## Sources

Listed in frontmatter, all four read directly this pass.
