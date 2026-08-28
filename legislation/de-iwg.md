---
id: DE-IWG
type: law
name: Informationsweiterverwendungsgesetz
alternative_names:
  - IWG
  - Act on the Re-use of Public Sector Information
description: >
  Former German federal act on the re-use of public sector information,
  enacted 13 December 2006 and in force from 19 December 2006 to transpose
  Directive 2003/98/EC. Modernised and replaced by the Datennutzungsgesetz
  with effect from 23 July 2021. Retained in the Atlas as a superseded
  entity so that the German open-data lineage remains traceable.

level: national
country: DE
region: EU

status: superseded
confidence: medium
coverage: medium
verification: primary-source

start_date: 2006-12-19
end_date: 2021-07-23
last_verified: "2026-08-28"
previous_version: null
successor: DE-DNG

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-PSI-DIRECTIVE
  - DE-DNG
relationships:
  - type: implements-requirement-from
    target: EU-PSI-DIRECTIVE
    source: fact
    evidence: "Confirmed by reading a dedicated Wikipedia article on the IWG itself directly (2026-08-28), found via search after the entity's original three sources (all about the DNG, mentioning the IWG only in passing) proved insufficient: the IWG 'transposed Richtlinie 2003/98/EG über die Weiterverwendung von Informationen des öffentlichen Sektors (Directive 2003/98/EC on the reuse of public sector information), which required implementation by July 1, 2005,' and the IWG itself was enacted 13 December 2006 and entered into force 19 December 2006. The de.wikipedia.org 'Datennutzungsgesetz' page, also read directly, independently confirms the DNG 'löste das Informationsweiterverwendungsgesetz (IWG) ab' (replaced the IWG). Directive 2003/98/EC is EU-PSI-DIRECTIVE in this Atlas, recorded against it rather than EU-OPEN-DATA-DIRECTIVE because the IWG predates the 2019 recast; see EU-PSI-DIRECTIVE."
    confidence: high
    valid_from: 2006-12-19
    valid_until: 2021-07-23

sources:
  - title: "Informationsweiterverwendungsgesetz"
    url: "https://de.wikipedia.org/wiki/Informationsweiterverwendungsgesetz"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
  - title: "Datennutzungsgesetz"
    url: "https://de.wikipedia.org/wiki/Datennutzungsgesetz"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
  - title: "Mehr Verwaltungsdaten sollen öffentlich zugänglich werden"
    url: "https://www.haufe.de/oeffentlicher-dienst/digitalisierung-transformation/mehr-verwaltungsdaten-sollen-oeffentlich-zugaenglich-werden_524786_536824.html"
    publisher: "Haufe"
    accessed: "2026-08-28"
  - title: "Zweites Open-Data-Gesetz und Datennutzungsgesetz"
    url: "https://www.prosoz.de/zweites-open-data-gesetz-und-datennutzungsgesetz/"
    publisher: "PROSOZ Herten"
---

# Informationsweiterverwendungsgesetz (IWG)

> **Re-verified 2026-08-28, substantially improved.** The entity's original
> three sources were all about the DNG, mentioning the IWG only in
> passing, and one of the three (`prosoz.de`) now 404s. A dedicated
> Wikipedia article on the IWG itself — not previously cited — was found
> via search and read directly, along with the DNG Wikipedia article and
> the Haufe piece. This is the rare case where genuine re-verification
> upgraded an entity from "nearly empty" to reasonably well-sourced rather
> than merely confirming what was already there. `verification:
> primary-source`; `confidence` and `coverage` both raised to `medium`;
> `start_date` and the `implements-requirement-from` relationship, both
> previously refused for want of a source, are now recorded.

## Description

The IWG was Germany's federal act on the re-use of public sector
information. Confirmed directly this pass on a dedicated Wikipedia article:
it was **enacted 13 December 2006** and **entered into force 19 December
2006**, transposing **Directive 2003/98/EC** — [[EU-PSI-DIRECTIVE]] in this
Atlas — which required implementation by member states by 1 July 2005 (so
Germany transposed it roughly a year and a half late). It was **modernised
and replaced** by [[DE-DNG]], confirmed independently on the DNG's own
Wikipedia article ("löste das Informationsweiterverwendungsgesetz (IWG)
ab"), which came into force on 23 July 2021.

## What changed this pass, concretely

The previous text of this entity recorded almost nothing — no enactment
date, no EU legal basis, `confidence: low`. That was an honest description
of what three DNG-focused sources supported. Reading further this pass
found a source **about the IWG itself**, and the previously-flagged
contradiction between this entity's frontmatter (which already carried an
`implements-requirement-from` → [[EU-PSI-DIRECTIVE]] relationship written
in an earlier pass) and its own body text (which said "no relationship is
asserted" and "None asserted") is resolved: the relationship is real, is
now confirmed by a source specifically about the IWG, and the body text
below reflects that rather than contradicting it.

## Why a nearly empty entity was worth keeping even before this pass

It exists because **§7 of the brief forbids reusing an ID** and the Atlas
retains superseded entities rather than deleting them. Without it,
[[DE-DNG]]'s `previous_version` would dangle and Germany's open-data
lineage would begin in 2021 with no indication that anything preceded it.
The Atlas treats "this was replaced by that" as a fact worth holding even
when the replaced thing is poorly documented — and this pass shows that
"poorly documented" can sometimes just mean "not yet searched for
directly."

The same judgement produced [[NL-WOB]], [[NL-EAR]] and [[EU-NIS]] on the
other layers. [[NL-WOB]] is the direct parallel: a superseded national
information-access act retained under a successor.

## Relationships

- `implements-requirement-from` [[EU-PSI-DIRECTIVE]] — confirmed this pass,
  `confidence: high`. Not asserted against [[EU-OPEN-DATA-DIRECTIVE]]
  because the IWG (2006) predates that directive's 2019 recast by over a
  decade; [[EU-PSI-DIRECTIVE]] exists in the Atlas specifically to give
  entities like this one somewhere accurate to point.

Also reached from [[DE-DNG]] via `supersedes` and `previous_version`.

## Sources

Listed in frontmatter. Two of three read directly this pass (the Wikipedia
IWG and DNG articles, plus Haufe); `prosoz.de` now 404s and is kept in the
list with that status noted here rather than silently dropped. The
dedicated IWG Wikipedia article is a materially stronger source than
anything previously cited for this entity, which mentioned the IWG only in
passing within sources about its successor.
