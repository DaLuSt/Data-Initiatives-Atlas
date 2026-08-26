---
id: ES-UNE
type: organisation
name: Asociación Española de Normalización
alternative_names:
  - UNE
  - AENOR
  - Spanish Association for Standardization
description: >
  The national standardization body of Spain, and therefore its national
  member of CEN and its national committee in CENELEC. The national bodies
  operate the technical groups that draw up European Standards, coordinated
  by the CEN-CENELEC Management Centre in Brussels.

level: national
country: ES
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-CEN
  - EU-CENELEC
relationships:
  - type: participates-in
    target: EU-CEN
    source: fact
    evidence: "Confirmed by reading standards.cencenelec.eu's own current member list directly (2026-08-26): 'UNE | Spain | Asociación Española de Normalización | www.une.org', naming UNE directly as Spain's CEN national member. cencenelec.eu's own 'European Standards' page, also read directly, describes National Members as operating the technical groups that draw up standards, coordinated by the Brussels Management Centre. `une.org` itself is genuinely bot-walled (403) even with an honest User-Agent."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-CENELEC
    source: fact
    evidence: "CEN and CENELEC share the same national-member structure (cencenelec.eu's own 'European Standards' page, read directly, describes both bodies' National Members as the same set of countries' bodies); standards.cencenelec.eu's member list, also read directly, names UNE for Spain's CEN membership. No page read lists CENELEC's members separately from CEN's, so this edge is carried at the same evidentiary basis as the CEN edge."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "European Standards"
    url: "https://www.cencenelec.eu/european-standardization/european-standards/"
    publisher: "CEN-CENELEC"
    accessed: "2026-08-26"
  - title: "CEN Community — List of members"
    url: "https://standards.cencenelec.eu/ords/f?p=CEN:5"
    publisher: "CEN-CENELEC"
    accessed: "2026-08-26"
  - title: "UNE — Asociación Española de Normalización (currently bot-walled)"
    url: "https://www.une.org/"
    publisher: "UNE"
---

# Asociación Española de Normalización (UNE)

> **Verified 2026-08-26.** Two of three cited pages were read directly;
> `une.org` remains genuinely bot-walled (403) even with an honest
> User-Agent. standards.cencenelec.eu's own member list names UNE for
> Spain directly.

## Description

UNE is the national standardization body of Spain.

## Spain's standards body, and a naming change the Atlas should not get wrong

The Spanish standardization body is **UNE** (Asociación Española de
Normalización). **AENOR** is recorded here as an alternative name because the
two are routinely conflated and because `discovery/research-queue.md` queued
this entity as "AENOR / UNE".

They are not simply two names for one thing: the standardization and
certification functions were separated, with UNE retaining standardization
and AENOR continuing as a certification business. **The Atlas asserts nothing
about that split**, because no source read describes it — the alternative
name is there so a search for either resolves here, and the distinction is
logged in `discovery/unresolved.md`.

`UNE` is also the prefix of Spanish standards, which is why the acronym
appears in standard numbers as well as in the body's name.

**No [[INTL-ISO]] edge is asserted**, for the reason given on [[BE-NBN]].

## Not modelled

- Any **standard** UNE maintains. That is now true of **seven** national
  standards bodies in the Atlas — [[DE-DIN]], [[NL-NEN]], [[GB-BSI]],
  [[IE-NSAI]] and the three others added with this one — none of which
  maintains a single document the Atlas holds. The exception is
  [[INTL-IDS-RAM]], which reaches [[DE-DIN]] from the other direction.
- UNE's **relationship to [[EU-ETSI]]**, which only [[GB-BSI]] carries.

## Relationships

- `participates-in` [[EU-CEN]] and [[EU-CENELEC]].

## Sources

Listed in frontmatter, two of three read directly this pass; `une.org`
remains genuinely bot-walled.
