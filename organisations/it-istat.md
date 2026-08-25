---
id: IT-ISTAT
type: organisation
name: Istituto nazionale di statistica
alternative_names:
  - Istat
  - Italian National Institute of Statistics
description: >
  Italy's national statistical institute and the national authority within
  the European Statistical System.

level: national
country: IT
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
  - IT
  - EU-ESS
relationships:
  - type: part-of
    target: IT
    source: fact
    evidence: "Istat is a public body of IT; this anchor edge records national scope under metadata/relationship-types.md §2.3 and asserts no more than that."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: part-of
    target: EU-ESS
    source: fact
    evidence: "Confirmed directly by reading istat.it's own 'L'Istat nella UE e nel mondo' page (2026-08-25): 'L'Istituto contribuisce significativamente al coordinamento e al rafforzamento del Sistema statistico europeo' (the Institute contributes significantly to the coordination and strengthening of the European Statistical System) and, naming the specific body, 'L'Istituto è membro dello European Statistical System Committee (ESSC), l'organo incaricato di orientare il SSE' (the Institute is a member of the ESSC, the body tasked with steering the ESS). This is Istat naming its own ESS membership directly, the stronger evidence tier established for [[PL-GUS]] and [[EE-STATISTIKAAMET]], not the generic composition-rule inference ('the ESS is Eurostat plus the NSIs, Istat is the NSI') most national statistical offices in the Atlas still rest on."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Istituto nazionale di statistica"
    url: "https://www.istat.it/"
    publisher: "Istituto nazionale di statistica (Istat)"
    accessed: "2026-08-25"
  - title: "L'Istat nella UE e nel mondo"
    url: "https://www.istat.it/listituto/relazioni-internazionali/listat-nella-ue-e-nel-mondo/"
    publisher: "Istituto nazionale di statistica (Istat)"
    accessed: "2026-08-25"
  - title: "European Statistical System (ESS)"
    url: "https://ec.europa.eu/eurostat/web/european-statistical-system"
    publisher: "Eurostat"
    accessed: "2026-08-25"
---

# Istituto nazionale di statistica

> **Verified 2026-08-25.** All three cited pages were read directly.
> Istat's own "L'Istat nella UE e nel mondo" page names its [[EU-ESS]]
> membership directly — the strong evidence tier, matching [[PL-GUS]]
> and [[EE-STATISTIKAAMET]] rather than the weaker composition-rule
> tier most national statistical offices in the Atlas still carry.

## Description

Italy's national statistical institute - the **twelfth** on [[EU-ESS]].

## A direct statement, not a composition-rule inference

Istat's own page states plainly: "L'Istituto è membro dello European
Statistical System Committee (ESSC), l'organo incaricato di orientare
il SSE ai fini della produzione di statistiche europee in linea con i
principi contenuti nel Codice delle statistiche europee" (the
Institute is a member of the ESSC, the body tasked with steering the
ESS). Unlike [[LU-STATEC]], re-verified in the previous pass with no
direct ESS statement found on its own pages, Istat names the
membership itself.

## Relationships

- `part-of` [[EU-ESS]].
- `part-of` [[IT]] (anchor edge).

## Sources

Listed in frontmatter, all three read directly this pass.
