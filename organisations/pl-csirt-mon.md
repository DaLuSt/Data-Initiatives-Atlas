---
id: PL-CSIRT-MON
type: organisation
name: CSIRT MON
alternative_names:
  - Zespół Reagowania na Incydenty Bezpieczeństwa Komputerowego MON
  - Computer Security Incident Response Team of the Ministry of National Defence
description: >
  One of Poland's three national-level Computer Security Incident
  Response Teams established under the Act on the National Cybersecurity
  System, operated by the Ministry of National Defence. It coordinates
  incident handling for entities subordinate to or supervised by the
  Minister of National Defence, critical-infrastructure entities in its
  remit, and defence-significant enterprises.

level: national
country: PL
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-06"
previous_version: null
successor: null

domains:
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - PL-KSC
  - PL-ABW
  - PL-NASK
relationships:
  - type: implements
    target: PL-KSC
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP. Confirmed by reading gov.pl's own page directly (2026-09-06, Ministry of Digital Affairs): 'Ustawa o krajowym systemie cyberbezpieczeństwa ustanowiła trzy Zespoły Reagowania na Incydenty' (the national cybersecurity system act established three incident response teams), naming CSIRT MON as one of the three alongside CSIRT GOV (PL-ABW) and CSIRT NASK (PL-NASK). `csirt-mon.wp.mil.pl`, the team's own site, is genuinely CAPTCHA-walled in this environment on every attempt, consistent with the entire mil.pl domain."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: part-of
    target: PL
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. Confirmed by reading gov.pl's own page directly (2026-09-06): 'CSIRT MON – prowadzony przez Ministerstwo Obrony Narodowej' (CSIRT MON is operated by the Ministry of National Defence) — a Polish federal ministry not itself an Atlas entity, so the anchor targets the country."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Zespół Reagowania na Incydenty Bezpieczeństwa Komputerowego (CSIRT)"
    url: "https://www.gov.pl/web/cyfryzacja/zespol-reagowania-na-incydenty-bezpieczenstwa-komputerowego-csirt"
    publisher: "Ministerstwo Cyfryzacji (gov.pl)"
    accessed: "2026-09-06"
---

# CSIRT MON

> **Created 2026-09-06**, closing a gap this Atlas flagged twice: Poland's
> third national CSIRT, alongside [[PL-ABW]]'s CSIRT GOV and
> [[PL-NASK]]'s CSIRT NASK, was named but never modelled because its
> parent, the Ministry of National Defence, is not an Atlas entity. The
> team's own site (`csirt-mon.wp.mil.pl`) is genuinely CAPTCHA-walled in
> this environment — confirmed on the mil.pl domain generally, not just
> this one page — so gov.pl's own page, the Ministry of Digital Affairs'
> account of Poland's national CSIRT landscape, was read directly
> instead.

## Description

Confirmed by reading gov.pl's own page directly: "Ustawa o krajowym
systemie cyberbezpieczeństwa ustanowiła trzy Zespoły Reagowania na
Incydenty" — the National Cybersecurity System Act, [[PL-KSC]], established
three incident-response teams. CSIRT MON is "prowadzony przez
Ministerstwo Obrony Narodowej" — operated by the Ministry of National
Defence — the third, alongside [[PL-ABW]]'s CSIRT GOV and [[PL-NASK]]'s
CSIRT NASK.

A WebSearch cross-check of the team's own (CAPTCHA-walled) pages
describes its remit as coordinating incidents from entities subordinate
to or supervised by the Minister of National Defence, critical
infrastructure in its sector, and defence-significant enterprises, with a
footer identifying its parent command as the **Dowództwo Komponentu
Wojsk Obrony Cyberprzestrzeni** (Cyber Defence Component Command) — not
independently confirmed by a directly-read page this pass.

## The third of three, now all modelled

[[PL-KSC]]'s three CSIRTs are now all Atlas entities: [[PL-ABW]]
`implements` it for CSIRT GOV, [[PL-NASK]] `implements` it for CSIRT
NASK, and this entity `implements` it for CSIRT MON — completing a
cross-reference [[PL-KSC]]'s own "Not modelled" section had flagged.

## Not modelled

- The **Dowództwo Komponentu Wojsk Obrony Cyberprzestrzeni**, CSIRT MON's
  parent military command per secondary sourcing — not independently
  confirmed by a directly-read primary page this pass.
- The **Ministry of National Defence** itself, which is not an Atlas
  entity.

## Relationships

- `implements` [[PL-KSC]].
- `part-of` [[PL]] — a scope anchor, since its parent ministry is not
  modelled.

## Sources

Listed in frontmatter, read directly 2026-09-06.
