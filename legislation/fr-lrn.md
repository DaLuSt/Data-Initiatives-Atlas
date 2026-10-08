---
id: FR-LRN
type: act
name: Loi pour une République numérique
name_en: "Digital Republic Act"
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
rank: ordinary
confidence: medium
coverage: low
verification: primary-source

start_date: 2016-10-07
end_date: null
last_verified: "2026-10-08"
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
  - EU-PSI-DIRECTIVE
relationships:
  - type: applies-in
    target: FR
    source: fact
    evidence: "Confirmed by reading guides.data.gouv.fr's own open-data chronology directly (2026-08-26): '2016 - Loi pour une République numérique : consécration du principe de l'open data par défaut' (the loi pour une République numérique enshrines the principle of open data by default). decideo.fr's commentary, also read directly, confirms the 3,500-inhabitant threshold and gives a precise codification: the diffusion obligations sit at 'articles L312-1-1 et suivants du CRPA' (Code des relations entre le public et l'administration) — a citation this entity did not previously carry. `legifrance.gouv.fr` and the dead `guides.etalab.gouv.fr` were not read. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: implements-requirement-from
    target: EU-OPEN-DATA-DIRECTIVE
    source: fact
    evidence: "Confirmed by reading EUR-Lex's register of national implementing measures for Directive (EU) 2019/1024 directly (2026-10-08): France is listed with 52 notified measures, among them 'Article 16 de la LOI n° 2016-1321 du 7 octobre 2016 pour une République numérique' (published in the Journal officiel on 2016-10-08, NIM:202101334), alongside articles of the Code des relations entre le public et l'administration, the Code de la recherche and the Code de l'éducation. All of the notified measures read were adopted before the directive; the register lists no standalone act of 2019 or later. This edge therefore records that France itself notified part of this earlier act as implementing the directive, not that the act was made to transpose it; the act's other provisions are not covered. confidence medium because only the register's titles were read, not Article 16's text."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: references
    target: EU-PSI-DIRECTIVE
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP (this entity's own prose: 'the 2003 PSI Directive (2003/98/EC) — which is not an Atlas entity'). It now is, [[EU-PSI-DIRECTIVE]]. The Etalab/data.gouv.fr open-data chronology already cited on this entity places France's open-data legal history in a lineage running from the 2003 PSI Directive; `references` rather than `implements-requirement-from` because the chronology describes lineage, not a stated transposition by this specific 2016 act."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Directive (EU) 2019/1024 — national implementing measures (France)"
    url: "https://eur-lex.europa.eu/legal-content/FR/NIM/?uri=CELEX:32019L1024"
    publisher: "EUR-Lex (Publications Office of the European Union)"
    accessed: "2026-10-08"
  - title: "Chronologie juridique de l'open data"
    url: "https://guides.data.gouv.fr/guides/guide-juridique/chronologie-de-lopen-data"
    publisher: "data.gouv.fr"
    accessed: "2026-08-26"
  - title: "Open Data : ce qu'il faut retenir de la Loi Lemaire"
    url: "https://www.decideo.fr/Open-Data-ce-qu-il-faut-retenir-de-la-Loi-Lemaire_a9297.html"
    publisher: "Decideo"
    accessed: "2026-08-26"
  - title: "Le cadre juridique de l'open data en France"
    url: "https://datactivist.coop/ardeche/rapport/partie2.html"
    publisher: "Datactivist"
    accessed: "2026-08-26"
  - title: "LOI n° 2016-1321 du 7 octobre 2016 pour une République numérique"
    url: "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000033202746"
    publisher: "Légifrance (Direction de l'information légale et administrative)"
  - title: "Chronologie de l'open data"
    url: "https://guides.etalab.gouv.fr/juridique/chronologie/"
    publisher: "Etalab — guides.etalab.gouv.fr"
---

# Loi pour une République numérique (2016)

> **Verified 2026-08-26.** `guides.data.gouv.fr` and `decideo.fr` were
> read directly and confirm the open-data-by-default principle and the
> 3,500-inhabitant threshold, plus a precise codification (articles
> L312-1-1 et seq. of the CRPA) this entity did not previously carry.
> `legifrance.gouv.fr` is genuinely bot-walled; `guides.etalab.gouv.fr`
> no longer resolves.

## Description

The **loi n° 2016-1321 of 7 October 2016**, known as the *loi Lemaire*,
established the principle of **open data by default** in French public
administration and made open data an **obligation for local authorities
with more than 3,500 inhabitants**, codified at **articles L312-1-1 et
seq.** of the Code des relations entre le public et l'administration —
confirmed by reading decideo.fr's commentary directly (2026-08-26).

`coverage: low`: this act is wide-ranging — it also covers platform loyalty,
net neutrality and digital rights — and only its open-data provisions are
recorded here, because only those were sourced.

## France's Open Data Directive transposition: existing law, notified

- This act is from **2016**; [[EU-OPEN-DATA-DIRECTIVE]] is Directive (EU)
  **2019**/1024. A 2016 act was not made to transpose a 2019 directive.
- France passed **no standalone Open Data Directive instrument**. (An earlier
  belief that a 2021 ordinance existed was wrong: the ordinance that fits the
  description transposes Directive 2019/790 on copyright; see
  [[FR-LOI-VALTER]].) Its re-use regime was already in place and sits in the
  Code des relations entre le public et l'administration.
- EUR-Lex's register of national implementing measures for the directive,
  read directly on 2026-10-08, lists **France with 52 notified measures**: 
  articles of that code, of the Code de la recherche and the Code de
  l'éducation, an article of the loi n° 2020-1674, and **Article 16 of this
  act**. So France itself presented part of this act as implementing the
  directive. The Atlas records that as `implements-requirement-from`,
  `confidence: medium`, and says in the edge what it does and does not mean.
- The same register shows no French act of 2019 or later, which agrees with the
  finding in [[EU-OPEN-DATA-DIRECTIVE]] that France did nothing new.

The earlier lineage edge to [[EU-PSI-DIRECTIVE]] stays: the Etalab and
data.gouv.fr chronologies place this act in a line that runs from the 2003 PSI
Directive, and they describe a lineage, not a stated transposition.

## Relationships

- `applies-in` [[FR]] — anchor edge.
- `implements-requirement-from` [[EU-OPEN-DATA-DIRECTIVE]] — France's own
  notification of Article 16 to the Commission; see above.
- `references` [[EU-PSI-DIRECTIVE]] — lineage, not transposition.

**No `implements-requirement-from` is asserted** to
[[EU-OPEN-DATA-DIRECTIVE]] — `related_entities` records that association
for navigation only, since this 2016 act predates the 2019 directive.
Nor is any edge asserted to [[FR-DATA-GOUV]] — refined 2026-09-18,
closing `discovery/unresolved.md` row #76: data.gouv.fr's own legal
guide, read directly, traces the *platform's* designation to a
different article of the same code (CRPA Article R. 321-8, plus 2011
and 2021 circulars), not to this Act. The two sit in the same code at
different articles, neither naming the other — see [[FR-DATA-GOUV]] for
the full finding.

## Sources

Listed in frontmatter. `guides.data.gouv.fr`, `decideo.fr` and
`datactivist.coop` were read directly this pass; `legifrance.gouv.fr`
is genuinely bot-walled (403) even with an honest User-Agent, and
`guides.etalab.gouv.fr` no longer resolves at all — a dead domain,
apparently superseded by `guides.data.gouv.fr`.
