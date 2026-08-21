---
id: EU-CH-ADEQUACY
type: regulation
name: European Commission adequacy decision for Switzerland
alternative_names:
  - Decision 2000/518/EC
  - Swiss adequacy decision
description: >
  Commission Decision 2000/518/EC of 26 July 2000, adopted under Article
  25(6) of Directive 95/46/EC, finding that Switzerland provides an adequate
  level of protection for personal data transferred from the Community.
  Published in OJ L 215 of 25 August 2000. It predates the General Data
  Protection Regulation and remains in force under Article 45(9) GDPR, which
  keeps pre-GDPR adequacy decisions in effect until amended, replaced or
  repealed. On 15 January 2024 the European Commission published a report
  confirming that Switzerland continues to offer an adequate level of data
  protection, following the entry into force of the revised Swiss Federal Act
  on Data Protection.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2000-07-26
end_date: null
last_verified: "2026-08-21"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - EU-COMMISSION
related_entities:
  - CH
  - CH-REVDSG
  - CH-EDOEB
  - EU-GDPR
  - EU-UK-ADEQUACY
relationships:
  - type: applies-in
    target: CH
    source: fact
    evidence: "Commission Decision 2000/518/EC of 26 July 2000 pursuant to Directive 95/46/EC on the adequate protection of personal data provided in Switzerland: for the purposes of Article 25(2) of Directive 95/46/EC, Switzerland is considered as providing an adequate level of protection for personal data transferred from the Community; published in OJ L 215 of 25 August 2000 (eur-lex.europa.eu CELEX 32000D0518 and ELI dec/2000/518; bj.admin.ch 'Adequacy of Switzerland by the EU'). NOT READ — search-only."
    confidence: medium
    valid_from: 2000-07-26
    valid_until: null
  - type: references
    target: CH-REVDSG
    source: fact
    evidence: "On 15 January 2024 the European Commission published a report confirming that Switzerland offers an adequate level of data protection, an assessment made after the revised Swiss Federal Act on Data Protection took effect (edoeb.admin.ch '15.01.2024 — EU adequacy decision regarding Switzerland'; bj.admin.ch 'Adequacy of Switzerland by the EU'). NOT READ — search-only."
    confidence: medium
    valid_from: 2024-01-15
    valid_until: null

sources:
  - title: "2000/518/EC: Commission Decision of 26 July 2000 pursuant to Directive 95/46/EC on the adequate protection of personal data provided in Switzerland"
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32000D0518"
    publisher: "EUR-Lex — Publications Office of the European Union"
  - title: "Decision 2000/518 — consolidated record"
    url: "https://eur-lex.europa.eu/eli/dec/2000/518"
    publisher: "EUR-Lex — Publications Office of the European Union"
  - title: "EU adequacy decision regarding Switzerland (15.01.2024)"
    url: "https://www.edoeb.admin.ch/en/15012024-eu-adequacy-decision-regarding-switzerland"
    publisher: "Eidgenössischer Datenschutz- und Öffentlichkeitsbeauftragter (EDÖB)"
  - title: "Adequacy of Switzerland by the EU"
    url: "https://www.bj.admin.ch/bj/en/home/staat/datenschutz/internationales/angemessenheit-ch.html"
    publisher: "Bundesamt für Justiz — Swiss Federal Office of Justice"
---

# EU adequacy decision for Switzerland (2000/518/EC)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read — retrieval is blocked by
> the network egress proxy. `verification: search-only`.

## Description

Commission Decision **2000/518/EC of 26 July 2000**, published in **OJ L 215
of 25 August 2000**. It finds, for the purposes of Article 25(2) of Directive
95/46/EC, that **Switzerland provides an adequate level of protection** for
personal data transferred from the Community.

Switzerland has therefore held adequacy **continuously since 2000** — longer
than any Atlas country other than the handful covered by the same first wave
of decisions.

## Why a decision from 2000 is still current

The decision was adopted under the directive the GDPR repealed. It survives
because **Article 45(9) GDPR** keeps adequacy decisions taken under Article
25(6) of Directive 95/46/EC in force until they are amended, replaced or
repealed by a new Commission decision. None has been.

What has happened instead is a **review**: on **15 January 2024** the
Commission published a report confirming that Switzerland continues to offer
an adequate level of protection, an assessment made against
[[CH-REVDSG]] — the revised Federal Act on Data Protection — rather than
against the 1992 act that was in force when the original decision was taken.

## The asymmetry with the United Kingdom is the point

The Atlas already holds [[EU-UK-ADEQUACY]]. Placing the Swiss decision beside
it shows two different shapes of the same instrument:

| | Switzerland | United Kingdom |
|---|---|---|
| Instrument | One decision, 2000/518/EC | Two decisions, 2021 |
| Legal basis | Article 25(6) of Directive 95/46/EC | Article 45(3) GDPR and the LED |
| Sunset clause | None | Yes — extended rather than allowed to lapse |
| Since | 2000 | 2021, after leaving the Union |

`discovery/candidates.md` recorded the gap as *"the Atlas holds
[[EU-UK-ADEQUACY]] and nothing equivalent for Switzerland, although the same
Commission act type covers it"*. The two are the same act type and they are
not the same shape, which is the more useful thing to be able to see.

## Relationships

- `applies-in` [[CH]] — the country the finding is about.
- `references` [[CH-REVDSG]], the act the 2024 confirmation was assessed
  against. `governed-by` would invert the relationship: the Commission
  decision is not governed by Swiss law, it assesses it.
- No edge to [[EU-GDPR]] is asserted. The decision predates the regulation
  and was taken under a different instrument; the GDPR provision that keeps
  it alive is a transitional rule, not a relationship between the two acts.

## Sources

Listed in frontmatter — the EUR-Lex CELEX and ELI records of the decision,
the Swiss data protection commissioner's page on the 2024 confirmation, and
the Swiss Federal Office of Justice's own account of Swiss adequacy.
