---
id: NL-NEN-3610
type: standard
name: NEN 3610 Basismodel voor geo-informatie
alternative_names:
  - NEN 3610
  - Basismodel Geo-informatie
description: >
  Dutch base model forming the common foundation for all geo-information
  models. It simplifies the exchange of geo-information between parties and
  information systems and supports unambiguous, meaningful reuse of that
  information. Published as a NEN standard, with Geonovum as the point of
  contact for its application.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-18"
previous_version: null
successor: null

domains:
  - DOMAIN-GEOSPATIAL
organisations:
  - NL-NEN
  - NL-GEONOVUM
related_entities: []
relationships:
  - type: maintained-by
    target: NL-GEONOVUM
    source: fact
    evidence: "Confirmed by reading geonovum.nl's own NEN 3610 page directly (2026-08-27): Geonovum is the point of contact (aanspreekpunt) for applying NEN 3610 in geo-information models, advising model maintainers on conformance, semantic coordination and UML modelling — while NEN itself remains the formal standards body publishing the numbered standard. geonovum.nl's own page on mandatory and recommended standards, also read directly, confirms NEN 3610 sits in the basic geo-standards set Geonovum manages, on the government's 'pas toe of leg uit' (comply or explain) list, meaning government bodies are required to apply it or justify deviation. NARROWED 2026-09-18 (discovery/unresolved.md row #136): NEN's own news page announcing the 2022 revision, read directly, confirms NEN publishes the standard ('NEN publiceert nieuwe versie basismodel geo-informatie') and that it is revised by a working group of NEN's own 'Geo-informatie' normcommissie together with experts from Geonovum, Kadaster and Rijkswaterstaat — Geonovum contributes as one of three named expert bodies to a NEN-run committee, not as sole maintainer or exclusive point of contact. `maintained-by` NL-NEN would be the formally precise edge; kept on NL-GEONOVUM because that is the narrower, still-true claim this entity's sources directly support (advising on application), and NEN's own publishing role is now recorded in prose instead."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "NEN 3610 basismodel voor informatiemodellen"
    url: "https://www.geonovum.nl/geo-standaarden/nen-3610-basismodel-voor-informatiemodellen"
    publisher: "Geonovum"
    accessed: "2026-08-27"
  - title: "NEN 3610 Linked Data Profiel (confirmed dead, HTTP 404)"
    url: "https://docs.geostandaarden.nl/nen3610/cv-st-nldp-20190715/"
    publisher: "Geonovum"
  - title: "Verplichte en aanbevolen standaarden"
    url: "https://www.geonovum.nl/themas/standaardisatie/verplicht-aanbevolen"
    publisher: "Geonovum"
    accessed: "2026-08-27"
  - title: "NEN publiceert nieuwe versie basismodel geo-informatie"
    url: "https://www.nen.nl/nieuws/geotechniek/nen-publiceert-nieuwe-versie-basismodel-geo-informatie/"
    publisher: "NEN"
    accessed: "2026-09-18"
---

# NEN 3610

> **Verified 2026-08-27.** Two of three cited pages read directly. The
> Linked Data profile page returns a genuine HTTP 404 — confirmed dead, not
> merely unread — but the two Geonovum pages that were read confirm both
> the "point of contact" caveat this entity already carried and a detail it
> did not: NEN 3610 sits on the government's mandatory "pas toe of leg uit"
> standards list.
>
> **Narrowed 2026-09-18** (`discovery/unresolved.md` row #136): NEN's own
> publishing role, previously unconfirmed by any page read, is now sourced
> directly — see "The publisher question, closed" below.

## Description

NEN 3610 is the common basis for all Dutch geo-information models. Confirmed
by reading geonovum.nl's own page directly this pass: the NEN 3610:2022
Basismodel Geo-informatie establishes semantic agreements — terminology,
definitions and relationships between spatial objects — that simplify the
exchange of geo-information between parties and information systems, and
help that information be reused unambiguously and meaningfully. It sits in
the **basic geo-standards set** on the Dutch government's "pas toe of leg
uit" (comply or explain) list, meaning government organisations are, in
principle, required to apply it. A Linked Data profile of NEN 3610 is
referenced in the sources but its page returned a genuine HTTP 404 this
pass, so its content was not confirmed.

## A divided-custody caveat, now slightly better evidenced

The `maintained-by` relationship to [[NL-GEONOVUM]] is recorded at
`confidence: medium`. The sourced statement remains narrower than the
relationship type implies: Geonovum is described, in its own words read
directly, as the *aanspreekpunt* (point of contact) for applying NEN 3610
in geo-information models — advising on conformance, semantic coordination
between models and UML modelling — which is not the same as owning or
publishing the standard.

## The publisher question, closed — 2026-09-18

As a NEN-numbered standard it is published by [[NL-NEN]] — previously a
fact not confirmed by any page read. NEN's own news page announcing the
2022 revision, read directly, confirms it: *"NEN publiceert nieuwe versie
basismodel geo-informatie"* (NEN publishes new version of the basic model
for geo-information). The same page names the actual working group
behind the revision: *"Een werkgroep van leden van de normcommissie
'Geo-informatie' en experts van Geonovum, het Kadaster en
Rijkswaterstaat, heeft de norm herzien"* (a working group of members of
the "Geo-information" standards committee, and experts from Geonovum,
the Cadastre and Rijkswaterstaat, revised the standard).

This sharpens rather than resolves the custody split: NEN runs the
standing committee and publishes the standard; Geonovum is one of three
named expert contributors to a specific revision, alongside Kadaster and
Rijkswaterstaat — a real role, but narrower than "maintainer," and
consistent with Geonovum's own "point of contact for application" framing
rather than contradicting it. The `maintained-by` edge stays on
[[NL-GEONOVUM]] because that is the claim this entity's own sources
directly support; NEN's publishing role is recorded here in prose rather
than as a second `maintained-by` edge, since the Atlas gives each register
one such edge by convention.

## Relationships

- Point of contact for application: [[NL-GEONOVUM]].
- Published as a NEN standard by [[NL-NEN]] (association recorded in
  `organisations:`; no relationship asserted, as the publishing arrangement
  was not sourced).

## Sources

Listed in frontmatter. Two of the original three read directly in the
2026-08-27 pass — Geonovum's own NEN 3610 page and its
mandatory/recommended standards page (the Linked Data profile page is
confirmed genuinely dead, HTTP 404, not merely unread). NEN's own news
page on the 2022 revision, added and read directly 2026-09-18, closes
the publisher question.
