---
id: NO-DATATILSYNET
type: organisation
name: Datatilsynet
alternative_names:
  - Norwegian Data Protection Authority
  - Norwegian DPA
description: >
  Norway's data protection supervisory authority, designated by the Personal
  Data Act of 15 June 2018. Because Norway is an EEA EFTA state rather than
  an EU member state, it is notified to the EEA Joint Committee rather than
  to the European Commission, and the GDPR's supervisory cooperation
  mechanisms operate between it and member-state authorities through
  EEA-specific channels.

level: national
country: "NO"
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-09-13"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NO-PERSONOPPLYSNINGSLOVEN
  - EU-GDPR
  - EU-EDPB
  - INTL-EEA-JCD-154-2018
relationships:
  - type: applies-to
    target: NO-PERSONOPPLYSNINGSLOVEN
    source: fact
    evidence: "Confirmed verbatim by reading a Datatilsynet administrative-fine decision directly (2026-08-22): 'The Norwegian Data Protection Authority (hereinafter \"Datatilsynet\", \"we\", \"us\", \"our\") is the independent supervisory authority responsible for monitoring the application of the General Data Protection Regulation (\"GDPR\") with respect to Norway.' Independently confirmed on linklaters.com, read directly: 'The Norwegian Data Protection Authority will continue to act as the supervisory authority in Norway.' lovdata.no's own metadata record for the Act confirms its 20 July 2018 effective date."
    confidence: medium
    valid_from: 2018-07-20
    valid_until: null
  - type: participates-in
    target: EU-EDPB
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP (discovery/unresolved.md row #107). This entity previously withheld the edge on the ground that sources described only vague 'EEA-specific channels.' [[INTL-EEA-JCD-154-2018]]'s own text, read directly, states plainly: 'the supervisory authorities of the EFTA States shall participate fully in the one-stop-shop and the consistency mechanism and shall, but for the right to vote and to stand for election as chair or deputy chairs of the ... Board, have the same rights and obligations as supervisory authorities of the EU Member States in that Board.' This is the identical composition-rule basis already accepted for [[IS-PERSONUVERND]] and [[LI-DATENSCHUTZSTELLE]] — Norway is one of the same three named EFTA states the rule covers, so withholding the edge here while granting it to Iceland and Liechtenstein was an inconsistency, not a distinction."
    confidence: medium
    valid_from: 2018-07-06
    valid_until: null

sources:
  - title: "Data Protected — Norway"
    url: "https://www.linklaters.com/en/insights/data-protected/data-protected---norway"
    publisher: "Linklaters"
    accessed: "2026-08-22"
  - title: "Data protection laws in Norway"
    url: "https://www.dlapiperdataprotection.com/index.html?t=law&c=NO"
    publisher: "DLA Piper"
    accessed: "2026-08-22"
  - title: "Datatilsynet — administrative fine decision (example of published enforcement)"
    url: "https://www.datatilsynet.no/contentassets/f974410ee2e142c99cfc208cbae7634e/administrative-fine---sats-asa.pdf"
    publisher: "Datatilsynet"
    accessed: "2026-08-22"
  - title: "Decision of the EEA Joint Committee No 154/2018 of 6 July 2018"
    url: "https://eur-lex.europa.eu/eli/dec/2018/1022/oj"
    publisher: "EUR-Lex — Publications Office of the European Union"
    accessed: "2026-09-13"
---

# Datatilsynet

> **Verified 2026-08-22.** All three cited pages were read directly and
> confirm the claims below, verbatim in places — including Datatilsynet's
> own published administrative-fine decision, which states the
> authority's mandate in its own words.
>
> **Updated 2026-09-13**: added `participates-in` [[EU-EDPB]], closing
> `discovery/unresolved.md` row #107 — see below.

## Description

Confirmed verbatim by reading Datatilsynet's own published SATS ASA
administrative-fine decision directly (2026-08-22): "The Norwegian Data
Protection Authority (hereinafter 'Datatilsynet', 'we', 'us', 'our') is
the independent supervisory authority responsible for monitoring the
application of the General Data Protection Regulation ('GDPR') with
respect to Norway." Datatilsynet is Norway's data protection supervisory authority, designated
by [[NO-PERSONOPPLYSNINGSLOVEN]].

## A supervisory authority notified to a different body

The EEA route leaves a visible mark on this entity, and it is the reason it
is worth reading alongside [[NL-AP]] or [[DE-BFDI]].

When [[EU-GDPR]] was incorporated into the EEA Agreement by **Joint
Committee Decision No 154/2018**, the decision carried an adaptation:
Norway notifies its supervisory authority to the **EEA Joint Committee**,
not to the **European Commission**, and the Regulation's cooperation
mechanisms run between Datatilsynet and member-state authorities through
EEA-specific channels.

A member state's authority is notified to the Commission. Norway's is not.
The substance of supervision is the same; the plumbing is not.

## `participates-in` [[EU-EDPB]], closing a previously-flagged gap

This entity previously withheld the edge, reasoning that the sources
available described only vague "EEA-specific channels" for cooperation
with member-state authorities, without saying what standing that gave
Datatilsynet on the Board itself.

[[INTL-EEA-JCD-154-2018]], created 2026-08-22, closes that gap directly.
Its own text, read directly, states: "the supervisory authorities of the
EFTA States shall participate fully in the one-stop-shop and the
consistency mechanism and shall, but for the right to vote and to stand
for election as chair or deputy chairs of the ... Board, have the same
rights and obligations as supervisory authorities of the EU Member States
in that Board." That is the **identical composition-rule basis** already
accepted for [[IS-PERSONUVERND]] and [[LI-DATENSCHUTZSTELLE]] — the
Decision names "the EFTA States" as a class, of which Norway, Iceland and
Liechtenstein are the only three members. Granting the edge to two of the
three while withholding it from Norway was an inconsistency this entity
carried, not a distinction the sources supported — closed
`discovery/unresolved.md` row #107.

As with the other two EFTA DPAs: this is participation in the Board's
*activities*, not membership with a vote under Article 68(3) GDPR.

Note that the Atlas's EDPB connectivity was previously logged in
`discovery/candidates.md` as a cheap-fix opportunity; this closes one more
of the eight national data protection authorities in the graph.

## Relationships

- `applies-to` [[NO-PERSONOPPLYSNINGSLOVEN]].
- `participates-in` [[EU-EDPB]], on the composition rule in
  [[INTL-EEA-JCD-154-2018]], added 2026-09-13.

## Sources

Listed in frontmatter. The original three were read directly in the
2026-08-22 pass; the EUR-Lex record of Decision 154/2018 was added
2026-09-13, already read directly in an earlier pass on
[[INTL-EEA-JCD-154-2018]] itself. What was once this entity's weakest
point turned out to be its strongest: the "only a published fine"
citation, read directly, opens with the authority describing its own
mandate in its own words — a better source than either commercial
law-firm survey.
