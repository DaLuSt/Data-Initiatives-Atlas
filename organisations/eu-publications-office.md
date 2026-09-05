---
id: EU-PUBLICATIONS-OFFICE
type: organisation
name: Publications Office of the European Union
alternative_names:
  - Publications Office
  - OP
description: >
  Official publisher of the European Union, established 1969 and based in
  Luxembourg. An EU interinstitutional service (not a standalone agency),
  it provides publishing services to all EU institutions, bodies and
  agencies, managing EUR-Lex and the Official Journal, and is a
  co-initiator of the DCAT Application Profile for data portals in Europe.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-DCAT-AP
relationships:
  - type: part-of
    target: EU
    source: fact
    evidence: "Confirmed by reading european-union.europa.eu's own institutional-directory page for the Office directly (2026-09-05): 'the official provider of publishing services to all EU institutions, bodies and agencies,' classified as an 'EU interinstitutional service' — established 1969 (year only; no exact day given), based in Luxembourg, managing EUR-Lex and the Official Journal, led by Director-General Hilde Hardeman with 615 staff. Closes the gap this entity's own prior text flagged: the EUR-Lex publisher role was previously asserted only from the Atlas's own citation practice, which was circular."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Publications Office of the European Union (OP)"
    url: "https://european-union.europa.eu/institutions-law-budget/institutions-and-bodies/search-all-eu-institutions-and-bodies/publications-office-european-union-op_en"
    publisher: "European Union (official institutional directory)"
    accessed: "2026-09-05"
  - title: "About us: mission, vision, values"
    url: "https://op.europa.eu/en/web/about-us/about-publication-office-of-the-european-union"
    publisher: "Publications Office of the European Union"
  - title: "Get started with DCAT-AP"
    url: "https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/solution/dcat-application-profile-data-portals-europe/news/get-started-dcat-ap"
    publisher: "European Commission — Interoperable Europe Portal"
---

# Publications Office of the European Union

> **Verified 2026-08-21.** Every source this entity cites is on a domain the
> repository owner confirmed read and correct — `europa.eu`. `verification:
> primary-source`. See `docs/re-verification.md` §"The confirmed domains".
>
> **The circular-sourcing gap closed, 2026-09-05.** Picked up from
> `discovery/unresolved.md`. european-union.europa.eu's own institutional
> directory, read directly, now describes the Office itself — closing the
> gap the prior text flagged rather than resting on the Atlas's own
> citation practice.

## Description

The Publications Office is the EU's official publisher. Confirmed by
reading european-union.europa.eu's own institutional-directory page for
the Office directly: it is **"the official provider of publishing
services to all EU institutions, bodies and agencies,"** established in
**1969** (year only; no exact day found), based in **Luxembourg**, and
classified as an **EU interinstitutional service** — not a standalone
agency, but a service operating across multiple institutions. It manages
EUR-Lex and the Official Journal — the texts underpinning the entire
`legislation/` folder — led by Director-General Hilde Hardeman with a
staff of 615.

Its other sourced substantive role here is as a co-initiator of
[[EU-DCAT-AP]], alongside DG CONNECT and the Interoperable Europe
Programme.

## An honest weakness, now partly fixed

`confidence` raised from `low` to `medium`. **A source describing the
Publications Office itself was previously not located** — the only
citation was a DCAT-AP page mentioning it in passing, and its EUR-Lex
publisher role was asserted from the Atlas's own citation practice, which
was circular. That gap is closed this pass on the Office's own
institutional-directory entry. `coverage` stays `low`: no source read
covers its budget, full organisational structure, or the DCAT-AP
co-initiation in more depth than before.

## Relationships

- `part-of` [[EU]] — anchor edge, now sourced directly rather than
  asserted from citation practice.
- Co-initiator of [[EU-DCAT-AP]].

## Sources

Listed in frontmatter. The institutional-directory page was read directly
this pass; `op.europa.eu`'s own "About us" page is added as a further
citation but was not itself fetched this pass.
