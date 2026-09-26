---
id: GB-NATIONAL-DATA-LIBRARY
type: programme
name: National Data Library
alternative_names:
  - NDL
description: >
  UK government programme to provide easier, more ethical and more
  secure access to public data assets for researchers, businesses and
  the public sector, announced as part of the Department for Science,
  Innovation and Technology's (DSIT) 50-point AI Opportunities Action
  Plan at the start of 2025. Funded as a £100m component of DSIT's
  wider £1.9bn technology investment. Designed as "an access
  facilitator rather than a centralised repository," per DSIT's own
  public-attitudes research. An Expert Advisory Group was established
  in September 2025; a "discovery phase" of information-gathering and
  consultation completed by January 2026, alongside five pilot
  ("kickstarter") projects on energy bills, health conditions
  administration, adult social care, SME legal information access, and
  climate/weather data. DSIT stated it would publish more developed
  details in spring 2026. The data.gov.uk portal now brands itself
  under the National Data Library name, though the two are not the
  same thing: the portal is an existing dataset catalogue, while the
  Library is the broader programme DSIT is still designing.

level: national
country: GB
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - GB
  - GB-DATA-GOV-UK
relationships:
  - type: part-of
    target: GB
    source: fact
    evidence: "Closes a gap GB-DATA-GOV-UK's own file had flagged ('a rebrand this entity does not yet record ... worth a dedicated look in a future pass'). Confirmed by reading Computer Weekly's own reporting directly (computerweekly.com, 2026-09-26): the National Data Library was 'trumpeted as part of the government's 50-point AI opportunities action plan' at 'the start of 2025,' is 'a £100m part of an overall £1.9bn investment in DSIT,' and its Expert Advisory Group -- 'co-chaired by Sarah Hodgetts, director for Geospatial and the National Data Library, and Dom Hallas, executive director at Startup Coalition' -- was established in September 2025. The department 'completed its discovery phase by January 2026' involving 'information-gathering from surveys' and consultation with organisations including the Open Data Institute and Wellcome Trust, alongside five named pilot projects. DSIT 'will set out more specific and developed details ... in spring 2026.' GOV.UK's own executive summary of DSIT-commissioned public-attitudes research, also read directly, independently confirms DSIT's ownership and describes the NDL's proposed design as 'an access facilitator rather than a centralised repository.' Anchor edge under metadata/relationship-types.md §2.3, asserting UK national scope via `level: national`."
    confidence: high
    valid_from: null
    valid_until: null
  - type: related-to
    target: GB-DATA-GOV-UK
    source: fact
    evidence: "data.gov.uk's own homepage, read directly (2026-08-22, re-confirmed 2026-09-26), now brands itself 'National Data Library -- The home of UK public data -- data.gov.uk'. No source read states the portal and the programme are formally the same organisational entity -- Computer Weekly's reporting on the programme (discovery phase, Expert Advisory Group, pilot projects) describes DSIT policy work distinct from the existing CKAN-based catalogue's day-to-day operation -- so `related-to` is recorded rather than treating the portal as simply renamed."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "UK government's National Data Library works up steam"
    url: "https://www.computerweekly.com/news/366637775/UK-governments-National-Data-Library-works-up-steam"
    publisher: "Computer Weekly"
    accessed: "2026-09-26"
  - title: "National Data Library Report: executive summary"
    url: "https://www.gov.uk/government/publications/national-data-library-report-research-into-public-attitudes-towards-government-data-sharing/national-data-library-report-executive-summary"
    publisher: "GOV.UK — Department for Science, Innovation and Technology"
    accessed: "2026-09-26"
---

# National Data Library (NDL)

> **Created 2026-09-26**, closing a gap [[GB-DATA-GOV-UK]]'s own file had
> flagged (graph completion, not a numbered `discovery/unresolved.md`
> row): data.gov.uk's rebranding to "National Data Library" on its own
> homepage was noted but "not chased further" in an earlier pass.
> Sourced from Computer Weekly's reporting and DSIT's own public-attitudes
> research summary on GOV.UK, both read directly.

## Description

The National Data Library is a UK government programme to give
"researchers, businesses and the public sector" easier, more ethical and
more secure access to public data assets. Confirmed by reading Computer
Weekly directly: it was "trumpeted as part of the government's 50-point
AI opportunities action plan" at "the start of 2025," and is funded as a
**£100m part of an overall £1.9bn investment in DSIT**.

DSIT's own research summary, read directly, describes the NDL's proposed
design as **"an access facilitator rather than a centralised
repository"** — a distinction that matters for how it relates to
existing portals like [[GB-DATA-GOV-UK]] (below).

## Not the same thing as the data.gov.uk portal

data.gov.uk's own homepage now brands itself "**National Data
Library** — The home of UK public data — data.gov.uk." That is a
genuine rebrand of the *portal's* public face, but no source read states
that the pre-existing CKAN-based dataset catalogue **is** the National
Data Library programme in an organisational sense. Computer Weekly's
reporting describes DSIT policy work — an Expert Advisory Group, a
discovery phase, pilot projects — that reads as broader programme design
work, not day-to-day portal operation. `related-to` is recorded between
the two entities rather than treating the portal as simply renamed,
pending a source that states the relationship more precisely.

## Governance and progress, as of this pass

Confirmed by reading Computer Weekly directly:

- An **Expert Advisory Group** was established in **September 2025**,
  co-chaired by Sarah Hodgetts (DSIT's director for Geospatial and the
  National Data Library) and Dom Hallas (Startup Coalition).
- DSIT completed a **"discovery phase"** by **January 2026**, gathering
  information via surveys and consulting organisations including the
  Open Data Institute and the Wellcome Trust.
- **Five pilot ("kickstarter") projects** are underway, addressing energy
  bills, health conditions administration, adult social care, SME legal
  information access, and climate/weather data.
- DSIT stated it would publish "more specific and developed details" in
  **spring 2026** — not yet due as of this entity's creation date.

## Not modelled

- The **AI Opportunities Action Plan**, the 50-point DSIT/government
  plan the NDL was announced as part of — not itself an Atlas entity.
- The **Expert Advisory Group** and the **five pilot projects**
  individually.
- The **Open Data Institute** and **Wellcome Trust** as consultees —
  named in the source but not established as having an ongoing role.

## Relationships

- `part-of` [[GB]] (anchor edge, `level: national`).
- `related-to` [[GB-DATA-GOV-UK]] — `confidence: medium`, see above.

## Sources

Listed in frontmatter, both read directly.
