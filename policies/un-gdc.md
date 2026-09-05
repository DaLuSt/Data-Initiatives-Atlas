---
id: UN-GDC
type: policy
name: Global Digital Compact
alternative_names:
  - GDC
description: >
  Compact adopted by UN member states in September 2024 as part of the
  Pact for the Future (UN General Assembly resolution A/RES/79/1),
  committing to actions on digital inclusion, human-rights safeguards for
  digital technologies, and interoperable data governance. Paragraph 48
  of the Compact requested the Commission on Science and Technology for
  Development (hosted by UN Trade and Development) to establish a
  multi-stakeholder working group on data governance at all levels.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2024-09-01
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - UN
related_entities:
  - UN-UNCTAD
relationships:
  - type: part-of
    target: UN
    source: fact
    evidence: "Confirmed by reading un.org's own 'Global Digital Compact' and 'Annex I: Global Digital Compact' pages directly (2026-09-05): the Compact was adopted in September 2024 as part of the Pact for the Future, formally adopted by UN General Assembly resolution A/RES/79/1 ('Pact for the Future including the Global Digital Compact and Declaration on Future Generations'). Intergovernmental negotiations were co-facilitated by Sweden and Zambia."
    confidence: high
    valid_from: 2024-09-01
    valid_until: null
  - type: influences
    target: UN-UNCTAD
    source: fact
    evidence: "Confirmed by reading un.org's own Annex I page directly (2026-09-05), quoting paragraph 48 verbatim: 'we request the Commission on Science and Technology for Development to establish a dedicated working group to engage in a comprehensive and inclusive multi-stakeholder dialogue on data governance at all levels as relevant for development.' The CSTD is hosted within UN-UNCTAD, per that entity's own file."
    confidence: high
    valid_from: 2024-09-01
    valid_until: null

sources:
  - title: "The United Nations members adopted a Global Digital Compact shaping a safe and sustainable digital future for all"
    url: "https://digital-strategy.ec.europa.eu/en/news/united-nations-members-adopted-global-digital-compact-shaping-safe-and-sustainable-digital-future"
    publisher: "European Commission — Shaping Europe's digital future"
  - title: "Global Digital Compact"
    url: "https://www.un.org/en/summit-of-the-future/global-digital-compact"
    publisher: "United Nations (Summit of the Future)"
    accessed: "2026-09-05"
  - title: "Annex I: Global Digital Compact"
    url: "https://www.un.org/pact-for-the-future/en/annex-i-global-digital-compact"
    publisher: "United Nations (Pact for the Future)"
    accessed: "2026-09-05"
---

# Global Digital Compact

> **Re-verified 2026-09-05.** `un.org`'s own pages were read directly for
> the first time this pass, closing the "sourcing asymmetry" this entity
> previously flagged (its only source had been a European Commission news
> page, not a UN one). The adoption date and the data-governance
> working-group connection are now sourced facts rather than gaps.

## Description

The Global Digital Compact was adopted by UN member states in
**September 2024** as part of the **Pact for the Future**, formally
adopted by **UN General Assembly resolution A/RES/79/1** ("Pact for the
Future including the Global Digital Compact and Declaration on Future
Generations") — confirmed by reading `un.org`'s own pages directly.
Intergovernmental negotiations were co-facilitated by **Sweden and
Zambia**. Reported commitments by 2030 include:

- developing innovative financing mechanisms and incentives to connect the
  remaining **2.6 billion people** without internet access;
- establishing safeguards against adverse human-rights impacts from digital
  technologies;
- providing access to independent, science-based information to counter
  misinformation.

## Requests a data-governance working group

Reading `un.org`'s own "Annex I: Global Digital Compact" page directly:
**paragraph 48** states, in the Compact's own words, *"we request the
Commission on Science and Technology for Development to establish a
dedicated working group to engage in a comprehensive and inclusive
multi-stakeholder dialogue on data governance at all levels as relevant
for development."* That CSTD working group is hosted within
[[UN-UNCTAD]], whose own file separately confirms this same text and was
promoted to `primary-source` the same pass. This closes a long-standing
gap on both entities: neither could previously confirm the working
group's founding instrument from a page actually read.

## Sourcing asymmetry, now resolved

The only source previously located for this UN instrument was a European
Commission news page — odd and weak for a UN compact. Two of `un.org`'s
own pages are now read directly, closing that gap, and the adoption date
(previously unrecorded, `start_date: null`) is now `2024-09-01`.

## Typing note

Recorded as `policy` rather than `strategy` or `initiative`: it is a
negotiated set of commitments adopted by member states, closer to a policy
instrument than to an organisational strategy. It is not binding
legislation, so `law`/`regulation` would be wrong.

## Relationships

- Adopted within [[UN]], via UN General Assembly resolution A/RES/79/1.
- `influences` [[UN-UNCTAD]] — paragraph 48 requests its CSTD establish
  the data-governance working group.

## Sources

Listed in frontmatter. The two `un.org` pages were read directly this
pass; the European Commission news page was not re-fetched.
