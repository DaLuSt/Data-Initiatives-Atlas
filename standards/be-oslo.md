---
id: BE-OSLO
type: standard
name: OSLO
alternative_names:
  - Open Standaarden voor Linkende Organisaties
  - Open Standards for Linking Organisations
  - Open Standards for Local Administrations (OSLO, original name)
description: >
  Flemish semantic interoperability standard providing open, extensible
  data vocabularies for exchanging core government data — contact
  information, persons, location and public-service delivery. Development
  began in October 2012 under the name "Open Standards for Local
  Administrations," led by V-ICT-OR (the Flemish local-government ICT
  association) as a public-private collaboration with 58 people from 28
  organisations; version 1.0 was released 30 May 2013. That original
  initiative is recorded by the European Commission's own interoperable
  Europe catalogue as archived from October 2017. A broader successor
  effort, renamed "Open Standaarden voor Linkende Organisaties" to reflect
  a scope beyond local government, continues under the Flemish
  government's own support and is maintained by [[BE-DIGITAAL-VLAANDEREN]].

level: subnational
country: BE
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2012-10-01
end_date: null
last_verified: "2026-09-04"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - BE-DIGITAAL-VLAANDEREN
relationships:
  - type: maintained-by
    target: BE-DIGITAAL-VLAANDEREN
    source: fact
    evidence: "Confirmed by reading the European Commission's own interoperable Europe catalogue entry for OSLO directly (2026-09-04), which names V-ICT-OR as the original 2012-2017 initiative's lead and records the solution archived from 2 October 2017. A WebSearch-surfaced summary (not independently fetched this pass) states the standard was later renamed and continued under Flemish Government support because 'this isn't just a story about local governments' — corroborated by OSLO's own GitHub organisation, github.com/Informatievlaanderen, carrying the pre-2021 name of the agency now called [[BE-DIGITAAL-VLAANDEREN]], which this pass did not independently open and read."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "OSLO — Open Standards for Local Administrations, Flanders"
    url: "https://interoperable-europe.ec.europa.eu/collection/oslo-open-standards-local-administrations-flanders/solution/oslo-open-standards-local-administrations-flanders"
    publisher: "European Commission — interoperable Europe"
    accessed: "2026-09-04"
---

# OSLO

> **Added 2026-09-04, `verification: primary-source` from creation.**
> `discovery/research-queue.md` had flagged OSLO as "a major European
> semantic-interoperability programme, entirely unmodelled," blocked (it
> said) on the Atlas having no `level` term for a Belgian Region —
> resolved by `level: subnational`, added 2026-08-21. The European
> Commission's own interoperable Europe catalogue page was read
> directly this pass; the current, post-2017 phase of OSLO rests on a
> WebSearch-surfaced secondary summary that was not independently
> fetched, and is flagged as such below.

## Description

OSLO provides open, extensible data vocabularies for four domains: contact
information, persons, location and public-service delivery. Reading the
European Commission's own **interoperable Europe** catalogue page
directly: development began in **October 2012** under the original name
**"Open Standards for Local Administrations,"** led by **V-ICT-OR** (the
Flemish local-government ICT association) as a public-private
collaboration involving **58 people from 28 organisations**, sponsored by
ICT service providers and government bodies including Belgacom, CIPAL and
Digipolis. **Version 1.0 was released 30 May 2013**, after a public
review period.

## Built on the EU's own core vocabularies

The same page states the specifications are **"a local extension of the
standards developed at European level within the ISA Programme"**
(Interoperability Solutions for European Public Administrations),
specifically extending the EU's Core Person, Core Business, Core
Location and Core Public Service vocabularies. No relationship is
asserted to those EU-level vocabularies, because none is an Atlas entity
— the same restraint the Atlas already applies to unmodelled European
vocabularies elsewhere (see [[EU-DCAT-AP]]'s own upstream, [[INTL-DCAT]]).

## Two phases, one name

The European Commission's own catalogue entry records the **original**
OSLO initiative — the local-government-scoped one V-ICT-OR led — as
**archived, completed 2 October 2017**. A WebSearch-surfaced summary,
not independently fetched this pass, describes a broader successor:
renamed **"Open Standaarden voor Linkende Organisaties"** (dropping the
local-government-only scope) and continued under the Flemish
government's own support, now maintained by [[BE-DIGITAAL-VLAANDEREN]]
— whose GitHub organisation still carries OSLO's repositories under the
pre-2021 name, `Informatievlaanderen`. This entity's `status: active`
and `maintained-by` edge describe that later, continuing phase; the
`start_date` records the original 2012 origin because no source read
gives a separate founding date for the renamed continuation.

## Not modelled

- The EU's own **ISA Programme core vocabularies** (Person, Business,
  Location, Public Service) that OSLO extends. Not Atlas entities.
- **V-ICT-OR**, OSLO's original 2012 initiator, now a secondary role
  once the Flemish government took over stewardship.

## Relationships

- `maintained-by` [[BE-DIGITAAL-VLAANDEREN]].

## Sources

Listed in frontmatter, read directly this pass. The post-2017 renaming
and current GitHub-hosted status rest on a WebSearch summary that was
not independently fetched.
