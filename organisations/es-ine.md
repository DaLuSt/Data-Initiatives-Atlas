---
id: ES-INE
type: organisation
name: Instituto Nacional de Estadística
alternative_names:
  - INE
  - Spanish National Statistics Institute
description: >
  Spanish national statistical office. An autonomous administrative body
  with its own legal personality and assets, attached to the Ministry of
  Economy, Commerce and Business, governed principally by Ley 12/1989 on the
  public statistical function and by the statute approved by Real Decreto
  803/2022. It carries out large-scale statistical operations including
  demographic and economic censuses, prepares the National Statistical Plan,
  proposes norms on statistical concepts and classifications, and manages
  statistical relations with international organisations including Eurostat.

level: national
country: ES
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - ES
  - EU-EUROSTAT
  - EU-ESS
relationships:
  - type: part-of
    target: ES
    source: fact
    evidence: "Confirmed by reading ine.es's own page directly (2026-08-26): 'El Instituto Nacional de Estadística es un organismo autónomo de carácter administrativo, con personalidad jurídica y patrimonio propio', attached to the Ministry of Economy, Commerce and Business through the Secretaría de Estado de Economía y Apoyo a la Empresa. Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: part-of
    target: EU-ESS
    source: fact
    evidence: "Upgraded from the composition-rule tier to a direct statement: confirmed by reading ine.es's own 'Qué es el SEE y cómo funciona' page directly (2026-08-26): 'Sistema Estadístico Europeo (SEE) está formado por: Eurostat (la oficina de estadística de la UE), las oficinas de estadística de todos los estados miembros (los diferentes INE) y otros organismos que elaboran estadísticas europeas' (the ESS is formed by Eurostat, the statistical offices of all member states — the various NSIs — and other bodies producing European statistics), naming INE among 'los diferentes INE' directly. This is INE's own page naming its ESS membership, the same strong-evidence tier set for [[PL-GUS]] and [[FI-TILASTOKESKUS]]."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "BOE-A-1989-10767 Ley 12/1989, de 9 de mayo, de la Función Estadística Pública"
    url: "https://www.boe.es/buscar/doc.php?id=BOE-A-1989-10767"
    publisher: "Boletín Oficial del Estado (BOE)"
    accessed: "2026-08-26"
  - title: "El Instituto Nacional de Estadística"
    url: "https://www.ine.es/dyngs/INE/index.htm?cid=498"
    publisher: "Instituto Nacional de Estadística (INE)"
    accessed: "2026-08-26"
  - title: "Qué es el SEE y cómo funciona"
    url: "https://www.ine.es/ss/Satellite?L=es_ES&c=Page&cid=1254735905268&p=1254735905268&pagename=INE/INELayout"
    publisher: "Instituto Nacional de Estadística (INE)"
    accessed: "2026-08-26"
  - title: "Estadísticas europeas: cómo funciona el Sistema Estadístico Europeo"
    url: "https://eur-lex.europa.eu/ES/legal-content/summary/european-statistics-how-the-european-statistical-system-works.html"
    publisher: "EUR-Lex — Publications Office of the European Union"
---

# INE — Instituto Nacional de Estadística

> **Verified 2026-08-26.** Three of four cited pages were read directly.
> INE's own SEE page names its ESS membership directly, upgrading the
> edge this entity previously carried as an Atlas interpretation to a
> sourced fact — see below.

## Description

The INE is Spain's national statistical office: an **autonomous
administrative body** with its own legal personality and assets, attached to
the Ministry of Economy, Commerce and Business.

It is governed by **Ley 12/1989 on the public statistical function** —
amended in 2022 — and by the statute approved by Real Decreto 803/2022. The
1989 law established it as an autonomous body and provided for coordination
with the autonomous communities, the National Statistical Plan, and
relations with the European Union in statistical matters.

Its functions include large-scale statistical operations (demographic and
economic censuses, social and economic statistics, business directories),
preparing the National Statistical Plan with the ministries and the Bank of
Spain, proposing norms on statistical concepts and classifications, and
**managing statistical relations with international organisations such as
Eurostat**.

## The statistics cluster's first edge, now a stated fact

`discovery/unresolved.md` carried a cluster of **five refused links**
across four countries: [[UN-UNSD]] → [[EU-EUROSTAT]], [[NL-CBS]] and
[[DE-DESTATIS]] to Eurostat, and [[DE-BSTATG]] and [[NL-WET-CBS]] to
[[UN-FPOS]]. Every one was refused for want of a source.

This entity was the first to close a version of that gap, though
originally only as an Atlas interpretation at low confidence: the
sources available at the time described the European Statistical
System's three-party structure (Eurostat, the member states' NSIs, and
other bodies) without directly naming INE among them.

**Re-reading ine.es's own SEE page directly this pass closes that gap
properly.** The page states outright: "Sistema Estadístico Europeo (SEE)
está formado por: Eurostat..., las oficinas de estadística de todos los
estados miembros (**los diferentes INE**)..." — INE names itself, in its
own words, as one of "the various INEs" the ESS comprises. That is no
longer a structure the Atlas infers a connection from; it is INE stating
its own membership, the same tier of evidence [[PL-GUS]] and
[[FI-TILASTOKESKUS]] carry.

**Correction: the ESS entity now exists.** This entity's own prose, from
before this pass, said no [[EU-ESS]] node had been created and that doing
so inside a country batch would bake country-shaped assumptions into a
shared layer. That is stale — [[EU-ESS]] was created in an intervening
batch and already carries `part-of` edges from [[PL-GUS]] and
[[FI-TILASTOKESKUS]]. This entity's edge now points to that existing
node directly, rather than to [[EU-EUROSTAT]] as it did before.

## Relationships

- `part-of` [[ES]] — anchor edge, confirmed this pass.
- `part-of` [[EU-ESS]] — upgraded to a sourced fact this pass.

## Sources

Listed in frontmatter, three of four read directly this pass — the BOE
text of Ley 12/1989, INE's own "about us" page, and its own SEE
explanation. The EUR-Lex summary was not attempted.
