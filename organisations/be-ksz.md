---
id: BE-KSZ
type: organisation
name: Kruispuntbank van de Sociale Zekerheid
alternative_names:
  - KSZ
  - Banque Carrefour de la Sécurité Sociale
  - BCSS
  - Crossroads Bank for Social Security
description: >
  Belgian federal institution established in 1990, acting as a service
  integrator that organises secure data exchange across an electronic
  network connecting roughly 2000 institutions in the social security
  sector. It upholds the "only once" principle: data already held by an
  authentic source is not collected again from citizens and businesses. The
  data is not centralised — it stays in the decentralised databases of the
  authentic sources, and the KSZ itself has no access to it.

level: sectoral
country: BE
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 1990-01-15
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - BE-KSZ-WET
relationships:
  - type: governed-by
    target: BE-KSZ-WET
    source: fact
    evidence: "The KSZ was established and organised by the wet van 15 januari 1990 houdende oprichting en organisatie van een Kruispuntbank van de sociale zekerheid (ksz-bcss.fgov.be; nl.wikipedia.org 'Kruispuntbank van de Sociale Zekerheid'). NOT READ — search-only."
    confidence: medium
    valid_from: 1990-01-15
    valid_until: null

sources:
  - title: "Wat doet de KSZ en hoe doet ze het?"
    url: "https://www.ksz-bcss.fgov.be/nl/over-de-ksz/ksz-in-het-kort/wat-doet-de-ksz-en-hoe-doet-ze-het"
    publisher: "Kruispuntbank van de Sociale Zekerheid (KSZ/BCSS)"
  - title: "Wet van 15 januari 1990 houdende oprichting en organisatie van een Kruispuntbank van de sociale zekerheid"
    url: "https://www.ksz-bcss.fgov.be/nl/page/wet-van-15-januari-1990-houdende-oprichting-en-organisatie-van-een-kruispuntbank-van-de-sociale-zekerheid"
    publisher: "Kruispuntbank van de Sociale Zekerheid (KSZ/BCSS)"
  - title: "Gegevens- en dienstencatalogus sociale sector"
    url: "https://www.ksz-bcss.fgov.be/nl/gegevensbescherming/gegevens-en-dienstencatalogus-sociale-sector"
    publisher: "Kruispuntbank van de Sociale Zekerheid (KSZ/BCSS)"
  - title: "Kruispuntbank van de Sociale Zekerheid"
    url: "https://nl.wikipedia.org/wiki/Kruispuntbank_van_de_Sociale_Zekerheid"
    publisher: "Wikipedia"
---

# Kruispuntbank van de Sociale Zekerheid (KSZ / BCSS)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The KSZ is a Belgian federal institution **established in 1990** under the
FOD Sociale Zekerheid, acting as a **service integrator**
(dienstenintegrator) that organises secure data exchange across an
electronic network connecting roughly **2000 institutions** in the social
security sector.

Its architecture is the interesting part, and it is unusually explicit in
the sources:

- It upholds the **"only once"** principle — data already held is not
  collected again from citizens and businesses.
- Information exchanged through the network is **not centralised**. It is
  collected and validated by different **authentic sources** and stored in
  their own decentralised databases.
- Personal data is exchanged automatically and securely **without the KSZ
  having access to it**.
- Duplicate storage and duplicate quality control across public social
  security institutions are avoided as far as possible.

## Three national answers to the same problem

Once-only is a European commitment ([[EU-SDG]]), and the Atlas now holds
three national mechanisms for it — which is the clearest illustration so
far of why the country-neutral model matters:

| Country | Mechanism | Approach |
|---|---|---|
| Belgium | **KSZ/BCSS** (1990) | a **broker** between decentralised authentic sources, with no central store and no access by the broker |
| Netherlands | [[NL-BASISREGISTRATIES]] | a system of designated **authentic registrations** |
| Germany | [[DE-REGMOG]] (2021) | a **shared identifier** (the Steuer-ID) used across existing registers |

Three federal-or-decentralised states, three genuinely different designs,
and Belgium's is the oldest by three decades. **No relationship between
them is asserted** — they solve a common problem, which is not a
relationship.

**No `implements-requirement-from` → [[EU-SDG]] is asserted either**, for
the same reason it was refused for [[DE-REGMOG]]: the KSZ predates the
regulation by 28 years, and no source read connects them.

## `level: sectoral`

Recorded as `sectoral` rather than `national`: the KSZ is a federal
institution whose authority is bounded to the social security sector, which
is the reading already applied to [[NL-NICTIZ]] and [[NL-ROSA]]. The
convention is now used four times across three countries and should
probably be written into `metadata/taxonomy.md` rather than remaining a
precedent. Logged in `discovery/unresolved.md`.

## Relationships

- `governed-by` [[BE-KSZ-WET]].

## Sources

Listed in frontmatter.
