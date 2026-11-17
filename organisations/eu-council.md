---
id: EU-COUNCIL
type: organisation
name: Council of the European Union
alternative_names:
  - Council of the EU
  - Council
description: >
  Institution representing member state governments and, with the European
  Parliament, one of the two co-legislators of the European Union under the
  ordinary legislative procedure.

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
  - EU-PARLIAMENT
  - EU-COMMISSION
relationships:
  - type: part-of
    target: EU
    source: fact
    evidence: "Treaty on European Union (consolidated, CELEX 12016M/TXT), read directly 2026-11-17 from the Publications Office text: Article 13(1), \"The Union's institutions shall be: — the European Parliament, — the European Council, — the Council, — the European Commission ...\"; Article 16(1), \"The Council shall, jointly with the European Parliament, exercise legislative and budgetary functions\", and 16(2), it 'shall consist of a representative of each Member State at ministerial level'."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "The ordinary legislative procedure"
    url: "https://www.consilium.europa.eu/en/council-eu/decision-making/ordinary-legislative-procedure/"
    publisher: "Council of the European Union"
  - title: "Treaty on European Union (consolidated version 2016), Articles 13 to 17"
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:12016M/TXT"
    publisher: "EUR-Lex (Publications Office of the European Union)"
    accessed: "2026-11-17"
---

# Council of the European Union

> **Verified 2026-08-21.** Every source this entity cites is on a domain the
> repository owner confirmed read and correct — `europa.eu`. `verification:
> primary-source`. See `docs/re-verification.md` §"The confirmed domains".

## Description

The Council of the European Union represents member state governments and is
one of the EU's two co-legislators. Under the ordinary legislative procedure
it has equal rights and obligations with [[EU-PARLIAMENT]]: the two adopt
legislation jointly, and both must approve an identical text.

As with the Parliament, **no adoption relationships to individual
instruments are asserted** — see the reasoning on [[EU-PARLIAMENT]].

`coverage: low`: the Council's configurations, presidency rotation and
working-party structure were not researched. This entity exists so that the
legislative picture has both co-legislators rather than one.

## Relationships

- Co-legislator with [[EU-PARLIAMENT]]; acts on proposals from
  [[EU-COMMISSION]].

## Sources

Listed in frontmatter — a single source.
