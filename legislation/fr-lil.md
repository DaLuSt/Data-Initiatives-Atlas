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
verification: primary-source

start_date: 1978-01-06
end_date: null
last_verified: "2026-08-26"
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
    evidence: "Confirmed by reading cnil.fr's own page directly (2026-08-26): 'La loi n° 2018-493 du 20 juin 2018, promulguée le 21 juin 2018, a modifié la loi Informatique et Libertés afin de mettre en conformité le droit national avec le cadre juridique européen' (Law n° 2018-493 of 20 June 2018, promulgated 21 June 2018, modified the loi Informatique et Libertés to bring national law into conformity with the European legal framework), and confirms this enabled 'la mise en œuvre concrète du Règlement général sur la protection des données (RGPD)' (the concrete implementation of the GDPR). Ordinance n° 2018-1125 of 12 December 2018's exact title and date are confirmed directly by reading moirouxavocats.com. `legifrance.gouv.fr` — which would carry the acts' own text — is genuinely bot-walled (403) even with an honest User-Agent, so neither text was read at first hand."
    confidence: medium
    valid_from: 2018-06-20
    valid_until: null

sources:
  - title: "Entrée en vigueur de la nouvelle loi Informatique et Libertés"
    url: "https://www.cnil.fr/fr/entree-en-vigueur-de-la-nouvelle-loi-informatique-et-libertes"
    publisher: "Commission nationale de l'informatique et des libertés (CNIL)"
    accessed: "2026-08-26"
  - title: "Les modifications apportées par l'ordonnance n° 2018-1125 du 12 décembre 2018 à la loi n° 78-17 du 6 janvier 1978"
    url: "https://moirouxavocats.com/actualites/les-modifications-apportees-par-lordonnance-n-2018-1125-du-12-decembre-2018-a-la-loi-n-78-17-du-6-janvier-1978-relative-a-linformatique-aux-fichiers-et-aux-libertes/"
    publisher: "Moiroux Avocats"
    accessed: "2026-08-26"
  - title: "Loi informatique et libertés"
    url: "https://fr.wikipedia.org/wiki/Loi_informatique_et_libert%C3%A9s"
    publisher: "Wikipédia"
    accessed: "2026-08-26"
  - title: "RGPD : une ordonnance réécrit la loi informatique et libertés"
    url: "https://www.entreprises.cci-paris-idf.fr/fiches-pratiques/la-loi-informatique-et-libertes-et-le-rgpd"
    publisher: "CCI Paris Île-de-France"
    accessed: "2026-08-26"
  - title: "DOSSIER — Réforme de la Loi informatique et Libertés"
    url: "https://www.gers.cci.fr/actualites/dossier-reforme-de-la-loi-informatique-et-libertes.html"
    publisher: "CCI Gers"
    accessed: "2026-08-26"
---

# Loi Informatique et Libertés (loi n° 78-17)

> **Verified 2026-08-26.** All five cited pages were read directly.
> CNIL's own page confirms the 2018 reform's date and purpose verbatim.
> `legifrance.gouv.fr`, which would carry the acts' own text, is
> genuinely bot-walled (403) even with an honest, identifying
> User-Agent — confirmed on several JORF pages across this cluster.

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

## Five countries, four techniques — and France's is the outlier

[[EU-GDPR]] is one Atlas entity with five national implementations, and the
*legislative technique* differs across them:

| Country | Instrument | Technique |
|---|---|---|
| **France** | **loi 78-17 (1978)** | **amended in place — the pre-existing act was deliberately kept** |
| Netherlands | [[NL-UAVG]] | new implementing act |
| Germany | [[DE-BDSG]] | new act, replacing the earlier BDSG |
| Belgium | [[BE-GDPR-WET]] | new act, repealing the 1992 privacy act |
| Spain | [[ES-LOPDGDD]] | new organic law, carrying digital rights beyond data protection |

The French choice was **explicit and symbolic**, not incidental: the
sources record that the decision was made to *preserve* the 1978 act and
proceed by modification. Three countries drew a line under their old law;
France kept it and rewrote it underneath.

That produces a fact the Atlas can state and would otherwise have no way to
notice: **the entity implementing the GDPR in France is 40 years older than
the regulation it implements**, and older than every other instrument in
this Atlas except [[BE-KSZ-WET]] (1990) — which it also predates by twelve
years, making it the oldest entity here.

**No relationship between the national acts is asserted.** They are
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

Listed in frontmatter, all five read directly this pass. **Still no
Légifrance citation for loi 78-17 itself** — `legifrance.gouv.fr` is
genuinely bot-walled (403) even with an honest User-Agent, so the
1978 date continues to rest on CNIL and secondary commentary rather
than the act's own text. Three of the five sources are
chamber-of-commerce or law-firm commentary.
