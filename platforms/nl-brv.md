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
last_verified: "2026-09-20"
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
  - EU-GDPR
  - NL-UAVG
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
  - type: related-to
    target: EU-GDPR
    source: interpretation
    evidence: "NARROWS discovery/unresolved.md row #141, does not close it. rdw.nl's own privacy-statement page, read directly (2026-09-19), names the AVG ('Algemene Verordening Gegevensbescherming (AVG), de wet die in Nederland en de Europese Unie de bescherming van persoonsgegevens regelt') as the law governing how the RDW handles the personal data it processes, and a separate rdw.nl page, also read directly, states 'Voor het kentekenregister en het Nationaal Parkeer Register heeft een onafhankelijk instituut vastgesteld dat de RDW aan alle privacy-aspecten voldoet' (an independent institute has determined the RDW complies with all privacy aspects for the kentekenregister and the National Parking Register) and that owner name/address data ('de tenaamgestelde') is not public. No single sentence read on any rdw.nl page names the AVG and the kentekenregister/BRV together in the same statement, so this stops short of the sourced fact the row asks for; it is recorded as `source: interpretation` at `confidence: low` rather than left as a bare legal inference from 'contains personal data' alone."
    confidence: low
    valid_from: null
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
  - title: "Hoe beschermt de RDW mijn persoonsgegevens?"
    url: "https://www.rdw.nl/over-rdw/privacy-en-security/privacyverklaring/hoe-beschermt-de-rdw-mijn-persoonsgegevens"
    publisher: "RDW"
    accessed: "2026-09-19"
  - title: "Gegevens die de RDW registreert"
    url: "https://www.rdw.nl/over-rdw/privacy-en-security/privacyverklaring/gegevens-die-de-rdw-registreert"
    publisher: "RDW"
    accessed: "2026-09-19"
---

# BRV — Basisregistratie Voertuigen

> **Verified 2026-08-27.** Two new sources added and read directly this
> pass — the RDW's own kentekenregister page and the Wegenverkeerswet
> 1994's official text — pushed this entity to a genuine majority.
> digitaleoverheid.nl's BRV and rollen pages are confirmed genuinely
> bot-walled in this environment, not merely unread.
>
> **Narrowed 2026-09-19** (`discovery/unresolved.md` row #141): a
> low-confidence `related-to` [[EU-GDPR]] edge is added, sourced from
> two rdw.nl privacy pages read directly. See "A register that is also
> personal data" below.
>
> **Closed 2026-09-20** (`discovery/unresolved.md` row #149): the RDW's
> consumption of BRP data, described below, is now a typed `uses-data-from`
> edge recorded on [[NL-RDW]]'s own entity.

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

**Closed 2026-09-20**: `maintained-by` covers holding and providing well
enough; the consumption of BRP data is now recorded too, as a
`uses-data-from` edge on [[NL-RDW]]'s own entity — a new relationship type
added specifically because the stelsel's own documentation chose this exact
RDW example to explain itself, and the Atlas could previously express only
part of it. See metadata/relationship-types.md §2.1.

## A register that is also personal data — narrowed 2026-09-19

The BRV holds information about the **persons** to whom registration
certificates are issued, which makes it a personal-data register as well as
a vehicle register — and therefore, presumably, in scope for [[EU-GDPR]]
and [[NL-UAVG]].

`discovery/unresolved.md` row #141 flagged that nothing read connected the
two. That is now narrowed rather than closed: rdw.nl's own privacy pages,
read directly, name the **AVG** as the law governing how RDW handles
personal data generally, and separately state that "an independent
institute has determined that the RDW complies with all privacy aspects"
specifically **for the kentekenregister** (this entity), and that owner
name/address data is not public. No single sentence names the AVG and the
kentekenregister together, so the connection is recorded as a low-confidence
`related-to` [[EU-GDPR]] edge rather than the direct sourced fact the row
originally asked for. **No relationship to [[NL-UAVG]] specifically is
asserted** — nothing read names it at all, only the AVG.

## Relationships

- `part-of` [[NL-BASISREGISTRATIES]].
- `maintained-by` [[NL-RDW]].
- `related-to` [[EU-GDPR]] — `confidence: low`, narrowed not closed.

## Sources

Listed in frontmatter, three of five read directly this pass — the RDW's own
page (added this pass), the Wegenverkeerswet 1994's official text (added
this pass), and the data.overheid.nl group listing. digitaleoverheid.nl's
BRV and rollen pages are confirmed genuinely bot-walled in this environment
on two separate attempts each, not merely unread.
