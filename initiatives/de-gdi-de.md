---
id: DE-GDI-DE
type: initiative
name: Geodateninfrastruktur Deutschland
alternative_names:
  - GDI-DE
  - German Spatial Data Infrastructure
description: >
  Joint undertaking of the German federation, the Länder and the
  municipalities to make spatial data from different administrative levels
  available across state and departmental boundaries through standardised
  services. It is Germany's contribution to the European spatial data
  infrastructure under INSPIRE, is governed by the Lenkungsgremium GDI-DE,
  and rests on an administrative agreement between the federation and all
  Länder in force since 1 January 2018.

level: national
country: DE
region: EU

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
  - DOMAIN-GEOSPATIAL
organisations: []
related_entities:
  - EU-INSPIRE
  - DE-GEOZG
relationships:
  - type: implements
    target: EU-INSPIRE
    source: fact
    evidence: "The GDI-DE is Germany's contribution to creating a spatial data infrastructure in the European Community (INSPIRE); the Lenkungsgremium GDI-DE steers and coordinates the development and further development of the GDI-DE including implementation of the INSPIRE Directive (2007/2/EC) (lvermgeo.sachsen-anhalt.de; mik.brandenburg.de; gdi-de.org). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: DE-GEOZG
    source: fact
    evidence: "The Geodatenzugangsgesetz of 10 February 2009 forms the legal basis both for building a national spatial data infrastructure and for implementing the INSPIRE Directive at federal level (mik.brandenburg.de; gdi.bayern.de/gdiby/gesetze). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "INSPIRE Umsetzung | Geodateninfrastruktur Deutschland"
    url: "https://www.gdi-de.org/en/praxis-projekte/inspire-umsetzung"
    publisher: "Geodateninfrastruktur Deutschland (GDI-DE)"
  - title: "GDI-DE — Geodateninfrastruktur Deutschland"
    url: "https://www.lvermgeo.sachsen-anhalt.de/de/gdp-gdi-deutschland.html"
    publisher: "Landesamt für Vermessung und Geoinformation Sachsen-Anhalt"
  - title: "Geodateninfrastruktur Deutschland"
    url: "https://mik.brandenburg.de/mik/de/themen/vermessung-geoinformation-grundstueckswerte/fachthemen/geodateninfrastruktur/geodateninfrastruktur-deutschland/"
    publisher: "Ministerium des Innern und für Kommunales des Landes Brandenburg"
  - title: "Geodateninfrastruktur"
    url: "https://de.wikipedia.org/wiki/Geodateninfrastruktur"
    publisher: "Wikipedia"
---

# Geodateninfrastruktur Deutschland (GDI-DE)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The GDI-DE is a **joint undertaking of the Bund, the Länder and the
Kommunen** whose aim is to make spatial data from different administrative
levels available across state and departmental boundaries through
standardised services. It is at the same time **Germany's contribution to
creating a spatial data infrastructure in the European Community** under
[[EU-INSPIRE]].

Its governance and legal basis:

- The **Lenkungsgremium GDI-DE** steers and coordinates the development and
  further development of the GDI-DE, including implementation of the
  INSPIRE Directive.
- The current **Verwaltungsvereinbarung (VV GDI-DE)** between the Bund and
  the Länder governs its build-out and operation. It was signed by the Bund
  and all Länder and entered into force on **1 January 2018**.
- [[DE-GEOZG]] is the statutory basis.

## Typed `initiative`, not `organisation` or `platform`

The classification took some deciding and is recorded because a later
contributor will face the same question.

- It is **not an organisation**: the sources describe a joint project
  (gemeinschaftliches Projekt) of three levels of government, with a
  steering committee rather than a legal personality.
- It is **not a platform**: it is not a portal but an infrastructure
  programme under which portals and services are built.
- **`initiative`** fits `metadata/taxonomy.md`'s definition of a named
  effort that does not fit a more specific type.

The Lenkungsgremium GDI-DE is **not modelled as a separate organisation**,
though it arguably could be. It is a governing committee of an initiative
rather than a standing institution, and creating it would add a node
reachable only from this one.

## The second Bund-Länder Verwaltungsvereinbarung in this batch

[[DE-GOVDATA]] rests on the same kind of instrument: an administrative
agreement acceded to by the federation and all sixteen Länder. Two
different policy areas, the same constitutional device.

That recurrence is a genuine finding about German digital governance rather
than a coincidence of sourcing — where a Dutch initiative can be
established by central government decision, a German one that touches Land
competences needs an interstate agreement. **The Verwaltungsvereinbarung
itself is not modelled** in either case: it is neither legislation nor
policy in the Atlas's sense, and there is no entity type for an
intergovernmental agreement. Logged in `discovery/unresolved.md`.

## Relationships

- `implements` [[EU-INSPIRE]].
- `governed-by` [[DE-GEOZG]].

Note the type contrast with [[DE-GEOZG]], which
`implements-requirement-from` the same directive. That is intentional:
`implements-requirement-from` is reserved for **legal instruments
transposing obligations**, while `implements` covers a programme putting a
policy into effect. One directive, two German responses, two relationship
types.

## Sources

Listed in frontmatter — including two Land authorities, which is again the
Atlas citing the Länder while unable to model them (see [[DE-GEOZG]]).
