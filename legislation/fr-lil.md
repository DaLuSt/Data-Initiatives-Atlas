---
id: FR-LIL
type: law
name: Loi relative à l'informatique, aux fichiers et aux libertés
alternative_names:
  - Loi Informatique et Libertés
  - Loi n° 78-17 du 6 janvier 1978
  - French Data Protection Act
description: >
  French data protection act of 6 January 1978, brought into conformity
  with the GDPR by the law of 20 June 2018 and the ordinance of 12 December
  2018 rather than being replaced. The 2018 reform took positions on the
  discretionary options the GDPR leaves to member states, implemented the
  law-enforcement directive for criminal-sphere files, and moved the CNIL
  from prior to posterior control.

level: national
country: FR
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 1978-01-06
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - FR-CNIL
related_entities:
  - EU-GDPR
  - NL-UAVG
  - DE-BDSG
  - BE-GDPR-WET
relationships:
  - type: implements-requirement-from
    target: EU-GDPR
    source: fact
    evidence: "Law n° 2018-493 of 20 June 2018 modified the loi Informatique et Libertés to bring French law into conformity with the European framework, taking positions on the roughly fifty discretionary options the GDPR leaves to member states; ordinance n° 2018-1125 of 12 December 2018 completed the conformity of law n° 78-17 of 6 January 1978 with the GDPR (cnil.fr; entreprises.cci-paris-idf.fr; moirouxavocats.com). NOT READ — search-only."
    confidence: medium
    valid_from: 2018-06-20
    valid_until: null

sources:
  - title: "Entrée en vigueur de la nouvelle loi Informatique et Libertés"
    url: "https://www.cnil.fr/fr/entree-en-vigueur-de-la-nouvelle-loi-informatique-et-libertes"
    publisher: "Commission nationale de l'informatique et des libertés (CNIL)"
  - title: "Loi informatique et libertés"
    url: "https://fr.wikipedia.org/wiki/Loi_informatique_et_libert%C3%A9s"
    publisher: "Wikipédia"
  - title: "RGPD : une ordonnance réécrit la loi informatique et libertés"
    url: "https://www.entreprises.cci-paris-idf.fr/fiches-pratiques/la-loi-informatique-et-libertes-et-le-rgpd"
    publisher: "CCI Paris Île-de-France"
  - title: "Les modifications apportées par l'ordonnance n° 2018-1125 du 12 décembre 2018 à la loi n° 78-17 du 6 janvier 1978"
    url: "https://moirouxavocats.com/actualites/les-modifications-apportees-par-lordonnance-n-2018-1125-du-12-decembre-2018-a-la-loi-n-78-17-du-6-janvier-1978-relative-a-linformatique-aux-fichiers-et-aux-libertes/"
    publisher: "Moiroux Avocats"
  - title: "DOSSIER — Réforme de la Loi informatique et Libertés"
    url: "https://www.gers.cci.fr/actualites/dossier-reforme-de-la-loi-informatique-et-libertes.html"
    publisher: "CCI Gers"
---

# Loi Informatique et Libertés (loi n° 78-17)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The **loi n° 78-17 of 6 January 1978** is France's data protection act. It
predates the GDPR by 38 years and predates the EU itself in its current
form.

It was brought into conformity with [[EU-GDPR]] by:

- **Law n° 2018-493 of 20 June 2018**, which took positions on the roughly
  **fifty discretionary options** the GDPR leaves to member states, and
  implemented the law-enforcement directive for criminal-sphere files;
- **Ordinance n° 2018-1125 of 12 December 2018**, which completed the
  conformity work and rewrote the act.

The reform moved [[FR-CNIL]] **from prior control to posterior control**,
based on the accountability of organisations.

## Four countries, four techniques — and France's is the outlier

[[EU-GDPR]] is one Atlas entity with four national implementations, and the
*legislative technique* differs in each:

| Country | Instrument | Technique |
|---|---|---|
| **France** | **loi 78-17 (1978)** | **amended in place — the pre-existing act was deliberately kept** |
| Netherlands | [[NL-UAVG]] | new implementing act |
| Germany | [[DE-BDSG]] | new act, replacing the earlier BDSG |
| Belgium | [[BE-GDPR-WET]] | new act, repealing the 1992 privacy act |

The French choice was **explicit and symbolic**, not incidental: the
sources record that the decision was made to *preserve* the 1978 act and
proceed by modification. Three countries drew a line under their old law;
France kept it and rewrote it underneath.

That produces a fact the Atlas can state and would otherwise have no way to
notice: **the entity implementing the GDPR in France is 40 years older than
the regulation it implements**, and older than every other instrument in
this Atlas except [[BE-KSZ-WET]] (1990) — which it also predates by twelve
years, making it the oldest entity here.

**No relationship between the four national acts is asserted.** They are
siblings under [[EU-GDPR]].

## The amendment question, answered from the other side

[[DE-NIS2UMSUCG]] → [[DE-BSIG]] is the Atlas's standing modelling problem:
an amending act recorded as `supersedes` at `confidence: low`, with the two
entities deliberately disagreeing, because there is no amendment-lineage
relationship type.

France is the same situation handled **without any strain**, and the
contrast shows why:

- In Germany, the amending instrument ([[DE-NIS2UMSUCG]]) has its **own
  name and identity**, so it wants to be an entity — and then needs a
  relationship to the thing it amended.
- In France, the amending instruments (**loi 2018-493**, **ordonnance
  2018-1125**) are recorded **as facts in this entity's body**, and only the
  amended act is an entity.

Both are defensible. The German one was forced by the act being widely known
under its own name; the French one is cleaner. **No `FR-LOI-2018-493`
entity was created**, for the same reason no `DE-OZGAENDG` was: modelling
amending instruments separately multiplies entities and immediately demands
a relationship type the Atlas does not have.

This is the clearest evidence yet that the missing type is worth adding —
two countries, two workarounds, both documented.

## Sources

Listed in frontmatter. **No Légifrance citation for loi 78-17 itself** —
none was returned by search, so the act's text is not cited and the 1978
date rests on the CNIL and secondary commentary. Three of the five sources
are chamber-of-commerce or law-firm commentary.
