---
id: PT-IPQ
type: organisation
name: Instituto Português da Qualidade
alternative_names:
  - IPQ
  - Portuguese Institute for Quality
description: >
  Portugal's national standardization body, established in 1986, which
  manages and develops the Portuguese Quality System and coordinates with the
  European and international standardization organisations. It is Portugal's
  member of CEN and its national committee in CENELEC, and an ISO member
  body.

level: national
country: PT
region: EU

status: active
confidence: medium
coverage: medium
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
  - PT
  - EU-CEN
  - EU-CENELEC
  - INTL-ISO
relationships:
  - type: part-of
    target: PT
    source: fact
    evidence: "Confirmed by reading ipq.pt's own homepage directly (2026-08-26): 'O Instituto Português da Qualidade é o Organismo Nacional de Normalização e a Instituição Nacional de Metrologia' (IPQ is the National Standardization Body and the National Metrology Institution) — a second mandate, metrology, this entity did not previously carry. Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-CEN
    source: fact
    evidence: "Confirmed by reading standards.cencenelec.eu's own CEN membership list directly (2026-08-26): the entry reads 'IPQ | Portugal | Instituto Português da Qualidade | www.ipq.pt', naming IPQ directly as Portugal's CEN national member."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-CENELEC
    source: fact
    evidence: "CEN and CENELEC share the same national-member structure (cencenelec.eu's own 'European Standards' page, read directly, describes both bodies' National Members as the National Standardization Organizations of the same set of countries); standards.cencenelec.eu's member list, also read directly, names IPQ for Portugal's CEN membership. No page read lists CENELEC's members separately from CEN's, so this edge is carried at the same evidentiary basis as the CEN edge rather than an independently named CENELEC entry."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: INTL-ISO
    source: interpretation
    evidence: "iso.org's own member page for IPQ (iso.org/member/2054) is genuinely bot-walled (403) even with an honest, identifying User-Agent, so this pass could not read ISO's own listing directly. The edge is retained at reduced confidence on the strength of the previously compiled search-index description (ISO's member directory naming IPQ for Portugal) rather than a page read this pass."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Instituto Português da Qualidade"
    url: "https://www.ipq.pt/"
    publisher: "Instituto Português da Qualidade (IPQ)"
    accessed: "2026-08-26"
  - title: "European Standards"
    url: "https://www.cencenelec.eu/european-standardization/european-standards/"
    publisher: "CEN-CENELEC"
    accessed: "2026-08-26"
  - title: "CEN Community — List of members"
    url: "https://standards.cencenelec.eu/ords/f?p=CEN:5"
    publisher: "CEN-CENELEC"
    accessed: "2026-08-26"
  - title: "ISO — IPQ, Instituto Português da Qualidade (currently bot-walled)"
    url: "https://www.iso.org/member/2054.html"
    publisher: "International Organization for Standardization (ISO)"
---

# Instituto Português da Qualidade

> **Re-verified 2026-08-26.** Three of four cited pages were read
> directly — standards.cencenelec.eu's own CEN membership list names IPQ
> for Portugal by name, and ipq.pt's own homepage reveals a second
> mandate (metrology) this entity did not previously carry. `iso.org`
> remains genuinely bot-walled (403) even with an honest User-Agent, so
> the `INTL-ISO` edge is downgraded to `interpretation`/`low` rather than
> dropped.

## Description

IPQ is Portugal's national standardization body **and its national
metrology institution**, established in **1986**, managing and
developing the **Portuguese Quality System (SPQ)**. The metrology
mandate, confirmed by reading ipq.pt's own homepage directly, was not
previously carried by this entity.

## The CEN membership, now directly named

Earlier passes inferred CEN/CENELEC membership from the general rule
that all EU member states' standards bodies belong; this pass instead
read standards.cencenelec.eu's own member list directly, which names
IPQ for Portugal by row: "IPQ | Portugal | Instituto Português da
Qualidade | www.ipq.pt" — a source that states membership rather than a
rule that implies it, the same upgrade [[PL-PKN]] and its CEN-group
siblings have not yet had.

## The ISO edge, downgraded rather than dropped

`iso.org`'s own member page for IPQ is genuinely bot-walled (403), even
with an honest, identifying User-Agent — the same block found on
`eur-lex.europa.eu`, `www.coe.int` and `unece.org` elsewhere in the
Atlas. Rather than repeat the previously compiled, unread claim at
`confidence: medium`, it is retained at `source: interpretation`,
`confidence: low`, honestly reflecting that ISO's own listing was not
read this pass either.

## Relationships

- `part-of` [[PT]] — anchor edge, confirmed this pass.
- `participates-in` [[EU-CEN]] — confirmed by name this pass.
- `participates-in` [[EU-CENELEC]] — same evidentiary basis as CEN.
- `participates-in` [[INTL-ISO]] — `confidence: low`,
  `source: interpretation`; `iso.org` remains bot-walled.

## Sources

Listed in frontmatter. Three of four read directly this pass; `iso.org`
remains genuinely bot-walled.
