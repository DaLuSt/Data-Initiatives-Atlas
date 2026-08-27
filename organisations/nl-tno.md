---
id: NL-TNO
type: organisation
name: Nederlandse Organisatie voor toegepast-natuurwetenschappelijk onderzoek
alternative_names:
  - TNO
  - Netherlands Organisation for Applied Scientific Research
description: >
  Dutch independent applied research organisation, originally established
  by the TNO-wet of 30 October 1930 (in force 1 May 1932). Its current
  constituting statute is the TNO-wet of 19 December 1985 (in force 1 May
  1986), which replaced the 1930 act. TNO conducts applied research on
  societally significant topics and hosts the Geological Survey of the
  Netherlands.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 1932-05-01
end_date: null
last_verified: "2026-08-27"
previous_version: null
successor: null

domains:
  - DOMAIN-RESEARCH
organisations: []
related_entities:
  - NL-GEONOVUM
  - NL-TNO-WET
relationships:
  - type: governed-by
    target: NL-TNO-WET
    source: fact
    evidence: "Corrected this pass (2026-08-27): reading wetten.overheid.nl's own TNO-wet text directly (BWBR0003906) shows the statute currently governing TNO is the act of 19 December 1985, in force 1 May 1986 — NOT the 1930/1932 act this relationship previously cited alone. The 1985 act replaced the 1930 one. TNO's own organisational continuity traces to the 1930 founding (organisaties.overheid.nl lists TNO as active '01-01-1931 to present'; nl.wikipedia.org, read directly, confirms the 1930 act's 1 May 1932 commencement and traces TNO's establishment to the Lorentz Commission of 1918 and the Went Commission of 1923), but the currently operative constituting statute — what [[NL-TNO-WET]] now represents — is the 1985/1986 recasting."
    confidence: high
    valid_from: 1932-05-01
    valid_until: null

sources:
  - title: "Contactgegevens Nederlandse organisatie voor toegepast-natuurwetenschappelijk onderzoek"
    url: "https://organisaties.overheid.nl/28212147/Nederlandse_organisatie_voor_toegepast-natuurwetenschappelijk_onderzoek"
    publisher: "Overheid.nl"
    accessed: "2026-08-27"
  - title: "Nederlandse Organisatie voor toegepast-natuurwetenschappelijk onderzoek"
    url: "https://nl.wikipedia.org/wiki/Nederlandse_Organisatie_voor_toegepast-natuurwetenschappelijk_onderzoek"
    publisher: "Wikipedia"
    accessed: "2026-08-27"
  - title: "Nederlandse organisatie voor toegepast-natuurwetenschappelijk onderzoek — trefwoord"
    url: "https://www.eerstekamer.nl/trefwoord/nederlandse_organisatie_voor"
    publisher: "Eerste Kamer der Staten-Generaal"
    accessed: "2026-08-27"
---

# TNO

> **Verified 2026-08-27 — includes a factual correction.** All three cited
> pages were read directly this pass, closing the previous `search-only`
> status (never previously `last_verified`). Reading `wetten.overheid.nl`'s
> own TNO-wet text on the sibling [[NL-TNO-WET]] entity found that the
> statute **currently** governing TNO is not the 1930 act this entity's
> `governed-by` relationship implied, but a 1985 act (in force 1986) that
> replaced it — corrected below and on [[NL-TNO-WET]].

## Description

TNO is an independent Dutch applied research organisation. Reading
nl.wikipedia.org's own article directly traces its origin to the **Lorentz
Commission (1918)** and a subsequent commission led by **Frits Went
(1923)**, both recommending a central applied-research organisation; the
government adopted this in the **Wet van 30 oktober 1930**, in force **1
May 1932**, with TNO's first board installed 10 May 1932. `organisaties.
overheid.nl`, also read directly, independently lists TNO as active from
"01-01-1931" (a related administrative date, likely the year the founding
act was passed, rather than a conflicting commencement date) and confirms
TNO's status as a "Zelfstandig bestuursorgaan" with its own legal
personality, publicly noting the Kaderwet zelfstandige bestuursorganen does
not apply to it for lack of public-authority powers.

**That 1930/1932 act is no longer the statute in force.** It was replaced
by the **Wet van 19 december 1985** (in force 1 May 1986) — see
[[NL-TNO-WET]], corrected this pass to represent the currently-operative
statute rather than the 1930 one. TNO's organisational continuity is
unbroken across that recasting; `start_date` here still records the
**1932** commencement of TNO's original founding act, since the
organisation itself has existed continuously since then, while
[[NL-TNO-WET]]'s own `start_date` now correctly records **1986**, the
commencement of the statute currently in force.

Within the Atlas's scope, TNO enters chiefly as a research organisation
with a data role: the **Geological Survey of the Netherlands** sits within
TNO — confirmed directly via nl.wikipedia.org, which states TNO "vervult
een rol als innovator namens... de Geologische Dienst Nederland" among
other delegated government roles — and is one of the funders of
[[NL-GEONOVUM]]'s base programme, connecting TNO to Dutch
geo-standardisation.

`coverage: low`: TNO is a large organisation whose activities extend well
beyond the Atlas's scope, and only its data/digital-relevant aspects have
been researched.

## Relationships

- `governed-by` [[NL-TNO-WET]] — now correctly pointing at the 1985/1986
  statute currently in force, not the 1930/1932 one.
- Co-funder of [[NL-GEONOVUM]] through the Geological Survey of the
  Netherlands.

## Sources

All three read directly this pass: `organisaties.overheid.nl`, the Dutch
Wikipedia article, and the Eerste Kamer keyword page (which lists related
dossiers — a 1998 TNO-wet amendment bill and a 2000 science-budget bill —
without itself giving the 1930/1985 history, which came from the Wikipedia
article and from `wetten.overheid.nl`, read directly on [[NL-TNO-WET]]).
