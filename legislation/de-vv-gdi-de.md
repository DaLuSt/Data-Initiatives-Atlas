---
id: DE-VV-GDI-DE
type: law
name: Verwaltungsvereinbarung über die Geodateninfrastruktur Deutschland
alternative_names:
  - VV GDI-DE
  - GDI-DE Administrative Agreement
description: >
  Administrative agreement (Verwaltungsvereinbarung) between the German
  federation and all sixteen Länder governing the build-out and operation
  of [[DE-GDI-DE]], the German Spatial Data Infrastructure. Signed by the
  Bund and all Länder, dated 5 December 2017, and entered into force on
  1 January 2018. One of two known Bund-Länder Verwaltungsvereinbarungen
  underpinning German digital-government infrastructure recorded in this
  Atlas, alongside [[DE-VV-GOVDATA]] — the same constitutional device used
  for two different policy areas, closing `discovery/unresolved.md` item
  #6.

level: national
country: DE
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2017-12-05
end_date: null
last_verified: "2026-09-20"
previous_version: null
successor: null

domains:
  - DOMAIN-GEOSPATIAL
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - DE-GDI-DE
  - DE-VV-GOVDATA
  - DE
relationships:
  - type: part-of
    target: DE
    source: fact
    evidence: "Confirmed via mik.brandenburg.de and lvermgeo.sachsen-anhalt.de, both read directly for [[DE-GDI-DE]]'s own file (2026-08-28): the current Verwaltungsvereinbarung (VV GDI-DE) between the Bund and all Länder governs GDI-DE's build-out and operation, signed by the Bund and all Länder, dated 5 December 2017 (per mik.brandenburg.de) and entered into force on 1 January 2018 (per lvermgeo.sachsen-anhalt.de) — both dates kept as plausibly describing signature and entry-into-force separately. Anchor edge under metadata/relationship-types.md §2.3: a binding intergovernmental agreement between the federation and all Länder, not domestic legislation in the ordinary sense, is treated as `type: law` — the same pragmatic fit already used for EEA Joint Committee Decisions ([[INTL-EEA-JCD-154-2018]] and siblings), an intergovernmental binding instrument that does not cleanly fit any other entity type either. Ontology decision closing item #6, 2026-09-20."
    confidence: medium
    valid_from: 2017-12-05
    valid_until: null

sources:
  - title: "Geodateninfrastruktur Deutschland"
    url: "https://mik.brandenburg.de/mik/de/themen/vermessung-geoinformation-grundstueckswerte/fachthemen/geodateninfrastruktur/geodateninfrastruktur-deutschland/"
    publisher: "Ministerium des Innern und für Kommunales des Landes Brandenburg"
    accessed: "2026-08-28"
  - title: "GDI-DE — Geodateninfrastruktur Deutschland"
    url: "https://www.lvermgeo.sachsen-anhalt.de/de/gdp-gdi-deutschland.html"
    publisher: "Landesamt für Vermessung und Geoinformation Sachsen-Anhalt"
    accessed: "2026-08-28"
---

# Verwaltungsvereinbarung über die Geodateninfrastruktur Deutschland (VV GDI-DE)

> **Created 2026-09-20**, closing `discovery/unresolved.md` ontology item
> #6 ("Verwaltungsvereinbarungen — should these be entities?") alongside
> [[DE-VV-GOVDATA]]. Both sources were already cited and read directly on
> [[DE-GDI-DE]]'s own file (2026-08-28); no new fetch was needed, only the
> ontology decision to give the instrument its own node.

## Description

The VV GDI-DE is the **administrative agreement between the German
federation and all sixteen Länder** that governs the build-out and
operation of [[DE-GDI-DE]], Germany's spatial data infrastructure. Two
independently-sourced dates are kept rather than reconciled into one:
**signed 5 December 2017** (mik.brandenburg.de) and **entered into force
1 January 2018** (lvermgeo.sachsen-anhalt.de) — plausibly describing
signature and entry-into-force as separate events rather than conflicting.

## Why `type: law`

Ontology item #6 flagged that "neither legislation nor policy fits" a
Bund-Länder Verwaltungsvereinbarung, and "no entity type does either." The
decision closing that item, 2026-09-20: file it as `type: law` anyway,
matching the pragmatic treatment this Atlas already gives EEA Joint
Committee Decisions (`[[INTL-EEA-JCD-154-2018]]` and siblings) — a binding
intergovernmental instrument that isn't ordinary domestic legislation
either, but for which `law` is the closest available fit and creating a
new `agreement` type for two known instances was judged unwarranted (see
`metadata/ontology.md` §6's design-decisions log). This does **not**
resolve the separate, larger legislative-rank question (ontology item
#11) of whether `type: law` should itself be split by rank — it only
decides where a Verwaltungsvereinbarung sits within the existing
vocabulary.

## The second Bund-Länder Verwaltungsvereinbarung in this Atlas

[[DE-VV-GOVDATA]] is the same constitutional device applied to a
different policy area (open data rather than spatial data) — see that
entity's own file for the parallel case, sourced independently from the
agreement's own text.

## Relationships

- `part-of` [[DE]] (anchor edge).

Inbound: [[DE-GDI-DE]] `governed-by` this entity.

## Sources

Listed in frontmatter, both already read directly for [[DE-GDI-DE]]'s own
file (2026-08-28).
