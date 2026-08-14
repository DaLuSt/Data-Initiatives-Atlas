---
id: NL-AP
type: organisation
name: Autoriteit Persoonsgegevens
alternative_names:
  - AP
  - Dutch Data Protection Authority
description: >
  The Netherlands' independent data protection supervisory authority. It
  monitors and promotes the protection of personal data, and is the national
  supervisory authority designated under the EU General Data Protection
  Regulation, with enforcement powers including the imposition of fines.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities: []
relationships: []

sources:
  - title: "Autoriteit Persoonsgegevens (AP) — Contactgids"
    url: "https://www.rijksoverheid.nl/service/contact/contactgids/a/autoriteit-persoonsgegevens"
    publisher: "Rijksoverheid"
  - title: "AP (Autoriteit Persoonsgegevens)"
    url: "https://www.noraonline.nl/wiki/AP_(Autoriteit_Persoonsgegevens)"
    publisher: "NORA Online (ICTU)"
  - title: "Privacyregels beschermen persoonsgegevens"
    url: "https://www.rijksoverheid.nl/onderwerpen/privacy-en-persoonsgegevens/privacyregels-beschermen-persoonsgegevens"
    publisher: "Rijksoverheid"
---

# Autoriteit Persoonsgegevens (AP)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The AP is the Netherlands' independent supervisory authority for the
protection of personal data. It is a zelfstandig bestuursorgaan designated
by law as the supervisory authority for the processing of personal data.

Its tasks derive from the EU General Data Protection Regulation, under which
every member state must designate an independent supervisory authority. The
AP assesses whether individuals and organisations — government included —
comply with the regulation, and may intervene where they do not, including
by imposing fines. Its independence is structural: in performing its tasks
and exercising its powers it may neither seek nor accept instructions from
others, and must have sufficient resources to do its work.

## Relationships

No relationships are recorded yet, and this is a deliberate gap rather than
an oversight. The AP's defining relationship is to the GDPR and, through it,
to the European Data Protection Board — both EU-level entities scheduled for
Batches 8 and 9. Once `EU-GDPR` exists, this entity should gain an
`implements-requirement-from` relationship to it, and the Dutch
implementation act (UAVG, Batch 3) should link here too. Recorded in
`discovery/research-queue.md`.

This is exactly the vertical EU→national chain the Atlas is meant to make
visible, and it will only be assertable once the EU layer is populated.

## Sources

Listed in frontmatter.
