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
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
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
    evidence: "The Czech Republic is represented at state level in the international and European standardization organizations by ÚNMZ, the Czech Office for Standards, Metrology and Testing, which represents the country at ISO, IEC, CEN and CENELEC and holds the formal membership and legal responsibility on behalf of the state, while ČAS — Česká agentura pro standardizaci — performs the operational work of technical committees, standard drafting and publication (cencenelec.eu 'UNMZ/ČAS and UNMS SR celebrated the 100th anniversary of Czechoslovak standardization'; agenturacas.gov.cz 'Standards development'; unmz.cz). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-CENELEC
    source: fact
    evidence: "The Czech Republic is represented at state level in the international and European standardization organizations by ÚNMZ, the Czech Office for Standards, Metrology and Testing, which represents the country at ISO, IEC, CEN and CENELEC and holds the formal membership and legal responsibility on behalf of the state, while ČAS — Česká agentura pro standardizaci — performs the operational work of technical committees, standard drafting and publication (cencenelec.eu 'UNMZ/ČAS and UNMS SR celebrated the 100th anniversary of Czechoslovak standardization'; agenturacas.gov.cz 'Standards development'; unmz.cz). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: INTL-ISO
    source: fact
    evidence: "The Czech Republic is represented at state level in the international and European standardization organizations by ÚNMZ, the Czech Office for Standards, Metrology and Testing, which represents the country at ISO, IEC, CEN and CENELEC and holds the formal membership and legal responsibility on behalf of the state, while ČAS — Česká agentura pro standardizaci — performs the operational work of technical committees, standard drafting and publication (cencenelec.eu 'UNMZ/ČAS and UNMS SR celebrated the 100th anniversary of Czechoslovak standardization'; agenturacas.gov.cz 'Standards development'; unmz.cz). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: INTL-IEC
    source: fact
    evidence: "The Czech Republic is represented at state level in the international and European standardization organizations by ÚNMZ, the Czech Office for Standards, Metrology and Testing, which represents the country at ISO, IEC, CEN and CENELEC and holds the formal membership and legal responsibility on behalf of the state, while ČAS — Česká agentura pro standardizaci — performs the operational work of technical committees, standard drafting and publication (cencenelec.eu 'UNMZ/ČAS and UNMS SR celebrated the 100th anniversary of Czechoslovak standardization'; agenturacas.gov.cz 'Standards development'; unmz.cz). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "UNMZ/ČAS and UNMS SR celebrated the 100th anniversary of Czechoslovak standardization"
    url: "https://www.cencenelec.eu/news-events/news/2023/newsletter/on-the-spot-40-unmz-cas-and-unms-sr/"
    publisher: "CEN-CENELEC"
  - title: "Standards development"
    url: "https://agenturacas.gov.cz/en/standards-development/standards-development-2/"
    publisher: "Česká agentura pro standardizaci (ČAS)"
  - title: "Úřad pro technickou normalizaci, metrologii a státní zkušebnictví"
    url: "https://www.unmz.cz/"
    publisher: "ÚNMZ"
  - title: "European Standards"
    url: "https://www.cencenelec.eu/european-standardization/european-standards/"
    publisher: "CEN-CENELEC"
---

# Úřad pro technickou normalizaci, metrologii a státní zkušebnictví

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

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

## Relationships

- `participates-in` [[EU-CEN]], [[EU-CENELEC]], [[INTL-ISO]] and
  [[INTL-IEC]].

## Sources

Listed in frontmatter.
