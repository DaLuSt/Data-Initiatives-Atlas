---
id: DE-BFDI
type: organisation
name: Bundesbeauftragte für den Datenschutz und die Informationsfreiheit
alternative_names:
  - BfDI
  - Federal Commissioner for Data Protection and Freedom of Information
description: >
  Independent supreme federal authority for data protection and freedom of
  information in Germany, seated in Bonn. It is the data-protection
  supervisory authority for all federal public bodies, certain social
  security institutions, the fiscal authorities and telecommunications and
  postal undertakings, and it also handles complaints about access to
  information under the Informationsfreiheitsgesetz.

level: national
country: DE
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - DE-BDSG
  - DE-IFG
relationships:
  - type: applies-to
    target: DE-BDSG
    source: fact
    evidence: "The BfDI is the independent supreme federal authority for data protection and freedom of information in Germany and the data-protection supervisory authority for all federal public bodies, certain social security institutions, the fiscal authorities and telecommunications and postal undertakings; the Bundesdatenschutzgesetz is the federal act under which that supervision is exercised (bfdi.bund.de 'Aufgaben des BfDI'; de.wikipedia.org 'Bundesbeauftragter fuer den Datenschutz und die Informationsfreiheit'; wirtschaftslexikon.gabler.de). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: DE-IFG
    source: fact
    evidence: "Among the BfDI's tasks is helping persons who consider their fundamental right of access to information under the IFG to have been violated (bfdi.bund.de 'Aufgaben und Befugnisse der BfDI'; de.wikipedia.org). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Aufgaben und Befugnisse der BfDI"
    url: "https://www.bfdi.bund.de/DE/BfDI/Inhalte/BfDI/AufgabenBFDI.html"
    publisher: "Bundesbeauftragte für den Datenschutz und die Informationsfreiheit (BfDI)"
  - title: "Der Bundesbeauftragte für den Datenschutz und die Informationsfreiheit (BfDI)"
    url: "https://www.bfdi.bund.de/DE/BfDI/Inhalte/Datenschutzpfad/BfDI.html"
    publisher: "Bundesbeauftragte für den Datenschutz und die Informationsfreiheit (BfDI)"
  - title: "Bundesbeauftragter für den Datenschutz und die Informationsfreiheit"
    url: "https://de.wikipedia.org/wiki/Bundesbeauftragter_f%C3%BCr_den_Datenschutz_und_die_Informationsfreiheit"
    publisher: "Wikipedia"
  - title: "Bundesbeauftragter für den Datenschutz und die Informationsfreiheit (BfDI)"
    url: "https://wirtschaftslexikon.gabler.de/definition/bundesbeauftragter-fuer-den-datenschutz-und-die-informationsfreiheit-bfdi-31020"
    publisher: "Gabler Wirtschaftslexikon"
---

# Bundesbeauftragte für den Datenschutz und die Informationsfreiheit (BfDI)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The BfDI is an **independent supreme federal authority** (unabhängige
eigenständige oberste Bundesbehörde) for data protection and freedom of
information, seated in Bonn.

As a supervisory authority it covers all federal public bodies, certain
social security institutions, the fiscal authorities, and
telecommunications and postal undertakings, checking whether data
protection law is implemented and observed at those bodies. The sources
describe it as the guardian of the fundamental right to informational
self-determination.

Its tasks span both halves of its name:

- **Data protection** — supervising and advising federal authorities and
  other federal public bodies.
- **Freedom of information** — helping people who consider their right of
  access to information under [[DE-IFG]] to have been violated, and
  advising and checking on access to environmental information at federal
  public bodies.

The office-holder is proposed by the federal government, elected by the
Bundestag, and serves a five-year term.

## ⚠ The federal supervisory landscape is not modelled

Germany does not have one data protection authority. The BfDI supervises
**federal** bodies; each Land has its own supervisory authority for the
public bodies and, in most cases, the private sector within it. **None of
those authorities is an Atlas entity**, for the same reason no Land is: the
Atlas has no sub-national level.

This makes the German entry structurally different from the Dutch one in a
way worth stating plainly. [[NL-AP]] is *the* Dutch supervisory authority;
the BfDI is *one of seventeen* German ones. Anyone reading `country: DE`
plus `type: organisation` plus "data protection authority" and inferring
national coverage would be wrong.

## Two relationships that are not asserted

- **`implements` or `governed-by` → [[DE-BDSG]].** The BfDI is plainly the
  authority the BDSG constitutes and empowers, and the BDSG's own sources
  discuss the supervisory regime. But no source read states the connection
  in terms the Atlas can cite, and the BfDI's own task page describes
  powers without being quoted on their statutory basis.
- **`participates-in` → [[EU-EDPB]].** [[NL-AP]] carries exactly this
  relationship, and the German federal and Land authorities are certainly
  represented in the European Data Protection Board. **No source read says
  so**, and the German representation arrangement is precisely the kind of
  detail — which authority represents Germany, and how — that should not be
  guessed at. Refusing this one costs the Atlas a DE→EU edge it would
  otherwise gain for free, which is why it is recorded here rather than
  passed over silently.

Both are logged in `discovery/unresolved.md`.

## Relationships

- `applies-to` [[DE-IFG]].

## Sources

Listed in frontmatter.
