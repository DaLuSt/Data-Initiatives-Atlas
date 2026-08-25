---
id: LU
type: country
name: Luxembourg
alternative_names:
  - Grand Duchy of Luxembourg
  - Grand-Duché de Luxembourg
  - Lëtzebuerg
description: >
  Country anchor entity for Luxembourg, the twelfth national scope covered by
  the Data Initiatives Atlas and its tenth European Union member state. It is
  the smallest country in the Atlas by population and, through ILNAS, has
  the most-connected national standards body in the Atlas — six
  memberships across the European and international standardisation
  organisations the Atlas holds, one more than any other.

level: national
country: LU
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-25"
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
    evidence: "Confirmed verbatim by reading european-union.europa.eu's own 'EU countries' page directly (2026-08-25): 'Luxembourg EU Member State since 1958, Euro area member since 1999, Schengen area member since 1995.' Anchor edge under metadata/relationship-types.md §2.3: it records EU membership and asserts no more than that. Added in the European country batch so that all fifty anchors carry the same membership edge."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "EU countries"
    url: "https://european-union.europa.eu/principles-countries-history/eu-countries_en"
    publisher: "European Union"
    accessed: "2026-08-25"
  - title: "Government IT Centre — CTIE"
    url: "https://ctie.gouvernement.lu/en.html"
    publisher: "Le gouvernement du Grand-Duché de Luxembourg"
    accessed: "2026-08-25"
  - title: "LU — Luxembourg (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:LU"
    publisher: "International Organization for Standardization (ISO)"
  - title: "ISO — ILNAS"
    url: "https://www.iso.org/member/1776.html"
    publisher: "International Organization for Standardization (ISO)"
---

# Luxembourg

> **Verified 2026-08-25.** `european-union.europa.eu` and
> `ctie.gouvernement.lu` were read directly and confirm the 1958
> membership date verbatim. `iso.org` remains bot-walled (403), even with
> an honest, identifying User-Agent, and stays cited but unread.

## Description

Luxembourg (ISO 3166-1 alpha-2: **`LU`**) is the **twelfth country** in the
Atlas and its **tenth EU member state**.

## The smallest country, and the case against reading size into the graph

Luxembourg is by a wide margin the smallest country the Atlas holds. It is
also, through [[LU-ILNAS]], home to the **most-connected national
standards body in the Atlas**: six memberships, confirmed by reading
ILNAS's own page directly — [[INTL-ISO]], [[INTL-IEC]], [[UN-ITU]],
[[EU-CEN]], [[EU-CENELEC]] and [[EU-ETSI]] — one more than the **United
Kingdom**'s [[GB-BSI]], which the Atlas had recorded as tied with ILNAS
until this pass found ILNAS's ITU membership.

A reader inferring institutional reach from population would get that
backwards. Luxembourg beats the UK and eight other larger member states
on standards connectivity, several of which have no standards body in the
Atlas at all.

## One body does three jobs

[[LU-ILNAS]] is the **normalisation, accreditation and product-safety**
authority in one institute. Everywhere else in the Atlas these functions sit
in separate bodies, and mostly the Atlas holds only the standardisation one.
Small-state administration concentrates functions that larger states split,
and Luxembourg is where that shows.

## EU instruments that apply in Luxembourg

Recorded as `applies-in` edges on the instruments themselves. See
`countries/lu/index.md`.

## Not modelled

- **Luxembourg's role as an EU institutional seat.** The Court of Justice,
  the Court of Auditors, the EIB and the **Publications Office of the
  European Union** are based there. The Publications Office is an Atlas
  entity ([[EU-PUBLICATIONS-OFFICE]]) and **carries no relationship to
  [[LU]]** — being headquartered in a member state is not a relationship the
  Atlas models, and treating it as one would make every host state look like
  a participant in what it hosts.
- **LuxProvide** and the **MeluXina** supercomputer, Luxembourg's EuroHPC
  presence.
- The **financial sector** and the CSSF, which dominate Luxembourg's data
  economy and are outside the Atlas's public-sector scope.

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

Listed in frontmatter. `european-union.europa.eu` and
`ctie.gouvernement.lu` were read directly this pass; `iso.org` remains
bot-walled (403) even with an honest User-Agent.
