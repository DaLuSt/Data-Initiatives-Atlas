---
id: PL-KRI
type: framework
name: Krajowe Ramy Interoperacyjności
alternative_names:
  - KRI
  - National Interoperability Framework (Poland)
description: >
  Poland's national interoperability framework, established by
  Rozporządzenie Rady Ministrów (Regulation of the Council of Ministers)
  of 12 April 2012, an executive act issued under the 2005 law on
  informatising the activities of entities performing public tasks. It
  sets minimum requirements for public registers, electronic information
  exchange and public-sector IT systems across organisational, semantic
  and technical interoperability, including data-format and protocol
  specifications, information-security obligations, open file formats,
  WCAG accessibility compliance and annual security audits.

level: national
country: PL
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2012-04-12
end_date: null
last_verified: "2026-09-04"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - PL
  - PL-MC
relationships:
  - type: applies-in
    target: PL
    source: fact
    evidence: "Confirmed by reading gov.pl's own 'Krajowe Ramy Interoperacyjności obchodzą 10-lecie' (KRI turns 10) retrospective directly (2026-09-04): the regulation was signed 12 April 2012 by the Prime Minister as an executive act under the 2005 law on informatising public entities, and standardises how public institutions (offices, ministries, courts, hospitals) manage IT systems across organisational, semantic and technical interoperability. No connection to the European Interoperability Framework is stated in this or the companion gov.pl standards page, so none is asserted — the same restraint the Atlas already applies on ES-ENI, FR-RGI and DE. Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: 2012-04-12
    valid_until: null
  - type: maintained-by
    target: PL-MC
    source: fact
    evidence: "Confirmed by reading gov.pl's own 'Standardy Krajowych Ram Interoperacyjności' page directly (2026-09-04): it states 'Minister właściwy do spraw informatyzacji publikuje w repozytorium interoperacyjności' (the minister responsible for informatisation matters publishes to the interoperability repository) — the same statutory formula the mObywatel Act's own Article 19 uses for the ministry now called Ministerstwo Cyfryzacji, confirmed on PL-MOBYWATEL. The page does not name the ministry by its current title directly."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Krajowe Ramy Interoperacyjności obchodzą 10-lecie"
    url: "https://www.gov.pl/web/baza-wiedzy/krajowe-ramy-interoperacyjnosci-obchodza-10-lecie"
    publisher: "Portal Gov.pl"
    accessed: "2026-09-04"
  - title: "Standardy Krajowych Ram Interoperacyjności (KRI)"
    url: "https://www.gov.pl/web/ia/standardy-krajowych-ram-interoperacyjnosci-kri"
    publisher: "Portal Gov.pl — Portal Interoperacyjności i Architektury"
    accessed: "2026-09-04"
---

# Krajowe Ramy Interoperacyjności (KRI)

> **Added 2026-09-04, `verification: primary-source` from creation.**
> `discovery/research-queue.md` had flagged this as "Poland's national
> interoperability framework — the sixth national NIF, and the sixth
> potential [[EU-EIF]] descent." Both gov.pl pages were read directly
> this pass; neither states an EIF connection, so none is asserted,
> consistent with the Atlas's existing restraint on [[ES-ENI]] and
> [[FR-RGI]].

## Description

KRI is Poland's national interoperability framework, established by a
**Rozporządzenie Rady Ministrów** (Regulation of the Council of
Ministers) **signed 12 April 2012** — an executive act issued under the
**2005 law on informatising the activities of entities performing
public tasks**, confirmed by reading gov.pl's own ten-year retrospective
directly.

It sets minimum requirements across three layers — **organisational,
semantic and technical** — for public registers, electronic information
exchange and public-sector IT systems: unified data structures,
information-security measures, open file formats, **WCAG** digital
accessibility, and annual security audits.

## No sourced link to the European Interoperability Framework

Five other national interoperability frameworks in the Atlas ([[NL-NORA]],
[[BE-BELGIF]], [[FR-RGI]], [[ES-ENI]] and Germany's IT-Planungsrat
resolutions) have each been checked for a descent from [[EU-EIF]], and
the Atlas has refused the link everywhere it was not directly stated.
Neither gov.pl page read this pass mentions the EIF. KRI is the **sixth**
national interoperability instrument to reach the same result: no edge
asserted, for the same reason each time.

## An executive act, not primary legislation

KRI is a regulation (rozporządzenie) issued by the Council of Ministers
under a parent statute, not a law passed by the Sejm — the same
primary/secondary distinction the Atlas already flattens under `type:
law` for [[IE-PSI-REGULATIONS-2021]] and notes explicitly on [[IT-CAD]].
The 2005 parent act itself is not modelled.

## Relationships

- `applies-in` [[PL]] (anchor edge).
- `maintained-by` [[PL-MC]].

## Sources

Listed in frontmatter, both read directly this pass.
