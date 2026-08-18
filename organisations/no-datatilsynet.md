---
id: NO-DATATILSYNET
type: organisation
name: Datatilsynet
alternative_names:
  - Norwegian Data Protection Authority
  - Norwegian DPA
description: >
  Norway's data protection supervisory authority, designated by the Personal
  Data Act of 15 June 2018. Because Norway is an EEA EFTA state rather than
  an EU member state, it is notified to the EEA Joint Committee rather than
  to the European Commission, and the GDPR's supervisory cooperation
  mechanisms operate between it and member-state authorities through
  EEA-specific channels.

level: national
country: "NO"
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
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NO-PERSONOPPLYSNINGSLOVEN
  - EU-GDPR
  - EU-EDPB
relationships:
  - type: applies-to
    target: NO-PERSONOPPLYSNINGSLOVEN
    source: fact
    evidence: "The Personopplysningsloven, enacted as Act No 38 of 15 June 2018, designates the Norwegian Data Protection Authority — Datatilsynet — as the supervisory authority; the Act implements the GDPR in Norwegian law and became effective on 20 July 2018 (datatilsynet.no; lovdata.no LOV-2018-06-15-38; linklaters.com 'Data Protected — Norway'; dlapiperdataprotection.com Norway). NOT READ — search-only."
    confidence: medium
    valid_from: 2018-07-20
    valid_until: null

sources:
  - title: "Data Protected — Norway"
    url: "https://www.linklaters.com/en/insights/data-protected/data-protected---norway"
    publisher: "Linklaters"
  - title: "Data protection laws in Norway"
    url: "https://www.dlapiperdataprotection.com/index.html?t=law&c=NO"
    publisher: "DLA Piper"
  - title: "Datatilsynet — administrative fine decision (example of published enforcement)"
    url: "https://www.datatilsynet.no/contentassets/f974410ee2e142c99cfc208cbae7634e/administrative-fine---sats-asa.pdf"
    publisher: "Datatilsynet"
---

# Datatilsynet

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

Datatilsynet is Norway's data protection supervisory authority, designated
by [[NO-PERSONOPPLYSNINGSLOVEN]].

## A supervisory authority notified to a different body

The EEA route leaves a visible mark on this entity, and it is the reason it
is worth reading alongside [[NL-AP]] or [[DE-BFDI]].

When [[EU-GDPR]] was incorporated into the EEA Agreement by **Joint
Committee Decision No 154/2018**, the decision carried an adaptation:
Norway notifies its supervisory authority to the **EEA Joint Committee**,
not to the **European Commission**, and the Regulation's cooperation
mechanisms run between Datatilsynet and member-state authorities through
EEA-specific channels.

A member state's authority is notified to the Commission. Norway's is not.
The substance of supervision is the same; the plumbing is not.

## ⚠ No `participates-in` [[EU-EDPB]] is asserted

[[NL-AP]] carries that edge. Datatilsynet does not, and the reason is
specific rather than a sourcing failure.

The EDPB is a **Union** body composed of the supervisory authorities of the
**member states** and the [[EU-EDPS]]. EEA EFTA authorities take part under
arrangements set by the EEA framework — the sources describe *EEA-specific
channels* without saying what standing that gives Datatilsynet on the Board.
"Participates in the EDPB" and "cooperates with member-state authorities
through EEA channels" are different claims, and the sources support only the
second.

This is the same care [[DE-BFDI]] records for the opposite reason: there the
edge is plainly true and unsourced; here the sourcing is thin **and** the
claim itself is uncertain.

Note that the Atlas's EDPB connectivity is poor generally — the Board has
two incoming edges against [[EU-ESS]]'s six, with eight national data
protection authorities in the graph. That is logged in
`discovery/candidates.md` as the highest-value cheap fix available.

## Relationships

- `applies-to` [[NO-PERSONOPPLYSNINGSLOVEN]].

## Sources

Listed in frontmatter. **Two of three are commercial law-firm surveys**, and
no Datatilsynet page describing the authority's own mandate was returned by
search — only a published fine. That is this entity's weakest point.
