---
id: DE-GEMATIK
type: organisation
name: gematik GmbH
alternative_names:
  - gematik
  - Gesellschaft für Telematikanwendungen der Gesundheitskarte
description: >
  German company responsible for the conception and development of the
  Telematikinfrastruktur, the national infrastructure for the secure exchange
  of medical data and information. It defines the legally binding standards
  and specifications of the infrastructure's components and services, and
  operates the interoperability navigator through which those specifications
  are published.

level: national
country: DE
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-21"
previous_version: null
successor: null

domains:
  - DOMAIN-HEALTH
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - DE
  - DE-GDNG
  - EU-EHDS
relationships:
  - type: part-of
    target: DE
    source: fact
    evidence: "gematik GmbH is responsible for the conception and development of the Telematikinfrastruktur and defines legally binding standards and specifications of its components and services; the unified Telematikinfrastruktur is the foundation for the secure exchange of medical data in the German health system (gematik.de; ina.gematik.de 'Digital Health und Interoperabilität in Deutschland'; bundesaerztekammer.de 'Telematikinfrastruktur'). NOT READ — search-only. Anchor edge under metadata/relationship-types.md §2.3: gematik is a company whose majority shareholder is the federal health ministry, which the sources describe as setting legally binding standards."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "INA — Interoperabilitäts-Navigator: Digital Health und Interoperabilität in Deutschland"
    url: "https://www.ina.gematik.de/themenbereiche/digital-health-und-interoperabilitaet-in-deutschland"
    publisher: "gematik GmbH"
  - title: "Telematikinfrastruktur"
    url: "https://www.bundesaerztekammer.de/themen/aerzte/digitalisierung/digitale-anwendungen/telematikinfrastruktur"
    publisher: "Bundesärztekammer"
  - title: "Digitalisierung im Gesundheitswesen"
    url: "https://www.bundesregierung.de/breg-de/aktuelles/digitalisierung-im-gesundheitswesen-2447110"
    publisher: "Die Bundesregierung"
---

# gematik

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read — retrieval is blocked by
> the network egress proxy. `verification: search-only`.

## Description

The company responsible for the **Telematikinfrastruktur** — Germany's
national infrastructure for secure exchange of medical data. It defines the
**legally binding standards and specifications** of the infrastructure's
components and services.

The applications that run on it include the **elektronische Patientenakte**
(ePA), the electronic patient record, which is opt-out, and the
E-Prescription, through which pharmacies get restricted access.

## Germany's health data custodian, and the Atlas's second health country

Before 2026-08-21, [[DOMAIN-HEALTH]] was attached to entities in **one
country** — the Netherlands, through [[NL-NICTIZ]] and [[NL-HEALTH-RI]] — in
an Atlas that holds [[EU-EHDS]], the European Health Data Space.

`discovery/candidates.md` measured that as *"the single largest correction
available"*: fifty-seven of fifty-eight countries with no health-data entity
at all. gematik is the German answer to the question [[NL-NICTIZ]] answers
for the Netherlands — who defines the standards by which health data moves.

## Relationships

- `part-of` [[DE]] — anchor edge. gematik is a GmbH rather than a ministry,
  but the sources describe it as setting *legally binding* standards, which
  is a public function and not a private one. The edge records that; it does
  not assert a shareholding the sources here do not state.
- No edge to [[EU-EHDS]] is asserted. The European Health Data Space and the
  Telematikinfrastruktur are both health data infrastructures and no source
  in this set connects them; see [[DE-GDNG]] for what the German legislation
  does say.

## Sources

Listed in frontmatter — gematik's own interoperability navigator, the German
Medical Association's page on the infrastructure, and the federal
government's overview of health-system digitalisation.
