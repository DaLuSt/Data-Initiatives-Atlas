---
id: BE-OCAD
type: organisation
name: Coördinatieorgaan voor de Dreigingsanalyse
alternative_names:
  - OCAD
  - OCAM
  - Organe de coordination pour l'analyse de la menace
  - Coordination Unit for Threat Analysis
description: >
  Belgian body coordinating the evaluation of the terrorism and
  extremism threat, established by the act of 10 July 2006 as successor
  to the Antiterroristische Gemengde Groep (AGG). Placed under the joint
  authority of the Minister of Justice and the Minister of the Interior,
  and drawing on intelligence from VSSE, ADIV and other government
  services. Jointly overseen by Comité P and Comité I since the 2006 act.

level: national
country: BE
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2006-12-01
end_date: null
last_verified: "2026-09-17"
previous_version: BE-AGG
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - BE-WET-DREIGINGSANALYSE-2006
  - BE-COMITE-I
  - BE-VSSE
  - BE-ADIV
  - BE-AGG
relationships:
  - type: governed-by
    target: BE-WET-DREIGINGSANALYSE-2006
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP (BE-COMITE-I's own body text). Confirmed by reading etaamb.openjustice.be's own text of the law directly (2026-09-06), Article 5, and corroborated independently by VSSE's own page: 'opgericht door de wet van 10 juli 2006 betreffende de analyse van de dreiging' (established by the law of 10 July 2006 on the analysis of the threat)."
    confidence: high
    valid_from: 2006-07-10
    valid_until: null
  - type: part-of
    target: BE
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. Confirmed by reading etaamb.openjustice.be's own text of the law directly (2026-09-06), Article 5: 'Dit orgaan staat onder het gemeenschappelijke gezag van de minister van Justitie en de minister van Binnenlandse Zaken' (this body is placed under the joint authority of the Minister of Justice and the Minister of the Interior) — two Belgian federal ministers."
    confidence: high
    valid_from: 2006-07-10
    valid_until: null
  - type: supersedes
    target: BE-AGG
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP (this entity's own 'not itself an Atlas entity' note). Confirmed by reading etaamb.openjustice.be's own text of the Royal Decree of 28 November 2006 directly (2026-09-17), which implements Article 17 of the underlying Act: 'het OCAD in de rechten en de verplichtingen treedt van de Antiterroristische Gemengde Groep' (OCAD succeeds to the rights and obligations of the AGG). The same Decree independently confirms OCAD's operational start date of 1 December 2006, previously WebSearch-only."
    confidence: high
    valid_from: "2006-12-01"
    valid_until: null

sources:
  - title: "Coördinatieorgaan voor de Dreigingsanalyse (OCAD)"
    url: "https://vsse.be/nl/coordinatieorgaan-voor-de-dreigingsanalyse-ocad"
    publisher: "Veiligheid van de Staat (VSSE)"
    accessed: "2026-09-06"
  - title: "Wet van 10 juli 2006 betreffende de analyse van de dreiging"
    url: "https://etaamb.openjustice.be/nl/wet-van-10-juli-2006_n2006009570.html"
    publisher: "etaamb / OpenJustice (Belgisch Staatsblad)"
    accessed: "2026-09-06"
  - title: "Wat is het Coördinatieorgaan voor de dreigingsanalyse?"
    url: "https://www.comiteri.be/index.php/nl/19-pages-nl-nl-1/54-wat-is-het-cooerdinatieorgaan-voor-de-dreigingsanalyse"
    publisher: "Vast Comité I"
    accessed: "2026-09-06"
  - title: "28 NOVEMBER 2006. — Koninklijk besluit tot uitvoering van de wet van 10 juli 2006 betreffende de analyse van de dreiging"
    url: "https://etaamb.openjustice.be/nl/koninklijk-besluit-van-28-november-2006_n2006009957.html"
    publisher: "etaamb / OpenJustice (Belgisch Staatsblad)"
    accessed: "2026-09-17"
---

# Coördinatieorgaan voor de Dreigingsanalyse (OCAD)

> **Created 2026-09-06**, closing a gap [[BE-COMITE-I]] flagged
> explicitly on 2026-08-27: OCAD's joint 2006 placement under Comité
> P/Comité I supervision was "recorded here but not modelled, because
> OCAD is not an Atlas entity." VSSE's own page and the Act's own
> official text (etaamb.openjustice.be) were read directly this pass and
> agree.
>
> **Closed 2026-09-17.** The Royal Decree of 28 November 2006, previously
> flagged as unread, is now read directly — closing two gaps at once: the
> predecessor AGG is now [[BE-AGG]], and this entity's own operational
> start date (1 December 2006) is now confirmed by a primary source
> rather than WebSearch alone.

## Description

Confirmed by reading VSSE's own page directly: OCAD was "opgericht door
de wet van 10 juli 2006 betreffende de analyse van de dreiging"
(established by the law of 10 July 2006 on the analysis of the threat),
succeeding the **Antiterroristische Gemengde Groep (AGG)**. Its mission,
per VSSE's own words, is evaluating "de dreiging voor wat betreft
terrorisme en extremisme" (the threat regarding terrorism and
extremism), through both punctual and strategic threat analyses, drawing
on intelligence from [[BE-VSSE]], [[BE-ADIV]] and other government
services.

**Joint ministerial authority**: confirmed by reading the Act's own text
directly (Article 5): OCAD is placed "onder het gemeenschappelijke gezag
van de minister van Justitie en de minister van Binnenlandse Zaken" — the
joint authority of the Ministers of Justice and the Interior. This is why
`part-of` targets [[BE]] rather than a single ministry: no Atlas entity
exists for either ministry, and the Act's own text names two, not one.

**Operational since 1 December 2006** — confirmed 2026-09-17 by reading
the Royal Decree of 28 November 2006 directly, whose own provisions take
effect on that date, superseding the earlier WebSearch-only corroboration.

## The joint oversight arrangement, now statable

[[BE-COMITE-I]]'s own FAQ page, read directly in an earlier pass, already
named OCAD among the bodies under its parliamentary supervision, alongside
[[BE-VSSE]] and [[BE-ADIV]]. What was missing was OCAD itself as an
entity to point that edge at. See [[BE-COMITE-I]] for the completed
`applies-to` edge.

## Not modelled

- The **intelligence-supply relationships** from VSSE and ADIV to OCAD —
  the sources describe OCAD as drawing on their input, but no Atlas
  relationship type cleanly expresses "supplies intelligence to a
  threat-assessment coordinator" without overstating a chain-of-command
  that does not exist (VSSE and ADIV are not subordinate to OCAD).
## Relationships

- `governed-by` [[BE-WET-DREIGINGSANALYSE-2006]].
- `part-of` [[BE]] — a scope anchor, reflecting joint ministerial
  authority rather than a single parent ministry.
- `supersedes` [[BE-AGG]] — added 2026-09-17, closing this entity's own
  previous non-assertion. The Royal Decree of 28 November 2006, read
  directly, implements the underlying Act's own Article 17 statement
  that OCAD succeeds to the AGG's rights and obligations.

## Sources

Listed in frontmatter, four of four read directly across two passes.
