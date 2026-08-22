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
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
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
    evidence: "Confirmed verbatim by reading a Datatilsynet administrative-fine decision directly (2026-08-22): 'The Norwegian Data Protection Authority (hereinafter \"Datatilsynet\", \"we\", \"us\", \"our\") is the independent supervisory authority responsible for monitoring the application of the General Data Protection Regulation (\"GDPR\") with respect to Norway.' Independently confirmed on linklaters.com, read directly: 'The Norwegian Data Protection Authority will continue to act as the supervisory authority in Norway.' lovdata.no's own metadata record for the Act confirms its 20 July 2018 effective date."
    confidence: medium
    valid_from: 2018-07-20
    valid_until: null

sources:
  - title: "Data Protected — Norway"
    url: "https://www.linklaters.com/en/insights/data-protected/data-protected---norway"
    publisher: "Linklaters"
    accessed: "2026-08-22"
  - title: "Data protection laws in Norway"
    url: "https://www.dlapiperdataprotection.com/index.html?t=law&c=NO"
    publisher: "DLA Piper"
    accessed: "2026-08-22"
  - title: "Datatilsynet — administrative fine decision (example of published enforcement)"
    url: "https://www.datatilsynet.no/contentassets/f974410ee2e142c99cfc208cbae7634e/administrative-fine---sats-asa.pdf"
    publisher: "Datatilsynet"
    accessed: "2026-08-22"
---

# Datatilsynet

> **Verified 2026-08-22.** All three cited pages were read directly and
> confirm the claims below, verbatim in places — including Datatilsynet's
> own published administrative-fine decision, which states the
> authority's mandate in its own words.

## Description

Confirmed verbatim by reading Datatilsynet's own published SATS ASA
administrative-fine decision directly (2026-08-22): "The Norwegian Data
Protection Authority (hereinafter 'Datatilsynet', 'we', 'us', 'our') is
the independent supervisory authority responsible for monitoring the
application of the General Data Protection Regulation ('GDPR') with
respect to Norway." Datatilsynet is Norway's data protection supervisory authority, designated
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

Listed in frontmatter, all three read directly this pass. What was once
this entity's weakest point turned out to be its strongest: the "only a
published fine" citation, read directly, opens with the authority
describing its own mandate in its own words — a better source than either
commercial law-firm survey.
