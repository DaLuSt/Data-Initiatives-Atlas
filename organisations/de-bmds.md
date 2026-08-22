---
id: DE-BMDS
type: organisation
name: Bundesministerium für Digitales und Staatsmodernisierung
alternative_names:
  - BMDS
  - Digitalministerium
description: >
  German federal ministry for digital affairs and state modernisation,
  established on 6 May 2025. It bundles competences previously spread
  across six departments, including the Federal Chancellery, the Federal
  Ministry of the Interior, the Federal Ministry for Economic Affairs and
  the Federal Ministry of Justice, and leads the federal modernisation
  agenda and the Deutschland-Stack.

level: national
country: DE
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: 2025-05-06
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - DE-BMI
relationships:
  - type: produces
    target: DE-MODERNISIERUNGSAGENDA-BUND
    source: fact
    evidence: "Confirmed by reading bmds.bund.de's 'Modernisierungsagenda Bund' page (2026-08-22): 'Mit der am 1. Oktober 2025 vom Bundeskabinett beschlossenen \"Modernisierungsagenda – für Staat und Verwaltung (Bund)\" hat die Bundesregierung einen Rahmen geschaffen', published and steered under the BMDS's own domain."
    confidence: medium
    valid_from: 2025-10-01
    valid_until: null
  - type: produces
    target: DE-DEUTSCHLAND-STACK
    source: fact
    evidence: "Confirmed by reading bmds.bund.de's 'Deutschland-Stack' page (2026-08-22), which is published and maintained under the BMDS's own domain and describes the Stack as driven by the ministry toward sovereign, interoperable digital components for Bund, Länder and Kommunen by 2028."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Amtsübergabe an den neuen Bundesdigitalminister"
    url: "https://bmds.bund.de/aktuelles/aktuelle-meldungen/detail/amtsuebergabe-an-den-neuen-bundesdigitalminister"
    publisher: "Bundesministerium für Digitales und Staatsmodernisierung (BMDS)"
    accessed: "2026-08-22"
  - title: "Staatsmodernisierung: Bürokratie abbauen, Wirtschaft stärken"
    url: "https://bmds.bund.de/themen/staatsmodernisierung"
    publisher: "Bundesministerium für Digitales und Staatsmodernisierung (BMDS)"
  - title: "Bundesministerium für Digitales und Staatsmodernisierung"
    url: "https://de.wikipedia.org/wiki/Bundesministerium_f%C3%BCr_Digitales_und_Staatsmodernisierung"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
  - title: "Das neue Digitalministerium: Struktur, Aufgaben und Ziele"
    url: "https://www.smartcountry.berlin/de/newsblog/das-neue-digitalministerium-struktur-aufgaben-und-ziele.html"
    publisher: "Smart Country Convention"
    accessed: "2026-08-22"
  - title: "Neues Digitalministerium: So will Schwarz-Rot das Land digitalisieren"
    url: "https://netzpolitik.org/2025/neues-digitalministerium-so-will-schwarz-rot-das-land-digitalisieren/"
    publisher: "netzpolitik.org"
    accessed: "2026-08-22"
---

# Bundesministerium für Digitales und Staatsmodernisierung (BMDS)

> **Verified 2026-08-22.** The BMDS's own "Amtsübergabe" announcement page
> was read directly and confirmed the establishment date and personnel
> named below.

## Description

Confirmed directly on bmds.bund.de's "Amtsübergabe an den neuen
Bundesdigitalminister" page (2026-08-22): "Mit Wirkung zum 6. Mai 2025 hat
Dr. Karsten Wildberger das Amt des Bundesministers für Digitales und
Staatsmodernisierung (BMDS) übernommen." The BMDS was **established on 6
May 2025** as Germany's dedicated digital
ministry. It bundles competences from six existing departments, among them
the Federal Chancellery, the Bundesministerium des Innern ([[DE-BMI]]), the
Federal Ministry for Economic Affairs and the Federal Ministry of Justice.

As of 12 August 2025 its departments were reported as **S** (Service),
**DS** (Deutschland-Stack for digital administration), **DI** (Digital
Infrastructures) and **L** (Communication and Strategy). The DS department
carries [[DE-DEUTSCHLAND-STACK]].

It is the German counterpart in role to the Dutch
[[NL-BZK]] as the ministry owning central government digitalisation,
though **no source connects them** and no relationship is asserted.

## A ministry that reorganised the layer around it

The BMDS's creation matters for the Atlas beyond its own entity, because it
invalidates part of the context of older German entities:

- [[DE-DATENSTRATEGIE]] (2023) was presented jointly by the BMDV, the BMWK
  and [[DE-BMI]]. **The BMDV no longer exists in that form** — its digital
  competences moved here.
- [[DE-BUNDID]] is now operated by the BMDS, though its legal basis
  ([[DE-OZG]]) was a BMI instrument.

This is a case the Atlas's temporal model handles only partially. The BMDS
is not recorded as a `successor` to the BMDV, because the BMDV is not an
Atlas entity and because a ministry that absorbs competences from six
departments is not the successor of any one of them. Recorded in
`discovery/unresolved.md`.

## Personnel

The sources name Dr. Karsten Wildberger as the first minister, taking
office 6 May 2025, supported by State Secretary Markus Richter and
Parliamentary State Secretaries Philipp Amthor and Thomas Jarzombek — all
confirmed by name on the "Amtsübergabe" page at the time of the handover.
The BMDS's current organisation page, read the same day, lists Thomas
Jarzombek alongside a different second Parliamentary State Secretary (Gitta
Connemann) rather than Amthor — exactly the kind of drift this section
warns about, and left unedited below rather than "corrected" to a snapshot
that will itself be stale by the next re-verification.

**Named office-holders are not modelled as Atlas entities.** They are
recorded here as prose because they date the entity, not because the Atlas
tracks people. This is deliberate: personnel change far faster than the
Atlas is re-verified, and an unverifiable person entity would age worse
than anything else in the repository.

## Relationships

- Produces [[DE-MODERNISIERUNGSAGENDA-BUND]] and [[DE-DEUTSCHLAND-STACK]].

**No `part-of` link to [[DE]] is asserted**, and this is a convention, not
an oversight. [[EU-COMMISSION]] is `part-of` [[EU]] and the UN agencies are
`part-of` [[UN]], but no Dutch organisation is `part-of` [[NL]]. Batch 11
examined the asymmetry and judged it correct: a country anchor is the place
law *applies in*, not a body that institutions belong to, and every German
organisation already carries `country: DE`. Germany follows the Netherlands
here rather than inventing a third pattern — which is exactly the kind of
drift a second country exists to catch.

## Sources

Listed in frontmatter. Three of the five are secondary (Wikipedia, a
conference newsroom, netzpolitik.org); the two BMDS pages are primary in
kind, though unread like everything else here.
