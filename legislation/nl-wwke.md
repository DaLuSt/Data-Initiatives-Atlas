---
id: NL-WWKE
type: law
name: Wet weerbaarheid kritieke entiteiten
alternative_names:
  - Wwke
  - Dutch Critical Entities Resilience Act
description: >
  Dutch implementing act for the EU Critical Entities Resilience (CER)
  Directive, in force since 15 August 2026. It strengthens the resilience
  of roughly 500 organisations across thirteen sectors against threats such
  as natural disasters, accidents, sabotage and terrorism, and requires
  significant incidents to be reported within 24 hours to a competent
  authority combining the responsible ministry and a supervisor. Passed
  alongside, and complementary to, the Cyberbeveiligingswet.

level: national
country: NL
region: EU

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: 2026-08-15
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - EU-CER
  - NL-CBW
  - NL-NCTV
relationships:
  - type: implements-requirement-from
    target: EU-CER
    source: fact
    evidence: "Confirmed by reading nctv.nl's own 'Wet weerbaarheid kritieke entiteiten' page directly (2026-09-05): the law implements 'de Critical Entities Resilience Directive (CER-richtlijn).'"
    confidence: high
    valid_from: 2026-08-15
    valid_until: null
  - type: related-to
    target: NL-CBW
    source: fact
    evidence: "Confirmed by reading nctv.nl directly (2026-09-05): critical entities designated under the Wwke automatically become essential entities under the Cyberbeveiligingswet, and rijksoverheid.nl's own 15 August 2026 news page, also read directly, confirms both acts entered into force on the same date and were approved together by the Tweede Kamer on 15 April 2026 (already recorded on NL-CBW's own file)."
    confidence: high
    valid_from: 2026-08-15
    valid_until: null

sources:
  - title: "Wet weerbaarheid kritieke entiteiten"
    url: "https://www.nctv.nl/onderwerpen/v/vitale-infrastructuur/wet-weerbaarheid-kritieke-entiteiten"
    publisher: "Nationaal Coördinator Terrorismebestrijding en Veiligheid (NCTV)"
    accessed: "2026-09-05"
  - title: "Cyberbeveiligingswet en Wet weerbaarheid kritieke entiteiten vanaf vandaag van kracht"
    url: "https://www.rijksoverheid.nl/actueel/nieuws/2026/08/15/cyberbeveiligingswet-en-wet-weerbaarheid-kritieke-entiteiten-vanaf-vandaag-van-kracht"
    publisher: "Rijksoverheid"
    accessed: "2026-09-05"
---

# Wet weerbaarheid kritieke entiteiten (Wwke)

> **Added 2026-09-05, `verification: primary-source` from creation.**
> `discovery/research-queue.md` had flagged this as "approved 15 Apr 2026,
> should mirror [[NL-CBW]] → [[EU-NIS2]]" — the sibling act approved and
> brought into force alongside the Cyberbeveiligingswet. Both cited pages
> were read directly this pass.

## Description

The Wwke is the Dutch implementation of the EU's [[EU-CER]] (Critical
Entities Resilience) Directive. Reading `nctv.nl`'s own page directly: it
strengthens the resilience of organisations providing essential services
against threats including natural disasters, accidents, sabotage and
terrorism. Reading `rijksoverheid.nl`'s own 15 August 2026 news page
directly: it covers **roughly 500 organisations** across **thirteen
sectors** — energy, transport, drinking water, healthcare, government,
digital infrastructure, banking, chemicals, financial market
infrastructure, wastewater, space, nuclear, land management, meteorology,
and food production/processing/distribution.

Responsible ministries designate the critical entities in their sector.
Oversight runs through **"the competent authority, consisting of the
responsible ministry and the supervisor,"** to whom significant incidents
must be reported within 24 hours.

## Entered into force alongside the Cyberbeveiligingswet

Both pages read directly confirm the Wwke entered into force on **15
August 2026**, the same date as [[NL-CBW]] — matching [[NL-CBW]]'s own
file, which records both bills' joint Tweede Kamer approval on 15 April
2026. `nctv.nl`'s own page adds a substantive link between the two: a
critical entity designated under the Wwke **automatically becomes an
essential entity** under the Cyberbeveiligingswet, making physical
resilience (Wwke) and digital/cyber resilience (Cbw) complementary,
sector-linked obligations rather than two independent regimes.

## Relationships

- Implements requirements from [[EU-CER]].
- `related-to` [[NL-CBW]] — jointly approved, jointly entered into force,
  and substantively linked (Wwke designation triggers Cbw obligations).

## Sources

Listed in frontmatter, both read directly this pass.
