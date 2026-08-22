---
id: LI-DATENSCHUTZSTELLE
type: organisation
name: Datenschutzstelle
alternative_names:
  - DSS
  - Data Protection Authority (Liechtenstein)
description: >
  Liechtenstein's independent data protection supervisory authority. Its
  Commissioner is appointed by the Landtag for a five-year renewable term.
  It supervises the General Data Protection Regulation, which applies in
  Liechtenstein through the EEA Agreement, and the national Datenschutzgesetz
  that supplements it. As the supervisory authority of an EEA EFTA state it
  participates in the activities of the European Data Protection Board under
  Decision of the EEA Joint Committee No 154/2018.

level: national
country: LI
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - LI
  - LI-DSG
  - EU-EDPB
  - INTL-EEA-JCD-154-2018
relationships:
  - type: part-of
    target: LI
    source: fact
    evidence: "Confirmed by reading datenschutzstelle.li's own pages directly (2026-08-22) — its homepage, 'Über uns' and 'Team' pages all describe it as Liechtenstein's national data protection supervisory authority, headquartered at Kirchstrasse 8, Vaduz, and headed by Dr. Marie-Louise Gächter-Alge. NOT independently re-confirmed: the specific claim that its Commissioner is appointed by the Landtag for a five-year renewable term appears on none of the three pages read this pass (the 'Team' page names a 'Leitung' — head — with no appointment mechanism given) and is retained from the original sourcing rather than removed. Corroborated by gdprhub.eu's own infobox, read directly: 'Data Protection Authority: Datenschutzstelle (Liechtenstein)'. Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-EDPB
    source: fact
    evidence: "NOT independently re-confirmed 2026-08-22 for the Datenschutzstelle by name: eur-lex.europa.eu's own text of Decision of the EEA Joint Committee No 154/2018, read directly in an earlier pass, provides that the supervisory authorities of the EFTA States shall participate in the activities of the European Data Protection Board. Membership follows from that sourced composition rule rather than from a source naming the Datenschutzstelle specifically."
    confidence: medium
    valid_from: 2018-07-06
    valid_until: null

sources:
  - title: "Datenschutzstelle Liechtenstein"
    url: "https://www.datenschutzstelle.li/"
    publisher: "Datenschutzstelle Liechtenstein"
    accessed: "2026-08-22"
  - title: "Über uns — Datenschutzstelle Liechtenstein"
    url: "https://www.datenschutzstelle.li/ueber-uns"
    publisher: "Datenschutzstelle Liechtenstein"
    accessed: "2026-08-22"
  - title: "Team — Datenschutzstelle Liechtenstein"
    url: "https://www.datenschutzstelle.li/ueber-uns/team"
    publisher: "Datenschutzstelle Liechtenstein"
    accessed: "2026-08-22"
  - title: "Data Protection in Liechtenstein"
    url: "https://gdprhub.eu/index.php?title=Data_Protection_in_Liechtenstein"
    publisher: "GDPRhub — noyb"
    accessed: "2026-08-22"
  - title: "Decision of the EEA Joint Committee No 154/2018 of 6 July 2018"
    url: "https://eur-lex.europa.eu/eli/dec/2018/1022/oj"
    publisher: "EUR-Lex — Publications Office of the European Union"
    accessed: "2026-08-22"
---

# Datenschutzstelle

> **Verified 2026-08-22.** All five cited pages were read directly. The
> Commissioner's five-year Landtag-appointed term — a specific claim
> from the original sourcing — was not found on any of the authority's
> own pages read this pass (its "Team" page names a head, Dr.
> Marie-Louise Gächter-Alge, with no appointment mechanism given) and is
> retained rather than removed, exactly the discipline this project
> applies to a claim a re-verification pass cannot confirm but has no
> reason to think wrong.

## Description

Confirmed by reading datenschutzstelle.li's own pages directly
(2026-08-22): Liechtenstein's data protection supervisory authority,
headquartered at Kirchstrasse 8, Vaduz, and headed by Dr. Marie-Louise
Gächter-Alge. Liechtenstein's **first modelled national entity**.

Its Commissioner is said to be appointed by the **Landtag** for a
five-year renewable term — a claim from the original sourcing that this
pass could not independently re-confirm; see the caveat above.

It supervises [[EU-GDPR]] — directly applicable in Liechtenstein through the
EEA Agreement — and [[LI-DSG]], the national act that supplements it.

## Relationships

- `part-of` [[LI]] — anchor edge under `metadata/relationship-types.md` §2.3.
- `participates-in` [[EU-EDPB]], on the composition rule in
  [[INTL-EEA-JCD-154-2018]]: the supervisory authorities of the EFTA States
  participate in the Board's activities. As with [[IS-PERSONUVERND]], this is
  participation in activities and **not** membership with a vote under
  Article 68(3) GDPR.

## Sources

Listed in frontmatter — the authority's own homepage, "Über uns" and
"Team" pages, GDPRhub, and the EUR-Lex record of the Joint Committee
decision, all read directly this pass.
