---
id: "NO"
type: country
name: Norway
alternative_names:
  - Kingdom of Norway
  - Norge
  - Noreg
description: >
  Country anchor entity for Norway, the eighth national scope covered by the
  Data Initiatives Atlas and the first that is a party to the Agreement on
  the European Economic Area without being a member of the European Union.
  EU acts do not apply in Norway by force of Union law; they take effect
  only once incorporated into the EEA Agreement by a decision of the EEA
  Joint Committee and then implemented in Norwegian law.

level: national
country: "NO"
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains: []
organisations: []
related_entities: []
relationships: []

sources:
  - title: "NO — Norway (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:NO"
    publisher: "International Organization for Standardization (ISO)"
  - title: "Decision of the EEA Joint Committee No 154/2018 of 6 July 2018 amending Annex XI and Protocol 37 to the EEA Agreement"
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv:OJ.L_.2018.183.01.0023.01.ENG"
    publisher: "EUR-Lex / Publications Office of the European Union"
  - title: "Data Protected — Norway"
    url: "https://www.linklaters.com/en/insights/data-protected/data-protected---norway"
    publisher: "Linklaters"
  - title: "Norway's agreements with the EU"
    url: "https://www.regjeringen.no/en/topics/european-policy/norway-eu/eos-avtalen/id685024/"
    publisher: "Regjeringen (Norwegian Government)"
---

# Norway

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read, because the working
> environment blocks page retrieval. `verification: search-only`. See
> `discovery/reverification-allowlist.md`.

## Description

Norway (ISO 3166-1 alpha-2: **`NO`**) is the **eighth country** in the
Atlas, after [[NL]], [[DE]], [[BE]], [[FR]], [[ES]], [[PL]] and [[GB]].

It is the first **EEA** country the Atlas holds — a party to the Agreement
on the European Economic Area, and not a member of the European Union.

## The third relationship to EU law in this Atlas

The Atlas now records three distinct ways a country can stand to an EU
instrument, and Norway is the one that needed a new explanation:

| Country type | How an EU act reaches it | Example |
|---|---|---|
| **Member state** ([[NL]], [[DE]], [[BE]], [[FR]], [[ES]], [[PL]], [[IE]]) | Directly applicable, or transposed | [[EU-GDPR]] `applies-in` [[NL]] |
| **Former member state** ([[GB]]) | Assimilated law, adequacy, extraterritorial scope — **no `applies-in` at all** | [[GB-UK-GDPR]] `derived-from` [[EU-GDPR]] |
| **EEA EFTA state** (Norway) | **Incorporation** into the EEA Agreement by Joint Committee decision, *then* national implementation | see below |
| **Neither** ([[CH]]) | Autonomous law plus an adequacy decision | see [[CH]] |

## Incorporation is not direct applicability

This is the distinction the batch exists to record.

[[EU-GDPR]] was incorporated into **Annex XI of the EEA Agreement** by
**Decision of the EEA Joint Committee No 154/2018 of 6 July 2018**. Only then
did it take effect in Norway, through
[[NO-PERSONOPPLYSNINGSLOVEN]], with effect from **20 July 2018** —
**two years and two months after** the Regulation became applicable in the
member states on 25 May 2018.

A member state has no such gap and no such step. Nothing in Norwegian law
gives an EU regulation force on its own.

The incorporation also came with an **adaptation**: Norway notifies its
supervisory authority to the **EEA Joint Committee** rather than to the
European Commission, and the GDPR's cooperation mechanisms run between
[[NO-DATATILSYNET]] and member-state authorities through EEA-specific
channels.

## ⚠ No `applies-in` edge from any EU instrument points at Norway

None is asserted, and this is a deliberate reading rather than a gap.

`applies-in` in this repository carries the member-state meaning: the
instrument applies of its own force, or through a transposition the
instrument itself requires. Neither is true here. Norwegian effect runs
through an EEA Joint Committee decision — **an instrument the Atlas does not
hold** — and then through a national act.

Asserting `applies-in` [[NO]] on [[EU-GDPR]] would make the Atlas say
Norway is in the same position as the Netherlands. It is not, and the
two-month gap in 2018 is the proof.

**The EEA Agreement and Joint Committee Decision 154/2018 are both queued in
`discovery/candidates.md`.** Until one of them exists, Norway's route to
[[EU-GDPR]] is recorded in prose on [[NO-PERSONOPPLYSNINGSLOVEN]] and here,
and not in the graph. That is an honest under-modelling, not a claim that no
relationship exists.

## Not modelled

- **The EEA Agreement itself**, the **EEA Joint Committee**, **EFTA**, the
  **EFTA Surveillance Authority** and the **EFTA Court** — the last two being
  Norway's counterparts to the Commission and the Court of Justice, and the
  reason Norway is supervised at all without being a member state.
- **Iceland and Liechtenstein**, the other EEA EFTA states.
- **The Schengen and Dublin association agreements**, under which Norway
  participates in instruments outside the EEA framework entirely.
- Any **sub-national** level. Norway's counties and municipalities are out
  of scope for the same reason everyone else's are: the Atlas has no
  `level: local` entity.

## Sources

Listed in frontmatter.
