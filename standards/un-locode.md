---
id: UN-LOCODE
type: standard
name: United Nations Code for Trade and Transport Locations
alternative_names:
  - UN/LOCODE
description: >
  Code list maintained under the United Nations Economic Commission for
  Europe through UN/CEFACT, assigning coded designations to locations used in
  trade and transport. It is named in Union law: Regulation (EU) 2019/1239
  establishing a European Maritime Single Window environment provides for a
  common location database holding a reference list of location codes
  including UN/LOCODE, alongside SafeSeaNet-specific codes and the IMO port
  facility codes registered in GISIS.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains:
  - DOMAIN-MOBILITY
organisations:
  - UN-CEFACT
related_entities:
  - UN-CEFACT
  - UN-UNECE
  - EU-EMSWE
relationships:
  - type: maintained-by
    target: UN-CEFACT
    source: fact
    evidence: "Both originally-cited unece.org pages returned HTTP 403 this pass (domain-wide block, confirmed by testing the bare root). eur-lex.europa.eu's own page for Regulation (EU) 2019/1239 also failed to return readable content (empty response). Per this batch's source-substitution instruction, legislation.gov.uk's UK retained-EU-law text of the same regulation was fetched directly instead and confirms, in the regulation's own words: 'A Common Location Database should be established which holds a reference list of location codes, including the United Nations Code for Trade and Transport Locations (UN/LOCODE), the SafeSeaNet-specific codes, and the port facility codes as registered in [IMO GISIS]' (Article 15 / Article 2(1)). Wikipedia's UN/LOCODE article, also read directly, independently confirms UNECE develops and maintains it, though it does not itself mention the EMSWE regulation."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "UN/LOCODE — Code List by Country and Territory"
    url: "https://unece.org/trade/cefact/unlocode-code-list-country-and-territory"
    publisher: "United Nations Economic Commission for Europe"
  - title: "Regulation (EU) 2019/1239 establishing a European Maritime Single Window environment — retained EU law text"
    url: "https://www.legislation.gov.uk/eur/2019/1239/data.xht?view=snippet&wrap=true"
    publisher: "UK National Archives — legislation.gov.uk"
    accessed: "2026-08-28"
  - title: "UN/LOCODE"
    url: "https://en.wikipedia.org/wiki/UN/LOCODE"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
---

# UN/LOCODE

> **Verified 2026-08-28, via source substitution.** Both `unece.org` and
> `eur-lex.europa.eu` remained unreachable this pass (the former
> domain-wide 403-blocked, the latter returning empty content on every
> attempt). Per this batch's instruction, `legislation.gov.uk`'s retained-EU-
> law mirror of the exact same regulation text was fetched directly and
> confirms the UN/LOCODE reference verbatim, and Wikipedia's UN/LOCODE
> article corroborates UNECE's maintainer role. Two of the three sources in
> the resulting list are now genuinely read.

## Description

The **United Nations Code for Trade and Transport Locations**: a code list
maintained under [[UN-UNECE]] through [[UN-CEFACT]], assigning coded
designations to the locations used in trade and transport.

## This is the answer to a question the UN batch asked and could not answer

`discovery/candidates.md` §2 recorded that [[UN-CEFACT]] *"connects to
nothing European"*, and posed a deliberately narrow question:

> ***does any instrument already in this Atlas reference one [UN/CEFACT
> standard]?*** — *"Open — narrow, answerable"*

The honest answer turned out to be **no, and here is the one that would**.
No instrument that was already in the Atlas names a UN/CEFACT output. But
**Regulation (EU) 2019/1239**, establishing the European Maritime Single
Window environment, provides for a common location database holding a
reference list of location codes **including UN/LOCODE**, alongside
SafeSeaNet-specific codes and the IMO port facility codes registered in
GISIS.

So the row is closed by adding the instrument — [[EU-EMSWE]] — rather than by
finding one already present. The trade and e-business cluster is no longer an
island:

```
   UN ─▶ UN-UNECE ─▶ UN-CEFACT
                         ▲
                   maintained-by
                         │
                     UN-LOCODE ◀── references ── EU-EMSWE ──▶ EU
```

## Relationships

- `maintained-by` [[UN-CEFACT]].
- The `references` edge from [[EU-EMSWE]] lives on the regulation, which is
  the citing party.

## Sources

Listed in frontmatter, two of three read directly this pass. The UNECE code
list page stays on record but is 403-blocked this session; EUR-Lex's own
page for the regulation returned empty content on fetch and is replaced
here with legislation.gov.uk's retained-EU-law mirror of the identical
provisions, plus Wikipedia's UN/LOCODE article as a second corroborating
source.
