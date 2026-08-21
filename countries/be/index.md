# Belgium — Index

Curated navigation hub for all Belgium-scoped (`country: BE`) entities in
the Atlas. This is a human-maintained page, not a generated one — add a
wikilink here whenever a new BE-scoped entity is judged important enough to
belong on the country's front page (`CONTRIBUTING.md`).

Anchor entity: [[BE]]

> **Sourcing caveat.** Every Belgian entity below was compiled from
> search-engine results only: the cited pages were confirmed to exist but
> were **not read**, because the working environment blocked page
> retrieval. They carry `verification: search-only` and need a
> re-verification pass against primary sources. See
> `progress/current-batch.md`.

> ⚠ **This index covers the federal layer only.** Belgium's Regions and
> Communities run much of its public-sector digitalisation — Digitaal
> Vlaanderen, the Agence du Numérique, Paradigm, and the **OSLO** semantic
> interoperability standards — and none of them is modelled, because the
> Atlas has no `level` term for a Belgian Region. See [[BE]].

## Organisations

- [[BE-BOSA]] — FOD Beleid en Ondersteuning, DG Digitale Transformatie
- [[BE-CCB]] — Centrum voor Cybersecurity België _(national CSIRT)_
- [[BE-APD]] — Gegevensbeschermingsautoriteit
- [[BE-STATBEL]] — national statistical office
- [[BE-KSZ]] — Kruispuntbank van de Sociale Zekerheid _(service integrator)_

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
| [[EU-OPEN-DATA-DIRECTIVE]] | _(not established)_ | [[DE-DNG]] | [[NL-WHO]] |
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

- **Any Region or Community**, and therefore **OSLO**, Digitaal Vlaanderen,
  the Agence du Numérique and Paradigm. The Atlas's `level` vocabulary has
  no term between `national` and `local`, and `regional` already means
  supra-national. This is the batch's principal finding — see [[BE]].
- The **six public service integrators** as a set; only [[BE-KSZ]] is
  modelled.
- Belgium's eID / itsme digital identity scheme, the eHealth platform, the
  Kruispuntbank van Ondernemingen, and NBN (the national standards body).
  All queued in `discovery/research-queue.md`.
