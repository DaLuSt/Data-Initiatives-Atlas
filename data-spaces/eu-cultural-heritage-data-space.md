---
id: EU-CULTURAL-HERITAGE-DATA-SPACE
type: data-space
name: Common European data space for cultural heritage
alternative_names:
  - Cultural heritage data space
  - Europeana data space
description: >
  One of the fourteen common European data spaces, described by the
  Commission as a flagship to accelerate the digital transformation of the
  cultural heritage sector. It is funded under the Digital Europe Programme
  and built on Europeana, which provides multilingual access to over 60
  million digitised items from cultural heritage institutions across Europe.
  The Europeana Foundation, with eighteen partners, was selected by the
  Commission to deploy and steward it.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - EU-COMMON-DATA-SPACES
relationships:
  - type: part-of
    target: EU-COMMON-DATA-SPACES
    source: fact
    evidence: "Confirmed by reading digital-strategy.ec.europa.eu's own news page directly (2026-08-28): 'Commission proposes a common European data space for cultural heritage' states Europeana 'offers access to 52 million cultural heritage assets' and will be the basis for the data space, aiming to 'accelerate the digitisation of cultural heritage assets.' A second Commission news page on the deployment, also read directly, confirms a service contract 'awarded to a consortium led by Europeana Foundation' comprising 19 partners across 9 member states, entering force 20 September 2022, supported by the Digital Europe Programme. The 'staff working document on data spaces' URL originally cited here pointed to the wrong Commission document (the first SWD, SWD(2022) 45 final of Feb 2022, not SWD(2024) 21 final) — corrected below."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Commission proposes a common European data space for cultural heritage"
    url: "https://digital-strategy.ec.europa.eu/en/news/commission-proposes-common-european-data-space-cultural-heritage"
    publisher: "European Commission — Shaping Europe's digital future"
    accessed: "2026-08-28"
  - title: "The deployment of a common European data space for cultural heritage"
    url: "https://digital-strategy.ec.europa.eu/en/news/deployment-common-european-data-space-cultural-heritage"
    publisher: "European Commission — Shaping Europe's digital future"
    accessed: "2026-08-28"
  - title: "European Commission proposes a common European data space for cultural heritage"
    url: "https://www.ne-mo.org/news-events/article/european-commission-proposes-a-common-european-data-space-for-cultural-heritage/"
    publisher: "Network of European Museum Organisations (NEMO)"
    accessed: "2026-08-28"
  - title: "Second staff working document on data spaces — SWD(2024) 21 final"
    url: "https://digital-strategy.ec.europa.eu/en/library/second-staff-working-document-data-spaces"
    publisher: "European Commission"
    accessed: "2026-08-28"
  - title: "The common European data space for cultural heritage"
    url: "https://www.dataspace-culturalheritage.eu/en"
    publisher: "Europeana Foundation"
  - title: "Common European data space for cultural heritage — FAQs"
    url: "https://pro.europeana.eu/page/the-common-european-data-space-for-cultural-heritage-faqs"
    publisher: "Europeana PRO"
---

# Common European data space for cultural heritage

> **Re-verified 2026-08-28.** The two Europeana-hosted sources
> (`dataspace-culturalheritage.eu`, `pro.europeana.eu`) both returned
> HTTP 403 to this pass's fetch tooling and were not read. Two Commission
> news pages and an independent museum-sector article were read directly
> instead and confirm the same substance with more precision (partner
> count, contract date), which is why `verification` moves to
> `primary-source` despite the blocked pair. A stale SWD citation (pointing
> to the wrong staff working document) was also found and corrected.

## Description

The cultural heritage data space is a Commission flagship to accelerate the
digital transformation of the cultural heritage sector, funded under the
Digital Europe Programme.

It is the one of the fourteen with the **largest existing asset behind it**:
**Europeana** provides multilingual access to tens of millions of digitised
items — books, paintings, maps, manuscripts, audiovisual and 3D media — from
cultural heritage institutions across Europe, and is the basis on which the
data space is being built. The Commission's own news page, read directly,
gives **52 million** cultural heritage assets (45% reusable, 97.5% images
and text); the figure of "over 60 million" reported elsewhere appears to
reflect the collection's continued growth in the time since. Both figures
are recorded here rather than resolved, since neither source read
contradicts the other — they read as the same collection at different
points in time.

The **Europeana Foundation**, in cooperation with the Europeana Network
Association and the Europeana Aggregators' Forum, was selected by the
Commission to deploy and steward it. The Commission's own deployment news
page, read directly, puts the consortium at **19 partners** across **9**
member states, with the service contract in force since **20 September
2022**; the figure of eighteen partners reported elsewhere is close enough
to read as the same consortium counted at a slightly different point or by
a slightly different method, not a contradiction worth flagging as an
error.

## The one that started with the data already there

Most of the fourteen are being built from strategy documents outward. This
one inverts that: the aggregation infrastructure, the content and the
institutional network existed for over a decade before the data space was
designated, and the designation reorganises what was already running.

That makes it the closest analogue in the EU layer to what the Atlas records
nationally for [[NL-DSGO]] and [[NL-HEALTH-RI]] — a data space over an
established sectoral network rather than a greenfield one.

## Interoperability that is stated but not modelled

The sources say the cultural heritage data space will be interoperable with
the wider data spaces ecosystem and will explore cooperation **in particular
with media and tourism**. Both are Atlas entities as of this batch
([[EU-MEDIA-DATA-SPACE]], [[EU-TOURISM-DATA-SPACE]]).

**No relationship is asserted between them.** "Will explore opportunities for
cooperation" is a statement of intent, not of an existing connection, and the
Atlas does not turn intentions into edges.

## Not modelled

- **Europeana**, the Europeana Foundation, the Network Association and the
  Aggregators' Forum — the operator, and the batch's most conspicuous gap.
- The **Europeana Data Model (EDM)**, which would connect to the Atlas's
  metadata-standards layer around [[INTL-DCAT]].

## Sources

Listed in frontmatter. Four of six read directly this pass: both Commission
news pages and the NEMO article confirm the substance above; the corrected
SWD library page was confirmed to exist under its correct title and date.
`dataspace-culturalheritage.eu` and `pro.europeana.eu` both returned HTTP
403 to this pass's fetch tooling and were not read — noted explicitly
rather than dropped.
