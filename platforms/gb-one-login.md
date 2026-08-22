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
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - GB-GDS
related_entities:
  - GB
  - FR-FRANCECONNECT
  - DE-BUNDID
  - PL-MOBYWATEL
  - EU-EIDAS2
relationships:
  - type: part-of
    target: GB
    source: fact
    evidence: "Confirmed by reading oneid.uk (2026-08-22): 'In the UK, a government ID in digital form now covers three things worth separating: GOV.UK One Login, the system for proving your identity when you use government services; the GOV.UK Wallet, an app that holds government-issued credentials on your phone; and a separate national digital ID scheme, announced in September 2025 and built on One Login.' The January 2026 non-compulsory confirmation is also verbatim on this page: 'In January 2026 the government confirmed that holding it will not be compulsory, and that access to public services will not depend on having one.' Separately, gds.blog.gov.uk's 2021 post confirms 'single sign' and 'identity verification' verbatim, and its 2026 HMRC post confirms Government Gateway replacement: 'users who already have and actively use Government Gateway to access HMRC services.' Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "GOV.UK One Login — technical documentation"
    url: "https://docs.sign-in.service.gov.uk/"
    publisher: "Government Digital Service (UK)"
    accessed: "2026-08-22"
  - title: "GOV.UK One Login for HMRC: how we made it happen and what comes next"
    url: "https://gds.blog.gov.uk/2026/04/28/gov-uk-one-login-for-hmrc-how-we-made-it-happen-and-what-comes-next/"
    publisher: "Government Digital Service (UK)"
    accessed: "2026-08-22"
  - title: "A single sign-on and digital identity solution for government"
    url: "https://gds.blog.gov.uk/2021/07/13/a-single-sign-on-and-digital-identity-solution-for-government"
    publisher: "Government Digital Service (UK)"
    accessed: "2026-08-22"
  - title: "UK government ID: the digital ID scheme and the wallet"
    url: "https://oneid.uk/news-and-events/uk-government-id-the-digital-id-scheme-and-the-wallet"
    publisher: "OneID"
    accessed: "2026-08-22"
---

# GOV.UK One Login

> **Verified 2026-08-22.** oneid.uk, gds.blog.gov.uk's 2021 launch post and
> its 2026 HMRC post were read directly and confirmed the claims below,
> verbatim in places. `docs.sign-in.service.gov.uk` was fetched but its
> technical documentation did not restate these framing claims in its own
> words, so it is retained as a source without being the basis for any
> quote here. The phased-rollout dates (Companies House WebFiling from
> October 2025) were not independently re-confirmed this pass.

## Description

Confirmed by reading oneid.uk (2026-08-22): "GOV.UK One Login, the system
for proving your identity when you use government services; the GOV.UK
Wallet, an app that holds government-issued credentials on your phone; and
a separate national digital ID scheme, announced in September 2025 and
built on One Login." One Login is the UK's single sign-in and identity
verification service, replacing Government Gateway and dozens of separate
departmental logins — confirmed via gds.blog.gov.uk's HMRC post ("users
who already have and actively use Government Gateway to access HMRC
services"). It spans three things: **sign-in and identity proving**, the
**GOV.UK Wallet** for government-issued credentials on a phone, and a
**national digital ID scheme** announced in September 2025 and built on
top of it.

Rollout is phased — Companies House WebFiling from October 2025, new HMRC
users from February 2026. NOT independently re-confirmed this pass.

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

Confirmed verbatim on oneid.uk (2026-08-22): "In January 2026 the government
confirmed that holding it will not be compulsory, and that access to public
services would not depend on having one."

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

Listed in frontmatter — three GDS-published, one industry. oneid.uk,
the 2021 GDS post and the 2026 HMRC post were read directly this pass;
the technical documentation site was fetched but did not restate these
particular claims.
