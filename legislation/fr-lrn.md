---
id: FR-LRN
type: law
name: Loi pour une République numérique
alternative_names:
  - Loi n° 2016-1321 du 7 octobre 2016
  - Loi Lemaire
  - Digital Republic Act
description: >
  French act of 7 October 2016 for a Digital Republic. It established open
  data by default for public administrations and made open data an
  obligation for local authorities with more than 3,500 inhabitants.

level: national
country: FR
region: EU

status: active
confidence: medium
coverage: low
verification: search-only

start_date: 2016-10-07
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - FR
  - FR-DATA-GOUV
  - EU-OPEN-DATA-DIRECTIVE
  - FR-LOI-VALTER
relationships:
  - type: applies-in
    target: FR
    source: fact
    evidence: "The loi pour une République numérique is a French act of 7 October 2016 establishing open data by default for public administrations and making open data an obligation for local authorities with more than 3,500 inhabitants (legifrance.gouv.fr; numerique.gouv.fr). NOT READ — search-only. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "LOI n° 2016-1321 du 7 octobre 2016 pour une République numérique"
    url: "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000033202746"
    publisher: "Légifrance (Direction de l'information légale et administrative)"
  - title: "Chronologie de l'open data"
    url: "https://guides.etalab.gouv.fr/juridique/chronologie/"
    publisher: "Etalab — guides.etalab.gouv.fr"
  - title: "Chronologie juridique de l'open data"
    url: "https://guides.data.gouv.fr/guides/guide-juridique/chronologie-de-lopen-data"
    publisher: "data.gouv.fr"
  - title: "Le cadre juridique de l'open data en France"
    url: "https://datactivist.coop/ardeche/rapport/partie2.html"
    publisher: "Datactivist"
  - title: "Open Data : ce qu'il faut retenir de la Loi Lemaire"
    url: "https://www.decideo.fr/Open-Data-ce-qu-il-faut-retenir-de-la-Loi-Lemaire_a9297.html"
    publisher: "Decideo"
---

# Loi pour une République numérique (2016)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The **loi n° 2016-1321 of 7 October 2016**, known as the *loi Lemaire*,
established the principle of **open data by default** in French public
administration and made open data an **obligation for local authorities
with more than 3,500 inhabitants**.

`coverage: low`: this act is wide-ranging — it also covers platform loyalty,
net neutrality and digital rights — and only its open-data provisions are
recorded here, because only those were sourced.

## ⚠ This is not France's Open Data Directive transposition

The same trap Belgium sprang, and it is worth stating in the same terms.

- This act is from **2016**.
- [[EU-OPEN-DATA-DIRECTIVE]] is Directive (EU) **2019**/1024.

A 2016 act cannot transpose a 2019 directive, so **no
`implements-requirement-from` is asserted**. The Etalab and data.gouv.fr
open-data chronologies place this act in a lineage that runs from the 2003
PSI Directive (2003/98/EC) — which is not an Atlas entity — rather than
from the Open Data Directive.

France's actual transposition of Directive (EU) 2019/1024 is understood to
be a 2021 ordinance, but **no source read identifies it**, so it is not
recorded. That leaves the four-country picture:

| Country | Open Data Directive transposition |
|---|---|
| Netherlands | [[NL-WHO]] — recorded |
| Germany | [[DE-DNG]] — recorded |
| Belgium | **not identified** |
| France | **not identified** |
| Spain | [[ES-LEY-37-2007]] — recorded, as amended in 2021 |

Two of five countries now have a visible gap here, both for the same
reason: each has a well-known, easily-found *earlier* open data act that
looks like the answer and is not. The Atlas records the earlier acts and
declines to mislabel them.

Both gaps, and the unmodelled PSI Directive that would give these acts
somewhere to point, are in `discovery/research-queue.md`.

## Relationships

**None asserted.** `related_entities` records the association with
[[EU-OPEN-DATA-DIRECTIVE]] for navigation only — deliberately not as a
relationship — and with [[FR-DATA-GOUV]], which this act's obligations feed
but which no source connects to it directly.

## Sources

Listed in frontmatter, including the **Légifrance JORF entry** — the
strongest citation available for a French act, and one [[FR-LIL]] lacks.
