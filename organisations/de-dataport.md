---
id: DE-DATAPORT
type: organisation
name: Dataport
alternative_names:
  - Dataport AöR
  - Dataport Anstalt des öffentlichen Rechts
description: >
  German multi-Land information and communication technology service
  provider for public administration, an Anstalt des öffentlichen Rechts
  (public-law institution) established 1 January 2004 by a Staatsvertrag
  (state treaty, signed 27 August 2003) between Hamburg and
  Schleswig-Holstein. Mecklenburg-Vorpommern and Bremen joined as further
  Träger (carrier states) on 1 January 2006, Niedersachsen on 1 January
  2010, and Sachsen-Anhalt on 1 January 2013 — with Schleswig-Holstein's
  own municipal IT association (ITVSH) joining as an additional Träger on
  1 January 2012. Headquartered in Altenholz near Kiel, it provides IT
  infrastructure and digital services for public administration across
  its Träger states, employing roughly 6,200 staff.

level: subnational
country: DE
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2004-01-01
end_date: null
last_verified: "2026-09-20"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - DE
  - DE-HZD
  - DE-BITBW
relationships:
  - type: part-of
    target: DE
    source: fact
    evidence: "Confirmed by reading dataport.de's own 'Das Unternehmen' page directly (2026-09-20): Dataport is an Anstalt des öffentlichen Rechts headquartered in Altenholz, Schleswig-Holstein, with roughly 6,200 employees, functioning as the IT service provider for public administration for its Träger states. German Wikipedia's own Dataport article, also read directly, gives the Staatsvertrag basis (signed 27 August 2003, in force 1 January 2004) and the accession dates for later Träger — Mecklenburg-Vorpommern and Bremen (1 January 2006), Niedersachsen (1 January 2010), Schleswig-Holstein's municipal IT association ITVSH (1 January 2012) and Sachsen-Anhalt (1 January 2013). A search-only Bremen government Senate communication (finanzen.bremen.de, not independently fetched) corroborates the Sachsen-Anhalt accession date. Anchor edge under metadata/relationship-types.md §2.3, asserting sub-federal scope via `level: subnational` — the same treatment given to Belgium's regional digital agencies, though Dataport is unusual in spanning six Länder under one Staatsvertrag rather than serving a single sub-national unit."
    confidence: medium
    valid_from: 2004-01-01
    valid_until: null

sources:
  - title: "Das Unternehmen — Dataport"
    url: "https://www.dataport.de/unternehmen/dataport/"
    publisher: "Dataport AöR"
    accessed: "2026-09-20"
  - title: "Dataport — Wikipedia"
    url: "https://de.wikipedia.org/wiki/Dataport"
    publisher: "Wikipedia (German)"
    accessed: "2026-09-20"
  - title: "Mitteilung des Senats an die Bremische Bürgerschaft — Dataport-Beitritt Sachsen-Anhalt (not independently fetched)"
    url: "https://www.finanzen.bremen.de/sixcms/media.php/13/2013-06-25_MdS_Dataport_Beitritt_LSA.pdf"
    publisher: "Senat der Freien Hansestadt Bremen"
---

# Dataport

> **Created 2026-09-20**, closing part of `discovery/unresolved.md` item
> #5 — Germany's own sub-national digital-government bodies, unmodelled
> even after `level: subnational` was added to the schema for Belgium's
> equivalents on 2026-08-21. Sourced from Dataport's own page and German
> Wikipedia, both read directly.

## Description

Dataport is a **multi-Land** IT service provider for German public
administration — an **Anstalt des öffentlichen Rechts** (public-law
institution), not a private company, headquartered in **Altenholz** near
Kiel with roughly **6,200 employees**.

## Founded by treaty between two Länder, joined by four more

Confirmed by reading German Wikipedia's own article directly: Dataport was
established by a **Staatsvertrag** — a state treaty — between
**Schleswig-Holstein** and the **Free and Hanseatic City of Hamburg**,
signed **27 August 2003** and entering into force **1 January 2004**. The
treaty was left open-ended for further accessions, and four more Träger
(carrier states) joined over the following decade:

| Date | Accession |
|---|---|
| 1 January 2004 | **Founding**: Schleswig-Holstein, Hamburg |
| 1 January 2006 | Mecklenburg-Vorpommern, Bremen |
| 1 January 2010 | Niedersachsen |
| 1 January 2012 | ITVSH (Schleswig-Holstein's own municipal IT association) |
| 1 January 2013 | Sachsen-Anhalt |

## A different shape of "sub-national"

Belgium's equivalent entities ([[BE-DIGITAAL-VLAANDEREN]],
[[BE-AGENCE-NUMERIQUE]], [[BE-PARADIGM]]) each serve one Region. Dataport
is the opposite case: one public-law body constituted by treaty among
**six** Länder, serving all of them jointly rather than any single one.
`level: subnational` still fits — Dataport operates below the national
tier, and no single Land governs it alone — but this entity is a useful
counter-example to the "one agency per sub-national unit" pattern the
Belgian entities might otherwise suggest.

## Not modelled

- Individual sector-specific services Dataport operates (e.g. tax
  administration IT for Mecklenburg-Vorpommern and Niedersachsen, which
  the sources describe as a narrower relationship than full Träger
  status).
- The Staatsvertrag's own text — this entity rests on Dataport's own page
  and Wikipedia's account of it, not a direct read of the treaty.
- Any relationship to [[DE-FITKO]] or [[DE-KOSIT]] — no source read
  connects Dataport to the federal IT-cooperation bodies specifically.
- Any relationship to [[DE-HZD]] (Hesse) or [[DE-BITBW]] (Baden-
  Württemberg), two more single-Land IT providers now modelled — no
  source connects them; recorded for navigation only.

## Relationships

- `part-of` [[DE]] (anchor edge, `level: subnational`).

## Sources

Listed in frontmatter, two of three read directly — Dataport's own page
and German Wikipedia. The Bremen Senate communication was found by search
and not independently fetched.
