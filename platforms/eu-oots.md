---
id: EU-OOTS
type: platform
name: Once-Only Technical System
alternative_names:
  - OOTS
description: >
  The technical system for the cross-border automated exchange of evidence between public authorities that Article
  14(1) of the Single Digital Gateway Regulation provides for. Commission Implementing Regulation (EU) 2022/1463 of 5
  August 2022 sets its specifications: procedure portals of evidence requesters and data services of evidence
  providers, eIDAS nodes for authenticating the user, eDelivery Access Points, and common services (a data service
  directory, an evidence broker and a semantic repository) that the Commission sets up with the Member States. The
  Implementing Regulation has applied since 12 December 2023.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2023-12-12
end_date: null
last_verified: "2026-11-14"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - EU-COMMISSION
related_entities:
  - EU-SDG
  - EU-EIDAS
relationships:
  - type: governed-by
    target: EU-SDG
    source: fact
    evidence: "Commission Implementing Regulation (EU) 2022/1463, read directly 2026-11-14 from the Publications Office (CELEX 32022R1463): its title, 'setting out technical and operational specifications of the technical system for the cross-border automated exchange of evidence and application of the once-only principle in accordance with Regulation (EU) 2018/1724'; Article 1(1), the OOTS 'means the technical system for the cross-border automated exchange of evidence referred to in Article 14(1) of Regulation (EU) 2018/1724'; Article 36, it applies from 12 December 2023."
    confidence: high
    valid_from: 2023-12-12
    valid_until: null
  - type: part-of
    target: EU
    source: fact
    evidence: "Implementing Regulation (EU) 2022/1463, Article 4(1): 'The Commission in cooperation with Member States shall establish the following services of the OOTS (common services): (a) the data service directory ...; (b) the evidence broker ...; (c) the semantic repository'. Article 36: binding in its entirety and directly applicable in all Member States. Read directly 2026-11-14."
    confidence: high
    valid_from: 2023-12-12
    valid_until: null
  - type: depends-on
    target: EU-EIDAS
    source: fact
    evidence: "Implementing Regulation (EU) 2022/1463, Article 2: the OOTS consists of, among other things, '(e) eIDAS nodes for user authentication and identity matching'; Article 1(5) defines an eIDAS node by Implementing Regulation (EU) 2015/1501; Article 3(1), 'Member States shall ensure that evidence requesters are connected to an eIDAS-node to enable user authentication'. That the 2015 implementing regulation was adopted under Regulation (EU) No 910/2014 was not read here, which is why the confidence is medium."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Commission Implementing Regulation (EU) 2022/1463, Official Journal text"
    url: "https://publications.europa.eu/resource/celex/32022R1463"
    publisher: "Publications Office of the European Union"
    accessed: "2026-11-14"
---

# Once-Only Technical System (OOTS)

> **Created 2026-11-14** (roadmap #771). Sourced from Commission Implementing Regulation (EU) 2022/1463, read directly from the
> Official Journal text: the title, Articles 1 (points 1 to 6), 2, 3(1), 4(1) and (2) opening, and 36. `start_date` is
> the date the Implementing Regulation applies from; **how far the system is in operation in each Member State was not
> read**, so `confidence` is medium.

## What the text says

- **What it is** (Article 1(1)): the technical system for the cross-border automated exchange of evidence of
  [[EU-SDG]] Article 14(1). An *evidence requester* is the authority handling a procedure; an *evidence provider* is the
  authority that lawfully issues the evidence.
- **What it consists of** (Article 2): the requesters' procedure portals and the providers' data services, intermediary
  platforms, preview spaces, national registries and services, eIDAS nodes, eDelivery Access Points, the common services,
  and the integration elements between them.
- **Common services** (Article 4): a data service directory, an evidence broker and a semantic repository, set up by the
  Commission with the Member States; Member States connect their portals and register their data services.
- **Dates.** Implementing Regulation of 5 August 2022, OJ L 231, 6.9.2022, p. 1, applying from **12 December 2023**
  (Article 36).

## What the Atlas already said

[[EU-SDG]]'s own entity records, from a Commission news page, that the Member States approved the system on 22 June 2022
and that it was to be rolled out for the 21 procedures of Annex II by December 2023. That is on that entity; it was not
re-read for this one.

## Not modelled

- The national components (procedure portals, registries, intermediary platforms): none was read.
- **Implementing Regulation (EU) 2015/1501** (eIDAS nodes) and the **eDelivery** building block are not Atlas entities.
- The semantic repository is the kind of shared metadata asset the Atlas tracks elsewhere ([[EU-SEMIC]]); the text read
  does not say who maintains it, so no edge is drawn.

## Sources

Listed in frontmatter, read directly.
