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
  secretariat — collecting requirements on behalf of the IT-Planungsrat and
  FITKO, developing the XÖV framework further, and publishing standards on
  the XRepository platform — while ITZBund certifies XÖV conformity. They
  harmonise and simplify data transfer in federal-state communication, and
  include the mandatory OSCI technical transport protocol alongside semantic
  standards such as XMeld, XJustiz, XBau, XhD and XAusländer.

level: national
country: DE
region: null

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-28"
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
    evidence: "Confirmed by reading itzbund.de's own page and blog.d-velop.de directly (2026-08-28): itzbund.de states KoSIT 'sammelt im Auftrag des IT-Planungsrates beziehungsweise der Föderalen IT-Kooperation (FITKO) Anforderungen an neue Standards und entwickelt das XÖV-Rahmenwerk weiter,' publishing standards on the XRepository platform and maintaining the XÖV Handbook; blog.d-velop.de (reached via a 301 redirect from the originally-cited d-velop.de URL) independently confirms 'KoSIT develops and maintains XÖV standards,' with ITZBund additionally certifying XÖV conformity — a fact not previously recorded on this entity."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Startseite — Koordinierungsstelle für IT-Standards"
    url: "https://www.xoev.de/startseite-1459"
    publisher: "Koordinierungsstelle für IT-Standards (KoSIT)"
    accessed: "2026-08-28"
  - title: "XÖV — Das Datenformat XML in der öffentlichen Verwaltung"
    url: "https://www.itzbund.de/DE/itloesungen/standardloesungen/xoev/xoev.html"
    publisher: "Informationstechnikzentrum Bund (ITZBund)"
    accessed: "2026-08-28"
  - title: "XÖV: Grundlagen, Bedeutung und Anwendung in der öffentlichen Verwaltung"
    url: "https://blog.d-velop.de/branchenprozesse/xoev/"
    publisher: "d.velop AG"
    accessed: "2026-08-28"
  - title: "XÖV erklärt: Standard für Datenaustausch in der Verwaltung"
    url: "https://www.glomas.de/glossar/xoev"
    publisher: "Glomas"
    accessed: "2026-08-28"
---

# XÖV

> **Re-verified 2026-08-28.** All four cited pages read directly (the
> `d-velop.de` URL 301-redirected to `blog.d-velop.de`, which loaded and
> was followed as the guidance for redirects instructs). `verification:
> primary-source`; `confidence` raised to `high`.

## Description

XÖV — *XML in der öffentlichen Verwaltung* — designates the family of
XML-based standards for electronic data exchange between German authorities
and departments. Their purpose is systematic data transmission across
public administration, harmonising and simplifying data transfer in
**Bund-Länder communication** specifically, confirmed directly this pass on
itzbund.de's own page.

Specifications are developed in **technical committees and working groups**
made up of public-administration representatives and IT experts, with
[[DE-KOSIT]] acting as secretariat — confirmed directly this pass in more
specific terms than before: itzbund.de states KoSIT "collects requirements
for new standards on behalf of the IT-Planungsrat and FITKO" and
"advances the XÖV framework further," publishing standards on the
**XRepository** platform and maintaining the **XÖV-Handbuch**. A
previously-unrecorded fact, also confirmed directly this pass on
blog.d-velop.de: **ITZBund certifies XÖV conformity**, a distinct role from
KoSIT's development and maintenance function.

The family comprises both **semantic standards** — itzbund.de names XMeld
(address data), XhD (official documents), XAusländer, XJustiz and
XPersonenstand, and glomas.de separately names XBau (construction permits)
as among the most widely adopted — and the **technical standard OSCI**
(Online Services Computer Interface), confirmed directly this pass to be
the mandatory protocol for secure, encrypted data transmission between
authorities.

[[DE-XRECHNUNG]] was developed within the XÖV framework and is the
best-known member of the family.

One source, blog.d-velop.de (read directly this pass, reached via
redirect), states that **over 80% of German authorities** now use
XÖV-conformant standards for data exchange. glomas.de, also read directly,
does **not** repeat this figure and states no overall adoption rate is
given on its own page — confirming the claim's attribution is specifically
to d-velop.de's vendor blog rather than to KoSIT or any other authority,
and it is recorded here with that narrower provenance rather than in the
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
— XMeld, XJustiz, XBau, XhD, XAusländer, XPersonenstand, XPlanung and
others — are not Atlas entities. Only [[DE-XRECHNUNG]] is, because it is
the one the sources describe in its own right. OSCI, the family's
technical transport protocol, is likewise not modelled separately.

Creating an entity per XÖV standard would inflate the German layer without
adding structure, which is the failure mode §1 of the brief warns against:
*"do not optimise for the number of files created."* Queued as a group in
`discovery/research-queue.md`.

## Relationships

- Maintained by [[DE-KOSIT]] — confirmed directly this pass, `confidence:
  high`.

## Sources

Listed in frontmatter, all four read directly this pass. Two are commercial
sources (d-velop, Glomas); the KoSIT's own portal and the ITZBund page
carry the substantive weight, and ITZBund's certification role is a new
finding this pass.
