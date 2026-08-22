---
id: NL-MIDO
type: programme
name: Meerjarenprogramma Infrastructuur Digitale Overheid
alternative_names:
  - MIDO
description: >
  Dutch multi-year programme, running since 2022, in which central
  government, municipalities, provinces, water authorities and private
  service providers with a public task work together to modernise the
  Generieke Digitale Infrastructuur (GDI). Its bureau sits organisationally
  within the Ministry of the Interior and Kingdom Relations.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: 2022-07-12
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-BZK
  - NL-OBDO
related_entities:
  - NL-GDI
relationships:
  - type: governed-by
    target: NL-OBDO
    source: fact
    evidence: "The OBDO advises the responsible bewindspersoon on MIDO and the GDI; the OBDO chair is BZK's DGDOO (digitaleoverheid.nl MIDO governance page)."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: NL-GDI
    source: fact
    evidence: "MIDO is described as the framework for modernising the GDI (digitaleoverheid.nl, 'Wat is het MIDO?')."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Wat is het MIDO?"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/mido/wat-is-het-mido/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-08-22"
  - title: "Governance Meerjarenprogramma Infrastructuur Digitale overheid (MIDO)"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/mido/governance/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-08-22"
  - title: "Kabinetsbeleid MIDO"
    url: "https://www.digitaleoverheid.nl/mido/kabinetsbeleid/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-08-22"
  - title: "Voortgang MIDO (tijdlijn)"
    url: "https://www.digitaleoverheid.nl/mido/voortgang-mido/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-08-20"
  - title: "Besluit Sturing Digitale Overheid 2022 (Stcrt. 2022, 18861)"
    url: "https://zoek.officielebekendmakingen.nl/stcrt-2022-18861.html"
    publisher: "Ministerie van Binnenlandse Zaken en Koninkrijksrelaties"
    accessed: "2026-08-22"
---

# Meerjarenprogramma Infrastructuur Digitale Overheid (MIDO)

> **Verified 2026-08-20, deepened 2026-08-21.** Every cited source was read
> and confirmed to support what this entity says. `verification:
> primary-source`.

## Description

MIDO has been, since 2022, the framework within which central government,
municipalities, provinces, water authorities and private service providers
carrying out a public task work "as one government" to modernise the
[[NL-GDI]].

Its core is described as three components: the MIDO framework itself,
setting out governance principles and the agreements for central financing
of the GDI; the *Meerjarenvisie Digitale Overheid*, describing the intended
development of the digital government over a five-year horizon; and the GDI
programming plan (programmeringsplan), giving an overview of the activities
programmed for the coming year.

Bureau MIDO sits organisationally under [[NL-BZK]]'s Directorate Digital
Government, in a coordinating and facilitating role. Political
responsibility rests with the responsible state secretary, advised by the
[[NL-OBDO]]. The Atlas deliberately does not record which individual
currently holds that office — office-holder facts go stale silently, and
this one could not be verified; see `discovery/unresolved.md`.

## `start_date` corrected: 2022-01-01 was a placeholder, now 2022-07-12

The previous `start_date` recorded only "since 2022" as a year with no cited
day — an implicit 1 January placeholder. The *Besluit Sturing Digitale
Overheid 2022* (Stcrt. 2022, 18861), signed by the State Secretary for BZK
on **12 July 2022**, is confirmed as the amendment to [[NL-OBDO]]'s founding
Instellingsbesluit that introduces multi-year programming
(*meerjarenprogrammering*) on the generic digital infrastructure — MIDO's
direct legal basis. `start_date` now reflects that signing date rather than
a year-only guess.

**A second source has gone dead since 2026-08-20.** The "Voortgang MIDO"
timeline page now returns `404 Not Found`; no replacement URL was located.
Combined with a dead link found the same day on [[NL-OBDO]], this suggests
digitaleoverheid.nl reorganised some of its digital-government pages between
2026-08-20 and this pass — worth watching if more dead links turn up
elsewhere in this cluster.

## Relationships

- Governed via [[NL-OBDO]]; bureau sits within [[NL-BZK]].
- Modernises [[NL-GDI]].

## Sources

Listed in frontmatter.
