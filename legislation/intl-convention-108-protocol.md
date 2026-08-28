---
id: INTL-CONVENTION-108-PROTOCOL
type: law
name: Additional Protocol to Convention 108 regarding supervisory authorities and transborder data flows
alternative_names:
  - ETS No. 181
  - CETS No. 181
  - Additional Protocol to Convention 108
description: >
  Council of Europe treaty opened for signature on 8 November 2001,
  supplementing Convention 108 in two respects. It requires each party to
  set up one or more supervisory authorities responsible for compliance,
  exercising their functions in complete independence and co-operating with
  one another by exchanging information; and it permits transfers of
  personal data to a recipient state or international organisation only
  where that recipient affords an adequate level of protection. Parties
  regard its substantive articles as additional articles to Convention 108
  itself.

level: international
country: null
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2001-11-08
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - INTL-CONVENTION-108
  - INTL-COE
  - EU-GDPR
  - EU-UK-ADEQUACY
relationships:
  - type: part-of
    target: INTL-CONVENTION-108
    source: fact
    evidence: "The Additional Protocol to Convention ETS No. 108 on supervisory authorities and transborder data flows, ETS No. 181, was opened for signature on 8 November 2001; parties regard its substantive articles as additional articles to the Convention (coe.int 'Convention 108 and Protocols'; coe.int 'Treaties — Data Protection'; rm.coe.int ETS 181 Explanatory Report). Confirmed independently by reading cnpd.public.lu directly (2026-08-28), Luxembourg's data protection authority, which states the Additional Protocol 'supplements Convention 108' and that Luxembourg ratified it on 24 February 2004, having ratified the Convention itself on 10 February 1988. Both coe.int pages and rm.coe.int returned HTTP 403 on retry 2026-08-28 (domain-wide block, see INTL-COE) and stay unread."
    confidence: medium
    valid_from: 2001-11-08
    valid_until: null
  - type: maintained-by
    target: INTL-COE
    source: fact
    evidence: "The Additional Protocol is a Council of Europe treaty, ETS No. 181, published in the Council of Europe treaty series and listed by the Council of Europe alongside Convention 108 and the amending protocol (coe.int 'Convention 108 and Protocols'). NOT READ — coe.int returned HTTP 403 on retry 2026-08-28 (domain-wide block, see INTL-COE)."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Convention 108 and Protocols"
    url: "https://www.coe.int/en/web/data-protection/convention108-and-protocol"
    publisher: "Council of Europe"
  - title: "European Treaty Series No. 181 — Explanatory Report"
    url: "https://rm.coe.int/16800cce56"
    publisher: "Council of Europe"
  - title: "Council of Europe conventions and rights"
    url: "https://cnpd.public.lu/en/legislation/droit-europ/conseil-europe.html"
    publisher: "Commission nationale pour la protection des données (CNPD), Luxembourg"
    accessed: "2026-08-28"
---

# Additional Protocol to Convention 108 (ETS 181)

> **Re-verification attempted 2026-08-28, stays `search-only`.** One of
> three cited sources was read directly this pass: cnpd.public.lu
> (Luxembourg's data protection authority), which confirms the Additional
> Protocol supplements Convention 108 and gives Luxembourg's own
> ratification dates for both instruments. The other two — `coe.int` and
> `rm.coe.int` — both returned HTTP 403 on retry (domain-wide block,
> confirmed again this pass; see [[INTL-COE]]). One of three is not a
> majority, so `verification` stays `search-only` rather than being
> forced.

## Description

The 2001 protocol that added the two things the 1981 Convention lacked: an
**independent supervisory authority** in every party, and a rule that data
may only leave for a jurisdiction offering **adequate** protection.

## Where two of the Atlas's biggest structures come from

This is a small treaty with an outsized footprint in the graph, because both
of its provisions became load-bearing in EU law and the Atlas already models
their descendants without holding the ancestor.

**Independent supervisory authorities.** The Atlas holds eleven national
data protection authorities — [[NL-AP]], [[DE-BFDI]], [[BE-APD]], [[FR-CNIL]],
[[ES-AEPD]], [[PL-UODO]], [[GB-ICO]], [[IE-DPC]], [[NO-DATATILSYNET]],
[[PT-CNPD]], [[LU-CNPD]] and their peers, all connected to [[EU-EDPB]]. The
requirement that such a body exist *and act in complete independence* is
here, in 2001, seventeen years before the GDPR restated it.

**Adequacy.** [[EU-UK-ADEQUACY]] is an adequacy decision. The concept — that
a transfer is permitted only where the recipient affords an adequate level of
protection — is Article 2 of this protocol.

**No relationship is asserted from any of those entities to this one.** The
descent is real and it is not stated by any source read, which is the same
call made on [[BE-DATA-GOV-BE]]/[[BE-HERGEBRUIK-WET]] and
[[DE-GOVDATA]]/[[DE-DNG]]. It is recorded here in prose instead.

## Absorbed, not superseded

[[INTL-CONVENTION-108-PLUS]] folds this protocol's substance into the
Convention itself. Until that protocol enters into force, ETS 181 remains
the operative instrument for the parties that ratified it, which is why this
entity is `active` rather than `superseded`.

## Sources

Listed in frontmatter. One of three read directly this pass —
cnpd.public.lu. Both `coe.int`/`rm.coe.int` citations remain unread
(domain-wide block; see verification note above).
