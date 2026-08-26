---
id: FR-AFNOR
type: organisation
name: Association française de normalisation
alternative_names:
  - AFNOR
  - French standards body
description: >
  The national standardization body of France, and therefore its national
  member of CEN and its national committee in CENELEC. The national bodies
  operate the technical groups that draw up European Standards, coordinated
  by the CEN-CENELEC Management Centre in Brussels.

level: national
country: FR
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
    evidence: "Confirmed by reading standards.cencenelec.eu's own CEN Community member list directly (2026-08-26): it lists 'AFNOR France Association Française de Normalisation www.afnor.org' among the national standardization bodies. cencenelec.eu's own 'European Standards' page, also read, describes the national-body/CEN-CENELEC Management Centre structure but does not name France or AFNOR specifically."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-CENELEC
    source: fact
    evidence: "The same standards.cencenelec.eu member list, read directly (2026-08-26), names AFNOR as France's national body under the shared CEN/CENELEC membership structure; the list fetched this pass is presented as CEN's own ('p=CEN:5' in the URL), so CENELEC membership specifically still rests on the general pattern that CEN national members are also CENELEC national committees, not on a CENELEC-specific list read this pass."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "CEN Community — List of members"
    url: "https://standards.cencenelec.eu/ords/f?p=CEN:5"
    publisher: "CEN-CENELEC"
    accessed: "2026-08-26"
  - title: "AFNOR — Association française de normalisation"
    url: "https://www.afnor.org/"
    publisher: "AFNOR"
    accessed: "2026-08-26"
  - title: "European Standards"
    url: "https://www.cencenelec.eu/european-standardization/european-standards/"
    publisher: "CEN-CENELEC"
    accessed: "2026-08-26"
---

# Association française de normalisation (AFNOR)

> **Verified 2026-08-26.** All three cited pages were read directly.
> CEN's own member list names AFNOR directly; the generic CEN-CENELEC
> explainer page does not mention France or AFNOR by name. ⚠
> `coverage: low`.

## Description

Confirmed by reading standards.cencenelec.eu's own member list
directly (2026-08-26): AFNOR is the national standardization body of
France.

## France's standards body

AFNOR is France's national standardization body and therefore its CEN member
and CENELEC national committee.

It joins [[FR-INSEE]], created in the same batch, in filling out the French
institutional layer: France now has a statistical office and a standards
body, both of which every other large Atlas country already had.

**No [[INTL-ISO]] edge is asserted**, for the reason given on [[BE-NBN]].

## Not modelled

- Any **standard** AFNOR maintains. That is now true of **seven** national
  standards bodies in the Atlas — [[DE-DIN]], [[NL-NEN]], [[GB-BSI]],
  [[IE-NSAI]] and the three others added with this one — none of which
  maintains a single document the Atlas holds. The exception is
  [[INTL-IDS-RAM]], which reaches [[DE-DIN]] from the other direction.
- AFNOR's **relationship to [[EU-ETSI]]**, which only [[GB-BSI]] carries.

## Relationships

- `participates-in` [[EU-CEN]] and [[EU-CENELEC]].

## Sources

Listed in frontmatter, all three read directly this pass.
