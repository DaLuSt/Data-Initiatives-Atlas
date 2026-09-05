---
id: NL-NCTV
type: organisation
name: Nationaal Coördinator Terrorismebestrijding en Veiligheid
alternative_names:
  - NCTV
description: >
  Dutch national coordinator for counter-terrorism, cybersecurity, national
  security, crisis management and resilience against state threats.
  Organisationally structured as a directorate-general within the Ministry
  of Justice and Security. Publishes guidance and coordination material for
  the Cyberbeveiligingswet and the Wet weerbaarheid kritieke entiteiten,
  the sector-by-sector "doorverwijsboom" of competent authorities among
  them.

level: national
country: NL
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-CYBERSECURITY
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - NL-NCSC
  - NL-CBW
  - NL-WWKE
relationships:
  - type: part-of
    target: NL
    source: fact
    evidence: "Anchor edge (metadata/relationship-types.md §2.3): NCTV is a body of the Dutch state. Confirmed by reading nctv.nl's own 'Organisatie' page and rijksoverheid.nl's own organogram page directly (2026-09-05): both name NCTV as part of the Ministerie van Justitie en Veiligheid, organised like a directorate-general within it. No Ministry-of-Justice-and-Security entity exists yet in the Atlas to carry a more specific edge; [[NL-NCSC]]'s own file separately notes 'The NCTV and the Ministry of Justice and Security more broadly' as its own unmodelled parent context."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Organisatie"
    url: "https://www.nctv.nl/organisatie"
    publisher: "Nationaal Coördinator Terrorismebestrijding en Veiligheid (NCTV)"
    accessed: "2026-09-05"
  - title: "Nationaal Coördinator Terrorismebestrijding en Veiligheid (NCTV)"
    url: "https://www.rijksoverheid.nl/ministeries/ministerie-van-justitie-en-veiligheid/organisatie/organogram/nationaal-coordinator-terrorismebestrijding-en-veiligheid-nctv"
    publisher: "Rijksoverheid (Ministerie van Justitie en Veiligheid)"
    accessed: "2026-09-05"
  - title: "Wet weerbaarheid kritieke entiteiten"
    url: "https://www.nctv.nl/onderwerpen/v/vitale-infrastructuur/wet-weerbaarheid-kritieke-entiteiten"
    publisher: "Nationaal Coördinator Terrorismebestrijding en Veiligheid (NCTV)"
    accessed: "2026-09-05"
---

# NCTV — Nationaal Coördinator Terrorismebestrijding en Veiligheid

> **Added 2026-09-05, `verification: primary-source` from creation.**
> `discovery/research-queue.md` had flagged "NCSC / NCTV" jointly as
> "cybersecurity authorities named in Cyberbeveiligingswet sources." NCSC
> was already modelled ([[NL-NCSC]]); this pass closes the NCTV half by
> reading `nctv.nl`'s own organisation page and `rijksoverheid.nl`'s own
> organogram page directly.

## Description

The NCTV protects the Netherlands against threats that could disrupt
society. Reading `nctv.nl`'s own page directly, its mission is stated in
its own words: **"The NCTV serves national security. We protect interests,
signal threats and strengthen resilience,"** organised around three
societal objectives — **counter-terrorism, cybersecurity and state-level
threats** — alongside responsibilities for protecting facilities, persons
and national events, and civil aviation oversight.

Both `nctv.nl`'s own page and `rijksoverheid.nl`'s own organogram, read
directly, confirm NCTV is part of the **Ministry of Justice and Security**
(Ministerie van Justitie en Veiligheid), organised like a
directorate-general within it. Neither page read this pass gives an
establishment date or confirms secondary reporting that NCTV formed from a
2012 merger of the former National Counter-Terrorism Coordinator (NCTb),
the national-security directorate and GovCert — so `start_date` is left
`null` rather than asserted on unconfirmed sourcing.

## Publishes the Wwke/Cbw coordination material

Reading `nctv.nl`'s own [[NL-WWKE]] page directly: NCTV is the publisher of
that act's own guidance, and states the substantive link between the
Wwke and [[NL-CBW]] — a critical entity designated under the Wwke
automatically becomes an essential entity under the Cbw. [[NL-CBW]]'s own
file separately credits `nctv.nl` as one of two sources (with `ncsc.nl`)
describing the sector-by-sector "doorverwijsboom" (routing tree) of
competent authorities and CSIRTs under that act.

## Relationships

- `part-of` [[NL]] — anchor edge; no Ministry-of-Justice-and-Security
  entity exists yet to carry a more specific `part-of` relationship.

## Sources

Listed in frontmatter, all three read directly this pass.
