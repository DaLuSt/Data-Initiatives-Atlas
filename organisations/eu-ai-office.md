---
id: EU-AI-OFFICE
type: organisation
name: AI Office
alternative_names:
  - European AI Office
description: >
  A function of the European Commission, not a separate body: the AI Act defines the AI Office as "the Commission's
  function of contributing to the implementation, monitoring and supervision of AI systems and general-purpose AI
  models, and AI governance, provided for in Commission Decision of 24 January 2024", and says references to the AI
  Office are to be read as references to the Commission. Through it the Commission develops Union expertise and
  capabilities in AI, and it attends the meetings of the European Artificial Intelligence Board without voting.

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
related_entities:
  - EU-AI-ACT
relationships:
  - type: part-of
    target: EU-COMMISSION
    source: fact
    evidence: "Regulation (EU) 2024/1689, read directly 2026-11-14 from the Publications Office (CELEX 32024R1689), Article 3, point (47): 'AI Office' means 'the Commission’s function of contributing to the implementation, monitoring and supervision of AI systems and general-purpose AI models, and AI governance, provided for in Commission Decision of 24 January 2024; references in this Regulation to the AI Office shall be construed as references to the Commission'."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: EU-AI-ACT
    source: fact
    evidence: "Regulation (EU) 2024/1689, Article 64: '1. The Commission shall develop Union expertise and capabilities in the field of AI through the AI Office. 2. Member States shall facilitate the tasks entrusted to the AI Office, as reflected in this Regulation.' Article 65(2): 'The AI Office shall also attend the Board’s meetings, without taking part in the votes.' Read directly 2026-11-14."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Regulation (EU) 2024/1689 (Artificial Intelligence Act), Official Journal text"
    url: "https://publications.europa.eu/resource/celex/32024R1689"
    publisher: "Publications Office of the European Union"
    accessed: "2026-11-14"
---

# AI Office

> **Created 2026-11-14** (roadmap #771). Sourced from the AI Act's own text, read directly: Article 3, point (47), and
> Articles 64 and 65(1) and (2). The Commission Decision of 24 January 2024 that the definition names was not read, so
> what it provides (structure, staffing, the date the Office began work) is not recorded and `confidence` is medium.

## What the text says

- **What it is** ([[EU-AI-ACT]] Article 3(47)): a function of [[EU-COMMISSION]], provided for in a Commission Decision of
  24 January 2024. Wherever the Regulation says "AI Office", it means the Commission.
- **What it is for** (Article 64): the Commission develops Union expertise and capabilities in AI through it, and Member
  States facilitate its tasks.
- **The Board** (Article 65): the European Artificial Intelligence Board has one representative per Member State; the
  European Data Protection Supervisor participates as observer and the AI Office attends without voting.

## Why it is an entity although it is not a separate body

The AI Act assigns tasks to it by name, and readers look for it by name. Recording it as `part-of` the Commission, with
the definition quoted, says exactly what it is and keeps the supervision of the AI Act from ending in prose.

## Not modelled

- The **European Artificial Intelligence Board** and the national market surveillance and notifying authorities.
- `start_date`: the Decision's date is known from the Regulation, the date the Office started work is not.
- The AI Act's own dates are on [[EU-AI-ACT]] and [[EU-DIGITAL-OMNIBUS-AI]]; Article 113 as adopted (application from 2
  August 2026, with earlier and later dates for parts) was read here only in passing.

## Sources

Listed in frontmatter, read directly.
