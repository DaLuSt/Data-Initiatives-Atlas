---
id: INTL-OECD
type: organisation
name: Organisation for Economic Co-operation and Development
alternative_names:
  - OECD
description: >
  Intergovernmental economic organisation, **not** part of the UN system. It
  works on data governance, framed as the technical, policy and regulatory
  frameworks for managing data across its value cycle and across policy
  domains including health, research, public administration and finance.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: search-only

start_date: 1961-09-30
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities: []
relationships: []

sources:
  - title: "Data governance — OECD"
    url: "https://www.oecd.org/en/topics/sub-issues/data-governance.html"
    publisher: "Organisation for Economic Co-operation and Development (OECD)"
  - title: "European Data Governance Act (DGA), Regulation (EU) 2022/868"
    url: "https://www.oecd.org/en/publications/access-to-public-research-data-toolkit_a12e8998-en/european-data-governance-act-dga-regulation-eu-2022-868_920b8b28-en.html"
    publisher: "Organisation for Economic Co-operation and Development (OECD)"
  - title: "OECD"
    url: "https://en.wikipedia.org/wiki/OECD"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
---

# OECD

> **Re-verification attempted 2026-08-28, blocked — stays `search-only`.**
> `oecd.org` is domain-wide 403-blocked for this pass's retrieval tool:
> both cited pages, plus the bare `oecd.org` homepage tried as a control,
> all returned HTTP 403. This matches the domain-wide blocks already
> documented for `coe.int` and (newly, this pass) `iso.org` — three
> separate organisational domains, all fully inaccessible to this
> environment's page-fetch tool regardless of path. Neither original
> source could be read. A Wikipedia article on the OECD was added and
> read directly as a partial substitute, confirming the OECD's founding
> (the 1960 convention, superseding the OEEC on 30 September 1961), its
> current 38-country membership, and that "The OECD is an official United
> Nations observer" — distinct from being a UN specialised agency, so the
> entity's "not part of the UN system" framing stands uncontradicted.
> That is one source read out of three (including the new addition),
> well short of a majority, so `verification` stays `search-only` rather
> than being forced. `confidence` and `coverage` are unchanged.

## Description

The OECD is an intergovernmental economic organisation with a substantial
data governance workstream. Its framing — data governance as the technical,
policy and regulatory frameworks for managing data along its value cycle
from creation to deletion, across policy domains including health, research,
public administration and finance — is close to this Atlas's own scope
definition.

It is named alongside [[INTL-ISO]] and [[UN-ITU]] as a participant in
international data governance work.

## Not a UN organisation

`INTL` scope, not `UN`. The OECD is an independent intergovernmental
organisation with its own membership, distinct from the UN system — a
distinction Batch 13's brief asks to be maintained, and one that is easy to
get wrong given how often the OECD appears in the same discussions as UN
bodies. One nuance found via Wikipedia this pass, worth stating precisely:
the OECD **is** "an official United Nations observer" — a formal
recognition status — which is not the same thing as being a UN specialised
agency (as [[UN-ITU]] is). The `INTL` framing survives that nuance intact.

## An OECD source already relied on elsewhere

The OECD's Access to Public Research Data Toolkit is one of the sources
cited on [[EU-DGA]]. That is worth noting for the same reason as
[[EU-PUBLICATIONS-OFFICE]]: the Atlas leans on this organisation's material
while barely documenting the organisation.

`coverage: low`: no OECD instrument, recommendation or guideline is
modelled. The OECD Privacy Guidelines and its data governance
recommendations are the obvious candidates. Queued.

## Sources

Listed in frontmatter. Neither original `oecd.org` source could be read
this pass (domain-wide block, see verification note above); the added
Wikipedia article was read directly as a partial substitute.
