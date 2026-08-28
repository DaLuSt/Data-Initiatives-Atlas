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
  - EU-DSSC
relationships:
  - type: part-of
    target: EU-COMMON-DATA-SPACES
    source: fact
    evidence: "Confirmed by reading digital-strategy.ec.europa.eu's own 'Second staff working document on data spaces' library page directly (2026-08-28): title 'Second staff working document on data spaces', reference SWD(2024) 21 final, publication date 24 January 2024. The original citation in this entity pointed to the WRONG Commission URL — 'staff-working-document-data-spaces' (which is the FIRST SWD, SWD(2022) 45 final of 23 February 2022), not the second one labelled SWD(2024) 21. Corrected here. Energy's membership of the fourteen data spaces was independently confirmed by reading digital-strategy.ec.europa.eu's main 'Common European data spaces' overview page directly, which lists all fourteen by name."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Common European data spaces"
    url: "https://digital-strategy.ec.europa.eu/en/policies/data-spaces"
    publisher: "European Commission — Shaping Europe's digital future"
    accessed: "2026-08-28"
  - title: "Second staff working document on data spaces — SWD(2024) 21 final"
    url: "https://digital-strategy.ec.europa.eu/en/library/second-staff-working-document-data-spaces"
    publisher: "European Commission"
    accessed: "2026-08-28"
  - title: "EU Advances Common Energy Data Space (CEEDS)"
    url: "https://interoperable-europe.ec.europa.eu/collection/eprocurement/news/eu-advances-common-energy-data-space-ceeds"
    publisher: "Interoperable Europe Portal, European Commission"
    accessed: "2026-08-28"
  - title: "CEEDS.energy — Common European Energy Data Space"
    url: "https://www.ceeds.energy/"
    publisher: "CEEDS"
    accessed: "2026-08-28"
  - title: "Blueprint of the Common European Energy Data Space, version 2.0, July 2024"
    url: "https://intnet.eu/images/resources/Blueprint_CEEDS_v2.pdf"
    publisher: "int:net (Horizon Europe)"
---

# Common European Energy Data Space (CEEDS)

> **Re-verified 2026-08-28.** Four of five cited sources were read
> directly, and a genuine citation error was found and fixed: the SWD
> "staff working document on data spaces" URL this entity cited was the
> **first** staff working document (SWD(2022) 45 final, February 2022),
> not the January 2024 document (SWD(2024) 21 final) the source title
> claimed. The correct Commission URL is now cited and was read directly.
> `verification` moves from `search-only` to `primary-source`.

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

Listed in frontmatter, four of five read directly this pass. `ceeds.energy`,
read directly, confirms CEEDS.energy as a joint effort of ENTARC.eu,
Digital4Grids and EDA GmbH to operationalise the space, aiming at a
"digital twin for Europe's energy system." The Interoperable Europe news
article, also read directly, confirms Digital Europe Programme funding and
a March 2024 Brussels stakeholder meeting where a preliminary blueprint was
unveiled. The `intnet.eu` Blueprint PDF was attempted but returned
unreadable binary/stream content to this pass's fetch tooling; it was not
read.
