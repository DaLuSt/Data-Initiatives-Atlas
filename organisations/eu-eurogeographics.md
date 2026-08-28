---
id: EU-EUROGEOGRAPHICS
type: organisation
name: EuroGeographics
alternative_names:
  - EuroGeographics AISBL
description: >
  International not-for-profit association — AISBL/IVZW under Belgian law,
  BCE registration 833 607 112 — and the membership association ("the voice
  of Europe's National Mapping, Cadastral and Land Registry Authorities")
  for the European National Mapping, Cadastral and Land Registry
  Authorities. eurogeographics.org's own current homepage (read directly
  2026-08-28) states 60 organisations across 44 countries; the prior figure
  of 63 organisations from 46 countries could not be re-confirmed and
  appears to be from an earlier count. Its stated purpose is to further the
  development of the European Spatial Data Infrastructure through
  collaboration in the area of geographic information and to represent its
  members and their capabilities; through it, members participate in policy
  developments, share knowledge and experience, and collaborate on common
  challenges.

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
  - DOMAIN-GEOSPATIAL
organisations: []
related_entities:
  - EU
  - NL-KADASTER
  - NO-KARTVERKET
  - CH-SWISSTOPO
  - GB-OS
  - IE-TAILTE
  - UN-GGIM-EUROPE
  - EU-INSPIRE
relationships:
  - type: part-of
    target: EU
    source: interpretation
    evidence: "Anchor edge under metadata/relationship-types.md §2.3 for an EU-scoped entity. EuroGeographics is an association registered under Belgian law whose membership spans dozens of countries (44 per eurogeographics.org's own current count, read directly 2026-08-28) and is not an EU body; the edge records the scope at which the Atlas files it and asserts nothing about EU ownership or control."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Members — EuroGeographics"
    url: "https://eurogeographics.org/our-members/"
    publisher: "EuroGeographics"
    accessed: "2026-08-28"
  - title: "EuroGeographics — Home"
    url: "https://eurogeographics.org/"
    publisher: "EuroGeographics"
    accessed: "2026-08-28"
  - title: "EuroGeographics — data providers and partners"
    url: "https://www.eea.europa.eu/data-and-maps/data-providers-and-partners/eurogeographics/folder_contents"
    publisher: "European Environment Agency"
    note: "Dead as of 2026-08-28: redirects (302) to https://eurogeographics.org//folder_contents, which returns 404. Not usable as a corroborating source this pass."
---

# EuroGeographics

> **Re-verified 2026-08-28.** `eurogeographics.org` was previously reported
> as blocked by the network egress proxy; it is reachable this pass, and
> both its own pages cited in frontmatter (home page and members page) were
> read directly. The third source, an EEA page, is now dead — it 302s to a
> EuroGeographics URL that 404s. Two of three cited sources read directly
> is a majority; `verification` promoted `search-only` → `primary-source`.
> One correction: eurogeographics.org's own homepage now states **60
> organisations across 44 countries**, not the 63/46 figure previously
> recorded, which could not be re-confirmed from any source read this pass
> and is most likely an earlier count that has since changed.

## Description

The membership association for Europe's **National Mapping, Cadastral and
Land Registry Authorities** (NMCAs) — confirmed by reading
eurogeographics.org's own homepage directly (2026-08-28), which describes
itself as "the not-for-profit association for the European National
Mapping, Cadastral and Land [Registry]" bodies and "the voice of Europe's
National Mapping, Cadastral and Land Registry Authorities." It is an
international not-for-profit association under Belgian law — **AISBL/IVZW,
BCE registration 833 607 112** — and, per that same page, brings together
**60 organisations across 44 countries** (previously recorded as 63 from
46; see caveat above).

Its stated purpose is to further the development of the **European Spatial
Data Infrastructure** through collaboration in geographic information, and to
represent its members and their capabilities. Through it, members take part in
policy development, share expertise, and work on common problems. The
homepage also describes three areas of activity: representation, data
(integrating datasets from 50+ national producers), and knowledge exchange
(through eight networks).

Confirmed by reading eurogeographics.org's own members page directly
(2026-08-28): members are described as "the European National Mapping,
Cadastre and Land Registry Authorities" that "use cutting edge technologies
to collect, maintain and deliver high quality, official geospatial data" —
though that page itself does not restate the membership count given on the
homepage.

## The cluster's missing middle

`discovery/candidates.md` carried this entity as **"the cluster's missing
middle"** with an explicit analogy: EuroGeographics *"probably plays the role
[[EU-ESS]] plays for statistics"* — a European association through which
national authorities of the same kind attach to each other and to the
international layer.

The analogy holds, and the geospatial and statistical verticals are now the
same shape:

```
   statistics                     geospatial
   ──────────                     ──────────
   UN-UNSC · UN-CES               UN-GGIM · UN-GGIM-EUROPE
        ▲                                 ▲
   participates-in                   (not asserted — see below)
        │                                 │
   EU-EUROSTAT                            │
        │ part-of                         │
        ▼                                 │
     EU-ESS                      EU-EUROGEOGRAPHICS
        ▲                                 ▲
      part-of                      participates-in
   ┌────┴────┬────┐              ┌────┬───┴──┬────┬────┐
 NL-CBS  DE-DESTATIS …        NL-KADASTER NO-KARTVERKET
                              CH-SWISSTOPO GB-OS IE-TAILTE
```

## Why the members attach with `participates-in` and not `part-of`

[[EU-ESS]] takes `part-of` from its members because the ESS **is** the
partnership — a national statistical institute is constitutionally a
component of it under [[EU-REG-223-2009]].

EuroGeographics is a **membership association**, and a member of an
association is not structurally contained by it. The Atlas already settled
this shape for [[EU-CEN]], whose national standardisation bodies carry
`participates-in`. The same reading applies here, on the same basis: a
sourced composition rule — *"the membership association for the European
National Mapping, Cadastral and Land Registry Authorities"*, spanning 46
countries — rather than a member list the Atlas can retrieve.

Five Atlas organisations are NMCAs of European countries and are attached on
that rule: [[NL-KADASTER]], [[NO-KARTVERKET]], [[CH-SWISSTOPO]], [[GB-OS]]
and [[IE-TAILTE]]. The edges live on the members.

## The edge that is still refused

`discovery/candidates.md` also carried *"[[EU-INSPIRE]] → the UN-GGIM
structure"* as **"the one edge that would finish the geospatial vertical"**,
and refused it because the evidence was *"a 2016 EuroGeographics presentation
**about** UN-GGIM delivered to an INSPIRE audience"* — evidence that the
communities talk, not that the instruments relate.

**Creating this entity does not change that.** EuroGeographics being the
author of the deck is why the deck exists; it is not a source for a
relationship between a European directive and a UN expert committee. No edge
to [[UN-GGIM-EUROPE]] or [[EU-INSPIRE]] is asserted here either, and the row
stays open.

That is the difference between this case and the one [[EU-ESS]] closed. There,
the missing node was the reason five edges were refused, and creating it made
them statable. Here, the missing node was **also** genuinely missing, but it
was never what the INSPIRE↔UN-GGIM refusal turned on.

## Relationships

- `part-of` [[EU]] — anchor edge, marked `source: interpretation` because
  EuroGeographics is a Belgian-law association with members in 46 countries,
  not an EU body. The edge records where the Atlas files it and nothing more.

## Sources

Listed in frontmatter — the association's own membership page and home page
were read directly this pass (2026-08-28); the European Environment
Agency's page is dead (302 → 404, see caveat above) and is retained in the
list only as a record of what was originally cited, not as a live source.
