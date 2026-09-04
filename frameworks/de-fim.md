---
id: DE-FIM
type: framework
name: Föderales Informationsmanagement
alternative_names:
  - FIM
  - Federal Information Management
description: >
  German governance framework of the IT-Planungsrat, developed from 2013 and
  an official IT-Planungsrat application since 1 January 2017. It provides
  methods for standardising administrative services across the federation,
  Länder and municipalities in three building blocks — Leistungen
  (citizen-friendly service descriptions), Prozesse (standardised process
  models) and Datenfelder (uniform data fields for forms) — so that
  information created once can be reused by every authority rather than
  redefined locally.

level: national
country: DE
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2017-01-01
end_date: null
last_verified: "2026-09-04"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - DE-IT-PLANUNGSRAT
  - DE-FITKO
related_entities:
  - DE-IT-PLANUNGSRAT
  - DE-FITKO
  - DE-KOSIT
  - DE-GOVDATA
relationships:
  - type: governed-by
    target: DE-IT-PLANUNGSRAT
    source: fact
    evidence: "Confirmed by reading docs.fitko.de's own 'Kompass der föderalen IT-Architektur' page on FIM directly (2026-09-04): 'Seit dem 01.01.2017 ist FIM eine Anwendung des IT-Planungsrats' (since 1 January 2017, FIM has been an application of the IT-Planungsrat). The same page states FIM 'wurde bereits 2013 entwickelt' (was already developed in 2013), predating its formal adoption as an IT-Planungsrat application by four years, and that a 'Bundesredaktion' (federal editorial office) under BMI leadership manages federal-level content while Bund and Länder work closely together on its operation and governance."
    confidence: high
    valid_from: 2017-01-01
    valid_until: null
  - type: maintained-by
    target: DE-FITKO
    source: fact
    evidence: "Confirmed by reading docs.fitko.de's own page directly (2026-09-04): the Föderale IT-Kooperation 'coordinates the process across administration levels' for FIM. This is consistent with DE-FITKO's own entity, which lists FIM as a product under FITKO's product management alongside DE-KOSIT and DE-GOVDATA — closing the gap that entity flagged: 'nothing further about it was established even after this pass's direct reads.' docs.fitko.de's dedicated FIM documentation page, not previously found, is the source that closes it."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Föderales Informationsmanagement (FIM) — Kompass der föderalen IT-Architektur"
    url: "https://docs.fitko.de/kompass/docs/grundlagen-und-rahmen/fim/"
    publisher: "Föderale IT-Kooperation (FITKO)"
    accessed: "2026-09-04"
  - title: "FIM - Das Föderale Informationsmanagement"
    url: "https://www.digitale-verwaltung.de/Webs/DV/DE/onlinezugangsgesetz/ozg-grundlagen/fim/fim-node.html"
    publisher: "Digitale Verwaltung (Bundesministerium des Innern)"
  - title: "Föderales Informationsmanagement"
    url: "https://de.wikipedia.org/wiki/F%C3%B6derales_Informationsmanagement"
    publisher: "Wikipedia"
    accessed: "2026-09-04"
---

# Föderales Informationsmanagement (FIM)

> **Added 2026-09-04, `verification: primary-source` from creation.** A
> research-queue item flagged as **Next** since the Germany batch, and
> explicitly declined by [[DE-FITKO]]'s own re-verification pass — "FIM is
> not an entity... nothing further about it was established even after
> this pass's direct reads" — is now closed. `docs.fitko.de`, FITKO's own
> dedicated documentation site, was not found in that earlier pass; its
> "Kompass der föderalen IT-Architektur" carries a page on FIM specifically,
> read directly this pass, that supplies exactly the governance detail,
> start date and structure the earlier pass could not find.

## Description

FIM is a governance framework of the [[DE-IT-PLANUNGSRAT]] providing
"Methoden für die einheitliche Aufbereitung der Verwaltungsleistungen in
Bezug auf Prozesse, Daten und bürger-freundliche Beschreibung" — methods
for the standardised preparation of administrative services with respect
to processes, data and citizen-friendly description — confirmed by reading
`docs.fitko.de`'s own page directly. It was **developed already in 2013**,
integrating results from existing digitalisation projects into one unified
methodology, and became a **formal IT-Planungsrat application on 1 January
2017**.

## Three building blocks

Confirmed by reading `docs.fitko.de` directly, FIM is organised around
three components:

1. **Leistungen (Services)** — citizen-friendly descriptions of
   administrative services in a standardised format.
2. **Prozesse (Processes)** — descriptions of how each service is delivered
   within the responsible agency.
3. **Datenfelder (Data Fields)** — standardised data structures and formats
   for the forms and documents behind those services.

The point of standardising all three, per the same source, is that FIM
content created once by any single authority can be reused by every other
authority — "efficiently, with legal certainty, and up-to-date" — rather
than each of Germany's federal, Land and municipal authorities redefining
the same administrative service independently.

## Who runs it

Confirmed by reading `docs.fitko.de` directly: a **Bundesredaktion**
(federal editorial office) under the leadership of the Bundesministerium
des Innern manages FIM content at the federal level, while the "Föderale
IT-Kooperation" — [[DE-FITKO]] — coordinates the process across all levels
of administration, and "Bund und Länder arbeiten dabei eng zusammen"
(the federation and the Länder work closely together) on its operation.

This makes FIM one of three products FITKO manages alongside [[DE-KOSIT]]
and [[DE-GOVDATA]], as [[DE-FITKO]]'s own entity already recorded — but
until this pass, FIM itself had no Atlas entity to be `maintained-by` that
relationship.

## What remains unrecorded

`coverage: low`, deliberately. Not established by anything read this pass:
FIM's relationship to individual OZG administrative services, how many
Länder actively participate versus merely have access, and whether any
FIM-derived data field standard is itself cited elsewhere in the Atlas
(e.g. by [[DE-XRECHNUNG]] or the other XÖV standards).

## Relationships

- `governed-by` [[DE-IT-PLANUNGSRAT]] — an IT-Planungsrat application since
  1 January 2017.
- `maintained-by` [[DE-FITKO]], which coordinates FIM across administration
  levels.

## Sources

Listed in frontmatter. `docs.fitko.de`'s dedicated FIM page and Wikipedia's
article were both read directly; the `digitale-verwaltung.de` page is
listed as a source but was not fetched this pass — a prior pass on
[[DE-FITKO]] and [[DE-OZG]] found the same domain returning HTTP 400 on
every attempt, so it was not retried here.
