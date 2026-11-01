---
id: PL-E-ZDROWIE-P1
type: platform
name: "e-zdrowie (P1)"
alternative_names:
  - "P1"
  - "system e-zdrowie"
  - "Platforma P1"
description: >
  The flagship system of Poland's Centrum e-Zdrowia, which the Centre calls the basis of the digital ecosystem of medical services. Known only
  from the Centre's home page; its functions, legal basis and launch were not read.

level: national
country: PL
region: null

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-11-01"
previous_version: null
successor: null

domains:
  - DOMAIN-HEALTH
  - DOMAIN-DIGITAL-INFRASTRUCTURE
organisations:
  - PL-CEZ

related_entities:
  - PL
  - PL-CEZ
relationships:
  - type: owned-by
    target: PL-CEZ
    source: fact
    evidence: "Centrum e-Zdrowia's home page (read directly 2026-11-01): 'Flagowym produktem Centrum e-Zdrowia jest system e-zdrowie (P1)'."
    confidence: high
    valid_from: null
    valid_until: null
  - type: applies-in
    target: PL
    source: fact
    evidence: "The page describes P1 as the basis of the digital ecosystem of medical services in Poland, with access for patients, medical staff and public administration; the scope is inferred from the Centre's national role, so medium confidence."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Centrum e-Zdrowia — home page"
    url: "https://www.cez.gov.pl/en"
    publisher: "Centrum e-Zdrowia"
    accessed: "2026-11-01"
---

# e-zdrowie (P1)

> **Created 2026-11-01** (roadmap #460). Known **only** from one sentence on the Centre's home page; its legal basis (the Polish act on the healthcare information system), its launch date and its modules (e-prescription, e-referral and others) were not read, so none is recorded.

## What the page says

"Flagowym produktem Centrum e-Zdrowia jest system e-zdrowie (P1), który stanowi podstawę cyfrowego ekosystemu usług medycznych." The Centre's products "wspierają procesy leczenia i profilaktyki oraz wspomagają administrację państwową w podejmowaniu decyzji inwestycyjnych w zakresie ochrony zdrowia w Polsce" (support treatment and prevention and help the state administration in investment decisions on health protection).

## Relationships

`owned-by` [[PL-CEZ]]; `applies-in` Poland (medium).

## Sources

Listed in frontmatter, read directly.
