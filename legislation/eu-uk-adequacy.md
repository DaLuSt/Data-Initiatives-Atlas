---
id: EU-UK-ADEQUACY
type: regulation
name: European Commission adequacy decisions for the United Kingdom
alternative_names:
  - UK adequacy decisions
  - UK data adequacy
description: >
  Two European Commission adequacy decisions permitting the free flow of
  personal data from the European Union to the United Kingdom, one adopted
  under the General Data Protection Regulation and one under Directive
  2016/680, the Law Enforcement Directive. The Commission renewed both on
  19 December 2025 for a further six years, following the changes made by
  the Data (Use and Access) Act 2025 and opinions adopted by the European
  Data Protection Board on the draft decisions. The renewed decisions are
  subject to a sunset clause and expire on 27 December 2031 unless extended.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2025-12-19
end_date: 2031-12-27
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - EU-EDPB
  - GB-ICO
related_entities:
  - EU-GDPR
  - GB-UK-GDPR
  - GB-DUAA
  - GB
relationships:
  - type: governed-by
    target: EU-GDPR
    source: fact
    evidence: "The European Commission adopted two adequacy decisions for the United Kingdom, one based on the General Data Protection Regulation and one based on Directive 2016/680, the Law Enforcement Directive; the European Data Protection Board adopted opinions on the Commission's draft decisions extending the validity of the UK adequacy decisions under the GDPR and the Law Enforcement Directive (eucrim.eu 'Commission Renewed Adequacy Decisions for Data Transfers to the UK'; edpb.europa.eu 'Draft UK adequacy decisions: EDPB adopts opinions'; hunton.com; aoshearman.com). NOT READ — search-only."
    confidence: medium
    valid_from: 2025-12-19
    valid_until: null
  - type: references
    target: GB-UK-GDPR
    source: fact
    evidence: "The adequacy decisions assess the United Kingdom's data protection regime; the Commission indicated that the UK remains adequate following the introduction of the Data (Use and Access) Act 2025, and renewed both decisions on 19 December 2025 with a sunset clause expiring 27 December 2031 (arnoldporter.com 'European Commission Indicates That the UK Remains Adequate Following the Introduction of the Data (Use and Access) Act 2025'; eucrim.eu; shepwedd.com; ico.org.uk 'Receiving personal information from the EEA'). NOT READ — search-only."
    confidence: medium
    valid_from: 2025-12-19
    valid_until: 2031-12-27
  - type: references
    target: GB-DUAA
    source: fact
    evidence: "The renewal followed the changes made by the Data (Use and Access) Act 2025; the European Commission indicated that the UK remains adequate following the introduction of that Act, and the extension to December 2031 was adopted after it (arnoldporter.com; aoshearman.com 'EU confirms UK adequacy decisions under EU GDPR and Law Enforcement Directive'; eucrim.eu). NOT READ — search-only."
    confidence: medium
    valid_from: 2025-12-19
    valid_until: null

sources:
  - title: "Commission Renewed Adequacy Decisions for Data Transfers to the UK"
    url: "https://eucrim.eu/news/commission-renewed-adequacy-decisions-for-data-transfers-to-the-uk/"
    publisher: "eucrim — The European Criminal Law Associations' Forum"
  - title: "Draft UK adequacy decisions: EDPB adopts opinions"
    url: "https://www.edpb.europa.eu/news/news/2025/draft-uk-adequacy-decisions-edpb-adopts-opinions_en"
    publisher: "European Data Protection Board (EDPB)"
  - title: "EU confirms UK adequacy decisions under EU GDPR and Law Enforcement Directive"
    url: "https://www.aoshearman.com/en/insights/ao-shearman-on-data/eu-confirms-uk-adequacy-decisions-under-eu-gdpr-and-law-enforcement-directive"
    publisher: "A&O Shearman"
  - title: "European Commission Indicates That the UK Remains Adequate Following the Introduction of the Data (Use and Access) Act 2025"
    url: "https://www.arnoldporter.com/en/perspectives/advisories/2025/07/uk-remains-adequate-following-intro-of-duaa-2025"
    publisher: "Arnold & Porter"
  - title: "Receiving personal information from the EEA"
    url: "https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/receiving-personal-information-from-the-eea/"
    publisher: "Information Commissioner's Office (UK)"
---

# EU adequacy decisions for the United Kingdom

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

Two European Commission decisions permitting personal data to flow freely
from the EU to the United Kingdom — one under [[EU-GDPR]], one under the Law
Enforcement Directive. Both were **renewed on 19 December 2025** for six
years, after the European Data Protection Board gave opinions on the drafts,
and both **expire on 27 December 2031** under a sunset clause unless
extended.

## The connection the UK batch refused, now made

[[GB]] and `countries/gb/index.md` both say this outright:

> *This is the single most important connective fact between the UK and the
> EU data layer, and **no entity or edge in this batch represents it**.*

It was the first item in the backlog's UK section. This entity closes it, and
what it adds is a **third kind** of EU–UK link, different from the two the UK
already had:

| Edge | Direction | What it means |
|---|---|---|
| [[GB-UK-GDPR]] `derived-from` [[EU-GDPR]] | UK → EU | the UK text came from the EU text |
| [[GB-NIS-REGULATIONS]] `implements-requirement-from` [[EU-NIS]] | UK → EU | a transposition made while a member state |
| **this entity** `references` [[GB-UK-GDPR]] | **EU → UK** | **the EU's present-tense judgement about the UK** |

The first two run **from** the UK and are both about history — what the UK
inherited, and what it did before leaving. This one runs **towards** the UK,
is current, and is the only edge in the Atlas where the European Union says
something about a non-member state's regime. It is also the only one with an
**expiry date in the structured data**.

## Why it is `level: regional` and `region: EU`

Because it is an **EU act**, not a UK one. The decisions are adopted by the
Commission, bind EU exporters, and are reviewable by the Court of Justice —
none of which is UK law. Filing it under `country: GB` would have made the
graph assert that the UK legislated its own adequacy, which is precisely
backwards.

It is therefore the first entity in the Atlas that is **about** one country
while belonging to another scope, and `related_entities` carries [[GB]] so
the association is visible from the UK side.

## `end_date`, used for the first time as a live deadline

`end_date: 2031-12-27` is not a historical fact. It is a **sunset clause**:
the decisions lapse on that date unless the Commission extends them. The
Atlas has `status: active` and an end date in the future, which is a
combination worth noticing — most entities with an `end_date` have already
ended.

⚠ **This is a second data point for a gap the UK batch opened.** [[GB-ICO]]
records a status the vocabulary cannot express: an instrument in force whose
mandated change has an unverified date. Here the shape is inverted — in force,
with a *known* date on which it stops being in force absent action. Neither
`active` nor `superseded` says that.

## Not modelled

- **The Law Enforcement Directive** (Directive 2016/680) itself, which is one
  of the two legal bases and is not an Atlas entity. The `governed-by` edge
  therefore points only at [[EU-GDPR]], and this body text is the only place
  the second basis is recorded.
- **The EDPB opinions** on the draft decisions, cited as a source and not
  modelled. [[EU-EDPB]] appears in `organisations:` as an association only.
- **The 2021 decisions** these replaced. No `previous_version` is set,
  because whether the December 2025 instruments are new decisions or
  extensions of the old ones is described both ways in the sources — as a
  *renewal* and as an *extension of validity* — and the distinction matters
  too much to guess.

## Relationships

- `governed-by` [[EU-GDPR]] — adopted under it.
- `references` [[GB-UK-GDPR]] and [[GB-DUAA]] — the regime assessed, and the
  Act whose changes the renewal followed.

## Sources

Listed in frontmatter. One is an EU institution (EDPB) and one a UK regulator
(ICO); the remaining three are legal commentary, which is why the whole
entity is `confidence: medium` and why the Commission's own decision texts
are the obvious first fetch.
