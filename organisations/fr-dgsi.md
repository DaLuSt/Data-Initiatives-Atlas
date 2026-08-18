---
id: FR-DGSI
type: organisation
name: Direction générale de la Sécurité intérieure
alternative_names:
  - DGSI
  - Directorate-General for Internal Security
description: >
  France's internal intelligence service, under the authority of the
  Minister of the Interior, responsible for counter-espionage, internal
  surveillance and counter-terrorism. It belongs to the "premier cercle" of
  the French intelligence community and uses the intelligence-gathering
  techniques governed by the law of 24 July 2015, codified in Book VIII of
  the Code de la sécurité intérieure.

level: national
country: FR
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - FR-LOI-RENSEIGNEMENT-2015
  - FR-LIL
  - FR-DGSE
  - FR-DRM
  - FR-DRSD
  - FR-CNCTR
relationships:
  - type: governed-by
    target: FR-LIL
    source: fact
    evidence: "Title IV of the loi Informatique et Libertés contains the provisions applicable to processing concerning state security and defence; the national law remains fully applicable to files in the domain of intelligence and state security, and such processing must be authorised by decree after a reasoned and published opinion of the CNIL, with a decree in Conseil d'État where sensitive data are involved — the sources name CRISTINA, the file of the DGSI's predecessor, among the examples (cnil.fr 'La loi Informatique et Libertés'; cnil.fr 'Le cadre national'; fr.wikipedia.org 'Loi informatique et libertés'). NOT READ — search-only. The sources describe the state-security and defence regime and name an intelligence file rather than naming the DGSI as a controller, so this edge is weaker than the equivalent UK and Belgian ones."
    confidence: low
    valid_from: null
    valid_until: null
  - type: governed-by
    target: FR-LOI-RENSEIGNEMENT-2015
    source: fact
    evidence: "The DGSI, under the authority of the Minister of the Interior, handles counter-espionage, internal surveillance and counter-terrorism, and is one of the first-circle services holding the fullest legal authority to employ intelligence-gathering techniques under the Internal Security Code; the DGSI publishes its legal foundations under 'notre cadre légal' (dgsi.interieur.gouv.fr 'Les fondements'; cnctr.fr 'Les principaux services de renseignement'; interieur.gouv.fr 'La direction générale de la Sécurité intérieure'). NOT READ — search-only."
    confidence: medium
    valid_from: 2015-07-24
    valid_until: null

sources:
  - title: "Les fondements — notre cadre légal"
    url: "https://www.dgsi.interieur.gouv.fr/decouvrir-dgsi/notre-cadre-legal/fondements"
    publisher: "Direction générale de la Sécurité intérieure (DGSI)"
  - title: "La communauté du renseignement"
    url: "https://www.dgsi.interieur.gouv.fr/decouvrir-la-dgsi/nos-partenaires/la-communaute-du-renseignement"
    publisher: "Direction générale de la Sécurité intérieure (DGSI)"
  - title: "La direction générale de la Sécurité intérieure"
    url: "https://www.interieur.gouv.fr/ministere/direction-generale-de-securite-interieure"
    publisher: "Ministère de l'Intérieur"
---

# Direction générale de la Sécurité intérieure (DGSI)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

The DGSI is France's **internal** intelligence service, under the Minister of
the Interior. The sources give its remit as three functions:
counter-espionage, internal surveillance and counter-terrorism.

Its external counterpart is [[FR-DGSE]], under the Minister of the Armed
Forces.

## The comparison this entity supports

Across the Atlas, the domestic intelligence function sits in the interior
ministry in three countries and elsewhere in two:

| Country | Domestic service | Ministry |
|---|---|---|
| France | DGSI | Interior |
| Germany | [[DE-BFV]] | Interior ([[DE-BMI]]) |
| Netherlands | [[NL-AIVD]] | Interior ([[NL-BZK]]) |
| Belgium | [[BE-VSSE]] | **Justice** |
| United Kingdom | [[GB-MI5]] | Home Office |

Belgium is the outlier: its civilian service is a department of the FPS
Justice, not of an interior ministry.

Only [[DE-BFV]] and [[NL-AIVD]] carry a `part-of` edge, because only
[[DE-BMI]] and [[NL-BZK]] are Atlas entities. The French Ministry of the
Interior is not, so no edge is asserted here — the same coverage artefact
recorded on [[NL-MIVD]] and [[DE-BND]].

## Relationships

- `governed-by` [[FR-LOI-RENSEIGNEMENT-2015]].
- `governed-by` [[FR-LIL]] — `confidence: low`. Title IV of the loi
  Informatique et Libertés holds the provisions for processing concerning
  state security and defence, and such processing must be authorised by
  decree after a reasoned CNIL opinion. The sources describe the regime and
  name an intelligence file — CRISTINA, held by the DGSI's predecessor —
  rather than naming the DGSI as a controller, so this edge is weaker than
  the UK's Part 4 edge or Belgium's, and is the only one of the four
  cross-cluster bridges in this batch carried at low confidence. It is
  asserted on this entity alone; [[FR-DGSE]], [[FR-DRM]] and [[FR-DRSD]]
  carry no equivalent, because nothing read connects them to a named file.

## Sources

Listed in frontmatter.
