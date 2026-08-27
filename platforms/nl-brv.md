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
verification: primary-source

start_date: 2008-07-01
end_date: null
last_verified: "2026-08-27"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-MOBILITY
organisations:
  - NL-RDW
related_entities:
  - NL-WEGENVERKEERSWET-1994
  - NL-BASISREGISTRATIES
  - NL-RDW
  - NL-BRP
relationships:
  - type: governed-by
    target: NL-WEGENVERKEERSWET-1994
    source: fact
    evidence: "Confirmed by reading wetten.overheid.nl's own text of BWBR0006622 directly (2026-08-27): it is the Wegenverkeerswet 1994, which establishes the Dienst Wegverkeer (RDW) and its vehicle-registration functions among a much broader set of road-traffic rules (conduct, type-approval, licences, inspection, enforcement)."
    confidence: high
    valid_from: null
    valid_until: null
  - type: part-of
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "Confirmed by reading data.overheid.nl's basisregistraties_10 group listing directly (2026-08-27), which names 'Basisregistratie: Voertuigen (BRV)' among the ten. digitaleoverheid.nl's own BRV page and its page on roles within the stelsel both returned a bot-verification wall on two separate attempts each this pass ('Please wait while your request is being verified...') and are confirmed genuinely unreadable in this environment, not merely unread."
    confidence: high
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NL-RDW
    source: fact
    evidence: "Confirmed by reading rdw.nl's own page directly (2026-08-27): 'the kentekenregister has functioned as the basisregistratie voertuigen since 1 July 2008,' and the RDW 'maintains this foundational registry.' The stelsel's own worked example describing the RDW as simultaneously provider, holder and user is carried on digitaleoverheid.nl's rollen page, which is confirmed genuinely bot-walled this pass (see above) and was not independently re-read; the same quotation was, however, read directly on [[NL-RDW]]'s own cited page in a prior verification of that entity's sources and is not contradicted by anything read here."
    confidence: high
    valid_from: 2008-07-01
    valid_until: null

sources:
  - title: "Basisregistratie Voertuigen (BRV) — Stelsel van basisregistraties (confirmed bot-walled, not read)"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/10-basisregistraties/brv/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "Rollen — Stelsel van basisregistraties (confirmed bot-walled, not read)"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/rollen-stelsel-basisregistraties/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "Basisregistraties: de 10 basisregistraties"
    url: "https://data.overheid.nl/community/group/basisregistraties_10"
    publisher: "data.overheid.nl"
    accessed: "2026-08-27"
  - title: "Kentekenregister is basisregistratie voertuigen"
    url: "https://www.rdw.nl/over-rdw/organisatie/kerntaken/kentekenregister-is-basisregistratie-voertuigen"
    publisher: "RDW"
    accessed: "2026-08-27"
  - title: "Wegenverkeerswet 1994 — official text"
    url: "https://wetten.overheid.nl/BWBR0006622"
    publisher: "Overheid.nl (Basiswettenbestand)"
    accessed: "2026-08-27"
---

# BRV — Basisregistratie Voertuigen

> **Verified 2026-08-27.** Two new sources added and read directly this
> pass — the RDW's own kentekenregister page and the Wegenverkeerswet
> 1994's official text — pushed this entity to a genuine majority.
> digitaleoverheid.nl's BRV and rollen pages are confirmed genuinely
> bot-walled in this environment, not merely unread.

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

Listed in frontmatter, three of five read directly this pass — the RDW's own
page (added this pass), the Wegenverkeerswet 1994's official text (added
this pass), and the data.overheid.nl group listing. digitaleoverheid.nl's
BRV and rollen pages are confirmed genuinely bot-walled in this environment
on two separate attempts each, not merely unread.
