---
id: EU-CEEDS
type: data-space
name: Common European Energy Data Space
alternative_names:
  - CEEDS
  - Energy data space
description: >
  One of the fourteen common European data spaces, announced by the European
  Data Strategy and the EU action plan on digitalising the energy system.
  Its deployment is supported by the Digital Europe Programme, building on
  the results of six energy data space projects funded under Horizon Europe,
  and it is anchored as a central building block of the Commission's
  Strategic Roadmap for Digitalisation and AI in the Energy Sector presented
  on 3 June 2026.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - EU-COMMON-DATA-SPACES
  - EU-DSSC
relationships:
  - type: part-of
    target: EU-COMMON-DATA-SPACES
    source: fact
    evidence: "Energy is one of the fourteen common European data spaces identified in the Commission's January 2024 staff working document (SWD(2024) 21 final of 24.1.2024; digital-strategy.ec.europa.eu 'Common European data spaces'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "SWD(2024) 21 final — Staff working document on common European data spaces"
    url: "https://digital-strategy.ec.europa.eu/en/library/staff-working-document-data-spaces"
    publisher: "European Commission"
  - title: "EU Advances Common Energy Data Space (CEEDS)"
    url: "https://interoperable-europe.ec.europa.eu/collection/eprocurement/news/eu-advances-common-energy-data-space-ceeds"
    publisher: "Interoperable Europe Portal, European Commission"
  - title: "CEEDS.energy — Common European Energy Data Space"
    url: "https://www.ceeds.energy/"
    publisher: "CEEDS"
  - title: "Blueprint of the Common European Energy Data Space, version 2.0, July 2024"
    url: "https://intnet.eu/images/resources/Blueprint_CEEDS_v2.pdf"
    publisher: "int:net (Horizon Europe)"
---

# Common European Energy Data Space (CEEDS)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

CEEDS is the energy sector's common European data space, announced by the
[[EU-DATA-STRATEGY]] and by the EU action plan on digitalising the energy
system.

Its deployment is supported by the **Digital Europe Programme**, building on
six energy data space projects funded under Horizon Europe. The Commission's
**Strategic Roadmap for Digitalisation and AI in the Energy Sector**,
presented on **3 June 2026**, anchors CEEDS as a central building block and
governance framework.

## What "in deployment" looks like in practice

The Atlas's other sectoral data spaces are mostly described in strategy
documents. CEEDS has something more concrete attached: **INSIEME**, a
flagship initiative under the Digital Europe Programme with **more than 50
European partners**, piloting the building blocks for operationalising CEEDS
through **15+ deployments across member states**.

That is the useful thing about adding the energy data space specifically — it
shows the stage between "the Commission announced a data space" and "there is
a regulation", which [[EU-EHDS]] has and most of the fourteen do not.

## No `applies-in` edges

[[EU-EHDS]] carries `applies-in` to eight countries because it is backed by a
Regulation. CEEDS is a deployment programme, not an instrument: it is
supported by funding programmes and anchored in a roadmap, and neither of
those makes it *applicable* in a member state in the sense `applies-in`
carries here.

The same reasoning applies to the nine other data spaces added in this batch.
Only [[EU-EHDS]] among the fourteen has a Regulation behind it.

## Not modelled

- **INSIEME**, and the six Horizon Europe energy data space projects.
- The **EU action plan on digitalising the energy system** and the 2026
  Strategic Roadmap.
- Germany's **ENDA** reference architecture project, tested on the
  Redispatch 3.0 use case, which the sources name as a national contribution.
- Any **energy domain** entity. `DOMAIN-ENERGY` does not exist and is not
  created here: the Atlas's domain entities record a two-entity threshold,
  and CEEDS would be the only member.

## Sources

Listed in frontmatter.
