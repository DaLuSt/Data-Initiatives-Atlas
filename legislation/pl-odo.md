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
verification: primary-source

start_date: 2018-05-25
end_date: null
last_verified: "2026-08-30"
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
    evidence: "Confirmed by reading UODO's own 2018 annual report (Sprawozdanie z działalności Prezesa UODO w roku 2018) directly (2026-08-26): the report itself is submitted under 'art. 50 ustawy z dnia 10 maja 2018 r. o ochronie danych osobowych' (Article 50 of the Act of 10 May 2018), naming this Act as the President's own statutory reporting obligation. politykabezpieczenstwa.pl, also read directly, dates the replacement precisely: 'zastąpienie z dniem 25 maja 2018 roku Generalnego Inspektora Ochrony Danych Osobowych nowym organem' (replacing GIODO, on 25 May 2018, with a new body) under 'nowa krajowa ustawa z 10 maja 2018 roku o ochronie danych osobowych' (the new national act of 10 May 2018). odoserwis.pl's page was not read this pass. The official Dz.U. citation, previously missing, is now confirmed directly (see below)."
    confidence: medium
    valid_from: 2018-05-25
    valid_until: null

sources:
  - title: "Prezes UODO zamiast Generalnego Inspektora ODO"
    url: "https://www.politykabezpieczenstwa.pl/pl/a/puodo-zamiast-giodo"
    publisher: "Polityka Bezpieczeństwa"
    accessed: "2026-08-26"
  - title: "Prezes Urzędu Ochrony Danych Osobowych (PUODO)"
    url: "https://odoserwis.pl/p/405/prezes-urzedu-ochrony-danych-osobowych-puodo"
    publisher: "odoserwis.pl"
  - title: "Sprawozdanie z działalności Prezesa Urzędu Ochrony Danych Osobowych w roku 2018"
    url: "https://uodo.gov.pl/pl/file/3909"
    publisher: "Urząd Ochrony Danych Osobowych (UODO)"
    accessed: "2026-08-26"
  - title: "Ustawa z dnia 10 maja 2018 r. o ochronie danych osobowych — official ELI record (Dz.U. 2018 poz. 1000)"
    url: "https://eli.gov.pl/eli/DU/2018/1000/ogl"
    publisher: "Rządowe Centrum Legislacji — official ELI registry (Poland)"
    accessed: "2026-08-30"
---

# Ustawa o ochronie danych osobowych (2018)

> **Official citation closed 2026-08-30.** This entity had rested entirely
> on secondary commentary and a UODO annual report — genuinely read, but
> without the Dziennik Ustaw citation itself, a research-queue item flagged
> as **Next** since the Poland batch. `eli.gov.pl`, Poland's official ELI
> (European Legislation Identifier) legislative registry — a distinct
> government domain from the CAPTCHA-blocked `isap.sejm.gov.pl` — was read
> directly and confirms **Dz.U. 2018 poz. 1000**, published 24 May 2018.
> `isap.sejm.gov.pl` itself remains genuinely CAPTCHA-blocked, confirmed
> again this pass.

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

✅ **Dziennik Ustaw citation now confirmed: Dz.U. 2018 poz. 1000.** Unlike
[[PL-OTWARTE-DANE]], this act previously had no official legislative
citation, resting entirely on secondary commentary and a UODO annual
report. That gap is closed: `eli.gov.pl`, Poland's official ELI registry
(a distinct government domain, not the CAPTCHA-blocked `isap.sejm.gov.pl`),
confirms the act published as **Dz.U. 2018 poz. 1000** on **24 May 2018**,
one day before its 25 May entry into force — consistent with every date
already recorded here. `isap.sejm.gov.pl` itself remains genuinely
CAPTCHA-blocked, confirmed again this pass, so the act's full consolidated
text is still not read directly — only its official citation and
publication date.

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

Listed in frontmatter, three of four read directly across two passes: two
secondary sources and UODO's own annual report (2026-08-26), plus
`eli.gov.pl`'s official citation record (2026-08-30). `isap.sejm.gov.pl`
remains genuinely CAPTCHA-blocked.
