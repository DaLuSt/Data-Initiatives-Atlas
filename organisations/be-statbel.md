---
id: BE-STATBEL
type: organisation
name: Statbel
alternative_names:
  - Algemene Directie Statistiek
  - Statistics Belgium
  - Direction générale Statistique
description: >
  Belgian national statistical office, the Algemene Directie Statistiek
  within the FOD Economie. It opened an open data portal in October 2015,
  publishes its statistics under a Creative Commons Attribution 4.0 licence
  and maintains a DCAT catalogue of its open data.

level: national
country: BE
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - BE-DCAT-AP-BE
relationships:
  - type: aligned-with
    target: BE-DCAT-AP-BE
    source: fact
    evidence: "Statbel publishes a DCAT catalogue for its open data (statbel.fgov.be 'DCAT catalogue for Statbel's open data'). Not re-confirmed this pass either — statbel.fgov.be returned a CAPTCHA challenge again on a fresh direct attempt (2026-08-27), including on the underlying PDF asset. Recorded as aligned-with rather than based-on: the sources establish that Statbel publishes a DCAT catalogue, not that it conforms to the Belgian federal DCAT profile specifically."
    confidence: low
    valid_from: null
    valid_until: null

  - type: part-of
    target: EU-ESS
    source: fact
    evidence: "The European Statistical System is the partnership between the Community statistical authority, which is the Commission (Eurostat), and the national statistical institutes and other national authorities responsible in each member state for the development, production and dissemination of European statistics; the ESS Committee is composed of NSI representatives and chaired by Eurostat (ec.europa.eu/eurostat/web/european-statistical-system; EUR-Lex CELEX 32009R0223; cso.ie European Statistical System page). Statbel is the Belgian NSI. Corroborated by reading Wikipedia's Statistics Belgium page directly (2026-08-26), which independently states Statbel 'serves as Belgium's official representative to Eurostat and the OECD'. Further corroborated by reading ec.europa.eu's own Eurostat news page directly (2026-08-27): Belgium's statistical system underwent an ESS peer review in December 2021, one of '31 ESS members' whose reports were published on Eurostat's own website — Statbel's participation in that peer-review cycle is itself evidence of ESS membership. This relationship was added in the UN batch (2026-08-16) correcting this entity's own earlier body text, which wrongly claimed no such link existed; see below."
    confidence: high
    valid_from: null
    valid_until: null
sources:
  - title: "Open Data | Statbel"
    url: "https://statbel.fgov.be/nl/open-data?category=214"
    publisher: "Statbel (Algemene Directie Statistiek)"
  - title: "DCAT catalogue for Statbel's open data"
    url: "https://statbel.fgov.be/en/open-data/dcat-catalogue-statbels-open-data"
    publisher: "Statbel (Algemene Directie Statistiek)"
  - title: "De Algemene Directie Statistiek van de FOD Economie gaat voor Open Data"
    url: "https://news.belgium.be/nl/de-algemene-directie-statistiek-van-de-fod-economie-gaat-voor-open-data"
    publisher: "news.belgium.be (Belgian federal government)"
  - title: "Statistics Belgium"
    url: "https://en.wikipedia.org/wiki/Statistics_Belgium"
    publisher: "Wikipedia"
    accessed: "2026-08-26"
  - title: "Wet van 4 juli 1962 betreffende de openbare statistiek"
    url: "https://etaamb.openjustice.be/nl/wet-van-04-juli-1962_n2006001011.html"
    publisher: "etaamb / OpenJustice"
    accessed: "2026-08-27"
  - title: "Algemene Directie Statistiek - Statistics Belgium"
    url: "https://nl.wikipedia.org/wiki/Algemene_Directie_Statistiek_-_Statistics_Belgium"
    publisher: "Wikipedia (NL)"
    accessed: "2026-08-27"
  - title: "Peer review report on Belgium now online"
    url: "https://ec.europa.eu/eurostat/web/products-eurostat-news/-/cn-20220518-1"
    publisher: "Eurostat — European Commission"
    accessed: "2026-08-27"
---

# Statbel (Algemene Directie Statistiek)

> **Verified 2026-08-27.** `statbel.fgov.be` (both cited pages, plus a
> PDF asset tried this pass) and `news.belgium.be` all still return
> CAPTCHA/403 challenges. But three previously-uncited pages were found
> via search and read directly this pass — etaamb.openjustice.be's own
> text of the 1962 public-statistics law, the Dutch Wikipedia article,
> and Eurostat's own news page on Belgium's ESS peer review — closing
> the "no statutory basis found" gap and adding a second independent
> corroboration of the `part-of` [[EU-ESS]] edge. Four of seven cited
> pages are now read directly, a genuine majority.

## Description

Statbel is Belgium's national statistical office — the Algemene Directie
Statistiek within the FOD Economie. Confirmed by reading Wikipedia's
Statistics Belgium page directly: it is part of the "Federal Public Service
Economy, SMEs, Self-Employed and Energy," and "serves as Belgium's official
representative to Eurostat and the OECD" — a detail not previously recorded
in this entity's prose (the frontmatter relationship already existed; see
the correction below).

Its open data portal opened on **22 October 2015**, carrying datasets on
population, income, land use and other subjects in freely reusable formats
under a **Creative Commons Attribution 4.0** licence. It maintains a
**DCAT catalogue** of that open data. Neither claim was re-confirmed this
pass — both `statbel.fgov.be` pages returned CAPTCHA challenges.

`coverage: medium`, up from `low`: a Belgian equivalent of [[DE-BSTATG]]
and [[NL-WET-CBS]] is now identified. Confirmed by reading
etaamb.openjustice.be's own text of the **Wet van 4 juli 1962 betreffende
de openbare statistiek** (public statistics act) directly: it establishes
the National Statistical Institute (predecessor name of today's Statbel),
a Coordination Committee for statistical programmes, a Statistical
Control Committee for data-protection oversight, and a High Council for
Statistics as advisory body. No `governed-by` edge is asserted to it,
because the 1962 act is not yet its own Atlas entity — creating one is a
follow-up, logged in `discovery/unresolved.md`, rather than something to
do inside this pass.

Confirmed by reading the Dutch Wikipedia article on Statbel directly: the
organisation's name changed twice after the 1962 act — from "Nationaal
Instituut voor de Statistiek" to "Algemene Directie Statistiek en
Economische Informatie" on 20 November 2003 (retroactive to 1 January
2003), then to "Algemene Directie Statistiek - Statistics Belgium" on 27
March 2014 — before adopting "Statbel" for external communication from 1
January 2018. The old acronym "NIS" still surfaces in some contexts, such
as the "NIS-code" geographic identifier.

## A stale claim in this entity's own prose, corrected

This section previously said, of the statistics cluster: *"no source read
connects Statbel to Eurostat, to the European Statistical System or to the
UN statistical system either. Three national statistical offices now sit
in the Atlas and none of them connects upward."*

That was already wrong when re-verification began this pass: the
frontmatter has carried `part-of` → [[EU-ESS]] since the UN-connection
batch of **2026-08-16**, ten days before this prose was still claiming the
opposite. `discovery/unresolved.md` records the correction under "Belgium
batch — third country," flagged with a warning that the claim "was wrong
when written and was repeated for three batches." This entity's own body
text was the place that repetition survived until now — a second instance
of frontmatter and body drifting apart, distinct from but the same class of
error as the one found and fixed on [[BE-APD]] this pass.

The corrected picture: two of three national statistical offices in the
Atlas connect upward — [[NL-CBS]] and now **Statbel**, both `part-of`
[[EU-ESS]] — and [[DE-DESTATIS]] does not, because its own sources name
only "the European Union," not Eurostat by name. The **UN** half of the
original claim still stands: no source read connects Statbel, or any
national statistical office in the Atlas, to the UN statistical system.

## Relationships

- `part-of` [[EU-ESS]] — recorded since the UN batch; corroborated by
  Wikipedia's "official representative to Eurostat" statement and, this
  pass, by Eurostat's own ESS peer-review news page; `confidence: high`.
- `aligned-with` [[BE-DCAT-AP-BE]] — at `confidence: low`. What is sourced
  is that Statbel publishes *a* DCAT catalogue; that it conforms to the
  Belgian federal profile is the obvious reading and is not stated. The
  weaker relationship type and the low confidence carry that distinction.
  Not confirmed this pass either (statbel.fgov.be still bot-walled).

## Sources

Four of seven read directly this pass: the English Wikipedia article
(prior pass), plus three found this pass — the Dutch Wikipedia article,
etaamb.openjustice.be's own text of the 1962 public-statistics act, and
Eurostat's own news page. Both `statbel.fgov.be` pages, the PDF asset
tried this pass, and `news.belgium.be` all returned CAPTCHA/403
challenges, the same pattern found across `bosa.belgium.be`,
`ccb.belgium.be`, `data.gov.be` and `financien.belgium.be` in this batch.
