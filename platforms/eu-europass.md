---
id: EU-EUROPASS
type: platform
name: Europass
alternative_names:
  - Europass online platform
description: >
  European Commission online platform, provided by the
  Directorate-General for Employment, Social Affairs and Inclusion (DG
  EMPL), free of charge, for managing skills, qualifications and career
  documentation across the EU. Its current legal basis is Decision (EU)
  2018/646 of the European Parliament and of the Council of 18 April
  2018, establishing a common framework for better services for skills
  and qualifications and repealing the original Decision No 2241/2004/EC
  of 15 December 2004. It provides a CV editor (31 languages), cover
  letter editor, Diploma and Certificate Supplements, Europass Mobility
  documentation, digital skills testing, job/learning-opportunity
  matching, and European Digital Credentials storage and sharing.

level: regional
country: null
region: EU

status: active
confidence: high
coverage: low
verification: primary-source

start_date: 2004-12-15
end_date: null
last_verified: "2026-09-26"
previous_version: null
successor: null

domains:
  - DOMAIN-EDUCATION
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-SKILLS-DATA-SPACE
  - EU-ESCO
relationships:
  - type: part-of
    target: EU
    source: fact
    evidence: "Closes a gap EU-SKILLS-DATA-SPACE's own file had flagged (not a numbered discovery/unresolved.md row: Europass was 'previously presumed' to be existing EU skills-data machinery, then checked against EU-DS4SKILLS's sources on 2026-09-05 and found unmentioned). Confirmed by reading europass.europa.eu's own 'About Europass' page directly (2026-09-26): the European Commission, via DG EMPL, provides it free of charge, offering a CV editor, cover letter editor, Diploma/Certificate Supplements, Mobility documentation, digital skills testing, opportunity matching and European Digital Credentials storage. legislation.gov.uk's own mirror of Decision (EU) 2018/646, also read directly (eur-lex.europa.eu returned empty content for this CELEX number on every attempt), confirms the Decision's date (18 April 2018), its title ('a common framework for the provision of better services for skills and qualifications (Europass)'), and that it repeals the original Decision No 2241/2004/EC of 15 December 2004 -- the date recorded as `start_date`, since that is when the Europass framework itself began, not when the current legal basis was adopted. Anchor edge under metadata/relationship-types.md §2.3, asserting EU-wide scope via `level: regional`, `region: EU`."
    confidence: high
    valid_from: "2004-12-15"
    valid_until: null
  - type: related-to
    target: EU-SKILLS-DATA-SPACE
    source: interpretation
    evidence: "EU-SKILLS-DATA-SPACE's own file found Europass unmentioned when checked against EU-DS4SKILLS's sources (2026-09-05). Re-checked this pass (2026-09-26): europass.europa.eu's own page does not mention the skills data space either. Recorded as `source: interpretation`, `confidence: low` -- both concern EU skills/career data, but no source states a governance or structural link, matching the same discipline already applied to EU-ESCO earlier this session."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "About Europass"
    url: "https://europass.europa.eu/en/about-europass"
    publisher: "European Commission — DG Employment, Social Affairs and Inclusion"
    accessed: "2026-09-26"
  - title: "Decision (EU) 2018/646"
    url: "https://www.legislation.gov.uk/eudn/2018/646/contents"
    publisher: "legislation.gov.uk (mirroring EUR-Lex; eur-lex.europa.eu returned empty content for CELEX:32018D0646)"
    accessed: "2026-09-26"
---

# Europass

> **Created 2026-09-26**, closing a gap [[EU-SKILLS-DATA-SPACE]]'s own
> file had flagged (graph completion, not a numbered
> `discovery/unresolved.md` row). Sourced from Europass's own official
> page and a legislation.gov.uk mirror of its governing Decision, both
> read directly.

## Description

Europass is a European Commission online platform, provided **free of
charge** by the **Directorate-General for Employment, Social Affairs
and Inclusion (DG EMPL)**, for managing skills, qualifications and
career documentation. Confirmed directly on its own "About Europass"
page: it provides a **CV editor** (31 languages), a **cover letter
editor**, **Diploma and Certificate Supplements**, **Europass Mobility**
documentation, **digital skills testing**, job/learning-opportunity
matching, and storage/sharing of **European Digital Credentials**.

## A framework re-founded once

Europass's current legal basis is **Decision (EU) 2018/646** of the
European Parliament and of the Council, **adopted 18 April 2018**,
confirmed by reading a legislation.gov.uk mirror of the Decision
directly (`eur-lex.europa.eu` returned empty content for this CELEX
number on every attempt, a known issue for some EU instruments). It
establishes "a common framework for the provision of better services for
skills and qualifications (Europass)" and **repeals the original
Decision No 2241/2004/EC** of **15 December 2004**, which first created
the Europass framework. `start_date` records the original 2004 framework,
since that is when Europass itself began, not the 2018 re-founding.

## Checked against EU-SKILLS-DATA-SPACE — still no stated link

Matching [[EU-ESCO]]'s own finding earlier this session: neither
Europass's own page nor its governing Decision mentions
[[EU-SKILLS-DATA-SPACE]]. The edge is recorded at `source:
interpretation`, `confidence: low` rather than asserted as fact.

## Not modelled

- The **European Digital Credentials** infrastructure Europass stores
  and shares — a distinct technical system, not independently
  researched this pass.
- The **European Skills Agenda**, the third item named alongside ESCO
  and Europass on [[EU-SKILLS-DATA-SPACE]]'s file — not independently
  researched this pass.

## Relationships

- `part-of` [[EU]] (anchor edge, `level: regional`, `region: EU`).
- `related-to` [[EU-SKILLS-DATA-SPACE]] — `confidence: low`, no direct
  source connects them.

## Sources

Listed in frontmatter, both read directly.
