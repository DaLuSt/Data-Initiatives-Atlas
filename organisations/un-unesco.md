---
id: UN-UNESCO
type: organisation
name: United Nations Educational, Scientific and Cultural Organization
alternative_names:
  - UNESCO
description: >
  Specialised agency of the United Nations dedicated to strengthening
  international cooperation in education, science, culture, communication
  and information, outlined in a constitution signed on 16 November 1945 and
  working with 194 member states. Its mission is to contribute to the
  building of peace, the eradication of poverty, sustainable development and
  intercultural dialogue. In the Atlas's subject area it adopted the
  Recommendation on the Ethics of Artificial Intelligence in November 2021,
  and it has an agreement with the European Commission to accelerate that
  Recommendation's global implementation.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: search-only

start_date: 1945-11-16
end_date: null
last_verified: null
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - UN
  - UN-AI-ETHICS-RECOMMENDATION
  - EU-COMMISSION
relationships:
  - type: part-of
    target: UN
    source: fact
    evidence: "UNESCO is a specialized agency of the United Nations dedicated to strengthening international cooperation in the fields of education, science, culture and information; its constitution was signed on 16 November 1945 and it works with 194 member states (unesco.org/en/about-us; ec.europa.eu/eurostat Statistics Explained glossary entry for UNESCO; dagdok.org UN specialized agencies). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "UNESCO in brief"
    url: "https://www.unesco.org/en/about-us"
    publisher: "UNESCO"
  - title: "Glossary: United Nations Educational, Scientific and Cultural Organization (UNESCO)"
    url: "https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Glossary%3AUnited_Nations_Educational%2C_Scientific_and_Cultural_Organization_%28UNESCO%29"
    publisher: "Eurostat — European Commission"
  - title: "Artificial intelligence: Partnership between UNESCO and the EU to speed implementation of ethical rules"
    url: "https://www.unesco.org/en/articles/artificial-intelligence-partnership-between-unesco-and-eu-speed-implementation-ethical-rules"
    publisher: "UNESCO"
  - title: "UNESCO — UN specialized agencies"
    url: "https://www.dagdok.org/w/dd/en/un-system/un-specialized-agencies/unesco"
    publisher: "DagDok"
---

# UNESCO

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

UNESCO is a **specialised agency of the United Nations** for international
cooperation in education, science, culture, communication and information.
Its constitution was signed on **16 November 1945** and it works with **194
member states**.

Its relevance to this Atlas is narrow and specific: it adopted the
[[UN-AI-ETHICS-RECOMMENDATION]] in November 2021, and has an agreement with
the [[EU-COMMISSION]] to accelerate that Recommendation's implementation.

## A Batch 13 refusal, reversed

`progress/backlog.md` and `discovery/research-queue.md` have carried this
since Batch 13:

> *UN DESA, UNDP, **UNESCO**, WHO, UNECE — named in Batch 13's scope; **no
> usable source located for any**, so none created.*

That refusal was right at the time and is now obsolete for two of the five
named: UNESCO here, and [[UN-UNECE]] in the same batch. Three — UN DESA,
UNDP and WHO — remain uncreated, and this batch did not go looking for them.

**What changed is not the standard, it is the evidence.** Batch 13 searched
for UNESCO as an institution and found nothing usable. This batch reached it
sideways, through the AI ethics Recommendation and the EU partnership around
it, and arrived at UNESCO's own `about-us` page. The lesson is worth
recording: an organisation that cannot be sourced head-on may be reachable
through an instrument it owns.

## `coverage: low`, deliberately

Almost nothing about UNESCO as an institution is recorded here — no
governance, no budget, no programme structure, no relationship to any of its
other instruments. Only the AI ethics thread is modelled, because only the
AI ethics thread was researched.

The Atlas does not benefit from a thin, encyclopedic UNESCO node, and this
entity exists to hold one real relationship rather than to be a
comprehensive description. That is the same reasoning `metadata/taxonomy.md`
§1 applies to domain entities.

## Not asserted

The **UNESCO–European Commission agreement** is described in the sources and
is genuinely a European↔UN connection — the kind this batch set out to
find. It is **not** recorded as a relationship, because what the sources
describe is a funding-and-cooperation agreement to help *other* countries
implement the Recommendation, with a €4 million budget for least developed
countries. That is a partnership about implementation elsewhere; it is not
the Commission adopting, implementing or being governed by the
Recommendation, and none of the Atlas's relationship types says "has an
agreement with".

Logged in `discovery/unresolved.md`. It may justify a new relationship type
one day; it does not justify one on a single example.

## Relationships

- `part-of` [[UN]].

## Sources

Listed in frontmatter — UNESCO's own overview, the Eurostat glossary entry,
the UNESCO/EU partnership announcement, and a UN-system reference page.
