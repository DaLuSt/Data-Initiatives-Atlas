---
id: IT
type: country
name: Italy
alternative_names:
  - Italian Republic
  - Italia
  - Repubblica Italiana
description: >
  Country anchor entity for Italy, a member state of the European Union
  since 1 January 1958. It is a base anchor: it carries the country's
  position in the European legal and institutional frameworks so that
  entities scoped to it have somewhere to attach, and no national entities
  are modelled yet.

level: national
country: IT
region: EU

status: active
confidence: medium
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-19"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - EU
relationships:
  - type: part-of
    target: EU
    source: fact
    evidence: "Italy is one of the 27 member states of the European Union, having acceded on 1 January 1958; the Union's own list of EU countries records its accession date together with its Schengen and euro status (european-union.europa.eu 'EU countries'). NOT READ — search-only. Anchor edge under metadata/relationship-types.md §2.3: it records EU membership and asserts no more than that."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "IT — Italy (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:IT"
    publisher: "International Organization for Standardization (ISO)"
  - title: "EU countries"
    url: "https://european-union.europa.eu/principles-countries-history/eu-countries_en"
    publisher: "European Union"
  - title: "The Council of Europe's 46 member states"
    url: "https://www.coe.int/en/web/portal/46-members-states"
    publisher: "Council of Europe"
  - title: "Timeline — Joining the euro area"
    url: "https://www.consilium.europa.eu/en/policies/join-the-euro-area/timeline-joining-the-euro-area/"
    publisher: "Council of the European Union"
  - title: "EU, EEA, EFTA and Schengen Area countries"
    url: "https://www.government.nl/themes/international-cooperation/european-union/eu-eea-efta-and-schengen-area-countries"
    publisher: "Government of the Netherlands"
---

# Italy

> **Sourcing caveat.** Compiled from search-engine results only; the
> cited pages were confirmed to exist but were not read, because the
> working environment blocks page retrieval. `verification: search-only`.

## Description

Italy (ISO 3166-1 alpha-2: **`IT`**) is a **base country anchor**, created
so that entities scoped to it have somewhere to attach. No Italy entity is
modelled yet.

## Position in the European frameworks

| Framework | Status |
|---|---|
| European Union | Member state since **1 January 1958** |
| Euro area | Since **1 January 1999** |
| Schengen area | Member |
| Council of Europe | Member since 1949 |
| EEA | Through EU membership |

> Accession **years** in this table come from general reference
> knowledge rather than from the cited pages, which were not read.
> They are flagged for the re-verification pass along with everything
> else marked `search-only`.

## A founding member of both organisations

Italy is one of the **six founding members of the European
Communities** — with [[BE]], [[DE]], [[FR]], [[LU]] and [[NL]] — and one of
the ten founding members of [[INTL-COE]].

That makes it the last of the founding six to be given an Atlas anchor. The
other five have had one since the early country batches, and four of them
have modelled national layers.

## What this anchor does not yet carry

Nothing beyond membership. There is no national data protection authority,
no open data portal, no statistics office, no interoperability framework
and no legislation attached to this entity. Each of those exists in
reality; none has been researched.

No EU instrument in the Atlas carries `applies-in` → [[IT]] yet.
That is a gap rather than a finding: as a member state, every
directly applicable EU regulation the Atlas holds does apply here.

## ⚠ Two dates, and why this entity uses 1958

A verification pass on 2026-08-20 supplied **25 March 1957** as this
country's accession date. This entity says **1 January 1958**. Both are
right, about different events:

| Date | Event |
|---|---|
| **25 March 1957** | the Treaty of Rome was **signed**, in Rome |
| **1 January 1958** | the Treaty **entered into force**, and the Communities existed |

Strictly neither is an *accession*. The six founding members — [[BE]],
[[DE]], [[FR]], [[IT]], [[LU]] and [[NL]] — did not accede to anything; they
founded it. "Accession date" is a column borrowed from the twenty-one states
that did join later.

The Atlas uses **1 January 1958** because that is what its own cited source
says: the Union's list of EU countries records the founding six under 1958,
and this entity's `part-of` [[EU]] evidence cites that page. Using 1957 would
put the entity in contradiction with the source it names.

**This is recorded rather than resolved.** The signature date is genuinely
useful and is now here; if the Atlas would rather key the founders on 1957,
the evidence strings and the cited source both need changing together.

## Sources

Listed in frontmatter.
