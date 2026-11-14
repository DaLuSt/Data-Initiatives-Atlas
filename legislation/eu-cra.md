---
id: EU-CRA
type: regulation
name: Cyber Resilience Act
alternative_names:
  - CRA
  - Regulation (EU) 2024/2847
description: >
  Regulation (EU) 2024/2847 of 23 October 2024 on horizontal cybersecurity requirements for products with digital
  elements, published in the Official Journal on 20 November 2024. It sets essential cybersecurity requirements for the
  design, development and production of such products and for manufacturers' handling of vulnerabilities, with market
  surveillance by the Member States. It is in force but applies generally only from 11 December 2027; the reporting
  duties of manufacturers apply from 11 September 2026 and the chapter on conformity assessment bodies from 11 June 2026.

level: regional
country: null
region: EU

status: adopted
rank: ordinary
confidence: high
coverage: medium
verification: primary-source

start_date: 2024-12-10
end_date: null
last_verified: "2026-11-14"
previous_version: null
successor: null

domains:
  - DOMAIN-CYBERSECURITY
organisations:
  - EU-ENISA
related_entities:
  - EU-NIS2
  - EU-CYBERSECURITY-ACT
relationships:
  - type: applies-in
    target: EU
    source: fact
    evidence: "The Regulation's text, read directly 2026-11-14 from the Publications Office (CELEX 32024R2847): Article 71, it enters into force on the twentieth day after publication (published 20.11.2024), 'shall apply from 11 December 2027', except that 'Article 14 shall apply from 11 September 2026 and Chapter IV (Articles 35 to 51) shall apply from 11 June 2026', and is 'binding in its entirety and directly applicable in all Member States'."
    confidence: high
    valid_from: 2024-12-10
    valid_until: null
  - type: references
    target: EU-NIS2
    source: fact
    evidence: "Article 3 takes definitions from Directive (EU) 2022/2555: 'incident' (point 43, 'as defined in Article 6, point (6)'), 'near miss' (point 45) and 'CSIRT designated as coordinator' (point 51, 'pursuant to Article 12(1) of Directive (EU) 2022/2555'); Article 14(1) has manufacturers notify actively exploited vulnerabilities to that CSIRT and to ENISA. Read directly 2026-11-14."
    confidence: high
    valid_from: null
    valid_until: null
  - type: references
    target: EU-CYBERSECURITY-ACT
    source: fact
    evidence: "Article 3, point (46): 'cyber threat' means a cyber threat 'as defined in Article 2, point (8), of Regulation (EU) 2019/881'. Read directly 2026-11-14."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Regulation (EU) 2024/2847 (Cyber Resilience Act), Official Journal text"
    url: "https://publications.europa.eu/resource/celex/32024R2847"
    publisher: "Publications Office of the European Union"
    accessed: "2026-11-14"
---

# Cyber Resilience Act (Regulation (EU) 2024/2847)

> **Created 2026-11-14** (roadmap #771). The Official Journal text was downloaded from the Publications Office and read
> directly: the title, Articles 1, 2, 3 (points 42 to 51), 14(1) and (2) opening, 16(1), 52(1) and (2), 64(1) and (2) and
> 71. The rest, including the annexes, was not read.

## What the text says

- **Title and dates.** "Regulation (EU) 2024/2847 of the European Parliament and of the Council of 23 October 2024 on
  horizontal cybersecurity requirements for products with digital elements and amending Regulations (EU) No 168/2013 and
  (EU) No 2019/1020 and Directive (EU) 2020/1828 (Cyber Resilience Act)", OJ L, 2024/2847, 20.11.2024.
- **Three dates of application** (Article 71): generally from **11 December 2027**; Article 14 (reporting by
  manufacturers) from **11 September 2026**; Chapter IV (Articles 35 to 51) from **11 June 2026**. It entered into force
  on the twentieth day after publication, which is 10 December 2024; that computed date is the `start_date`, and the
  status is `adopted` because the Regulation does not yet apply in general, as with [[EU-EURO-7]].
- **Content** (Article 1): rules for making products with digital elements available on the market, essential
  cybersecurity requirements for their design, development and production, requirements for manufacturers'
  vulnerability handling, and rules on market surveillance and enforcement.
- **Scope** (Article 2): products with digital elements whose intended or foreseeable use includes a data connection to
  a device or network. Products covered by the medical devices regulations and Regulation (EU) 2019/2144, and products
  certified under Regulation (EU) 2018/1139, are out of scope.
- **Reporting** (Articles 14 and 16): a manufacturer notifies an actively exploited vulnerability to the CSIRT designated
  as coordinator and to ENISA, with an early warning within 24 hours, through a single reporting platform that
  [[EU-ENISA]] establishes and runs.
- **Enforcement** (Articles 52 and 64): each Member State designates market surveillance authorities. Breaches of the
  essential requirements and of Articles 13 and 14 carry fines of up to EUR 15 million or 2.5 percent of total worldwide
  annual turnover, whichever is higher.

## Not modelled

- The national market surveillance authorities: none was read.
- The acts it amends (Regulations (EU) No 168/2013 and (EU) 2019/1020, Directive (EU) 2020/1828) are not Atlas entities.
- ENISA's role is under `organisations` and in prose; the convention records `governed-by` on the body.

## Sources

Listed in frontmatter, read directly.
