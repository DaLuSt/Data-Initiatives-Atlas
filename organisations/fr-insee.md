---
id: FR-INSEE
type: organisation
name: Institut national de la statistique et des études économiques
alternative_names:
  - INSEE
  - Insee
  - National Institute of Statistics and Economic Studies
description: >
  France's national statistical institute, a directorate-general of the
  Ministry for the Economy and Finance, headquartered in Montrouge. It
  collects, analyses and disseminates information on the French economy and
  society across the whole French territory and carries out the periodic
  national census, operating with professional independence.

level: national
country: FR
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-ESS
  - EU-EUROSTAT
relationships:
  - type: part-of
    target: EU-ESS
    source: fact
    evidence: "The European Statistical System is the partnership between the Community statistical authority, which is the Commission (Eurostat), and the national statistical institutes and other national authorities responsible in each member state for the development, production and dissemination of European statistics; the ESS Committee is composed of NSI representatives and chaired by Eurostat (ec.europa.eu/eurostat/web/european-statistical-system; EUR-Lex CELEX 32009R0223). INSEE is the French NSI and is described as the French branch of Eurostat (insee.fr; knowledge4policy.ec.europa.eu 'INSEE'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Accueil — Insee"
    url: "https://www.insee.fr/en/accueil"
    publisher: "Institut national de la statistique et des études économiques (INSEE)"
  - title: "INSEE — Institut National de la Statistique et des Etudes Economiques"
    url: "https://knowledge4policy.ec.europa.eu/organisation/insee-institut-national-de-la-statistique-et-des-etudes-economiques_en"
    publisher: "European Commission — Knowledge for policy"
  - title: "European Statistical System (ESS)"
    url: "https://ec.europa.eu/eurostat/web/european-statistical-system"
    publisher: "Eurostat / European Commission"
---

# Institut national de la statistique et des études économiques (INSEE)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

INSEE is France's national statistical institute — a **directorate-general
of the Ministry for the Economy and Finance**, seated in Montrouge, operating
with professional independence. It collects, analyses and disseminates
information on the French economy and society and carries out the periodic
national census.

## The last missing statistical office

This entity closes a gap queued since the **France batch** and named in every
structural review since: France was the **only Atlas country with no
statistical office at all**, in a repository that already held six and that
had created [[EU-ESS]] specifically to connect them.

[[EU-ESS]] now has **seven** national institutes plus [[EU-EUROSTAT]]:

| Country | Institute |
|---|---|
| Netherlands | [[NL-CBS]] |
| Germany | [[DE-DESTATIS]] |
| Belgium | [[BE-STATBEL]] |
| Spain | [[ES-INE]] |
| Poland | [[PL-GUS]] |
| Ireland | [[IE-CSO]] |
| **France** | **INSEE** |

Every EU member state in the Atlas is now represented. The three
non-member-state countries are not, and each for its own reason:
[[GB-ONS]] reaches the international layer through [[UN-CES]] instead;
[[NO-SSB]] and [[CH-BFS]] carry no ESS edge, because the ESS is defined as a
partnership with the institutes **of the member states**.

## A directorate-general, not an agency

INSEE is structurally unlike most of its peers: it is **part of a ministry**
rather than an independent body or an agency attached to one. The sources
pair that with "total professional independence" — a combination that is
common in French administration and unusual among the Atlas's statistical
offices.

**No `part-of` edge to the ministry is asserted**, because no French ministry
is an Atlas entity — the same coverage limit recorded on [[FR-DGSI]].

## Not modelled

- The **Autorité de la statistique publique**, France's statistical
  oversight body, and the **CNIS**.
- The **census** and INSEE's registers, including SIRENE — the business
  register that would sit beside [[NL-NHR]].
- Any relationship to [[UN-CES]], which only [[GB-ONS]] carries.

## Relationships

- `part-of` [[EU-ESS]].

## Sources

Listed in frontmatter.
