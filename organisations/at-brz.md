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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-26"
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
    evidence: "Confirmed by reading brz.gv.at's own organisation page directly (2026-08-26): 'Eigentümer des BRZ ist die Republik Österreich, vertreten durch das Bundesministerium für Finanzen (BMF)' (the owner of the BRZ is the Republic of Austria, represented by the Federal Ministry of Finance) — a wholly state-owned body, confirming national scope under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Austrian Federal Computing Center - BRZ"
    url: "https://www.brz.gv.at/en/"
    publisher: "Bundesrechenzentrum (BRZ)"
    accessed: "2026-08-26"
  - title: "Organisation - BRZ"
    url: "https://www.brz.gv.at/wer-wir-sind/organisation.html"
    publisher: "Bundesrechenzentrum (BRZ)"
    accessed: "2026-08-26"
  - title: "Open Data - data.gv.at - BRZ"
    url: "https://www.brz.gv.at/was-wir-tun/services-produkte/open-data.html"
    publisher: "Bundesrechenzentrum (BRZ)"
    accessed: "2026-08-26"
  - title: "Austrian Federal Computing Centre"
    url: "https://en.wikipedia.org/wiki/Austrian_Federal_Computing_Centre"
    publisher: "Wikipedia"
    accessed: "2026-08-26"
  - title: "ID Austria - BRZ"
    url: "https://www.brz.gv.at/was-wir-tun/services-produkte/id-austria.html"
    publisher: "Bundesrechenzentrum (BRZ)"
    accessed: "2026-08-26"
---

# Bundesrechenzentrum

> **Verified 2026-08-26.** All five cited pages were read directly.
> BRZ's own organisation page confirms its 1997 founding as a spin-off
> from the Ministry of Finance and its state ownership; its own Open
> Data page confirms the `maintained-by` edge onto [[AT-DATA-GV-AT]]
> directly, with an updated dataset count.

## Description

Austria's federal IT provider - and a different institutional shape
from the digital agencies the Atlas holds elsewhere.

## 1997: spun off from the Finance Ministry, still wholly state-owned

Confirmed by reading brz.gv.at's own organisation page directly:
"1997 wurden die IT-Bereiche des Finanzministeriums in die
Bundesrechenzentrum GmbH ausgegliedert" (in 1997 the Finance Ministry's
IT departments were spun off into Bundesrechenzentrum GmbH). It has
operated ever since as a limited-liability company **wholly owned by
the Republic of Austria**, represented by the Federal Ministry of
Finance, and run on commercial-market principles in competition with
private IT firms. No exact founding day is given, so `start_date`
stays unset rather than guessed.

## A computing centre, not a policy agency

[[NL-LOGIUS]], [[SE-DIGG]], [[DK-DIGST]] and [[IT-AGID]] are agencies
with policy or coordination mandates. The BRZ is a **service provider**:
it builds and runs systems for the ministries.

That matters for reading the graph. Austria's federal digital policy
sits with a ministry the Atlas does not yet model — as of this pass,
that portfolio has moved to the **Bundeskanzleramt** itself (see
[[AT-ID-AUSTRIA]]) — so BRZ appearing as the hub of the Austrian layer
reflects what is modelled rather than how Austria is governed.

## Relationships

- `part-of` [[AT]] (anchor edge).
- Operates [[AT-DATA-GV-AT]] and [[AT-ID-AUSTRIA]]. BRZ's own Open Data
  page states this directly: "Das BRZ betreibt den zentralen
  österreichischen Datenkatalog (data.gv.at) für den österreichischen
  Bund sowie die nationalen und internationalen Schnittstellen
  (EU-Datenportal) zu diesem Datenkatalog" (the BRZ operates the
  central Austrian data catalogue for the federal government, as well
  as the national and international interfaces to it).

## Sources

Listed in frontmatter, all five read directly this pass.
