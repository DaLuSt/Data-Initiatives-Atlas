---
id: EU-DMA
type: regulation
name: Digital Markets Act
alternative_names:
  - DMA
  - Regulation (EU) 2022/1925
description: >
  Regulation (EU) 2022/1925 of 14 September 2022 on contestable and fair markets in the digital sector, published in
  OJ L 265 of 12 October 2022. It lays down harmonised rules for core platform services provided by undertakings the
  Commission designates as gatekeepers, among them limits on combining and cross-using personal data without the end
  user's consent within the meaning of the GDPR. The Commission enforces it, with fines of up to 10 percent of total
  worldwide turnover. It has applied since 2 May 2023.

level: regional
country: null
region: EU

status: active
rank: ordinary
confidence: high
coverage: medium
verification: primary-source

start_date: 2023-05-02
end_date: null
last_verified: "2026-11-13"
previous_version: null
successor: null

domains:
  - DOMAIN-DIGITAL-INFRASTRUCTURE
organisations:
  - EU-COMMISSION
  - EU-EDPS
  - EU-EDPB
related_entities:
  - EU-GDPR
  - EU-DSA
relationships:
  - type: applies-in
    target: EU
    source: fact
    evidence: "The Regulation's text, read directly 2026-11-13 from the Publications Office (CELEX 32022R1925): Article 1(2), it applies 'to core platform services provided or offered by gatekeepers to business users established in the Union or end users established or located in the Union, irrespective of the place of establishment or residence of the gatekeepers'; Article 54, it is binding in its entirety and applies from 2 May 2023."
    confidence: high
    valid_from: 2023-05-02
    valid_until: null
  - type: references
    target: EU-GDPR
    source: fact
    evidence: "Article 5(2): a gatekeeper shall not process for advertising, combine or cross-use personal data across its services, or sign end users in to other services in order to combine personal data, 'unless the end user has been presented with the specific choice and has given consent within the meaning of Article 4, point (11), and Article 7 of Regulation (EU) 2016/679'. Read directly 2026-11-13."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Regulation (EU) 2022/1925 (Digital Markets Act), Official Journal text"
    url: "https://publications.europa.eu/resource/celex/32022R1925"
    publisher: "Publications Office of the European Union"
    accessed: "2026-11-13"
---

# Digital Markets Act (Regulation (EU) 2022/1925)

> **Created 2026-11-13** (roadmap #771, from the repository scan). The Official Journal text was downloaded from the
> Publications Office and read directly: the title, Articles 1, 2 (opening), 3 (opening), 5(1) and (2), 30(1), 40 and 54.
> The rest was not read; nothing below goes beyond those articles.

## What the text says

- **Title and dates.** "Regulation (EU) 2022/1925 of the European Parliament and of the Council of 14 September 2022 on
  contestable and fair markets in the digital sector and amending Directives (EU) 2019/1937 and (EU) 2020/1828 (Digital
  Markets Act)", OJ L 265, 12.10.2022, p. 1. Article 54: it enters into force on the twentieth day after publication and
  applies from **2 May 2023**; Article 3(6) and (7) and Articles 40, 46 to 50 apply from 1 November 2022, and Articles 42
  and 43 from 25 June 2023. `start_date` is the date of general application.
- **Purpose and scope** (Article 1): harmonised rules "ensuring for all businesses, contestable and fair markets in the
  digital sector across the Union where gatekeepers are present". It applies to core platform services that gatekeepers
  offer to business users established in the Union or end users established or located there, wherever the gatekeeper
  is. Member States may not impose further obligations on gatekeepers for the same purpose.
- **Core platform services** (Article 2): the list begins with online intermediation services, online search engines,
  online social networking services, video-sharing platform services, number-independent interpersonal communications
  services, operating systems, web browsers, virtual assistants, cloud computing services and online advertising
  services. The proposed EU KIDS Act takes definitions from this Article (`discovery/candidates.md` C11).
- **Gatekeepers** (Article 3): an undertaking with a significant impact on the internal market, a core platform service
  that is an important gateway, and an entrenched and durable position. The presumptions include an annual Union turnover
  of EUR 7.5 billion or more in each of the last three financial years, or a market capitalisation of at least EUR 75
  billion, and a core platform service with at least 45 million monthly active end users and at least 10,000 yearly
  active business users in the Union.
- **Personal data** (Article 5(2)): no processing for advertising of data from third parties' use of the service, no
  combining or cross-use of personal data across services, and no signing-in to combine data, unless the end user has
  given consent within the meaning of [[EU-GDPR]]; a refused request may not be repeated more than once a year.
- **Fines** (Article 30): up to 10 percent of the gatekeeper's total worldwide turnover in the preceding financial year.
- **The high-level group** (Article 40): set up by the Commission and composed of European bodies and networks, among
  them the European Data Protection Supervisor and the European Data Protection Board ([[EU-EDPS]], [[EU-EDPB]]).

## Not modelled

- The **designated gatekeepers** and the Commission's designation decisions: not read, so none is named.
- **Directives (EU) 2019/1937 and (EU) 2020/1828**, which the Regulation amends, are not Atlas entities, so no `amends`
  edge is recorded.
- The seats of [[EU-EDPS]] and [[EU-EDPB]] in the high-level group are in prose only; the edge type that would carry them
  (`participates-in`) needs the group as an entity, which it is not.

## Sources

Listed in frontmatter, read directly.
