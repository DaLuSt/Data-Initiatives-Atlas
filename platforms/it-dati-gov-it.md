---
id: IT-DATI-GOV-IT
type: platform
name: dati.gov.it
alternative_names:
  - Portale dei dati aperti della PA
  - Italian open data portal
description: >
  Italy's national open data portal, the single catalogue of open data
  published by Italian public administrations. Launched as a government
  project in 2011 and managed by AgID since 2015.

level: national
country: IT
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-25"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - IT
  - IT-AGID
relationships:
  - type: part-of
    target: IT
    source: fact
    evidence: "dati.gov.it is a public body of IT; this anchor edge records national scope under metadata/relationship-types.md §2.3 and asserts no more than that."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: IT-AGID
    source: fact
    evidence: "Confirmed by reading dati.gov.it's own 'Chi siamo' page directly (2026-08-25): 'Dati.gov.it nasce come progetto promosso nel 2011 dal Governo italiano e dal 2015 viene gestito dall'Agenzia per l'Italia Digitale' (dati.gov.it began as a project promoted in 2011 by the Italian Government and has been managed by AgID since 2015), and 'L'attività di pubblicazione e di aggiornamento dei dataset del portale è frutto di un processo collaborativo coordinato dall'Agenzia per l'Italia Digitale' (publication and updating of the portal's datasets is coordinated by AgID). This is a new relationship this pass — the entity previously asserted no custodian edge at all."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "dati.gov.it - Portale dei dati aperti della Pubblica Amministrazione"
    url: "https://www.dati.gov.it/"
    publisher: "Agenzia per l'Italia Digitale (AgID)"
    accessed: "2026-08-25"
  - title: "Chi siamo - dati.gov.it"
    url: "https://www.dati.gov.it/chi-siamo"
    publisher: "Agenzia per l'Italia Digitale (AgID)"
    accessed: "2026-08-25"
---

# dati.gov.it

> **Verified 2026-08-25, and the custodian gap closed.** Both cited
> pages were read directly. dati.gov.it's own "Chi siamo" page states
> plainly that it has been managed by [[IT-AGID]] since 2015 — a
> `maintained-by` edge this entity did not previously carry.

## Description

Italy's national open data portal, confirmed by reading its own "Chi
siamo" page directly (2026-08-25): launched in 2011 as an Italian
government project and managed by [[IT-AGID]] since 2015, under Article
9 of decreto legislativo n. 36/2006 (Italy's transposition of the EU
Directive on the re-use of public sector information).

## The portal-custodian gap, closed for Italy

The previous pass on this entity found no source that named
[[IT-AGID]] as the portal's operator, despite it being the obvious
candidate — the same call made on [[NL-DATA-OVERHEID]] and recorded in
`discovery/research-queue.md` as a general gap. Reading dati.gov.it's
own "Chi siamo" page this pass closes it for Italy specifically: "dal
2015 viene gestito dall'Agenzia per l'Italia Digitale" (managed by
AgID since 2015). [[NL-DATA-OVERHEID]]'s own gap remains open.

## Sources

Listed in frontmatter, both read directly this pass.
