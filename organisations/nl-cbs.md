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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-EZK
related_entities:
  - NL-WET-CBS
  - EU-EUROSTAT
relationships:
  - type: part-of
    target: EU-ESS
    source: fact
    evidence: "Confirmed by reading kst-28277-3.html directly (2026-08-27), the bill's own explanatory memorandum: it states the CBS 'executes EU statistical obligations and participates in European statistical governance frameworks.' The European Statistical System's composition rule (Eurostat plus each member state's NSI) was not itself re-read this pass; this edge rests on the CBS's role as the Dutch NSI, which the memorandum confirms in its own words."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: NL-WET-CBS
    source: fact
    evidence: "Confirmed by reading eerstekamer.nl's own bill page directly (2026-08-27): the bill 'regelt de verzelfstandiging van het Centraal bureau voor de Statistiek (CBS) tot zelfstandig bestuursorgaan (zbo)' (arranges the CBS's externalisation into an independent administrative body). kst-28277-3.html, also read directly, confirms the CBS becomes independent with its own legal personality, ending its status as part of the Ministry of Economic Affairs, governed by a Director-General (professional/statistical matters) and the independent Centrale Commissie voor de Statistiek (work programme approval and oversight)."
    confidence: high
    valid_from: 2004-01-01
    valid_until: null

sources:
  - title: "Wet op het Centraal bureau voor de statistiek (28.277)"
    url: "https://www.eerstekamer.nl/wetsvoorstel/28277_wet_op_het_centraal_bureau"
    publisher: "Eerste Kamer der Staten-Generaal"
    accessed: "2026-08-27"
  - title: "Wet van 20 november 2003, houdende vaststelling van een wet op het Centraal bureau voor de statistiek (Staatsblad 2003, 516)"
    url: "https://archief.rijksbegroting.nl/algemeen/gerefereerd/8/1/5/stb8156.html"
    publisher: "Rijksbegroting.nl"
  - title: "Kamerstuk 28277, nr. 3"
    url: "https://zoek.officielebekendmakingen.nl/kst-28277-3.html"
    publisher: "Overheid.nl — Officiële bekendmakingen"
    accessed: "2026-08-27"
---

# Centraal Bureau voor de Statistiek (CBS)

> **Verified 2026-08-27.** Two of three cited pages were read directly.
> The third — rijksbegroting.nl's archived Staatsblad text — returned a
> 503 both times it was fetched; a targeted search corroborated its date
> (Staatsblad 2003, 516) without substituting for a direct read. `coverage`
> stays `medium`; `verification` moves from `search-only` to
> `primary-source` on the strength of the two direct reads.

## Description

The CBS is the national statistical office of the Netherlands. Confirmed by
reading kst-28277-3.html (the bill's own explanatory memorandum) directly:
its statutory task is to conduct statistical research for practice, policy
and science, and to publish the resulting statistics — expressed there as
addressing "the dual tension between professional statistical independence
and administrative dependence" that existed before the reform.

Its legal basis is the *Wet op het Centraal bureau voor de statistiek*,
dated **20 November 2003** (Staatsblad 2003, 516 — confirmed by the act's
own title and corroborated by search of official sources; the archived
Staatsblad text itself could not be fetched this pass). Under that act the
CBS became a zelfstandig bestuursorgaan on **1 January 2004**, ending its
status as part of the Ministry of Economic Affairs. Confirmed directly: the
act sets rules on the acquisition, use and provision of data for statistical
information services, expands the supervisory powers of the Centrale
Commissie voor de Statistiek (CCS), and clarifies the relationship between
the responsible minister, the CCS and the CBS — read directly as guaranteeing
the CBS's independent position relative to government and other public
institutions.

Batch 3 added the act itself as [[NL-WET-CBS]], closing the relationship
this entity carried as a gap in Batch 2.

**Which ministry today, closed 2026-09-04.** `discovery/research-queue.md`
had flagged Dutch ministry naming as volatile and asked which ministry
currently holds this oversight relationship. Confirmed by reading
`organisaties.overheid.nl`'s own organisation profile for CBS directly:
its "Relatie met ministerie" field names **Economische Zaken en
Klimaat** — the current name of the ministry the 2003 act ended CBS's
status as part of. No separate Atlas entity is created for the
ministry itself, consistent with how the Atlas treats ministries
without a direct digital-government role.

**Closed 2026-09-05.** [[NL-EZK]] is now an Atlas entity, and `organisations`
above points to it. The responsible ministry was Economic Affairs at the
time of the 2003 act (per kst-28277-3.html); today's Economische Zaken en
Klimaat is that same ministry's current, renamed form (confirmed on
[[NL-EZK]]'s own page). The CCS is still not yet an entity.

## Relationships

- Governed by [[NL-WET-CBS]], under which it became a ZBO on
  1 January 2004 — confirmed this pass by reading both eerstekamer.nl and
  the bill's own explanatory memorandum directly.
- Participates in the European Statistical System with [[EU-EUROSTAT]].
  The explanatory memorandum, read directly this pass, confirms the CBS
  "executes EU statistical obligations and participates in European
  statistical governance frameworks" in its own words — a stronger basis
  than the composition-rule inference this edge previously rested on, though
  Regulation (EC) No 223/2009, the ESS's legal basis, remains unmodelled.
- The relationship to [[NL-BASISREGISTRATIES]] is still not established.

## Sources

Listed in frontmatter, two of three read directly this pass. The archived
Staatsblad page (rijksbegroting.nl) returned HTTP 503 on both attempts —
genuinely unreachable this pass, not silently dropped.
