---
id: EU-ESS
type: framework
name: European Statistical System
alternative_names:
  - ESS
  - Système statistique européen
description: >
  The partnership between the Community statistical authority — the
  Commission, acting through Eurostat — and the national statistical
  institutes and other national authorities responsible in each member state
  for the development, production and dissemination of European statistics.
  It was formalised in March 2009 when the European Parliament and the
  Council adopted Regulation (EC) No 223/2009 on European statistics,
  informally known as the EU Statistical Law, which consolidated the
  activities of the ESS and clarified the roles of Eurostat, the national
  statistical institutes and other national authorities. The regulation was
  amended in 2015 by Regulation (EU) 2015/759 and again in 2024. The ESS
  Committee, composed of representatives of the national statistical
  institutes and chaired by Eurostat, is established under the regulation.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2009-03-11
end_date: null
last_verified: null
previous_version: null
successor: null

domains: []
organisations:
  - EU-EUROSTAT
related_entities:
  - EU-EUROSTAT
  - NL-CBS
  - DE-DESTATIS
  - BE-STATBEL
  - ES-INE
  - UN-CES
relationships: []

sources:
  - title: "Regulation (EC) No 223/2009 of the European Parliament and of the Council on European statistics"
    url: "https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=celex%3A32009R0223"
    publisher: "EUR-Lex — Publications Office of the European Union"
  - title: "Overview — European Statistical System (ESS)"
    url: "https://ec.europa.eu/eurostat/web/european-statistical-system"
    publisher: "Eurostat — European Commission"
  - title: "Eurostat and the European Statistical System — Statistics Explained"
    url: "https://ec.europa.eu/eurostat/statistics-explained/SEPDF/cache/10129.pdf"
    publisher: "Eurostat — European Commission"
  - title: "European Statistical System — Central Statistics Office"
    url: "https://www.cso.ie/en/aboutus/pagesforfoi/europeanstatisticalsystem/"
    publisher: "Central Statistics Office (Ireland)"
  - title: "ESS — European Statistical System and Eurostat"
    url: "https://stat.gov.pl/en/international-statistics/international-institutions-organisations/ess-european-statistical-system-and-eurostat/"
    publisher: "Statistics Poland"
---

# ESS — European Statistical System

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The ESS is the **partnership** between the Community statistical authority —
the Commission, acting through [[EU-EUROSTAT]] — and the **national
statistical institutes** and other national authorities responsible in each
member state for developing, producing and disseminating European
statistics.

It was formalised in **March 2009** by **Regulation (EC) No 223/2009**,
informally the *EU Statistical Law*, which consolidated the ESS's activities
and clarified the respective roles of Eurostat, the NSIs and other national
authorities. It was amended in 2015 by Regulation (EU) 2015/759 and again in
2024, the later amendment aimed at improving data access, enabling faster
responses in crises and supporting new statistical outputs.

The **ESS Committee**, composed of NSI representatives and chaired by
Eurostat, is established under the regulation.

## This entity was created to fix five refused edges at once

`discovery/unresolved.md` carried a cluster of refusals across four
countries: [[NL-CBS]], [[DE-DESTATIS]] and [[BE-STATBEL]] to
[[EU-EUROSTAT]], and lineage links to [[UN-FPOS]]. The Spain batch added a
sixth case and resolved it only partially — [[ES-INE]] was given a
`related-to` edge to Eurostat marked `source: interpretation`, with its body
stating plainly what the real problem was:

> *The sources describe a three-party structure — INE and Eurostat both
> within the European Statistical System — not a direct bilateral
> relationship. **The correct fix is an `EU-ESS` entity.***

That is this entity, and the fix is now applied. Five national statistical
offices and Eurostat attach here by `part-of`, which is what the sources
actually describe:

```
                     UN-UNSC · UN-CES          ← the UN layer
                          ▲
                    participates-in
                          │
                    EU-EUROSTAT
                          │ part-of
                          ▼
                       EU-ESS
             ┌────────┬────┴────┬─────────┐
          part-of  part-of  part-of   part-of
             ▼        ▼        ▼         ▼
          NL-CBS  DE-DESTATIS BE-STATBEL ES-INE
```

**[[ES-INE]]'s interpretation edge has been removed** and replaced with a
`part-of` to this entity, marked `source: fact`. The weaker edge existed
only because there was nowhere correct to point; leaving it beside the
correct one would double-count the relationship and keep an inference in the
graph that the data no longer needs.

## Regulation (EC) No 223/2009 is cited, not modelled

The regulation is this entity's legal basis and its first source. **No entity
was created for it**, and that is a deliberate limit rather than an
oversight: `discovery/research-queue.md` has carried Regulation 223/2009
since Batch 9 as an unmodelled legal base, alongside Regulation (EU)
1025/2012 for the European standardisation organisations. Creating one of
that pair inside this batch and not the other would leave the Atlas
inconsistent about how statutory bases are handled.

The consequence is recorded rather than hidden: this framework has **no
`governed-by` edge**, and the instrument that establishes it appears only as
a citation.

## Relationships

None asserted from this entity. Every edge in the diagram above lives on the
member — `part-of` belongs on the part, not the whole — which is the same
direction convention [[EU-EUROSTAT]] already used for `part-of`
[[EU-COMMISSION]].

## Sources

Listed in frontmatter — the EUR-Lex text of Regulation 223/2009, two
Eurostat pages, and the Irish and Polish statistical offices' own
descriptions of the system they belong to.
