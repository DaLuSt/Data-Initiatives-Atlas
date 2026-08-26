---
id: PL-MC
type: organisation
name: Ministerstwo Cyfryzacji
alternative_names:
  - MC
  - Ministry of Digital Affairs
  - Ministry of Digitization
description: >
  Polish ministry responsible for digital affairs. It is the supervisory
  body that sets the development directions for the Centralny Ośrodek
  Informatyki and supervises it in the scope of the tasks entrusted to it,
  implements policy for eliminating paper document circulation in public
  administration, and monitors the rollout of the EZD RP electronic document
  management system. It announced the draft law converting the Centralny
  Ośrodek Informatyki into an Agencja Informatyzacji, and it is the ministry
  that indicated new digital identity solutions would be made available by
  the end of 2026.

level: national
country: PL
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - PL-COI
  - PL-MOBYWATEL
  - PL-NASK
relationships: []

sources:
  - title: "Ministerstwo Cyfryzacji — Portal Gov.pl"
    url: "https://www.gov.pl/web/cyfryzacja"
    publisher: "Ministerstwo Cyfryzacji"
    accessed: "2026-08-26"
  - title: "Centralny Ośrodek Informatyki — Ministerstwo Cyfryzacji"
    url: "https://www.gov.pl/web/cyfryzacja/centralny-osrodek-informatyki"
    publisher: "Ministerstwo Cyfryzacji"
    accessed: "2026-08-26"
  - title: "Centralny Ośrodek Informatyki przekształci się w Agencję Informatyzacji"
    url: "https://www.gov.pl/web/cyfryzacja/centralny-osrodek-informatyki-przeksztalci-sie-w-agencje-informatyzacji-co-usprawni-realizacje-zadan-w-obszarze-informatyzacji-panstwa"
    publisher: "Ministerstwo Cyfryzacji"
    accessed: "2026-08-26"
  - title: "Departament Transformacji Cyfrowej — Ministerstwo Cyfryzacji"
    url: "https://www.gov.pl/web/cyfryzacja/departament-transformacji-cyfrowej"
    publisher: "Ministerstwo Cyfryzacji"
    accessed: "2026-08-26"
  - title: "Ustawa o aplikacji mObywatel (tekst skonsolidowany)"
    url: "https://lexlege.pl/ustawa-o-aplikacji-mobywatel/"
    publisher: "LexLege"
    accessed: "2026-08-26"
---

# Ministerstwo Cyfryzacji

> **Verified 2026-08-26.** All four cited pages were read directly, and
> confirm every claim this entity carried, verbatim. A fifth source —
> the mObywatel Act's own text — was read too, and closes a gap flagged
> on [[PL-MOBYWATEL]]: see below.

## Description

The Ministry of Digital Affairs is Poland's central digital-government
department. Confirmed by reading its own Departament Transformacji
Cyfrowej page directly: it "realizuje politykę eliminacji obiegu
dokumentacji papierowej w administracji publicznej" (implements policy
for eliminating paper document circulation in public administration) and
"monitoruje wdrażanie systemu EZD RP" (monitors the rollout of the EZD RP
system) — matching this entity's prior description word for word. Within
the Atlas's scope it:

- **supervises [[PL-COI]]** as a budgetary institution ("Organ nadrzędny:
  Ministerstwo Cyfryzacji", confirmed by reading COI's own gov.pl page
  directly) and sets its development directions;
- **is also NASK's supervising ministry** — see [[PL-NASK]], confirmed
  this pass, previously unestablished;
- **is the statutory legal operator of [[PL-MOBYWATEL]]** — see below;
- announced the draft law converting COI into an **Agencja Informatyzacji**;
- stated that new digital identity solutions would be available by the end
  of 2026, after [[PL-MOBYWATEL]] was found unable to serve as an EUDI
  Wallet.

## Closing the mObywatel operator gap

[[PL-MOBYWATEL]] previously flagged that "which body is its legal
operator was not established," with [[PL-COI]] sourced only as
maintaining the application's *systems*. Reading the mObywatel Act's own
consolidated text directly this pass finds the answer in the Act itself:
Article 19 names "minister właściwy do spraw informatyzacji" — the
Ministry of Digital Affairs — as the body that "udostępnia, utrzymuje
oraz zapewnia rozwój aplikacji mObywatel" (provides, maintains and
ensures development of the application), and Article 20 makes the same
minister the personal-data administrator for its users. The
`maintained-by` edge is recorded on [[PL-MOBYWATEL]], pointing here.

## The sixth central digital-government body

| Country | Body | Form |
|---|---|---|
| Netherlands | [[NL-BZK]] | ministry, with [[NL-LOGIUS]] as the implementing service |
| Germany | [[DE-BMDS]] | ministry |
| Belgium | [[BE-BOSA]] | federal public service |
| France | [[FR-DINUM]] | interministerial directorate under the Prime Minister |
| Spain | [[ES-AEAD]] | **state agency**, transformed from a directorate in 2025 |
| **Poland** | **Ministerstwo Cyfryzacji** | **ministry, with [[PL-COI]] as the implementing body** |

The Polish arrangement is closest to the Dutch: a ministry that sets
direction plus a separate operational organisation that runs the systems.
Whether that similarity is structural or coincidental is not something the
Atlas can establish — **no relationship between the two pairs is asserted**,
for the same reason no relationship connects the national identity systems.

## Still unrecorded

The ministry's founding, legal basis, internal structure beyond the named
Departament Transformacji Cyfrowej, and its relationship to the Prime
Minister's Chancellery remain unestablished even after this pass.

## Relationships

None asserted from this entity — [[PL-COI]], [[PL-NASK]] and
[[PL-MOBYWATEL]] each carry an edge pointing here instead, all confirmed
or newly added this pass.

## Sources

Listed in frontmatter, all five read directly this pass.
