---
id: INTL-ISO-IEC-27002
type: standard
name: "ISO/IEC 27002 — Information security controls"
alternative_names:
  - ISO 27002
  - "ISO/IEC 27002:2022"
  - NEN-EN-ISO/IEC 27002
description: >
  International standard on information security, cybersecurity and privacy
  protection, providing a set of information security controls. Published
  jointly by ISO and IEC under JTC 1/SC 27, and applied in a risk-driven way
  alongside ISO/IEC 27001.

level: international
country: null
region: null

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-25"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations:
  - INTL-ISO
  - INTL-IEC
related_entities:
  - INTL-ISO-IEC-27001
  - NL-BIO
relationships:
  - type: maintained-by
    target: INTL-ISO
    source: fact
    evidence: "ISO/IEC 27002 is published by ISO and the IEC, titled 'Information security, cybersecurity and privacy protection — Information security controls', under JTC 1/SC 27. Confirmed independently by reading en.wikipedia.org's own ISO/IEC 27002 article directly (2026-09-05), which names the same two publishers and committee. Confirmed a second, stronger way 2026-09-25: standards.iteh.ai, an authorized ISO/IEC standards reseller, serves a free 'redline' preview PDF of the actual ISO/IEC 27002:2022 text (catalog number 75652, matching iso.org/standard/75652.html), read directly — its own Foreword states in as many words 'This document was prepared by Joint Technical Committee ISO/IEC JTC 1, Information technology, Subcommittee SC 27, Information security, cybersecurity and privacy protection' and 'This third edition cancels and replaces the second edition (ISO/IEC 27002:2013)', with 'Copyright Protected Document © ISO/IEC 2022' and ISO's own copyright-office address on every page. `iso.org` itself remains domain-wide blocked to this environment's own tooling (INTL standards-body cluster pass, 2026-08-28), but this is the standard's own published text, not a page about it."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "ISO/IEC 27002 — Information technology — Security techniques — Code of practice for information security controls (edition 2, 2013 — see the edition-mismatch note below)"
    url: "https://www.iso.org/obp/ui/#iso:std:iso-iec:27002:ed-2:en"
    publisher: "International Organization for Standardization (ISO)"
  - title: "ISO/IEC 27000 family — Information security management"
    url: "https://www.iso.org/standard/iso-iec-27000-family"
    publisher: "International Organization for Standardization (ISO)"
  - title: "ISO/IEC 27002:2022 — Information security, cybersecurity and privacy protection — Information security controls (current edition 3; identified via WebSearch 2026-09-05, not itself part of the owner's 2026-08-21 confirmed-domain review, and iso.org is now confirmed blocked to this environment's own fetch tooling)"
    url: "https://www.iso.org/standard/75652.html"
    publisher: "International Organization for Standardization (ISO)"
  - title: "ISO/IEC 27002"
    url: "https://en.wikipedia.org/wiki/ISO/IEC_27002"
    publisher: "Wikipedia"
    accessed: "2026-09-05"
  - title: "ISO/IEC 27002:2022 — redline preview (compares third edition to second edition), catalog #75652"
    url: "https://cdn.standards.iteh.ai/samples/75652/0430bd40787c42488cea9c48525b8fc2/ISO-IEC-27002-2022.pdf"
    publisher: "iTeh Standards (authorized ISO/IEC reseller), reproducing © ISO/IEC 2022 text"
    accessed: "2026-09-25"
---

# ISO/IEC 27002

> **Verified 2026-08-21.** Every source this entity cites is on a domain the
> repository owner confirmed read and correct — `iso.org`. `verification:
> primary-source`. See `docs/re-verification.md` §"The confirmed domains".
>
> **Edition citation narrowed, 2026-09-05.** The correct edition-3 (2022)
> standard number — `iso.org/standard/75652.html` — was found via
> WebSearch and Wikipedia's own ISO/IEC 27002 article (read directly),
> which independently corroborates the March 2022 publication date and the
> ISO/IEC/JTC 1 SC 27 maintainer. The original edition-2 citation stays in
> `sources` rather than being replaced, since it is the specific URL the
> owner's confirmed-domain review actually covered; the new edition-3 URL
> is added alongside it but is not itself owner-confirmed, and iso.org is
> now separately known to be domain-wide blocked to this environment's own
> fetch tooling. The edition mismatch this entity exists to flag is
> narrowed — the correct URL is now known — but not fully closed, since
> nobody has read the edition-3 page's own content directly.
>
> **Closed 2026-09-25**, `discovery/unresolved.md` row #166: `iso.org`
> itself remains domain-wide blocked, but `standards.iteh.ai` — an
> authorized ISO/IEC standards reseller — serves a free "redline" preview
> PDF of the actual ISO/IEC 27002:2022 text under the same catalog number
> (75652), read directly. Its own Foreword states outright that "this
> third edition cancels and replaces the second edition (ISO/IEC
> 27002:2013)" and names the JTC 1/SC 27 authorship, confirming the
> edition-3 citation from the standard's own published text rather than a
> third party's description of it. `confidence` raised to `high` on the
> `maintained-by` edge.

## Description

ISO/IEC 27002 is titled *Information security, cybersecurity and privacy
protection — Information security controls*. It supplies the control set
applied alongside [[INTL-ISO-IEC-27001]]: where 27001 specifies ISMS
requirements, 27002 provides the controls to be selected on the basis of
assessed risk.

Published jointly by [[INTL-ISO]] and [[INTL-IEC]] under JTC 1/SC 27.

## An edition mismatch — closed, 2026-09-25

The originally-cited ISO Online Browsing Platform link resolves to
**edition 2 (2013)**, whose title is the older *Information technology —
Security techniques — Code of practice for information security controls*.
The current edition is **27002:2022** (the 3rd edition, published **March
2022** per en.wikipedia.org's own article, read directly), with the newer
title used in the `name` field above, and it is that edition [[NL-BIO]]'s
BIO2 references (as NEN-EN-ISO/IEC 27002:2022).

`iso.org` remains domain-wide blocked to this environment's own fetch
tooling, so its catalog page (`iso.org/standard/75652.html`) itself was
still not read directly this pass. But the standard's own text now has
been: `standards.iteh.ai`, an authorized ISO/IEC standards reseller,
serves a free "redline" preview PDF of ISO/IEC 27002:2022 under the same
catalog number (75652) — 15 pages including the full front matter,
Foreword, Introduction and the opening clauses (Scope, Normative
references, Terms and definitions through 3.1.17), read directly. The
Foreword states in its own words: **"This third edition cancels and
replaces the second edition (ISO/IEC 27002:2013)"** and names "Joint
Technical Committee ISO/IEC JTC 1, Information technology, Subcommittee
SC 27, Information security, cybersecurity and privacy protection" as the
document's author — independently confirming both facts Wikipedia had
already supplied, this time from the standard's own published text rather
than a third party's description of it. Every page carries "Copyright
Protected Document © ISO/IEC 2022" and ISO's own copyright-office
address, leaving no doubt this is ISO/IEC's own content served through an
authorized channel, not a paraphrase. The original edition-2 citation is
kept in `sources` as a record of what the entity originally, mistakenly,
pointed to.

`coverage` raised from `low` to `medium`: this is the first pass to read
any part of the standard's own substantive text (structure, scope,
terminology) rather than resting entirely on a bibliographic citation.

## Relationships

- Published by [[INTL-ISO]] and [[INTL-IEC]].
- Companion to [[INTL-ISO-IEC-27001]].
- Basis for [[NL-BIO]]'s control set.

## Sources

Listed in frontmatter — see the edition caveat above. The Wikipedia
article was read directly in the 2026-09-05 pass; the `iso.org` citations
themselves were never read directly (owner-confirmed-domain licensing for
the original two; the domain is now confirmed blocked). The
`standards.iteh.ai` redline preview PDF, added and read directly
2026-09-25, is the first source in this list that reproduces the
standard's own text rather than describing or cataloguing it.
