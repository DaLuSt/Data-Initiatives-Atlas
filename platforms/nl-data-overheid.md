---
id: NL-DATA-OVERHEID
type: platform
name: data.overheid.nl
alternative_names:
  - Dataregister van de Nederlandse Overheid
  - Nationaal Dataportaal
description: >
  The Dutch national open data portal, where data made available by
  government bodies can be found. More than 180 government organisations
  publish data through it. Datasets are described using the DCAT metadata
  standard.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-30"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-BZK
  - NL-LOGIUS
related_entities:
  - NL-WHO
  - NL-LOGIUS
relationships:
  - type: depends-on
    target: NL-DCAT-AP-NL
    source: fact
    evidence: "standaarden.overheid.nl, read directly (2026-08-27), states datasets on data.overheid.nl are described using DCAT (referred to there as an EU DCAT-AP-based Dutch profile, 'DCAT-NL' / 'IPM voor datasets'). Neither data.overheid.nl's own front page nor opennederland.nl, both also read directly, names DCAT explicitly, so the specific mechanism is confirmed by the third source rather than the two originally cited."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NL-LOGIUS
    source: fact
    evidence: "Confirmed by reading koopoverheid.nl's own page directly (2026-08-30): KOOP describes itself as 'de drijvende kracht achter de grootste portalen met overheidsinformatie op internet: overheid.nl, wetten.nl en officielebekendmakingen.nl. Via het platform Data.overheid.nl kunnen overheidsorganisaties data delen' (the driving force behind the largest portals with government information on the internet ... via the Data.overheid.nl platform, government organisations can share data) — naming KOOP as the body behind the platform, not merely a data-owning participant. koopoverheid.nl's own site, read directly, also states 'Sinds 1 januari 2023 maakt KOOP onderdeel uit van Logius' (since 1 January 2023, KOOP has been part of Logius), which is why the edge points at Logius: KOOP is the operational team, but it has been organisationally absorbed into Logius, itself part of [[NL-BZK]], for over three years. This closes the previous open question — the entity's prior text found both KOOP and Logius named as dataset owners without either confirmed as the platform's actual operator."
    confidence: medium
    valid_from: 2023-01-01
    valid_until: null

sources:
  - title: "Dataregister van de Nederlandse Overheid"
    url: "https://data.overheid.nl/"
    publisher: "Overheid.nl"
    accessed: "2026-08-27"
  - title: "Data.overheid.nl"
    url: "https://www.opennederland.nl/platforms/data-overheid/"
    publisher: "Vereniging Open Nederland"
    accessed: "2026-08-27"
  - title: "DCAT — standaarden.overheid.nl"
    url: "https://standaarden.overheid.nl/dcat"
    publisher: "Overheid.nl"
    accessed: "2026-08-27"
  - title: "Data.overheid.nl | KOOP Kennis- en exploitatiecentrum officiële overheidspublicaties"
    url: "https://www.koopoverheid.nl/open-data--linked-data/data.overheid.nl"
    publisher: "KOOP (part of Logius since 1 January 2023)"
    accessed: "2026-08-30"
---

# data.overheid.nl

> **Custodian confirmed 2026-08-30.** A research-queue item open since
> Batch 1 — the operator of this portal, the only one of the Atlas's
> national open-data portals with no custodian modelled — is now closed.
> `koopoverheid.nl`'s own page, read directly, names KOOP as the body
> "behind" the platform, and states in its own words that KOOP has been
> part of Logius since 1 January 2023. The `maintained-by` edge points at
> [[NL-LOGIUS]] accordingly: KOOP is the operational team, but it has sat
> inside Logius for over three years.

## Description

data.overheid.nl is the national data portal of the Dutch government.
Confirmed by reading data.overheid.nl directly: it presents itself as "the
National Data Portal of the Dutch government" and functions as a registry
describing government data, both open and closed — the front page itself
did not state a specific count of participating organisations this pass (it
surfaced a total of 27,087 search results across content types instead), so
the "more than 180 government organisations" figure is carried over
unconfirmed from the prior text rather than independently verified.

Its datasets are described with metadata using DCAT, confirmed by reading
standaarden.overheid.nl directly — which is where this platform connects to
the standards layer: the Dutch profile [[NL-DCAT-AP-NL]] is what makes those
descriptions interoperable with other Dutch catalogues and with European
data catalogues.

It is also the operational counterpart to [[NL-WHO]]: the re-use obligations
in that act, including the designation of high-value datasets, are what this
portal exists to serve. The precise legal relationship was not sourced, so
no relationship is asserted beyond the association.

**The portal's operator is now confirmed.** A prior pass narrowed the
question to two named candidates — KOOP and Logius — without confirming
either as the platform's actual operator. This pass closes it: reading
`koopoverheid.nl`'s own page directly, KOOP describes itself as the
"driving force" behind data.overheid.nl (among other government-information
portals), and states in its own words that it has been part of [[NL-LOGIUS]]
since **1 January 2023**. [[NL-LOGIUS]] itself sits under [[NL-BZK]].

## Relationships

- Depends on [[NL-DCAT-AP-NL]] for dataset metadata — confirmed 2026-08-27.
- Serves the re-use regime established by [[NL-WHO]].
- `maintained-by` [[NL-LOGIUS]] — confirmed 2026-08-30, closing a
  research-queue item open since Batch 1.

## Sources

Listed in frontmatter, four of four read directly: the three original
pages (2026-08-27) plus `koopoverheid.nl`'s own page confirming the
operator (2026-08-30).
