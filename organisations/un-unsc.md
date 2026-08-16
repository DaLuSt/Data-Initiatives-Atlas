---
id: UN-UNSC
type: organisation
name: United Nations Statistical Commission
alternative_names:
  - UNSC
  - UN Statistical Commission
  - StatCom
description: >
  The highest body of the global statistical system, established in 1946 and
  a functional commission of the United Nations Economic and Social Council.
  It brings together the chief statisticians of member states from around
  the world and is the highest decision-making body for international
  statistical activities, responsible for setting statistical standards and
  developing concepts and methods, including their implementation at
  national and international level. It consists of 24 member states elected
  by ECOSOC for four-year terms on the basis of equitable geographical
  distribution, and it oversees the work of the United Nations Statistics
  Division, which acts as its secretariat.

level: international
country: null
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 1946-01-01
end_date: null
last_verified: null
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - UN
  - UN-UNSD
  - EU-EUROSTAT
  - UN-SDG-INDICATORS
relationships:
  - type: part-of
    target: UN
    source: fact
    evidence: "The United Nations Statistical Commission, established in 1946, is a Functional Commission of the UN Economic and Social Council, and consists of 24 member states elected by ECOSOC for a term of four years based on equitable geographical distribution (unstats.un.org/UNSDWebsite/statcom/; ecosoc.un.org Statistical Commission event page; un.org/en/desa 'Shaping the future of global statistics'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "United Nations Statistical Commission"
    url: "https://unstats.un.org/UNSDWebsite/statcom/"
    publisher: "United Nations Statistics Division (UNSD)"
  - title: "Shaping the future of global statistics"
    url: "https://www.un.org/en/desa/shaping-future-global-statistics"
    publisher: "United Nations Department of Economic and Social Affairs"
  - title: "Statistical Commission | Economic and Social Council"
    url: "https://ecosoc.un.org/en/events/2026/statistical-commission"
    publisher: "United Nations Economic and Social Council (ECOSOC)"
  - title: "17.3 United Nations Statistical Commission (UNSC) — Handbook on Management and Organization of National Statistical Systems"
    url: "https://projects.officialstatistics.org/hb-mgnt-org-nss/handbook/chapters/C17/17_3_United_Nations_Statistical_Commission_(UNSC).html"
    publisher: "Handbook on Management and Organization of National Statistical Systems"
---

# UNSC — United Nations Statistical Commission

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The Statistical Commission is the **highest body of the global statistical
system**, established in **1946** and a functional commission of ECOSOC. It
brings together the chief statisticians of member states worldwide and is
the highest decision-making body for international statistical activities —
setting statistical standards and developing concepts and methods, including
their implementation nationally and internationally.

It consists of **24 member states elected by ECOSOC** for four-year terms on
equitable geographical distribution.

## This resolves an open modelling question

`discovery/unresolved.md` has carried it since Batch 13:

> *Should UNSD and the UN Statistical Commission be separate entities? UNSD
> is the secretariat; the Commission is the intergovernmental body. Folded
> into one on a single sourced sentence.*

They are now separate, because a source distinguishes them: **the Commission
oversees the work of UNSD**, and the Statistics Division of DESA **acts as
the Commission's secretariat**. One is an intergovernmental decision-making
body of 24 elected states; the other is a division of a UN department.

The split is not cosmetic. It is what allows [[EU-EUROSTAT]] to attach:
Eurostat is described as representing the EU **in the Commission**, which is
a forum, not in the Division, which is a secretariat. Folding the two
together had made that edge unstatable — the Atlas had a node for the
secretariat and none for the body Eurostat actually sits in.

**That is the same shape as the `EU-ESS` problem**, and the two together are
most of why the UN layer stayed an island: in both cases the refused edge
was pointing at a node that did not exist.

## Relationships

- `part-of` [[UN]].

Edges pointing here, recorded on the other entity in each case:

- [[UN-UNSD]] `governed-by` this Commission — the Commission oversees the
  Division's work.
- [[EU-EUROSTAT]] `participates-in` this Commission — **the first edge from
  the European layer into the UN layer in the Atlas's history.**
- [[UN-SDG-INDICATORS]] `governed-by` this Commission — the global indicator
  framework was designed under its supervision.

## Sources

Listed in frontmatter — the Commission's own UNSD-hosted site, the DESA
overview, the ECOSOC session page, and the international handbook on
national statistical systems.
