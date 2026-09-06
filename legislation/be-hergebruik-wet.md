---
id: BE-HERGEBRUIK-WET
type: law
name: Wet inzake het hergebruik van overheidsinformatie
alternative_names:
  - Wet van 4 mei 2016
  - Loi du 4 mai 2016 relative à la réutilisation des informations du secteur public
  - Belgian PSI Re-use Act
description: >
  Belgian federal act of 4 May 2016 on open data and the re-use of public
  sector information, described as the regulatory framework for open data
  in Belgium and as aligned with the European PSI Directive on the re-use of
  public sector information.

level: national
country: BE
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-06"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-PSI-DIRECTIVE
  - BE
  - BE-DATA-GOV-BE
  - EU-OPEN-DATA-DIRECTIVE
  - BE-HERGEBRUIK-WET-2023
relationships:
  - type: implements-requirement-from
    target: EU-PSI-DIRECTIVE
    source: fact
    evidence: "Confirmed by reading the act's original enacted text at etaamb.openjustice.be directly (2026-08-26): its Article 1 states 'Deze wet vormt de omzetting in Belgisch recht van de Richtlijn 2003/98/EG van het Europees Parlement en de Raad van 17 november 2003' — this act transposes Directive 2003/98/EC into Belgian law, as amended by Directive 2013/37/EU, later recast as Directive (EU) 2019/1024. Recorded against the PSI Directive rather than the Open Data Directive because the 2016 act predates the 2019 recast; see EU-PSI-DIRECTIVE."
    confidence: high
    valid_from: null
    valid_until: null
  - type: applies-in
    target: BE
    source: fact
    evidence: "Confirmed by reading the act's text directly (2026-08-26): it is a Belgian federal act on open data and the re-use of public sector information. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Wet van 04/05/2016 inzake het hergebruik van overheidsinformatie"
    url: "https://etaamb.openjustice.be/nl/wet-van-04-mei-2016_n2016009236.html"
    publisher: "etaamb / OpenJustice"
    accessed: "2026-09-06"
  - title: "Wet van 4 mei 2016 inzake het hergebruik van overheidsinformatie (Belgisch Staatsblad) — geconsolideerde tekst (Justel)"
    url: "https://www.ejustice.just.fgov.be/cgi_loi/change_lg.pl?language=nl&la=N&table_name=wet&cn=2016050417"
    publisher: "Belgisch Staatsblad / Moniteur belge (FOD Justitie)"
    accessed: "2026-08-26"
  - title: "De Algemene Directie Statistiek van de FOD Economie gaat voor Open Data"
    url: "https://news.belgium.be/nl/de-algemene-directie-statistiek-van-de-fod-economie-gaat-voor-open-data"
    publisher: "news.belgium.be (Belgian federal government)"
  - title: "Hergebruik van overheidsdata"
    url: "https://www.bipt.be/operatoren/hergebruik-van-overheidsdata"
    publisher: "BIPT (Belgisch Instituut voor postdiensten en telecommunicatie)"
    accessed: "2026-08-26"
---

# Wet van 4 mei 2016 (re-use of public sector information)

> **Verified 2026-08-26; licensing/pricing/appeals content closed
> 2026-09-06.** The act's own original text and its current consolidated
> (Justel) text, both on Belgium's statute-book mirrors, and a BIPT
> sectoral page have all been read directly. `news.belgium.be` was not
> read. `verification: primary-source`.

## Description

The act of **4 May 2016** governs open data and the re-use of public sector
information at Belgian federal level. Confirmed directly from its own
Article 1: it transposes **Directive 2003/98/EC**, the original PSI
Directive, as amended by Directive 2013/37/EU — whose stated aims are to
improve knowledge, develop the potential of information, and contribute to
economic growth and job creation. BIPT's own page independently states the
same transposition and adds that a **Royal Decree of 2 June 2019**
implements the act's re-use procedures.

## ⚠ This does not connect to [[EU-OPEN-DATA-DIRECTIVE]] *directly* — and reading the act's own text confirms why

The obvious move would be `implements-requirement-from` →
[[EU-OPEN-DATA-DIRECTIVE]], matching [[NL-WHO]] and [[DE-DNG]]. **It stays
refused, and this pass turned the chronological argument from an inference
into a reading.**

- This act is from **2016**, and its own Article 1, read directly, cites
  **Directive 2003/98/EC**, not the 2019 recast.
- [[EU-OPEN-DATA-DIRECTIVE]] is Directive (EU) **2019**/1024.

A 2016 act cannot transpose a 2019 directive, and now its own text says so.
What the act actually transposes is the **PSI Directive** — Directive
2003/98/EC as amended by 2013/37/EU — which the Open Data Directive later
recast, and which is **not an Atlas entity**.

So Belgium's original position differed from its two neighbours:

| Country | Open Data Directive transposition |
|---|---|
| Netherlands | [[NL-WHO]] — recorded |
| Germany | [[DE-DNG]] — recorded |
| Belgium | **found by a later pass**: [[BE-HERGEBRUIK-WET-2023]] |

That gap is now closed. [[BE-HERGEBRUIK-WET-2023]], adopted seven years
after this act and confirmed this pass, amended this act to add exactly the
missing reference: reading the **current consolidated (Justel) text** of
this act shows its Article 1 now also reads *"Deze wet vormt de omzetting in
Belgisch recht van Richtlijn (EU) 2019/1024 ... (herschikking)"* — the
recast directive's citation was inserted by the 2023 amendment. The
consolidated text's title has also changed, from "Wet inzake het hergebruik
van overheidsinformatie" to **"Wet inzake open data en het hergebruik van
overheidsinformatie"**.

**The `implements-requirement-from` → [[EU-OPEN-DATA-DIRECTIVE]] edge still
does not go on this entity.** Following the convention already used for
[[BE-BRU-ORDONNANCE-2016]] / [[BE-BRU-ORDONNANCE-2021]] — where the amending
instrument carries `implements-requirement-from` and the amended act carries
only the receiving end of `amends` — that edge lives on
[[BE-HERGEBRUIK-WET-2023]], not here, even though this act's own current
text now cites the directive. This entity keeps its original
`implements-requirement-from` → [[EU-PSI-DIRECTIVE]], describing what it
did in 2016.

This was the sharpest case in the original batch of the pattern-matching
trap: the shape of the Atlas made a wrong answer attractive. It is recorded
in `discovery/unresolved.md` as closed by [[BE-HERGEBRUIK-WET-2023]].

`confidence: medium` (raised from `low`) reflects that the act's
transposition basis and its later amendment are now both confirmed from
primary text.

## Licensing, pricing and the appeals commission, closed 2026-09-06

**Closes a previously-flagged gap.** `coverage` raised to `medium`:
these obligations were previously described only in prose from BIPT, a
secondary source; the act's own text at etaamb.openjustice.be, read
directly, now supports them.

- **Licensing (Articles 5, 7)**: authorities may make documents available
  for re-use unconditionally or subject to conditions; where conditions
  are set, the King establishes standard licences, made available
  electronically in machine-readable form where possible. Conditions
  "mogen niet discriminerend zijn voor vergelijkbare categorieën van
  hergebruik" (Article 5§1) — may not discriminate between comparable
  categories of re-use.
- **Pricing (Articles 6, 8)**: where a fee is charged, "blijft deze
  vergoeding beperkt tot de marginale kosten voor hun vermenigvuldiging,
  verstrekking en verspreiding" (Article 8§1) — limited to the marginal
  cost of reproduction, provision and dissemination, with an exception for
  bodies required by regulation to generate substantial revenue, whose
  fees must instead follow "vooraf vastgestelde objectieve, transparante en
  controleerbare criteria." Public bodies must publish fee amounts and
  calculation bases, and explain the calculation on request (Article 6§2–3).
- **Appeals commission (Articles 11–17)**: "Er wordt een federale
  beroepscommissie van het hergebruik van de bestuursdocumenten opgericht"
  (Article 11§1) — a federal appeals commission for the re-use of
  administrative documents is established. Appeals must be filed within
  sixty days (Article 14); the commission decides "zo spoedig mogelijk"
  and within thirty days of registration at the latest (Article 17§1).

## Relationships

**None asserted from this entity toward [[EU-OPEN-DATA-DIRECTIVE]]** — see
above. `related_entities` records the association for navigation only.

- `implements-requirement-from` [[EU-PSI-DIRECTIVE]] — confirmed directly
  from the act's own Article 1.
- `applies-in` [[BE]] — anchor edge.

## Sources

Listed in frontmatter, three of four read directly across two passes —
the act's original 2016 text (Articles 1, 5–8 and 11–17, read directly
this pass for the licensing/pricing/appeals gap), its current
consolidated (Justel) text showing the 2023 amendment, and a BIPT
sectoral page. `news.belgium.be` was not read.
