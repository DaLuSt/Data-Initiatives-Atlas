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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
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
    evidence: "Confirmed by reading ejustice.just.fgov.be's own official Justel text of the 1991 act directly (2026-08-27, succeeded on retry after three prior timeouts): Article 1 establishes two permanent oversight committees, one for police services and one for intelligence and security services. A second official text, also read directly (etaamb.openjustice.be, a later statute on Comité P's investigation-service staff), cites the 1991 act's own Articles 17, 20, 20bis and 22bis–22quater on committee composition, disciplinary authority and members' statutory consequences."
    confidence: high
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
  - title: "Justel — wet van 18 juli 1991"
    url: "https://www.ejustice.just.fgov.be/cgi_loi/change_lg_2.pl?language=nl&nm=1991009963&la=N"
    publisher: "Belgisch Staatsblad / FOD Justitie"
    accessed: "2026-08-27"
  - title: "Wet statuut van de directeur-generaal en van de leden van de dienst enquêtes van het Vast Comité P"
    url: "https://etaamb.openjustice.be/nl/wet_n2007018027.html"
    publisher: "etaamb / OpenJustice"
    accessed: "2026-08-27"
---

# Vast Comité van Toezicht op de inlichtingen- en veiligheidsdiensten (Comité I)

> **Verified 2026-08-27.** Comité I's own FAQ page confirms the
> `applies-to` [[BE-VSSE]] and [[BE-ADIV]] edges in substance, and two
> official texts of the governing 1991 act — ejustice.just.fgov.be's own
> Justel text (which timed out three times in the prior pass, succeeded
> on this pass's retry) and a citing etaamb.openjustice.be statute — were
> read directly, giving this entity's `governed-by` edge a genuine
> textual basis for the first time. Three of five cited pages are now
> read directly. The PDF codex of the 1991 act remains unreadable (a
> compressed binary stream) and the `wetgeving-mainmenu-7` citation
> remains dead (404).

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

- `governed-by` [[BE-TOEZICHTSWET-1991]] — confirmed this pass via the
  act's own official text; `confidence: high`.
- `applies-to` [[BE-VSSE]] and [[BE-ADIV]].

## Sources

Three of five read directly this pass: the FAQ page, ejustice.just.fgov.be's
own Justel text, and a citing etaamb.openjustice.be statute. The PDF codex
is unreadable as extracted text and the `wetgeving-mainmenu-7` page is
dead (404).
