---
id: EU-BRIS
type: platform
name: Business Registers Interconnection System
alternative_names:
  - BRIS
description: >
  EU-wide system interconnecting national business registers, giving
  public electronic access to company information and documents through
  the European e-Justice Portal and enabling registers to exchange data
  on cross-border operations, companies and their branches. Operational
  since 8 June 2017, established under Directive (EU) 2017/1132.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2017-06-08
end_date: null
last_verified: "2026-09-06"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-COMPANY-LAW-DIRECTIVE
  - NL-NHR
relationships:
  - type: governed-by
    target: EU-COMPANY-LAW-DIRECTIVE
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP (NL-HANDELSREGISTERWET's own body text). Confirmed by reading EUR-Lex's own text of Directive (EU) 2017/1132 directly (2026-09-06): Article 22 establishes 'the system of interconnection of registers,' composed of the Member States' registers, the central platform, and the portal serving as the European electronic access point; Article 23 gives the Commission authority to develop/operate the platform; Article 25 sets its EU-budget financing. The European Commission's own blog, read independently, confirms the system 'became a reality on 8 June 2017' and traces its original mandate to the earlier Directive 2012/17/EU, later codified into this directive."
    confidence: high
    valid_from: 2017-06-08
    valid_until: null
  - type: applies-to
    target: NL-NHR
    source: fact
    evidence: "The Company Law Directive's interconnection system applies to the business registers of every EU member state; the Netherlands' Handelsregister (NL-NHR), held by NL-KVK, is the Dutch register connected to it. NOT independently confirmed by a Dutch-side source naming NL-NHR's specific technical connection to BRIS this pass — the edge follows from BRIS's EU-wide, all-member-state scope rather than a Dutch-authored citation."
    confidence: medium
    valid_from: 2017-06-08
    valid_until: null

sources:
  - title: "Business Register Interconnection System (BRIS)"
    url: "https://ec.europa.eu/digital-building-blocks/sites/spaces/DIGITAL/blog/2017/09/19/533365899/Business+Register+Interconnection+System+BRIS"
    publisher: "European Commission (Digital Building Blocks)"
    accessed: "2026-09-06"
  - title: "Directive (EU) 2017/1132 of the European Parliament and of the Council of 14 June 2017 relating to certain aspects of company law (codification)"
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32017L1132"
    publisher: "EUR-Lex (Publications Office of the European Union)"
    accessed: "2026-09-06"
---

# Business Registers Interconnection System (BRIS)

> **Created 2026-09-06**, closing a gap [[NL-HANDELSREGISTERWET]] flagged
> explicitly: "business registers are interconnected across the Union
> through the Business Registers Interconnection System (BRIS) under the
> Company Law Directive. Neither is an Atlas entity... [[NL-NHR]] appears
> as a purely national register when it is in fact part of a European
> network." Both the founding directive's own EUR-Lex text and the
> European Commission's own blog were read directly.

## Description

Confirmed by reading the European Commission's own blog directly: BRIS
"became a reality on 8 June 2017," linking business registers across EU
member states to a central European platform, giving "a single point of
access via the European e-Justice Portal, through which citizens,
businesses and public administrations can search for information on
companies and their branches opened in other Member States."

Confirmed by reading EUR-Lex's own text of [[EU-COMPANY-LAW-DIRECTIVE]]
directly: **Article 22** defines the system as composed of member states'
registers, a central platform, and the e-Justice portal; registers also
exchange messages directly with each other, routed through the platform.
Registers can notify each other of cross-border mergers, conversions and
divisions, and of the opening or closing of a company's branches in other
member states.

## A national register shown as purely national

[[NL-NHR]], the Dutch Handelsregister held by [[NL-KVK]], is one of the
national registers the system connects — every EU member state's
commercial register participates, by the directive's own terms. No
Dutch-authored source was found this pass naming NL-NHR's specific
technical integration, so the `applies-to` edge here is recorded at
`confidence: medium`, resting on BRIS's EU-wide legal scope rather than a
register-specific citation.

## Not modelled

- The **European Central Platform (ECP)**, the specific technical
  component managing message routing between registers — named in
  secondary sourcing (not independently read this pass) as distinct from
  the "platform" the directive itself describes.
- The **Digitalisation Directive (EU) 2019/1151**, which extended BRIS's
  scope to online company formation and branch registration.

## Relationships

- `governed-by` [[EU-COMPANY-LAW-DIRECTIVE]].
- `applies-to` [[NL-NHR]] — the Netherlands' connected register.

## Sources

Listed in frontmatter, both read directly 2026-09-06.
