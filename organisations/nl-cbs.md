---
id: NL-CBS
type: organisation
name: Centraal Bureau voor de Statistiek
alternative_names:
  - CBS
  - Statistics Netherlands
description: >
  The Dutch national statistical office. An independent administrative body
  (zelfstandig bestuursorgaan) since 1 January 2004, with its legal basis in
  the Wet op het Centraal bureau voor de statistiek (2003). Its task is to
  conduct statistical research for practice, policy and science and to
  publish the resulting statistics.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
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
  - NL-WET-CBS
  - EU-EUROSTAT
relationships:
  - type: participates-in
    target: EU-EUROSTAT
    source: fact
    evidence: "The European Statistical System is the partnership between the Commission (Eurostat) and the national statistical institutes; the ESS Committee consists of the heads of Eurostat and of the NSIs. CBS is the Dutch NSI. Membership follows from the sourced composition rule. NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: NL-WET-CBS
    source: fact
    evidence: "The Wet op het Centraal bureau voor de statistiek (2003) is the CBS's legal basis; the CBS became a ZBO under it on 1 January 2004 (Eerste Kamer dossier 28.277). NOT READ — search-only."
    confidence: medium
    valid_from: 2004-01-01
    valid_until: null

sources:
  - title: "Wet op het Centraal bureau voor de statistiek (28.277)"
    url: "https://www.eerstekamer.nl/wetsvoorstel/28277_wet_op_het_centraal_bureau"
    publisher: "Eerste Kamer der Staten-Generaal"
  - title: "Wet van 20 november 2003, houdende vaststelling van een wet op het Centraal bureau voor de statistiek"
    url: "https://archief.rijksbegroting.nl/algemeen/gerefereerd/8/1/5/stb8156.html"
    publisher: "Rijksbegroting.nl"
  - title: "Kamerstuk 28277, nr. 3"
    url: "https://zoek.officielebekendmakingen.nl/kst-28277-3.html"
    publisher: "Overheid.nl — Officiële bekendmakingen"
---

# Centraal Bureau voor de Statistiek (CBS)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The CBS is the national statistical office of the Netherlands. Its statutory
task is to conduct statistical research on behalf of practice, policy and
science, and to publish the statistics compiled from that research.

Its legal basis is the *Wet op het Centraal bureau voor de statistiek*,
enacted 20 November 2003. Under that act the CBS became a zelfstandig
bestuursorgaan (independent administrative body) on 1 January 2004. The act
sets rules on the acquisition, use and provision of data for statistical
information services, strengthens the supervisory powers of the Centrale
Commissie voor de Statistiek (CCS), and clarifies the relationship between
the responsible minister, the CCS and the CBS. It is described as
guaranteeing the CBS's independent position relative to government and other
public institutions.

Batch 3 added the act itself as [[NL-WET-CBS]], closing the relationship
this entity carried as a gap in Batch 2.

The responsible ministry — named in research as Economic Affairs — is still
not linked, because Dutch ministry names and portfolio boundaries have
changed repeatedly and no ministry entity for it exists yet; see
`discovery/unresolved.md`. The CCS is likewise not yet an entity.

## Relationships

- Governed by [[NL-WET-CBS]], under which it became a ZBO on
  1 January 2004.
- Participates in the European Statistical System with [[EU-EUROSTAT]],
  added in Batch 9 — again on a composition rule rather than a source naming
  CBS. Regulation (EC) No 223/2009, the ESS's legal basis, is not modelled.
- The relationship to [[NL-BASISREGISTRATIES]] is still not established.

## Sources

Listed in frontmatter.
