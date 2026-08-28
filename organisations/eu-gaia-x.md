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
verification: primary-source

start_date: 2021-02-19
end_date: null
last_verified: "2026-08-28"
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
    accessed: "2026-08-28"
  - title: "Gaia-X AISBL"
    url: "https://www.gaia-x.at/en/association-gaia-x-aisbl/"
    publisher: "Gaia-X Hub Austria"
    note: "Unreadable as of 2026-08-28: the page returns only a truncated/JS-rendered shell to automated fetches across multiple attempts. Not counted toward this pass's verified majority."
  - title: "Gaia-X explained"
    url: "https://gaia-x-hub.de/en/gaia-x-explained/"
    publisher: "Gaia-X Hub Germany"
    accessed: "2026-08-28"
  - title: "GAIA-X"
    url: "https://www.oecd.org/en/publications/access-to-public-research-data-toolkit_a12e8998-en/gaia-x_db008090-en.html"
    publisher: "OECD"
    note: "Returns HTTP 403 as of 2026-08-28. Not counted toward this pass's verified majority."
  - title: "GAIA-X: A secure, federated data infrastructure for Europe"
    url: "https://wikis.ec.europa.eu/download/attachments/33527460/MIG12_GAIA-X.pdf?version=1&modificationDate=1606377365505&api=v2"
    publisher: "European Commission"
    note: "Dead as of 2026-08-28: redirects to an ECAS login wall (303 → webgate.ec.europa.eu/cas/login). Not counted toward this pass's verified majority."
  - title: "Gaia-X"
    url: "https://en.wikipedia.org/wiki/Gaia-X"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
  - title: "Mobility Data"
    url: "https://digital-strategy.ec.europa.eu/en/policies/mobility-data"
    publisher: "European Commission — Shaping Europe's digital future"
    accessed: "2026-08-28"
---

# Gaia-X European Association for Data and Cloud (AISBL)

> **Re-verified 2026-08-28.** Two of the five originally cited pages could
> be read directly (gaia-x.eu's own "Association" page and Gaia-X Hub
> Germany's explainer); the other three are now dead or unreadable —
> gaia-x.at returns only a truncated/JS shell across repeated attempts, the
> OECD page 403s, and the European Commission wikis.ec.europa.eu PDF
> redirects to an ECAS login wall. That left the originally cited set below
> a majority, so two alternate sources were found and read directly per
> the re-verification discipline: Wikipedia's "Gaia-X" article (which
> corroborates the founding date, founders, and legal form independently)
> and the Commission's own "Mobility Data" policy page. Combined, four of
> the seven sources now listed were read directly this pass —
> `verification` promoted `search-only` → `primary-source`.

## Description

Gaia-X AISBL is an **international non-profit association under Belgian
law**, founded to develop the technical framework for and to operate the
Gaia-X federation services. Its subject is a secure, federated data
infrastructure for Europe meeting high standards of **digital
sovereignty** while promoting innovation.

- Confirmed by reading Wikipedia's Gaia-X article directly (2026-08-28):
  the initiative was originally presented at the 2019 Digital Summit in
  Dortmund, championed by Germany's and France's economy ministers, and
  **launched 15 September 2020** in Brussels with the signatures of 22
  founding companies and institutions — **eleven each from Germany and
  France**, including SAP, Siemens, Deutsche Telekom, Orange and OVHcloud.
- **Legally established 19 February 2021** by public notary, per
  gaia-x.eu (read directly 2026-08-28) as "Gaia-X AISBL," an
  international private non-profit association under Belgian law
  headquartered in Brussels.
- Confirmed by reading gaia-x.eu directly: the association operates under
  a "one member = one vote" governance model and describes itself as
  developing "a set of specifications, rules, policies, and a verification
  framework" for federated data and infrastructure ecosystems, aiming to
  be "the de facto standard" for secure, cross-border data sharing.
- Over 300 members have since joined (unchanged from the prior pass; not
  re-confirmed with a current count this pass).

It is backed by European governments, Germany and France in particular, and
involves private sector participants, research organisations and
non-profits. Confirmed by reading Wikipedia directly: Commission President
von der Leyen described Gaia-X as "a key building block of the European
Digital Strategy" in her 2020 State of the Union address, and the
Commission's own "Mobility Data" page (read directly 2026-08-28) treats
Gaia-X as an existing initiative that Commission-led data spaces "build
upon and promote interoperability with" — description, not a stated
institutional relationship (see "What is not asserted" below).

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
connects them.** The Commission's own "Mobility Data" page, read directly
this pass, treats a Gaia-X-affiliated private initiative (Eona-X) as an
existing ecosystem that the European Mobility Data Space "will build upon
and promote interoperability with" — proximity and shared subject matter,
not a stated institutional relationship. The originally cited
wikis.ec.europa.eu PDF, which this section previously flagged as a
Commission document *about* Gaia-X rather than a relationship statement,
is now dead (see Sources). Logged in `discovery/unresolved.md`.

## Sources

Listed in frontmatter. Four of seven read directly this pass (2026-08-28):
gaia-x.eu, Gaia-X Hub Germany, Wikipedia, and the Commission's Mobility
Data page. gaia-x.at, the OECD page and the wikis.ec.europa.eu PDF are
dead or unreadable as of this pass; see the per-source notes in
frontmatter.
