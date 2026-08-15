---
id: EU-GAIA-X
type: organisation
name: Gaia-X European Association for Data and Cloud
alternative_names:
  - Gaia-X
  - Gaia-X AISBL
  - GAIA-X
description: >
  International non-profit association under Belgian law (AISBL) founded to
  develop the technical framework for and operate the Gaia-X federation
  services — a secure, federated data infrastructure for Europe built around
  digital sovereignty. It was launched on 15 September 2020 with 22 founding
  companies and institutions, eleven each from Germany and France, and was
  legally established on 19 February 2021.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2021-02-19
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - DE-CATENA-X
  - EU-COMMON-DATA-SPACES
relationships: []

sources:
  - title: "Association — Gaia-X: A Federated Secure Data Infrastructure"
    url: "https://gaia-x.eu/who-we-are/association/"
    publisher: "Gaia-X European Association for Data and Cloud AISBL"
  - title: "Gaia-X AISBL"
    url: "https://www.gaia-x.at/en/association-gaia-x-aisbl/"
    publisher: "Gaia-X Hub Austria"
  - title: "Gaia-X explained"
    url: "https://gaia-x-hub.de/en/gaia-x-explained/"
    publisher: "Gaia-X Hub Germany"
  - title: "GAIA-X"
    url: "https://www.oecd.org/en/publications/access-to-public-research-data-toolkit_a12e8998-en/gaia-x_db008090-en.html"
    publisher: "OECD"
  - title: "GAIA-X: A secure, federated data infrastructure for Europe"
    url: "https://wikis.ec.europa.eu/download/attachments/33527460/MIG12_GAIA-X.pdf?version=1&modificationDate=1606377365505&api=v2"
    publisher: "European Commission"
---

# Gaia-X European Association for Data and Cloud (AISBL)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

Gaia-X AISBL is an **international non-profit association under Belgian
law**, founded to develop the technical framework for and to operate the
Gaia-X federation services. Its subject is a secure, federated data
infrastructure for Europe meeting high standards of **digital
sovereignty** while promoting innovation.

- **Launched 15 September 2020** in Brussels with the signatures of 22
  founding companies and institutions — **eleven each from Germany and
  France**.
- **Legally established 19 February 2021** by public notary.
- Over 300 members have since joined.

It is backed by European governments, Germany and France in particular, and
involves private sector participants, research organisations and
non-profits.

## Why this is not a German entity

Gaia-X is the clearest test in this batch of whether the Atlas can resist
country-shaping an entity because of how it arrived.

Everything about the route here was German. It was found while researching
[[DE-CATENA-X]]; its most-cited explanatory page is the **Gaia-X Hub
Germany**; German industry and the German federal government are among its
principal backers; and it is routinely described in German sources as a
German initiative.

It is nonetheless recorded as `country: null`, `region: EU`,
`level: regional`, with an `EU-` scope prefix, because that is what the
sources say it is: a **Belgian-law association founded jointly by German
and French institutions** with pan-European membership. Recording it as
`DE-GAIA-X` would have been the country-specific duplication README §16
forbids, arrived at not by duplicating an existing entity but by
mis-scoping a new one — the subtler version of the same error, and the one
a validator cannot catch.

The `EU-` prefix follows [[EU-CEN]], [[EU-CENELEC]] and [[EU-ETSI]], which
are likewise European bodies rather than EU institutions. The prefix
denotes European regional scope in this Atlas, not membership of the Union's
institutional structure.

## The national hubs are not modelled

Two of the sources cited here are **national Gaia-X hubs** — Germany's and
Austria's. The hub network is a real structure, and a `DE-GAIA-X-HUB` would
be a legitimate national entity rather than a duplicate of this one.

None is created. Nothing about any hub's constitution, remit or governance
was established beyond its existence as a website, and a batch that has
just argued carefully about scoping should not then create a national
entity on the strength of a URL. Queued in
`discovery/research-queue.md`.

## Relationships

**None asserted.** Reached from [[DE-CATENA-X]], which is `based-on` the
Gaia-X technologies.

A relationship to [[EU-COMMON-DATA-SPACES]] or [[EU-DSSC-BLUEPRINT]] would
be the obvious one to look for — Gaia-X and the Commission's data-spaces
programme are plainly part of the same European effort. **No source read
connects them**, and the fifth source cited here is a Commission document
*about* Gaia-X rather than a statement of an institutional relationship.
Logged in `discovery/unresolved.md`.

## Sources

Listed in frontmatter.
