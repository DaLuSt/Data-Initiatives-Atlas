---
id: IS-PERSONUVERND
type: organisation
name: Persónuvernd
alternative_names:
  - Icelandic Data Protection Authority
  - Data Protection Authority (Iceland)
description: >
  Iceland's data protection supervisory authority. It supervises the
  application of Act No. 90/2018 on Data Protection and the Processing of
  Personal Data, which gives the General Data Protection Regulation effect
  in Icelandic law, and continued in that role when the act replaced Act
  No. 77/2000. As the supervisory authority of an EEA EFTA state it
  participates in the activities of the European Data Protection Board under
  Decision of the EEA Joint Committee No 154/2018.

level: national
country: IS
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
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - IS
  - IS-PERSONUVERNDARLOG
  - EU-EDPB
  - INTL-EEA-JCD-154-2018
relationships:
  - type: part-of
    target: IS
    source: fact
    evidence: "Persónuvernd is Iceland's Data Protection Authority and continues to act as the supervisory authority under Act No. 90/2018 on Data Protection and the Processing of Personal Data (personuvernd.is; linklaters.com 'Data Protected — Iceland'; dlapiperdataprotection.com Iceland). NOT READ — search-only. Anchor edge under metadata/relationship-types.md §2.3: a national supervisory authority established by statute is part of the state."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-EDPB
    source: fact
    evidence: "Decision of the EEA Joint Committee No 154/2018 of 6 July 2018 provides that the supervisory authorities of the EFTA States shall participate in the activities of the European Data Protection Board (eur-lex.europa.eu ELI dec/2018/1022/oj; efta.int 154-2018). NOT READ — search-only. Membership follows from the sourced rule rather than from a source naming Persónuvernd, the same basis on which the national standardisation bodies were attached to EU-CEN."
    confidence: medium
    valid_from: 2018-07-06
    valid_until: null

sources:
  - title: "Persónuvernd — Icelandic Data Protection Authority"
    url: "https://www.personuvernd.is/"
    publisher: "Persónuvernd"
  - title: "Data Protected — Iceland"
    url: "https://www.linklaters.com/en/insights/data-protected/data-protected---iceland"
    publisher: "Linklaters"
  - title: "Decision of the EEA Joint Committee No 154/2018 of 6 July 2018"
    url: "https://eur-lex.europa.eu/eli/dec/2018/1022/oj"
    publisher: "EUR-Lex — Publications Office of the European Union"
---

# Persónuvernd

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read — retrieval is blocked by
> the network egress proxy. `verification: search-only`.

## Description

Iceland's data protection supervisory authority, and Iceland's **first
modelled national entity** — the country anchor was created in the European
country expansion with the note that *"no national entities are modelled
yet"*.

It supervises [[IS-PERSONUVERNDARLOG]] and continued in that role when the
2018 act replaced Act No. 77/2000.

## The EDPB edge, and how it is justified

Persónuvernd `participates-in` [[EU-EDPB]] even though Iceland is not a
member state. The basis is [[INTL-EEA-JCD-154-2018]], which provides that
**the supervisory authorities of the EFTA States shall participate in the
activities of the Board**.

This is the same kind of evidence the Atlas already accepted for
[[NL-NEN]] and [[EU-CEN]]: a sourced **composition rule** rather than a
source naming the individual body. The rule names a class — the supervisory
authorities of the EFTA States — and Persónuvernd is in it.

It is worth being precise about what the rule does and does not say. It says
the EFTA authorities *participate in the activities of* the Board. It does
not make them members with a vote under Article 68(3) GDPR, and no such
claim is made here.

## Relationships

- `part-of` [[IS]] — anchor edge under `metadata/relationship-types.md` §2.3.
- `participates-in` [[EU-EDPB]], on the composition rule above.

## Sources

Listed in frontmatter — the authority's own site, a comparative law survey,
and the EUR-Lex record of the Joint Committee decision.
