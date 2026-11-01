---
id: PL-CEZ
type: organisation
name: "Centrum e-Zdrowia"
alternative_names:
  - "CeZ"
  - "Centre for e-Health"
  - "Centrum e-Zdrowia (Poland)"
  - "CSIRT Centrum e-Zdrowia"
description: >
  Poland's centre for e-health: it runs the e-zdrowie (P1) system, which it calls the basis of the digital ecosystem of medical services,
  together with medical registers, business analytics and cybersecurity services (including a CSIRT, which detected nearly 1,400 incidents
  up to September 2026). Known only from its own home page, in Polish.

level: national
country: PL
region: null

status: active
organisation_role: executive
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
organisations: []
related_entities:
  - PL
  - PL-E-ZDROWIE-P1
relationships:
  - type: part-of
    target: PL
    source: fact
    evidence: "Centrum e-Zdrowia's own home page (read directly 2026-11-01) describes it as the provider of the national e-health system, 'Flagowym produktem Centrum e-Zdrowia jest system e-zdrowie (P1)', serving 'pacjentów, pracowników medycznych i administracji publicznej'. Its legal status (it is a state unit under the Ministry of Health in the sources the Atlas knows of) was not read on the pages used, so this edge is medium confidence."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: related-to
    target: PL-E-ZDROWIE-P1
    source: fact
    evidence: "The same page: 'Flagowym produktem Centrum e-Zdrowia jest system e-zdrowie (P1), który stanowi podstawę cyfrowego ekosystemu usług medycznych.'"
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Centrum e-Zdrowia — home page"
    url: "https://www.cez.gov.pl/en"
    publisher: "Centrum e-Zdrowia"
    accessed: "2026-11-01"
---

# Centrum e-Zdrowia (CeZ)

> **Created 2026-11-01** (roadmap #460, health data). Known **only** from the Centre's home page, read directly (in Polish; the English address shows the Polish text). Its legal form, founding date and supervising ministry were not read, so none is recorded and the `part-of` edge to Poland is medium confidence.

## What the page says

"Flagowym produktem Centrum e-Zdrowia jest system e-zdrowie (P1), który stanowi podstawę cyfrowego ekosystemu usług medycznych. W naszym portfolio znajdują się również systemy IT, rejestry medyczne, analizy biznesowe oraz usługi z zakresu cyberbezpieczeństwa." (The flagship product is the e-zdrowie (P1) system, the basis of the digital ecosystem of medical services; the portfolio also holds IT systems, medical registers, business analytics and cybersecurity services.) Their purpose: "bezpiecznego dostępu do informacji medycznej dla pacjentów, pracowników medycznych i administracji publicznej". News items: "Tylko do września 2026 roku wykryto blisko 1400 incydentów. Rośnie skuteczność CSIRT Centrum e-Zdrowia" (nearly 1,400 incidents detected up to September 2026), the Internetowe Konto Pacjenta (patient online account) and its mojeIKP app, and the ninth survey of the informatisation of healthcare providers.

## Relationships

`part-of` Poland (medium); `related-to` [[PL-E-ZDROWIE-P1]].

## Sources

Listed in frontmatter, read directly.
