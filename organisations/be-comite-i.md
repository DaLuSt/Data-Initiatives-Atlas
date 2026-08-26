---
id: BE-COMITE-I
type: organisation
name: Vast Comité van Toezicht op de inlichtingen- en veiligheidsdiensten
alternative_names:
  - Comité I
  - Comité R
  - Standing Intelligence Agencies Review Committee
description: >
  Belgian oversight committee exercising democratic control over the
  intelligence and security services VSSE and ADIV, and — jointly with
  Comité P — over the Coordination Unit for Threat Analysis. It reports to
  Parliament and operates under the law of 18 July 1991 regulating oversight
  of the police and intelligence services.

level: national
country: BE
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - BE-TOEZICHTSWET-1991
  - BE-VSSE
  - BE-ADIV
relationships:
  - type: governed-by
    target: BE-TOEZICHTSWET-1991
    source: fact
    evidence: "The law of 18 July 1991 regulates oversight of the police and intelligence services and the Coordination Organ for Threat Analysis; two permanent oversight committees were established, one for police services and one for intelligence and security services (comiteri.be 'Wetgeving' and the consolidated codex of the 1991 act; ejustice.just.fgov.be Justel 1991009963; comitep.be 'historiek'). Not independently re-confirmed this pass — the FAQ page read confirms Comité I's oversight role in substance but does not cite the 1991 act by name; the act's own text (attempted via a different mirror on BE-TOEZICHTSWET-1991) confirms the two-committee structure directly."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: BE-VSSE
    source: fact
    evidence: "Confirmed by reading comiteri.be's FAQ page directly (2026-08-26): Comité R/I 'functions as a parliamentary supervisory body monitoring the operations, conduct, actions or failures' of VSSE, ADIV and OCAD, as 'an independent public institution, connected to the Chamber of Representatives'."
    confidence: high
    valid_from: null
    valid_until: null
  - type: applies-to
    target: BE-ADIV
    source: fact
    evidence: "Confirmed by reading comiteri.be's FAQ page directly (2026-08-26): the same parliamentary oversight covers ADIV alongside VSSE and OCAD."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Wat zijn inlichtingen- en veiligheidsdiensten?"
    url: "https://www.comiteri.be/index.php/nl/vast-comite-i/faq?view=article&id=105%3Awat-zijn-inlichtingen-en-veiligheidsdiensten&catid=10%3Anl"
    publisher: "Vast Comité I"
    accessed: "2026-08-26"
  - title: "18 juli 1991 — Wet tot regeling van het toezicht op politie- en inlichtingendiensten (codex)"
    url: "https://www.comiteri.be/images/pdf/wetgeving/WToezicht_-_LContrle_-_codex.pdf"
    publisher: "Vast Comité I"
  - title: "Wetgeving"
    url: "https://www.comiteri.be/index.php/nl/wetgeving-mainmenu-7"
    publisher: "Vast Comité I"
---

# Vast Comité van Toezicht op de inlichtingen- en veiligheidsdiensten (Comité I)

> **Re-checked 2026-08-26, still `search-only`.** Comité I's own FAQ page
> was read directly and confirms the `applies-to` [[BE-VSSE]] and
> [[BE-ADIV]] edges in substance. The PDF codex of the 1991 act could not be
> read as text (a compressed binary stream) and the `wetgeving-mainmenu-7`
> citation is now dead (404). One of three read is not a majority, so this
> entity stays `search-only`.

## Description

Comité I exercises **democratic control**, reporting to Parliament, over
[[BE-VSSE]] and [[BE-ADIV]]. Confirmed by reading Comité I's own FAQ page
directly: it is "an independent public institution, connected to the
Chamber of Representatives, and is completely neutral and impartial,"
functioning as "a parliamentary supervisory body monitoring the operations,
conduct, actions or failures" of VSSE, ADIV and OCAD.

## Two committees from one act

The law of 18 July 1991 — [[BE-TOEZICHTSWET-1991]] — created **two**
standing committees at once: Comité P for the police services and Comité I
for the intelligence and security services. Only Comité I is modelled here;
Comité P oversees bodies the Atlas does not hold.

The 1991 act was amended on **10 July 2006**, when OCAD (the Coordination
Unit for Threat Analysis) was established, to place that body under the
**joint** supervision of both committees. That joint arrangement is recorded
here but not modelled, because OCAD is not an Atlas entity.

## Belgium's clean separation of instruments

Belgium is the one country in this batch where the act constituting the
services and the act constituting their overseer are **different statutes,
seven years apart, and both modelled**:

- [[BE-WIV-1998]] constitutes [[BE-VSSE]] and [[BE-ADIV]] (1998).
- [[BE-TOEZICHTSWET-1991]] constitutes Comité I (1991).

Note the order: **the overseer's statute is the older one.** Belgium
regulated oversight of its intelligence services seven years before it gave
those services their organic act.

Elsewhere the two are fused — [[NL-WIV-2017]] constitutes the services *and*
[[NL-TIB]] and [[NL-CTIVD]] — or split differently, as in the UK, where
[[GB-ISC]] comes from [[GB-JSA-2013]] and [[GB-IPCO]] from [[GB-IPA-2016]],
both later than the agency acts.

## Relationships

- `governed-by` [[BE-TOEZICHTSWET-1991]].
- `applies-to` [[BE-VSSE]] and [[BE-ADIV]].

## Sources

One of three read directly this pass — the FAQ page. The PDF codex is
unreadable as extracted text and the `wetgeving-mainmenu-7` page is dead
(404); the same PDF and a live alternate mirror were tried again on
[[BE-TOEZICHTSWET-1991]].
