---
id: FR-ETALAB
type: organisation
name: Etalab
alternative_names: []
description: >
  Department of the Direction interministérielle du numérique responsible
  for the state's open data policy. Its missions and organisation were set
  by the decree of 30 October 2019, when it became a DINUM department. It
  coordinates and promotes the action of the state and its supervised
  bodies on the inventory, governance, production, circulation,
  exploitation and opening of data, including source code, and administers
  the interministerial portal data.gouv.fr.

level: national
country: FR
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2019-10-30
end_date: null
last_verified: null
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
    evidence: "In 2019 Etalab became a department of DINUM, with its missions and organisation set by the decree of 30 October 2019 (fr.wikipedia.org 'Etalab'; numerique.gouv.fr). NOT READ — search-only."
    confidence: medium
    valid_from: 2019-10-30
    valid_until: null

sources:
  - title: "Etalab"
    url: "https://fr.wikipedia.org/wiki/Etalab"
    publisher: "Wikipédia"
  - title: "Organisation — Etalab | data.gouv.fr"
    url: "https://www.data.gouv.fr/organizations/etalab/datasets"
    publisher: "data.gouv.fr"
  - title: "Etalab — data.gouv.fr"
    url: "https://www.data.gouv.fr/en/organizations/etalab/"
    publisher: "data.gouv.fr"
  - title: "Etalab — Centre de ressources et d'ingénierie documentaires de l'INSP"
    url: "https://documentation.insp.gouv.fr/insp/doc/SYRACUSE/360515/etalab?_lg=fr-FR"
    publisher: "Institut national du service public (INSP)"
  - title: "Chronologie de l'open data"
    url: "https://guides.etalab.gouv.fr/juridique/chronologie/"
    publisher: "Etalab — guides.etalab.gouv.fr"
---

# Etalab

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

Etalab is the department of [[FR-DINUM]] responsible for the French state's
open data policy. **In 2019 it became a DINUM department**, with its
missions and organisation set by the **decree of 30 October 2019**.

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

`start_date: 2019-10-30` is the date Etalab became a DINUM department, not
the date Etalab was created — it existed before as a separate mission. **No
founding date is recorded**, because none was established.

## Relationships

- `part-of` [[FR-DINUM]].

Inbound: [[FR-DATA-GOUV]] is `maintained-by` this entity.

## Sources

Listed in frontmatter.
