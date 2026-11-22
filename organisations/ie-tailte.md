---
id: IE-TAILTE
type: organisation
name: Tailte Éireann
alternative_names:
  - Tailte Eireann
  - Ordnance Survey Ireland
  - OSi
  - Property Registration Authority
description: >
  Ireland's national mapping, land registration and property valuation
  body, formed by the merger of Ordnance Survey Ireland, the Property
  Registration Authority and the Valuation Office. It holds the national
  mapping function and the land registry in a single organisation.

level: national
country: IE
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: 2023-03-01
end_date: null
last_verified: "2026-11-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GEOSPATIAL
organisations: []
related_entities:
  - IE
  - EU-EUROGEOGRAPHICS
relationships:
  - type: part-of
    target: IE
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. The Tailte Éireann Act 2022 (No. 50 of 2022), read directly 2026-11-22 on the Irish Statute Book: section 7(1), 'There shall stand established on the establishment day a body which shall be known as Tailte Éireann to perform the functions conferred on it by or under this Act', and 7(2), it 'shall be a body corporate'; section 27, the Property Registration Authority and Ordnance Survey Ireland are 'dissolved on the establishment day'; section 6, the Minister appoints that day by order. tailte.ie, read directly 2026-08-22, lists Property Registration, Valuations and GeoHive among its services. The establishment day itself (1 March 2023, the `start_date`) comes from an encyclopedia article; the order appointing it was not read (roadmap #767)."
    confidence: high
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-EUROGEOGRAPHICS
    source: fact
    evidence: "EuroGeographics' own member list, read directly 2026-11-17: the members feed (eurogeographics.org/members/feed/) lists this authority, and its member page (eurogeographics.org/members/tailte-eireann/) gives 'National name Tailte Éireann', website https://www.tailte.ie/en/ (the page shows no member status, and its 'English spelling' field wrongly reads 'Natural Science Institute of Iceland', a template error on the page). Replaces evidence that inferred membership from the association's composition rule without a source naming this authority."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Tailte Éireann Act 2022 (No. 50 of 2022), sections 6, 7 and 27"
    url: "https://www.irishstatutebook.ie/eli/2022/act/50/enacted/en/print.html"
    publisher: "Irish Statute Book (Office of the Attorney General)"
    accessed: "2026-11-22"
  - title: "Tailte Éireann"
    url: "https://www.tailte.ie/"
    publisher: "Tailte Éireann"
    accessed: "2026-08-22"
  - title: "Ordnance Survey Ireland"
    url: "https://en.wikipedia.org/wiki/Ordnance_Survey_Ireland"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
  - title: "EuroGeographics member page"
    url: "https://eurogeographics.org/members/tailte-eireann/"
    publisher: "EuroGeographics"
    accessed: "2026-11-17"
---

# Tailte Éireann

> **Verified 2026-08-22.** Both cited pages were read directly. The
> Wikipedia article on Ordnance Survey Ireland, read this pass, confirms
> the merger and its exact date verbatim, upgrading `confidence` from low
> to medium and setting `start_date`. The Property Registration Authority
> and Valuation Office predecessors are confirmed on the same page.

## Description

Confirmed by reading en.wikipedia.org's Ordnance Survey Ireland article
directly (2026-08-22): Ordnance Survey Ireland was "Dissolved 1 March
2023 ... its functions transferred to a new body called Tailte Éireann,
which also incorporates the Property Registration Authority and the
Valuation Office." Tailte Éireann holds Ireland's national mapping, land
registration and property valuation functions, formed by merging
**Ordnance Survey Ireland**, the **Property Registration Authority** and
the **Valuation Office** on **1 March 2023**.

## `confidence: medium`, upgraded from `low`

The merger and its exact date are now confirmed against a source that
states them directly — Wikipedia's Ordnance Survey Ireland article,
rather than the two general-purpose pages this entity previously relied
on. `start_date: 2023-03-01` is set on that basis. `confidence` stops
short of the level the UK batch's better-sourced organisations carry
because neither page is a government legal source — see Sources below.

This is still the thinnest-sourced entity in the batch, and it is
included for one reason: it closes Ireland's [[DOMAIN-GEOSPATIAL]] gap on
the day the country joins, which four existing Atlas countries still have
open.

## A combination no other Atlas country has in one body

Mapping and the land registry sit together here. Elsewhere they are split:

- [[GB-OS]] maps; the UK land registries are separate and unmodelled.
- [[NL-KADASTER]] holds the cadastre **and** the topographic register
  [[NL-BRT]] — the closest parallel, and still not a merger of three bodies.
- [[NO-KARTVERKET]] holds mapping and the property register.

The merger is now confirmed: Ireland and Norway are the two countries in
the Atlas that fuse mapping and the land registry into one body.

## Not modelled

- The **establishing legislation** itself (the merger date is now known;
  the Act that authorised it is not).
- Whether Ireland has an **INSPIRE** transposition, and Tailte Éireann's
  role in it.
- **data.geohive.ie** and Ireland's spatial data infrastructure.

## Sources

Listed in frontmatter, both read directly this pass. **Neither is a
government legal source** — the establishing Act itself was not located —
which is why `confidence` stops at medium rather than reaching the level
of entities sourced directly from legislation.gov equivalents.
