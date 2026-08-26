---
id: FR-LOI-VALTER
type: law
name: Loi n° 2015-1779 du 28 décembre 2015 relative à la gratuité et aux modalités de la réutilisation des informations du secteur public
alternative_names:
  - Loi Valter
  - Loi n° 2015-1779
  - French Public Sector Information Re-use Act
description: >
  French act of 28 December 2015 on the free-of-charge nature and the
  arrangements for the re-use of public sector information, transposing
  Directive 2013/37/EU. It establishes the principle that re-use of public
  sector information is free of charge, with fees permitted only in defined
  cases. Its provisions were codified at constant law into Title II of Book
  III of the Code des relations entre le public et l'administration by
  Ordonnance n° 2016-307 of 17 March 2016, taken under the authorisation in
  Article 11 of this act. That codified title, not any standalone act, is
  where the French open data re-use regime now lives.

level: national
country: FR
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2015-12-28
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-PSI-DIRECTIVE
  - EU-OPEN-DATA-DIRECTIVE
  - FR
  - FR-LRN
  - FR-DATA-GOUV
relationships:
  - type: implements-requirement-from
    target: EU-PSI-DIRECTIVE
    source: fact
    evidence: "Confirmed by reading senat.fr's own legislative dossier directly (2026-08-26): 'Loi relative à la gratuité et aux modalités de la réutilisation des informations du secteur public — Loi n° 2015-1779 du 28 décembre 2015 parue au JO n°0301 du 29 décembre 2015' (Law on the free-of-charge nature and arrangements for the re-use of public sector information — Law n° 2015-1779 of 28 December 2015, published in the Official Journal no. 0301 of 29 December 2015), confirming the exact title, number and date this entity's name field already carried. Directive 2013/37/EU is the amending directive within EU-PSI-DIRECTIVE, which the Atlas models as Directive 2003/98/EC as amended. `legifrance.gouv.fr`, which would carry the act's own text, is genuinely bot-walled (403) even with an honest User-Agent."
    confidence: medium
    valid_from: 2015-12-28
    valid_until: null
  - type: applies-in
    target: FR
    source: fact
    evidence: "Confirmed by reading senat.fr's own legislative dossier directly (2026-08-26), same passage as above: the act is Loi n° 2015-1779 du 28 décembre 2015, promulgated and published in the JO. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Réutilisation des informations du secteur public — dossier législatif pjl15-034"
    url: "https://www.senat.fr/dossier-legislatif/pjl15-034.html"
    publisher: "Sénat"
    accessed: "2026-08-26"
  - title: "The Commission calls on 19 Member States to comply with EU rules on open data and the reuse of public sector information"
    url: "https://www.pubaffairsbruxelles.eu/eu-institution-news/the-commission-calls-on-19-member-states-to-comply-with-eu-rules-on-open-data-and-the-reuse-of-public-sector-information/"
    publisher: "PubAffairs Bruxelles"
    accessed: "2026-08-26"
  - title: "LOI n° 2015-1779 du 28 décembre 2015 relative à la gratuité et aux modalités de la réutilisation des informations du secteur public"
    url: "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000031701525"
    publisher: "Légifrance (Direction de l'information légale et administrative)"
  - title: "Ordonnance n° 2016-307 du 17 mars 2016 portant codification des dispositions relatives à la réutilisation des informations publiques dans le code des relations entre le public et l'administration"
    url: "https://www.legifrance.gouv.fr/jorf/id/JORFSCTA000032242477"
    publisher: "Légifrance (Direction de l'information légale et administrative)"
  - title: "Titre II : LA RÉUTILISATION DES INFORMATIONS PUBLIQUES (Articles L321-1 à L327-1) — Code des relations entre le public et l'administration"
    url: "https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000031366350/LEGISCTA000031367750/"
    publisher: "Légifrance (Direction de l'information légale et administrative)"
---

# Loi Valter (2015)

> **Verified 2026-08-26.** Both the Sénat's own legislative dossier and
> the Commission compliance article were read directly and confirm the
> act's title, number and date. `legifrance.gouv.fr`'s three JORF/code
> citations remain genuinely bot-walled (403) even with an honest
> User-Agent — none of the act's own text was read this pass.

## Description

The French statute on free-of-charge re-use of public sector information,
transposing Directive 2013/37/EU — the amending directive the Atlas carries
inside [[EU-PSI-DIRECTIVE]].

## The 2021 ordinance does not exist

`discovery/research-queue.md` recorded, from the France batch:

> *"France's Open Data Directive transposition | Understood to be a **2021
> ordinance**; not identified."*

There is no such ordinance. The belief is traceable: France did issue an
**Ordonnance n° 2021-1518 du 24 novembre 2021** "complétant la
transposition" of a 2019 directive — but that directive is **2019/790**, on
copyright in the digital single market, not **2019/1024** on open data. Two
2019 directives, adjacent numbers in a search index, one plausible French
ordinance in between.

This is the same failure mode as the Dutch registers batch, where a search
returned the Archiefwet's BWBR identifier for the Kadasterwet. A wrong
citation in this field does not resolve to nothing; it resolves to a real
instrument about something else.

## Where the French regime actually lives

France transposed by amending a **code**, not by passing an act:

| Instrument | Date | Effect |
|---|---|---|
| This act (loi Valter) | 28 Dec 2015 | Transposes Directive 2013/37/EU; Article 11 authorises codification |
| Ordonnance n° 2016-307 | 17 Mar 2016 | Codifies those provisions at constant law into the CRPA |
| [[FR-LRN]] (loi Lemaire) | 7 Oct 2016 | Open data by default; obligation for authorities over 3,500 inhabitants |
| Décret n° 2021-1559 | 1 Dec 2021 | Amends the licence provisions |

The result is **Title II of Book III of the Code des relations entre le
public et l'administration**, articles L321-1 to L327-1. That title, not an
act with a name, is the French answer to the Open Data Directive.

Ordonnance n° 2016-307 and Décret n° 2021-1559 are recorded here rather than
modelled: a codification instrument that changes no law and a decree
amending licence lists are both thinner than the threshold the Atlas has
used for `type: law` elsewhere.

## The documented negative

Confirmed by reading pubaffairsbruxelles.eu's article directly
(2026-08-26): the Commission's letter of formal notice named "Belgium,
Bulgaria, Czechia, Spain, Estonia, Croatia, Ireland, Italy, Cyprus,
Latvia, Luxembourg, Hungary, the Netherlands, Austria, Romania,
Slovenia, Slovakia, Finland and Sweden" for failing to provide complete
transposition information on Directive (EU) 2019/1024 — nineteen
member states, and **France is not among them**, confirmed by name
search of the article's text.

France's absence from that list is the strongest available evidence that its
notified measures were already in place — which is what "we transposed by
having done it in 2015 and 2016" looks like from the Commission's side.

For this reason **no `implements-requirement-from` edge to
[[EU-OPEN-DATA-DIRECTIVE]] is asserted from France.** The comparison matrix
in the graph viewer will show France with an `applies-in` edge and no
national implementer on that row. That is the finding, not a gap.

## Relationships

- `implements-requirement-from` [[EU-PSI-DIRECTIVE]].
- `applies-in` [[FR]] (anchor edge).

## Sources

Listed in frontmatter. `senat.fr` and `pubaffairsbruxelles.eu` were
read directly this pass; `legifrance.gouv.fr`'s three citations remain
genuinely bot-walled.
