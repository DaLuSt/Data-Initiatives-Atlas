---
id: DE-VV-GOVDATA
type: law
name: Vereinbarung des Bundes und der Länder zum gemeinsamen Betrieb von "GovData - Das Datenportal für Deutschland"
alternative_names:
  - Verwaltungsvereinbarung GovData
  - VV GovData
  - GovData Administrative Agreement
description: >
  Administrative agreement (Verwaltungsvereinbarung) between the German
  federation and, originally, seven Länder, establishing joint operation
  of [[DE-GOVDATA]], Germany's central open-data portal, as a "gemeinsame
  Infrastruktur von Bund und Ländern im Sinne des Art. 91c GG" (a joint
  Bund-Länder infrastructure under Article 91c of the Basic Law). Signed
  by the Bundesministerium des Innern and the interior/finance/justice
  ministries of Baden-Württemberg, Berlin, Brandenburg, Hamburg,
  Nordrhein-Westfalen, Rheinland-Pfalz and Sachsen; entered into force
  4 December 2014 per its own §16(1), once the Bund and at least six
  Länder had signed. All sixteen Länder had acceded by the time GovData's
  own sources were read (2026-08-28), Saarland completing the set. One of
  two known Bund-Länder Verwaltungsvereinbarungen underpinning German
  digital-government infrastructure recorded in this Atlas, alongside
  [[DE-VV-GDI-DE]] — closing `discovery/unresolved.md` item #6.

level: national
country: DE
region: null

status: active
confidence: high
coverage: low
verification: primary-source

start_date: 2014-12-04
end_date: null
last_verified: "2026-09-20"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - DE-GOVDATA
  - DE-VV-GDI-DE
  - DE
relationships:
  - type: part-of
    target: DE
    source: fact
    evidence: "Confirmed by reading the agreement's own text directly (2026-09-20, govdata.de's own fileadmin PDF, 'Vereinbarung des Bundes und der Länder zum gemeinsamen Betrieb von \"GovData - Das Datenportal für Deutschland\" (Verwaltungsvereinbarung GovData)'): its opening page names the Bundesrepublik Deutschland (vertreten durch das Bundesministerium des Innern) and seven Länder — Baden-Württemberg, Berlin, Brandenburg, Hamburg, Nordrhein-Westfalen, Rheinland-Pfalz, Sachsen — as the original 'Vereinbarungspartner'; its Präambel states 'GovData stellt eine gemeinsame Infrastruktur von Bund und Ländern im Sinne des Art. 91c GG dar' (GovData constitutes a joint Bund-Länder infrastructure under Article 91c of the Basic Law). bravors.brandenburg.de's own official Bekanntmachung (also read directly, 2026-09-20) independently confirms: 'Die am 1. Dezember 2014 in Potsdam seitens des Landes Brandenburg unterzeichnete Vereinbarung... ist nach ihrem § 16 Absatz 1 Satz 1 am 4. Dezember 2014 in Kraft getreten' (entered into force 4 December 2014 per its own §16(1), once the Bund and at least six Länder had signed). Anchor edge under metadata/relationship-types.md §2.3, same `type: law` treatment as [[DE-VV-GDI-DE]] — see that entity's own file for the ontology decision closing item #6, 2026-09-20."
    confidence: high
    valid_from: 2014-12-04
    valid_until: null

sources:
  - title: "Vereinbarung des Bundes und der Länder zum gemeinsamen Betrieb von \"GovData - Das Datenportal für Deutschland\" (Verwaltungsvereinbarung GovData)"
    url: "https://www.govdata.de/fileadmin/Verwaltungsvereinbarung_GovData_finale_Fassung.pdf"
    publisher: "GovData"
    accessed: "2026-09-20"
  - title: "Bekanntmachung der Vereinbarung des Bundes und der Länder zum gemeinsamen Betrieb von \"GovData - Das Datenportal für Deutschland\""
    url: "https://bravors.brandenburg.de/verwaltungsvorschriften/govdata2014"
    publisher: "Land Brandenburg (Bravors — Brandenburgisches Vorschriftensystem)"
    accessed: "2026-09-20"
---

# Verwaltungsvereinbarung GovData

> **Created 2026-09-20**, closing `discovery/unresolved.md` ontology item
> #6 ("Verwaltungsvereinbarungen — should these be entities?") alongside
> [[DE-VV-GDI-DE]]. Sourced from the agreement's own text (govdata.de's
> own fileadmin PDF) and Brandenburg's own official Bekanntmachung, both
> read directly.

## Description

The Verwaltungsvereinbarung GovData is the administrative agreement
establishing joint Bund-Länder operation of [[DE-GOVDATA]]. Its own
Präambel, read directly, is explicit about its constitutional basis:
*"GovData stellt eine gemeinsame Infrastruktur von Bund und Ländern im
Sinne des Art. 91c GG dar"* — GovData is a joint Bund-Länder
infrastructure under **Article 91c of the Basic Law** (the provision
enabling the federation and Länder to cooperate on shared IT systems).

## Original signatories, not all sixteen at once

The agreement's own opening page names only **seven original
Vereinbarungspartner** alongside the Bund: Baden-Württemberg, Berlin,
Brandenburg, Hamburg, Nordrhein-Westfalen, Rheinland-Pfalz and Sachsen.
Brandenburg's own official Bekanntmachung, read directly, gives the exact
mechanics: the agreement's own §16(1) set entry into force once the Bund
and **at least six Länder** had signed, which happened on **4 December
2014** (Brandenburg itself signed 1 December 2014 in Potsdam). By the time
[[DE-GOVDATA]]'s own sources were read for this Atlas (2026-08-28), all
sixteen Länder had acceded, Saarland completing the set — the exact
accession date for the remaining Länder was not re-confirmed this pass and
is not asserted here.

## The first Bund-Länder Verwaltungsvereinbarung in this Atlas

[[DE-VV-GDI-DE]] is the same constitutional device applied to a different
policy area (spatial data rather than open data), created the same day —
see that entity's own file for the ontology decision (`type: law`,
closing `discovery/unresolved.md` item #6) this entity also follows.

## Relationships

- `part-of` [[DE]] (anchor edge).

Inbound: [[DE-GOVDATA]] `governed-by` this entity.

## Sources

Listed in frontmatter, both read directly this pass — the agreement's own
PDF via the local-path Read-tool workaround after WebFetch returned only
binary content, Brandenburg's Bekanntmachung directly via WebFetch.
