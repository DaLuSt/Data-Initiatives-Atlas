---
id: PL-PESEL
type: platform
name: PESEL
alternative_names:
  - Powszechny Elektroniczny System Ewidencji Ludności
  - Universal Electronic System for Registration of the Population
description: >
  Poland's central population register and the eleven-digit
  identification number it assigns to every person registered in it —
  the direct counterpart of the Dutch Basisregistratie Personen. The
  number is assigned by the minister responsible for informatisation,
  encodes date of birth and sex, and is required of permanent residents
  and of temporary residents living in Poland for more than two months.
  Since 1 March 2015 it has operated as part of the System Rejestrów
  Państwowych (State Registers System), run by the Centralny Ośrodek
  Informatyki, which also integrates Poland's identity-card and
  civil-status records.

level: national
country: PL
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: 1977-01-01
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - PL-COI
related_entities:
  - PL-EWIDENCJA-LUDNOSCI
  - PL-COI
  - PL-MC
  - NL-BRP
relationships:
  - type: governed-by
    target: PL-EWIDENCJA-LUDNOSCI
    source: fact
    evidence: "Confirmed verbatim by reading gov.pl's own 'Czym jest numer PESEL' page directly (2026-08-22): its 'Podstawa prawna' section cites 'Ustawa z dnia 24 września 2010 r. o ewidencji ludności (Dz. U. z 2015 r. poz. 388)' as the legal basis for the PESEL number, alongside a 2012 ministerial regulation on assigning and changing it. Corroborated on pl.wikipedia.org/wiki/PESEL: 'Od 1 marca 2015 podstawę prawną funkcjonowania systemu stanowi ustawa o ewidencji ludności z 24 września 2010.'"
    confidence: medium
    valid_from: 2015-03-01
    valid_until: null
  - type: maintained-by
    target: PL-COI
    source: fact
    evidence: "Confirmed by reading pl.wikipedia.org/wiki/PESEL directly (2026-08-22): '1 marca 2015 weszły w życie trzy nowe ustawy ... Tego dnia w celu wykonania powyższych ustaw uruchomiony został System Rejestrów Państwowych (SRP) obsługiwany przez Centralny Ośrodek Informatyki, w ramach którego połączone zostały: rejestry PESEL, ewidencja dowodów osobistych i akta stanu cywilnego' — the State Registers System, operated by the Central IT Centre, was launched the same day (1 March 2015), integrating the PESEL register, identity-card records and civil-status records. This corroborates PL-COI's own page, already listing the PESEL register among the systems it maintains, with a specific date and mechanism neither source gave alone."
    confidence: medium
    valid_from: 2015-03-01
    valid_until: null

sources:
  - title: "Czym jest numer PESEL"
    url: "https://www.gov.pl/web/gov/czym-jest-numer-pesel"
    publisher: "Portal Gov.pl"
    accessed: "2026-08-22"
  - title: "PESEL"
    url: "https://pl.wikipedia.org/wiki/PESEL"
    publisher: "Wikipedia (polski)"
    accessed: "2026-08-22"
  - title: "PESEL"
    url: "https://en.wikipedia.org/wiki/PESEL"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
---

# PESEL

> **Verified 2026-08-22.** Closes the research-queue item carried since
> the Poland batch: "PESEL, Poland's population register, the direct
> counterpart of [[NL-BRP]] ... Named in [[PL-COI]]'s list of systems and
> nothing more." Sourced from gov.pl's own page and two Wikipedia
> articles, all read directly. `isap.sejm.gov.pl` returns an Incapsula
> JavaScript challenge to every fetch regardless of User-Agent and
> remains unread — see [[PL-EWIDENCJA-LUDNOSCI]] for what that costs this
> entity's legal citation.

## Description

Confirmed by reading gov.pl's own "Czym jest numer PESEL" page directly
(2026-08-22): "Numer PESEL to jedenastocyfrowy symbol numeryczny, który
pozwala na łatwą identyfikację osoby, która go posiada. Numer PESEL
zawiera datę urodzenia, numer porządkowy, oznaczenie płci oraz liczbę
kontrolną" — the PESEL number is an eleven-digit numeric symbol that
identifies a person, encoding date of birth, a sequence number, sex and
a check digit. "Numer PESEL nadaje Minister właściwy do spraw
informatyzacji" — it is assigned by the minister responsible for
informatisation, currently [[PL-MC]].

Confirmed by reading en.wikipedia.org/wiki/PESEL directly: "The PESEL
number is mandatory for all permanent residents of Poland and for
temporary residents living in Poland for over 2 months."

## A history the sources do not fully agree on

Confirmed by reading pl.wikipedia.org/wiki/PESEL directly (2026-08-22):
the system was launched in 1977 as a pilot covering the Wola district of
Warsaw, then extended across Warsaw and its voivodeship, with PESEL
numbers assigned to all Polish citizens by 1984: "System PESEL został
uruchomiony w 1977 ... Numery PESEL dla wszystkich obywateli Polski
zostały nadane do 1984." Its name — Powszechny Elektroniczny System
Ewidencji Ludności — was set by a June 1970 Government Presidium
decision, and the system was a direct successor to MAGISTER, an earlier
1973–74 register of university-educated citizens.

This does not fully match en.wikipedia.org/wiki/PESEL, read the same
pass, which states the number has been "used in Poland since 1979"
without giving a launch mechanism. Both claims are retained rather than
reconciled: the Polish article is more specific and internally
consistent (pilot 1977, full rollout 1984), so `start_date` follows it,
but the discrepancy is not resolved.

## Origins under a different government, for a different purpose

Confirmed by reading pl.wikipedia.org/wiki/PESEL and en.wikipedia.org/wiki/PESEL
directly (2026-08-22): the system was designed by the communist
government of the Polish People's Republic to trace personal information
about citizens, addressing a problem of fragmented population records
inherited from documents left over from the Prussian, Russian and
Austrian partitions and further scattered by two world wars. That
origin, and the purpose it served, are unlike any other national
identifier the Atlas records.

## Who runs it today, and since when

[[PL-COI]]'s own entity already named the PESEL register among the
systems it maintains, without a date or mechanism. This pass supplies
both: the **State Registers System** (System Rejestrów Państwowych),
launched **1 March 2015** to give effect to [[PL-EWIDENCJA-LUDNOSCI]] and
its two companion acts, is "obsługiwany przez Centralny Ośrodek
Informatyki" — operated by COI — and integrates the PESEL register with
identity-card and civil-status records.

## Not modelled

- The **System Rejestrów Państwowych** as its own entity, distinct from
  [[PL-COI]], the body that operates it.
- **MAGISTER**, the 1973–74 predecessor register of university-educated
  citizens, and the **Departament PESEL MSW**, the historical department
  named on Polish Wikipedia.
- The **specific data fields** the register holds (name, parents' names
  and PESEL numbers, place and country of birth, marital status, and
  more) and the rules for assigning PESEL numbers to foreign nationals —
  both catalogued on pl.wikipedia.org/wiki/PESEL and nowhere in this
  entity.
- The **check-digit algorithm** and the century-encoding scheme for the
  birth-month field — mechanical detail, not an Atlas relationship.

## Relationships

- `governed-by` [[PL-EWIDENCJA-LUDNOSCI]].
- `maintained-by` [[PL-COI]], with a date (1 March 2015) and mechanism
  (the State Registers System) neither source gave on its own.

## Sources

Listed in frontmatter. All three pages were read directly this pass;
`isap.sejm.gov.pl` remains genuinely unreadable.
