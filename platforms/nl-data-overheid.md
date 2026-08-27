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
last_verified: "2026-08-27"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-BZK
related_entities:
  - NL-WHO
relationships:
  - type: depends-on
    target: NL-DCAT-AP-NL
    source: fact
    evidence: "standaarden.overheid.nl, read directly (2026-08-27), states datasets on data.overheid.nl are described using DCAT (referred to there as an EU DCAT-AP-based Dutch profile, 'DCAT-NL' / 'IPM voor datasets'). Neither data.overheid.nl's own front page nor opennederland.nl, both also read directly, names DCAT explicitly, so the specific mechanism is confirmed by the third source rather than the two originally cited."
    confidence: medium
    valid_from: null
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
---

# data.overheid.nl

> **Verified 2026-08-27.** Both originally-cited pages were read directly,
> plus a third (standaarden.overheid.nl) added to confirm the DCAT
> dependency neither original page actually states. `verification` moves
> from `search-only` to `primary-source`.

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

**The portal's operator remains not firmly established**, though this pass
narrowed the question. A targeted search surfaced (but did not directly
confirm via a fetched page) that the Open Data-team of KOOP works on
data.overheid.nl and that Logius — part of [[NL-BZK]] — develops and
manages it; data.overheid.nl's own organisation-filter page, read directly,
lists both KOOP and Logius as data owners of specific datasets without
stating either as the platform's operator. The `organisations: [NL-BZK]`
entry is therefore left as an **Atlas association pointing in a plausible
direction** (both named candidates sit under BZK) rather than a fully
sourced operator claim.

## Relationships

- Depends on [[NL-DCAT-AP-NL]] for dataset metadata — confirmed this pass.
- Serves the re-use regime established by [[NL-WHO]].

## Sources

Listed in frontmatter, all three read directly this pass.
