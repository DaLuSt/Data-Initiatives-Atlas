---
id: EU-EDIB
type: organisation
name: European Data Innovation Board
alternative_names:
  - EDIB
description: >
  The expert group that Article 29 of the Data Governance Act requires the Commission to establish. It consists of
  representatives of the Member States' competent authorities for data intermediation services and for the registration
  of data altruism organisations, the European Data Protection Board, the European Data Protection Supervisor, ENISA,
  the Commission, the EU SME Envoy and other relevant bodies. It advises and assists the Commission, among other things
  on consistent practice for data intermediation and data altruism. The Commission's own page says it has been
  established.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-11-14"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - EU-COMMISSION
  - EU-EDPB
  - EU-EDPS
  - EU-ENISA
related_entities:
  - EU-DGA
  - EU-COMMON-DATA-SPACES
relationships:
  - type: governed-by
    target: EU-DGA
    source: fact
    evidence: "Regulation (EU) 2022/868, read directly 2026-11-14 from the Publications Office (CELEX 32022R0868): Article 1(1)(d), the Regulation lays down 'a framework for the establishment of a European Data Innovation Board'; Article 29(1), 'The Commission shall establish a European Data Innovation Board in the form of an expert group'; Article 30 lists its tasks."
    confidence: high
    valid_from: null
    valid_until: null
  - type: part-of
    target: EU
    source: fact
    evidence: "Article 29(1) of Regulation (EU) 2022/868 makes it a Commission expert group at Union level. The Commission's page 'Data Governance Act explained' (last updated 3 July 2026, read 2026-11-14 through a summarising fetch tool) says: 'As provided in the DGA, the Commission established the European Data Innovation Board (EDIB)'."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Regulation (EU) 2022/868 (Data Governance Act), Official Journal text"
    url: "https://publications.europa.eu/resource/celex/32022R0868"
    publisher: "Publications Office of the European Union"
    accessed: "2026-11-14"
  - title: "Data Governance Act explained"
    url: "https://digital-strategy.ec.europa.eu/en/policies/data-governance-act-explained"
    publisher: "European Commission"
    accessed: "2026-11-14"
---

# European Data Innovation Board

> **Created 2026-11-14** (roadmap #771). Articles 1, 29 and 30 (points a to d) and 38 of the Data Governance Act were read
> directly from the Official Journal text. That the Board exists today rests on the Commission's own explainer page,
> read through a summarising fetch tool, so `confidence` is medium.

## What the sources say

- **Legal basis.** [[EU-DGA]] Article 29(1): the Commission "shall establish a European Data Innovation Board in the form
  of an expert group".
- **Who sits on it** (Article 29(1)): representatives of the competent authorities for data intermediation services and
  for the registration of data altruism organisations of all Member States, [[EU-EDPB]], [[EU-EDPS]], [[EU-ENISA]], the
  Commission, the EU SME Envoy or a representative of the network of SME envoys, and other representatives of relevant
  bodies in specific sectors and with specific expertise.
- **Subgroups** (Article 29(2)): at least three, one of the competent authorities, one for technical discussions on
  standardisation, portability and interoperability, and one for stakeholder involvement that includes the common
  European data spaces.
- **Tasks** (Article 30, first four read): to advise and assist the Commission on a consistent practice for re-use
  requests for protected public-sector data, for data altruism, and for the supervision of data intermediation services
  and data altruism organisations, and on guidelines for protecting commercially sensitive non-personal data.
- **Whether it exists.** The Commission's explainer says the Commission established it and that it "will have the power
  to propose guidelines for Common European Data Spaces".

## Not established

- **When it was set up.** A search result describing the Commission's register of expert groups (entry E03903) gives a
  Commission Decision of 20 February 2023 and meetings up to an eleventh on 16 June 2026. The register page itself
  returns only its title to the fetch tool, so the date is not recorded in `start_date`.
- The seats of [[EU-EDPB]], [[EU-EDPS]] and [[EU-ENISA]] are listed under `organisations` and in prose, not as
  `participates-in` edges on those bodies; that can follow once the membership is read from the register.
- The [[EU-DIGITAL-OMNIBUS]] would move the Data Governance Act's content into the Data Act; what that does to the
  Board was not read.

## Sources

Listed in frontmatter. The Regulation was read directly; the Commission page through a summarising fetch tool.
