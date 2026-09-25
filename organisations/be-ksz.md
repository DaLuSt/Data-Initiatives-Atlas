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
verification: primary-source

start_date: 1990-01-15
end_date: null
last_verified: "2026-09-25"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - BE-KSZ-WET
  - BE-BELGIF
relationships:
  - type: governed-by
    target: BE-KSZ-WET
    source: fact
    evidence: "Confirmed by reading the KSZ's own page directly (2026-08-26): its Article 1 establishes 'a public institution with legal personality' under the name Kruispuntbank van de sociale zekerheid; the KSZ's own GDPR register entry, also read directly, cites the same 1990 act as its legal basis for processing under Article 6(1)(c) GDPR."
    confidence: high
    valid_from: 1990-01-15
    valid_until: null
  - type: participates-in
    target: BE-BELGIF
    source: fact
    evidence: "Confirmed by reading belgif.be's own 'Wat is een dienstenintegrator?' page directly (2026-09-25): it names KSZ as one of Belgium's six public service integrators, describing it as 'de drijvende kracht en coordinator van e-government in de sociale sector' (the driving force and coordinator of e-government in the social sector) — matching [[BE-BELGIF]]'s own already-recorded description of the KSZ as one of its six supporting integrators."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Wat doet de KSZ en hoe doet ze het?"
    url: "https://www.ksz-bcss.fgov.be/nl/over-de-ksz/ksz-in-het-kort/wat-doet-de-ksz-en-hoe-doet-ze-het"
    publisher: "Kruispuntbank van de Sociale Zekerheid (KSZ/BCSS)"
    accessed: "2026-08-26"
  - title: "Wet van 15 januari 1990 houdende oprichting en organisatie van een Kruispuntbank van de sociale zekerheid"
    url: "https://www.ksz-bcss.fgov.be/nl/page/wet-van-15-januari-1990-houdende-oprichting-en-organisatie-van-een-kruispuntbank-van-de-sociale-zekerheid"
    publisher: "Kruispuntbank van de Sociale Zekerheid (KSZ/BCSS)"
    accessed: "2026-08-26"
  - title: "Gegevens- en dienstencatalogus sociale sector"
    url: "https://www.ksz-bcss.fgov.be/nl/gegevensbescherming/gegevens-en-dienstencatalogus-sociale-sector"
    publisher: "Kruispuntbank van de Sociale Zekerheid (KSZ/BCSS)"
  - title: "Kruispuntbank van de Sociale Zekerheid"
    url: "https://nl.wikipedia.org/wiki/Kruispuntbank_van_de_Sociale_Zekerheid"
    publisher: "Wikipedia"
    accessed: "2026-08-26"
  - title: "Kruispuntbank van de Sociale Zekerheid — AVG Register"
    url: "https://gdpr.belgium.be/nl/federal-institutions/kruispuntbank-van-de-sociale-zekerheid"
    publisher: "gdpr.belgium.be (Belgian federal government)"
    accessed: "2026-08-26"
  - title: "Wat is een dienstenintegrator?"
    url: "https://belgif.be/page/integrators.nl.html"
    publisher: "Belgian Interoperability Framework (BELGIF)"
    accessed: "2026-09-25"
---

# Kruispuntbank van de Sociale Zekerheid (KSZ / BCSS)

> **Verified 2026-08-26.** Four of five sources were read directly. The
> KSZ's own page quotes its founding Article 1; its own GDPR register entry
> gives a different institution count than Wikipedia does — flagged rather
> than resolved, below. `verification: primary-source`.
>
> **Linked to [[BE-BELGIF]], 2026-09-25**: BELGIF's own site, read
> directly, confirms KSZ as one of Belgium's six public service
> integrators, closing `discovery/unresolved.md` row #98 alongside
> [[BE-BOSA]] and [[BE-DIGITAAL-VLAANDEREN]].

## Description

The KSZ is a Belgian federal institution **established in 1990** under the
FOD Sociale Zekerheid, acting as a **service integrator**
(dienstenintegrator) that organises secure data exchange across an
electronic network connecting, per its own current GDPR register entry,
**approximately 3000 actors** responsible for social protection — Wikipedia,
also read this pass, instead gives "roughly 2000 institutions," matching
what this entity previously stated. Both are genuine, dated readings; the
discrepancy is recorded rather than resolved.

Its architecture is the interesting part, and it is unusually explicit in
the sources:

- It upholds the **"only once"** principle — data already held is not
  collected again from citizens and businesses. Confirmed verbatim from the
  KSZ's own page: "identical data are not requested twice by different
  institutions from the same person."
- Information exchanged through the network is **not centralised**. It is
  collected and validated by different **authentic sources** and stored in
  their own decentralised databases — confirmed directly: "the KSZ is not a
  central database," and wage data, for instance, "are preserved and
  updated by the RSZ."
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

- `governed-by` [[BE-KSZ-WET]] — confirmed directly from the KSZ's own
  Article 1 and its GDPR register entry.
- `participates-in` [[BE-BELGIF]] — new 2026-09-25, sourced from BELGIF's
  own integrators page.

## Sources

Four of five read directly the first pass — the KSZ's own "what it does"
page, its founding-act page (quoting Article 1), Wikipedia, and its GDPR
register entry. The data/services catalogue page was not re-fetched.
BELGIF's own integrators page was added and read directly 2026-09-25.
