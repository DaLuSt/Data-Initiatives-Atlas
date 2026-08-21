---
id: EU-COMMISSION
type: organisation
name: European Commission
alternative_names:
  - Commission
  - EC
description: >
  Executive body of the European Union and holder of the right of
  legislative initiative. Under the ordinary legislative procedure it
  submits legislative proposals to the European Parliament and the Council,
  and it authors the strategies and communications that shape EU digital and
  data policy.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-21"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-PARLIAMENT
  - EU-COUNCIL
  - EU-CYBERSECURITY-STRATEGY
  - EU-EUROSTAT
  - EU-SEMIC
relationships:
  - type: part-of
    target: EU
    source: fact
    evidence: "The European Commission is the EU's executive body and holds the right of legislative initiative under the ordinary legislative procedure (consilium.europa.eu; europarl.europa.eu). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: produces
    target: EU-DATA-STRATEGY
    source: fact
    evidence: "The European Commission published the Communication 'A European strategy for data' on 19 February 2020 (COM(2020) 66; digital-strategy.ec.europa.eu). NOT READ — search-only."
    confidence: medium
    valid_from: 2020-02-19
    valid_until: null
  - type: produces
    target: EU-CYBERSECURITY-STRATEGY
    source: fact
    evidence: "On 16 December 2020 the European Commission and the High Representative presented the EU Cybersecurity Strategy (digital-strategy.ec.europa.eu). Co-authored with the High Representative, who is not an Atlas entity. NOT READ — search-only."
    confidence: medium
    valid_from: 2020-12-16
    valid_until: null
  - type: produces
    target: EU-DIGITAL-OMNIBUS
    source: fact
    evidence: "The European Commission introduced the Digital Omnibus Regulation proposal on 19 November 2025 (COM(2025) 836). NOT READ — search-only."
    confidence: medium
    valid_from: 2025-11-19
    valid_until: null

sources:
  - title: "The ordinary legislative procedure"
    url: "https://www.consilium.europa.eu/en/council-eu/decision-making/ordinary-legislative-procedure/"
    publisher: "Council of the European Union"
  - title: "Ordinary legislative procedure — overview"
    url: "https://www.europarl.europa.eu/olp/en/ordinary-legislative-procedure/overview"
    publisher: "European Parliament"
---

# European Commission

> **Verified 2026-08-21.** Every source this entity cites is on a domain the
> repository owner confirmed read and correct — `europa.eu`. `verification:
> primary-source`. See `docs/re-verification.md` §"The confirmed domains".

## Description

The European Commission is the EU's executive body and holds the right of
legislative initiative: the ordinary legislative procedure begins with a
Commission proposal submitted to [[EU-PARLIAMENT]] and [[EU-COUNCIL]], and
the Commission is represented in the procedure by the responsible
Commissioner or the Director-General of the department handling the dossier.

Within the Atlas it appears in two roles: author of the strategies and
communications that open the EU policy chains ([[EU-DATA-STRATEGY]],
[[EU-CYBERSECURITY-STRATEGY]]), and originator of the legislative proposals
that become the regulations and directives in `legislation/`.

## Directorates-General not modelled

Batch 9's scope names "relevant Directorates-General". **None is created.**
DG CONNECT is named in sources as a co-initiator of [[EU-DCAT-AP]], but no
research was done into the DG structure, and no source describing DG CNECT
or DG DIGIT was returned. Creating DG entities from a single passing
mention would repeat the [[NL-PETRA]] mistake. Queued in
`discovery/research-queue.md`.

`coverage: low` for the same reason: this entity records the Commission's
role in the chains the Atlas already holds, not the institution itself.

## Relationships

- Produces [[EU-DATA-STRATEGY]] and [[EU-DIGITAL-OMNIBUS]].
- Co-legislates with [[EU-PARLIAMENT]] and [[EU-COUNCIL]].

## Sources

Listed in frontmatter.
