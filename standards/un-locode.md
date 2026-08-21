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
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-21"
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
    evidence: "UN/CEFACT is the subsidiary intergovernmental body of the UN Economic Commission for Europe serving as the focal point within ECOSOC for trade facilitation recommendations and electronic business standards, and works on standardising and harmonising the core information used in trade documents; UN/LOCODE is one of its code lists (unece.org/trade/uncefact; unece.org/trade/cefact/unlocode-code-list-country-and-territory). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "UN/LOCODE — Code List by Country and Territory"
    url: "https://unece.org/trade/cefact/unlocode-code-list-country-and-territory"
    publisher: "United Nations Economic Commission for Europe"
  - title: "UN/CEFACT — United Nations Centre for Trade Facilitation and Electronic Business"
    url: "https://unece.org/trade/uncefact"
    publisher: "United Nations Economic Commission for Europe"
  - title: "Regulation (EU) 2019/1239 establishing a European Maritime Single Window environment"
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32019R1239"
    publisher: "EUR-Lex — Publications Office of the European Union"
---

# UN/LOCODE

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read — retrieval of
> `unece.org` and `eur-lex.europa.eu` is blocked by the network egress proxy.
> `verification: search-only`.

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

Listed in frontmatter — the UNECE code list page, the UN/CEFACT overview, and
the EUR-Lex record of Regulation (EU) 2019/1239.
