---
id: EU-AGRI-DATA-SPACE
type: data-space
name: Common European Agriculture Data Space
alternative_names:
  - Agriculture Data Space
description: >
  One of the common European data spaces, intended to allow comparative
  analyses between farms in order to improve their sustainability and
  economic performance.

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
    evidence: "Confirmed by reading digital-strategy.ec.europa.eu's own 'Common European data spaces' page directly (2026-08-28): agriculture is listed among the 14 sectors with a data space in deployment, alongside cultural heritage, energy, finance, green deal, smart cities, health, language, manufacturing, media, mobility, public administration, research/EOSC and skills. The Commission's own library page 'Common European data spaces for agriculture and mobility', also read directly, confirms the agriculture space's objective as developing 'a secure and trusted data space to allow the farming sector to share and access data', explicitly in support of Green Deal and Common Agricultural Policy objectives."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Common European data spaces"
    url: "https://digital-strategy.ec.europa.eu/en/policies/data-spaces"
    publisher: "European Commission — Shaping Europe's digital future"
    accessed: "2026-08-28"
  - title: "Common European data spaces for agriculture and mobility"
    url: "https://digital-strategy.ec.europa.eu/en/library/common-european-data-spaces-agriculture-and-mobility"
    publisher: "European Commission — Shaping Europe's digital future"
    accessed: "2026-08-28"
  - title: "Common European Data Spaces — SWD(2024) 21 final"
    url: "https://www.tcontas.pt/en-gb/seminars/sais-data/Documents/Documents/Common%20European%20Data%20Spaces%20-%20latest%20report%20Jan%202024.pdf"
    publisher: "European Commission (copy hosted by Tribunal de Contas)"
---

# Common European Agriculture Data Space

> **Re-verified 2026-08-28.** Two of three cited sources were read directly.
> The Commission's own data-spaces overview confirms agriculture as one of
> the 14 sectors, and a Commission library document dedicated to the
> agriculture and mobility data spaces confirms and extends the purpose
> statement. `verification` moves from `search-only` to `primary-source`.

## Description

The agriculture data space is one of the fourteen common European data
spaces. Confirmed by reading the Commission's own library page directly:
its objective is to "develop a secure and trusted data space to allow the
farming sector to share and access data", improving economic and
environmental performance — explicitly framed as supporting both the
**European Green Deal** and the **Common Agricultural Policy**. This gives
the previously-sourced "comparative analyses between farms" purpose
statement a firmer, directly-read basis and a stated policy rationale.

The Commission also runs complementary data infrastructure — the **Farm
Sustainability Data Network (FSDN)**, which publishes economic reports on
EU farming (farm incomes, production costs) at member-state, farm-type and
economic-size level — though this is EU statistical infrastructure
adjacent to the data space rather than the data space itself, and is not
modelled as a relationship here.

`confidence: medium`, `coverage: medium` — up from `low`/`low`: the purpose
and policy framing are now confirmed from a Commission source read
directly, but governance, responsible organisations, standards and
technical infrastructure remain unresearched.

`domains:` is left empty for the same two-entity-threshold reason as
[[EU-GREEN-DEAL-DATA-SPACE]].

## What is still not read

The **SWD(2024) 21 final** staff working document (the Commission's own
"second staff working document on data spaces") is genuinely the primary
source for the 14-space enumeration, but the PDF mirror cited here (hosted
by the Portuguese Tribunal de Contas) returns as unreadable binary/stream
data to this pass's fetch tooling — attempted and confirmed to exist (its
title and 24 January 2024 date were independently confirmed via search),
but its content was not read. The two Commission web pages above cover the
same ground and were read directly, which is why this entity is promoted
on their strength.

## Relationships

- Part of [[EU-COMMON-DATA-SPACES]].

## Sources

Listed in frontmatter. Two of three read directly this pass — the
Commission's data-spaces overview and its agriculture-and-mobility library
page. The SWD(2024) 21 final PDF mirror was attempted but returned
unreadable binary content; its existence and date were independently
confirmed via search rather than by reading it.
