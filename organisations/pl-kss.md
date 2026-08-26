---
id: PL-KSS
type: organisation
name: Komisja do Spraw Służb Specjalnych
alternative_names:
  - KSS
  - Sejm Committee for Special Services
description: >
  Standing committee of the Polish Sejm for the oversight of the special
  services — ABW, AW, CBA, SKW and SWW. Sources disagree on its maximum
  size (seven per Wikipedia, eight per a Regulamin mirror); it sits in
  closed session and handles classified material under the 2010 act on
  protecting classified information. It has existed in this form since
  29 September 1995 and its basis is the Sejm's standing orders rather
  than a statute.

level: national
country: PL
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 1995-09-29
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - PL-ABW
  - PL-AW
  - PL-SKW
  - PL-SWW
relationships:
  - type: applies-to
    target: PL-ABW
    source: fact
    evidence: "Confirmed by reading pl.wikipedia.org's own article and arslege.pl's own mirror of the Sejm's Regulamin directly (2026-08-26): the Komisja do Spraw Służb Specjalnych is a standing parliamentary commission for controlling ABW, AW, CBA, SKW and SWW, in closed session (arslege.pl, Article 139.1: 'Posiedzenia Komisji do Spraw Służb Specjalnych są zamknięte'). `sejm.gov.pl` itself is genuinely CAPTCHA-blocked."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: PL-AW
    source: fact
    evidence: "Confirmed by reading pl.wikipedia.org's own article directly (2026-08-26): the Komisja do Spraw Służb Specjalnych is the specialised parliamentary institution for controlling ABW, AW, CBA, SKW and SWW. `sejm.gov.pl` itself is genuinely CAPTCHA-blocked."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: PL-SKW
    source: fact
    evidence: "Confirmed by reading pl.wikipedia.org's own article directly (2026-08-26): the Komisja do Spraw Służb Specjalnych is the specialised parliamentary institution for controlling ABW, AW, CBA, SKW and SWW. `sejm.gov.pl` itself is genuinely CAPTCHA-blocked."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: PL-SWW
    source: fact
    evidence: "Confirmed by reading pl.wikipedia.org's own article directly (2026-08-26): the Komisja do Spraw Służb Specjalnych is the specialised parliamentary institution for controlling ABW, AW, CBA, SKW and SWW. `sejm.gov.pl` itself is genuinely CAPTCHA-blocked."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Komisja do Spraw Służb Specjalnych (KSS) (currently CAPTCHA-blocked)"
    url: "https://www.sejm.gov.pl/sejm10.nsf/agent.xsp?symbol=KOMISJA&NrKadencji=10&KodKom=KSS"
    publisher: "Sejm Rzeczypospolitej Polskiej"
  - title: "Komisja do Spraw Służb Specjalnych"
    url: "https://pl.wikipedia.org/wiki/Komisja_do_Spraw_S%C5%82u%C5%BCb_Specjalnych"
    publisher: "Wikipedia"
    accessed: "2026-08-26"
  - title: "Rozdział 12. Komisja do spraw Służb Specjalnych i postępowanie w komisji — Regulamin Sejmu"
    url: "https://arslege.pl/regulamin-sejmu-rzeczypospolitej-polskiej/k374/s3572/"
    publisher: "arslege.pl (Regulamin Sejmu RP)"
    accessed: "2026-08-26"
---

# Komisja do Spraw Służb Specjalnych (KSS)

> **Re-verified 2026-08-26, with a conflict found and recorded rather
> than resolved.** Two of three cited pages were read directly.
> `sejm.gov.pl` itself remains genuinely CAPTCHA-blocked. Wikipedia and
> arslege.pl's own mirror of the Sejm's current Regulamin **disagree on
> the Commission's size** — see below.

## Description

The KSS is the Sejm's standing committee for oversight of the Polish special
services. The sources describe it as **the primary body** for monitoring
intelligence activity by the legislature, precisely because ordinary
parliamentary tools do not reach these bodies.

Its design is all constraint:

- **No more than seven or eight deputies** — the sources disagree; see below.
- **Closed sessions**, confirmed by reading arslege.pl's own text of Article
  139(1) of the Regulamin directly: "Posiedzenia Komisji do Spraw Służb
  Specjalnych są zamknięte."
- **Members must hold security clearances** for the classified material the
  Commission handles — arslege.pl's own text, read directly, ties this to
  the Act of 5 August 2010 on the protection of classified information
  (Article 138(4)) rather than stating a standalone clearance requirement
  in those words.

## ⚠ A conflict between two sources on the Commission's size

pl.wikipedia.org, read directly, gives "nie więcej niż siedmiu posłów
(dziewięciu w latach 2001–2015)" — no more than **seven** deputies (nine
between 2001 and 2015). arslege.pl, read directly and presented as a
current mirror of the Sejm's own Regulamin, gives Article 137(1) as "nie
więcej niż 8 posłów" — no more than **eight**.

Both were read this pass; neither is obviously stale, and `sejm.gov.pl`
itself — the authoritative source — is CAPTCHA-blocked. Rather than pick
one, the Atlas records the conflict, following the same discipline
applied to [[PT-LEI-26-2016]]'s standalone-legislation question.

Its functions include opinions on draft laws affecting the services, review
of the heads' annual reports, and opinions on appointments of heads and
deputy heads.

## Why this entity carries no `governed-by`

Every other oversight body in this batch is constituted by a **statute** —
[[DE-PKGRG]] for [[DE-PKGR]], [[BE-TOEZICHTSWET-1991]] for
[[BE-COMITE-I]], [[GB-JSA-2013]] for [[GB-ISC]], [[NL-WIV-2017]] for
[[NL-TIB]] and [[NL-CTIVD]].

The KSS is not. Its basis is **Chapter 12 of the Sejm's Regulamin** — the
chamber's own standing orders. That is a real difference in kind, not a gap
in the research: an oversight body created by the rules of the house it sits
in can be reorganised by that house, where one created by statute cannot.

No law entity is created for the Regulamin, because a chamber's standing
orders are not legislation in the sense the Atlas's `law` type means. The
absence of the edge **is** the finding, and it is why this entity's body says
so at length rather than leaving a reader to notice the asymmetry in the
graph.

## Poland has parliamentary oversight and no independent counterpart here

Germany and the UK run parliamentary and judicial-style oversight in
parallel — [[DE-PKGR]] with [[DE-UKR]], [[GB-ISC]] with [[GB-IPCO]]. The
Atlas holds only the parliamentary half for Poland.

Whether Poland has an independent legality-review body of the [[FR-CNCTR]] or
[[NL-TIB]] kind **was not researched**. Its absence here is a coverage limit,
not a claim that none exists.

## Not modelled

- **CBA**, which the KSS also oversees. See [[PL-ABW]].
- The **Kolegium do Spraw Służb Specjalnych** — a government-side
  coordinating college that includes the KSS chair, and is not the same body
  as this committee.

## Relationships

- `applies-to` [[PL-ABW]], [[PL-AW]], [[PL-SKW]] and [[PL-SWW]].

## Sources

Listed in frontmatter, two of three read directly this pass.
`sejm.gov.pl` remains genuinely CAPTCHA-blocked.
