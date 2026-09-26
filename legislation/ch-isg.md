---
id: CH-ISG
type: law
name: Informationssicherheitsgesetz
alternative_names:
  - ISG
  - Bundesgesetz über die Informationssicherheit beim Bund
  - Federal Act on Information Security
description: >
  Swiss federal act on information security at the federal level (SR
  128), ensuring the secure processing of information the Confederation
  is responsible for and the secure use of its IT resources, protecting
  public interests including governmental decision-making capacity,
  internal and external security, and foreign-policy and economic
  interests. Adopted 18 December 2020; most provisions entered into
  force 1 January 2024 (Article 87 alone from 1 May 2022). Amended to
  add Articles 74a-74e, a mandatory 24-hour reporting duty for cyber
  attacks on critical infrastructure operators, in force since 1 April
  2025, enforced by the Federal Office for Cybersecurity (BACS).

level: national
country: CH
region: null

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: "2020-12-18"
end_date: null
last_verified: "2026-09-26"
previous_version: null
successor: null

domains:
  - DOMAIN-CYBERSECURITY
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - CH
  - CH-BACS
relationships:
  - type: part-of
    target: CH
    source: fact
    evidence: "Closes a gap CH-BACS's own file had flagged ('The ISG itself is still not an Atlas entity ... nothing exists in the graph to point the edge at'). Confirmed by reading fedlex.admin.ch's own HTML text directly (2026-09-26, via the filestore path documented in discovery/unresolved.md's eur-lex/fedlex workaround entries, since fedlex.admin.ch's main site renders client-side in JavaScript): 'Bundesgesetz über die Informationssicherheit beim Bund (Informationssicherheitsgesetz, ISG)', enacted by the Federal Assembly following the Federal Council's message of 22 February 2017, adopted 18 December 2020. Article 87 entered into force 1 May 2022; all other provisions entered into force 1 January 2024. Article 1 states its purpose: ensuring 'the secure processing of information for which the Confederation is responsible, as well as the secure use of the Confederation's IT resources.' Anchor edge under metadata/relationship-types.md §2.3, asserting Swiss national scope via `level: national`."
    confidence: high
    valid_from: "2024-01-01"
    valid_until: null

sources:
  - title: "Bundesgesetz über die Informationssicherheit beim Bund (Informationssicherheitsgesetz, ISG), SR 128 — consolidated text as of 1 January 2024"
    url: "https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/232/20240101/de/html/fedlex-data-admin-ch-eli-cc-2022-232-20240101-de-html.html"
    publisher: "Fedlex — The Publication Platform of Swiss Law (Federal Chancellery)"
    accessed: "2026-09-26"
  - title: "Informationssicherheitsgesetz — consolidated text as of 1 April 2025 (Articles 74a-74e)"
    url: "https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/232/20250401/de/html/fedlex-data-admin-ch-eli-cc-2022-232-20250401-de-html.html"
    publisher: "Fedlex — The Publication Platform of Swiss Law (Federal Chancellery)"
    accessed: "2026-09-26"
  - title: "Gesetzliche Grundlagen zur Meldepflicht"
    url: "https://www.bacs.admin.ch/de/gesetzliche-grundlagen-zur-meldepflicht"
    publisher: "Bundesamt für Cybersicherheit (BACS)"
    accessed: "2026-09-26"
---

# Informationssicherheitsgesetz (ISG)

> **Created 2026-09-26**, closing a gap [[CH-BACS]]'s own file had
> flagged (`discovery/unresolved.md` row #115: "The ISG itself is still
> not an Atlas entity ... nothing exists in the graph to point the edge
> at"). `fedlex.admin.ch`'s main site renders client-side in JavaScript
> and is unreadable directly, per the workaround already documented in
> `discovery/unresolved.md`'s known-source-blocks table — its
> `filestore` HTML path, read directly, worked instead. `bacs.admin.ch`'s
> own page was also read directly.

## Description

Confirmed by reading Fedlex's own text directly: the ISG (SR 128) is the
federal act ensuring "the secure processing of information for which the
Confederation is responsible, as well as the secure use of the
Confederation's IT resources" (Article 1), protecting governmental
decision-making capacity, Switzerland's internal and external security,
foreign-policy interests, economic and financial interests, and legal
obligations around information protection.

Enacted by the Federal Assembly following the Federal Council's message
of 22 February 2017, the Act was **adopted 18 December 2020**. Article
87 alone entered into force **1 May 2022**; every other provision
entered into force **1 January 2024**.

## The 2025 reporting-duty amendment, read at article level

[[CH-BACS]]'s own file already cited a secondary legal publication
(Bratschi AG) for the critical-infrastructure cyber-attack reporting
duty. Reading Fedlex's own consolidated text as of 1 April 2025 directly
gives the article-level detail precisely:

- **Article 74a** imposes the duty: authorities and organisations listed
  in Article 74b must ensure cyber attacks on their information systems
  are reported to BACS.
- **Article 74b** lists the covered entities: banks, insurers, hospitals,
  energy suppliers, telecommunications providers, transport companies,
  cantonal and municipal administrations, and software manufacturers
  whose products serve critical infrastructure, among others.
- **Article 74e** sets the deadline: "Die Meldung muss innert 24 Stunden
  nach der Entdeckung des Cyberangriffs erfolgen" — the report must be
  submitted within 24 hours of discovering the attack.

BACS's own page, read directly, confirms both instruments — the ISG and
the accompanying Cybersecurity Ordinance (CSV) — came into force
together: "Der Bundesrat hat die Meldepflicht für Cyberangriffe auf
kritische Infrastrukturen per 1. April 2025 in Kraft gesetzt."

## Not modelled

- The **Cybersecurity Ordinance (CSV)**, the implementing ordinance
  setting the 24-hour/14-day deadlines and CHF 100,000 enforcement fine
  already described in prose on [[CH-BACS]]'s own file — not split into
  a separate entity, matching the Atlas's convention of not splitting an
  ordinance from the act it implements absent a specific reason to.
- The Act's provisions beyond Article 1 (purpose) and Articles 74a-74e
  (reporting duty) — its full internal structure was not read this pass.

## Relationships

- `part-of` [[CH]] (anchor edge, `level: national`).

[[CH-BACS]] carries the reciprocal `governed-by` edge to this entity on
its own file, per the Atlas's "record the edge once" convention.

## Sources

Listed in frontmatter, all three read directly.
