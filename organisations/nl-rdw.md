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
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-KVK
relationships:
  - type: participates-in
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "The kentekenregister has served as the basisregistratie voertuigen since 1 July 2008 (rdw.nl kerntaken; digitaleoverheid.nl BRV page). NOT READ — search-only."
    confidence: medium
    valid_from: 2008-07-01
    valid_until: null

sources:
  - title: "Kentekenregister is basisregistratie voertuigen"
    url: "https://www.rdw.nl/over-rdw/organisatie/kerntaken/kentekenregister-is-basisregistratie-voertuigen"
    publisher: "RDW"
  - title: "BRV — Stelsel van basisregistraties"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/10-basisregistraties/brv/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "BRV (Basisregistratie Voertuigen)"
    url: "https://www.noraonline.nl/wiki/BRV_(Basisregistratie_Voertuigen)"
    publisher: "NORA Online (ICTU)"
---

# RDW

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

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

## Relationships

- Participates in [[NL-BASISREGISTRATIES]] as holder of the BRV, since
  1 July 2008.

## Sources

Listed in frontmatter.
