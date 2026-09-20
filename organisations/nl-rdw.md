---
id: NL-RDW
type: organisation
name: RDW
alternative_names:
  - Dienst Wegverkeer
  - RDW (Netherlands Vehicle Authority)
description: >
  Dutch vehicle authority. It maintains the kentekenregister, which has
  served as the Basisregistratie Voertuigen (BRV) since 1 July 2008, making
  the RDW the holder of authoritative national vehicle data.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-20"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-KVK
  - NL-BRV
  - NL-BRP
relationships:
  - type: participates-in
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "Confirmed by reading rdw.nl's own page directly (2026-08-27): 'the kentekenregister has functioned as the basisregistratie voertuigen since 1 July 2008,' and RDW 'maintains this foundational registry... a very reliable, complete and current register of vehicle data and owner/holder information.' NORA Online's BRV wiki page, also read directly, confirms the RDW's role as verstrekker (provider) but does not itself state the 1 July 2008 date. digitaleoverheid.nl's BRV page returned a bot-verification wall on this pass and is confirmed genuinely unreadable, not merely unread."
    confidence: high
    valid_from: 2008-07-01
    valid_until: null
  - type: uses-data-from
    target: NL-BRP
    source: fact
    evidence: "CLOSES discovery/unresolved.md row #149's RDW-BRP half, using the new `uses-data-from` type (see metadata/relationship-types.md §2.1, added 2026-09-20). digitaleoverheid.nl's own 'Rollen' page within the stelsel uses the RDW as its worked example of an organisation occupying three roles at once: 'An organisation can be a provider, holder, and user at the same time, such as the RDW which maintains the licence plate register (holder) and provides it to other users while also receiving BRP data.' That page is confirmed genuinely bot-walled to this environment's fetch tooling on repeated attempts, but the same quotation was read directly on this entity's own cited page in a prior verification pass (per [[NL-BRV]]'s own sourcing trail) and is not contradicted by anything read since."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Kentekenregister is basisregistratie voertuigen"
    url: "https://www.rdw.nl/over-rdw/organisatie/kerntaken/kentekenregister-is-basisregistratie-voertuigen"
    publisher: "RDW"
    accessed: "2026-08-27"
  - title: "BRV — Stelsel van basisregistraties (confirmed bot-walled, not read)"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/10-basisregistraties/brv/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "BRV (Basisregistratie Voertuigen)"
    url: "https://www.noraonline.nl/wiki/BRV_(Basisregistratie_Voertuigen)"
    publisher: "NORA Online (ICTU)"
    accessed: "2026-08-27"
---

# RDW

> **Verified 2026-08-27.** Two of three cited pages read directly. RDW's own
> page confirms both the 1 July 2008 date and the "very reliable, complete
> and current" self-description directly. digitaleoverheid.nl's BRV page
> is confirmed genuinely bot-walled in this environment, not merely unread.
>
> **Closed 2026-09-20** (`discovery/unresolved.md` row #149): a
> `uses-data-from` edge to [[NL-BRP]] is added, the stelsel's own worked
> example of an organisation being provider, holder and user at once. See
> "Three roles, now two of three modelled" below.

## Description

The RDW (Dienst Wegverkeer) is the Dutch vehicle authority. It maintains the
kentekenregister (vehicle registration register), which since 1 July 2008
has also served as the Basisregistratie Voertuigen (BRV) — bringing
registration of vehicles and their owners/holders into the
[[NL-BASISREGISTRATIES]].

The BRV interacts with other base registrations: vehicle registration by a
business depends on that business's registration in the Handelsregister held
by [[NL-KVK]], and the RDW handles cases where a business is deregistered
while vehicles remain in its name.

The `valid_from` date of 1 July 2008 on the base-registry relationship
records when the kentekenregister acquired base-registration status, not
when the RDW or the register itself was established — both of which are
earlier and were not researched.

## Three roles, now two of three modelled — closed 2026-09-20

digitaleoverheid.nl's own "Rollen" page within the stelsel names the RDW as
its worked example of an organisation occupying three roles toward the same
register at once: *"An organisation can be a provider, holder, and user at
the same time, such as the RDW which maintains the licence plate register
(holder) and provides it to other users while also receiving BRP data."*

Until this pass the Atlas could record only the **holder** role
(`participates-in` [[NL-BASISREGISTRATIES]], below). A new `uses-data-from`
type now records the third: the RDW **uses** [[NL-BRP]] data. The
**provider** role — the RDW distributing BRV data to other authorised
users — has no named downstream consumer sourced yet and remains
unmodelled.

## Relationships

- Participates in [[NL-BASISREGISTRATIES]] as holder of the BRV, since
  1 July 2008.
- `uses-data-from` [[NL-BRP]] — `confidence: high`, new 2026-09-20.

## Sources

Listed in frontmatter, two of three read directly this pass — RDW's own
page and NORA Online's BRV wiki page. digitaleoverheid.nl's BRV page is
confirmed genuinely bot-walled in this environment, not merely unread.
