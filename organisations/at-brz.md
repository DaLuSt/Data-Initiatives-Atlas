---
id: AT-BRZ
type: organisation
name: Bundesrechenzentrum
alternative_names:
  - BRZ
  - Austrian Federal Computing Centre
description: >
  Austrian public IT service provider based in Vienna, which develops and
  operates e-government services for the federal government, including the
  federal ministries and the Federal Chancellery. It operates the Austrian
  open data catalogue at data.gv.at and delivers ID Austria, and
  implements the oesterreich.gv.at platform jointly with the responsible
  federal ministry.

level: national
country: AT
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-20"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - AT
  - AT-DATA-GV-AT
  - AT-ID-AUSTRIA
relationships:
  - type: part-of
    target: AT
    source: fact
    evidence: "The Bundesrechenzentrum is a public body of AT; this anchor edge records national scope under metadata/relationship-types.md §2.3 and asserts no more than that. NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Austrian Federal Computing Center - BRZ"
    url: "https://www.brz.gv.at/en/"
    publisher: "Bundesrechenzentrum (BRZ)"
  - title: "Austrian Federal Computing Centre"
    url: "https://en.wikipedia.org/wiki/Austrian_Federal_Computing_Centre"
    publisher: "Wikipedia"
  - title: "ID Austria - BRZ"
    url: "https://www.brz.gv.at/was-wir-tun/services-produkte/id-austria.html"
    publisher: "Bundesrechenzentrum (BRZ)"
---

# Bundesrechenzentrum

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

Austria's federal IT provider - and a different institutional shape
from the digital agencies the Atlas holds elsewhere.

## A computing centre, not a policy agency

[[NL-LOGIUS]], [[SE-DIGG]], [[DK-DIGST]] and [[IT-AGID]] are agencies
with policy or coordination mandates. The BRZ is a **service provider**:
it builds and runs systems for the ministries.

That matters for reading the graph. Austria's federal digital policy
sits with a ministry the Atlas does not yet model, so BRZ appearing as
the hub of the Austrian layer reflects what is modelled rather than how
Austria is governed.

## Relationships

- `part-of` [[AT]] (anchor edge).
- Operates [[AT-DATA-GV-AT]] and [[AT-ID-AUSTRIA]].

## Sources

Listed in frontmatter.
