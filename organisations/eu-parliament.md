---
id: EU-PARLIAMENT
type: organisation
name: European Parliament
alternative_names:
  - EP
description: >
  Directly elected legislative institution of the European Union. With the
  Council of the EU it is one of the two co-legislators under the ordinary
  legislative procedure, which applies in 85 defined policy areas covering
  most EU competences.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-11-17"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-COUNCIL
  - EU-COMMISSION
relationships:
  - type: part-of
    target: EU
    source: fact
    evidence: "Treaty on European Union (consolidated, CELEX 12016M/TXT), read directly 2026-11-17 from the Publications Office text: Article 13(1), \"The Union's institutions shall be: — the European Parliament, — the European Council, — the Council, — the European Commission ...\"; Article 14(1), \"The European Parliament shall, jointly with the Council, exercise legislative and budgetary functions.\""
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Ordinary legislative procedure — overview"
    url: "https://www.europarl.europa.eu/olp/en/ordinary-legislative-procedure/overview"
    publisher: "European Parliament"
  - title: "Ordinary legislative procedure — infographic"
    url: "https://www.europarl.europa.eu/infographic/legislative-procedure/index_en.html"
    publisher: "European Parliament"
  - title: "Treaty on European Union (consolidated version 2016), Articles 13 to 17"
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:12016M/TXT"
    publisher: "EUR-Lex (Publications Office of the European Union)"
    accessed: "2026-11-17"
---

# European Parliament

> **Verified 2026-08-21.** Every source this entity cites is on a domain the
> repository owner confirmed read and correct — `europa.eu`. `verification:
> primary-source`. See `docs/re-verification.md` §"The confirmed domains".

## Description

The European Parliament is one of the EU's two co-legislators. Under the
ordinary legislative procedure it stands on equal footing with
[[EU-COUNCIL]]: neither can adopt legislation without the other's
agreement, and both must approve an identical text. The procedure applies in
85 defined policy areas covering the majority of EU competences, and runs
through up to three readings.

Every regulation and directive in this Atlas's `legislation/` folder was
adopted by the Parliament and the Council jointly.

## No adoption relationships asserted

**The Parliament is deliberately not linked to the individual instruments it
adopted.** Doing so would add an `adopted-by` edge from every one of the
sixteen EU legislative entities to both co-legislators — 32 relationships
conveying one fact already implied by the entity type, and drowning the
substantive relationships (`implements-requirement-from`, `supersedes`)
the Atlas exists to surface.

If a future batch wants adoption modelled, it should be done systematically
with a dedicated relationship type, not piecemeal. Recorded in
`discovery/unresolved.md` as a modelling question.

`coverage: low`: the Parliament's committee structure and its role in
specific dossiers were not researched.

## Relationships

- Co-legislator with [[EU-COUNCIL]]; acts on proposals from
  [[EU-COMMISSION]].

## Sources

Listed in frontmatter.
