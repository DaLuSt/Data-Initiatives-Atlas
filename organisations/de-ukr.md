---
id: DE-UKR
type: organisation
name: Unabhängiger Kontrollrat
alternative_names:
  - UKR
  - Independent Control Council
description: >
  Independent German body exercising judicial-style legality control over
  the Bundesnachrichtendienst's intelligence measures. It adopts its own
  rules of procedure after consulting the Federal Chancellery, with those
  rules requiring the approval of the Parlamentarisches Kontrollgremium. A
  government bill would extend its remit to the Bundesamt für
  Verfassungsschutz.

level: national
country: DE
region: EU

status: active
confidence: low
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - DE-BND
  - DE-BNDG
  - DE-PKGR
relationships:
  - type: applies-to
    target: DE-BND
    source: fact
    evidence: "The already existing Unabhängiger Kontrollrat is to be upgraded and in future be responsible not only for the Bundesnachrichtendienst but also for the Bundesamt für Verfassungsschutz — i.e. its present responsibility is for the BND; in implementing the decision of the Federal Constitutional Court of 28 September 2022, provisions regarding the Unabhängiger Kontrollrat were to be removed from the BND-Gesetz (de.wikipedia.org 'Unabhängiger Kontrollrat'; taz.de 'Gesetzentwurf der Bundesregierung: Geheimdienstkontrolle aus einer Hand'; vorwaerts.de). NOT READ — search-only."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Unabhängiger Kontrollrat"
    url: "https://de.wikipedia.org/wiki/Unabh%C3%A4ngiger_Kontrollrat"
    publisher: "Wikipedia"
  - title: "Gesetzentwurf der Bundesregierung: Geheimdienstkontrolle aus einer Hand"
    url: "https://taz.de/Gesetzentwurf-der-Bundesregierung/!6203671/"
    publisher: "taz — die tageszeitung"
  - title: "Gesetzentwurf: So sollen die Geheimdienste kontrolliert werden"
    url: "https://www.vorwaerts.de/inland/gesetzentwurf-so-sollen-die-geheimdienste-kontrolliert-werden"
    publisher: "vorwärts"
---

# Unabhängiger Kontrollrat (UKR)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`. This is the **weakest entity in the batch** — see below.

## Description

The UKR is Germany's independent, judicial-style control body for
[[DE-BND]]'s intelligence measures, sitting alongside the Bundestag's
[[DE-PKGR]] rather than replacing it.

Its independence is visible in a small procedural detail the sources do
record: it establishes its **own** rules of procedure after consulting the
Federal Chancellery, and those rules require the approval of the
[[DE-PKGR]] — the executive is consulted, the legislature approves, and
neither writes them.

## ⚠ Why `confidence: low`

Three things about this entity are unresolved, and every one of them is
load-bearing:

1. **Its statutory basis is in motion.** The sources say that, in
   implementing the Federal Constitutional Court's decision of
   **28 September 2022**, the UKR provisions were to be *removed from the
   BND-Gesetz*. Where they landed instead — a free-standing act, or another
   statute — was not established. **No `governed-by` relationship is
   asserted**, because the Atlas does not know which instrument to point at.
   Every other oversight body in this batch has one.
2. **Its remit is the subject of a pending bill.** The sources describe a
   government bill upgrading the UKR to cover [[DE-BFV]] as well as the BND.
   That is a proposal. Only the BND edge is asserted.
3. **Its founding date is unknown.** `start_date` is null.

## What is asserted, and how far

Exactly one relationship: `applies-to` [[DE-BND]], at `confidence: low`.
Even that is inferred from a sentence about what the UKR *would in future*
also cover — the phrasing establishes the present BND remit only by
implication. It is recorded as `source: fact` with the inference stated in
the evidence, rather than as `source: interpretation`, because the
underlying sentence is a factual claim in the source; but a reader treating
this edge as firm would be over-reading it.

This entity is the first German one to re-source when page retrieval is
possible, ahead of even [[DE-BDSG]].

## Relationships

- `applies-to` [[DE-BND]] — `confidence: low`.

## Sources

Listed in frontmatter. **All three are secondary**: an encyclopaedia entry
and two political-press reports on a draft bill. No court decision, no
statute text, no official UKR page is cited, because none was returned by
search.
