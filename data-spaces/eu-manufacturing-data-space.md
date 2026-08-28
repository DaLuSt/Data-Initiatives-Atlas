---
id: EU-MANUFACTURING-DATA-SPACE
type: data-space
name: Common European manufacturing data space
alternative_names:
  - Manufacturing data space
  - Industrial data space
  - Data space for manufacturing
description: >
  One of the fourteen common European data spaces, covering the
  manufacturing and industrial sector. Its deployment is supported by the
  Digital Europe Programme through two Deployment Actions projects,
  UNDERPIN and SM4RTENANCE, which advance data-driven solutions in
  manufacturing and shape the governance and business frameworks the data
  space will run on.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - EU-COMMON-DATA-SPACES
relationships:
  - type: part-of
    target: EU-COMMON-DATA-SPACES
    source: fact
    evidence: "Confirmed by reading digital-strategy.ec.europa.eu's own 'Common European data spaces' overview directly (2026-08-28): manufacturing (as 'Data Space 4.0, SM4RTENANCE, and UNDERPIN') is named among the fourteen. A PMC (PubMed Central) mirror of the ScienceDirect article on the UNDERPIN and SM4RTENANCE frameworks, read directly, confirms both projects were funded under the DIGITAL-2022-CLOUD-AI-03-DS-MANUF call, that UNDERPIN (started late 2023, 11 partners from 5 EU countries) focuses on semantic interoperability via knowledge graphs with pilots in oil refineries and wind farms, and that SM4RTENANCE (started October 2023, 44 partners from 11 EU countries) runs nine implementation pilots across textiles, e-mobility, steel and automotive."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Second staff working document on data spaces — SWD(2024) 21 final"
    url: "https://digital-strategy.ec.europa.eu/en/library/second-staff-working-document-data-spaces"
    publisher: "European Commission"
    accessed: "2026-08-28"
  - title: "Common European data spaces"
    url: "https://digital-strategy.ec.europa.eu/en/policies/data-spaces"
    publisher: "European Commission — Shaping Europe's digital future"
    accessed: "2026-08-28"
  - title: "Deploying the common European manufacturing data space: The UNDERPIN and SM4RTENANCE frameworks' perspective (PMC mirror)"
    url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC13049574/"
    publisher: "PubMed Central (National Library of Medicine)"
    accessed: "2026-08-28"
  - title: "Data Spaces for Manufacturing in the Digital Europe Programme"
    url: "https://hadea.ec.europa.eu/document/download/15920bba-1e1f-4480-a543-d224ef177d62_en?filename=DEP+Call+6+-+Data+Space+for+Manufacturing+deployment_0.pdf"
    publisher: "European Health and Digital Executive Agency (HaDEA)"
  - title: "Deploying the common European manufacturing data space: the UNDERPIN and SM4RTENANCE frameworks' perspective"
    url: "https://www.sciencedirect.com/science/article/pii/S235234092600226X"
    publisher: "ScienceDirect (Elsevier)"
---

# Common European manufacturing data space

> **Re-verified 2026-08-28.** The stale SWD URL was corrected to the right
> Commission document, the Commission's main data-spaces page was read
> directly, and — since ScienceDirect itself returned HTTP 403 — a PMC
> (PubMed Central) mirror of the same UNDERPIN/SM4RTENANCE article was
> found and read directly instead, confirming and substantially extending
> the two projects' description. `verification` moves from `search-only`
> to `primary-source`.

## Description

One of the fourteen common European data spaces, covering the manufacturing and industrial sector.
Its deployment is supported by the Digital Europe Programme through two Deployment Actions projects, UNDERPIN and SM4RTENANCE, which advance data-driven solutions in manufacturing and shape the governance and business frameworks the data space will run on.

## The sector with the most national activity beneath it

Manufacturing is where the Atlas already holds the most sectoral machinery
below the EU level. [[DE-CATENA-X]] is an operating automotive data space
`based-on` [[EU-GAIA-X]] and following the IDS reference architecture, and
[[DE-MANUFACTURING-X]] extends that pattern across German industry.

**No relationship is asserted between this entity and either of them.** That
they occupy the same sector is not evidence that one is part of, implements
or derives from the other, and no source read states a connection. The
sectoral adjacency is discoverable through [[EU-COMMON-DATA-SPACES]] and the
country index, and the question is logged in `discovery/unresolved.md`.

## Deployment, not regulation

Two Deployment Actions projects, funded under the DIGITAL-2022-CLOUD-AI-03-DS-MANUF
call of the Digital Europe Programme, are advancing data-driven solutions
for manufacturing. Confirmed by reading a PMC mirror of the ScienceDirect
article on both projects directly:

- **UNDERPIN** — started late 2023, runs 24 months, 11 partners from 5 EU
  countries. Emphasises semantic interoperability through knowledge graphs
  and ontologies, validated via two pilots (oil refinery predictive
  maintenance; wind farm component health monitoring), and develops
  Digital Product Passports (DPPs).
- **SM4RTENANCE** — started October 2023, runs 36 months, 44 partners from
  11 EU countries. Builds federated data spaces for cross-sector
  collaboration, with nine implementation pilots across textiles,
  e-mobility, steel and automotive.

Both build on the earlier BOOST 4.0 and Data Space 4.0 projects. Neither is
modelled as its own Atlas entity — they remain projects, not the data space
itself, consistent with how this Atlas treats deployment actions elsewhere
in this batch (e.g. INSIEME under [[EU-CEEDS]]).

## Not modelled

- **UNDERPIN** and **SM4RTENANCE** as their own entities (described above).
- The **Data Act**'s industrial-data provisions, which are the legislative
  backdrop to this sector. [[EU-DATA-ACT]] is an Atlas entity and carries no
  edge to this one, because no source read connects them.

## Sources

Listed in frontmatter, three of five read directly this pass. The HaDEA
call PDF was attempted and returned unreadable binary/stream content; the
ScienceDirect article itself returned HTTP 403, but its PMC mirror was
found and read directly instead.
