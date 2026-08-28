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
verification: search-only

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
---

# GÉANT

> **Re-verified 2026-08-28 — stays at `search-only`.** All three of the
> geant.org-family pages originally cited remain unreadable this pass: two
> 403 to automated fetches on repeated attempts (bot-protection, not a
> dead link — the domain resolves and serves a challenge page), and the
> third (`compendium.geant.org`) returns only a bare page title with no
> rendered content. Per the re-verification discipline, three alternate
> sources were found and read directly instead: Wikipedia's GÉANT article,
> the CORDIS project record for GN5-1 (GÉANT's current EU-funded
> programme), and an archived GÉANT3+ "Partners" page. All three
> corroborate the existing description (NREN count in the high 30s to 40s
> depending on how coordinating bodies are counted, NORDUnet's role,
> EU co-funding, and the pan-European/beyond-EU membership footprint) but
> none is the specific page originally cited, and dfn.de and eduroam.org
> were tried as further alternates and also failed (404 and 403
> respectively). That leaves 3 of 6 listed sources read directly — exactly
> the borderline case the discipline calls out — so `verification` stays
> `search-only` rather than being forced to `primary-source`.

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
banner). Three alternate sources were read directly instead — Wikipedia,
CORDIS's GN5-1 project record, and an archived GÉANT3+ partners page —
which corroborate but do not replace the original citations. 3 of 6 is a
borderline majority, so `verification` is left at `search-only`
deliberately rather than forced upward.
