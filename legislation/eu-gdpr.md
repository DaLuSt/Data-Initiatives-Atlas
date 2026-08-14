---
id: EU-GDPR
type: regulation
name: General Data Protection Regulation
alternative_names:
  - GDPR
  - Regulation (EU) 2016/679
  - Algemene verordening gegevensbescherming
  - AVG
description: >
  EU regulation on the protection of natural persons with regard to the
  processing of personal data and on the free movement of such data.
  Directly applicable across the Union; applicable from 25 May 2018.

level: regional
country: null
region: EU

status: active
confidence: low
coverage: low
verification: search-only

start_date: 2018-05-25
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-UAVG
  - NL-AP
relationships:
  - type: applies-in
    target: NL
    source: fact
    evidence: "As an EU regulation the GDPR is directly applicable in all member states; the Netherlands adopted the UAVG as implementing legislation, in force from the GDPR's date of application. NOT READ — search-only."
    confidence: medium
    valid_from: 2018-05-25
    valid_until: null

sources:
  - title: "General data protection regulation (GDPR) — summary"
    url: "https://eur-lex.europa.eu/EN/legal-content/summary/general-data-protection-regulation-gdpr.html"
    publisher: "EUR-Lex (Publications Office of the European Union)"
---

# General Data Protection Regulation (GDPR)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited page was confirmed to exist but was not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The GDPR — Regulation (EU) 2016/679 — governs the protection of natural
persons in relation to the processing of personal data and the free movement
of such data. It protects individuals when their data is processed by the
private sector and most of the public sector. It became applicable on
25 May 2018.

## Scope note

This is a deliberately **minimal EU anchor entity**, created in Batch 3
rather than Batch 8. Batch 3's scope explicitly includes "applicable
European legislation", and without this entity the Dutch implementation
chain — [[NL-UAVG]] → GDPR — could not be expressed at all, which is the
Atlas's central purpose. `coverage: low` reflects that it has not been
researched in its own right.

**Batch 8 should deepen this entity**, adding the full citation, the
legislative history, the relationship to the EDPB and EDPS, and
applicability to further countries as they join.

## Relationships

- Applies in [[NL]] (and in every other EU member state — those
  `applies-in` relationships should be added as those countries join the
  Atlas, per the country-neutral model).
- Implemented in Dutch law by [[NL-UAVG]].
- [[NL-AP]] is the Dutch supervisory authority designated under it.

## Sources

Listed in frontmatter. Note the cited source is a EUR-Lex *summary* page,
not the Official Journal text; Batch 8 should cite the authoritative text.
