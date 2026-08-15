---
id: DE-XOEV
type: standard
name: XÖV
alternative_names:
  - XML in der öffentlichen Verwaltung
  - XÖV-Standards
description: >
  Family of XML-based standards for electronic data exchange between German
  authorities and departments. XÖV specifications are developed in technical
  committees and working groups of public-administration representatives and
  IT experts, with the Koordinierungsstelle für IT-Standards acting as
  secretariat, and they harmonise and simplify data transfer in
  federal-state communication.

level: national
country: DE
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - DE-KOSIT
related_entities:
  - DE-XRECHNUNG
relationships:
  - type: maintained-by
    target: DE-KOSIT
    source: fact
    evidence: "The Koordinierungsstelle für IT-Standards (KoSIT) maintains the XÖV standards; XÖV specifications are developed in technical committees and working groups with KoSIT coordinating procedures and ensuring committee work (d-velop.de; glomas.de; xoev.de). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Startseite — Koordinierungsstelle für IT-Standards"
    url: "https://www.xoev.de/startseite-1459"
    publisher: "Koordinierungsstelle für IT-Standards (KoSIT)"
  - title: "XÖV — Das Datenformat XML in der öffentlichen Verwaltung"
    url: "https://www.itzbund.de/DE/itloesungen/standardloesungen/xoev/xoev.html"
    publisher: "Informationstechnikzentrum Bund (ITZBund)"
  - title: "XÖV: Grundlagen, Bedeutung und Anwendung in der öffentlichen Verwaltung"
    url: "https://www.d-velop.de/blog/branchenprozesse/xoev/"
    publisher: "d.velop AG"
  - title: "XÖV erklärt: Standard für Datenaustausch in der Verwaltung"
    url: "https://www.glomas.de/glossar/xoev"
    publisher: "Glomas"
---

# XÖV

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

XÖV — *XML in der öffentlichen Verwaltung* — designates the family of
XML-based standards for electronic data exchange between German authorities
and departments. Their purpose is systematic data transmission across
public administration, harmonising and simplifying data transfer in
**Bund-Länder communication** specifically.

Specifications are developed in **technical committees and working groups**
made up of public-administration representatives and IT experts, with
[[DE-KOSIT]] acting as secretariat, coordinating procedures and supporting
the committee work.

[[DE-XRECHNUNG]] was developed within the XÖV framework and is the
best-known member of the family.

One source states that **over 80% of German authorities** now use
XÖV-conformant standards for data exchange. It is a vendor-glossary claim
attributed to the KoSIT rather than a figure read from a KoSIT publication,
and it is recorded here with that provenance rather than in the
description.

## The German counterpart to Digikoppeling

XÖV occupies the position [[NL-DIGIKOPPELING]] holds in the Dutch layer: the
mandated-in-practice interoperability standard family for
government-to-government exchange, custodied by a central body
([[DE-KOSIT]] / [[NL-LOGIUS]]).

**No relationship is asserted.** The technical bases differ — XÖV is an XML
modelling and specification methodology, Digikoppeling a message-exchange
protocol suite — and the resemblance is functional rather than genealogical.

## What is not modelled

XÖV is a **family**, not a single specification. Individual XÖV standards
— XPersonenstand, XMeld, XBau, XPlanung and others — are not Atlas
entities. Only [[DE-XRECHNUNG]] is, because it is the one the sources
describe in its own right.

Creating an entity per XÖV standard would inflate the German layer without
adding structure, which is the failure mode §1 of the brief warns against:
*"do not optimise for the number of files created."* Queued as a group in
`discovery/research-queue.md`.

## Relationships

- Maintained by [[DE-KOSIT]].

## Sources

Listed in frontmatter. Two are commercial glossaries; the KoSIT's own
portal and the ITZBund page carry the weight.
