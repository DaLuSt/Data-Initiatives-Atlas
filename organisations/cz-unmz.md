---
id: CZ-UNMZ
type: organisation
name: Úřad pro technickou normalizaci, metrologii a státní zkušebnictví
alternative_names:
  - ÚNMZ
  - UNMZ
  - Czech Office for Standards, Metrology and Testing
description: >
  Czechia's office for standards, metrology and testing, which represents the
  country at ISO, IEC, CEN and CENELEC and holds the formal membership and
  legal responsibility on behalf of the state. The operational work of
  technical committees, standard drafting and publication is performed by the
  Czech Standardization Agency (ČAS).

level: national
country: CZ
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-CEN
  - EU-CENELEC
  - INTL-ISO
  - INTL-IEC
relationships:
  - type: participates-in
    target: EU-CEN
    source: fact
    evidence: "Confirmed by reading cencenelec.eu's own centenary article directly (2026-08-26), which names 'the Czech Office for Standards, Metrology and Testing (ÚNMZ) and the Czech Standardization Agency (ČAS)' as distinct bodies, with ÚNMZ's president (Viktor Pokorný) and ČAS's director general (Zdeněk Veselý) attending separately. agenturacas.gov.cz's own 'Standards development' page, read independently, confirms ČAS's operational role is grounded in Act No. 22/1997 Coll. on technical requirements for products — a specific legal citation this entity did not previously carry."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-CENELEC
    source: fact
    evidence: "Same sourcing as the EU-CEN edge above — cencenelec.eu and agenturacas.gov.cz, both read directly (2026-08-26)."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: INTL-ISO
    source: fact
    evidence: "Same sourcing as the EU-CEN edge above — cencenelec.eu and agenturacas.gov.cz, both read directly (2026-08-26)."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: INTL-IEC
    source: fact
    evidence: "Same sourcing as the EU-CEN edge above — cencenelec.eu and agenturacas.gov.cz, both read directly (2026-08-26)."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "UNMZ/ČAS and UNMS SR celebrated the 100th anniversary of Czechoslovak standardization"
    url: "https://www.cencenelec.eu/news-events/news/2023/newsletter/on-the-spot-40-unmz-cas-and-unms-sr/"
    publisher: "CEN-CENELEC"
    accessed: "2026-08-26"
  - title: "Standards development"
    url: "https://agenturacas.gov.cz/en/standards-development/standards-development-2/"
    publisher: "Česká agentura pro standardizaci (ČAS)"
    accessed: "2026-08-26"
  - title: "Úřad pro technickou normalizaci, metrologii a státní zkušebnictví"
    url: "https://www.unmz.cz/"
    publisher: "ÚNMZ"
    accessed: "2026-08-26"
  - title: "European Standards"
    url: "https://www.cencenelec.eu/european-standardization/european-standards/"
    publisher: "CEN-CENELEC"
---

# Úřad pro technickou normalizaci, metrologii a státní zkušebnictví

> **Verified 2026-08-26.** Three of four cited pages were read directly
> (the generic "European Standards" explainer page adds no
> country-specific content and was not re-fetched). ČAS's own page adds
> a specific legal citation for its role and, unexpectedly, lists ETSI
> alongside ISO/IEC/CEN/CENELEC among its own cooperation duties — an
> open question about the membership split noted below, not resolved.

## Description

ÚNMZ is Czechia's office for standards, metrology and testing.

## Membership and the work are split between two bodies

This is the reason Czechia's standards entry needed care rather than a
template.

- **ÚNMZ holds the formal membership** at [[INTL-ISO]], [[INTL-IEC]],
  [[EU-CEN]] and [[EU-CENELEC]], and the legal responsibility on behalf of
  the state.
- **ČAS** — Česká agentura pro standardizaci — performs the **operational
  work**: technical committees, standard drafting, publication.

No other country in the Atlas splits it this way. Every other national
standards body is both the member and the drafter.

The `participates-in` edges are therefore asserted on **ÚNMZ and not ČAS**,
because membership is what those edges mean. **ČAS is not modelled**, which
understates Czech standardisation: the body that actually produces ČSN
standards is absent from the graph. That is logged in
`discovery/unresolved.md`.

Getting this wrong would have been easy — ČAS is the more visible body and
publishes the English-language standards pages — and the resulting entity
would have claimed a membership ČAS does not hold.

## A loose end: ETSI

ČAS's own "Standards development" page, read directly this pass, lists
its own cooperation and membership duties as spanning "ISO, IEC, CEN,
CENELEC, and ETSI" — adding [[EU-ETSI]] to the list, and doing so on
ČAS's page rather than ÚNMZ's. Whether ÚNMZ or ČAS holds the formal
ETSI membership is not established by anything read: it could follow
the same ÚNMZ-holds-membership pattern, or ETSI could be the one
standards body where ČAS itself is the member. No relationship to
[[EU-ETSI]] is asserted from either entity until this is resolved.

## Relationships

- `participates-in` [[EU-CEN]], [[EU-CENELEC]], [[INTL-ISO]] and
  [[INTL-IEC]].

## Sources

Listed in frontmatter, three of four read directly this pass.
