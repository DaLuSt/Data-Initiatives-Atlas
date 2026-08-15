---
id: DE-GEOZG
type: law
name: Geodatenzugangsgesetz
alternative_names:
  - GeoZG
  - Gesetz über den Zugang zu digitalen Geodaten
  - German Spatial Data Access Act
description: >
  German federal act of 10 February 2009 on access to digital spatial data.
  It provides the legal basis both for building a national spatial data
  infrastructure and for implementing the INSPIRE Directive at federal
  level; together with the corresponding acts of the individual Länder it
  constitutes Germany's transposition of the directive.

level: national
country: DE
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2009-02-10
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GEOSPATIAL
organisations: []
related_entities:
  - EU-INSPIRE
  - DE-GDI-DE
relationships:
  - type: implements-requirement-from
    target: EU-INSPIRE
    source: fact
    evidence: "The Geodatenzugangsgesetz of 10 February 2009 forms the legal basis both for building a national spatial data infrastructure and for implementing the INSPIRE directive at federal level; with the federal GeoZG and the acts of the individual Länder, Germany transposed the directive into national law (mik.brandenburg.de; gdi.bayern.de/gdiby/gesetze; geoportal.rlp.de 'Rechtliche Grundlage'). NOT READ — search-only."
    confidence: medium
    valid_from: 2009-02-10
    valid_until: null

sources:
  - title: "Geodateninfrastruktur Deutschland"
    url: "https://mik.brandenburg.de/mik/de/themen/vermessung-geoinformation-grundstueckswerte/fachthemen/geodateninfrastruktur/geodateninfrastruktur-deutschland/"
    publisher: "Ministerium des Innern und für Kommunales des Landes Brandenburg"
  - title: "GDI Bayern — Gesetze"
    url: "https://www.gdi.bayern.de/gdiby/gesetze/"
    publisher: "Geodateninfrastruktur Bayern"
  - title: "Rechtliche Grundlage — Geoportal RLP"
    url: "https://www.geoportal.rlp.de/mediawiki/index.php/Rechtliche_Grundlage"
    publisher: "Geoportal Rheinland-Pfalz"
  - title: "INSPIRE Umsetzung | Geodateninfrastruktur Deutschland"
    url: "https://www.gdi-de.org/en/praxis-projekte/inspire-umsetzung"
    publisher: "Geodateninfrastruktur Deutschland (GDI-DE)"
---

# Geodatenzugangsgesetz (GeoZG)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The GeoZG dates from **10 February 2009**. It provides the legal basis for
two things at once:

1. building a **national spatial data infrastructure** — [[DE-GDI-DE]];
2. **implementing [[EU-INSPIRE]] at federal level**.

Germany's transposition of the directive is not this act alone. It is the
federal GeoZG **together with the corresponding acts of the sixteen
Länder** — an arrangement the sources state explicitly and which the Atlas
can only partly represent.

## The clearest illustration of the federal modelling gap

Every German entity in this batch that touches the Bund-Länder relationship
loses information, but this one loses it most concretely and most
measurably.

The sourced fact is: *Germany transposed INSPIRE through the federal GeoZG
**and** sixteen Land acts.* What the Atlas records is: *one federal act
implements the directive.* Sixteen instruments that are jointly necessary
to the transposition are simply not representable, because the `level`
vocabulary has no term for a Land and inventing one for Germany alone would
be the country-specific ontology change the model exists to prevent.

Two of the four sources cited here are themselves **Land** geoportals —
Brandenburg's interior ministry and Bavaria's and Rhineland-Palatinate's
spatial data portals. The Atlas is citing the Länder while being unable to
model them.

This is the second country's most useful negative finding, and it is
recorded in `countries/de/de.md`, [[DE-KOSIT]] and
`discovery/unresolved.md` as an open ontology question. It is a genuine
limitation, and it would matter for any federal state added later —
Austria, Belgium, Spain, Switzerland.

## Relationships

- Implements requirements from [[EU-INSPIRE]].

This is the **fourth** EU→DE legislative chain in the Atlas, alongside
[[EU-GDPR]] → [[DE-BDSG]], [[EU-NIS2]] → [[DE-NIS2UMSUCG]] and
[[EU-OPEN-DATA-DIRECTIVE]] → [[DE-DNG]].

## Sources

Listed in frontmatter. **No statutory text is cited** — no
Gesetze-im-Internet URL for the GeoZG was returned by search — so the
10 February 2009 date and the act's content rest on Land government
descriptions rather than on the law itself.
