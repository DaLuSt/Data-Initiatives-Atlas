---
id: GB-OSR
type: organisation
name: Office for Statistics Regulation
alternative_names:
  - OSR
description: >
  The independent regulator of official statistics produced in the United
  Kingdom, and the regulatory arm of the UK Statistics Authority. It decides
  and enforces the standards of the Code of Practice for Statistics, reviews
  statistics against them, and grants the status of accredited official
  statistics (previously called National Statistics). It operates separately
  from ministers and from the producers of statistics.

level: national
country: GB
region: null

status: active
confidence: high
coverage: low
verification: primary-source
organisation_role: regulatory
start_date: null
end_date: null
last_verified: "2026-10-09"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - GB-UKSA
  - GB-ONS
relationships:
  - type: part-of
    target: GB-UKSA
    source: fact
    evidence: "Confirmed verbatim by reading OSR's own site directly (2026-10-09), osr.statisticsauthority.gov.uk 'Who we are': 'OSR is the regulatory arm of the UK Statistics Authority. We operate separately from government ministers and producers of statistics.' Corroborated on the Authority's own page (statisticsauthority.gov.uk/osr/): 'The Authority is responsible for the running of the Office for National Statistics and the Office for Statistics Regulation, as well as supervising official statistics produced by other public bodies.'"
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Who we are — Office for Statistics Regulation"
    url: "https://osr.statisticsauthority.gov.uk/about-us/who-we-are/"
    publisher: "Office for Statistics Regulation"
    accessed: "2026-10-09"
  - title: "Office for Statistics Regulation — home page"
    url: "https://osr.statisticsauthority.gov.uk/"
    publisher: "Office for Statistics Regulation"
    accessed: "2026-10-09"
  - title: "UK Statistics Authority — Independent oversight of the UK statistical system"
    url: "https://www.statisticsauthority.gov.uk/osr/"
    publisher: "UK Statistics Authority"
    accessed: "2026-10-09"
---

# Office for Statistics Regulation

> **Verified 2026-10-09.** OSR's own "Who we are" page and home page, and the
> UK Statistics Authority's page that describes the two offices it runs, were
> read directly.

## Description

Confirmed by reading OSR's "Who we are" page (2026-10-09): "The Office for
Statistics Regulation (OSR) is the independent regulator of all official
statistics produced in the UK." It reviews statistics against the Code of
Practice for Statistics, "the standards that all producers of official
statistics must adhere to", and "decides, and enforces, the standards of the
Code". "Statistics that meet the standards are granted the status of
accredited official statistics (previously called National Statistics)." It
also reports publicly on concerns across the UK statistical system, investigates
cases where statistics are used publicly in a misleading way, and publishes
research. It is "the regulatory arm of the UK Statistics Authority".

## Where it sits

[[GB-UKSA]] runs two offices: [[GB-ONS]], the largest producer of official
statistics, and OSR, the regulator. The producer and the regulator are kept
apart inside the same Authority, which is the structure the other countries'
statistical offices in the Atlas do not show; whether they have an equivalent
oversight body that has not been researched is still an open question
(`progress/backlog.md`, roadmap #459).

## `coverage: low`

The Code of Practice for Statistics is not modelled as an entity, and neither
are OSR's founding date (the name and the separation of the regulatory function
from the Authority's board are not dated on the pages read), its statutory
basis, or its governance. The statute (Statistics and Registration Service Act
2007) is named in general knowledge and was **not** established from the
pages read.

## Relationships

- `part-of` [[GB-UKSA]] — the regulatory arm of the Authority.

## Sources

Listed in frontmatter.
