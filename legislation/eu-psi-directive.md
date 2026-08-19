---
id: EU-PSI-DIRECTIVE
type: directive
name: Directive 2003/98/EC on the re-use of public sector information
alternative_names:
  - PSI Directive
  - Public Sector Information Directive
  - Directive 2003/98/EC
description: >
  The European Union's original directive on the re-use of public sector
  information, adopted in 2003 and amended by Directive 2013/37/EU. It was
  recast as Directive (EU) 2019/1024 on open data and the re-use of public
  sector information, which repealed it. Several national instruments still
  in force in the Atlas were written to transpose this directive rather than
  its successor.

level: regional
country: null
region: EU

status: superseded
confidence: medium
coverage: medium
verification: search-only

start_date: 2003-11-17
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: EU-OPEN-DATA-DIRECTIVE

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-OPEN-DATA-DIRECTIVE
  - BE-HERGEBRUIK-WET
  - DE-IWG
relationships:
  - type: applies-in
    target: EU
    source: fact
    evidence: "Directive 2003/98/EC of the European Parliament and of the Council of 17 November 2003 on the re-use of public sector information was an EU directive addressed to the member states; it was amended by Directive 2013/37/EU and recast as Directive (EU) 2019/1024 on open data and the re-use of public sector information, which repealed it (eur-lex.europa.eu ELI dir/2003/98; eur-lex.europa.eu ELI dir/2019/1024 'open data and the reuse of public-sector information'; digital-strategy.ec.europa.eu 'Open Data Directive'). NOT READ — search-only."
    confidence: medium
    valid_from: 2003-11-17
    valid_until: null

sources:
  - title: "Directive 2003/98/EC on the re-use of public sector information"
    url: "https://eur-lex.europa.eu/eli/dir/2003/98/oj"
    publisher: "EUR-Lex / Publications Office of the European Union"
  - title: "Directive (EU) 2019/1024 on open data and the re-use of public sector information"
    url: "https://eur-lex.europa.eu/eli/dir/2019/1024/oj/eng"
    publisher: "EUR-Lex / Publications Office of the European Union"
  - title: "Open data and the reuse of public-sector information (summary)"
    url: "https://eur-lex.europa.eu/EN/legal-content/summary/open-data-and-the-reuse-of-public-sector-information.html"
    publisher: "EUR-Lex / Publications Office of the European Union"
---

# PSI Directive (2003/98/EC)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

The EU's original **public sector information** directive, of 17 November
2003, amended in 2013 and recast as [[EU-OPEN-DATA-DIRECTIVE]] — which
repealed it.

## Why a repealed directive is worth an entity

This was queued in `discovery/research-queue.md` from the **Belgium batch**
with a precise reason: it would *"give [[BE-HERGEBRUIK-WET]] and [[DE-IWG]]
somewhere to point."*

Both are national instruments **still in force** that were written to
transpose *this* directive, not its successor. Before this entity existed
the Atlas had two options, both wrong:

- point them at [[EU-OPEN-DATA-DIRECTIVE]], which they do not implement and
  which post-dates them; or
- leave them pointing at nothing, which is what happened.

A repealed instrument is not an absent one. It is the thing that explains
why a national act exists in the form it does, and the Atlas needs it to
avoid attributing a 2016 Belgian act to a 2019 directive.

## `status: superseded`, with the successor named

`successor: EU-OPEN-DATA-DIRECTIVE`, following the convention in
`CONTRIBUTING.md`: superseded entities are not deleted, and the successor is
named on both ends.

This is the Atlas's clearest case of the pattern. [[GB-DSIT]] was abolished
and its functions dispersed; this directive was **recast** — the successor
is the same instrument rewritten, and the national acts transposing the old
one keep operating until each member state replaces them.

## Not modelled

- **Directive 2013/37/EU**, the amending directive. Its content was not
  established, and a separate entity for an amendment that was itself
  repealed would add a node and no clarity.

## Sources

Listed in frontmatter — all three EUR-Lex.
