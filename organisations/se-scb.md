---
id: SE-SCB
type: organisation
name: Statistics Sweden
alternative_names:
  - SCB
  - Statistiska centralbyran
  - Statistiska centralbyrån
description: >
  Sweden's national statistical institute and the national authority
  within the European Statistical System.

level: national
country: SE
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-25"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - SE
  - EU-ESS
relationships:
  - type: part-of
    target: SE
    source: fact
    evidence: "Confirmed by reading scb.se's own 'About us' page directly (2026-08-25): 'Statistics Sweden is responsible for official statistics and for other government statistics. This means that we develop, produce and disseminate the statistics. In addition, we coordinate the system for the official statistics in Sweden.'"
    confidence: medium
    valid_from: null
    valid_until: null
  - type: part-of
    target: EU-ESS
    source: fact
    evidence: "Statistics Sweden is the national statistical institute of its member state; the European Statistical System is the partnership between Eurostat and the national statistical institutes and other national authorities responsible for European statistics (ec.europa.eu/eurostat 'European Statistical System', read directly 2026-08-25). scb.se's own homepage and 'About us' page were both read this pass and neither names Eurostat or the ESS directly, so this edge still rests on the composition rule — the same call made on [[LU-STATEC]] and [[DK-DST]] in earlier passes."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Statistics Sweden"
    url: "https://www.scb.se/en/"
    publisher: "Statistiska centralbyran (SCB)"
    accessed: "2026-08-25"
  - title: "About us - Statistics Sweden"
    url: "https://www.scb.se/en/About-us/"
    publisher: "Statistiska centralbyran (SCB)"
    accessed: "2026-08-25"
  - title: "European Statistical System (ESS)"
    url: "https://ec.europa.eu/eurostat/web/european-statistical-system"
    publisher: "Eurostat"
    accessed: "2026-08-25"
---

# Statistics Sweden

> **Verified 2026-08-25.** All three cited pages were read directly.
> scb.se's own page confirms its identity directly, but does not
> describe [[EU-ESS]] membership in its own words — that edge still
> rests on the composition rule, the same call made on [[LU-STATEC]]
> and [[DK-DST]] in earlier passes.

## Description

Confirmed by reading scb.se directly (2026-08-25): Sweden's national
statistical institute - the **fifteenth** on [[EU-ESS]].

## Sources

Listed in frontmatter, all three read directly this pass.
