---
id: EU-EINVOICING-DIRECTIVE
type: directive
name: Directive 2014/55/EU on electronic invoicing in public procurement
alternative_names:
  - eInvoicing Directive
  - Directive 2014/55/EU
  - E-invoicing Directive
description: >
  European Union directive of 2014 on electronic invoicing in public
  procurement, which mandated the development of a common European standard
  for electronic invoices at the semantic level for use in
  business-to-government invoicing. CEN developed EN 16931 in response,
  through its technical committee CEN/TC 434.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2014-01-01
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-EN-16931
  - EU-CEN
relationships:
  - type: applies-in
    target: EU
    source: fact
    evidence: "In 2014 the EU adopted Directive 2014/55/EU on electronic invoicing in public procurement, which mandated the development of a common European e-invoice standard at the semantic level, to be used in business-to-government invoicing; CEN/TC 434 was established in 2014 to develop standards in the field of electronic invoicing and produced EN 16931-1 and the ancillary deliverables the directive required (en.wikipedia.org 'CEN/TC 434'; ec.europa.eu digital-building-blocks 'EN 16931 compliance'; vatupdate.com 'EN16931 — European E-Invoicing Standard'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Directive 2014/55/EU on electronic invoicing in public procurement"
    url: "https://eur-lex.europa.eu/eli/dir/2014/55/oj"
    publisher: "EUR-Lex / Publications Office of the European Union"
  - title: "EN 16931 compliance"
    url: "https://ec.europa.eu/digital-building-blocks/sites/spaces/DIGITAL/pages/467108950/EN+16931+compliance"
    publisher: "European Commission — Digital Building Blocks"
  - title: "CEN/TC 434"
    url: "https://en.wikipedia.org/wiki/CEN/TC_434"
    publisher: "Wikipedia"
---

# eInvoicing Directive (2014/55/EU)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

The 2014 directive on **electronic invoicing in public procurement**. Its
distinguishing feature is what it did *not* do: rather than specify a format,
it **mandated the development of a common European standard** at the semantic
level for business-to-government invoicing.

[[EU-CEN]] answered by establishing **CEN/TC 434** in 2014, which produced
[[EU-EN-16931]].

## A directive that commissions a standard

The Atlas holds many directives that require member states to do something.
This one requires a **standards body** to produce something, and then
requires member states to accept invoices conforming to it.

That makes it the hinge of the only complete **EU legislation → European
standard → national specification** chain the Atlas holds:

```
EU-EINVOICING-DIRECTIVE  →  EU-EN-16931  →  DE-XRECHNUNG
      (directive)          (CEN standard)   (German CIUS)
                                 ↑
                              EU-CEN
```

`discovery/research-queue.md` has carried this since the Germany batch as
the **highest-value German item**, for exactly this reason: it gives the
Atlas a standards-body EU→national chain, which nothing else did.

## Not modelled

- **CEN/TC 434**, the technical committee. It is a committee of [[EU-CEN]]
  rather than a body, the same reasoning that keeps the Czech NCKB out of the
  graph as a section of [[CZ-NUKIB]].
- The directive's **transposition** in any member state.
- **Peppol** and the transport layer, which the directive does not specify.

## Sources

Listed in frontmatter.
