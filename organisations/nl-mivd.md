---
id: NL-MIVD
type: organisation
name: Militaire Inlichtingen- en Veiligheidsdienst
alternative_names:
  - MIVD
  - Defence Intelligence and Security Service
  - Military Intelligence and Security Service
description: >
  The Dutch military intelligence and security service, operating under the
  Minister of Defence. It shares its statutory framework with the AIVD: the
  Wet op de inlichtingen- en veiligheidsdiensten 2017 governs both services,
  and both are subject to binding prior review by the TIB and retrospective
  oversight by the CTIVD.

level: national
country: NL
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - NL-WIV-2017
  - NL-TWCO
  - NL-AIVD
  - NL-CTIVD
  - NL-TIB
relationships:
  - type: governed-by
    target: NL-WIV-2017
    source: fact
    evidence: "The Wiv 2017 is the legal framework for the AIVD and the MIVD and establishes the tasks of the services and the exercise of their powers; the Ministry of Defence publishes the rules the MIVD must observe under that act (defensie.nl 'Regels waar de MIVD zich aan moet houden'; aivd.nl 'Wet op de inlichtingen- en veiligheidsdiensten'; rijksoverheid.nl). NOT READ — search-only."
    confidence: medium
    valid_from: 2018-05-01
    valid_until: null
  - type: governed-by
    target: NL-TWCO
    source: fact
    evidence: "The Tijdelijke wet onderzoeken AIVD en MIVD naar landen met een offensief cyberprogramma allows temporary deviation from the regime in the Wiv 2017 for investigations by the AIVD and MIVD into countries with an offensive cyber programme; it entered into force on 1 July 2024 (aivd.nl; eerstekamer.nl dossier 36.263; wetgevingskalender.overheid.nl WGK013565). NOT READ — search-only."
    confidence: medium
    valid_from: 2024-07-01
    valid_until: null

sources:
  - title: "Regels waar de MIVD zich aan moet houden"
    url: "https://www.defensie.nl/onderwerpen/m/militaire-inlichtingen-en-veiligheid/werken-volgens-de-regels"
    publisher: "Ministerie van Defensie"
  - title: "Toetsing, toezicht en controle"
    url: "https://www.defensie.nl/onderwerpen/m/militaire-inlichtingen-en-veiligheid/toetsing-toezicht-en-controle"
    publisher: "Ministerie van Defensie"
  - title: "Nieuwe Wet op de inlichtingen- en veiligheidsdiensten (Wiv 2017)"
    url: "https://www.rijksoverheid.nl/onderwerpen/bevoegdheden-inlichtingendiensten-en-veiligheidsdiensten/wet-op-de-inlichtingen-en-veiligheidsdiensten-wiv"
    publisher: "Rijksoverheid"
---

# Militaire Inlichtingen- en Veiligheidsdienst (MIVD)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

The MIVD is the **military** Dutch intelligence and security service, under
the Minister of Defence. [[NL-AIVD]] is its civilian counterpart under the
Minister of the Interior.

## One act, two services

The structurally interesting fact about the Dutch arrangement is that the
split runs through the *ministries*, not through the *law*.

[[NL-WIV-2017]] governs **both** services. There is no separate military
intelligence act, as there is in Germany ([[DE-MADG]] alongside
[[DE-BNDG]]) and in Poland ([[PL-USKWSWW-2006]] alongside
[[PL-UABWAW-2002]]). [[NL-TIB]] and [[NL-CTIVD]] likewise cover both.

That makes the Netherlands and Belgium — where [[BE-WIV-1998]] similarly
covers [[BE-VSSE]] and [[BE-ADIV]] — the two countries in the Atlas with a
single organic intelligence act, against the German, Polish and British
pattern of one act per service or per pair.

## No ministry parent is asserted

[[NL-AIVD]] carries `part-of` [[NL-BZK]] because the Ministry of the
Interior is an Atlas entity. The **Ministry of Defence is not**, so the
equivalent MIVD edge cannot be made without inventing a node for it. This is
recorded rather than papered over: the asymmetry between the two service
entities is an artefact of Atlas coverage, not of Dutch administrative law.

## Relationships

- `governed-by` [[NL-WIV-2017]] and [[NL-TWCO]].

## Sources

Listed in frontmatter.
