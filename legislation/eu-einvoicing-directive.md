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
verification: primary-source

start_date: 2014-01-01
end_date: null
last_verified: "2026-08-28"
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
    evidence: "Confirmed by reading en.wikipedia.org's own 'CEN/TC 434' article directly (2026-08-28): 'CEN/TC 434 was established in 2014' and 'has developed the European Standard on Electronic Invoicing (EN 16931-1) and other ancillary standardization deliverables required by the European Union's directive on electronic invoicing in public procurement' — EN 16931-1:2017 was published 28 June 2017. ec.europa.eu's own Digital Building Blocks page, also read directly, confirms the operative obligation: 'Public entities are required by Directive 2014/55 to be able to receive and process invoices that comply with the European eInvoicing standard.'"
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Directive 2014/55/EU on electronic invoicing in public procurement"
    url: "https://eur-lex.europa.eu/eli/dir/2014/55/oj"
    publisher: "EUR-Lex / Publications Office of the European Union"
  - title: "EN 16931 compliance"
    url: "https://ec.europa.eu/digital-building-blocks/sites/spaces/DIGITAL/pages/467108950/EN+16931+compliance"
    publisher: "European Commission — Digital Building Blocks"
    accessed: "2026-08-28"
  - title: "CEN/TC 434"
    url: "https://en.wikipedia.org/wiki/CEN/TC_434"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
---

# eInvoicing Directive (2014/55/EU)

> **Re-verified 2026-08-28.** Two of three cited sources were read
> directly. Wikipedia's CEN/TC 434 article confirms the committee's 2014
> establishment and its production of EN 16931-1, published 28 June 2017;
> the Commission's Digital Building Blocks page confirms the operative
> obligation on public entities. `eur-lex.europa.eu` returned empty
> content, consistent with every other EUR-Lex attempt made across this
> batch, and was not read. `verification` moves from `search-only` to
> `primary-source`.

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

Listed in frontmatter, two of three read directly this pass (Wikipedia's
CEN/TC 434 article, the Commission's Digital Building Blocks page).
`eur-lex.europa.eu` returned empty content and was not read.
