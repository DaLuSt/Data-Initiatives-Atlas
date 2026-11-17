---
id: EU-EDPS
type: organisation
name: European Data Protection Supervisor
alternative_names:
  - EDPS
description: >
  Independent data protection authority supervising the processing of
  personal data by EU institutions and bodies. It appoints a representative
  to the European Data Protection Board and issues opinions, often jointly
  with the Board, on EU legislative proposals.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-11-17"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-EDPB
relationships:
  - type: part-of
    target: EU
    source: fact
    evidence: "Regulation (EU) 2018/1725 (CELEX 32018R1725), read directly 2026-11-17 from the Official Journal text: Article 52(1), \"The European Data Protection Supervisor is hereby established\", and 52(2), it 'shall be responsible for ensuring that the fundamental rights and freedoms of natural persons, and in particular their right to data protection, are respected by Union institutions and bodies'. Article 55(1): it acts 'with complete independence'. A body established by Union law, hence `part-of` the EU as its scope anchor; it is not one of the institutions TEU Article 13(1) lists."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-EDPB
    source: fact
    evidence: "Regulation (EU) 2016/679, read directly 2026-11-17 from the Official Journal text (Publications Office, CELEX 32016R0679): Article 68(3), 'The Board shall be composed of the head of one supervisory authority of each Member State and of the European Data Protection Supervisor, or their respective representatives.'"
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "EDPB and EDPS support strengthening EU's cybersecurity — press release"
    url: "https://www.edps.europa.eu/press-publications/press-news/press-releases/2026/edpb-and-edps-support-strengthening-eus-cybersecurity-and-easing-compliance-while-protecting-individuals-personal-data_en"
    publisher: "European Data Protection Supervisor"
  - title: "Official Journal text (CELEX 32016R0679)"
    url: "https://publications.europa.eu/resource/celex/32016R0679"
    publisher: "Publications Office of the European Union"
    accessed: "2026-11-17"
  - title: "Regulation (EU) 2018/1725, Articles 52 and 55"
    url: "https://eur-lex.europa.eu/eli/reg/2018/1725/oj/eng"
    publisher: "EUR-Lex (Publications Office of the European Union)"
    accessed: "2026-11-17"
---

# European Data Protection Supervisor (EDPS)

> **Verified 2026-08-21.** Every source this entity cites is on a domain the
> repository owner confirmed read and correct — `europa.eu`. `verification:
> primary-source`. See `docs/re-verification.md` §"The confirmed domains".

## Description

The EDPS is an independent data protection authority whose supervisory remit
covers the EU institutions and bodies themselves — as distinct from
[[NL-AP]] and its counterparts, which supervise within member states. It
appoints one representative to [[EU-EDPB]].

In practice the EDPS and the EDPB issue joint opinions on EU legislative
proposals; a 2026 joint opinion on cybersecurity and network and information
security is among the sources here. The EDPS also issued an opinion on
[[EU-DATA-STRATEGY]] in 2020, cited in that entity's research.

`coverage: low`: the supervisory function over EU institutions, and the
EDPS's opinion practice, were not researched.

## Relationships

- Participates in [[EU-EDPB]].

## Sources

Listed in frontmatter — a single source, and a press release rather than an
institutional description.
