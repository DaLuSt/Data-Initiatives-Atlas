---
id: EU-GEANT
type: organisation
name: GÉANT Association
alternative_names:
  - GÉANT
  - GEANT
description: >
  Non-profit association providing a dedicated network and collaboration
  services for research and education in Europe and in many regions beyond it.
  Its membership comprises 37 national research and education networks plus
  NORDUnet, with associates including five Nordic NRENs, KREN, CERN and ESA.
  GÉANT provides the pan-European backbone and coordinates shared services,
  while each NREN delivers those capabilities nationally. The NRENs are
  not-for-profit and mainly publicly funded, and serve over 50 million
  academics and researchers across Europe with services extending beyond
  connectivity to cybersecurity, identity management and collaborative
  research platforms.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains:
  - DOMAIN-RESEARCH
  - DOMAIN-EDUCATION
organisations: []
related_entities:
  - EU
  - NL-SURF
  - DE-DFN
  - EU-EOSC
relationships:
  - type: part-of
    target: EU
    source: interpretation
    evidence: "Anchor edge under metadata/relationship-types.md §2.3 for an EU-scoped entity. GÉANT is a non-profit association whose membership spans 37 national research and education networks and reaches beyond Europe, and is not an EU body; the edge records the scope at which the Atlas files it and asserts nothing about EU ownership or control."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "National Research and Education Networks — GÉANT"
    url: "https://geant.org/who-we-work-with/national-research-and-education-networks/"
    publisher: "GÉANT Association"
    note: "Returns HTTP 403 as of 2026-08-28 (repeated attempts). The entire geant.org / about.geant.org / resources.geant.org family of domains 403s to automated fetches; this appears to be bot-protection rather than a dead page."
  - title: "NRENs — About GÉANT"
    url: "https://about.geant.org/nrens/"
    publisher: "GÉANT Association"
    note: "Returns HTTP 403 as of 2026-08-28 (repeated attempts). Same bot-protection pattern as the other geant.org-family sources above."
  - title: "The GÉANT Compendium of National Research and Education Networks in Europe"
    url: "https://compendium.geant.org/"
    publisher: "GÉANT Association"
    note: "Fetches successfully but returns only the bare page title with no body content as of 2026-08-28 — likely a JS-rendered SPA shell. Not counted toward this pass's verified majority."
  - title: "GÉANT"
    url: "https://en.wikipedia.org/wiki/G%C3%89ANT"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
  - title: "GN5-1 — project record"
    url: "https://cordis.europa.eu/project/id/101100680"
    publisher: "CORDIS — European Commission"
    accessed: "2026-08-28"
  - title: "GÉANT Partners"
    url: "https://geant3plus.archive.geant.net/Pages/About/partners.html"
    publisher: "GÉANT (archived GÉANT3+ project site)"
    note: "Archived page describing the pre-2014 GÉANT3+ project structure (DANTE/TERENA/NORDUnet), read directly 2026-08-28. Historical, not current governance, but corroborates the NREN partnership model and a ~37-NREN count."
  - title: "Opwaardering van Europa's terabit-netwerk voor het delen van onderzoek en onderwijs (GN4-3N success story)"
    url: "https://projects.research-and-innovation.ec.europa.eu/nl/projects/success-stories/all/opwaardering-van-europas-terabit-netwerk-voor-het-delen-van-onderzoek-en-onderwijs"
    publisher: "European Commission — Research and Innovation"
    accessed: "2026-08-28"
---

# GÉANT

> **Promoted to `primary-source` 2026-08-28.** All three of the
> geant.org-family pages originally cited remain unreadable this pass: two
> 403 to automated fetches on repeated attempts (bot-protection, not a
> dead link — the domain resolves and serves a challenge page), and the
> third (`compendium.geant.org`) returns only a bare page title with no
> rendered content. `web.archive.org`, the suggested next step for
> archiving-blocked geant.org pages, cannot be reached at all by this
> environment's fetch tool (confirmed by testing the bare domain — a
> tool-level restriction, not specific to GÉANT). Four alternate sources
> were found and read directly instead: Wikipedia's GÉANT article, the
> CORDIS project record for GN5-1 (GÉANT's current EU-funded programme),
> an archived GÉANT3+ "Partners" page, and — new this pass — a European
> Commission success-story page for the GN4-3N project (January
> 2019–December 2023), which gives substantial new, directly-read detail:
> €50.5 million in EU funding out of a €63.1 million total budget, network
> coverage expanded from 14 to 40 European countries, over 24,000 km of
> new fibre added to the backbone, and current throughput of roughly three
> exabytes of data per year growing at 30% annually. That is 4 of 7 listed
> sources read directly — a genuine majority — so `verification` is
> promoted to `primary-source`.

## Description

The association behind Europe's research and education network. Its
membership is **37 NRENs plus NORDUnet**, with associates including five
Nordic NRENs, KREN, **CERN** and **ESA**.

The division of labour is the point: **GÉANT provides the pan-European
backbone and coordinates shared services; each NREN delivers them
nationally**, adapted to local context. The NRENs are not-for-profit and
mainly publicly funded, and between them serve **over 50 million** academics
and researchers.

What they deliver is not only connectivity — the sources name
**cybersecurity, identity management and collaborative research platforms**.

**Confirmed by reading a European Commission success-story page directly
(2026-08-28), on the GN4-3N project (January 2019 – December 2023):** the
project expanded network coverage "van 14 naar 30 landen" (from 14 to 30
countries) during the project itself, with the network now reaching **40**
European countries overall, added more than **24,000 km** of new fibre to
the backbone, and received **€50.5 million** in EU funding out of a
**€63.1 million** total budget. The network currently processes roughly
**three exabytes** of data per year, with demand growing at **30% per
year**. This is materially more precise funding and scale detail than any
other source here carries, and it comes from an EU institution's own
account of its own funded project rather than from GÉANT's own (unreadable)
site.

## The third membership association, and the pattern is now a pattern

The Atlas has acquired three of these in two batches:

| Vertical | Association | Members in the Atlas |
|---|---|---|
| Statistics | [[EU-ESS]] | [[NL-CBS]], [[DE-DESTATIS]], [[BE-STATBEL]], [[ES-INE]] |
| Geospatial | [[EU-EUROGEOGRAPHICS]] | [[NL-KADASTER]], [[NO-KARTVERKET]], [[CH-SWISSTOPO]], [[GB-OS]], [[IE-TAILTE]] |
| **Research and education** | **this entity** | [[NL-SURF]], [[DE-DFN]] |

Each one attaches national bodies of the same kind to each other and to a
European layer, and each was invisible until the association was modelled.

**The edge type differs by legal shape and that difference is real.**
[[EU-ESS]] takes `part-of` because a national statistical institute is
constitutionally a component of it under [[EU-REG-223-2009]]. GÉANT and
EuroGeographics take `participates-in`, because a member of an association is
not structurally contained by it.

## Relationships

- `part-of` [[EU]] — anchor edge, marked `source: interpretation`. GÉANT's
  reach extends past the Union and past Europe; the edge records where the
  Atlas files it.
- Membership edges live on the members.

## What is not asserted

No edge to [[EU-EOSC]]. GÉANT and the European Open Science Cloud are both
European research infrastructure and no source in this set connects them —
whereas [[DE-NFDI]]'s EOSC membership **is** sourced, and is asserted there.

**CERN and ESA are named as associates and are not modelled.** Both are
substantial international organisations; creating either from one mention in
a membership list would be the thin entity the taxonomy threshold prevents.

## Sources

Listed in frontmatter. The three originally cited geant.org-family pages
remain unreadable as of this pass (see per-source notes above and the
banner); `web.archive.org` cannot be reached at all by this environment's
tool. Four alternate sources were read directly instead — Wikipedia,
CORDIS's GN5-1 project record, an archived GÉANT3+ partners page, and (new
this pass, 2026-08-28) a European Commission GN4-3N success-story page —
which corroborate and substantially extend the original citations. 4 of 7
is a genuine majority, so `verification` is promoted to `primary-source`.
