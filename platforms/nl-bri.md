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
verification: primary-source

start_date: 2009-01-01
end_date: null
last_verified: "2026-08-27"
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
    evidence: "Confirmed by reading data.overheid.nl's dataset page for the BRI directly (2026-08-27): it defines a basisregistratie as an officially designated registration that all government bodies must use for public-law tasks, and lists the Belastingdienst as data owner. digitaleoverheid.nl's dedicated BRI page returned a bot-verification wall on two attempts this pass ('Please wait while your request is being verified...') and is confirmed genuinely unreadable in this environment, not merely unread."
    confidence: high
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NL-BELASTINGDIENST
    source: fact
    evidence: "Confirmed by reading belastingdienst.nl's own page on 'geregistreerde inkomen' directly (2026-08-27): 'het inkomen dat wij registreren in de basisregistratie inkomen (BRI)' is based on the verzamelinkomen from a filed return, or on registered wage/benefit/pension income where no return was filed — the same authentic-datum definition this entity's description gives. NORA Online's BRI page, also read directly, confirms the Belastingdienst as both 'verstrekker' (provider) and 'bronhouder' (data holder), with the Ministry of Finance as commissioning body, and describes the BRI as covering roughly thirteen million citizens. Neither page read this pass states the Chapter IVA / articles 21–21k citation or the 1 January 2009 start date explicitly — those remain as sourced to nl.wikipedia.org and digitaleoverheid.nl (the latter confirmed bot-walled this pass), not independently re-confirmed by primary text."
    confidence: high
    valid_from: 2009-01-01
    valid_until: null

sources:
  - title: "BRI — Stelsel van basisregistraties (confirmed bot-walled, not read)"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/10-basisregistraties/bri/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "Alles over het geregistreerde inkomen"
    url: "https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/werk_en_inkomen/geregistreerde_inkomen_en_de_inkomensverklaring/alles_over_geregistreerde_inkomen/alles-over-het-geregistreerde-inkomen"
    publisher: "Belastingdienst"
    accessed: "2026-08-27"
  - title: "BRI (Basisregistratie Inkomen) — NORA Online"
    url: "https://www.noraonline.nl/wiki/BRI_(Basisregistratie_Inkomen)"
    publisher: "NORA Online"
    accessed: "2026-08-27"
  - title: "Basisregistratie: Inkomen (BRI)"
    url: "https://data.overheid.nl/dataset/22495-basisregistratie--inkomen--bri---donl-"
    publisher: "data.overheid.nl"
    accessed: "2026-08-27"
---

# BRI — Basisregistratie Inkomen

> **Verified 2026-08-27.** Three of four cited pages were read directly:
> the Belastingdienst's own page, NORA Online, and the data.overheid.nl
> dataset page. digitaleoverheid.nl's BRI page is confirmed genuinely
> bot-walled in this environment on two separate attempts, not merely
> unread. The Chapter IVA / articles 21–21k statutory citation was not
> independently re-confirmed by primary legal text this pass.

## Description

The BRI has existed since **1 January 2009** and is established in **Chapter
IVA, articles 21 to 21k, of the Algemene wet inzake rijksbelastingen** — a
citation carried over from Wikipedia and NORA Online and not independently
re-confirmed against primary legal text this pass; neither belastingdienst.nl
nor NORA Online's page, both read directly this pass, states the article
range. It holds the **authentic income datum** of roughly **thirteen
million citizens**, a figure NORA Online's own page, read directly, repeats.

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

Listed in frontmatter, three of four read directly this pass — the
Belastingdienst's own page, NORA Online and the data.overheid.nl dataset
page. digitaleoverheid.nl's BRI page returned a bot-verification wall on two
separate attempts and is confirmed genuinely unreadable in this environment,
not merely unread this pass.
