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
last_verified: "2026-09-18"
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
    source: fact
    evidence: "CLOSES discovery/unresolved.md row #81's remaining low-confidence question (does FR-LIL Title IV name the DGSI as a controller?). fr.wikipedia.org's CRISTINA-file article ('Cristina (fichier)'), read directly (2026-09-18), confirms CRISTINA's legal basis is Article 26(III) of the loi n° 78-17 du 6 janvier 1978 — the loi Informatique et Libertés's own national-security-file provision (Title IV) — authorised by a décret en Conseil d'État of 27 June 2008, on which the CNIL gave a favourable opinion with reservations (avis n° 2008-175 du 16 juin 2008) after being seized 27 March 2008. Independently, Légifrance's own official index page for the amending decree gives its full title verbatim: 'Décret du 2 août 2017 modifiant le décret du 27 juin 2008 portant création au profit de la direction générale de la sécurité intérieure d'un traitement automatisé de données à caractère personnel dénommé « CRISTINA »' — Légifrance's own metadata, not secondary commentary, names DGSI directly ('au profit de la direction générale de la sécurité intérieure') as the beneficiary/controller of the Title-IV-authorised processing. The decree's substantive text itself remains unpublished ('n'est pas publié'), confirmed by attempting to read it directly at Légifrance this pass — consistent with Wikipedia's note that CRISTINA's creation decree is withheld from the Journal officiel under defence-secrecy rules. `confidence: medium` rather than `high`: DGSI is named in a government source's own title, not in the readable substantive text of the instrument itself."
    confidence: medium
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
  - title: "Cristina (fichier)"
    url: "https://fr.wikipedia.org/wiki/Cristina_(fichier)"
    publisher: "Wikipédia"
    accessed: "2026-09-18"
  - title: "Décret du 2 août 2017 modifiant le décret du 27 juin 2008 portant création au profit de la direction générale de la sécurité intérieure d'un traitement automatisé de données à caractère personnel dénommé « CRISTINA »"
    url: "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000035355228"
    publisher: "Légifrance (République française)"
    accessed: "2026-09-18"
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
>
> **Closed 2026-09-18** (`discovery/unresolved.md` row #81, remaining
> question): DGSI is now named directly in a government source's own
> title for the CRISTINA file's authorising decree. See "CRISTINA, named
> at last" below.

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

## CRISTINA, named at last — 2026-09-18

For several passes, the `governed-by` [[FR-LIL]] edge was carried at low
confidence because DGSI was "nowhere named as a controller in its own
words" — only fr.wikipedia.org's DGSI article, at one remove, described
CRISTINA as exempted from CNIL oversight under the loi Informatique et
Libertés's national-security-file provisions.

Reading the Wikipedia article dedicated to the file itself, *Cristina
(fichier)*, directly this pass adds the legal chain: CRISTINA's basis is
**Article 26(III)** of loi n° 78-17 — the Act's own Title IV provision for
files touching state security, defence or public safety — authorised by a
**décret en Conseil d'État of 27 June 2008**, on which the CNIL gave a
favourable opinion with reservations (**avis n° 2008-175 du 16 juin
2008**) after being seized on 27 March 2008.

The stronger piece is independent of Wikipedia: **Légifrance's own index
page** for the decree that later amended CRISTINA's authorisation gives
the decree's full official title verbatim: *"Décret du 2 août 2017
modifiant le décret du 27 juin 2008 portant création **au profit de la
direction générale de la sécurité intérieure** d'un traitement automatisé
de données à caractère personnel dénommé « CRISTINA »."* That is a
government source's own naming of DGSI as the beneficiary of a Title-IV
processing authorisation — not secondary commentary describing DGSI, but
the state's own record of which service the decree was written for.

`confidence: medium`, not `high`: attempting to read the decree's
substantive text directly at Légifrance this pass confirms it remains
genuinely unpublished ("n'est pas publié"), consistent with Wikipedia's
note that CRISTINA's creation decree is withheld from the Journal officiel
under defence-secrecy rules. DGSI is named in the government's own title
for the instrument, not in readable operative text naming it a
"responsable du traitement" in so many words.

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
- `governed-by` [[FR-LIL]] — closed 2026-09-18, `confidence: medium`,
  `source: fact`. Légifrance's own decree title names DGSI as the
  beneficiary of CRISTINA's Title-IV (Article 26(III)) authorisation. See
  "CRISTINA, named at last" above.

## Sources

Listed in frontmatter. Six of nine read directly: `cnctr.fr` and
`fr.wikipedia.org`'s DGSI article (prior pass), Légifrance's text of
DGSI's founding decree and the Sénat's 2022–2023 intelligence-oversight
report (2026-08-28 pass), and `fr.wikipedia.org`'s CRISTINA-file article
plus Légifrance's index page for the 2017 amending decree (this pass,
2026-09-18 — the decree's own substantive text remains genuinely
unpublished, confirmed by a direct attempt). DGSI's own pages and
`interieur.gouv.fr`'s page remain genuinely bot-walled (403) even with an
honest User-Agent, re-confirmed by a fourth direct fetch attempt, even
though a search engine can evidently reach and index the same pages. Per
this pass's instruction, no further effort was spent on those exact
domains; Légifrance and the Sénat — both outside the `interieur.gouv.fr`
family — supplied the majority instead.
