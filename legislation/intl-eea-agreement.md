---
id: INTL-EEA-AGREEMENT
type: law
name: Agreement on the European Economic Area
alternative_names:
  - EEA Agreement
  - EØS-avtalen
  - Oporto Agreement
description: >
  International agreement signed at Oporto on 2 May 1992 and in force since
  1 January 1994, extending the European Union's single market to three
  EFTA states — Iceland, Liechtenstein and Norway. Its common rules are
  continuously updated by adding new EU legislation through decisions of the
  EEA Joint Committee, which is how an EU act comes to have effect in an EEA
  EFTA state.

level: international
country: null
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 1994-01-01
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - "NO"
  - CH
  - EU
  - NO-PERSONOPPLYSNINGSLOVEN
relationships:
  - type: applies-in
    target: "NO"
    source: fact
    evidence: "The Agreement on the European Economic Area was signed on 2 May 1992 in Oporto and entered into force on 1 January 1994; it extends the single market of the EU to three of the four EFTA countries, namely Iceland, Norway and Liechtenstein, and one of its central features is that its common rules are continuously updated by adding new EU legislation through decisions of the EEA Joint Committee (eur-lex.europa.eu 'Agreement on the European Economic Area' summary; europarl.europa.eu Fact Sheet 169 'The European Economic Area (EEA), Switzerland and the North'; government.is 'European Economic Area — General information'). NOT READ — search-only."
    confidence: medium
    valid_from: 1994-01-01
    valid_until: null

sources:
  - title: "Agreement on the European Economic Area (summary)"
    url: "https://eur-lex.europa.eu/EN/legal-content/summary/agreement-on-the-european-economic-area.html"
    publisher: "EUR-Lex / Publications Office of the European Union"
  - title: "The European Economic Area (EEA), Switzerland and the North — Fact Sheet 169"
    url: "https://www.europarl.europa.eu/factsheets/en/sheet/169/the-european-economic-area-eea-switzerland-and-the-north."
    publisher: "European Parliament"
  - title: "European Economic Area (EEA) — General information"
    url: "https://www.government.is/topics/foreign-affairs/iceland-in-europe/european-economic-area/"
    publisher: "Government of Iceland"
  - title: "Decision of the EEA Joint Committee No 154/2018 of 6 July 2018 amending Annex XI and Protocol 37 to the EEA Agreement"
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv:OJ.L_.2018.183.01.0023.01.ENG"
    publisher: "EUR-Lex / Publications Office of the European Union"
---

# Agreement on the European Economic Area

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

Signed at **Oporto on 2 May 1992**, in force since **1 January 1994**. It
extends the EU's single market to three of the four EFTA states — **Iceland,
Liechtenstein and Norway** — with free movement of goods, services, capital
and persons.

## The mechanism this entity exists to make visible

The EEA Agreement's defining feature is that it is **not static**. Its
common rules are continuously updated by adding new EU legislation through
**decisions of the EEA Joint Committee**, taken every few weeks.

That is the route by which an EU act comes to have effect in an EEA EFTA
state, and it is the thing the Atlas could describe in prose and not draw.

The worked example is [[EU-GDPR]] and Norway:

| Date | Event |
|---|---|
| 25 May 2018 | GDPR applicable **in the member states** |
| **6 July 2018** | **JCD No 154/2018 incorporates the GDPR into Annex XI of this Agreement** |
| 20 July 2018 | [[NO-PERSONOPPLYSNINGSLOVEN]] in force — the GDPR takes effect in Norway |

**Eight weeks of divergence.** A member state cannot have that gap.

## Why this entity carries `applies-in` [[NO]] and no EU instrument does

The distinction is the whole point.

- **The EEA Agreement applies in Norway.** Norway is a party to it. That is
  a plain, sourced statement of territorial application, and it is the edge
  asserted here.
- **[[EU-GDPR]] does not apply in Norway** in the sense `applies-in` carries
  elsewhere in this repository — of its own force, or through a
  transposition the instrument itself requires. It has effect there because
  *this Agreement* was amended to include it.

So [[NO]] is reached, correctly, through the instrument that actually
reaches it.

## ⚠ The individual Joint Committee decisions are not modelled

**JCD No 154/2018 is not an entity**, and neither is any other. Cataloguing
the decisions that incorporate each EU act into the EEA Agreement is a large
piece of work, and without them the Atlas cannot draw
`EU-GDPR → JCD 154/2018 → INTL-EEA-AGREEMENT → NO` as a chain.

What it can now draw is the endpoints. The chain's middle is recorded in
prose here and on [[NO-PERSONOPPLYSNINGSLOVEN]], and the decisions are
queued in `discovery/candidates.md`.

## Switzerland signed it and never joined

[[CH]] took part in the negotiation and **signed the Agreement in 1992**,
then **voted against membership in December 1992** and never became a party.
It remains an EFTA member outside the EEA, which is why its relationship
with the Union runs through bilateral agreements instead.

That is why this entity carries `applies-in` to Norway and **not** to
Switzerland, and it is the cleanest available illustration that the two
non-member countries in this Atlas are in genuinely different positions.

## Not modelled

- **Iceland and Liechtenstein**, the other two EEA EFTA states. Adding
  either would show whether the Norwegian pattern generalises.
- The **EEA Joint Committee**, **EFTA**, the **EFTA Surveillance Authority**
  and the **EFTA Court**.
- The **Annexes and Protocols**. Annex XI (electronic communication,
  audiovisual services and information society) is the one that matters for
  this Atlas and is named in the evidence rather than modelled.
- The **1994 EU enlargement**, which took Austria, Finland and Sweden out of
  the EFTA side of the Agreement and into the Union.

## Sources

Listed in frontmatter. Three of four are official — EUR-Lex, the European
Parliament and the Government of Iceland.
