---
id: GB-GDS
type: organisation
name: Government Digital Service
alternative_names:
  - GDS
  - the digital centre of government
description: >
  The United Kingdom's central digital government organisation, described as
  the digital centre of government and responsible for setting, leading and
  delivering the vision for a modern digital government. In January 2025 the
  Government Digital Service, the Central Digital and Data Office, the
  Incubator for Artificial Intelligence, the Geospatial Commission and the
  Responsible Technology Adoption Unit merged under the GDS name, reuniting
  functions that had been split out of GDS four years earlier. It was part
  of the Department for Science, Innovation and Technology until that
  department was abolished in July 2026, after which digital government
  functions including GDS transferred to the Department for Culture, Media
  and Sport.

level: national
country: GB
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - GB-DSIT
  - GB-DCMS
  - GB-ONE-LOGIN
  - GB-DATA-GOV-UK
  - NL-LOGIUS
  - ES-AEAD
relationships:
  - type: governed-by
    target: GB-DCMS
    source: fact
    evidence: "Confirmed by reading thinkdigitalpartners.com (2026-08-22): 'The Department for Culture, Media and Sport (DCMS) will be renamed the Department for Digital, Culture, Media and Sport (DDCMS), taking responsibility for digital government functions including the Government Digital Service (GDS).' CAVEAT: reported via a written ministerial statement quoted in trade press; no machinery-of-government order was located."
    confidence: medium
    valid_from: 2026-07-21
    valid_until: null

sources:
  - title: "Government Digital Service — About"
    url: "https://gds.blog.gov.uk/about"
    publisher: "Government Digital Service (UK)"
    accessed: "2026-08-22"
  - title: "A blueprint for modern digital government"
    url: "https://assets.publishing.service.gov.uk/media/678f6665f4ff8740d978864c/a-blueprint-for-modern-digital-government-web-optimised.pdf"
    publisher: "Department for Science, Innovation and Technology (UK)"
    accessed: "2026-08-22"
  - title: "CDDO brought back into GDS in digital government shake-up"
    url: "https://www.publictechnology.net/2025/01/21/education-and-skills/cddo-brought-back-into-gds-in-digital-government-shake-up/"
    publisher: "PublicTechnology"
    accessed: "2026-08-22"
  - title: "DSIT to be scrapped with 'strengthened DCMS to take responsibility for digital transformation'"
    url: "https://www.publictechnology.net/2026/07/21/government-and-politics/dsit-to-be-scrapped-with-strengthened-dcms-to-take-responsibility-for-digital-transformation/"
    publisher: "PublicTechnology"
    accessed: "2026-08-22"
  - title: "Central Digital and Data Office"
    url: "https://www.gov.uk/government/organisations/central-digital-and-data-office"
    publisher: "GOV.UK"
    accessed: "2026-08-22"
  - title: "Government abolishes DSIT as AI gains a seat at the Cabinet table"
    url: "https://www.thinkdigitalpartners.com/news/2026/07/21/government-abolishes-dsit-as-ai-gains-a-seat-at-the-cabinet-table/"
    publisher: "THINK Digital Partners"
    accessed: "2026-08-22"
---

# Government Digital Service

> **Verified 2026-08-22.** GDS's own blog and publictechnology.net's
> January 2025 reorganisation article were read directly and confirmed the
> claims below, verbatim in places.

## Description

Confirmed verbatim on gds.blog.gov.uk (2026-08-22): "The Government
Digital Service (GDS) is the digital centre of government — responsible
for setting, leading and delivering the vision for a modern digital
government." GDS is the UK's **digital centre of government**: responsible for setting,
leading and delivering the vision for a modern digital government, and for
the common platforms the rest of the public sector uses — including
[[GB-ONE-LOGIN]] and [[GB-DATA-GOV-UK]].

## The seventh central digital-government body, and a different shape

| Country | Body | Form |
|---|---|---|
| Netherlands | [[NL-BZK]] | ministry, with [[NL-LOGIUS]] as the implementing service |
| Germany | [[DE-BMDS]] | ministry |
| Belgium | [[BE-BOSA]] | federal public service |
| France | [[FR-DINUM]] | interministerial directorate under the Prime Minister |
| Spain | [[ES-AEAD]] | state agency, transformed from a directorate in 2025 |
| Poland | [[PL-MC]] | ministry, with [[PL-COI]] as the implementing body |
| **United Kingdom** | **GDS** | **an organisation inside a department, doing both jobs** |

Six countries separate *direction* from *delivery* — a ministry plus an
implementing body, or a ministry alone. The UK does not: GDS both sets
cross-government digital strategy and operates the platforms. It is the
first body in the Atlas that is neither a ministry nor a subordinate
delivery organisation, but the two functions in one unit.

## Merged, split, and merged again

Confirmed verbatim on GOV.UK's own "Central Digital and Data Office" page
(2026-08-22): "The Central Digital and Data Office (CDDO), the Geospatial
Commission, the Government Digital Service (GDS) and the Incubator for
Artificial Intelligence (i.AI) have merged to create the new Government
Digital Service — the digital centre of government ... CDDO existed from
April 2021 to January 2025." The **Responsible Technology Adoption Unit**
addition was not independently re-confirmed this pass and is retained from
the original sourcing. CDDO had itself been spun *out* of GDS four years
earlier (April 2021) to focus on cross-government strategy.

**None of the merged bodies is a separate Atlas entity**, and the merger is
therefore not modelled as a relationship — it is recorded here as
description. Creating CDDO or i.AI now, only to mark them superseded, would
add four entities to say one thing.

⚠ The **Geospatial Commission** was among the merged teams. It is the body
that would otherwise be the UK's counterpart to [[NL-KADASTER]] and the
geospatial authorities in [[DOMAIN-GEOSPATIAL]], and it **no longer exists
as an independent organisation**. Ordnance Survey, the UK's national mapping
agency, is not modelled either. The UK therefore joins this Atlas with **no
geospatial entity at all**.

## Its parent department changed twice in two years

GDS was part of [[GB-DSIT]] from that department's creation in February 2023
until its **abolition on 21 July 2026**, when digital government functions
moved to [[GB-DCMS]]. The `governed-by` edge here points at DCMS and is
dated from the abolition.

That edge is the least certain thing in this entity. It now rests on
thinkdigitalpartners.com's account of a written ministerial statement,
read directly, rather than unread trade press — a step up from the
original sourcing, but still not a machinery-of-government order, and the
`evidence` string says so.

## Relationships

- `governed-by` [[GB-DCMS]], valid from 21 July 2026.

**No relationship to [[NL-LOGIUS]], [[ES-AEAD]] or any other country's
delivery body.** They are national answers to a shared problem, which is not
a relationship — the same position taken for [[FR-FRANCECONNECT]] and
[[DE-BUNDID]].

## Sources

Listed in frontmatter. Two of the five are trade press rather than
government sources, and both carry the July 2026 reorganisation; GDS's own
blog and the January 2025 reorganisation article were read directly this
pass.
