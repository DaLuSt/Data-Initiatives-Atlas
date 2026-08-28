---
id: UN-GGIM
type: programme
name: United Nations Committee of Experts on Global Geospatial Information Management
alternative_names:
  - UN-GGIM
description: >
  United Nations programme on global geospatial information management,
  established in July 2011 by a resolution of the United Nations Economic
  and Social Council. It works through regional committees, each of which
  liaises with the UN-GGIM Secretariat on topics of interest and major
  developments between meetings of the Committee of Experts, facilitates
  regional development and discussion, and formally feeds into the Committee
  of Experts.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2011-07-27
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains:
  - DOMAIN-GEOSPATIAL
organisations: []
related_entities:
  - UN
  - UN-GGIM-EUROPE
relationships:
  - type: part-of
    target: UN
    source: fact
    evidence: "Confirmed by reading all three cited pages directly (2026-08-28): ggim.un.org 301-redirects permanently to un.org/globalgeospatial/en/, which was read and describes the Committee of Experts as 'the apex intergovernmental mechanism on geospatial information', established by ECOSOC; the regional-committees page confirms each regional committee 'formally feeds into the Committee of Experts'; and un-ggim-europe.org's news item, read directly, confirms the fifteenth session (New York, 6–8 August 2025) as reported by the child regional committee. A follow-up fetch of cepal.org's own UN-GGIM page (a UN regional commission's own site, read directly) narrows the founding date beyond 'July 2011': ECOSOC resolution 2011/24, adopted 27 July 2011, is named explicitly — 'ECOSOC resolution 2011/24, established the Committee of Experts...as the apex intergovernmental mechanism.' `start_date` is corrected from the previous 2011-07-01 placeholder to the confirmed 2011-07-27."
    confidence: high
    valid_from: 2011-07-27
    valid_until: null

sources:
  - title: "UN-GGIM — Global Geospatial Information Management"
    url: "https://ggim.un.org/"
    publisher: "United Nations Statistics Division (UNSD)"
    accessed: "2026-08-28"
  - title: "Regional Committees | Global Geospatial Information Management"
    url: "https://www.un.org/globalgeospatial/en/regional-committees"
    publisher: "United Nations"
    accessed: "2026-08-28"
  - title: "Fifteenth Session of the United Nations Committee of Experts on Global Geospatial Information Management (UN-GGIM)"
    url: "https://un-ggim-europe.org/news/fifteenth-session-of-the-united-nations-committee-of-experts-on-global-geospatial-information-management-un-ggim/"
    publisher: "UN-GGIM: Europe"
    accessed: "2026-08-28"
  - title: "G. UN-GGIM — Regional Committee of United Nations Global Geospatial Information Management"
    url: "https://www.cepal.org/en/regional-committee-united-nations-global-geospatial-information-management/g-un-ggim"
    publisher: "Economic Commission for Latin America and the Caribbean (CEPAL/ECLAC) — a UN regional commission"
    accessed: "2026-08-28"
---

# UN-GGIM — Committee of Experts on Global Geospatial Information Management

> **Verified 2026-08-28.** All three originally-cited pages were read
> directly (ggim.un.org via its own 301 redirect to un.org/globalgeospatial).
> A fourth source, CEPAL's own page (added this pass), narrows the founding
> date to an exact day: **27 July 2011, ECOSOC resolution 2011/24**. This is
> a genuine correction, not a fabrication — the day is stated by a UN
> regional commission's own page, not inferred or padded — so `start_date`
> moves from the prior `2011-07-01` placeholder to `2011-07-27`.

## Description

UN-GGIM is the United Nations programme on global geospatial information
management, **established in July 2011 by an ECOSOC resolution**.

It works through **regional committees**, each of which liaises with the
UN-GGIM Secretariat between meetings of the Committee of Experts,
facilitates regional discussion, and formally feeds into the Committee.
[[UN-GGIM-EUROPE]] is the European one.

## The geospatial cluster finally has an international parent

The Atlas has held a geospatial cluster since Batch 5 — [[EU-INSPIRE]],
[[DOMAIN-GEOSPATIAL]], [[NL-GEONOVUM]], [[DE-GEOZG]] — with **nothing above
the EU level**. It is the same shape as the statistics cluster: a
well-developed European and national layer with no international parent,
which is why `discovery/candidates.md` grouped them together.

The parent now exists. **What does not yet exist is the edge from
[[EU-INSPIRE]] to it** — see [[UN-GGIM-EUROPE]] for why.

## Sources are thin, and one is the child

`coverage: low` is still honest even after this pass: the Committee's
membership, budget and detailed outputs remain unrecorded, and one of the
four sources is [[UN-GGIM-EUROPE]]'s own news page reporting on a session of
its parent — not an independent source for the global committee's existence,
though good evidence of the relationship between them.

**What is no longer thin**: the ECOSOC resolution is now cited by number
(2011/24) and dated exactly (27 July 2011), closing the specific gap this
section used to flag.

## Relationships

- `part-of` [[UN]].

[[UN-GGIM-EUROPE]] carries the `part-of` edge pointing here.

## Sources

Listed in frontmatter, all four read directly this pass (ggim.un.org via
its own redirect).
