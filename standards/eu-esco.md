---
id: EU-ESCO
type: standard
name: European Skills, Competences, Qualifications and Occupations
alternative_names:
  - ESCO
description: >
  European multilingual classification of skills, competences,
  qualifications and occupations, developed and maintained by the
  European Commission's Directorate-General for Employment, Social
  Affairs and Inclusion (DG EMPL). Its first complete version launched
  on 28 July 2017. It provides a structured, machine-readable dictionary
  of occupations and skills — as of this pass, 3,039 occupations and
  13,939 linked skills, translated into 28 languages — used by online
  platforms to match jobseekers to positions and recommend training,
  supporting a more integrated EU labour market. Freely available
  through an online portal, with downloadable data and API access.

level: regional
country: null
region: EU

status: active
confidence: high
coverage: low
verification: primary-source

start_date: 2017-07-28
end_date: null
last_verified: "2026-09-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-SKILLS-DATA-SPACE
relationships:
  - type: part-of
    target: EU
    source: fact
    evidence: "Confirmed by reading esco.ec.europa.eu's own 'What is ESCO' page directly (2026-09-26): ESCO is 'the European multilingual classification of Skills, Competences and Occupations,' developed and maintained by the European Commission's DG EMPL, with its first complete version launched 28 July 2017. It covers 3,039 occupations and 13,939 linked skills across 28 languages. Anchor edge under metadata/relationship-types.md §2.3, asserting EU-wide scope via `level: regional`, `region: EU` -- DG EMPL itself is not modelled as a separate entity, matching the Atlas's convention of not modelling Directorates-General in their own right (discovery/unresolved.md ontology item #16)."
    confidence: high
    valid_from: "2017-07-28"
    valid_until: null
  - type: related-to
    target: EU-SKILLS-DATA-SPACE
    source: interpretation
    evidence: "EU-SKILLS-DATA-SPACE's own file, checking directly against EU-DS4SKILLS's sources (2026-09-05), found ESCO 'not mentioned' and 'not confirmed connected to this data space by any source read.' Re-checked this pass (2026-09-26): esco.ec.europa.eu's own page does not mention the skills data space either. Recorded as `source: interpretation`, `confidence: low` -- both concern EU skills data, but no source states a governance or structural link, matching the same discipline already applied elsewhere this session."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "What is ESCO"
    url: "https://esco.ec.europa.eu/en/about-esco/what-esco"
    publisher: "European Commission — DG Employment, Social Affairs and Inclusion"
    accessed: "2026-09-26"
---

# ESCO — European Skills, Competences, Qualifications and Occupations

> **Created 2026-09-26**, closing a gap [[EU-SKILLS-DATA-SPACE]]'s own
> file had flagged (graph completion, not a numbered
> `discovery/unresolved.md` row: ESCO was "previously presumed" to be
> existing EU skills-data machinery the data space builds on, then found
> unconnected on 2026-09-05 and left unmodelled). Sourced from the
> Commission's own ESCO portal, read directly.

## Description

ESCO is the European Commission's **multilingual classification of
skills, competences, qualifications and occupations** — a structured,
machine-readable dictionary, confirmed directly on its own official
page: **3,039 occupations** and **13,939 linked skills**, translated
into **28 languages** (all EU official languages plus Icelandic,
Norwegian, Ukrainian and Arabic). It is developed and maintained by the
Commission's **Directorate-General for Employment, Social Affairs and
Inclusion (DG EMPL)**, with its first complete version launched on
**28 July 2017**.

Its stated purpose: enabling online platforms to match jobseekers to
positions by skill, and to recommend training — supporting "a more
integrated and efficient labour market" across the EU. It is freely
available through an online portal, with downloadable data and API
access for developers.

## Checked against EU-SKILLS-DATA-SPACE — still no stated link

[[EU-SKILLS-DATA-SPACE]]'s own file already checked ESCO against
[[EU-DS4SKILLS]]'s sources and found it unmentioned. Re-checked this
pass against ESCO's own page directly: it likewise does not mention the
skills data space. Both concern EU skills data, but no source states a
governance or structural link between them, so the edge is recorded at
`source: interpretation`, `confidence: low` rather than asserted as
fact.

## Not modelled

- **DG EMPL** as a separate organisation entity — the Atlas does not
  model Directorates-General in their own right (a still-open ontology
  question, `discovery/unresolved.md` item #16).
- ~~**Europass** and the **European Skills Agenda**~~ — **researched
  later the same day**: now [[EU-EUROPASS]] and [[EU-SKILLS-AGENDA]].
  [[EU-SKILLS-DATA-SPACE]]'s own file records all three of its
  "previously presumed" connections as now researched.

## Relationships

- `part-of` [[EU]] (anchor edge, `level: regional`, `region: EU`).
- `related-to` [[EU-SKILLS-DATA-SPACE]] — `confidence: low`, no direct
  source connects them.

## Sources

Listed in frontmatter, read directly.
