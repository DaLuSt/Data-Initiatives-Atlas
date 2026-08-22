---
id: DE-UKR
type: organisation
name: Unabhängiger Kontrollrat
alternative_names:
  - UKR
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
confidence: medium
coverage: low
verification: primary-source
start_date: "2021-04-22"
end_date: null
last_verified: "2026-08-22"
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
    evidence: "Confirmed by reading de.wikipedia.org's 'Unabhängiger Kontrollrat' page (2026-08-22): the UKR was legally established on 22 April 2021 (part of a BND-Gesetz amendment implementing Bundesverfassungsgericht and Bundesverwaltungsgericht requirements) and took over its duties on 1 January 2022, with its remit being the Bundesnachrichtendienst. A pending reform (per taz.de and vorwaerts.de, not independently read) would extend this to the Bundesamt für Verfassungsschutz."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Unabhängiger Kontrollrat"
    url: "https://de.wikipedia.org/wiki/Unabh%C3%A4ngiger_Kontrollrat"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
  - title: "Gesetzentwurf der Bundesregierung: Geheimdienstkontrolle aus einer Hand"
    url: "https://taz.de/Gesetzentwurf-der-Bundesregierung/!6203671/"
    publisher: "taz — die tageszeitung"
    accessed: "2026-08-22"
  - title: "Gesetzentwurf: So sollen die Geheimdienste kontrolliert werden"
    url: "https://www.vorwaerts.de/inland/gesetzentwurf-so-sollen-die-geheimdienste-kontrolliert-werden"
    publisher: "vorwärts"
    accessed: "2026-08-22"
  - title: "Bundestag novelliert das BND-Gesetz"
    url: "https://www.bundestag.de/dokumente/textarchiv/2021/kw12-de-nachrichtendienst-830120"
    publisher: "Deutscher Bundestag"
    accessed: "2026-08-22"
---

# Unabhängiger Kontrollrat (UKR)

> **Verified 2026-08-22.** The de.wikipedia.org UKR
> article was read directly and confirmed the founding dates and the
> BND-Gesetz/UKR-Act transition below. `taz.de` and `vorwaerts.de`, on the
> pending BfV-extension bill, were not re-read this pass.

## Description

The UKR is Germany's independent, judicial-style control body for
[[DE-BND]]'s intelligence measures, sitting alongside the Bundestag's
[[DE-PKGR]] rather than replacing it.

Its independence is visible in a small procedural detail the sources do
record: it establishes its **own** rules of procedure after consulting the
Federal Chancellery, and those rules require the approval of the
[[DE-PKGR]] — the executive is consulted, the legislature approves, and
neither writes them.

## Its founding, in two steps

The UKR's origin is now sourced, not just its date. Reading the Bundestag's
2021 textarchiv article on the BND-Gesetz amendment ([[DE-BNDG]],
confirmed 2026-08-22): the Federal Constitutional Court, by decision of
**19 May 2020** (1 BvR 2835/17), found several BNDG provisions on
*Ausland-Ausland-Fernmeldeaufklärung* incompatible with Articles 5 and 10
of the Basic Law and set an end-2021 deadline for a constitutional fix. The
government's response was "ein neu einzurichtender Unabhängiger Kontrollrat
..., der die Kompetenz zur umfassenden Kontrolle der Rechtmäßigkeit der
gesamten technischen Aufklärung durch den BND erhält."

The UKR was legally established on **22 April 2021**, as part of that
BND-Gesetz amendment implementing requirements set by the
Bundesverfassungsgericht and the Bundesverwaltungsgericht. It took over its
actual oversight duties on **1 January 2022** — until the end of 2021, a
predecessor body (the *Unabhängige Gremium*, founding date not established
here) controlled the lawfulness and necessity of the BND's
Ausland-Ausland-Fernmeldeaufklärung. `start_date` is recorded as the
legal-establishment date.

## Its statutory basis is in motion

In implementing a **further** Federal Constitutional Court decision of
28 September 2022, the UKR's provisions are to be moved *out of* the
BND-Gesetz and *into* a dedicated "Gesetz über den Unabhängigen
Kontrollrat". Whether that transfer has completed was not established from
the Wikipedia article alone (it describes the plan, not a commencement
date for the new act). **No `governed-by` relationship is asserted**,
because the Atlas does not know which instrument currently governs the UKR.
Every other oversight body in this batch has one.

## ⚠ Its remit is the subject of a pending bill

The sources describe a government bill upgrading the UKR to cover
[[DE-BFV]] as well as the BND. That is a proposal, not yet read directly
this pass. Only the BND edge is asserted.

## What is asserted, and how far

Exactly one relationship: `applies-to` [[DE-BND]], now confirmed directly
by the Wikipedia article's account of the UKR's remit and history, at
`confidence: medium` — the taz.de/vorwaerts.de reporting on the pending
BfV-extension bill was not independently re-read this pass.

## Relationships

- `applies-to` [[DE-BND]] — `confidence: medium`.

## Sources

Listed in frontmatter. **Still all secondary**: an encyclopaedia entry
and two political-press reports on a draft bill. No court decision, no
statute text, no official UKR page is cited, because none was returned by
search.
