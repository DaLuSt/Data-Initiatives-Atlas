---
id: NL-DANS
type: organisation
name: Data Archiving and Networked Services
alternative_names:
  - DANS
description: >
  Dutch national centre of expertise and repository for research data,
  helping researchers make their data accessible for reuse and enabling
  verification and reproducibility of published research. Founded in
  2005 as a joint institute of KNAW (the Royal Netherlands Academy of
  Arts and Sciences) and NWO (the Dutch Research Council), consolidating
  several earlier institutions including the Steinmetz Archive (1964),
  the Dutch Historical Data Archive (1989) and the Electronic Depot of
  Netherlands Archaeology (2004). It maintains over 300,000 datasets
  with a staff of around 60, and is headquartered in The Hague.

level: national
country: NL
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-11-22"
previous_version: null
successor: null

domains:
  - DOMAIN-RESEARCH
organisations: []
related_entities:
  - NL
  - NL-NWO
relationships:
  - type: part-of
    target: NL
    source: fact
    evidence: "Confirmed by reading nwo.nl's own page directly (2026-09-04): DANS 'operates as an institute of KNAW... and NWO', described as the Dutch national centre of expertise and repository for research data. Its founding history, from an encyclopedia article, is in the prose and not needed for this edge (roadmap #767). Neither KNAW nor NWO is an Atlas entity, so the anchor edge is asserted at country scope rather than to either joint parent, the same pattern used for NL-SURF. Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Data Archiving and Networked Services (DANS)"
    url: "https://www.nwo.nl/en/data-archiving-and-networked-services-dans"
    publisher: "NWO — Dutch Research Council"
    accessed: "2026-09-04"
  - title: "Data Archiving and Networked Services"
    url: "https://nl.wikipedia.org/wiki/Data_Archiving_and_Networked_Services"
    publisher: "Wikipedia (NL)"
    accessed: "2026-09-04"
---

# DANS — Data Archiving and Networked Services

> **Added 2026-09-04, `verification: primary-source` from creation.**
> `discovery/research-queue.md` had flagged DANS, RIVM and NWO together
> as unresearched research/health infrastructure organisations since
> Batch 2. Both cited pages were read directly this pass.

## Description

DANS is the Dutch national centre of expertise and repository for
research data. Reading `nwo.nl`'s own page directly: it helps
researchers make their data accessible for reuse, "enabling
verification and reproducibility of published research," and maintains
over 300,000 datasets with a staff of around 60 — one of Europe's
leading data repositories.

## A joint institute, five predecessors absorbed

DANS operates as an institute of both **KNAW** (Royal Netherlands
Academy of Arts and Sciences) and **NWO** (Dutch Research Council).
Reading the Dutch Wikipedia article directly: it was founded in
**2005**, consolidating five earlier bodies — the **Steinmetz Archive**
(1964, transferred to KNAW 1972), the **Dutch Historical Data Archive**
(1989), the **Scientific Statistical Agency** (1994), the **Dutch
Institute for Scientific Information Services** (1997) and the
**Electronic Depot of Netherlands Archaeology** (2004). Neither KNAW
nor NWO is an Atlas entity, so this entity's anchor edge is asserted at
country scope, the same pattern used for [[NL-SURF]].

## Relationships

- `part-of` [[NL]] (anchor edge).

## Year only (2026-11-17)

The sources read give the year 2005, not a day. `start_date` was `2005-01-01`, a placeholder for "in 2005" that `metadata/metadata-schema.md` rules out, and is now empty; so are the 1 `valid_from` dates that repeated it. The year stays in the description and the text above.

## Sources

Listed in frontmatter, both read directly this pass.
