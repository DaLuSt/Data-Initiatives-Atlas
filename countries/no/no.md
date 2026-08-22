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
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - INTL-COE
relationships:
  - type: part-of
    target: INTL-COE
    source: fact
    evidence: "NOT independently re-confirmed 2026-08-22: coe.int returns a bot-defense challenge (403, Cloudflare 'Attention Required!') and was not read, the same obstacle found on GB's and CH's identical edges. The claim (Norway is one of the 46 member states of the Council of Europe, an intergovernmental organisation separate from the European Union) is retained rather than removed, since a bot-wall is not evidence it is wrong. Anchor edge under metadata/relationship-types.md §2.3: it records Council of Europe membership and asserts no more than that. Added in the European country batch so that all fifty anchors carry the same membership edge."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "The Council of Europe's 46 member states"
    url: "https://www.coe.int/en/web/portal/46-members-states"
    publisher: "Council of Europe"
  - title: "Norway"
    url: "https://en.wikipedia.org/wiki/Norway"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
  - title: "Decision of the EEA Joint Committee No 154/2018 of 6 July 2018 amending Annex XI and Protocol 37 to the EEA Agreement"
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv:OJ.L_.2018.183.01.0023.01.ENG"
    publisher: "EUR-Lex / Publications Office of the European Union"
    accessed: "2026-08-22"
  - title: "Data Protected — Norway"
    url: "https://www.linklaters.com/en/insights/data-protected/data-protected---norway"
    publisher: "Linklaters"
    accessed: "2026-08-22"
  - title: "Norway's agreements with the EU"
    url: "https://www.regjeringen.no/en/topics/european-policy/norway-eu/eos-avtalen/id685024/"
    publisher: "Regjeringen (Norwegian Government)"
---

# Norway

> **Verified 2026-08-22.** en.wikipedia.org's Norway article, EUR-Lex's
> own text of JCD No 154/2018, and the European Parliament's EEA/EFTA
> fact sheet were all read directly this pass — the network egress
> restriction this caveat originally described no longer applies to
> `eur-lex.europa.eu` or `europarl.europa.eu`, matching what the UK and
> German batches found for `legislation.gov.uk`. `coe.int` and
> `www.iso.org` remain bot-walled; the ISO citation has been dropped
> (unread, unattested) and Wikipedia added in its place for the
> alternative names. `regjeringen.no` (the Norwegian government's own
> site) is also Cloudflare-bot-walled ("Just a moment...") and stays
> cited but unread.

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

- The **EFTA Surveillance Authority** and the **EFTA Court** — Norway's
  counterparts to the Commission and the Court of Justice, and the reason
  Norway is supervised at all without being a member state — and the **EEA
  Joint Committee**, which takes the incorporation decisions.
- ~~**The EEA Agreement itself**~~ — now [[INTL-EEA-AGREEMENT]].
- ~~**EFTA**~~ — now [[INTL-EFTA]], created in the European country batch.
- ~~**Iceland and Liechtenstein**, the other EEA EFTA states~~ — now [[IS]]
  and [[LI]], created in the same batch as base anchors.
- **The Schengen and Dublin association agreements**, under which Norway
  participates in instruments outside the EEA framework entirely.
- Any **sub-national** level. Norway's counties and municipalities are out
  of scope for the same reason everyone else's are: the Atlas has no
  `level: local` entity.

## Sources

Listed in frontmatter. The Wikipedia article, the EUR-Lex JCD text and
the European Parliament fact sheet were read directly this pass;
`coe.int` remains cited but unread (bot-walled), and `linklaters.com` /
`regjeringen.no` were fetched for the adjacent Norwegian entities in this
same pass rather than for this one specifically.
