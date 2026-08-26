---
id: DK-DST
type: organisation
name: Statistics Denmark
alternative_names:
  - Danmarks Statistik
description: >
  Denmark's national statistical institute and the national authority
  within the European Statistical System.

level: national
country: DK
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
  - DK
  - EU-ESS
relationships:
  - type: part-of
    target: DK
    source: fact
    evidence: "Confirmed by reading dst.dk's own 'The role and mandate of Statistics Denmark' page directly (2026-08-25): 'Statistics Denmark is Denmark's national statistical authority... Statistics Denmark is responsible for official statistics in Denmark, as established by the Act on Statistics Denmark. We are an independent institution that has been providing statistics about and for Denmark since 1850.' The Act's own citation was not itself read this pass, so no legislation entity was created from the name alone."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: part-of
    target: EU-ESS
    source: fact
    evidence: "Statistics Denmark is the national statistical institute of its member state; the European Statistical System is the partnership between Eurostat and the national statistical institutes and other national authorities responsible for European statistics (ec.europa.eu/eurostat 'European Statistical System', read directly 2026-08-25). No page read this pass has Statistics Denmark describe its own ESS membership directly — dst.dk's 'role and mandate' and 'organisation' pages were both checked and neither mentions Eurostat or the ESS by name — so this edge still rests on the composition rule, the same basis on which most national statistical offices in the Atlas are attached."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Statistics Denmark"
    url: "https://www.dst.dk/en"
    publisher: "Danmarks Statistik"
    accessed: "2026-08-25"
  - title: "The role and mandate of Statistics Denmark"
    url: "https://www.dst.dk/en/OmDS/danmarks-statistiks-rolle-og-opgave"
    publisher: "Danmarks Statistik"
    accessed: "2026-08-25"
  - title: "European Statistical System (ESS)"
    url: "https://ec.europa.eu/eurostat/web/european-statistical-system"
    publisher: "Eurostat"
    accessed: "2026-08-25"
---

# Statistics Denmark

> **Verified 2026-08-25.** All three cited pages were read directly.
> dst.dk's own page confirms its identity, its 1850 founding and a
> named legal basis (the Act on Statistics Denmark) directly, but does
> not describe [[EU-ESS]] membership in its own words — that edge
> still rests on the composition rule, the same call made on
> [[LU-STATEC]] in the previous pass.

## Description

Confirmed by reading dst.dk directly (2026-08-25): Denmark's national
statistical institute - the **fourteenth** on [[EU-ESS]] - established
in 1850 as Det Statistiske Bureau and responsible for official
statistics in Denmark "as established by the Act on Statistics
Denmark." The Act itself was not read this pass, so no legislation
entity was created from the name alone.

## Sources

Listed in frontmatter, all three read directly this pass.
