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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-22"
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
    evidence: "Confirmed by reading personuvernd.is directly (2026-08-22): 'Persónuvernd er ríkisstofnun sem gætir hagsmuna þinna þegar persónuupplýsingum þínum er safnað' (Persónuvernd is a government institution that safeguards your interests when your personal data is collected). Corroborated by reading WIPO Lex's record of Act No. 90/2018 directly, whose own text names Persónuvernd as the body overseeing implementation of the GDPR and the Act. Anchor edge under metadata/relationship-types.md §2.3: a national supervisory authority established by statute is part of the state."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-EDPB
    source: fact
    evidence: "NOT independently re-confirmed 2026-08-22 for Persónuvernd by name: eur-lex.europa.eu's own text of Decision of the EEA Joint Committee No 154/2018, read directly in an earlier pass, provides that the supervisory authorities of the EFTA States shall participate in the activities of the European Data Protection Board. Membership follows from that sourced composition rule rather than from a source naming Persónuvernd specifically, the same basis on which the national standardisation bodies were attached to EU-CEN. `efta.int`'s own copy of the decision was not located this pass."
    confidence: medium
    valid_from: 2018-07-06
    valid_until: null

sources:
  - title: "Persónuvernd — Icelandic Data Protection Authority"
    url: "https://www.personuvernd.is/"
    publisher: "Persónuvernd"
    accessed: "2026-08-22"
  - title: "Act No. 90/2018 of June 27, 2018, on Data Protection and the Processing of Personal Data (Iceland)"
    url: "https://www.wipo.int/wipolex/en/legislation/details/18498"
    publisher: "WIPO Lex — World Intellectual Property Organization"
    accessed: "2026-08-22"
  - title: "Data Protected — Iceland"
    url: "https://www.linklaters.com/en/insights/data-protected/data-protected---iceland"
    publisher: "Linklaters"
    accessed: "2026-08-22"
  - title: "Decision of the EEA Joint Committee No 154/2018 of 6 July 2018"
    url: "https://eur-lex.europa.eu/eli/dec/2018/1022/oj"
    publisher: "EUR-Lex — Publications Office of the European Union"
    accessed: "2026-08-22"
---

# Persónuvernd

> **Verified 2026-08-22.** `personuvernd.is`, Linklaters' Iceland page
> and WIPO Lex's record of Act No. 90/2018 were all read directly. The
> `participates-in` [[EU-EDPB]] edge still rests on the JCD 154/2018
> composition rule rather than a source naming Persónuvernd itself,
> unchanged from before this pass.

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

Listed in frontmatter — the authority's own site, WIPO Lex's record of
the Act, a comparative law survey, and the EUR-Lex record of the Joint
Committee decision, all read directly this pass.
