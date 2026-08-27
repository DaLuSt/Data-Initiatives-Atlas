---
id: NL-GEONOVUM
type: organisation
name: Geonovum
alternative_names: []
description: >
  Dutch standardisation organisation for geo-information. Geonovum develops
  and manages the Dutch base set of geo-standards, intended to make
  geographic information findable, accessible, exchangeable and reusable
  through the national geo-information infrastructure.

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
  - DOMAIN-GEOSPATIAL
organisations: []
related_entities:
  - NL-KADASTER
  - NL-TNO
  - NL-BZK
relationships:
  - type: aligned-with
    target: NL-BOMOS
    source: fact
    evidence: "Confirmed by reading docs.geostandaarden.nl's own 'Beheer basis geo-standaarden' page directly (2026-08-27), which quotes Geonovum in its own words: 'Geonovum uses BOMOS for all standards it manages, to guarantee that these are open according to the definition that BOMOS gives to this.' The same page states Geonovum received the 'excellent management process' ('voorbeeldig beheerproces') designation from Forum Standaardisatie and the Nationaal Beraad Digitale Overheid in 2014 for its geo-standards management — previously recorded as 'December 2014'; the page read this pass gives the year 2014 without a specific month, so the date precision has been reduced to match what was actually confirmed."
    confidence: high
    valid_from: null
    valid_until: null
  - type: aligned-with
    target: NL-FORUM-STANDAARDISATIE
    source: interpretation
    evidence: "Both maintain open standards for Dutch public bodies, Geonovum for the geo domain and Forum Standaardisatie government-wide. No sourced statement of a formal relationship between them was found this pass either; recorded as interpretation."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Over Geonovum"
    url: "https://www.geonovum.nl/over-geonovum"
    publisher: "Geonovum"
    accessed: "2026-08-27"
  - title: "Geo-standaarden"
    url: "https://www.geonovum.nl/geo-standaarden"
    publisher: "Geonovum"
    accessed: "2026-08-27"
  - title: "Beheer basis geo-standaarden"
    url: "https://docs.geostandaarden.nl/gbd/gsb/"
    publisher: "Geonovum"
    accessed: "2026-08-27"
  - title: "Geonovum Uitvoeringsplan 2025, versie 1.0, 1 november 2024"
    url: "https://www.geonovum.nl/uploads/documents/Geonovum%20Uitvoeringsplan%202025%20v1.0.pdf"
    publisher: "Geonovum"
---

# Geonovum

> **Verified 2026-08-27.** Three of four cited pages were read directly
> this pass, closing the previous `search-only` status (never previously
> `last_verified`). The Uitvoeringsplan PDF was not re-fetched.

## Description

Geonovum develops and manages the Dutch base set of geo-standards.
Reading geonovum.nl's own pages directly confirms its purpose in the
organisation's own words: to work towards "improve[d] government
performance with geo-information" by making geographic information
findable, accessible, exchangeable and reusable via the national
geo-information infrastructure.

Its standards management is documented rather than ad hoc, and its use of
the **BOMOS** model is now a directly-confirmed fact rather than a
search-only claim: reading `docs.geostandaarden.nl` — a Geonovum-run
documentation site — directly quotes Geonovum's own statement that it
"uses BOMOS for all standards it manages, to guarantee that these are open
according to the definition that BOMOS gives to this." The same page
confirms Geonovum received the **"excellent management process"**
designation from Forum Standaardisatie and the Nationaal Beraad Digitale
Overheid in **2014**, for its geo-standards management — the previous
"December 2014" precision is not supported by what was read this pass and
has been softened to the year alone.

Its base programme is funded by subsidy from the ministries of the Interior
and Kingdom Relations ([[NL-BZK]]) and of Agriculture, by [[NL-KADASTER]]
and by the Geological Survey of the Netherlands, part of [[NL-TNO]] —
confirmed directly on geonovum.nl's own "Over Geonovum" page, which also
names **Rijkswaterstaat** among the funders, not previously recorded here.
Geonovum reports on this spending to its subsidy providers and through its
annual report.

The Programmaraad and BOMOS itself are not yet separate Atlas entities.
BOMOS in particular is a Dutch standards-management model likely to warrant
its own entity in a future batch; it remains queued in
`discovery/research-queue.md`.

## Relationships

- Funded by [[NL-BZK]], [[NL-KADASTER]] and [[NL-TNO]], and also
  Rijkswaterstaat (not yet an Atlas entity), per this pass's direct
  reading.
- `aligned-with` [[NL-BOMOS]] — now `source: fact`, confirmed directly in
  Geonovum's own words.
- Domain-specific counterpart to [[NL-FORUM-STANDAARDISATIE]] (Atlas
  interpretation — no sourced formal relationship, unchanged this pass).

## Atlas interpretation

The `aligned-with` relationship to Forum Standaardisatie remains an Atlas
reading of two bodies occupying complementary standardisation roles, not a
documented arrangement.

## Sources

Three of four read directly this pass: both `geonovum.nl` pages and the
`docs.geostandaarden.nl` management-process page. The Uitvoeringsplan PDF
was not re-fetched.
