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
verification: primary-source

start_date: 2003-11-17
end_date: null
last_verified: "2026-09-25"
previous_version: null
successor: EU-OPEN-DATA-DIRECTIVE

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-OPEN-DATA-DIRECTIVE
  - BE-HERGEBRUIK-WET
  - DE-IWG
  - FR-LOI-VALTER
  - FR-LRN
relationships:
  - type: applies-in
    target: EU
    source: fact
    evidence: "Directive 2003/98/EC of the European Parliament and of the Council of 17 November 2003 on the re-use of public sector information was an EU directive addressed to the member states; it was amended by Directive 2013/37/EU and recast as Directive (EU) 2019/1024 on open data and the re-use of public sector information, which repealed it (eur-lex.europa.eu ELI dir/2003/98; eur-lex.europa.eu ELI dir/2019/1024 'open data and the reuse of public-sector information'; digital-strategy.ec.europa.eu 'Open Data Directive'). NOT READ — search-only."
    confidence: medium
    valid_from: 2003-11-17
    valid_until: null

sources:
  - title: "Directive 2013/37/EU amending Directive 2003/98/EC"
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32013L0037"
    publisher: "EUR-Lex / Publications Office of the European Union"
    accessed: "2026-09-25"
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

> **Verified 2026-08-21.** Every source this entity cites is on a domain the
> repository owner confirmed read and correct — `europa.eu`. `verification:
> primary-source`. See `docs/re-verification.md` §"The confirmed domains".
>
> **Narrowed 2026-09-25**: Directive 2013/37/EU's own content, previously
> "not established" (`discovery/unresolved.md` row #47), is now read
> directly via EUR-Lex's TXT/HTML form. See "What the 2013 amendment
> actually did" below. The decision not to give it a separate entity
> stands unchanged.

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

## A third national instrument, cross-applied 2026-09-13

[[FR-LRN]] (France's 2016 loi pour une République numérique) had flagged
this directive by name as the source of the open-data lineage its own
chronology sources describe, but recorded it as "not an Atlas entity" —
stale, since fixed there with a `references` edge (lineage, not
transposition — no source states FR-LRN as this directive's actual French
transposing act).

## What the 2013 amendment actually did

**Directive 2013/37/EU of 26 June 2013**, read directly via EUR-Lex's
TXT/HTML form (2026-09-25), amended 2003/98/EC in five substantive ways:

- **Extended scope** to libraries (including university libraries),
  museums and archives — previously excluded entirely.
- **Turned re-use from optional to a duty**: its new Article 3 requires
  member states to ensure documents falling within the directive's scope
  "shall be re-usable," an affirmative obligation rather than the
  original's permissive framing.
- **Required open, machine-readable formats** for available documents and
  their metadata, "where possible and appropriate."
- **Tightened charging rules**, capping most charges at marginal cost,
  with a specific carve-out letting libraries, museums and archives
  recover collection costs plus a reasonable return on investment.
- **Allowed time-limited exclusive digitisation arrangements** for
  cultural materials, generally capped at ten years, with transparency
  duties and guaranteed public-sector access once exclusivity ends.

It entered into force, per its own text, "on the twentieth day following
that of its publication in the Official Journal" and set a transposition
deadline of **18 July 2015**.

## Not modelled

- **Directive 2013/37/EU** still has no entity of its own. Its content is
  now known (above), but the original reasoning for not splitting it out
  stands: it was itself repealed by [[EU-OPEN-DATA-DIRECTIVE]] alongside
  the directive it amended, and a separate node would add nothing a
  reader can't get from this entity's own prose.

## Sources

Listed in frontmatter — all three EUR-Lex.
