---
id: DE-ENDA
type: data-space
name: dena-ENDA
alternative_names:
  - ENDA
  - Energy Data Space (dena)
description: >
  German Gaia-X- and IDSA-compliant reference architecture for an energy
  data space, developed and implemented by the Deutsche Energie-Agentur
  (dena)'s Future Energy Lab in cooperation with ifok GmbH, Bonn
  Consulting, Fraunhofer FIT and innogence business consulting. It tests
  interoperable, sovereign exchange of energy data — including
  distribution-network and external environmental data — using the
  Redispatch 3.0 use case as its pilot, with Netzgesellschaft Niederrhein
  (NGN) as the connected pilot distribution network.

level: national
country: DE
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-25"
previous_version: null
successor: null

domains:
  - DOMAIN-ENERGY
organisations: []
related_entities:
  - EU-CEEDS
  - EU-GAIA-X
relationships:
  - type: based-on
    target: EU-GAIA-X
    source: fact
    evidence: "Confirmed by reading dena's own page directly (2026-09-20): 'A Gaia-X- and IDSA-compliant reference architecture was developed and implemented for a German energy data space.'"
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Data spaces in the energy industry"
    url: "https://www.dena.de/en/infocenter/data-spaces-in-the-energy-industry/"
    publisher: "Deutsche Energie-Agentur (dena)"
    accessed: "2026-09-20"
---

# dena-ENDA

> **Created 2026-09-20**, partially narrowing `discovery/unresolved.md`
> row #132 ("Germany's ENDA reference architecture project" — previously
> named only in [[EU-CEEDS]]'s own "Not modelled" prose, sourced from an
> unreadable PDF). Sourced from dena's own page, read directly. **The
> connection to CEEDS itself is not confirmed by this read** — see below.
>
> **Domain added 2026-09-25**: [[DOMAIN-ENERGY]], created because
> "Energie" is one of the Dutch Cyberbeveiligingswet's own named sectors.

## Description

dena-ENDA is a **Gaia-X- and IDSA-compliant reference architecture** for
a German energy data space, confirmed by reading dena's own page
directly. It was developed and implemented by dena's **Future Energy
Lab**, in cooperation with **ifok GmbH, Bonn Consulting, Fraunhofer FIT**
and **innogence business consulting**, under the oversight of Philipp
Richard, Head of Digital Technologies & Startup Ecosystem at dena.

## The Redispatch 3.0 use case — and a naming caveat

dena's own page states **Redispatch 3.0** was selected as the pilot use
case for testing ENDA's "sovereign and secure exchange of energy data,"
integrating distribution-network data and external environmental data
(e.g. weather), with **Netzgesellschaft Niederrhein (NGN)** connected as
the pilot distribution network.

**A separate, larger German research project also named "Redispatch
3.0"** exists — coordinated by OFFIS e.V., BMWK-funded, structured in
five phases with field tests in urban and rural environments (per
redispatch3.eu's own page, read directly, which does not mention ENDA or
dena at all). Whether dena-ENDA's "Redispatch 3.0" use case is this same
project, an independent implementation of the same regulatory concept
(Redispatch 3.0 as a grid-management framework introduced by the 2021
Grid Expansion Acceleration Act), or something else again, is not stated
by either source read. Both are recorded as distinct facts rather than
merged into one claim.

## Not confirmed: the connection to CEEDS

[[EU-CEEDS]]'s own entity names ENDA as "a national contribution" to the
Common European Energy Data Space, based on a source (the CEEDS Blueprint
PDF) that could not be read as text in a prior pass. dena's own page,
read directly this pass, **does not mention CEEDS** anywhere — its
"related initiatives" are limited to an "energy data – X project" and a
new data institute, neither further identified. The CEEDS connection
therefore remains an unconfirmed claim from an unread source, not
strengthened by this pass's direct read.

## Not modelled

- **ifok GmbH, Bonn Consulting, Fraunhofer FIT, innogence** — the
  cooperating organisations, not independently researched.
- **Netzgesellschaft Niederrhein (NGN)**, the pilot distribution network.
- The **OFFIS-coordinated "Redispatch 3.0"** project — a plausibly
  related but not confirmed-identical initiative, described above.
- An exact **start date or project duration** — dena's own page gives
  only the 25 April 2024 publication date of a report describing the
  project, not the project's own start date.

## Relationships

- `based-on` [[EU-GAIA-X]] — `confidence: high`.

## Sources

Listed in frontmatter, read directly. redispatch3.eu was also read
directly this pass for the naming-caveat check above but is not added as
a source, since it supports no claim this entity makes.
