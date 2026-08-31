---
id: NL-BRI
type: platform
name: Basisregistratie Inkomen
alternative_names:
  - BRI
  - Base Registry of Income
description: >
  The Dutch base registry of income, in existence since 1 January 2009 and
  established in Chapter IVA, articles 21 to 22i, of the Algemene wet inzake
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
last_verified: "2026-08-30"
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
    evidence: "Confirmed by reading belastingdienst.nl's own page on 'geregistreerde inkomen' directly (2026-08-27): 'het inkomen dat wij registreren in de basisregistratie inkomen (BRI)' is based on the verzamelinkomen from a filed return, or on registered wage/benefit/pension income where no return was filed — the same authentic-datum definition this entity's description gives. NORA Online's BRI page, also read directly, confirms the Belastingdienst as both 'verstrekker' (provider) and 'bronhouder' (data holder), with the Ministry of Finance as commissioning body, and describes the BRI as covering roughly thirteen million citizens. Neither page read this pass states the Chapter IVA / articles 21–21k citation or the 1 January 2009 start date explicitly. The article-range citation is now independently confirmed and corrected (see below)."
    confidence: high
    valid_from: 2009-01-01
    valid_until: null
  - type: governed-by
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "Confirmed by reading wetten.overheid.nl's own consolidated text of the Algemene wet inzake rijksbelastingen (BWBR0002320) directly (2026-08-30): Hoofdstuk IVA, titled 'Basisregistratie inkomen', runs from article 21 to article 22i — not 21 to 21k as this entity previously stated, a citation inherited from Wikipedia and never independently checked against primary legal text. Article 21 opens: 'In dit hoofdstuk en de daarop berustende bepalingen wordt verstaan onder: a. basisregistratie: verzameling gegevens waarvan bij wet is bepaald dat deze authentieke gegevens bevat...' and Article 21a states plainly: 'Er is een basisregistratie inkomen waarin inkomensgegevens met bijbehorende temporele en meta-kenmerken zijn opgenomen' (there is a base registry of income in which income data with associated temporal and meta characteristics are recorded) — closing the research-queue item that had stood open since the register batch, since the AWR itself is not modelled as a separate Atlas entity and this is the closest the ontology allows to a `governed-by` edge for the chapter that constitutes the BRI."
    confidence: high
    valid_from: null
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
  - title: "Algemene wet inzake rijksbelastingen — Hoofdstuk IVA (BWBR0002320)"
    url: "https://wetten.overheid.nl/BWBR0002320/2026-01-01"
    publisher: "wetten.overheid.nl (Ministerie van Justitie en Veiligheid / KOOP)"
    accessed: "2026-08-30"
---

# BRI — Basisregistratie Inkomen

> **Corrected 2026-08-30.** A research-queue item open since the register
> batch — Chapter IVA of the Algemene wet inzake rijksbelastingen, this
> entity's statutory basis, never checked against primary legal text — is
> now closed. Reading `wetten.overheid.nl`'s own consolidated AWR text
> directly finds a real correction: the chapter runs from **article 21 to
> article 22i**, not 21 to 21k as this entity previously stated (a citation
> inherited from Wikipedia and NORA Online and never independently
> verified). This is also the tenth and last of the Atlas's basisregistraties
> to gain a `governed-by` edge, closing the gap [[NL-BASISREGISTRATIES]]
> flagged as its one remaining open statute.

## Description

The BRI has existed since **1 January 2009** and is established in **Chapter
IVA, articles 21 to 22i, of the Algemene wet inzake rijksbelastingen** —
confirmed this pass by reading `wetten.overheid.nl`'s own consolidated text
directly, correcting the previous "21 to 21k" citation inherited from
Wikipedia and never checked against primary legal text. Neither
belastingdienst.nl nor NORA Online's page, both read directly in the prior
pass, states the article range; the chapter's own text does. It holds the
**authentic income datum** of roughly **thirteen million citizens**, a
figure NORA Online's own page, read directly, repeats.

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
- `governed-by` [[NL-BASISREGISTRATIES]] — the closest the ontology allows,
  since the AWR itself is not a separate Atlas entity (no law entity was
  created for any of the other nine registers' statutes that already
  existed as general acts, e.g. [[NL-KADASTERWET]] and [[NL-WET-WOZ]]).
  The chapter citation (articles 21–22i) is now confirmed directly against
  primary legal text.

## Sources

Listed in frontmatter, four of five read directly: the Belastingdienst's
own page, NORA Online and the data.overheid.nl dataset page (prior pass),
plus `wetten.overheid.nl`'s own consolidated AWR text (this pass,
2026-08-30). digitaleoverheid.nl's BRI page returned a bot-verification
wall on two separate attempts and is confirmed genuinely unreadable in this
environment, not merely unread.
