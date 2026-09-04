---
id: DE-BMV
type: organisation
name: Bundesministerium für Verkehr
alternative_names:
  - BMV
  - Federal Ministry for Transport
description: >
  German federal transport ministry, tracing its lineage to 1949 and most
  recently constituted as the Bundesministerium für Digitales und Verkehr
  (BMDV, 2021-2025). On 6 May 2025, with the formation of the Merz cabinet,
  it was renamed the Bundesministerium für Verkehr and its digital
  competences were transferred to the newly created Bundesministerium für
  Digitales und Staatsmodernisierung, leaving it responsible for federal
  highways, railways, waterways, shipping, aviation and road traffic
  policy. It publishes Mobilithek, Germany's national access point for
  mobility data.

level: national
country: DE
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2025-05-06
end_date: null
last_verified: "2026-09-04"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-MOBILITY
organisations: []
related_entities:
  - DE-BMDS
  - DE-MOBILITHEK
relationships:
  - type: produces
    target: DE-MOBILITHEK
    source: fact
    evidence: "Confirmed by reading bmv.de's own site directly (2026-09-04): the ministry's SharedDocs article on Mobilithek is published under the bmv.de domain and describes the platform as Germany's national data-exchange platform for mobility information. This is the ministry's current identity: de.wikipedia.org's dedicated article, read directly, confirms 'Mit der Bildung des Kabinetts Merz am 6. Mai 2025 wurde das Ministerium in Bundesministerium für Verkehr umbenannt' (with the formation of the Merz cabinet on 6 May 2025, the ministry was renamed the Bundesministerium für Verkehr), the same date DE-MOBILITHEK's own re-verification pass flagged as an unreconciled naming inconsistency between its BMV-labelled and BMDV-labelled sources."
    confidence: medium
    valid_from: 2025-05-06
    valid_until: null

sources:
  - title: "BMV — Aufgaben und Struktur"
    url: "https://www.bmv.de/DE/Ministerium/Aufgaben-Struktur/aufgaben-struktur.html"
    publisher: "Bundesministerium für Verkehr (BMV)"
    accessed: "2026-09-04"
  - title: "Bundesministerium für Verkehr (Deutschland)"
    url: "https://de.wikipedia.org/wiki/Bundesministerium_f%C3%BCr_Verkehr_(Deutschland)"
    publisher: "Wikipedia"
    accessed: "2026-09-04"
---

# Bundesministerium für Verkehr (BMV)

> **Added 2026-09-04, `verification: primary-source` from creation.** A
> research-queue item flagged as **Next** since the Germany batch — closes
> the sourcing inconsistency [[DE-MOBILITHEK]]'s own re-verification pass
> flagged explicitly: "the German transport ministry has been renamed and
> its digital competences moved to [[DE-BMDS]]. The publisher field records
> the name on the cited URL rather than reconciling the two." Two sources
> read directly this pass: the ministry's own current site and Wikipedia's
> dedicated article, which carries the history `bmv.de`'s own structure
> page does not.

## Description

The BMV traces an institutional lineage back to **20 September 1949** —
confirmed by reading Wikipedia's dedicated article directly, which records
the ministry's predecessor as the Reichsverkehrsministerium and lists 21
federal ministers to date. Its most recent prior form was the
**Bundesministerium für Digitales und Verkehr (BMDV)**, in office from
**8 December 2021** under minister Volker Wissing.

**On 6 May 2025**, with the formation of the Merz cabinet, the ministry was
**renamed the Bundesministerium für Verkehr** — confirmed directly in
Wikipedia's own words: "Mit der Bildung des Kabinetts Merz am 6. Mai 2025
wurde das Ministerium in Bundesministerium für Verkehr umbenannt." Its
digital competences transferred to the newly created [[DE-BMDS]], the same
date and the same reorganisation that entity's own file already records
from the digital-ministry side.

## Current structure

Confirmed by reading `bmv.de`'s own "Aufgaben und Struktur" page directly,
the ministry is organised into seven divisions: Leitungsstab (leadership
office), Zentralabteilung (central/administrative division), and dedicated
divisions for aviation, federal highways (roughly 13,200 km of Autobahn and
37,700 km of federal roads), waterways and shipping, railways, and road
traffic. The page itself gives no founding date or history — that comes
from Wikipedia's article instead, an example of the pattern seen elsewhere
in this batch where a ministry's current site describes only its present
structure.

## Personnel

Wikipedia's article, read directly, names Patrick Schnieder as the
minister at the ministry's 6 May 2025 founding and **Steffen Bilger** as
the current minister, having taken office **29 July 2026** — a mid-term
change the Atlas records because it dates the source rather than because
the Atlas tracks office-holders, the same convention already used on
[[DE-BMDS]].

## Resolves an open naming inconsistency

[[DE-MOBILITHEK]]'s own sources are split between a `bmv.de`-hosted page
and a `bmdv.bund.de`/BMDV-attributed one, and its own re-verification pass
explicitly declined to reconcile them: "the publisher field records the
name on the cited URL rather than reconciling the two." This entity is
that reconciliation: BMDV renamed to BMV on 6 May 2025, and Mobilithek —
a transport-sector platform — stayed with the transport ministry rather
than moving to [[DE-BMDS]] with the ministry's former digital competences.

## Relationships

- `produces` [[DE-MOBILITHEK]] — Germany's national access point for
  mobility data, published under `bmv.de`.

**No relationship to [[DE-BMDS]] is asserted.** The two ministries split
from a common predecessor (BMDV) on the same date, but no source read
describes one as governing, superseding or being derived from the other —
they are siblings, not relatives, the same reasoning already applied
elsewhere in this Atlas to instruments that share a common ancestor
without one implementing the other.

## Sources

Listed in frontmatter, both read directly.
