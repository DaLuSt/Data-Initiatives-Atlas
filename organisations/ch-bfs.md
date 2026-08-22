---
id: CH-BFS
type: organisation
name: Bundesamt für Statistik
alternative_names:
  - BFS
  - OFS
  - UST
  - FSO
  - Federal Statistical Office
description: >
  Switzerland's federal statistical office, responsible for official
  statistics. It also operates opendata.swiss, the central portal for open
  data of the Swiss public administration — an unusual combination among the
  statistical offices in the Atlas.

level: national
country: CH
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - CH-OPENDATA-SWISS
relationships: []

sources:
  - title: "Das Portal opendata.swiss"
    url: "https://www.bfs.admin.ch/bfs/de/home/dienstleistungen/ogd/portal.html"
    publisher: "Bundesamt für Statistik (BFS)"
    accessed: "2026-08-22"
  - title: "Open Government Data (OGD)"
    url: "https://www.bfs.admin.ch/bfs/de/home/dienstleistungen/ogd.html"
    publisher: "Bundesamt für Statistik (BFS)"
    accessed: "2026-08-22"
  - title: "The opendata.swiss portal"
    url: "https://www.bfs.admin.ch/bfs/en/home/services/ogd/portal.html"
    publisher: "Federal Statistical Office (FSO)"
    accessed: "2026-08-22"
  - title: "Office fédéral de la statistique — Accueil"
    url: "https://www.bfs.admin.ch/bfs/fr/home.html"
    publisher: "Office fédéral de la statistique (OFS)"
    accessed: "2026-08-22"
  - title: "Ufficio federale di statistica — Pagina iniziale"
    url: "https://www.bfs.admin.ch/bfs/it/home.html"
    publisher: "Ufficio federale di statistica (UST)"
    accessed: "2026-08-22"
  - title: "Bundesamt für Statistik"
    url: "https://de.wikipedia.org/wiki/Bundesamt_f%C3%BCr_Statistik"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
---

# Bundesamt für Statistik (BFS)

> **Verified 2026-08-22.** All cited pages were read directly. The
> French and Italian bfs.admin.ch homepages turned out to be
> JavaScript-driven dashboards with almost no static body text — the
> OFS/UST abbreviations they carry in their `<title>` tags do not appear
> in readable page content, so de.wikipedia.org's Bundesamt für Statistik
> article (whose infobox states BFS, OFS, UST, UFS and FSO together) was
> added as the actual source for those abbreviations, along with FSO
> itself, which the original entity did not carry. A finding worth
> flagging: the OGD office at BFS explicitly ties its operation of
> opendata.swiss to [[CH-EMBAG]]'s legal mandate — see [[CH-EMBAG]] and
> [[CH-OPENDATA-SWISS]] for the new `governed-by` edge this produced.

## Description

Confirmed by reading bfs.admin.ch directly (2026-08-22): "Die
Geschäftsstelle OGD, die beim Bundesamt für Statistik angesiedelt ist ...
betreibt ... das Portal opendata.swiss." The BFS is Switzerland's federal statistical office. It **operates
[[CH-OPENDATA-SWISS]]**, the central portal for open data of the Swiss
public administration, through the OGD office housed within it.

## A statistical office that runs the national open data portal

That combination is not the norm in this Atlas. Elsewhere the national
portal sits with a digital-government body or a dedicated operator, and the
statistical office is a separate participant:

| Country | Open data portal | Run by |
|---|---|---|
| **Switzerland** | [[CH-OPENDATA-SWISS]] | **the statistical office** |
| Netherlands | [[NL-DATA-OVERHEID]] | *no custodian modelled* |
| Germany | [[DE-GOVDATA]] | under [[DE-FITKO]]'s roof |
| Spain | [[ES-DATOS-GOB-ES]] | *no custodian modelled* |
| United Kingdom | [[GB-DATA-GOV-UK]] | — |

Statistics and open data are adjacent but distinct functions, and Swiss
practice fuses them at the office level.

## No `maintained-by` edge is asserted here

The edge is asserted on [[CH-OPENDATA-SWISS]], pointing at this entity —
the Atlas never mirrors a relationship onto both ends, and `maintained-by`
means *the target maintains the subject*.

## Not modelled

- The **Bundesstatistikgesetz**, the federal statistics act.
- Any relationship to [[EU-ESS]] or [[UN-CES]]. Switzerland is outside the
  Union and the EEA; whether the BFS participates in European or UN
  statistical cooperation, and on what basis, was not researched. Compare
  [[NO-SSB]], where the same question is open for different reasons, and
  [[GB-ONS]], which reaches [[UN-CES]] directly.
- The **cantonal statistical offices**.

## Sources

Listed in frontmatter — all federal, all read directly this pass. The
French and Italian homepages were added to confirm the OFS and UST
abbreviations.
