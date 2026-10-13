---
id: EU-DG-EMPL
type: organisation
name: "Directorate-General for Employment, Social Affairs and Inclusion"
alternative_names:
  - "DG EMPL"
description: >
  The department of the European Commission that develops and carries out
  the Commission's policies on employment, social affairs, inclusion, and
  skills and qualifications. In the Atlas it is the Commission's own
  department behind ESCO and Europass.

level: regional
country: null
region: EU

status: active
organisation_role: executive
confidence: high
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-10-13"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-EDUCATION
organisations: []
related_entities:
  - EU
  - EU-COMMISSION
  - EU-ESCO
  - EU-EUROPASS
relationships:
  - type: part-of
    target: EU-COMMISSION
    source: fact
    evidence: "The Commission's own page for the department, read directly (2026-10-13), opens: 'The European Commission's Directorate-General for Employment, Social Affairs and Inclusion (DG EMPL) develops and carries out the Commission's policies on employment, social affairs, inclusion, and skills and qualifications.' It sits in the Commission's list of departments and executive agencies."
    confidence: high
    valid_from: null
    valid_until: null
  - type: part-of
    target: EU
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3, through the Commission, which is part of the Union. Same page, read directly (2026-10-13)."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Employment, Social Affairs and Inclusion (DG EMPL)"
    url: "https://commission.europa.eu/about/departments-and-executive-agencies/employment-social-affairs-and-inclusion_en"
    publisher: "European Commission"
    accessed: "2026-10-13"
---

# Directorate-General for Employment, Social Affairs and Inclusion (DG EMPL)

> **Created 2026-10-13** (roadmap #509, the Directorates-General question,
> `discovery/unresolved.md` rows #15 and #16 now closed). Sourced from the
> Commission's own page for the department, read directly. It is the first
> Directorate-General made an entity on the rule recorded in
> `metadata/ontology.md` §6: an Atlas entity's own read source states that the
> department develops, maintains or provides it. [[EU-EUROSTAT]] was
> already modelled the same way before the question was asked.

## Description

The Commission's page says DG EMPL "develops and carries out the Commission's
policies on employment, social affairs, inclusion, and skills and
qualifications". Among the areas it names are the European Employment
Strategy and the European Social Fund Plus (ESF+, "with an EU budget of
€95.8 billion for the period 2021-2027, managed in partnership with Member
States"), skills and qualifications "including through the Union of Skills
and the European Skills Agenda", and "free movement of workers and
coordination of social security schemes".

## What it carries in the Atlas

- [[EU-ESCO]] is "developed and maintained by the European Commission's DG EMPL"
  (esco.ec.europa.eu's own page, read 2026-09-26): `maintained-by` this entity.
- [[EU-EUROPASS]] is "provided free of charge" by DG EMPL (europass.europa.eu's
  own page, read 2026-09-26): `maintained-by` this entity.

Neither page says more about how the department is organised, and the Atlas
does not record people, so the page's leadership list is not used.

## Relationships

- `part-of` [[EU-COMMISSION]] and `part-of` [[EU]] (anchor edge).
- Inbound `maintained-by` from [[EU-ESCO]] and [[EU-EUROPASS]].

## Sources

Listed in frontmatter, read directly.
