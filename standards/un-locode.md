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
  - UN-CCL
  - UN-IMO-GISIS
relationships:
  - type: maintained-by
    target: UN-CEFACT
    source: fact
    evidence: "The report of UN/CEFACT's twelfth session (ECE/TRADE/CEFACT/2006/18, 14 September 2006), read directly 2026-11-23 from the UN Digital Library (unece.org answers 403): UN/CEFACT's group 'had also revised and approved code list updates to the following UNECE Recommendations', including 'Update 2/2005 of UN/LOCODE (a biannual update based on Recommendation 16 - Codes for Trade and Transport Locations)'. That is a 2006 record of the maintenance; current maintenance pages on unece.org could not be read. Regulation (EU) 2019/1239, read directly through publications.europa.eu, names UN/LOCODE among the location codes of the Common Location Database but not who maintains it."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "UN/CEFACT, report of the twelfth session (ECE/TRADE/CEFACT/2006/18, 14 September 2006)"
    url: "https://digitallibrary.un.org/record/582956/files/%5BE_%5DECE_TRADE_CEFACT_2006_18-EN.pdf"
    publisher: "United Nations (UN Digital Library)"
    accessed: "2026-11-22"
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
