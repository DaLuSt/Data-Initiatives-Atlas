---
id: PL-MOBYWATEL
type: platform
name: mObywatel
alternative_names:
  - mObywatel 2.0
  - mDowód
description: >
  Polish state citizen application, regulated by the Act of 26 May 2023 on
  the mObywatel application, which entered into force on 14 July 2023. The
  Act established mObywatel as an electronic identification means handled
  through services provided within the application, in accordance with EU
  rules on electronic identification and trust services, and introduced the
  mDowód mobile document certifying the identity and Polish citizenship of
  users within Poland in situations of mutual physical presence. Reporting
  states the application is architecturally incompatible with the eIDAS 2.0
  regulation and cannot function as a European Digital Identity Wallet, that
  adapting it has been deemed technically impossible, and that the Ministry
  of Digital Affairs indicated new solutions would be made available by the
  end of 2026.

level: national
country: PL
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2023-07-14
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - PL-COI
  - PL-MC
related_entities:
  - EU-EIDAS2
  - EU-EIDAS
  - EU-EUDI-WALLET
  - PL-COI
  - PL-MC
  - FR-FRANCECONNECT
  - DE-BUNDID
  - ES-CLAVE
relationships:
  - type: maintained-by
    target: PL-MC
    source: fact
    evidence: "Confirmed by reading lexlege.pl's own consolidated text of the mObywatel Act directly (2026-08-26): Article 19 provides that 'Minister właściwy do spraw informatyzacji udostępnia, utrzymuje oraz zapewnia rozwój aplikacji mObywatel' (the minister responsible for digitalisation provides, maintains and ensures development of the mObywatel application), and Article 20 makes that same minister the personal-data administrator for its users. This closes the gap this entity previously flagged: 'which body is its legal operator was not established.' Confirmed independently by gov.pl's own mObywatel 2.0 launch article, read directly, which describes the Minister of Digitalisation, Janusz Cieszyński, presenting the application's development — the Ministry of Digital Affairs is the constant across both the 2023 launch and the Act's own current text."
    confidence: medium
    valid_from: 2023-07-14
    valid_until: null
  - type: related-to
    target: EU-EIDAS2
    source: fact
    evidence: "Confirmed by reading biznesinfo.pl directly (2026-08-26): 'Architektura mObywatela opiera się na rozwiązaniach, które są zasadniczo różne od technicznych wymagań UE' (mObywatel's architecture relies on solutions fundamentally different from the EU's technical requirements) — the EU mandates decentralised protocols and specific cryptographic standards for selective data disclosure, while mObywatel uses proprietary protocols; some modules may need complete reconstruction. Without full compatibility, the article warns mObywatel risks becoming a 'digital island', functional only within Poland. Poland must implement the EUDI Wallet by 2026. `orka.sejm.gov.pl` was not read this pass, and no ministry or Commission document confirming the incompatibility finding was found, so it still rests on press reporting alone. ATLAS NOTE: the relationship recorded is that the Regulation applies to Poland and this application cannot satisfy it. The vocabulary has no type for a requirement an entity fails to meet, so the weakest available type is used and the substance is carried in this evidence string."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Ustawa z dnia 26 maja 2023 r. o aplikacji mObywatel"
    url: "https://orka.sejm.gov.pl/proc9.nsf/ustawy/3050_u.htm"
    publisher: "Sejm Rzeczypospolitej Polskiej"
  - title: "Ustawa o aplikacji mObywatel (tekst skonsolidowany)"
    url: "https://lexlege.pl/ustawa-o-aplikacji-mobywatel/"
    publisher: "LexLege"
    accessed: "2026-08-26"
  - title: "mObywatel — Portal Gov.pl"
    url: "https://www.gov.pl/web/mobywatel"
    publisher: "Ministerstwo Cyfryzacji"
    accessed: "2026-08-26"
  - title: "Nowa jakość cyfrowych usług publicznych — startuje mObywatel 2.0"
    url: "https://www.gov.pl/web/cyfryzacja/nowa-jakosc-cyfrowych-uslug-publicznych--startuje-mobywatel-20"
    publisher: "Ministerstwo Cyfryzacji"
    accessed: "2026-08-26"
  - title: "Unijny portfel EUDI a przyszłość polskiej aplikacji"
    url: "https://www.biznesinfo.pl/unia-wprowadza-cyfrowa-tozsamosc-co-to-oznacza-dla-mobywatela-i-twoich-dokumentow-kp-wds-230226"
    publisher: "Biznes Info"
    accessed: "2026-08-26"
---

# mObywatel

> **Verified 2026-08-26.** Four of five cited pages were read directly.
> The Act's own text names its legal operator — a gap this entity
> previously flagged as unresolved — and independent press reporting
> corroborates the eIDAS2 incompatibility finding in more technical
> detail than before. `orka.sejm.gov.pl` was not read this pass.

## Description

mObywatel is the Polish state citizen application, regulated by the **Act of
26 May 2023**, in force from **14 July 2023**. The Act established it as an
**electronic identification means** delivered through services within the
application, and introduced **mDowód** — a mobile document certifying
identity and Polish citizenship **within Poland**, in situations of mutual
physical presence.

## The first sourced eIDAS2 link in the Atlas, and it is a failure

Four batches have recorded the same gap. [[FR-FRANCECONNECT]] predicted it
would *"become a factual question rather than a modelling one"*;
[[ES-CLAVE]] recorded that the deadline was roughly four months out with
**no country in the Atlas linked to [[EU-EIDAS2]]**.

Poland closes it, and the content is negative:

- mObywatel is **architecturally incompatible** with eIDAS 2.0;
- it **cannot function as a European Digital Identity Wallet**;
- adapting it has been **deemed technically impossible**;
- Poland must implement the wallet **by 2026**;
- the ministry says **new solutions by the end of 2026**.

So the first national system in the Atlas connected to the wallet regulation
is one that **must be replaced to comply with it**.

## The Atlas cannot say that, and this is the sixth time

The relationship recorded is `related-to` at `confidence: low` — the weakest
type available — with the substance written into the `evidence` string.

What the sources describe is: *a regulation applies to this member state, and
this national system cannot satisfy it.* No relationship type expresses a
requirement an entity **fails** to meet:

- `implements-requirement-from` asserts the opposite;
- `governed-by` implies the arrangement works;
- `depends-on`, `based-on`, `derived-from` are all plainly wrong.

The register batch found three shapes of missing vocabulary and the UN batch
two. **This is a sixth**, and it is the one with the shortest fuse: the
deadline is months away and five other national identity systems have no
eIDAS2 edge at all — not because they comply, but because nothing has been
read about them either way.

`progress/backlog.md` already carries *"propose relationship types for data
movement"* as the top vocabulary item. This adds a distinct need:
**non-compliance, or an obligation not yet met.**

## Four national identity architectures

| | Poland | France | Germany | Spain |
|---|---|---|---|---|
| Entity | **mObywatel** | [[FR-FRANCECONNECT]] | [[DE-BUNDID]] | [[ES-CLAVE]] |
| Model | **state app with an in-app mobile document** | identity **federation** | central **citizen account** | **credential scheme** + certificates |
| Physical-presence use | **yes — mDowód, in-person within Poland** | no | no | no |
| eIDAS2 edge | **yes — negative** | none | none | none |

mObywatel is the only one of the four whose primary artefact is a **document
shown in person**, rather than a login. That is a different conception of
what a national digital identity is for, and it may be part of why the
architecture does not map onto a wallet.

**No relationship between the four is asserted.** Four national solutions to
a shared problem is still not a relationship — the position taken since
[[FR-FRANCECONNECT]].

## Who operates it, now established

[[PL-COI]] is sourced as maintaining mObywatel among the state IT systems it
protects, develops and maintains, but the Act itself names a different
answer for who **operates** it. Reading the Act's own consolidated text
directly this pass: Article 19 makes the minister responsible for
digitalisation — [[PL-MC]] — the body that "udostępnia, utrzymuje oraz
zapewnia rozwój aplikacji mObywatel" (provides, maintains and ensures
development of the application), and Article 20 makes the same minister
the personal-data administrator for its users. The `maintained-by` edge
this entity previously withheld is now asserted, to [[PL-MC]] — COI's
systems-level role and the Ministry's legal-operator role are not in
tension, just two different questions the sources answer differently.

## Relationships

- `maintained-by` [[PL-MC]] — confirmed this pass.
- `related-to` [[EU-EIDAS2]] — see above. **Read the evidence string, not
  the type.**

## Sources

Listed in frontmatter, four of five read directly this pass. `orka.sejm.gov.pl`
was not attempted. ⚠ The incompatibility finding still rests on **press
reporting only**; no ministry or Commission document states it among the
sources found, which is why the edge is `confidence: low`.
