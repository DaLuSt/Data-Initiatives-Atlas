---
id: EU-PSD2
type: law
name: Revised Payment Services Directive
alternative_names:
  - PSD2
  - Directive (EU) 2015/2366
  - Payment Services Directive 2
description: >
  The EU's revised legal framework for payment services, establishing
  open-banking rights — third-party providers' access to payment-account
  data with customer consent — plus strong customer authentication and
  conduct-of-business rules for payment service providers. Adopted
  25 November 2015, it repealed the original Payment Services Directive
  (2007/64/EC). It is the open-banking "backdrop" the Commission's
  Financial Data Access framework (FIDA) is designed to extend beyond
  payment accounts.

level: regional
country: null
region: EU

status: active
confidence: high
coverage: low
verification: primary-source

start_date: 2015-11-25
end_date: null
last_verified: "2026-09-18"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - EU-FIDA
  - EU-FINANCIAL-DATA-SPACE
relationships: []

sources:
  - title: "Procedure file 2013/0264(COD) — Payment services in the internal market"
    url: "https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2013/0264(COD)"
    publisher: "European Parliament — Legislative Observatory (OEIL)"
    accessed: "2026-09-18"
  - title: "Payment Services Directive (PSD2)"
    url: "https://finance.ec.europa.eu/regulation-and-supervision/financial-services-legislation/implementing-and-delegated-acts/payment-services-directive_en"
    publisher: "European Commission — Finance"
    accessed: "2026-09-18"
  - title: "PSD2: Payment Services Directive"
    url: "https://www.eba.europa.eu/regulation-and-policy/payment-services-and-electronic-money"
    publisher: "European Banking Authority (EBA)"
    accessed: "2026-09-18"
---

# Revised Payment Services Directive (PSD2)

> **Created 2026-09-18**, closing the second half of
> `discovery/unresolved.md` row #123: [[EU-FIDA]]'s own entity already
> described itself as "building on the existing open-banking framework
> under PSD2," but PSD2 itself was never modelled. It now is.

## Description

Directive (EU) 2015/2366, the revised Payment Services Directive. The
European Parliament's own Legislative Observatory (OEIL) procedure file,
read directly, confirms: the final act was **signed 25 November 2015**
and published at **OJ L 337, 23.12.2015, p. 35**, repealing the original
Payment Services Directive, 2007/64/EC. The European Commission's own
Finance page and the European Banking Authority's own regulation page,
both read directly, corroborate the directive number and describe its
scope: authorisation and supervision of payment service providers,
strong customer authentication and secure communication, and — the part
that matters for this Atlas — the open-banking mechanism giving
third-party providers access to a customer's payment-account data with
consent.

## Why this entity exists: it's the thing FIDA extends beyond

[[EU-FINANCIAL-DATA-SPACE]]'s own entity names the Commission's Financial
Data Access proposal ([[EU-FIDA]]) as extending data-sharing rights
"beyond payment accounts" — implicitly contrasting it with what PSD2
already covers. [[EU-FIDA]]'s own entity, created 2026-09-05, already
said as much directly, quoting the Commission's finance.ec.europa.eu page:
FIDA is "building on the existing open-banking framework under PSD2."
That made PSD2 the one named point of comparison for FIDA's own scope
that had never been modelled — this entity closes that gap. No
relationship edge is added here in the other direction (this file
carries no outbound `relationships:`); the sourced "builds on" statement
belongs on [[EU-FIDA]]'s own file, where it is added now as a `based-on`
edge pointing here.

## Not modelled

- The 2007/64/EC predecessor Directive (PSD1) itself — named in the
  OEIL procedure file as repealed, but not independently sourced beyond
  that mention, so no entity or `supersedes` edge is created for it.
- The implementing/delegated acts under PSD2 (regulatory technical
  standards on strong customer authentication, secure communication,
  etc.) — named on the Commission's and EBA's pages but numerous and out
  of scope for this pass.
- Whether PSD2 is itself one of the three named components of
  [[EU-FINANCIAL-DATA-SPACE]] — no source read states this; the
  Commission's language treats it as a backdrop FIDA extends beyond, not
  as one of the three components. The other two components of the three
  remain unidentified, tracked separately in `discovery/unresolved.md`.

## Sources

Three sources, all read directly: the European Parliament's own OEIL
procedure file (signature and Official Journal dates), the European
Commission's Finance page, and the European Banking Authority's
regulation page.
