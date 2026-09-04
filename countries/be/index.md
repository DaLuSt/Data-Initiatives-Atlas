# Belgium — Index

Curated navigation hub for all Belgium-scoped (`country: BE`) entities in
the Atlas. This is a human-maintained page, not a generated one — add a
wikilink here whenever a new BE-scoped entity is judged important enough to
belong on the country's front page (`CONTRIBUTING.md`).

Anchor entity: [[BE]]

> **Re-verified 2026-08-26, completed 2026-08-27.** All 24 Belgian
> entities carrying `verification: search-only` were checked against
> primary sources across two passes. **22 are now `primary-source`.**
> The first pass promoted 18: [[BE-BELGIF]], [[BE-BRU-ORDONNANCE-2016]],
> [[BE-BRU-ORDONNANCE-2021]], [[BE-GDPR-WET]], [[BE-HERGEBRUIK-WET-2023]],
> [[BE-HERGEBRUIK-WET]], [[BE-KSZ-WET]], [[BE-NIS1-WET]], [[BE-NIS2-WET]],
> [[BE-VL-BESTUURSDECREET-2021]], [[BE-WAL-DECRET-2022]], [[BE-WIV-1998]],
> [[BE-ADIV]], [[BE-APD]], [[BE-KSZ]], [[BE-NBN]], [[BE-VSSE]] and
> [[BE-DCAT-AP-BE]]. A second pass, finding previously-uncited pages via
> search rather than re-fetching the same blocked URLs, promoted four
> more: [[BE-TOEZICHTSWET-1991]] and [[BE-COMITE-I]] (an
> ejustice.just.fgov.be Justel page that timed out three times in the
> first pass finally succeeded), [[BE-CCB]] (five independent law-firm
> analyses of the NIS2 royal decree), and [[BE-STATBEL]] (the 1962 public
> statistics act, found on etaamb.openjustice.be, closes a long-standing
> "no statutory basis found" gap). **[[BE-BOSA]] and [[BE-DATA-GOV-BE]]
> stay `search-only`** even after both passes tried further routes —
> `dtservices.bosa.be`, `fedweb.belgium.be`, `digitall.be`, GitHub's own
> `Fedict/dcattools` repository — because `bosa.belgium.be`,
> `ccb.belgium.be`, `data.gov.be`, `financien.belgium.be` and
> `statbel.fgov.be` are genuinely bot-walled (CAPTCHA/403) even with an
> honest User-Agent, the Belgian counterpart to the `.gouv.fr` block found
> in the France batch. Two corrections of note from the first pass:
> [[BE-HERGEBRUIK-WET-2023]] was actually published in the Moniteur belge
> on **23 January 2024**, not 25 December 2023 as previously recorded (25
> December is the act's own date); and [[BE-STATBEL]]'s own body text was
> still claiming, ten days after the fact, that no source connected it to
> the European Statistical System — the frontmatter had carried that edge
> since the UN batch of 2026-08-16. See each entity for its own sourcing
> detail.

> ⚠ **This index covered the federal layer only, until 2026-09-04.**
> Belgium's Regions and Communities run much of its public-sector
> digitalisation, and a research-queue pickup closed the gap
> `level: subnational` (added 2026-08-21) had already unblocked:
> [[BE-DIGITAAL-VLAANDEREN]] (Flanders), [[BE-AGENCE-NUMERIQUE]]
> (Wallonia), [[BE-PARADIGM]] (Brussels-Capital, formerly CIRB/CIBG) and
> [[BE-OSLO]], the Flemish semantic-interoperability standard, are now
> all Atlas entities. See [[BE]].

## Organisations

- [[BE-BOSA]] — FOD Beleid en Ondersteuning, DG Digitale Transformatie
- [[BE-CCB]] — Centrum voor Cybersecurity België _(national CSIRT)_
- [[BE-APD]] — Gegevensbeschermingsautoriteit
- [[BE-STATBEL]] — national statistical office
- [[BE-KSZ]] — Kruispuntbank van de Sociale Zekerheid _(service integrator)_
- [[BE-NBN]] — Bureau de Normalisation / Bureau voor Normalisatie _(national standards body — CEN member, CENELEC national committee)_

### Regional and Community digital agencies (`level: subnational`, added 2026-09-04)

- [[BE-DIGITAAL-VLAANDEREN]] — Flanders _(formerly Informatie
  Vlaanderen; renamed 2021)_
- [[BE-AGENCE-NUMERIQUE]] — Wallonia _(AdN; succeeded the Agence
  wallonne des Télécommunications, 2015)_
- [[BE-PARADIGM]] — Brussels-Capital _(formerly CIRB/CIBG, founded 1987)_

## Legislation

### Sub-federal (`level: subnational`, added 2026-08-21)

- [[BE-VL-BESTUURSDECREET-2021]] — Flanders _(adopted 2 July, in force 17 July 2021 — the deadline to the day)_
- [[BE-BRU-ORDONNANCE-2021]] — Brussels-Capital _(amends [[BE-BRU-ORDONNANCE-2016]])_
- [[BE-WAL-DECRET-2022]] — Wallonia
- [[BE-BRU-ORDONNANCE-2016]] — the Brussels 2016 open data ordonnance the
  2021 one amends _(predates the directive by two and a half years)_

### Data protection

- [[BE-GDPR-WET]] — Wet van 30 juli 2018 _(implements [[EU-GDPR]])_

### Cybersecurity

- [[BE-NIS2-WET]] — Wet van 26 april 2024 _(implements [[EU-NIS2]])_
  - [[BE-NIS1-WET]] — Wet van 7 april 2019 _(superseded 2024)_

### Open data and data sharing

- [[BE-HERGEBRUIK-WET]] — Wet van 4 mei 2016 _(PSI-era; **not** the Open
  Data Directive transposition — see the entity)_
  - [[BE-HERGEBRUIK-WET-2023]] — Wet van 25 december 2023 _(**the** Open Data
    Directive transposition, and the amendment that closes the gap the 2016
    entity has flagged since the Belgium batch — twenty-nine months late)_
- [[BE-KSZ-WET]] — Wet van 15 januari 1990 _(the oldest instrument in the Atlas)_

## Frameworks and standards

- [[BE-BELGIF]] — Belgian Interoperability Framework _(`based-on` [[EU-EIF]])_
- [[BE-DCAT-AP-BE]] — Belgian federal DCAT profile _(`based-on` [[EU-DCAT-AP]])_
- [[BE-OSLO]] — Flemish semantic interoperability vocabularies
  _(`maintained-by` [[BE-DIGITAAL-VLAANDEREN]]; added 2026-09-04)_

## Platforms

- [[BE-DATA-GOV-BE]] — federal open data portal

---

## EU instruments that apply in Belgium

**No Belgian copy of any EU instrument exists**, and none should be created
(README §"Country-Neutral Architecture"). Each instrument below is a single
Atlas entity now carrying `applies-in` → [[BE]] alongside [[NL]] and
[[DE]]:

[[EU-GDPR]] · [[EU-NIS2]] · [[EU-CER]] · [[EU-DATA-ACT]] · [[EU-DGA]] ·
[[EU-OPEN-DATA-DIRECTIVE]] · [[EU-AI-ACT]] · [[EU-CYBERSECURITY-ACT]] ·
[[EU-EIDAS2]] · [[EU-SDG]] · [[EU-INTEROPERABLE-EUROPE-ACT]] ·
[[EU-ITS-DIRECTIVE]] · [[EU-INSPIRE]] · [[EU-EHDS]] · [[EU-EIF]] ·
[[EU-DIGITAL-DECADE]]

### The three-country picture

| EU instrument | Belgium | Germany | Netherlands |
|---|---|---|---|
| [[EU-GDPR]] | [[BE-GDPR-WET]] | [[DE-BDSG]] | [[NL-UAVG]] |
| [[EU-NIS2]] | [[BE-NIS2-WET]] | [[DE-NIS2UMSUCG]] | [[NL-CBW]] |
| [[EU-DCAT-AP]] | [[BE-DCAT-AP-BE]] | [[DE-DCAT-AP-DE]] | [[NL-DCAT-AP-NL]] |
| [[EU-EIF]] | **[[BE-BELGIF]]** | _(none sourced)_ | _(none sourced)_ |
| [[EU-OPEN-DATA-DIRECTIVE]] | [[BE-HERGEBRUIK-WET-2023]] _(federal; three sub-federal instruments too)_ | [[DE-DNG]] | [[NL-WHO]] |
| [[EU-INSPIRE]] | [[BE-DCAT-AP-BE]] _(mapping)_ | [[DE-GEOZG]] | _(gap)_ |
| [[EU-ITS-DIRECTIVE]] | _(none)_ | [[DE-MOBILITHEK]] | [[NL-NTM]] |

The blanks are as informative as the entries, and each is explained in the
entity concerned rather than left to be read as absence of fact.

## Intelligence and security services

Added with the intelligence-services batch.

- [[BE-VSSE]] — the **only civilian** service, a department of FPS Justice
- [[BE-ADIV]] / SGRS — military service, under Defence
- [[BE-COMITE-I]] — democratic oversight, reporting to Parliament

Legislation:

- [[BE-WIV-1998]] — the organic act, prescribing the duties of **both**
  services. Its title uses the **singular** while governing two of them.
- [[BE-TOEZICHTSWET-1991]] — the oversight act, creating Comité I *and*
  Comité P.

**Belgium regulated the watchers seven years before the watched.** The
oversight act is 1991; the organic act is 1998. That ordering is unique in
the Atlas — everywhere else the oversight instrument is the later one, by up
to 27 years in the UK.

Both services also carry `governed-by` [[BE-GDPR-WET]]: the 2018 act has a
dedicated subtitle for processing by the intelligence and security services,
and routes verification through [[BE-COMITE-I]] rather than [[BE-APD]].

## Not modelled

- The **six public service integrators** as a set; only [[BE-KSZ]] is
  modelled.
- Belgium's eID / itsme digital identity scheme, the eHealth platform, and
  the Kruispuntbank van Ondernemingen. Queued in
  `discovery/research-queue.md`. **Correction (2026-08-26): NBN, the
  national standards body, was already modelled as [[BE-NBN]]** — this line
  was stale and NBN was missing from the "Organisations" list above, now
  added.
