---
id: DE-IT-NIEDERSACHSEN
type: organisation
name: Landesbetrieb IT.Niedersachsen
alternative_names:
  - IT.Niedersachsen
  - IT.N
description: >
  Lower Saxony's own central IT service provider, a Landesbetrieb
  (state enterprise) established 1 January 2014, formed by dissolving
  and succeeding the former Landesbetrieb für Statistik und
  Kommunikationstechnologie Niedersachsen (LSKN). It provides
  information-technology services for the Lower Saxony state
  administration, headquartered in Hannover with sites across several
  Lower Saxon cities, organised into three business divisions, and
  overseen by the state's Ministry for Interior Affairs and Sports.

level: subnational
country: DE
region: EU

status: active
confidence: high
coverage: low
verification: primary-source

start_date: 2014-01-01
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
  - DE-LDI
relationships:
  - type: part-of
    target: DE
    source: fact
    evidence: "Confirmed by reading niedersachsen.de's own Interior Ministry page directly (2026-09-20): 'Der Landesbetrieb IT.Niedersachsen besteht seit dem 01. Januar 2014' (has existed since 1 January 2014), formed from 'dem ehemaligen Landesbetrieb für Statistik und Kommunikationstechnologie Niedersachsen (LSKN)' (the former State Office for Statistics and Communications Technology Lower Saxony), operating as a central IT service provider for Lower Saxony's state administration under the oversight of the Ministry for Interior Affairs and Sports. de.wikipedia.org, also read directly, independently confirms the same founding date and the LSKN predecessor being dissolved when IT.Niedersachsen was created. Same Landesbetrieb legal form as [[DE-IT-NRW]], [[DE-HZD]], [[DE-BITBW]] and [[DE-LDI]]. Anchor edge under metadata/relationship-types.md §2.3, asserting Lower Saxony sub-federal scope via `level: subnational`."
    confidence: high
    valid_from: 2014-01-01
    valid_until: null

sources:
  - title: "Landesbetrieb IT.Niedersachsen"
    url: "https://www.mi.niedersachsen.de/startseite/themen/it_bevollmachtigter_der_landesregierung/landesbetrieb_it_niedersachsen/landesbetrieb-itniedersachsen-62270.html"
    publisher: "Niedersächsisches Ministerium für Inneres und Sport"
    accessed: "2026-09-20"
  - title: "IT.Niedersachsen"
    url: "https://de.wikipedia.org/wiki/IT.Niedersachsen"
    publisher: "Wikipedia (German)"
    accessed: "2026-09-20"
---

# Landesbetrieb IT.Niedersachsen

> **Created 2026-09-20**, further narrowing `discovery/unresolved.md`
> item #5 — Lower Saxony's own IT service provider, alongside
> [[DE-HZD]] (Hesse), [[DE-BITBW]] (Baden-Württemberg) and [[DE-LDI]]
> (Rhineland-Palatinate). Sourced from the Lower Saxony Interior
> Ministry's own page and German Wikipedia, both read directly.

## Description

IT.Niedersachsen is Lower Saxony's central IT service provider, a
**Landesbetrieb** confirmed directly on the state's own Interior
Ministry page: **"besteht seit dem 01. Januar 2014"** (has existed since
1 January 2014).

## A clean successor, like BITBW

Both the ministry's own page and Wikipedia, read directly, confirm
IT.Niedersachsen was formed by dissolving and succeeding its sole
predecessor, the **Landesbetrieb für Statistik und
Kommunikationstechnologie Niedersachsen (LSKN)** — a one-to-one
succession structurally similar to [[DE-BITBW]]'s replacement of IZLBW,
rather than [[DE-IT-NRW]]'s multi-body merger.

## Not modelled

- **LSKN**, IT.Niedersachsen's dissolved predecessor — described here in
  prose only.
- IT.Niedersachsen's three internal Geschäftsbereiche (business
  divisions) and specific site locations beyond Hannover.
- **How this entity's remit relates to [[DE-DATAPORT]]'s own
  Niedersachsen Träger role** (joined 2010) — [[DE-DATAPORT]]'s own file
  notes its Niedersachsen relationship is narrower than full Träger
  status (tax-administration IT specifically), which is consistent with
  the two coexisting, but no source read states this explicitly. Logged
  as an open question in `discovery/unresolved.md` item #5.

## Relationships

- `part-of` [[DE]] (anchor edge, `level: subnational`).

## Sources

Listed in frontmatter, both read directly.
