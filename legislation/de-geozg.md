---
id: DE-GEOZG
type: law
name: Geodatenzugangsgesetz
alternative_names:
  - GeoZG
  - Gesetz über den Zugang zu digitalen Geodaten
  - German Spatial Data Access Act
description: >
  German federal act of 10 February 2009 (published 13 February 2009 as
  BGBl. I S. 278) on access to digital spatial data. Its own preamble
  states it transposes Directive 2007/2/EC (INSPIRE) into German law. It
  provides the legal basis both for building a national spatial data
  infrastructure and for implementing the INSPIRE Directive at federal
  level; together with the corresponding acts of the individual Länder it
  constitutes Germany's transposition of the directive.

level: national
country: DE
region: EU

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: 2009-02-10
end_date: null
last_verified: "2026-08-28"
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
    evidence: "Confirmed by reading four sources directly (2026-08-28), two of them quoting the GeoZG's own statutory text: buzer.de quotes the law's preamble verbatim — 'This law serves to transpose Directive 2007/2/EG of the European Parliament and Council from March 14, 2007 regarding the establishment of a spatial data infrastructure in the European Community (INSPIRE Directive)' — and dejure.org independently confirms the enactment date (10 February 2009) and Bundesgesetzblatt citation (BGBl. I 2009 S. 278, published 13 February 2009). geoportal.rlp.de's own page and gdi.bayern.de's own page, also read directly, both state the GeoZG implements INSPIRE at federal level while the individual Länder's own geodata-infrastructure acts (e.g. Bavaria's BayGDIG, in force from 1 August 2008) implement it at Land level. The official gesetze-im-internet.de text itself returned HTTP 503 on three attempts this pass and could not be read directly; the two independent legal-database mirrors quoting its preamble and citation substitute for it."
    confidence: high
    valid_from: 2009-02-10
    valid_until: null

sources:
  - title: "Geodateninfrastruktur Deutschland"
    url: "https://mik.brandenburg.de/mik/de/themen/vermessung-geoinformation-grundstueckswerte/fachthemen/geodateninfrastruktur/geodateninfrastruktur-deutschland/"
    publisher: "Ministerium des Innern und für Kommunales des Landes Brandenburg"
    accessed: "2026-08-28"
  - title: "GDI Bayern — Gesetze"
    url: "https://www.gdi.bayern.de/gdiby/gesetze/"
    publisher: "Geodateninfrastruktur Bayern"
    accessed: "2026-08-28"
  - title: "Rechtliche Grundlage — Geoportal RLP"
    url: "https://www.geoportal.rlp.de/mediawiki/index.php/Rechtliche_Grundlage"
    publisher: "Geoportal Rheinland-Pfalz"
    accessed: "2026-08-28"
  - title: "INSPIRE Umsetzung | Geodateninfrastruktur Deutschland"
    url: "https://www.gdi-de.org/en/praxis-projekte/inspire-umsetzung"
    publisher: "Geodateninfrastruktur Deutschland (GDI-DE)"
    accessed: "2026-08-28"
  - title: "GeoZG — Gesetz über den Zugang zu digitalen Geodaten (official text)"
    url: "https://www.gesetze-im-internet.de/geozg/BJNR027800009.html"
    publisher: "Bundesministerium der Justiz (Gesetze im Internet)"
  - title: "BGBl. I 2009 S. 278 — Geodatenzugangsgesetz"
    url: "https://dejure.org/BGBl/2009/BGBl._I_S._278"
    publisher: "dejure.org"
    accessed: "2026-08-28"
  - title: "GeoZG Geodatenzugangsgesetz"
    url: "https://www.buzer.de/gesetz/8630/index.htm"
    publisher: "buzer.de"
    accessed: "2026-08-28"
---

# Geodatenzugangsgesetz (GeoZG)

> **Re-verified 2026-08-28.** All four originally-cited pages read
> directly. The official statute at `gesetze-im-internet.de`, still not
> cited before this pass, returned HTTP 503 on three attempts and could not
> be read directly this pass either — but two independent legal-database
> mirrors (`dejure.org`, `buzer.de`), both read directly, quote the law's
> own preamble and its exact Bundesgesetzblatt citation, closing most of
> the previously-flagged "no statutory text is cited" gap even without a
> successful fetch of the primary site itself. `verification:
> primary-source`; `confidence` raised to `high`.

## Description

The GeoZG dates from **10 February 2009**, published two days later on
**13 February 2009** as **BGBl. I 2009 S. 278** — confirmed directly this
pass via dejure.org's own Bundesgesetzblatt citation page. buzer.de, also
read directly, quotes the law's own preamble: "This law serves to
transpose Directive 2007/2/EG of the European Parliament and Council from
March 14, 2007 regarding the establishment of a spatial data infrastructure
in the European Community (INSPIRE Directive)" — the transposition
relationship stated in the statute's own words, not merely inferred from
government descriptions of it.

It provides the legal basis for two things at once:

1. building a **national spatial data infrastructure** — [[DE-GDI-DE]];
2. **implementing [[EU-INSPIRE]] at federal level**.

Germany's transposition of the directive is not this act alone. It is the
federal GeoZG **together with the corresponding acts of the sixteen
Länder** — confirmed directly this pass on gdi.bayern.de's own page, which
names Bavaria's own **Bayerisches Geodateninfrastrukturgesetz (BayGDIG)**,
in force since **1 August 2008** (a date not previously recorded on this
entity), as the Land-level counterpart to the federal GeoZG.

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

Three of the sources cited here are themselves **Land** geoportals or
ministries — Brandenburg's interior ministry, Bavaria's spatial data portal
and Rhineland-Palatinate's geoportal. The Atlas is citing the Länder while
being unable to model them.

This is the second country's most useful negative finding, and it is
recorded in `countries/de/index.md`, [[DE-KOSIT]] and
`discovery/unresolved.md` as an open ontology question. It is a genuine
limitation, and it would matter for any federal state added later —
Austria, Belgium, Spain, Switzerland.

## Relationships

- Implements requirements from [[EU-INSPIRE]] — confirmed directly this
  pass, `confidence: high`, now resting partly on the statute's own
  preamble text via two independent mirrors.

This is the **fourth** EU→DE legislative chain in the Atlas, alongside
[[EU-GDPR]] → [[DE-BDSG]], [[EU-NIS2]] → [[DE-NIS2UMSUCG]] and
[[EU-OPEN-DATA-DIRECTIVE]] → [[DE-DNG]].

## Sources

Listed in frontmatter. The official `gesetze-im-internet.de` text is now
cited but was not successfully fetched this pass (HTTP 503 on three
attempts, treated as a transient-but-persistent block rather than dropped
silently); `dejure.org` and `buzer.de`, both read directly, substitute by
quoting the statute's own citation and preamble text, which is a stronger
sourcing position than the Land-government descriptions this entity relied
on previously.
