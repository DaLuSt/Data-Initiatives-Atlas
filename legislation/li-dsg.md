---
id: LI-DSG
type: law
name: Datenschutzgesetz (Liechtenstein)
alternative_names:
  - DSG
  - Liechtenstein Data Protection Act
description: >
  Liechtenstein's data protection act of 4 October 2018, in force since
  1 January 2019. The General Data Protection Regulation became directly
  applicable in Liechtenstein through the EEA Agreement on 20 July 2018,
  following its incorporation by Decision of the EEA Joint Committee
  No 154/2018; the DSG supplements it by exercising the national opening
  clauses, in areas including employment data, journalistic expression,
  video surveillance, national identification numbers and criminal-conviction
  data. It designates the Datenschutzstelle as the supervisory authority, and
  is modelled on the German Federal Data Protection Act rather than on Swiss
  law.

level: national
country: LI
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2019-01-01
end_date: null
last_verified: "2026-08-21"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - LI-DATENSCHUTZSTELLE
related_entities:
  - EU-GDPR
  - INTL-EEA-JCD-154-2018
  - LI-DATENSCHUTZSTELLE
  - DE-BDSG
relationships:
  - type: implements-requirement-from
    target: EU-GDPR
    source: fact
    evidence: "The Datenschutzgesetz (DSG) is Liechtenstein's national Data Protection Act, enacted 4 October 2018 and in force since 1 January 2019; the GDPR applies in Liechtenstein through the EEA Agreement and became directly applicable on 20 July 2018, and the DSG supplements the GDPR by exercising national opening clauses in areas such as employment data, journalistic expression, video surveillance, national ID numbers and criminal data (datenschutzstelle.li 'Nationale Gesetze'; gdprhub.eu 'Data Protection in Liechtenstein'; naegele.law 'Liechtenstein & the GDPR'). NOT READ — search-only."
    confidence: medium
    valid_from: 2019-01-01
    valid_until: null
  - type: references
    target: INTL-EEA-JCD-154-2018
    source: fact
    evidence: "The GDPR applies in Liechtenstein through the EEA Agreement and became directly applicable on 20 July 2018, the route being its incorporation into Annex XI by Decision of the EEA Joint Committee No 154/2018 of 6 July 2018 (eur-lex.europa.eu ELI dec/2018/1022/oj; gdprhub.eu 'Data Protection in Liechtenstein'). NOT READ — search-only."
    confidence: medium
    valid_from: 2018-07-20
    valid_until: null

sources:
  - title: "Nationale Gesetze — Datenschutzstelle Liechtenstein"
    url: "https://www.datenschutzstelle.li/rechtsgrundlagen/nationale-gesetze"
    publisher: "Datenschutzstelle Liechtenstein"
  - title: "Data Protection in Liechtenstein"
    url: "https://gdprhub.eu/index.php?title=Data_Protection_in_Liechtenstein"
    publisher: "GDPRhub — noyb"
  - title: "Liechtenstein & the GDPR"
    url: "https://www.naegele.law/archiv/liechtenstein-the-gdpr"
    publisher: "NÄGELE Rechtsanwälte GmbH"
  - title: "Decision of the EEA Joint Committee No 154/2018 of 6 July 2018"
    url: "https://eur-lex.europa.eu/eli/dec/2018/1022/oj"
    publisher: "EUR-Lex — Publications Office of the European Union"
---

# Datenschutzgesetz (Liechtenstein)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read — retrieval is blocked by
> the network egress proxy. `verification: search-only`.

## Description

Liechtenstein's data protection act, enacted **4 October 2018** and in force
since **1 January 2019**. It designates [[LI-DATENSCHUTZSTELLE]] as the
supervisory authority.

Its function is **supplementary, not transposing**. [[EU-GDPR]] became
directly applicable in Liechtenstein on **20 July 2018** through the EEA
Agreement; the DSG exercises the GDPR's **national opening clauses** in
areas the regulation leaves to member-state law:

- employment data
- journalistic expression
- video surveillance
- national identification numbers
- criminal-conviction data

The sources also note that it is **modelled on the German
Bundesdatenschutzgesetz** rather than on Swiss law — which, for a state in
customs and currency union with Switzerland, is a choice worth recording.

## The case that breaks the pattern in an informative way

The three EEA EFTA states all reached the GDPR through
[[INTL-EEA-JCD-154-2018]]. Two of them then passed acts that *give the GDPR
effect*. Liechtenstein did not need to:

| | Norway | Iceland | Liechtenstein |
|---|---|---|---|
| National act's function | gives GDPR effect | gives GDPR effect | **supplements** an already-applicable GDPR |
| GDPR applicable from | 20 July 2018 | 15 July 2018 | **20 July 2018, directly** |
| National act in force | 20 July 2018 | 15 July 2018 | **1 January 2019** — five months later |

The five-month gap is the tell. Norway's and Iceland's acts had to be in
force on the day the GDPR started to apply, because **their acts were what
made it apply**. Liechtenstein's did not, because the regulation was already
applicable and the DSG only fills in what the regulation leaves open.

This is why [[IS-PERSONUVERNDARLOG]] can say the Norwegian pattern
generalises and this entity can still be different: the *route* is identical
in all three, and the *national instrument's job* is not.

## What is not asserted

The sources describe the DSG as modelled on the German BDSG. **No
`based-on` edge to [[DE-BDSG]] is asserted.** "Modelled after" in a law-firm
commentary is a characterisation of legislative style, not a sourced statement
that the Liechtenstein legislature adapted a specific text — which is what
`based-on` claims. It is recorded here in prose and left in
`discovery/unresolved.md` for a source that says more.

## Relationships

- `implements-requirement-from` [[EU-GDPR]]. This is the closest available
  type and it slightly overstates: the DSG supplements rather than transposes.
  The distinction is stated above and in the evidence string, and no better
  type exists — a `supplements` type would have exactly one instance.
- `references` [[INTL-EEA-JCD-154-2018]].

## Sources

Listed in frontmatter — the Datenschutzstelle's own register of national
laws, GDPRhub, a Liechtenstein law firm's account, and the EUR-Lex record of
the Joint Committee decision.
