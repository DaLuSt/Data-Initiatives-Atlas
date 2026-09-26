---
id: INTL-PEPPOL-BIS-BILLING
type: standard
name: Peppol BIS Billing 3.0
alternative_names:
  - Peppol BIS Billing
  - Peppol BIS 3.0
description: >
  Peppol Business Interoperability Specification for invoices and credit
  notes, maintained by OpenPeppol. Its own documentation states it is a
  Core Invoice Usage Specification (CIUS) of the European e-invoicing
  standard EN 16931, following the guidance given in EN 16931's own
  chapter 7; any document compliant with this specification is compliant
  with EN 16931. Expressed in the OASIS UBL 2.1 syntax (with Cross
  Industry Invoice supported for related specifications), validated by
  Schematron rules, and used as the de-facto invoicing format across the
  Peppol network spanning the EU and other participating jurisdictions
  worldwide.

level: international
country: null
region: null

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - INTL-OPENPEPPOL
related_entities:
  - INTL-OPENPEPPOL
  - EU-EN-16931
relationships:
  - type: maintained-by
    target: INTL-OPENPEPPOL
    source: fact
    evidence: "Confirmed by reading docs.peppol.eu's own Peppol BIS Billing 3.0 specification page directly (2026-09-26), OpenPeppol's official documentation site."
    confidence: high
    valid_from: null
    valid_until: null
  - type: based-on
    target: EU-EN-16931
    source: fact
    evidence: "PARTIALLY CLOSES discovery/unresolved.md row #49's residual Peppol BIS clause. Confirmed by reading docs.peppol.eu's own Peppol BIS Billing 3.0 page directly (2026-09-26): 'This specification[...] is a Core Invoice Usage Specification (CIUS) of EN 16931, following the guidance given in chapter 7 of the EN 16931,' expressed primarily in the UBL syntax. The same shape of edge already carried by [[DE-XRECHNUNG]], [[IT-FATTURAPA]] and [[FR-CIUS-FR]] — Peppol BIS Billing is a fourth CIUS of EN 16931, this one maintained by an international standards body rather than a single national government."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Peppol BIS Billing 3.0"
    url: "https://docs.peppol.eu/poacc/billing/3.0/bis/"
    publisher: "OpenPeppol"
    accessed: "2026-09-26"
---

# Peppol BIS Billing 3.0

> **Created 2026-09-26**, closing the Peppol BIS half of
> `discovery/unresolved.md` row #49's residual clause. Sourced from
> OpenPeppol's own official documentation, read directly. See
> [[INTL-OPENPEPPOL]] for the maintaining organisation.

## Description

Peppol BIS Billing 3.0 is the Peppol Business Interoperability
Specification for invoices and credit notes, maintained by
[[INTL-OPENPEPPOL]]. Its own documentation states directly: "This
specification[...] is a Core Invoice Usage Specification (CIUS) of EN
16931, following the guidance given in chapter 7 of the EN 16931" — any
document compliant with this specification is compliant with
[[EU-EN-16931]] itself.

It is expressed primarily in the **OASIS UBL 2.1** syntax, validated by
Schematron business rules, and is the de-facto invoicing format across
the Peppol network.

## A fourth CIUS, and the first not tied to one country

[[DE-XRECHNUNG]], [[IT-FATTURAPA]] and [[FR-CIUS-FR]] are each a national
government's own CIUS of EN 16931. Peppol BIS Billing is the fourth CIUS
the Atlas now holds, and the first maintained by an international
standards body rather than a single national government — matching
`discovery/unresolved.md` row #48's closing observation that "the CIUS
mechanism ... its concrete instances ... are exactly the entities worth
modelling."

## Not modelled

- The **UBL 2.1 syntax** itself, or the Schematron validation rules —
  technical artefacts of this specification, the same call already made
  for EN 16931's own UBL/CII syntax bindings (row #48).
- **Peppol BIS Self-Billing** and other Peppol BIS specifications beyond
  billing — not yet researched.

## Relationships

- `maintained-by` [[INTL-OPENPEPPOL]] — `confidence: high`.
- `based-on` [[EU-EN-16931]] — `confidence: high`.

## Sources

Listed in frontmatter, read directly.
