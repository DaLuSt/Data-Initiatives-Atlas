---
id: IE-CSO
type: organisation
name: Central Statistics Office
alternative_names:
  - CSO
  - An Phríomh-Oifig Staidrimh
description: >
  Ireland's national statistical institute, responsible for the collection
  and dissemination of official statistics and Ireland's national
  statistical institute within the European Statistical System.

level: national
country: IE
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-21"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-ESS
relationships:
  - type: part-of
    target: EU-ESS
    source: fact
    evidence: "The European Statistical System is the partnership between the Community statistical authority, which is the Commission (Eurostat), and the national statistical institutes and other national authorities responsible in each member state for the development, production and dissemination of European statistics, confirmed 2026-08-21 on ec.europa.eu/eurostat/web/european-statistical-system. The CSO is the Irish NSI (cso.ie). The founding regulation, EC 223/2009, is cited on secondary sources but was not itself read — eur-lex.europa.eu returns an AWS WAF bot-defense challenge to every fetch attempt in this environment, not the statute text."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Central Statistics Office"
    url: "https://www.cso.ie/en/"
    publisher: "Central Statistics Office (Ireland)"
    accessed: "2026-08-21"
  - title: "European Statistical System (ESS)"
    url: "https://ec.europa.eu/eurostat/web/european-statistical-system"
    publisher: "Eurostat / European Commission"
    accessed: "2026-08-21"
  - title: "Central Statistics Office (Ireland)"
    url: "https://en.wikipedia.org/wiki/Central_Statistics_Office_(Ireland)"
    publisher: "Wikipedia"
    accessed: "2026-08-21"
---

# Central Statistics Office (CSO)

> **Verified 2026-08-21.** Every cited source was read and confirmed to
> support what this entity says. `verification: primary-source`.

## Description

The CSO is Ireland's national statistical institute.

## The sixth member of [[EU-ESS]] in the Atlas

[[EU-ESS]] was created in the UN-connection batch and was described there as
"the single highest-value item this batch produced" — one entity that
connected four national statistical offices at once.

It now connects six: [[NL-CBS]], [[DE-DESTATIS]], [[BE-STATBEL]],
[[ES-INE]], [[PL-GUS]] and the CSO, plus [[EU-EUROSTAT]] itself.

The two countries in this batch that do **not** join it are the interesting
ones. [[NO-SSB]] and [[CH-BFS]] both carry no ESS edge, because the ESS is
defined as a partnership with the national statistical institutes **of the
member states** and neither Norway nor Switzerland is one. Ireland joins
without argument for exactly the reason they cannot.

France remains the only Atlas member state with **no statistical office at
all** — INSEE is still unmodelled and still queued.

## Not modelled

- The **Statistics Act 1993**, the CSO's statutory basis.
- Any relationship to [[UN-CES]], which [[GB-ONS]] carries.
- **data.cso.ie** and the CSO's open data publication.

## Relationships

- `part-of` [[EU-ESS]].

## Sources

Listed in frontmatter.
