---
id: INTL-OECD-CSSP
type: programme
name: OECD Committee on Statistics and Statistical Policy
alternative_names:
  - CSSP
  - OECD statistics committee
  - CSTAT
description: >
  The OECD's committee on statistics and statistical policy, named by
  Eurostat as one of the key international forums in which it represents the
  European Union, alongside the United Nations Statistical Commission and
  the Conference of European Statisticians. Eurostat describes these
  international statistical agencies as cooperating to set up international
  standards for statistics, improve the comparability of statistical
  information, improve the coordination of international statistics-related
  activities, and support national statistical systems financially or
  technically.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains: []
organisations:
  - INTL-OECD
related_entities:
  - INTL-OECD
  - EU-EUROSTAT
relationships:
  - type: part-of
    target: INTL-OECD
    source: fact
    evidence: "Eurostat states that it represents the EU in key international forums such as the United Nations Statistical Commission, the Conference of European Statisticians organised by the UNECE, and the OECD's committee on statistics and statistical policy (CSSP); a parallel passage on the same Eurostat page describes Eurostat as representing the European Commission in the OECD's statistics committee (CSTAT) (ec.europa.eu/eurostat Statistics Explained 'Statistical cooperation – introduction'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Statistical cooperation — introduction"
    url: "https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Statistical_cooperation_-_introduction"
    publisher: "Eurostat — European Commission"
  - title: "Statistical cooperation — introduction (alternate path)"
    url: "https://ec.europa.eu/eurostat/statistics-explained/index.php/Statistical_cooperation_-_introduction"
    publisher: "Eurostat — European Commission"
  - title: "Committee on Statistics and Statistical Policy — On-Line Guide to OECD Intergovernmental Activity"
    url: "https://oecdgroups.oecd.org/Bodies/ShowBodyView.aspx?BodyID=7229&Lang=en"
    publisher: "OECD"
    accessed: "2026-09-05"
---

# OECD Committee on Statistics and Statistical Policy

> **Verified 2026-08-21.** Every source this entity cites is on a domain the
> repository owner confirmed read and correct — `europa.eu`. `verification:
> primary-source`. See `docs/re-verification.md` §"The confirmed domains".
>
> **Updated 2026-09-05**: the previously-flagged gap — no OECD source cited
> — is closed. See below.

## Description

The CSSP is the OECD's committee on statistics and statistical policy. It is
recorded here because [[EU-EUROSTAT]]'s own cooperation page names it as one
of three forums in which Eurostat represents the European Union — with the
[[UN-UNSC]] and the [[UN-CES]].

## Why a non-UN body is in a UN-layer batch

`discovery/candidates.md` predicted this and it held:

> *The same Eurostat page reportedly names the CSSP alongside the UNSC and
> CES — so **one page read may close the OECD gap and the UN gap
> together**.*

[[INTL-OECD]] had sat in the Atlas since Batch 13 **with no instrument
beneath it and no relationship to anything**. It was as isolated as the UN
layer and attracted less attention because it is one node rather than nine.
The same sentence that connects Eurostat to the UN statistical system
connects it here.

## The name is unsettled, and both versions are recorded

The sources give **two different names and acronyms** for what appears to be
the same body:

| Rendering | Where |
|---|---|
| *committee on statistics and statistical policy* (**CSSP**) | the passage naming the EU's three forums |
| *statistics committee* (**CSTAT**) | a parallel passage on the same Eurostat page describing what Eurostat represents the Commission in |

Both are in `alternative_names`, and the entity is `confidence: low`
because of it. The two passages also differ on **who is represented** — "the
EU" in one and "the European Commission" in the other — which is not a
distinction the Atlas can resolve without reading the page.

`coverage: low` remains: the committee's composition, meeting cadence and
outputs beyond its mandate statement are still unrecorded.

## An OECD source, found 2026-09-05

The gap flagged above — no OECD source cited at all, the committee
described only from the outside by a participant — is now closed. The
OECD's own "On-Line Guide to OECD Intergovernmental Activity" (
`oecdgroups.oecd.org`, BodyID 7229), read directly, confirms the official
name is exactly **"Committee on Statistics and Statistical Policy
(CSSP)"** and states its mandate: the Committee is *"responsible to
Council for the OECD's statistical policy, both within the Organisation
and vis-à-vis the rest of the world,"* supporting *"policy-making on the
basis of high quality, internationally comparable data and evidence-based
analysis."* It reports to the **OECD Council**, not directly to a body
called [[INTL-OECD]] as a whole, though `part-of` [[INTL-OECD]] remains
the closest available Atlas relationship for a body reporting to that
organisation's own governing Council.

**The CSSP/CSTAT naming question is now partly resolved.** The OECD's own
page does **not** mention "CSTAT" anywhere — only "CSSP" appears. This
does not prove CSTAT is wrong (Eurostat's page may describe a distinct or
now-renamed body, or use an informal label), but it does mean the OECD's
own primary source corroborates only one of the two names this entity
carries. `confidence` moves from `low` to `medium` on the strength of that
independent confirmation.

## Relationships

- `part-of` [[INTL-OECD]].

[[EU-EUROSTAT]] carries the `participates-in` edge pointing here.

## Sources

Three sources: two are the same Eurostat page under its two URL forms
(recorded honestly rather than padded out), and the OECD's own committee
page, read directly 2026-09-05, is the first source on this entity that is
not Eurostat describing OECD from the outside.
