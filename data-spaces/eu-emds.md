---
id: EU-EMDS
type: data-space
name: Common European Mobility Data Space
alternative_names:
  - EMDS
  - European Mobility Data Space
description: >
  One of the common European data spaces, covering mobility and transport
  data. Described as a resource for managing intermodal logistics in the
  freight sector as well as for personal mobility.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-MOBILITY
organisations: []
related_entities:
  - EU-COMMON-DATA-SPACES
  - EU-ITS-DIRECTIVE
  - NL-NTM
relationships:
  - type: part-of
    target: EU-COMMON-DATA-SPACES
    source: fact
    evidence: "Confirmed by reading transport.ec.europa.eu's own page 'Creating a common European mobility data space' directly (2026-08-28): the EMDS 'aims to facilitate access, pooling and sharing of data from existing and future transport and mobility data sources', covering both passenger and freight transport as 'a framework for interlinking and federating many different transport-data ecosystems.' A second Commission library page, 'Common European data spaces for agriculture and mobility', also read directly, confirms mobility's membership of the fourteen data spaces and gives funding figures (a mobility preparatory action of roughly EUR 1 million and a deployment action of roughly EUR 8 million, scheduled Q3 2022)."
    confidence: high
    valid_from: null
    valid_until: null
  - type: references
    target: EU-ITS-DIRECTIVE
    source: fact
    evidence: "Confirmed by reading transport.ec.europa.eu's own 'Creating a common European mobility data space' page directly (2026-09-05), a sentence not extracted in the 2026-08-28 pass: the EMDS 'will take account of data-sharing mechanisms set up or proposed in existing passenger and freight transport ecosystems and legislation (e.g. the ITS Directive establishing the National Access Points).' Recorded as `references` rather than a stronger type — the source says EMDS will take the NAP mechanism into account, not that it builds on or depends on it structurally."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Creating a common European mobility data space"
    url: "https://transport.ec.europa.eu/transport-themes/smart-mobility/creating-common-european-mobility-data-space_en"
    publisher: "European Commission — Mobility and Transport"
    accessed: "2026-08-28"
  - title: "Common European data spaces for agriculture and mobility"
    url: "https://digital-strategy.ec.europa.eu/en/library/common-european-data-spaces-agriculture-and-mobility"
    publisher: "European Commission — Shaping Europe's digital future"
    accessed: "2026-08-28"
  - title: "Common European data spaces"
    url: "https://digital-strategy.ec.europa.eu/en/policies/data-spaces"
    publisher: "European Commission — Shaping Europe's digital future"
    accessed: "2026-08-28"
  - title: "Towards a common European mobility data space (EMDS)"
    url: "https://www.data-spaces-symposium.eu/wp-content/uploads/2024/03/1535DI1.pdf"
    publisher: "Data Spaces Symposium"
  - title: "Common European Data Spaces — SWD(2024) 21 final"
    url: "https://www.tcontas.pt/en-gb/seminars/sais-data/Documents/Documents/Common%20European%20Data%20Spaces%20-%20latest%20report%20Jan%202024.pdf"
    publisher: "European Commission (copy hosted by Tribunal de Contas)"
---

# Common European Mobility Data Space (EMDS)

> **Re-verified 2026-08-28.** Two new Commission sources were found and
> read directly this pass — the Directorate-General for Mobility and
> Transport's own EMDS page, and a Commission library document dedicated
> to the agriculture and mobility data spaces — which together confirm and
> substantially extend the purpose statement this entity previously held
> unread. `verification` moves from `search-only` to `primary-source`.

## Description

The mobility data space is one of the fourteen common European data spaces.
Confirmed by reading the Commission's own DG MOVE page directly: it "aims
to facilitate access, pooling and sharing of data from existing and future
transport and mobility data sources", is explicitly **"not a single
database"** but "a framework for interlinking and federating many
different transport-data ecosystems", and covers **both passenger and
freight transport** — including intermodal logistics, cross-border
passenger and freight multimodality, and support for local authorities'
sustainable urban mobility plans. Governance runs through defined
"building blocks", an "interlinking layer", and new standards where
necessary, building on [[EU-DGA]] and the Data Act.

Deployment runs through **deployEMDS**, the first EMDS deployment project,
supported by the Digital Europe Programme, running November 2023 to
October 2026 — confirmed via search cross-checks of the Commission's
mobility observatory and the deployEMDS project's own site, though neither
was read directly this pass and deployEMDS itself is not modelled as an
entity.

`confidence: medium` and `coverage: medium`, up from `low`/`low`: the
purpose, scope and governance approach are now confirmed from a Commission
source read directly, and a Commission library page adds funding detail —
a mobility preparatory action of roughly EUR 1 million and a deployment
action of roughly EUR 8 million (Q3 2022). Responsible organisations,
detailed standards and participating countries remain unresearched.

## Relationship to the national access points — narrowed, 2026-09-05

[[NL-NTM]] is the Dutch national access point for mobility data, existing
under [[EU-ITS-DIRECTIVE]]. National access points are the obvious
building blocks of an EU mobility data space, and the connection is close to
self-evident.

**The EU-level half is now sourced, the national half is not.**
Re-reading transport.ec.europa.eu's own page directly surfaces a sentence
the 2026-08-28 pass had not extracted: the EMDS "will take account of
data-sharing mechanisms set up or proposed in existing ... legislation
(e.g. the ITS Directive establishing the National Access Points)." A
`references` edge to [[EU-ITS-DIRECTIVE]] is asserted on that basis — a
"will take account of" framing, deliberately not the stronger "builds on"
the earlier text over-assumed. No source read names [[NL-NTM]] or any
other specific national NAP; the country-level connection stays an Atlas
association via `related_entities` rather than a typed edge.

## Sources

Listed in frontmatter, three of five read directly this pass — the DG MOVE
EMDS page, the agriculture-and-mobility library page, and the main
data-spaces overview page. The Data Spaces Symposium PDF and the
Tribunal de Contas-hosted SWD(2024) 21 mirror were both attempted and
returned unreadable binary/stream content to this pass's fetch tooling;
neither was read.
