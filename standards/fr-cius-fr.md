---
id: FR-CIUS-FR
type: standard
name: CIUS-FR
alternative_names:
  - Core Invoice Usage Specification — France
description: >
  France's national Core Invoice Usage Specification (CIUS) of the
  European e-invoicing standard EN 16931, making certain optional fields
  of the core semantic model mandatory for the French context (such as
  specific buyer and seller identifiers and payment-means codes). It is
  the specification suppliers to public bodies must follow when submitting
  invoices through Chorus Pro, France's centralised B2G e-invoicing
  platform operated by the Agence pour l'Informatique Financière de
  l'État (AIFE), which accepts invoices in the UN/CEFACT CII and OASIS
  UBL 2.1 syntaxes, both conformant with CIUS-FR. Its legal basis is
  Article 193 of Law n° 2019-486 of 22 May 2019, codified in the Public
  Procurement Code, transposing Directive 2014/55/EU.

level: national
country: FR
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-19"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-EINVOICING-DIRECTIVE
  - EU-EN-16931
relationships:
  - type: based-on
    target: EU-EN-16931
    source: fact
    evidence: "PARTIALLY CLOSES discovery/unresolved.md row #49. Confirmed by reading the European Commission's own 'eInvoicing in France' page directly (digital-building-blocks.ec.europa.eu, 2026-09-19): 'France has established a national CIUS and implementation guidelines for the EN to make optional fields of the core semantic model mandatory in the national CIUS.' The same page states Chorus Pro, France's national eInvoicing platform, 'already supports UN/CEFACT CII and OASIS UBL 2.1' — the two EN 16931 syntaxes CIUS-FR is written in — and names 'Factur-X, the Franco-German standard for hybrid eInvoicing (named ZUGFeRD in Germany)' as the format Chorus Pro uses with CII. Factur-X's binational scope (also used in Germany) is why this entity models CIUS-FR — the specification itself, unambiguously French — rather than Factur-X, which spans two countries."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: implements-requirement-from
    target: EU-EINVOICING-DIRECTIVE
    source: fact
    evidence: "Confirmed by reading the European Commission's own 'eInvoicing in France' page directly (2026-09-19): the legal basis is 'Article 193 of the Law n°2019-486 of 22 May 2019 codified in the Public Procurement Code... which transposes Directive 2014/55/EU,' requiring public sector entities to receive and process EN 16931-compliant structured eInvoices."
    confidence: high
    valid_from: "2019-05-22"
    valid_until: null

sources:
  - title: "eInvoicing in France"
    url: "https://ec.europa.eu/digital-building-blocks/sites/spaces/DIGITAL/pages/467108885/eInvoicing+in+France"
    publisher: "European Commission — Digital Building Blocks"
    accessed: "2026-09-19"
---

# CIUS-FR

> **Created 2026-09-19**, partially closing `discovery/unresolved.md` row
> #49 (other national CIUSes beyond [[DE-XRECHNUNG]] are not modelled).
> Sourced from the European Commission's own "eInvoicing in France" page,
> read directly.

## Description

CIUS-FR is France's national **Core Invoice Usage Specification** of
[[EU-EN-16931]] — confirmed by reading the Commission's own "eInvoicing in
France" page directly: "France has established a national CIUS and
implementation guidelines for the EN to make optional fields of the core
semantic model mandatory in the national CIUS," for example specific
buyer/seller identifiers and payment-means codes Chorus Pro requires.

Its legal basis is **Article 193 of Law n° 2019-486 of 22 May 2019**,
codified in the Public Procurement Code, which transposes
[[EU-EINVOICING-DIRECTIVE]] — confirmed directly on the same page.

## Chorus Pro and Factur-X, not separately modelled here

CIUS-FR is the specification suppliers must follow to submit invoices to
public bodies through **Chorus Pro**, France's centralised B2G platform
operated by the Agence pour l'Informatique Financière de l'État (AIFE).
The Commission's page, read directly, confirms Chorus Pro "already
supports UN/CEFACT CII and OASIS UBL 2.1" — the two syntaxes EN 16931
defines and CIUS-FR is written in.

**Factur-X**, the hybrid PDF/XML format Chorus Pro uses with the CII
syntax, is explicitly named on the same page as "the **Franco-German**
standard for hybrid eInvoicing (named ZUGFeRD in Germany)." Because it
spans two countries rather than being uniquely French, it is not modelled
as a `FR-` entity here — doing so would misstate its scope the way the
Atlas's `country`-field discussions elsewhere warn against. CIUS-FR, the
specification itself, is unambiguously French and is what this entity
records.

## Not modelled

- **Chorus Pro** as a separate platform entity — described here in prose
  as the operating channel, the same treatment [[DE-XRECHNUNG]] gives
  [[DE-KOSIT]]'s operational role without splitting it further.
- **Factur-X**, the binational hybrid format — see above.
- The **Agence pour l'Informatique Financière de l'État (AIFE)** as an
  organisation entity.

## Relationships

- `based-on` [[EU-EN-16931]] — `confidence: medium`.
- `implements-requirement-from` [[EU-EINVOICING-DIRECTIVE]] —
  `confidence: high`.

## Sources

Listed in frontmatter — a single source, read directly.
