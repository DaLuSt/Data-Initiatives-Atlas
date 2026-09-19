---
id: IT-FATTURAPA
type: standard
name: FatturaPA
alternative_names:
  - Fattura elettronica
  - Sistema di Interscambio invoicing format
description: >
  Italy's mandatory national XML format for electronic invoicing, exchanged
  through the Sistema di Interscambio (SDI) operated by the Agenzia delle
  Entrate. It predates the European standard EN 16931 and is not itself
  natively EN 16931-compliant, but the European Commission's own eInvoicing
  framework recognises it as aligned with EN 16931's core invoice model via
  a national CIUS, mandatory since the Agenzia delle Entrate's Provvedimento
  of 18 April 2019, through which the SDI translates EN 16931-compliant
  invoices to and from the national schema.

level: national
country: IT
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
    evidence: "PARTIALLY CLOSES discovery/unresolved.md row #49. Confirmed by reading the European Commission's own 'eInvoicing in Italy' page directly (digital-building-blocks.ec.europa.eu, 2026-09-19): 'The national XML format, FatturaPA, is specifically designed to align with EN 16931 and is mandatory for all B2G transactions.' The same page: 'The use of the Italian CIUS is mandatory, through the exchange system (Sistema di Interscambio) for eInvoicing processing... CIUS is used to ensure the translation to the national XML standard. The communication of the CIUS is done through the regulation of the Revenue Agency' — citing the Agenzia delle Entrate's Provvedimento of 18 April 2019. Unlike DE-XRECHNUNG, which is itself a CIUS in EN 16931's own syntaxes, FatturaPA is a pre-existing national XML schema that the CIUS translates to and from — recorded as `based-on` at `confidence: medium` to reflect that indirection, rather than the `confidence: high` XRechnung carries as a direct CIUS."
    confidence: medium
    valid_from: "2019-04-18"
    valid_until: null
  - type: implements-requirement-from
    target: EU-EINVOICING-DIRECTIVE
    source: fact
    evidence: "As an EU member state's B2G e-invoicing mandate implementing Directive 2014/55/EU's requirement that public entities be able to receive and process EN 16931-compliant invoices, confirmed by the same European Commission page (digital-building-blocks.ec.europa.eu 'eInvoicing in Italy'), read directly 2026-09-19, which frames FatturaPA's EN 16931 alignment explicitly in terms of that directive's compliance framework."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "eInvoicing in Italy"
    url: "https://ec.europa.eu/digital-building-blocks/sites/spaces/DIGITAL/pages/467108890/eInvoicing+in+Italy"
    publisher: "European Commission — Digital Building Blocks"
    accessed: "2026-09-19"
---

# FatturaPA

> **Created 2026-09-19**, partially closing `discovery/unresolved.md` row
> #49 (other national CIUSes beyond [[DE-XRECHNUNG]] are not modelled).
> Sourced from the European Commission's own "eInvoicing in Italy" page,
> read directly.

## Description

FatturaPA is Italy's own XML format for electronic invoicing, exchanged
through the **Sistema di Interscambio (SDI)**, operated by the Agenzia
delle Entrate (Italy's Revenue Agency). Confirmed by reading the
Commission's own "eInvoicing in Italy" page directly: FatturaPA **predates
[[EU-EN-16931]]** and "is not natively EN 16931-compliant," unlike
[[DE-XRECHNUNG]], which is itself written as a Core Invoice Usage
Specification in EN 16931's own UBL/CII syntaxes.

## A CIUS that translates rather than defines

The same Commission page states the mechanism precisely: "The use of the
Italian CIUS is mandatory, through the exchange system (Sistema di
Interscambio) for eInvoicing processing... CIUS is used to ensure the
translation to the national XML standard." Cross-border suppliers can
submit an EN 16931-compliant invoice, and the SDI translates it into
FatturaPA on the way in. The Italian CIUS's mandatory status is set by the
Agenzia delle Entrate's **Provvedimento of 18 April 2019**, cited directly
on the same Commission page.

This is a different shape from Germany's case: XRechnung *is* a CIUS,
written directly in EN 16931's own syntaxes. Italy's CIUS is a **separate
translation layer** sitting in front of a pre-existing national schema
that was never itself rewritten to be EN 16931-native. `based-on` is
recorded at `confidence: medium` rather than `high` to reflect that
indirection.

## Not modelled

- The **Sistema di Interscambio (SDI)** itself as a separate platform
  entity — described here in prose as the exchange system FatturaPA moves
  through, the same treatment [[DE-XRECHNUNG]] gives [[DE-KOSIT]]'s
  operational role without splitting it further.
- **CIUS-IT / "FatturaEU"**, the cross-border-facing EN 16931-native
  profile the SDI maps onto FatturaPA — named on the Commission's page but
  not independently researched beyond the mapping mechanism above.
- The **Agenzia delle Entrate** as an organisation entity.

## Relationships

- `based-on` [[EU-EN-16931]] — via the Italian CIUS translation mechanism,
  `confidence: medium`.
- `implements-requirement-from` [[EU-EINVOICING-DIRECTIVE]].

## Sources

Listed in frontmatter — a single source, read directly.
