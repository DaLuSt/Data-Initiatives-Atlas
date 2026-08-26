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
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-26"
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
    evidence: "Statbel publishes a DCAT catalogue for its open data (statbel.fgov.be 'DCAT catalogue for Statbel's open data'). Not re-confirmed this pass — statbel.fgov.be returned a CAPTCHA challenge rather than content. Recorded as aligned-with rather than based-on: the sources establish that Statbel publishes a DCAT catalogue, not that it conforms to the Belgian federal DCAT profile specifically."
    confidence: low
    valid_from: null
    valid_until: null

  - type: part-of
    target: EU-ESS
    source: fact
    evidence: "The European Statistical System is the partnership between the Community statistical authority, which is the Commission (Eurostat), and the national statistical institutes and other national authorities responsible in each member state for the development, production and dissemination of European statistics; the ESS Committee is composed of NSI representatives and chaired by Eurostat (ec.europa.eu/eurostat/web/european-statistical-system; EUR-Lex CELEX 32009R0223; cso.ie European Statistical System page). Statbel is the Belgian NSI. Corroborated this pass by reading Wikipedia's Statistics Belgium page directly (2026-08-26), which independently states Statbel 'serves as Belgium's official representative to Eurostat and the OECD' — this relationship was added in the UN batch (2026-08-16) correcting this entity's own earlier body text, which wrongly claimed no such link existed; see below."
    confidence: medium
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
---

# Statbel (Algemene Directie Statistiek)

> **Re-checked 2026-08-26, still `search-only`.** `statbel.fgov.be` (both
> cited pages) and `news.belgium.be` all returned CAPTCHA/403 challenges
> rather than content. Only Wikipedia was read directly, which corroborates
> the already-recorded `part-of` [[EU-ESS]] edge with a new detail. One of
> four is not a majority, so this entity stays `search-only` despite the
> correction made to its own body text below.

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

`coverage: low`: unlike [[DE-DESTATIS]] and [[NL-CBS]], no statutory basis
for Statbel was established — no Belgian equivalent of [[DE-BSTATG]] or
[[NL-WET-CBS]] was found by search, so none is recorded and no
`governed-by` relationship is asserted.

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

- `part-of` [[EU-ESS]] — recorded since the UN batch; corroborated this
  pass by Wikipedia's "official representative to Eurostat" statement.
- `aligned-with` [[BE-DCAT-AP-BE]] — at `confidence: low`. What is sourced
  is that Statbel publishes *a* DCAT catalogue; that it conforms to the
  Belgian federal profile is the obvious reading and is not stated. The
  weaker relationship type and the low confidence carry that distinction.
  Not re-confirmed this pass (statbel.fgov.be bot-walled).

## Sources

One of four read directly this pass — Wikipedia. Both `statbel.fgov.be`
pages and `news.belgium.be` returned CAPTCHA/403 challenges, the same
pattern found across `bosa.belgium.be`, `ccb.belgium.be`, `data.gov.be` and
`financien.belgium.be` in this batch.
