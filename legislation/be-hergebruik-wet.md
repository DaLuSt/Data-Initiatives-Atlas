---
id: BE-HERGEBRUIK-WET
type: law
name: Wet inzake het hergebruik van overheidsinformatie
alternative_names:
  - Wet van 4 mei 2016
  - Loi du 4 mai 2016 relative à la réutilisation des informations du secteur public
  - Belgian PSI Re-use Act
description: >
  Belgian federal act of 4 May 2016 on open data and the re-use of public
  sector information, described as the regulatory framework for open data
  in Belgium and as aligned with the European PSI Directive on the re-use of
  public sector information.

level: national
country: BE
region: EU

status: active
confidence: low
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - BE-DATA-GOV-BE
  - EU-OPEN-DATA-DIRECTIVE
relationships: []

sources:
  - title: "Wet van 04/05/2016 inzake het hergebruik van overheidsinformatie"
    url: "https://etaamb.openjustice.be/nl/wet-van-04-mei-2016_n2016009236.html"
    publisher: "etaamb / OpenJustice"
  - title: "Wet van 4 mei 2016 inzake het hergebruik van overheidsinformatie (Belgisch Staatsblad)"
    url: "https://www.ejustice.just.fgov.be/cgi_loi/change_lg.pl?language=nl&la=N&table_name=wet&cn=2016050417"
    publisher: "Belgisch Staatsblad / Moniteur belge (FOD Justitie)"
  - title: "De Algemene Directie Statistiek van de FOD Economie gaat voor Open Data"
    url: "https://news.belgium.be/nl/de-algemene-directie-statistiek-van-de-fod-economie-gaat-voor-open-data"
    publisher: "news.belgium.be (Belgian federal government)"
  - title: "Hergebruik van overheidsdata"
    url: "https://www.bipt.be/operatoren/hergebruik-van-overheidsdata"
    publisher: "BIPT (Belgisch Instituut voor postdiensten en telecommunicatie)"
---

# Wet van 4 mei 2016 (re-use of public sector information)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The act of **4 May 2016** governs open data and the re-use of public sector
information at Belgian federal level. Sources describe it as *the*
regulatory framework for open data in Belgium, and as aligned with the
European **PSI Directive** on the re-use of public sector information —
whose stated aims are to improve knowledge, develop the potential of
information, and contribute to economic growth and job creation.

## ⚠ This does not connect to [[EU-OPEN-DATA-DIRECTIVE]], and the gap is real

The obvious move would be `implements-requirement-from` →
[[EU-OPEN-DATA-DIRECTIVE]], matching [[NL-WHO]] and [[DE-DNG]]. **It is
refused, and not merely for want of a source — the chronology rules it
out.**

- This act is from **2016**.
- [[EU-OPEN-DATA-DIRECTIVE]] is Directive (EU) **2019**/1024.

A 2016 act cannot transpose a 2019 directive. What the sources actually say
is that it aligns with the **PSI Directive** — Directive 2003/98/EC as
amended by 2013/37/EU — which the Open Data Directive later recast, and
which is **not an Atlas entity**.

So Belgium's position differs from its two neighbours:

| Country | Open Data Directive transposition |
|---|---|
| Netherlands | [[NL-WHO]] — recorded |
| Germany | [[DE-DNG]] — recorded |
| Belgium | **not established** |

Belgium will have transposed Directive 2019/1024 — every member state was
required to by July 2021 — but **no source read identifies the instrument**,
and this 2016 act is not it. Recording this act as the transposition would
be a plausible-looking error that survives review precisely because it
looks like the pattern the other two countries set.

This is the sharpest case in the batch of the pattern-matching trap: the
shape of the Atlas made a wrong answer attractive. Both the missing Belgian
transposition and the unmodelled PSI Directive are logged in
`discovery/research-queue.md`.

`confidence: low` and `coverage: low` reflect that the act's scope, its
obligations and its relationship to the current EU regime are all unknown.

## Relationships

**None asserted.** `related_entities` records the association with
[[EU-OPEN-DATA-DIRECTIVE]] for navigation only — deliberately *not* as a
relationship, for the reasons above.

## Sources

Listed in frontmatter, including the Belgisch Staatsblad entry and a
consolidated text.
