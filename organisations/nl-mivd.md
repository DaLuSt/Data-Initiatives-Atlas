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
confidence: high
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
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
    evidence: "Confirmed by reading defensie.nl's own 'Werken volgens de regels' page directly (2026-08-27): the MIVD operates under the Wiv 2017 and the Wet veiligheidsonderzoeken (Wvo), with the Wiv 2017 describing 'what the MIVD and AIVD may and must do to safeguard national security'; the MIVD's tasks are formally defined in article 10 of the Wiv 2017. rijksoverheid.nl's current page on the subject (the URL previously cited had moved — read at its new `/themas/` location) independently confirms both the AIVD and MIVD are covered."
    confidence: high
    valid_from: 2018-05-01
    valid_until: null
  - type: governed-by
    target: NL-TWCO
    source: fact
    evidence: "Confirmed by reading defensie.nl's own oversight page directly (2026-08-27): the Tijdelijke wet cyberoperaties applies to the MIVD 'as of July 1, 2024', alongside the Wiv 2017 and Wvo. eerstekamer.nl dossier 36.263 and njb.nl, read directly this pass on the NL-TWCO entity, corroborate the 1 July 2024 entry into force."
    confidence: high
    valid_from: 2024-07-01
    valid_until: null

sources:
  - title: "Regels waar de MIVD zich aan moet houden"
    url: "https://www.defensie.nl/onderwerpen/m/militaire-inlichtingen-en-veiligheid/werken-volgens-de-regels"
    publisher: "Ministerie van Defensie"
    accessed: "2026-08-27"
  - title: "Toetsing, toezicht en controle"
    url: "https://www.defensie.nl/onderwerpen/m/militaire-inlichtingen-en-veiligheid/toetsing-toezicht-en-controle"
    publisher: "Ministerie van Defensie"
    accessed: "2026-08-27"
  - title: "Nieuwe Wet op de inlichtingen- en veiligheidsdiensten (Wiv 2017)"
    url: "https://www.rijksoverheid.nl/themas/recht-veiligheid-en-defensie/bevoegdheden-inlichtingendiensten-en-veiligheidsdiensten/wet-op-de-inlichtingen-en-veiligheidsdiensten-wiv"
    publisher: "Rijksoverheid"
    accessed: "2026-08-27"
---

# Militaire Inlichtingen- en Veiligheidsdienst (MIVD)

> **Verified 2026-08-27.** All three cited pages were read directly this
> pass, closing the previous `search-only` status. The `rijksoverheid.nl`
> URL originally cited had moved (the old address now 404s); its content
> was confirmed at its current `/themas/` location, also read directly, and
> the frontmatter source has been updated to that working URL.

## Description

The MIVD is the **military** Dutch intelligence and security service, under
the Minister of Defence. [[NL-AIVD]] is its civilian counterpart under the
Minister of the Interior. Reading defensie.nl's own pages directly confirms
the MIVD also operates under the **Wet veiligheidsonderzoeken (Wvo)**
alongside the Wiv 2017 — a second statutory instrument not previously
recorded here, though not separately modelled (it is not yet an Atlas
entity).

## One act, two services

The structurally interesting fact about the Dutch arrangement is that the
split runs through the *ministries*, not through the *law*.

[[NL-WIV-2017]] governs **both** services — its Article 10, per defensie.nl,
formally defines the MIVD's tasks (investigating foreign powers, threats to
international order, personnel vetting, and protecting classified military
information). There is no separate military intelligence act, as there is
in Germany ([[DE-MADG]] alongside [[DE-BNDG]]) and in Poland
([[PL-USKWSWW-2006]] alongside [[PL-UABWAW-2002]]). [[NL-TIB]] and
[[NL-CTIVD]] likewise cover both.

That makes the Netherlands and Belgium — where [[BE-WIV-1998]] similarly
covers [[BE-VSSE]] and [[BE-ADIV]] — the two countries in the Atlas with a
single organic intelligence act, against the German, Polish and British
pattern of one act per service or per pair.

## Powers and oversight, confirmed directly

defensie.nl's own page divides MIVD powers into **general powers** (always
permitted, such as consulting informants) and **special powers** (restricted
to serious threats, including surveillance, wiretapping, hacking and
property searches). The most intrusive of these require prior approval from
[[NL-TIB]], whose judgment is binding ("het oordeel van de TIB is bindend");
[[NL-CTIVD]] supervises during and after the fact and can investigate and
make recommendations, though — per this page — its recommendations are
**not binding** in the way TIB's prior approval is. A third layer, the CIVD
(a confidential parliamentary committee of the five largest factions'
leaders), is mentioned but not modelled.

## No ministry parent is asserted

[[NL-AIVD]] carries `part-of` [[NL-BZK]] because the Ministry of the
Interior is an Atlas entity. The **Ministry of Defence is not**, so the
equivalent MIVD edge cannot be made without inventing a node for it. This is
recorded rather than papered over: the asymmetry between the two service
entities is an artefact of Atlas coverage, not of Dutch administrative law.

## Relationships

- `governed-by` [[NL-WIV-2017]] and [[NL-TWCO]].

## Sources

All three sources read directly this pass. The `rijksoverheid.nl` citation
was updated from a now-dead URL to the page's current location, confirmed
live and read.
