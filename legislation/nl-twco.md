---
id: NL-TWCO
type: law
name: Tijdelijke wet onderzoeken AIVD en MIVD naar landen met een offensief cyberprogramma
alternative_names:
  - Tijdelijke wet cyberoperaties
  - TWCO
  - Temporary Act on cyber operations
description: >
  Dutch temporary act allowing deviation from the regime of the Wiv 2017 for
  investigations by the AIVD and MIVD into countries with an offensive cyber
  programme, and covering bulk datasets and other specific provisions. Passed
  by the Eerste Kamer on 12 March 2024, in force from 1 July 2024, and
  expiring four years after entry into force.

level: national
country: NL
region: EU

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: 2024-07-01
end_date: null
last_verified: "2026-08-27"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - NL-WIV-2017
  - NL-AIVD
  - NL-MIVD
relationships:
  - type: references
    target: NL-WIV-2017
    source: fact
    evidence: "Confirmed by reading all four cited pages directly (2026-08-27). aivd.nl's own page: the act gives 'enhanced operational flexibility' against countries with offensive cyber programmes (named as Russia and China), partly supplementing and partly deviating from the Wiv 2017. njb.nl: Stb. 2024, 88 (13 March 2024, published 17 April 2024), entered into force 1 July 2024 via Stb. 2024, 148. eerstekamer.nl dossier 36.263: submitted 1 December 2022, Tweede Kamer approved 24 October 2023 (14 for, 6 against), Eerste Kamer debated 5 March and approved 12 March 2024 (9 for, 6 against). wetgevingskalender.overheid.nl (WGK013565): confirms the same milestones and the 1 July 2024 entry into force following a 13 June 2024 implementation decree."
    confidence: high
    valid_from: 2024-07-01
    valid_until: null

sources:
  - title: "Tijdelijke wet onderzoeken AIVD en MIVD naar landen met een offensief cyberprogramma"
    url: "https://www.aivd.nl/onderwerpen/wet-op-de-inlichtingen-en-veiligheidsdiensten/tijdelijke-wet-onderzoeken-aivd-en-mivd-naar-landen-met-een-offensief-cyberprogramma"
    publisher: "Algemene Inlichtingen- en Veiligheidsdienst (AIVD)"
    accessed: "2026-08-27"
  - title: "Tijdelijke wet onderzoeken AIVD en MIVD naar landen met een offensief cyberprogramma, bulkdatasets en overige specifieke voorzieningen (36.263)"
    url: "https://www.eerstekamer.nl/wetsvoorstel/36263_tijdelijke_wet_onderzoeken"
    publisher: "Eerste Kamer der Staten-Generaal"
    accessed: "2026-08-27"
  - title: "Tijdelijke wet cyberoperaties"
    url: "https://www.njb.nl/wetgeving/staatsbladen/tijdelijke-wet-cyberoperaties/"
    publisher: "Nederlands Juristenblad (NJB)"
    accessed: "2026-08-27"
  - title: "Tijdelijke wet onderzoeken AIVD en MIVD naar landen met een offensief cyberprogramma"
    url: "https://wetgevingskalender.overheid.nl/Regeling/WGK013565"
    publisher: "Overheid.nl Wetgevingskalender"
    accessed: "2026-08-27"
---

# Tijdelijke wet onderzoeken AIVD en MIVD naar landen met een offensief cyberprogramma

> **Verified 2026-08-27.** All four cited pages were read directly this
> pass, closing the previous `search-only` status. This entity now carries
> a full, cross-confirmed timeline with an official Staatsblad citation
> (Stb. 2024, 88), previously missing.

## Description

A **temporary** Dutch act letting [[NL-AIVD]] and [[NL-MIVD]] deviate from
the [[NL-WIV-2017]] regime for investigations into countries with an
offensive cyber programme — aivd.nl's own page, read directly, names
**Russia and China** as the programmes in view — and covering **bulk
datasets** and other specific provisions.

Its stated purpose, per aivd.nl, is to give the services better operational
agility: the current Wiv 2017 gives "insufficient operational space to act
quickly and agilely against cyberattacks", for instance to follow an
attacker switching servers or devices without halting the operation. In
exchange, oversight bodies gain **binding authority to stop an operation
immediately** — a trade of agility for real-time, binding oversight.

## The only entity in the Atlas with a designed expiry

Timeline, now fully cross-confirmed across all four sources read directly:

| Date | Event |
|---|---|
| 1 December 2022 | Bill submitted |
| 24 October 2023 | Tweede Kamer approves (14 parties for, 6 against) |
| 5 March 2024 | Eerste Kamer debates |
| **12 March 2024** | Eerste Kamer adopts (9 parties for, 6 against) |
| 13 March 2024 | Act dated; published as **Stb. 2024, 88** on 17 April 2024 |
| 13 June 2024 | Implementation decree published |
| **1 July 2024** | In force (implementation decree Stb. 2024, 148) |
| **1 July 2028** | Expires — four years after entry into force |

`end_date` is nonetheless **null**, and deliberately so. The Atlas records
dates its sources state; "four years after entry into force" is a rule for
computing an expiry, and no source read gives the resulting date or says
whether it can be extended. Writing `2028-07-01` into the frontmatter would
be the Atlas doing arithmetic and presenting the result as a sourced fact.
The rule is recorded here in prose instead.

This is the first Atlas entity whose `status: active` is known in advance to
be temporary. [[GB-DSIT]] stopped existing; this one is scheduled to.

## What the deviation actually does

Previously recorded only as "the purpose, not the provisions" — reading
aivd.nl and njb.nl directly this pass adds real detail: the act partly
supplements and partly deviates from the Wiv 2017 on **bulk dataset
retention rules**, introduces a **binding appeals process** for disputes
between ministers and oversight bodies, and — for the powers it covers —
shifts review from [[NL-TIB]] pre-approval towards **real-time [[NL-CTIVD]]
monitoring** with binding authority to halt an operation. It also
introduces binding advance review specifically for real-time interception
of traffic and location data. See [[NL-AIVD]], [[NL-TIB]] and [[NL-CTIVD]]
for how this reshapes their relationship.

## `references`, not `supersedes`

The relationship to [[NL-WIV-2017]] is `references`. It is not `supersedes`
or `replaces`: the Wiv 2017 remains fully in force, and this act **stands
alongside** it, deviating from its regime in a defined respect for a defined
period. Both are `governed-by` targets on [[NL-AIVD]] and [[NL-MIVD]] for
exactly that reason.

## Not modelled

- The full statutory text of the bulk-dataset and appeals provisions.
- A July 2026 development surfaced in search but not verified this pass: a
  commission reportedly delivered input on implementation following an
  oversight-body report on bulk data processing. Flagged for a future pass
  rather than asserted here.

## Sources

All four read directly this pass: aivd.nl's own page, the Eerste Kamer
dossier, the NJB Staatsblad note, and the Wetgevingskalender entry.
