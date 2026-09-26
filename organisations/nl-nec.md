---
id: NL-NEC
type: organisation
name: Stichting Koninklijk Nederlands Elektrotechnisch Comité
alternative_names:
  - NEC
  - Nederlands Elektrotechnisch Comité
  - Royal Netherlands Electrotechnical Committee
description: >
  Dutch national standardisation body for electrotechnical engineering,
  information technology and telecommunications, founded on 17 March 1911
  as the Nederlands Electrotechnisch Comité and reconstituted as an
  independent foundation on 8 October 1962. Represents the Netherlands as
  the national member of the European Committee for Electrotechnical
  Standardisation (CENELEC) and the International Electrotechnical
  Commission (IEC). Since 8 May 2000 it has cooperated closely with
  [[NL-NEN]] under the shared "NEN" name, sharing facilities in Delft
  while each foundation keeps its own board.

level: national
country: NL
region: EU

status: active
confidence: high
coverage: low
verification: primary-source
organisation_role: standards-body

start_date: 1911-03-17
end_date: null
last_verified: "2026-09-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-NEN
  - EU-CENELEC
  - INTL-IEC
relationships:
  - type: participates-in
    target: EU-CENELEC
    source: fact
    evidence: "NARROWS discovery/unresolved.md row #28. Confirmed by reading CENELEC's own official members list directly (standards.cencenelec.eu/ords/f?p=CENELEC:5, 2026-09-26): the organisation representing the Netherlands is named 'Nederlands Electrotechnisch Comité' with the acronym NEC. nen.nl's own history page ('Onze historie'), also read directly, gives NEC's founding (17 March 1911) and its becoming an independent foundation on 8 October 1962, stating the change 'emphasized both international and national standards in the electrotechnical field.'"
    confidence: high
    valid_from: null
    valid_until: null
  - type: participates-in
    target: INTL-IEC
    source: fact
    evidence: "Confirmed by reading nen.nl's own history page directly (2026-09-26): after becoming an independent foundation in 1962, NEC 'focused entirely on the work of the international organization IEC' — the International Electrotechnical Commission, the IEC-side counterpart to NEC's CENELEC membership at the European level."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Onze historie"
    url: "https://www.nen.nl/onze-historie"
    publisher: "NEN"
    accessed: "2026-09-26"
  - title: "CENELEC Community — List of members"
    url: "https://standards.cencenelec.eu/ords/f?p=CENELEC:5"
    publisher: "CEN-CENELEC"
    accessed: "2026-09-26"
---

# NEC — Nederlands Elektrotechnisch Comité

> **Created 2026-09-26**, narrowing `discovery/unresolved.md` row #28
> ("Does the NEN/NEC cooperation or NEC itself warrant a separate
> entity?"). Sourced from NEN's own history page and CENELEC's own
> official membership list, both read directly. Completes the national
> counterpart the Atlas's [[EU-CENELEC]] entity had flagged as missing.

## Description

NEC is the Netherlands' own standardisation body for **electrotechnical
engineering, information technology and telecommunications** — founded
as the *Nederlands Electrotechnisch Comité* on **17 March 1911**,
predating even [[NL-NEN]]'s own 1916 founding. It became an independent
foundation on **8 October 1962**, a change NEN's own history page
describes as emphasising "both international and national standards in
the electrotechnical field."

## The missing half of a pairing the Atlas already had one side of

[[EU-CENELEC]]'s own file already noted "the Dutch counterpart
structure" as an open modelling question: NEN has been the shared name of
a cooperation between the NNI foundation (now [[NL-NEN]]) and NEC since 8
May 2000, with NEC as CENELEC's Dutch national counterpart. Confirmed
directly on CENELEC's own official members list: the Netherlands' entry
is "Nederlands Electrotechnisch Comité," acronym NEC — completing the
[[EU-CEN]]/[[EU-CENELEC]] ↔ [[NL-NEN]]/NEC national-counterpart structure
the Atlas already models for CEN's side.

## Two foundations, one shared name, separate boards

NEC and NEN have cooperated under the shared "NEN" name since 2000 and
share facilities in Delft, but — as [[NL-NEN]]'s own file already
recorded — each keeps its own governing board. This entity models NEC as
a distinct foundation rather than folding it into [[NL-NEN]], matching
the two bodies' own genuinely separate legal existence.

## Not modelled

- The **combined "NEN" cooperative arrangement** itself (as opposed to
  either foundation) — described here and on [[NL-NEN]] in prose, not as
  a third entity.

## Relationships

- `participates-in` [[EU-CENELEC]] — `confidence: high`, confirmed on
  CENELEC's own official members list.
- `participates-in` [[INTL-IEC]] — `confidence: medium`, confirmed on
  NEN's own history page, though less explicitly than the CENELEC edge.

## Sources

Listed in frontmatter, both read directly.
