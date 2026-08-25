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
  since 1958. It anchors six national entities: a data protection
  authority, a statistical institute, a digital-government agency, a
  digital-identity code and platform, and a national open data portal.

level: national
country: IT
region: EU

status: active
confidence: medium
coverage: low
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
    evidence: "Confirmed verbatim by reading european-union.europa.eu's own 'EU countries' page directly (2026-08-25): 'Italy EU Member State since 1958, Euro area member since 1999, Schengen area member since 1997.' Corroborated independently by government.nl's own EU/EEA/EFTA/Schengen page, which lists Italy among the 27 EU member states. Anchor edge under metadata/relationship-types.md §2.3: it records EU membership and asserts no more than that."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "EU countries"
    url: "https://european-union.europa.eu/principles-countries-history/eu-countries_en"
    publisher: "European Union"
    accessed: "2026-08-25"
  - title: "EU, EEA, EFTA and Schengen Area countries"
    url: "https://www.government.nl/themes/international-cooperation/european-union/eu-eea-efta-and-schengen-area-countries"
    publisher: "Government of the Netherlands"
    accessed: "2026-08-25"
  - title: "IT — Italy (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:IT"
    publisher: "International Organization for Standardization (ISO)"
  - title: "The Council of Europe's 46 member states"
    url: "https://www.coe.int/en/web/portal/46-members-states"
    publisher: "Council of Europe"
  - title: "Timeline — Joining the euro area"
    url: "https://www.consilium.europa.eu/en/policies/join-the-euro-area/timeline-joining-the-euro-area/"
    publisher: "Council of the European Union"
---

# Italy

> **Re-verified 2026-08-25.** `european-union.europa.eu` and
> `government.nl` were read directly and confirm EU, euro-area and
> Schengen membership verbatim. `coe.int`, `consilium.europa.eu` and
> `iso.org` remain genuinely bot-walled (403) even with an honest,
> identifying User-Agent and stay cited but unread. This entity's own
> body text was also out of date — it described Italy as carrying "no
> national entities," which had not been true since [[IT-AGID]],
> [[IT-CAD]], [[IT-DATI-GOV-IT]], [[IT-ISTAT]] and [[IT-SPID]] were
> added and [[IT-GARANTE]] was re-verified in an earlier pass. Fixed
> below.

## Description

Italy (ISO 3166-1 alpha-2: **`IT`**) anchors six national entities: a
data protection authority ([[IT-GARANTE]]), a statistical institute
([[IT-ISTAT]]), a digital-government agency ([[IT-AGID]]), a digital
administration code and identity platform ([[IT-CAD]], [[IT-SPID]])
and a national open data portal ([[IT-DATI-GOV-IT]]).

## Position in the European frameworks

| Framework | Status |
|---|---|
| European Union | Member state since **1958** |
| Euro area | Since **1999** |
| Schengen area | Since **1997** |
| Council of Europe | Member since 1949 |
| EEA | Through EU membership |

> EU, euro-area and Schengen dates are confirmed verbatim by
> `european-union.europa.eu`, read directly on 2026-08-25. The Council
> of Europe founding-membership date rests on general reference
> knowledge; `coe.int` remains bot-walled even with an honest
> User-Agent.

## A founding member of both organisations

Italy is one of the **six founding members of the European
Communities** — with [[BE]], [[DE]], [[FR]], [[LU]] and [[NL]] — and one of
the ten founding members of [[INTL-COE]] (the latter not reconfirmed this
pass; `coe.int` is bot-walled).

## Six national entities, all re-verified

As of 2026-08-25 every entity scoped to Italy carries
`verification: primary-source`: [[IT-GARANTE]] (re-verified 2026-08-21,
an earlier pass), and [[IT-AGID]], [[IT-CAD]], [[IT-DATI-GOV-IT]],
[[IT-ISTAT]] and [[IT-SPID]] (this pass). See `countries/it/index.md`
for the full list.

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

Listed in frontmatter. `european-union.europa.eu` and `government.nl`
were read directly this pass; `coe.int`, `consilium.europa.eu` and
`iso.org` remain bot-walled (403) even with an honest User-Agent.
