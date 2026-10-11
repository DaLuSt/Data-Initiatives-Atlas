---
id: DE-STATISTISCHER-BEIRAT
type: organisation
name: "Statistischer Beirat"
name_en: "Statistical Advisory Council"
alternative_names:
  - "Beirat"
  - "Statistical Advisory Council"
description: >
  The advisory council attached to Germany's Federal Statistical Office
  under § 4 of the Bundesstatistikgesetz. It advises the Office on
  statistical technical questions and represents the interests of the users
  of federal statistics.

level: national
country: DE
region: null

status: active
organisation_role: advisory
confidence: high
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-10-11"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - DE
  - DE-DESTATIS
  - DE-BSTATG
relationships:
  - type: part-of
    target: DE
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. § 4 of the Bundesstatistikgesetz, read directly on gesetze-im-internet.de (2026-10-11): 'Beim Statistischen Bundesamt besteht ein Statistischer Beirat, der es in statistischen Fachfragen berät und die Belange der Nutzer der Bundesstatistik vertritt.'"
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: DE-BSTATG
    source: fact
    evidence: "§ 4 BStatG (read 2026-10-11) creates the Beirat and gives it a Geschäftsordnung that needs the approval of the Federal Ministry of the Interior in agreement with the federal ministries."
    confidence: high
    valid_from: null
    valid_until: null
  - type: related-to
    target: DE-DESTATIS
    source: fact
    evidence: "§ 4 BStatG (read 2026-10-11): the Beirat exists 'beim Statistischen Bundesamt' and advises it. Advice and user representation, not oversight of the Office."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "§ 4 BStatG — Statistischer Beirat (Bundesstatistikgesetz)"
    url: "https://www.gesetze-im-internet.de/bstatg_1987/__4.html"
    publisher: "Bundesministerium der Justiz / juris (Gesetze im Internet)"
    accessed: "2026-10-11"
---

# Statistischer Beirat (Germany)

> **Created 2026-10-11** (roadmap #459, bodies beside statistical offices). § 4 of the Bundesstatistikgesetz was read directly. It is a user-representation and advice body, not an independent watchdog like [[GB-OSR]], [[FR-ASP]] or [[EU-ESGAB]]. The Beirat's membership and chair are not in § 4 as read; search summaries describe seats for ministries and others in an older version, and are not asserted.

## Description

Attached to the Federal Statistical Office ([[DE-DESTATIS]]) by § 4 BStatG ([[DE-BSTATG]]): it "berät es in statistischen Fachfragen" (advises it on statistical technical questions) and "vertritt die Belange der Nutzer der Bundesstatistik" (represents the interests of users of federal statistics). Its rules of procedure need the approval of the Federal Ministry of the Interior in agreement with the federal ministries.

## Relationships

`part-of` [[DE]] (anchor edge); `governed-by` [[DE-BSTATG]]; `related-to` [[DE-DESTATIS]].
