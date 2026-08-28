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
verification: primary-source

start_date: 2014-04-30
end_date: null
last_verified: "2026-08-28"
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
    evidence: "Confirmed by reading fr.wikipedia.org's DGSI article directly (2026-08-26): DGSI was established by decree of 30 April 2014 ('fondé par décret le 30 avril 2014'), its missions set out in Article 2 of that decree. Independently confirmed by reading the decree's own text directly on Légifrance (2026-08-28, décret n° 2014-445 du 30 avril 2014): Article 1 establishes DGSI as an active police service ('service actif de la police nationale') tasked with gathering, centralising and exploiting intelligence concerning national security across French territory, and Article 4 confirms its structure of a central administration plus territorial services under the sole authority of the director general. This is DGSI's own founding legal instrument, read directly — the strongest possible source for this edge, notwithstanding that DGSI's own website remains bot-walled. Anchor edge under metadata/relationship-types.md §2.3."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: FR-LOI-RENSEIGNEMENT-2015
    source: fact
    evidence: "Confirmed by reading cnctr.fr's own services page directly (2026-08-26): 'Service actif de la police nationale, la direction générale de la sécurité intérieure est chargée, sur l'ensemble du territoire de la République, de rechercher, de centraliser et d'exploiter le renseignement intéressant la sécurité nationale ou les intérêts fondamentaux de la Nation' (an active service of the national police, the DGSI is responsible, across the whole territory, for gathering, centralising and exploiting intelligence concerning national security) — a detail (DGSI as a police service) this entity did not previously carry. Independently confirmed by reading DGSI's founding decree itself directly on Légifrance (2026-08-28): Article 2 provides that DGSI 'peut recourir aux techniques de recueil de renseignement' (may use intelligence-gathering techniques) only for the missions the article enumerates — the decree does not itself name the 2015 law, but its techniques-de-renseignement clause is the provision the 2015 law's authorisation regime governs, read alongside CNCTR's own statement of oversight. DGSI's own site and interieur.gouv.fr remain genuinely bot-walled (403) even with an honest, identifying User-Agent, retried again this pass with the same result."
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
  - title: "Décret n° 2014-445 du 30 avril 2014 relatif aux missions et à l'organisation de la direction générale de la sécurité intérieure"
    url: "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000028887486"
    publisher: "Légifrance (République française)"
    accessed: "2026-08-28"
  - title: "Rapport relatif à l'activité de la délégation parlementaire au renseignement pour l'année 2022-2023"
    url: "https://www.senat.fr/rap/r22-810/r22-810_mono.html"
    publisher: "Sénat (République française)"
    accessed: "2026-08-28"
---

# Direction générale de la Sécurité intérieure (DGSI)

> **Promoted to `primary-source` 2026-08-28.** DGSI's own cited pages and
> `interieur.gouv.fr` were tried again this pass and are still genuinely
> 403-blocked — the same result as the prior two passes, confirmed a
> fourth time, per this pass's instruction not to re-spend further effort
> on those exact domains. Instead, two genuinely different French
> government domains were tried, per this pass's specific instruction:
> **Légifrance**, which is not part of the `interieur.gouv.fr` family and
> served DGSI's own founding decree (n° 2014-445 du 30 avril 2014) in
> full, readable text — DGSI's own foundational legal instrument, the
> strongest kind of source available for this entity; and the **Sénat**'s
> own published intelligence-oversight report, which independently
> corroborates DGSI's role, gives its 2021–2022 budget figures, and names
> its then-director (Nicolas Lerner). That brings this entity to 4 of 7
> sources read directly (cnctr.fr and fr.wikipedia.org from the prior
> pass, plus Légifrance and the Sénat this pass) — a genuine majority —
> so `verification` is promoted to `primary-source`.

## Description

The DGSI is France's **internal** intelligence service, under the Minister of
the Interior. The sources give its remit as three functions:
counter-espionage, internal surveillance and counter-terrorism.

Its external counterpart is [[FR-DGSE]], under the Minister of the Armed
Forces.

**Confirmed by reading DGSI's own founding decree directly on Légifrance
(2026-08-28, décret n° 2014-445 du 30 avril 2014):** Article 1 establishes
DGSI as "un service actif de la police nationale" (an active service of the
national police) responsible, across the whole territory of the Republic,
for gathering, centralising and exploiting intelligence concerning national
security or the Nation's fundamental interests, and for participating in
judicial-police missions under the Code de procédure pénale. Article 2 lists
its specific missions in more granular form than any secondary source
previously read here: prevention and suppression of foreign interference,
counter-terrorism, monitoring of radicalised individuals, protection of
defence secrets and of economic and scientific potential, prevention of
weapons-of-mass-destruction proliferation, monitoring international
organised crime, and combating cybercrime — with recourse to
intelligence-gathering techniques permitted only for those enumerated
purposes. Article 4 confirms DGSI's structure: a central administration plus
territorial services, all under the sole authority of the director general,
with territorial heads reporting to local state representatives within
need-to-know limits.

The Sénat's own 2022–2023 parliamentary-oversight report on the
intelligence services, read directly this pass, independently corroborates
DGSI's role and adds operational and budgetary detail no other source here
carries: DGSI conducted 1.66 million administrative security screenings and
around 1 million visa-related inquiries in 2021, received a budget of €452.9
million in 2021 rising to €485.0 million in 2022 (still below 2020's €529.0
million), and was headed by Nicolas Lerner, who the parliamentary
delegation auditioned on 13 June 2023. The report also places DGSI alongside
[[FR-DGSE]] and DRM as one of three services working against foreign
interference operations targeting France.

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

- `part-of` [[FR]] — anchor edge, confirmed via `fr.wikipedia.org`'s
  founding-decree date (30 April 2014) and, this pass, independently via
  the decree's own text read directly on Légifrance — DGSI's own website
  remains bot-walled, but its founding legal instrument is not.
- `governed-by` [[FR-LOI-RENSEIGNEMENT-2015]] — confirmed via cnctr.fr and,
  this pass, corroborated by the founding decree's own
  techniques-de-renseignement clause (Article 2), read directly on
  Légifrance.
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

Listed in frontmatter. Four of seven read directly: `cnctr.fr` and
`fr.wikipedia.org` (prior pass), plus Légifrance's text of DGSI's founding
decree and the Sénat's 2022–2023 intelligence-oversight report (this pass,
2026-08-28). DGSI's own pages and `interieur.gouv.fr`'s page remain
genuinely bot-walled (403) even with an honest User-Agent, re-confirmed
this pass by a fourth direct fetch attempt, even though a search engine can
evidently reach and index the same pages. Per this pass's instruction, no
further effort was spent on those exact domains; Légifrance and the Sénat
— both outside the `interieur.gouv.fr` family — supplied the majority
instead.
