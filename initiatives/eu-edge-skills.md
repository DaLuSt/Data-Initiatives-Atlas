---
id: EU-EDGE-SKILLS
type: initiative
name: EDGE-Skills
alternative_names:
  - European Dataspace for Growth and Education-Skills
description: >
  A project led by Prometheus-X, uniting 36 organisations from eight EU
  countries, aiming to provide a human-centric, distributed and sovereign
  data-space infrastructure for education and skills, deployed as
  plug-and-play cloud services with first use cases in the education and
  tourism domains. It is one of two projects the European Commission's
  own "Common European data spaces" page names under the rollout of the
  skills data space, the other being DS4Skills. It aims to impact over
  5 million learners by the end of 2026.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-20"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-SKILLS-DATA-SPACE
  - EU-DS4SKILLS
relationships:
  - type: part-of
    target: EU-SKILLS-DATA-SPACE
    source: fact
    evidence: "CLOSES discovery/unresolved.md row #125's EDGE-Skills half. Confirmed by reading digital-strategy.ec.europa.eu's own 'Common European data spaces' page directly (already cited on [[EU-SKILLS-DATA-SPACE]]): under the page's rollout listing for the Skills data space, it names exactly two projects, DS4Skills and EDGE-Skills, with no further description on that page. Prometheus-X's own EDGE-Skills whitepaper (publisher: PROMETHEUS-X association, dated December 2024, read directly as a local PDF since WebFetch returned only binary content for it) states directly: 'The EDGE-Skills project (European Dataspace for Growth and Education-Skills), which is led by Prometheus-X, aims to provide a human-centric, distributed and sovereign data space infrastructure ... with first use cases in the education and tourism domains,' uniting '36 organisations from eight European Union (EU) countries' with a target to 'impact over 5 million learners by the end of 2026.'"
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Common European data spaces"
    url: "https://digital-strategy.ec.europa.eu/en/policies/data-spaces"
    publisher: "European Commission — Shaping Europe's digital future"
    accessed: "2026-09-20"
  - title: "EDGE-Skills — Creating the future of data spaces in Europe (Whitepaper)"
    url: "https://prometheus-x.org/wp-content/uploads/2025/06/EDGE-Skills_Whitepaper.pdf"
    publisher: "PROMETHEUS-X association"
    accessed: "2026-09-20"
---

# EDGE-Skills

> **Created 2026-09-20**, closing the EDGE-Skills half of
> `discovery/unresolved.md` row #125 (DS4Skills already closed the other
> half, 2026-09-05). Sourced from Prometheus-X's own whitepaper on the
> project, published under its own name, read directly as a local PDF.

## Description

EDGE-Skills — **European Dataspace for Growth and Education-Skills** — is
"led by **Prometheus-X**," confirmed by reading the project's own
whitepaper directly, published by the PROMETHEUS-X association itself.
Prometheus-X is described in the same document as "a non-profit
organisation, founded in **October 2021**," whose mission is "to fund,
govern and develop open source building blocks for data spaces."

The project unites **36 organisations from eight EU countries**, aiming
to "provide a human-centric, distributed and sovereign data space
infrastructure that is deployed and ready to use as plug and play through
a set of innovative cloud services with first use cases in the
**education and tourism domains**." Its stated target: to "impact over
**5 million learners** by the end of 2026" through three objectives —
developing high-value education/skills data ecosystems, innovating
cloud-to-edge services, and ensuring accessibility for all stakeholders.

## The Commission's own naming, now matched to a real project

[[EU-SKILLS-DATA-SPACE]]'s own entity already recorded that the
Commission's "Common European data spaces" page names exactly two
projects under the Skills data space's rollout — DS4Skills and
EDGE-Skills — without further description on that page. [[EU-DS4SKILLS]]
closed the first half of that gap on 2026-09-05; this entity closes the
second, sourced from EDGE-Skills' own whitepaper rather than the thin
Commission listing.

## A note on partner counts

Secondary sources found in search (a University of Koblenz project page,
among others) give **40 organisations**, not 36. The whitepaper — a
primary source published under Prometheus-X's own name — is preferred,
and its figure (36) is the one recorded here.

## Not modelled

- **Prometheus-X** itself, as an organisation distinct from this project —
  not independently modelled; its founding date and mission are recorded
  in prose here rather than on a separate entity.
- EDGE-Skills' **36 named partner organisations**.
- The **use cases** named in the whitepaper (skill-gap analytics for
  students, "MyTravelConnect") as separate entities.
- Its **funding programme code** — search-only sources give conflicting
  figures (DIGITAL-2021-PREPACTS-DS-01-SKILLS vs. HORIZON-CL5-2023-D6-01-05)
  neither confirmed by the whitepaper pages read this pass.

## Relationships

- `part-of` [[EU-SKILLS-DATA-SPACE]] — `confidence: high`.

## Sources

Listed in frontmatter, both read directly.
