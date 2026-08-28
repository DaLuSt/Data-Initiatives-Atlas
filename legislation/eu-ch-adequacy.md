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
verification: primary-source

start_date: 2000-07-26
end_date: null
last_verified: "2026-08-28"
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
    evidence: "Confirmed by reading legislation.gov.uk's mirror of the adopted decision directly (2026-08-28), which quotes Article 1 verbatim: 'For the purposes of Article 25(2) of Directive 95/46/EC, for all the activities falling within the scope of that Directive, Switzerland is considered as providing an adequate level of protection for personal data transferred from the Community.' edoeb.admin.ch, the Swiss data protection commissioner's own page, also read directly, confirms the decision's continuity and the 2024 re-confirmation. `bj.admin.ch`, the URL originally cited here, now returns HTTP 404 — the Swiss Federal Office of Justice appears to have reorganised its site; a working replacement page at the same domain was found but no longer covers this specific decision's content, so it was dropped rather than kept as a citation that no longer supports the claim."
    confidence: high
    valid_from: 2000-07-26
    valid_until: null
  - type: references
    target: CH-REVDSG
    source: fact
    evidence: "Confirmed by reading edoeb.admin.ch's own page directly (2026-08-28): 'Switzerland's new data protection legislation meets the applicable adequacy requirements of the GDPR' — the Commission's 15 January 2024 confirmation was assessed against the revised Federal Act on Data Protection, not the 1992 act in force when the original 2000 decision was taken."
    confidence: high
    valid_from: 2024-01-15
    valid_until: null

sources:
  - title: "2000/518/EC: Commission Decision of 26 July 2000 pursuant to Directive 95/46/EC on the adequate protection of personal data provided in Switzerland"
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32000D0518"
    publisher: "EUR-Lex — Publications Office of the European Union"
  - title: "2000/518/EC — adopted text (mirror)"
    url: "https://www.legislation.gov.uk/eudn/2000/518/adopted"
    publisher: "The National Archives (legislation.gov.uk)"
    accessed: "2026-08-28"
  - title: "EU adequacy decision regarding Switzerland (15.01.2024)"
    url: "https://www.edoeb.admin.ch/en/15012024-eu-adequacy-decision-regarding-switzerland"
    publisher: "Eidgenössischer Datenschutz- und Öffentlichkeitsbeauftragter (EDÖB)"
    accessed: "2026-08-28"
---

# EU adequacy decision for Switzerland (2000/518/EC)

> **Re-verified 2026-08-28.** `eur-lex.europa.eu` remains unreadable to
> this pass's fetch tooling, consistent with every other EUR-Lex attempt
> made across this batch. In its place, a working UK National Archives
> mirror of the adopted decision text was found and read directly,
> quoting Article 1 verbatim, alongside the Swiss data protection
> commissioner's own page (re-confirmed). `bj.admin.ch`, previously cited,
> is now a dead link (HTTP 404) and has been dropped. `verification`
> moves from `search-only` to `primary-source`.

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

Listed in frontmatter, two of three read directly this pass: the UK
National Archives mirror of the decision's adopted text (quoting Article 1
verbatim) and the Swiss data protection commissioner's own page on the
2024 confirmation. The EUR-Lex CELEX record was attempted and returned
empty content, consistent with every other EUR-Lex attempt made across
this batch; it remains listed as the authoritative-but-unread citation.
The Swiss Federal Office of Justice's page, previously cited, is now a
dead link and has been removed rather than kept as a non-functioning
citation.
