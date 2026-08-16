---
id: NL-BRV
type: platform
name: Basisregistratie Voertuigen
alternative_names:
  - BRV
  - Kentekenregister
  - Base Registry of Vehicles
description: >
  The Dutch base registry of vehicles, held by the RDW since 1 July 2008 and
  one of the ten registrations in the stelsel van basisregistraties. It
  contains vehicle data, vehicle registration certificates and information
  about the persons to whom registration certificates are issued, and the
  RDW provides information from it to other users. The RDW is the stelsel's
  own worked example of an organisation occupying several roles at once: it
  holds this register and provides it to others while also receiving data
  from the persons register.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2008-07-01
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-MOBILITY
organisations:
  - NL-RDW
related_entities:
  - NL-BASISREGISTRATIES
  - NL-RDW
  - NL-BRP
relationships:
  - type: part-of
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "The ten base registrations are the BRP, HR, BAG, BRT, BRK, BRV (Basisregistratie Voertuigen), BRI, WOZ, BGT and BRO (digitaleoverheid.nl '10 basisregistraties'; data.overheid.nl; noraonline.nl). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NL-RDW
    source: fact
    evidence: "The Basisregistratie Voertuigen contains vehicle data, vehicle registration certificates and information about persons to whom registration certificates are issued, with the RDW providing information from this registration; the RDW has held the BRV since 1 July 2008, and the stelsel documentation gives the RDW as its example of an organisation that is holder, provider and user at once — maintaining the licence-plate register and providing it to other users while also receiving BRP data (digitaleoverheid.nl BRV page and 'Rollen Stelsel van basisregistraties'; rdw.nl). NOT READ — search-only."
    confidence: medium
    valid_from: 2008-07-01
    valid_until: null

sources:
  - title: "Basisregistratie Voertuigen (BRV) — Stelsel van basisregistraties"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/10-basisregistraties/brv/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "Rollen — Stelsel van basisregistraties"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/rollen-stelsel-basisregistraties/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "Basisregistraties: de 10 basisregistraties"
    url: "https://data.overheid.nl/community/group/basisregistraties_10"
    publisher: "data.overheid.nl"
---

# BRV — Basisregistratie Voertuigen

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The BRV is the Dutch base registry of vehicles — the *kentekenregister* —
held by [[NL-RDW]] since **1 July 2008**. It contains vehicle data, vehicle
registration certificates, and information about the persons to whom those
certificates are issued.

## The stelsel's own example of multiple roles

The `digitaleoverheid.nl` page on roles within the stelsel uses the RDW as
its worked example, and it is worth quoting because it is the clearest
statement of how the system is meant to work:

> An organisation can be a provider, holder, and user at the same time, such
> as the RDW which maintains the licence plate register (holder) and
> provides it to other users while also receiving BRP data.

So the RDW **holds** this register, **provides** it, and **consumes**
[[NL-BRP]].

The Atlas records one of those three. `maintained-by` covers holding and
providing well enough; **the consumption of BRP data is not modelled**, for
the same reason the Belastingdienst's use of the WOZ is not — there is no
relationship type for authorised use.

That the stelsel's own documentation chooses this exact example to explain
itself, and that the Atlas can express only part of it, is the sharpest
illustration in this batch of what the missing vocabulary costs.

## A register that is also personal data

The BRV holds information about the **persons** to whom registration
certificates are issued, which makes it a personal-data register as well as
a vehicle register — and therefore in scope for [[EU-GDPR]] and
[[NL-UAVG]].

**No relationship to either is asserted.** Nothing read connects them, and
"a register containing personal data is subject to data protection law" is a
legal inference, not a sourced fact about this register. It is the kind of
obviously-true statement the Atlas's provenance model exists to keep out
until someone reads a page that says it.

## Relationships

- `part-of` [[NL-BASISREGISTRATIES]].
- `maintained-by` [[NL-RDW]].

## Sources

Listed in frontmatter.
