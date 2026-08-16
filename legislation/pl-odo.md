---
id: PL-ODO
type: law
name: Ustawa z dnia 10 maja 2018 r. o ochronie danych osobowych
alternative_names:
  - Ustawa o ochronie danych osobowych
  - Polish Personal Data Protection Act 2018
description: >
  Polish act of 10 May 2018 on the protection of personal data, adopted to
  give effect to the GDPR in Polish law. It regulates the status, tasks,
  competencies, principles and appointment procedure of the President of the
  Office for Personal Data Protection, who has been the competent body for
  personal data protection in Poland since 25 May 2018 and who replaced the
  Generalny Inspektor Ochrony Danych Osobowych.

level: national
country: PL
region: EU

status: active
confidence: medium
coverage: low
verification: search-only

start_date: 2018-05-25
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - PL-UODO
related_entities:
  - EU-GDPR
  - NL-UAVG
  - DE-BDSG
  - BE-GDPR-WET
  - FR-LIL
  - ES-LOPDGDD
relationships:
  - type: implements-requirement-from
    target: EU-GDPR
    source: fact
    evidence: "As of 25 May 2018 the competent body for the protection of personal data in Poland is the President of the Office for Personal Data Protection, whose status, tasks, competencies, principles and mode of appointment are regulated by the Act of 10 May 2018 on the protection of personal data; the President replaced the Generalny Inspektor Ochrony Danych Osobowych on the date the GDPR became applicable (uodo.gov.pl; politykabezpieczenstwa.pl 'Prezes UODO zamiast Generalnego Inspektora ODO'; odoserwis.pl). NOT READ — search-only. CAVEAT: the sources establish the Act's role in constituting the supervisory authority; the Atlas has not established the Act's substantive GDPR-specification provisions."
    confidence: medium
    valid_from: 2018-05-25
    valid_until: null

sources:
  - title: "Prezes UODO zamiast Generalnego Inspektora ODO"
    url: "https://www.politykabezpieczenstwa.pl/pl/a/puodo-zamiast-giodo"
    publisher: "Polityka Bezpieczeństwa"
  - title: "Prezes Urzędu Ochrony Danych Osobowych (PUODO)"
    url: "https://odoserwis.pl/p/405/prezes-urzedu-ochrony-danych-osobowych-puodo"
    publisher: "odoserwis.pl"
  - title: "Sprawozdanie z działalności Prezesa Urzędu Ochrony Danych Osobowych w roku 2018"
    url: "https://uodo.gov.pl/pl/file/3909"
    publisher: "Urząd Ochrony Danych Osobowych (UODO)"
---

# Ustawa o ochronie danych osobowych (2018)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The Act of **10 May 2018** gives effect to [[EU-GDPR]] in Polish law. It
regulates the status, tasks, competencies and appointment of the President
of the Office for Personal Data Protection — see [[PL-UODO]] — who became
the competent body on **25 May 2018**, the day the GDPR became applicable.

## The GDPR technique table, sixth entry

| Country | Instrument | Technique |
|---|---|---|
| France | [[FR-LIL]] | **amended a 1978 act in place** |
| Netherlands | [[NL-UAVG]] | new implementing act |
| Germany | [[DE-BDSG]] | new act, replacing the earlier one |
| Belgium | [[BE-GDPR-WET]] | new act, repealing the 1992 privacy law |
| Spain | [[ES-LOPDGDD]] | new organic law, carrying digital rights beyond data protection |
| **Poland** | **this act** | **new act, timed to the GDPR's application date** |

Six countries, and France remains the only one that amended rather than
enacted.

What is distinctive here is **the date**. The Polish act was passed on
10 May 2018 and its supervisory authority took office on **25 May 2018** —
the GDPR's own application date, to the day. None of the other five aligns
that precisely; Belgium's law is dated 30 July 2018 and in force from
5 September, and Spain's did not arrive until December.

## `coverage: low`, and the reason is specific

Every source found for this act describes it **through the authority it
creates**. What the Act says about the roughly fifty discretionary options
the GDPR leaves to member states — the substance that makes national GDPR
acts differ — was not established at all.

The `implements-requirement-from` edge therefore carries an explicit caveat
in its own `evidence` string: the sources support the Act's role in
constituting the supervisory body, not its substantive specification of the
GDPR. That distinction matters, because it is the difference between "this
is Poland's GDPR act" (asserted) and "this is what Poland did with the
GDPR's opening clauses" (unknown).

⚠ **No ISAP or Dziennik Ustaw citation.** Unlike [[PL-OTWARTE-DANE]], which
has one, this act rests entirely on secondary commentary and a UODO annual
report. It is the weakest-sourced of the six national GDPR instruments and
the first thing a re-verification pass should fetch for Poland.

## A naming collision worth flagging

Polish usage overloads the abbreviation **UODO**: it denotes both the
*Urząd* (the office, [[PL-UODO]]) and, in some writing, the *ustawa o
ochronie danych osobowych* (this act). The Atlas separates them —
`PL-UODO` for the authority, `PL-ODO` for the act — and neither ID may be
reused for the other.

## Relationships

- `implements-requirement-from` [[EU-GDPR]] — with the caveat above.

[[PL-UODO]] carries the `applies-to` edge pointing here.

## Sources

Listed in frontmatter.
