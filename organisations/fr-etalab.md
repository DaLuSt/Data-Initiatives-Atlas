---
id: FR-ETALAB
type: organisation
name: Etalab
alternative_names: []
description: >
  Department of the Direction interministérielle du numérique responsible
  for the state's open data policy. Created by decree on 21 February 2011
  as a mission attached to the Secrétariat général du Gouvernement; became
  a DINUM department in 2019, with its missions and organisation set by
  the decree of 30 October 2019. It coordinates and promotes the action of
  the state and its supervised bodies on the inventory, governance,
  production, circulation, exploitation and opening of data, including
  source code, and administers the interministerial portal data.gouv.fr.

level: national
country: FR
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2011-02-21
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - FR-DINUM
  - FR-DATA-GOUV
relationships:
  - type: part-of
    target: FR-DINUM
    source: fact
    evidence: "Confirmed verbatim by reading data.gouv.fr's own organisation page directly (2026-08-26): 'Etalab est un département de la direction interministérielle du numérique (DINUM), dont les missions et l'organisation sont fixées par le décret du 30 Octobre 2019' (Etalab is a department of DINUM, whose missions and organisation are set by the decree of 30 October 2019). fr.wikipedia.org's page, also read directly, adds a founding date this entity previously said was unestablished: 'La mission Etalab a été créée par décret le 21 février 2011' (the Etalab mission was created by decree on 21 February 2011), originally placed under the Prime Minister's authority and attached to the Secrétariat général du Gouvernement, before becoming a DINUM department in 2019."
    confidence: medium
    valid_from: 2019-10-30
    valid_until: null

sources:
  - title: "Organisation — Etalab | data.gouv.fr"
    url: "https://www.data.gouv.fr/organizations/etalab/datasets"
    publisher: "data.gouv.fr"
    accessed: "2026-08-26"
  - title: "Etalab"
    url: "https://fr.wikipedia.org/wiki/Etalab"
    publisher: "Wikipédia"
    accessed: "2026-08-26"
  - title: "Etalab — data.gouv.fr"
    url: "https://www.data.gouv.fr/en/organizations/etalab/"
    publisher: "data.gouv.fr"
    accessed: "2026-08-26"
  - title: "Etalab — Centre de ressources et d'ingénierie documentaires de l'INSP"
    url: "https://documentation.insp.gouv.fr/insp/doc/SYRACUSE/360515/etalab?_lg=fr-FR"
    publisher: "Institut national du service public (INSP)"
    accessed: "2026-08-26"
  - title: "Chronologie de l'open data"
    url: "https://guides.etalab.gouv.fr/juridique/chronologie/"
    publisher: "Etalab — guides.etalab.gouv.fr"
---

# Etalab

> **Verified 2026-08-26, and a founding date finally sourced.** Four of
> five cited pages were read directly. data.gouv.fr's own page confirms
> the 2019 DINUM-department decree verbatim, and fr.wikipedia.org
> supplies a founding date — 21 February 2011 — this entity previously
> said was unestablished.

## Description

Confirmed verbatim by reading data.gouv.fr's own organisation page
directly (2026-08-26): Etalab is the department of [[FR-DINUM]]
responsible for the French state's open data policy. It was **created
by decree on 21 February 2011**, as a mission attached to the
Secrétariat général du Gouvernement under the Prime Minister's
authority (fr.wikipedia.org, read directly). **In 2019 it became a
DINUM department**, with its missions and organisation set by the
**decree of 30 October 2019**.

Its remit is broader than publishing datasets. It coordinates and promotes
the action of the state and the bodies under its supervision on the
**inventory, governance, production, circulation, exploitation and opening**
of data — **including source code**.

It administers [[FR-DATA-GOUV]], the interministerial portal intended to
gather and freely provide the public information of the state, its public
establishments, and — where they wish — territorial authorities and bodies
charged with a public service mission.

## A structural contrast worth recording

Etalab is the only national open-data body in the Atlas that is **a
department inside the central digital-government organisation** rather than
a separate institution or a shared product:

| Country | Open data run by | Relationship to the digital-government body |
|---|---|---|
| France | **Etalab** | a **department of** [[FR-DINUM]] |
| Belgium | [[BE-BOSA]] | the same service, no separate body |
| Germany | [[DE-FITKO]] | a **Bund-Länder institution** running it as a product |
| Netherlands | — | [[NL-DATA-OVERHEID]] is modelled without a custodian |

The Dutch row is a gap, not a finding: no custodian was ever established
for [[NL-DATA-OVERHEID]]. Three countries now have one, which makes the
omission visible. Logged in `discovery/research-queue.md`.

`start_date: 2011-02-21` is now Etalab's own founding date, confirmed
by reading fr.wikipedia.org directly this pass — closing the gap this
entity previously left as "no founding date is recorded." The
`part-of` [[FR-DINUM]] relationship's `valid_from: 2019-10-30` is the
separate, later date Etalab became a DINUM department, not its
founding.

## Relationships

- `part-of` [[FR-DINUM]].

Inbound: [[FR-DATA-GOUV]] is `maintained-by` this entity.

## Sources

Listed in frontmatter, four of five read directly this pass;
`guides.etalab.gouv.fr` no longer resolves at all — a dead domain,
apparently superseded by `guides.data.gouv.fr` (see [[FR-LRN]]).
