---
id: NL-BRI
type: platform
name: Basisregistratie Inkomen
alternative_names:
  - BRI
  - Base Registry of Income
description: >
  The Dutch base registry of income, in existence since 1 January 2009 and
  established in Chapter IVA, articles 21 to 21k, of the Algemene wet inzake
  rijksbelastingen. It holds the authentic income datum of approximately
  thirteen million citizens, with associated temporal and meta
  characteristics. The authentic datum is the income as determined by the
  tax administration for the relevant tax year: the combined income for
  those obliged to file, or the taxable annual wage for those who are not.
  The registry holds only the combined income, or where unavailable the
  taxable annual wage, for the previous calendar year. Its purpose is to
  supply income data to authorised government bodies so that individuals do
  not have to supply their income themselves, and it is used to determine
  allowances, subsidies and benefits.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2009-01-01
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-BELASTINGDIENST
related_entities:
  - NL-BASISREGISTRATIES
  - NL-BELASTINGDIENST
relationships:
  - type: part-of
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "The ten base registrations are the BRP, HR, BAG, BRT, BRK, BRV, BRI (Basisregistratie Inkomen), WOZ, BGT and BRO (digitaleoverheid.nl '10 basisregistraties'; data.overheid.nl; noraonline.nl). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NL-BELASTINGDIENST
    source: fact
    evidence: "The BRI has existed since 1 January 2009 and is established in Chapter IVA (articles 21 to 21k) of the Algemene wet inzake rijksbelastingen; the authentic income datum is the income as determined by the Belastingdienst for the relevant tax year (nl.wikipedia.org 'Basisregistratie Inkomen'; noraonline.nl 'BRI'; digitaleoverheid.nl BRI page; belastingdienst.nl 'Alles over het geregistreerde inkomen'). NOT READ — search-only."
    confidence: medium
    valid_from: 2009-01-01
    valid_until: null

sources:
  - title: "BRI — Stelsel van basisregistraties"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/10-basisregistraties/bri/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "Alles over het geregistreerde inkomen"
    url: "https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/werk_en_inkomen/geregistreerde_inkomen_en_de_inkomensverklaring/alles_over_geregistreerde_inkomen/alles-over-het-geregistreerde-inkomen"
    publisher: "Belastingdienst"
  - title: "BRI (Basisregistratie Inkomen) — NORA Online"
    url: "https://www.noraonline.nl/wiki/BRI_(Basisregistratie_Inkomen)"
    publisher: "NORA Online"
  - title: "Basisregistratie: Inkomen (BRI)"
    url: "https://data.overheid.nl/dataset/22495-basisregistratie--inkomen--bri---donl-"
    publisher: "data.overheid.nl"
---

# BRI — Basisregistratie Inkomen

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The BRI has existed since **1 January 2009** and is established in **Chapter
IVA, articles 21 to 21k, of the Algemene wet inzake rijksbelastingen**. It
holds the **authentic income datum** of roughly **thirteen million
citizens**.

The authentic datum is the income as determined by the
[[NL-BELASTINGDIENST]] for the relevant tax year:

- for those **obliged to file**, the combined income (*verzamelinkomen*);
- for those **not obliged to file**, the taxable annual wage
  (*belastbaar jaarloon*).

The registry holds only that one figure, for the **previous calendar year**.
Its purpose is that government bodies can obtain a citizen's income without
the citizen supplying it, and it is used to determine allowances, subsidies
and benefits.

## The narrowest register in the stelsel, and the most consequential per field

The BRI is one number per person per year. That is the whole register.

Yet it determines allowances, subsidies and benefits for thirteen million
people, which makes it the register where a single incorrect value has the
most direct effect on an individual. The stelsel's design goal — collect
once, reuse everywhere — is at its most visible and its most consequential
here.

**The Atlas records none of that consequence**, because the "afnemer"
relationships that carry it are exactly what the relationship vocabulary
cannot express. See [[NL-BELASTINGDIENST]].

## `authentiek gegeven` is a concept the Atlas has no field for

*Authentiek gegeven* is a specific legal status in the stelsel: a datum
government bodies are **obliged to use** and, in principle, may not
independently re-determine. It is what distinguishes a base registry from
any other government database.

The Atlas has no metadata field for it, and no relationship type that says
"is the authoritative source for". It appears in this description and in
those of the other nine registers, and nowhere in the structured data.

This is a **third distinct expressive gap** found in this batch, alongside
authorised use and key-sharing couplings. All three are logged together in
`discovery/unresolved.md`, because they are plausibly one gap: the Atlas
models what things *are* and what they *descend from*, and has almost no
vocabulary for how data actually moves between them.

## Relationships

- `part-of` [[NL-BASISREGISTRATIES]].
- `maintained-by` [[NL-BELASTINGDIENST]].

**No `governed-by` edge**, though the statutory basis is well sourced: the
AWR is not an entity in the Atlas, and no law entity was created for any of
the nine registers whose statute was not already modelled. See
[[NL-BASISREGISTRATIES]].

## Sources

Listed in frontmatter. Note that one of the four is Wikipedia; it is the
source of the article-range detail (21–21k), corroborated by NORA Online.
