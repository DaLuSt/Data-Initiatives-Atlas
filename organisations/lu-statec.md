---
id: LU-STATEC
type: organisation
name: Institut national de la statistique et des études économiques (Luxembourg)
alternative_names:
  - STATEC
  - Statistics Luxembourg
description: >
  Luxembourg's national statistical institute, and its national statistical
  institute within the European Statistical System.

level: national
country: LU
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-25"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-ESS
relationships:
  - type: part-of
    target: EU-ESS
    source: fact
    evidence: "Confirmed by reading statistiques.public.lu directly (2026-08-25): STATEC is Luxembourg's national statistical institute, publishing 'la base de données LUSTAT' and operating the Grand Duchy's statistics portal, of which it is the editor ('le portail ... est édité par le STATEC', confirmed on the site's own 'A propos du site' page). The European Statistical System is the partnership between the Community statistical authority (the Commission/Eurostat) and the national statistical institutes and other national authorities responsible in each member state for developing, producing and disseminating European statistics (ec.europa.eu/eurostat/web/european-statistical-system; EUR-Lex CELEX 32009R0223). No page read this pass has STATEC describe the ESS directly in its own words, so this edge still rests on the composition rule rather than a source naming the membership itself — the same basis on which most national statistical offices in the Atlas are attached."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "STATEC — Institut national de la statistique et des études économiques"
    url: "https://statistiques.public.lu/"
    publisher: "STATEC"
    accessed: "2026-08-25"
  - title: "A propos du site — STATEC"
    url: "https://statistiques.public.lu/fr/support/a-propos.html"
    publisher: "STATEC"
    accessed: "2026-08-25"
  - title: "European Statistical System (ESS)"
    url: "https://ec.europa.eu/eurostat/web/european-statistical-system"
    publisher: "Eurostat / European Commission"
    accessed: "2026-08-25"
---

# Institut national de la statistique et des études économiques (Luxembourg)

> **Verified 2026-08-25.** Both pages were read directly and confirm
> STATEC's identity and its role as editor of Luxembourg's statistics
> portal. Unlike [[PL-GUS]] or [[EE-STATISTIKAAMET]], no page read this
> pass has STATEC describe [[EU-ESS]] membership in its own words, so
> that edge still rests on the composition rule.

## Description

Confirmed by reading statistiques.public.lu directly (2026-08-25):
STATEC is Luxembourg's national statistical institute, publishing the
LUSTAT database and operating the Grand Duchy's statistics portal. Its
own "A propos du site" page confirms: "Ce portail est le Portail des
statistiques du Grand-Duché de Luxembourg. Le portail est la propriété
de l'Etat luxembourgeois et est édité par le STATEC" (this portal is the
property of the Luxembourg State and is published by STATEC).

## ⚠ A third name collision, and this one is exact

STATEC's full name is *Institut national de la statistique et des études
économiques* — **word for word the same** as France's [[FR-INSEE]].

Two member states, one French-language institutional formula, two different
bodies. The acronyms differ (STATEC, INSEE) and the full names do not.
This is the third collision in a single batch, after the two CNPDs and the
two INEs, and together they are a decent argument for why the Atlas keys on
scoped IDs rather than on names.

## The tenth member of [[EU-ESS]]

Ten national statistical institutes plus [[EU-EUROSTAT]].

## Sources

Listed in frontmatter, both read directly this pass.
