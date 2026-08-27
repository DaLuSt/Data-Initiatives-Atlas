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

start_date: 2014-04-30
end_date: null
last_verified: "2026-08-27"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - FR
  - FR-LOI-RENSEIGNEMENT-2015
  - FR-LIL
  - FR-DGSE
  - FR-DRM
  - FR-DRSD
  - FR-CNCTR
relationships:
  - type: governed-by
    target: FR-LIL
    source: interpretation
    evidence: "Confirmed by reading fr.wikipedia.org's DGSI article directly (2026-08-26): CRISTINA, the file inherited from DGSI's predecessor, is explicitly carved out rather than routinely authorised — 'Au nom de dispositions de la loi informatique et libertés concernant les fichiers de Sécurité nationale, il n'est pas soumis au contrôle de la Commission nationale de l'informatique et des libertés (CNIL)' (under national-security-file provisions of the loi Informatique et Libertés, it is not subject to CNIL oversight), though the same article notes CNIL retains a general supervisory role over personal data DGSI may otherwise collect. This is a narrower and more precise claim than this entity previously carried (that Title IV processing 'must be authorised by decree after a reasoned CNIL opinion') — the specific file most often cited, CRISTINA, is instead exempted from CNIL control outright. DGSI's own three cited pages remain bot-walled (see below), so this edge still rests on secondary corroboration rather than DGSI naming itself as subject to the Act."
    confidence: low
    valid_from: null
    valid_until: null
  - type: part-of
    target: FR
    source: fact
    evidence: "Confirmed by reading fr.wikipedia.org's DGSI article directly (2026-08-26): DGSI was established by decree of 30 April 2014 ('fondé par décret le 30 avril 2014'), its missions set out in Article 2 of that decree. DGSI's own three cited pages remain bot-walled; this date was not previously carried by the entity. Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: FR-LOI-RENSEIGNEMENT-2015
    source: fact
    evidence: "Confirmed by reading cnctr.fr's own services page directly (2026-08-26): 'Service actif de la police nationale, la direction générale de la sécurité intérieure est chargée, sur l'ensemble du territoire de la République, de rechercher, de centraliser et d'exploiter le renseignement intéressant la sécurité nationale ou les intérêts fondamentaux de la Nation' (an active service of the national police, the DGSI is responsible, across the whole territory, for gathering, centralising and exploiting intelligence concerning national security) — a detail (DGSI as a police service) this entity did not previously carry. All three of DGSI's own and interieur.gouv.fr's pages were tried this pass and are genuinely bot-walled (403) even with an honest, identifying User-Agent, so this edge rests on CNCTR's corroboration rather than DGSI's own site."
    confidence: medium
    valid_from: 2015-07-24
    valid_until: null

sources:
  - title: "Les principaux services de renseignement"
    url: "https://www.cnctr.fr/services-de-renseignement"
    publisher: "Commission nationale de contrôle des techniques de renseignement (CNCTR)"
    accessed: "2026-08-26"
  - title: "Les fondements — notre cadre légal"
    url: "https://www.dgsi.interieur.gouv.fr/decouvrir-dgsi/notre-cadre-legal/fondements"
    publisher: "Direction générale de la Sécurité intérieure (DGSI)"
  - title: "La communauté du renseignement"
    url: "https://www.dgsi.interieur.gouv.fr/decouvrir-la-dgsi/nos-partenaires/la-communaute-du-renseignement"
    publisher: "Direction générale de la Sécurité intérieure (DGSI)"
  - title: "La direction générale de la Sécurité intérieure"
    url: "https://www.interieur.gouv.fr/ministere/direction-generale-de-securite-interieure"
    publisher: "Ministère de l'Intérieur"
  - title: "Direction générale de la Sécurité intérieure"
    url: "https://fr.wikipedia.org/wiki/Direction_g%C3%A9n%C3%A9rale_de_la_S%C3%A9curit%C3%A9_int%C3%A9rieure"
    publisher: "Wikipédia"
    accessed: "2026-08-26"
---

# Direction générale de la Sécurité intérieure (DGSI)

> **Re-checked 2026-08-27, still `search-only`.** DGSI's own cited page
> was tried again this pass and is still genuinely 403-blocked — the
> same result as the prior pass, confirmed a third time. A web search
> shows Google's own index has crawled and cached DGSI's "fondements"
> page (content on prior control by the CNCTR and the July 2015
> intelligence law), which means the block is specific to automated
> fetch tools rather than to all outside access — but a search-engine
> snippet is not a direct read, so it is not counted as one and nothing
> here is sourced to it. That is still 2 of 5 sources read directly
> (cnctr.fr, fr.wikipedia.org), short of the majority needed to call
> the entity `primary-source`.

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

- `part-of` [[FR]] — anchor edge, confirmed this pass via
  `fr.wikipedia.org`'s founding-decree date (30 April 2014); DGSI's own
  pages remain bot-walled.
- `governed-by` [[FR-LOI-RENSEIGNEMENT-2015]] — confirmed via cnctr.fr,
  since DGSI's own pages remain bot-walled.
- `governed-by` [[FR-LIL]] — `confidence: low`, `source: interpretation`.
  `fr.wikipedia.org`'s DGSI article, read this pass, narrows the claim
  this entity previously carried: CRISTINA, the file most often cited in
  this context, is specifically **exempted** from CNIL oversight under
  the loi Informatique et Libertés's national-security-file provisions,
  rather than routinely authorised by decree after a CNIL opinion as
  this entity previously implied. CNIL retains a general supervisory
  role over DGSI's other personal-data processing. This edge is weaker
  than the UK's Part 4 edge or Belgium's, and remains the only one of
  the four cross-cluster bridges in this batch carried at low
  confidence, because DGSI is still nowhere named as a controller in its
  own words — DGSI's own three pages remain bot-walled.

## Sources

Listed in frontmatter. `cnctr.fr` and `fr.wikipedia.org` remain the only
two read directly (from the prior pass); DGSI's own pages and
`interieur.gouv.fr`'s page are genuinely bot-walled (403) even with an
honest User-Agent, re-confirmed this pass by a third direct fetch
attempt, even though a search engine can evidently reach and index the
same pages.
