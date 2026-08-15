---
id: DE-BMDS
type: organisation
name: Bundesministerium für Digitales und Staatsmodernisierung
alternative_names:
  - BMDS
  - Federal Ministry for Digital and State Modernisation
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
verification: search-only

start_date: 2025-05-06
end_date: null
last_verified: null
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
    evidence: "The BMDS leads the steering of the Modernisierungsagenda für Staat und Verwaltung (Bund), adopted by the federal cabinet on 1 October 2025 (bmds.bund.de/themen/staatsmodernisierung/modernisierungsagenda-bund). NOT READ — search-only."
    confidence: medium
    valid_from: 2025-10-01
    valid_until: null
  - type: produces
    target: DE-DEUTSCHLAND-STACK
    source: fact
    evidence: "Implementation of the Deutschland-Stack is driven by the BMDS, with a department 'DS' established to develop it across technology, governance and policy (bmds.bund.de; netzpolitik.org). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Amtsübergabe an den neuen Bundesdigitalminister"
    url: "https://bmds.bund.de/aktuelles/aktuelle-meldungen/detail/amtsuebergabe-an-den-neuen-bundesdigitalminister"
    publisher: "Bundesministerium für Digitales und Staatsmodernisierung (BMDS)"
  - title: "Staatsmodernisierung: Bürokratie abbauen, Wirtschaft stärken"
    url: "https://bmds.bund.de/themen/staatsmodernisierung"
    publisher: "Bundesministerium für Digitales und Staatsmodernisierung (BMDS)"
  - title: "Bundesministerium für Digitales und Staatsmodernisierung"
    url: "https://de.wikipedia.org/wiki/Bundesministerium_f%C3%BCr_Digitales_und_Staatsmodernisierung"
    publisher: "Wikipedia"
  - title: "Das neue Digitalministerium: Struktur, Aufgaben und Ziele"
    url: "https://www.smartcountry.berlin/de/newsblog/das-neue-digitalministerium-struktur-aufgaben-und-ziele.html"
    publisher: "Smart Country Convention"
  - title: "Neues Digitalministerium: So will Schwarz-Rot das Land digitalisieren"
    url: "https://netzpolitik.org/2025/neues-digitalministerium-so-will-schwarz-rot-das-land-digitalisieren/"
    publisher: "netzpolitik.org"
---

# Bundesministerium für Digitales und Staatsmodernisierung (BMDS)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The BMDS was **established on 6 May 2025** as Germany's dedicated digital
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
Parliamentary State Secretaries Philipp Amthor and Thomas Jarzombek.

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
