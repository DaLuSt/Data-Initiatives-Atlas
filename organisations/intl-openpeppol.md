---
id: INTL-OPENPEPPOL
type: organisation
name: OpenPeppol
alternative_names:
  - OpenPEPPOL
  - OpenPeppol AISBL
description: >
  International non-profit association (AISBL — Association Internationale
  Sans But Lucratif) under Belgian law, headquartered in Brussels, founded
  in 2012 when the EU-funded Peppol pilot project concluded and its
  services and responsibilities were transferred to the association. It
  develops, publishes and maintains the Peppol Interoperability Framework
  and the Peppol Business Interoperability Specifications (Peppol BIS), a
  network for standardised electronic exchange of business documents
  (invoices, orders and related documents) between the public and private
  sectors, governed democratically by member-elected leadership across End
  User, Service Provider and Peppol Authority stakeholder communities.
  Membership and Peppol Authorities span well beyond the EU, including
  Singapore, Japan, Australia, New Zealand, the United Arab Emirates and
  Nigeria.

level: international
country: null
region: null

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: 2012-09-01
end_date: null
last_verified: "2026-09-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU
  - INTL-PEPPOL-BIS-BILLING
relationships:
  - type: related-to
    target: EU
    source: fact
    evidence: "OpenPeppol's own 'About' and 'Organisation' pages (peppol.org/about/, peppol.org/learn-more/organisation/), read directly (2026-09-26), confirm it is an AISBL under Belgian law, headquartered in Brussels, founded 1 September 2012 when 'the Peppol project was finalised, and its services and responsibilities were taken over by OpenPeppol' — the EU-funded PEPPOL (Pan-European Public Procurement Online) pilot project that preceded it. Its own Peppol Authorities page (peppol.org/members/peppol-authorities/), also read directly, lists authorities across 26 jurisdictions including non-European ones (Japan, Malaysia, New Zealand, Nigeria, Oman, Singapore, Taiwan, United Arab Emirates) alongside EU member states — genuinely international scope, not an EU body, despite originating in an EU-funded pilot and being legally seated in Brussels. `related-to` rather than `part-of`: OpenPeppol is legally independent of the EU, not a body of it, though every EU member state participates in its network."
    confidence: high
    valid_from: "2012-09-01"
    valid_until: null

sources:
  - title: "About — OpenPeppol"
    url: "https://peppol.org/about/"
    publisher: "OpenPeppol"
    accessed: "2026-09-26"
  - title: "Organisation — OpenPeppol"
    url: "https://peppol.org/learn-more/organisation/"
    publisher: "OpenPeppol"
    accessed: "2026-09-26"
  - title: "Peppol Authorities — OpenPeppol"
    url: "https://peppol.org/members/peppol-authorities/"
    publisher: "OpenPeppol"
    accessed: "2026-09-26"
---

# OpenPeppol

> **Created 2026-09-26**, closing the OpenPeppol half of
> `discovery/unresolved.md` row #49's residual clause — previously
> "neither OpenPeppol nor Peppol BIS is researched enough to model."
> Sourced from OpenPeppol's own official pages, all read directly. See
> [[INTL-PEPPOL-BIS-BILLING]] for the specification itself.

## Description

OpenPeppol is an **AISBL** (Association Internationale Sans But Lucratif —
international non-profit association) under **Belgian law**, headquartered
in **Brussels**. It was founded on **1 September 2012**, when the EU-funded
PEPPOL pilot project concluded and its services and responsibilities were
transferred to the newly formed association — confirmed verbatim on
OpenPeppol's own "About" page.

It develops, publishes and maintains the **Peppol Interoperability
Framework**, including the **Peppol Business Interoperability
Specifications (Peppol BIS)** — see [[INTL-PEPPOL-BIS-BILLING]] for the
invoicing specification specifically.

## Genuinely international, not an EU body

OpenPeppol's own "Peppol Authorities" page, read directly, lists
authorities across **26 jurisdictions** — EU member states and other
European countries (Norway, Switzerland, Iceland, England), but also
**Japan, Malaysia, New Zealand, Nigeria, Oman, Singapore, Taiwan and the
United Arab Emirates**. Despite its Brussels legal seat and its origin in
an EU-funded pilot project, OpenPeppol's own network reaches well beyond
the EU — the same reasoning that gives this entity `level: international`
rather than `region: EU`, matching the convention already used for
[[INTL-ISO]] and other globally-scoped standards bodies headquartered in
one particular country.

## Governance

Confirmed on OpenPeppol's own "Organisation" page: membership has four
categories (End Users, Service Providers, Peppol Authorities, Observers),
with all but Observers holding voting rights at the annual General
Assembly. A Managing Committee (the Secretary General plus six elected
members, two from each stakeholder community) and a Coordinating
Committee oversee day-to-day and cross-community work.

## Not modelled

- The individual **Peppol Authorities** (e.g. Singapore's IMDA, Japan's
  Digital Agency) as separate entities — each is a national/territorial
  government body designating itself, or being designated, as Peppol's
  local point of contact, and none is yet researched to Atlas standard.
- The original, EU-funded **PEPPOL pilot project** (2008–2012) that
  preceded OpenPeppol — described here in prose as the association's own
  origin story, not as a separate entity.

## Relationships

- `related-to` [[EU]] — `confidence: high`. Not `part-of`: OpenPeppol is
  legally independent of the EU (a Belgian AISBL, not an EU institution
  or agency), even though it originated in an EU-funded pilot and every
  EU member state participates in its network.

## Sources

Listed in frontmatter, all three read directly.
