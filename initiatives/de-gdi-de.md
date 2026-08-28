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
  infrastructure under INSPIRE, is governed by the Lenkungsgremium GDI-DE
  (supported by a coordination office at the Bundesamt für Kartographie und
  Geodäsie in Frankfurt am Main), and rests on an administrative agreement
  between the federation and all Länder dated 5 December 2017 and in force
  since 1 January 2018.

level: national
country: DE
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-28"
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
    evidence: "Confirmed by reading gdi-de.org's own page, mik.brandenburg.de and lvermgeo.sachsen-anhalt.de directly (2026-08-28): gdi-de.org's own page states INSPIRE's rules on geodata interoperability 'have been in effect since 28.12.2010' and that GDI-DE provides the German structure for compliance; lvermgeo.sachsen-anhalt.de confirms the Lenkungsgremium GDI-DE 'steers and coordinates' GDI-DE development and INSPIRE compliance; mik.brandenburg.de confirms the current Verwaltungsvereinbarung governs both GDI-DE's expansion and its integration with the European INSPIRE framework."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: DE-GEOZG
    source: fact
    evidence: "Confirmed by reading lvermgeo.sachsen-anhalt.de directly (2026-08-28): 'The Geodata Access Act (GeoZG) from February 10, 2009, establishes the legal foundation for both the national geodata infrastructure and INSPIRE directive implementation at the federal level.' de.wikipedia.org, also read directly, confirms the federal government and the individual Länder each enacted Geodatenzugangsgesetze/Geodateninfrastrukturgesetze to fulfil the same requirement."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "INSPIRE Umsetzung | Geodateninfrastruktur Deutschland"
    url: "https://www.gdi-de.org/en/praxis-projekte/inspire-umsetzung"
    publisher: "Geodateninfrastruktur Deutschland (GDI-DE)"
    accessed: "2026-08-28"
  - title: "GDI-DE — Geodateninfrastruktur Deutschland"
    url: "https://www.lvermgeo.sachsen-anhalt.de/de/gdp-gdi-deutschland.html"
    publisher: "Landesamt für Vermessung und Geoinformation Sachsen-Anhalt"
    accessed: "2026-08-28"
  - title: "Geodateninfrastruktur Deutschland"
    url: "https://mik.brandenburg.de/mik/de/themen/vermessung-geoinformation-grundstueckswerte/fachthemen/geodateninfrastruktur/geodateninfrastruktur-deutschland/"
    publisher: "Ministerium des Innern und für Kommunales des Landes Brandenburg"
    accessed: "2026-08-28"
  - title: "Geodateninfrastruktur"
    url: "https://de.wikipedia.org/wiki/Geodateninfrastruktur"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
---

# Geodateninfrastruktur Deutschland (GDI-DE)

> **Re-verified 2026-08-28.** All four cited pages read directly (one,
> `mik.brandenburg.de`, returned a transient HTTP 503 on the first attempt
> and loaded correctly on retry, matching the batch guidance that a single
> 503 on a known German-government domain is often transient rather than a
> genuine block). `verification: primary-source`.

## Description

The GDI-DE is a **joint undertaking of the Bund, the Länder and the
Kommunen** whose aim is to make spatial data from different administrative
levels available across state and departmental boundaries through
standardised services. It is at the same time **Germany's contribution to
creating a spatial data infrastructure in the European Community** under
[[EU-INSPIRE]] — confirmed directly this pass on gdi-de.org's own page,
which states INSPIRE's interoperability rules "have been in effect since
28.12.2010."

Its governance and legal basis, now more precisely dated than before:

- The **Lenkungsgremium GDI-DE** steers and coordinates the development and
  further development of the GDI-DE, including INSPIRE compliance —
  confirmed directly this pass, with membership from the federal
  government, all sixteen Länder and three municipal associations, plus
  advisory participation from business and science. A **Koordinierungsstelle**
  (coordination office) housed at the **Bundesamt für Kartographie und
  Geodäsie (BKG) in Frankfurt am Main** — newly confirmed this pass and not
  previously recorded — executes its decisions.
- The current **Verwaltungsvereinbarung (VV GDI-DE)** between the Bund and
  the Länder governs its build-out and operation. It was signed by the Bund
  and all Länder, **dated 5 December 2017** per mik.brandenburg.de (read
  directly), and **entered into force on 1 January 2018** per
  lvermgeo.sachsen-anhalt.de (also read directly) — both dates are kept, as
  they plausibly describe signature and entry-into-force separately rather
  than conflicting.
- [[DE-GEOZG]] is the statutory basis, confirmed directly this pass.

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
reachable only from this one. The same applies to the newly-confirmed
Koordinierungsstelle at the BKG.

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

- `implements` [[EU-INSPIRE]] — confirmed directly this pass, `confidence:
  high`.
- `governed-by` [[DE-GEOZG]] — confirmed directly this pass, `confidence:
  high`.

Note the type contrast with [[DE-GEOZG]], which
`implements-requirement-from` the same directive. That is intentional:
`implements-requirement-from` is reserved for **legal instruments
transposing obligations**, while `implements` covers a programme putting a
policy into effect. One directive, two German responses, two relationship
types.

## Sources

Listed in frontmatter — including two Land authorities, which is again the
Atlas citing the Länder while unable to model them (see [[DE-GEOZG]]). All
four read directly this pass.
