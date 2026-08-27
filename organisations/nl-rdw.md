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
last_verified: "2026-08-27"
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
    evidence: "Confirmed by reading rdw.nl's own page directly (2026-08-27): 'the kentekenregister has functioned as the basisregistratie voertuigen since 1 July 2008,' and RDW 'maintains this foundational registry... a very reliable, complete and current register of vehicle data and owner/holder information.' NORA Online's BRV wiki page, also read directly, confirms the RDW's role as verstrekker (provider) but does not itself state the 1 July 2008 date. digitaleoverheid.nl's BRV page returned a bot-verification wall on this pass and is confirmed genuinely unreadable, not merely unread."
    confidence: high
    valid_from: 2008-07-01
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

Listed in frontmatter, two of three read directly this pass — RDW's own
page and NORA Online's BRV wiki page. digitaleoverheid.nl's BRV page is
confirmed genuinely bot-walled in this environment, not merely unread.
