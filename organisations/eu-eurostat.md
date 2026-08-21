---
id: EU-EUROSTAT
type: organisation
name: Eurostat
alternative_names:
  - Statistical Office of the European Union
description: >
  The statistical authority of the European Union. With the national
  statistical institutes of the member states it forms the European
  Statistical System, the partnership responsible for developing, producing
  and disseminating European statistics.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-21"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-CBS
relationships:
  - type: part-of
    target: EU-COMMISSION
    source: fact
    evidence: "The European Statistical System is the partnership between the Community statistical authority, which is the Commission (Eurostat), and the national statistical institutes (eurostat Statistics Explained; Reg. (EC) 223/2009). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: part-of
    target: EU-ESS
    source: fact
    evidence: "The European Statistical System is the partnership between the Community statistical authority, which is the Commission (Eurostat), and the national statistical institutes and other national authorities responsible in each member state for the development, production and dissemination of European statistics; the ESS Committee is chaired by Eurostat (ec.europa.eu/eurostat/web/european-statistical-system; EUR-Lex CELEX 32009R0223; cso.ie European Statistical System page). NOT READ — search-only."
    confidence: medium
    valid_from: 2009-03-11
    valid_until: null
  - type: participates-in
    target: UN-UNSC
    source: fact
    evidence: "Eurostat represents the EU in key international forums such as the United Nations Statistical Commission (UNSC), in the Conference of European Statisticians (CES) organised by the UNECE and in the OECD's committee on statistics and statistical policy (CSSP) (ec.europa.eu/eurostat Statistics Explained 'Statistical cooperation – introduction'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: UN-CES
    source: fact
    evidence: "Eurostat represents the EU in key international forums such as the United Nations Statistical Commission (UNSC), in the Conference of European Statisticians (CES) organised by the UNECE and in the OECD's committee on statistics and statistical policy (CSSP) (ec.europa.eu/eurostat Statistics Explained 'Statistical cooperation – introduction'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: INTL-OECD-CSSP
    source: fact
    evidence: "Eurostat represents the EU in key international forums such as the United Nations Statistical Commission (UNSC), in the Conference of European Statisticians (CES) organised by the UNECE and in the OECD's committee on statistics and statistical policy (CSSP); a parallel passage on the same page says Eurostat represents the European Commission in the OECD's statistics committee (CSTAT) (ec.europa.eu/eurostat Statistics Explained 'Statistical cooperation – introduction'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Eurostat and the European Statistical System — Statistics Explained"
    url: "https://ec.europa.eu/eurostat/statistics-explained/SEPDF/cache/10129.pdf"
    publisher: "Eurostat (European Commission)"
  - title: "Regulation (EC) No 223/2009 on European statistics"
    url: "https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=celex%3A32009R0223"
    publisher: "EUR-Lex (Publications Office of the European Union)"
  - title: "Regulation (EC) No 223/2009 — summary"
    url: "https://eur-lex.europa.eu/legal-content/EN/LSU/?uri=celex:32009R0223"
    publisher: "EUR-Lex (Publications Office of the European Union)"
---

# Eurostat

> **Verified 2026-08-21.** Every source this entity cites is on a domain the
> repository owner confirmed read and correct — `europa.eu`. `verification:
> primary-source`. See `docs/re-verification.md` §"The confirmed domains".

## Description

Eurostat is the EU's statistical authority. The **European Statistical
System (ESS)** is the partnership between Eurostat and the national
statistical institutes and other national authorities responsible in each
member state for developing, producing and disseminating European
statistics. The ESS was formalised by Regulation (EC) No 223/2009 —
informally the EU Statistical Law — amended by Regulation (EU) 2015/759 and
again by Regulation (EU) 2024/3018, which entered into force on
6 December 2024.

The nucleus of the ESS is the European Statistical System Committee (ESSC),
made up of the heads of Eurostat and of the national statistical institutes.
It decides on matters such as the annual European Statistical Programme,
response burden, cost effectiveness and statistical confidentiality.

## The CBS connection

[[NL-CBS]] is the Netherlands' national statistical institute, which makes
it an ESS participant and an ESSC member by the composition rule above. The
`participates-in` relationship is recorded on `NL-CBS`, with evidence noting
that the rule is sourced generically rather than by a source naming CBS.

**Regulation 223/2009 is not modelled as an entity.** It is arguably in
scope as EU legislation with a Dutch counterpart ([[NL-WET-CBS]]), and the
ESS would be better represented with it. Queued rather than added, to keep
Batch 9 within organisations and standards.

`coverage: low`: Eurostat's data holdings, dissemination infrastructure and
relationship to [[EU-DATA-STRATEGY]] were not researched.

## Relationships

- Partners with [[NL-CBS]] in the European Statistical System.

## Sources

Listed in frontmatter.
