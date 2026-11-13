---
id: EU-DSA
type: regulation
name: Digital Services Act
alternative_names:
  - DSA
  - Regulation (EU) 2022/2065
description: >
  Regulation (EU) 2022/2065 of 19 October 2022 on a Single Market for Digital Services, published in OJ L 277 of
  27 October 2022. It lays down harmonised rules for intermediary services offered to recipients in the Union: a
  conditional exemption from liability, due-diligence obligations by category of provider, and rules on enforcement.
  Platforms and search engines with 45 million or more average monthly active recipients in the Union can be designated
  as very large, and the Commission supervises those. It has applied since 17 February 2024.

level: regional
country: null
region: EU

status: active
rank: ordinary
confidence: high
coverage: medium
verification: primary-source

start_date: 2024-02-17
end_date: null
last_verified: "2026-11-13"
previous_version: null
successor: null

domains:
  - DOMAIN-DIGITAL-INFRASTRUCTURE
organisations:
  - EU-COMMISSION
related_entities:
  - EU-GDPR
  - EU-EPRIVACY-DIRECTIVE
  - EU-DMA
relationships:
  - type: applies-in
    target: EU
    source: fact
    evidence: "The Regulation's text, read directly 2026-11-13 from the Publications Office (CELEX 32022R2065): its closing formula, 'This Regulation shall be binding in its entirety and directly applicable in all Member States'; Article 2(1), it applies 'to intermediary services offered to recipients of the service that have their place of establishment or are located in the Union, irrespective of where the providers of those intermediary services have their place of establishment'."
    confidence: high
    valid_from: 2024-02-17
    valid_until: null
  - type: references
    target: EU-GDPR
    source: fact
    evidence: "Article 2(4)(g): the Regulation is 'without prejudice to' Union law on the protection of personal data, 'in particular Regulation (EU) 2016/679 and Directive 2002/58/EC'. Article 28(2) bars advertisements 'based on profiling as defined in Article 4, point (4), of Regulation (EU) 2016/679' where the provider is aware with reasonable certainty that the recipient is a minor. Read directly 2026-11-13."
    confidence: high
    valid_from: null
    valid_until: null
  - type: references
    target: EU-EPRIVACY-DIRECTIVE
    source: fact
    evidence: "Article 2(4)(g) names Directive 2002/58/EC beside Regulation (EU) 2016/679 among the Union acts the Regulation is 'without prejudice to'. Read directly 2026-11-13."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Regulation (EU) 2022/2065 (Digital Services Act), Official Journal text"
    url: "https://publications.europa.eu/resource/celex/32022R2065"
    publisher: "Publications Office of the European Union"
    accessed: "2026-11-13"
---

# Digital Services Act (Regulation (EU) 2022/2065)

> **Created 2026-11-13** (roadmap #771, from the repository scan). The Official Journal text was downloaded from the
> Publications Office and read directly: the title, Articles 1, 2, 3 (opening), 28, 33, 49, 52, 56, 61, 62 (opening), 74
> and 93. The rest was not read; nothing below goes beyond those articles.

## What the text says

- **Title and dates.** "Regulation (EU) 2022/2065 of the European Parliament and of the Council of 19 October 2022 on a
  Single Market For Digital Services and amending Directive 2000/31/EC (Digital Services Act)", OJ L 277, 27.10.2022, p. 1.
  Article 93: it enters into force on the twentieth day after publication and applies from **17 February 2024**, except
  that Article 24(2), (3) and (6), Article 33(3) to (6), Article 37(7), Article 40(13), Article 43 and Sections 4, 5 and 6
  of Chapter IV apply from 16 November 2022. `start_date` is the date of general application, as for the other EU
  regulations in the Atlas.
- **Aim and content** (Article 1): a "safe, predictable and trusted online environment"; a framework for the conditional
  exemption from liability of providers of intermediary services, due-diligence obligations tailored to categories of
  provider, and rules on implementation and enforcement.
- **Scope** (Article 2): intermediary services offered to recipients established or located in the Union, wherever the
  provider is established. It does not affect Directive 2000/31/EC and is without prejudice to a list of other Union
  acts, among them Directive 2010/13/EU and data protection law ([[EU-GDPR]] and [[EU-EPRIVACY-DIRECTIVE]]).
- **Minors** (Article 28): providers of online platforms accessible to minors put in place appropriate and proportionate
  measures for a high level of privacy, safety and security of minors, and do not show them advertisements based on
  profiling. The proposed EU KIDS Act (`discovery/candidates.md` C11) says it specifies and complements this Regulation.
- **Very large platforms and search engines** (Article 33): those with average monthly active recipients in the Union
  "equal to or higher than 45 million" that are designated as such. The Commission adjusts the number when the Union's
  population changes by 5 percent, so that it corresponds to 10 percent of the population.
- **Who enforces** (Articles 49 and 56): each Member State designates competent authorities and one of them as its
  **Digital Services Coordinator**. The Member State of the provider's main establishment has exclusive powers, except
  that the Commission has exclusive powers over the section on very large platforms and search engines and may enforce
  the rest of the Regulation against them.
- **The Board** (Articles 61 and 62): the European Board for Digital Services, an independent advisory group of the
  Digital Services Coordinators.
- **Fines** (Articles 52 and 74): Member States' maximum for a failure to comply is 6 percent of the provider's annual
  worldwide turnover; the Commission may fine a very large platform or search engine up to 6 percent of its total
  worldwide annual turnover.

## Not modelled

- The **national Digital Services Coordinators** and the **European Board for Digital Services**: none is an Atlas entity
  yet. The Commission is listed under `organisations` and carries no typed edge, because the convention records
  `governed-by` on the body, not on the law.
- **Directive 2000/31/EC** (electronic commerce), which the Regulation amends, and **Directive 2010/13/EU** (audiovisual
  media services) are not Atlas entities, so no `amends` edge is recorded.
- Per-country `applies-in` edges are not repeated: the one edge to [[EU]] carries the applicability.

## Sources

Listed in frontmatter, read directly.
