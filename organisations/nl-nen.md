---
id: NL-NEN
type: organisation
name: Stichting Koninklijk Nederlands Normalisatie Instituut
alternative_names:
  - NEN
  - Royal Netherlands Standardization Institute
description: >
  The Dutch national standardisation institute, founded in 1916. A
  non-profit foundation holding the Royal predicate since 2016, NEN
  develops and manages national standards and administers the
  internationally (ISO, IEC) and European (EN, CENELEC) accepted standards
  recognised in the Netherlands.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-FORUM-STANDAARDISATIE
  - EU-CEN
  - INTL-ISO
relationships:
  - type: participates-in
    target: EU-CEN
    source: fact
    evidence: "Corrected and upgraded this pass (2026-08-27): previously recorded from the composition rule alone ('membership follows... rather than from a source naming NEN'). Reading nen.nl's own 'Over NEN' page directly finds NEN named explicitly: 'NEN is lid van de Europese en internationale normalisatienetwerken CEN en ISO' (NEN is a member of the European and international standardisation networks CEN and ISO). The page also names IEC, CENELEC and ETSI as networks NEN belongs to, and states NEN manages international secretariats in areas where the Netherlands has particular expertise."
    confidence: high
    valid_from: null
    valid_until: null
  - type: participates-in
    target: INTL-ISO
    source: fact
    evidence: "Same sentence as the EU-CEN edge above, read directly on nen.nl's own 'Over NEN' page (2026-08-27): 'NEN is lid van de Europese en internationale normalisatienetwerken CEN en ISO' names ISO alongside CEN in one breath. Picked up from `discovery/unresolved.md`, which had flagged NEN's ISO membership as recorded only from an unsourced 1947 co-founder claim (Batch 2) and asked for the same direct-naming treatment already given to the CEN edge — closed here on the source this pass already had, rather than requiring a fresh fetch."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Over NEN"
    url: "https://www.nen.nl/over-nen"
    publisher: "NEN"
    accessed: "2026-08-27"
  - title: "NEN (Stichting Koninklijk Nederlands Normalisatie Instituut)"
    url: "https://www.noraonline.nl/wiki/NEN_(Stichting_Koninklijk_Nederlands_Normalisatie_Instituut)"
    publisher: "NORA Online (ICTU)"
    accessed: "2026-08-27"
  - title: "NEN"
    url: "https://nl.wikipedia.org/wiki/NEN"
    publisher: "Wikipedia"
    accessed: "2026-08-27"
---

# NEN

> **Verified 2026-08-27.** All three cited pages were read directly this
> pass, closing the previous `search-only` status (never previously
> `last_verified`). Two corrections and one softened claim resulted — see
> below.

## Description

NEN is the standardisation institute of the Netherlands: a foundation
without profit motive, holding the Royal predicate, which brings
stakeholders together to reach agreements recorded in standards and
guidelines.

**Founding date, now sourced precisely at the year level.** Reading
nl.wikipedia.org's own article directly: NEN's predecessor, the
*Nederlands Normalisatie-instituut* (NNI), was established in **1916** by
the Koninklijk Instituut van Ingenieurs (KIvI) and the Nederlandsche
Maatschappij voor Nijverheid en Handel. The same article states NEN
received the **Royal predicate in 2016** — its centenary year.
`start_date` is left `null`: no source read gives an exact founding day for
1916, and per Atlas practice a year-only claim is recorded in prose rather
than padded into a specific date.

It manages a reported **34,000+ standards**, comprising the international
(ISO, IEC), European (EN, CENELEC) and national (NEN) standards recognised
in the Netherlands, confirmed directly on nen.nl's own page, which also
names **ETSI** as a fourth international network NEN belongs to (not
previously recorded here).

"NEN" abbreviates *NEderlandse Norm*, and since **8 May 2000** — confirmed
directly via nl.wikipedia.org — has also been the name of the close
cooperation between the Stichting Koninklijk Nederlands Normalisatie
Instituut and the **Stichting Koninklijk Nederlands Elektrotechnisch
Comité (NEC)**, the latter founded 17 March 1911 and specialising in
electrical engineering, information technology and telecommunications
standardisation. The two bodies maintain separate governance structures
while sharing facilities in Delft. The `name` field records the
foundation; the NEC and the combined arrangement are not separately
modelled, which may need revisiting.

**Unconfirmed this pass: the claim that NEN was "a co-founder of ISO in
1947."** No page read — nen.nl, the NORA wiki, or Dutch Wikipedia —
states this, and a targeted search for it turned up nothing beyond the
uncontroversial facts that NEN was founded in 1916 and ISO in 1947. The
claim is downgraded from stated fact to unconfirmed and should not be
repeated as established without a source.

**ISO membership itself closed, 2026-09-05.** A separate, narrower
question — not the 1947 co-founding claim above, but simply whether NEN
is a current ISO member at all — is answered by the same nen.nl sentence
already cited for the CEN edge: "NEN is lid van de Europese en
internationale normalisatienetwerken CEN en ISO." `participates-in`
[[INTL-ISO]] is now asserted alongside the existing [[EU-CEN]] edge.

## Relationships

- Complementary to [[NL-FORUM-STANDAARDISATIE]]: NEN operates the formal
  national standards infrastructure, while Forum Standaardisatie governs
  which open standards public bodies must apply. No relationship is
  asserted between them, as none was sourced this pass either.
- `participates-in` [[EU-CEN]] and [[INTL-ISO]] — both confirmed by a
  source naming NEN directly, not only by the composition rule (see
  relationship evidence). The ISO edge is new this pass.
- ISO and IEC remain unmodelled, so those relationships are still
  unassertable, though nen.nl confirms NEN's membership in both.
  [[EU-CENELEC]] is the European counterpart of the Dutch NEC, with which
  NEN has cooperated since 8 May 2000 (date now sourced) — see the open
  modelling question about whether NEC warrants its own entity.

## Sources

All three read directly this pass: nen.nl's own "Over NEN" page, the NORA
Online wiki entry, and the Dutch Wikipedia article.
