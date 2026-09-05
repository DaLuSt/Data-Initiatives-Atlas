---
id: EU-EUROPEANA-FOUNDATION
type: organisation
name: Europeana Foundation
alternative_names:
  - Stichting Europeana
description: >
  Dutch-law foundation (stichting) that governs and operates Europeana,
  the platform providing multilingual access to tens of millions of
  digitised items from cultural heritage institutions across Europe. It
  is housed within the Koninklijke Bibliotheek, the national library of
  the Netherlands, employs the platform's staff, bids for funding and
  leads the consortium the European Commission selected to deploy the
  common European data space for cultural heritage.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2008-11-20
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - EU-CULTURAL-HERITAGE-DATA-SPACE
relationships:
  - type: produces
    target: EU-CULTURAL-HERITAGE-DATA-SPACE
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP — 'the batch's most conspicuous gap' per EU-CULTURAL-HERITAGE-DATA-SPACE's own text. Confirmed by reading en.wikipedia.org's 'Europeana' article directly (2026-09-05): 'The Europeana Foundation is the governing body of the Europeana service... incorporated under Dutch law as Stichting Europeana... housed within the Koninklijke Bibliotheek, the national library of the Netherlands,' and 'promotes collaboration between museums, archives, audiovisual collections and libraries so that users can have integrated access to their content through Europeana and other services,' 'employing the staff, bidding for funding and enabling the sustainability of the service.' EU-CULTURAL-HERITAGE-DATA-SPACE's own sourcing (a European Commission news page, read directly in an earlier pass) independently confirms the Commission selected a consortium led by the Europeana Foundation, in force since 20 September 2022, to deploy the data space Europeana underpins. Recorded as `produces` — the Foundation operates the platform the data space is built on, rather than the data space itself being a further output of an already-existing thing."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Europeana"
    url: "https://en.wikipedia.org/wiki/Europeana"
    publisher: "Wikipedia"
    accessed: "2026-09-05"
  - title: "Europeana Foundation (Q20875125)"
    url: "https://www.wikidata.org/wiki/Q20875125"
    publisher: "Wikidata"
    accessed: "2026-09-05"
    note: "Used only for the inception date (20 November 2008), which independently matches the Europeana platform's own well-documented prototype launch date given by Wikipedia. pro.europeana.eu's own 'About us' page returned HTTP 403 to this pass's fetch tooling and was not read."
---

# Europeana Foundation

> **Created 2026-09-05**, closing the gap `discovery/unresolved.md` and
> [[EU-CULTURAL-HERITAGE-DATA-SPACE]] itself had flagged as the batch's
> most conspicuous omission: the operator behind the data space's
> largest existing asset was named in that entity's own sourcing but
> never modelled.

## Description

Confirmed by reading en.wikipedia.org's "Europeana" article directly:
the Europeana Foundation — incorporated under Dutch law as **Stichting
Europeana** — is "the governing body of the Europeana service," housed
within the **Koninklijke Bibliotheek**, the national library of the
Netherlands. It "employs the staff, bids for funding and enables the
sustainability of the service," and "promotes collaboration between
museums, archives, audiovisual collections and libraries so that users
can have integrated access to their content through Europeana and other
services."

`start_date` records **20 November 2008**, per Wikidata's inception
field — a date that independently matches the Europeana platform's own
documented prototype-launch date (Wikipedia), so the two facts corroborate
rather than merely coincide. `pro.europeana.eu`'s own "About us" page,
which would carry the Foundation's own account of its founding, returned
HTTP 403 to this pass's fetch tooling and was not read.

## Why this is not a Dutch entity

Everything about the Foundation's legal seat is Dutch: Dutch-law
incorporation, housed in the Dutch national library, physically in The
Hague. It is nonetheless recorded as `country: null`, `region: EU`,
`level: regional`, with an `EU-` scope prefix — the same call this Atlas
made for [[EU-GAIA-X]] (Belgian-law AISBL) and [[EU-DSSC]] (an EU support
body with no single national seat asserted): what the sources describe is
a pan-European governing body for a Commission-designated data space,
not a Dutch national institution that happens to operate one.

## Relationships

- `produces` [[EU-CULTURAL-HERITAGE-DATA-SPACE]] — the Foundation governs
  and operates Europeana, the platform the data space is built on, and
  led the Commission-selected consortium deploying it.

## Not modelled

- The **Europeana Network Association** and the **Europeana Aggregators'
  Forum**, named alongside the Foundation in the data space's own
  deployment sourcing as co-participants, but not independently
  researched here.
- The **Europeana Data Model (EDM)**, which would connect to the Atlas's
  metadata-standards layer around [[INTL-DCAT]].

## Sources

Two sources, one (Wikipedia) read directly. Wikidata is cited for a
single structured fact (the inception date) corroborated independently
by Wikipedia's account of the platform's own launch. `pro.europeana.eu`
is confirmed genuinely blocked (HTTP 403), consistent with
[[EU-CULTURAL-HERITAGE-DATA-SPACE]]'s own experience with the same
domain in an earlier pass.
