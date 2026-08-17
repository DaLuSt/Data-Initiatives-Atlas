---
id: GB-ONE-LOGIN
type: platform
name: GOV.UK One Login
alternative_names:
  - One Login
  - GOV.UK One Login
description: >
  The United Kingdom government's single sign-in and identity verification
  service, designed to replace Government Gateway and other separate logins
  with one account across government services. It covers the system for
  proving identity when using government services and the GOV.UK Wallet,
  which holds government-issued credentials on a phone. A separate national
  digital ID scheme announced in September 2025 is built on it; in January
  2026 the government confirmed that holding a digital ID would not be
  compulsory and that access to public services would not depend on having
  one. Rollout has proceeded in phases, including Companies House WebFiling
  from October 2025 and new HMRC users from February 2026.

level: national
country: GB
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
  - GB-GDS
related_entities:
  - FR-FRANCECONNECT
  - DE-BUNDID
  - PL-MOBYWATEL
  - EU-EIDAS2
relationships: []

sources:
  - title: "GOV.UK One Login — technical documentation"
    url: "https://docs.sign-in.service.gov.uk/"
    publisher: "Government Digital Service (UK)"
  - title: "GOV.UK One Login for HMRC: how we made it happen and what comes next"
    url: "https://gds.blog.gov.uk/2026/04/28/gov-uk-one-login-for-hmrc-how-we-made-it-happen-and-what-comes-next/"
    publisher: "Government Digital Service (UK)"
  - title: "A single sign-on and digital identity solution for government"
    url: "https://gds.blog.gov.uk/2021/07/13/a-single-sign-on-and-digital-identity-solution-for-government"
    publisher: "Government Digital Service (UK)"
  - title: "UK government ID: the digital ID scheme and the wallet"
    url: "https://oneid.uk/news-and-events/uk-government-id-the-digital-id-scheme-and-the-wallet"
    publisher: "OneID"
---

# GOV.UK One Login

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

One Login is the UK's single sign-in and identity verification service,
replacing Government Gateway and dozens of separate departmental logins.
It spans three things: **sign-in and identity proving**, the **GOV.UK
Wallet** for government-issued credentials on a phone, and a **national
digital ID scheme** announced in September 2025 and built on top of it.

Rollout is phased — Companies House WebFiling from October 2025, new HMRC
users from February 2026.

## The seventh national identity system, and the first outside eIDAS

| Country | System | Relationship to [[EU-EIDAS2]] |
|---|---|---|
| France | [[FR-FRANCECONNECT]] | in scope, not modelled |
| Germany | [[DE-BUNDID]] | in scope; implements [[EU-EIDAS]] |
| Poland | [[PL-MOBYWATEL]] | in scope and **cannot comply** |
| **United Kingdom** | **this platform** | **out of scope entirely** |

The eIDAS 2.0 deadline has been a running thread across four batches: no
country was linked to [[EU-EIDAS2]] at all until Poland provided the first
link, and that link was *negative* — [[PL-MOBYWATEL]] is reported
architecturally incapable of serving as an EUDI Wallet.

**The UK is the first identity system in the Atlas with no eIDAS
relationship to have or to fail.** It is building a wallet on the same
timetable as the EU is mandating one, under no obligation, to no common
specification. No relationship to [[EU-EIDAS2]] is asserted in either
direction — the absence is not a failure, and modelling it as one would
misstate the position.

## A policy fact the Atlas cannot hold

In **January 2026 the government confirmed that holding a digital ID would
not be compulsory**, and that access to public services would not depend on
having one.

That is a **constraint on a system**, and the Atlas has no field for it.
`status: active` says the platform runs. Nothing in the schema records "and
its use is guaranteed non-mandatory by policy" — which, for a national
identity scheme, is arguably the most consequential fact about it. It sits
in the description and this prose, where no query will find it.

This is a different shape from the gaps recorded in earlier batches: those
were relationships the vocabulary could not express, and this is an
*attribute* the metadata schema does not carry.

## Not modelled

- **The GOV.UK Wallet** — part of One Login rather than a separate system in
  the sources, so folded in here.
- **The national digital ID scheme** — announced September 2025 and built on
  One Login. Whether it warrants its own entity depends on whether it is a
  distinct system or a use of this one, and the sources found do not settle
  that.
- **Government Gateway**, the predecessor being replaced. No
  `previous_version` is set, because "replaces" and "is a version of" are
  different claims and only the first is sourced.

## Relationships

None asserted. [[GB-GDS]] appears in `organisations:` as the operator, on
the strength of GDS's common-platform brief and its own blog carrying the
rollout — but no `maintained-by` edge, for the same reason as
[[GB-DATA-GOV-UK]]: operating a service and being named as its maintainer
are different claims.

## Sources

Listed in frontmatter — three GDS-published, one industry. The technical
documentation site is the strongest and remains unread.
