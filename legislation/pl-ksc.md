---
id: PL-KSC
type: law
name: Ustawa o krajowym systemie cyberbezpieczeństwa
alternative_names:
  - Ustawa o KSC
  - KSC
  - National Cybersecurity System Act
description: >
  Polish act establishing the national cybersecurity system, originally of
  2018, as amended to implement the NIS2 Directive. The NIS2 amendment came
  into force on 3 April 2026. Poland missed the 17 October 2024
  transposition deadline and received a European Commission letter of
  formal notice alongside 22 other member states — the initial stage of
  the EU infringement procedure, not a referral to the Court of Justice.
  The amendment expands the scope from roughly 400 to roughly 42,000
  entities, replaces administrative designation with self-identification,
  introduces a distinction between critical and important entities, makes
  management personally responsible, and extends obligations across the
  supply chain to subcontractors. Entities have six months to register and
  twelve months to implement a full security management system, with
  self-assessment by 3 October 2026 and registration through the S46
  system, and penalties up to ten million euro.

level: national
country: PL
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2026-04-03
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - PL
  - EU-NIS2
  - NL-CBW
  - DE-NIS2UMSUCG
  - BE-NIS2-WET
  - FR-NIS2-LOI
  - ES-LCGC
relationships:
  - type: applies-in
    target: PL
    source: fact
    evidence: "Confirmed by reading gov.pl's own knowledge-base page directly (2026-08-26): 'Nowelizacja KSC weszła w życie 3 kwietnia 2026 roku' (the KSC amendment entered into force on 3 April 2026). Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: implements-requirement-from
    target: EU-NIS2
    source: fact
    evidence: "Confirmed by reading gov.pl's own knowledge-base page, itwiz.pl and trecom.pl directly (2026-08-26): the amendment to the Act on the National Cybersecurity System (KSC), implementing NIS2, entered into force 3 April 2026 (gov.pl's own date; trecom.pl separately reports 2 April, a one-day discrepancy not resolved this pass in the government source's favour), expanding scope to new sectors (ICT services management, electronic communications, space, postal services, manufacturing, chemicals, food, waste management and nuclear facilities per gov.pl) with self-assessment and registration via the S46 system due by 3 October 2026. **Correction of a prior claim**: this entity previously stated Poland 'is in proceedings before the Court of Justice of the European Union.' None of the three sources read this pass, nor the European Commission's own digital-strategy.ec.europa.eu page (also read directly), support that. The Commission's page instead confirms Poland was among 23 member states sent a **letter of formal notice** — explicitly the first stage of the infringement procedure ('these countries now have two months to respond... in the absence of a satisfactory response, the Commission may decide to issue a reasoned opinion') — not a referral to the Court of Justice. No source read this pass confirms Poland reached the reasoned-opinion or referral stage before completing transposition."
    confidence: medium
    valid_from: 2026-04-03
    valid_until: null

sources:
  - title: "Nowelizacja ustawy o krajowym systemie cyberbezpieczeństwa — Baza wiedzy"
    url: "https://www.gov.pl/web/baza-wiedzy/nowelizacja-ustawy-o-krajowym-systemie-cyberbezpieczenstwa"
    publisher: "Portal Gov.pl"
    accessed: "2026-08-26"
  - title: "Nowelizacja ustawy o KSC zaczyna obowiązywać — rusza harmonogram wdrożenia NIS2 w Polsce"
    url: "https://itwiz.pl/nowelizacja-ustawy-o-ksc-zaczyna-obowiazywac-rusza-harmonogram-wdrozenia-nis2-w-polsce/"
    publisher: "ITwiz"
    accessed: "2026-08-26"
  - title: "Ustawa o KSC w 2026 roku: Jak polskie prawo wdraża NIS 2?"
    url: "https://www.trecom.pl/ustawa-o-ksc-w-2026-roku-jak-polskie-prawo-wdraza-nis-2/"
    publisher: "Trecom"
    accessed: "2026-08-26"
  - title: "Commission calls on 23 Member States to fully transpose the NIS2 Directive"
    url: "https://digital-strategy.ec.europa.eu/en/news/commission-calls-23-member-states-fully-transpose-nis2-directive"
    publisher: "European Commission — Shaping Europe's digital future"
    accessed: "2026-08-26"
  - title: "Ustawa KSC 2026 — co zmienia nowelizacja NIS2"
    url: "https://legalgeek.pl/en/blog/nis2-ksc-2026-wprowadzenie/"
    publisher: "LegalGeek"
---

# KSC — Ustawa o krajowym systemie cyberbezpieczeństwa

> **Re-verified 2026-08-26, and one claim corrected.** Three of four cited
> pages were read directly, plus the European Commission's own page on
> the NIS2 infringement track. The transposition facts (dates, scope,
> S46 deadlines) all check out. **The CJEU claim did not**: this entity
> previously said Poland "is in proceedings before the Court of Justice."
> The Commission's own page says Poland received a **letter of formal
> notice** — the first infringement stage — not a court referral. See
> below.

## Description

The KSC Act establishes Poland's national cybersecurity system. Originally
of 2018, it was **amended to implement [[EU-NIS2]]**, with the amendment in
force from **3 April 2026**, confirmed by reading gov.pl's own knowledge-base
page directly.

What the amendment changes:

- **scope from ~400 to ~42,000 entities** in Poland;
- **self-identification** replaces administrative designation;
- a distinction between **critical** and **important** entities;
- **personal responsibility of management** for implementation;
- obligations cascading **across the supply chain** to subcontractors.

Entities have **six months to register** and **twelve months** to implement
a full security management system, with self-assessment due by **3 October
2026** and registration through the **S46** system. Penalties reach **ten
million euro**.

## A sixth NIS2 state, in force despite a late start — corrected this pass

| Country | Instrument | State |
|---|---|---|
| Belgium | [[BE-NIS2-WET]] | in force 18 Oct 2024 |
| Germany | [[DE-NIS2UMSUCG]] | in force 6 Dec 2025 — **amends** [[DE-BSIG]] |
| Netherlands | [[NL-CBW]] | in force 15 Aug 2026 |
| France | [[FR-NIS2-LOI]] | **`unknown`** — sources contradict each other |
| Spain | [[ES-LCGC]] | **`proposed`** — still a draft |
| **Poland** | **this act** | **in force 3 Apr 2026, after a Commission letter of formal notice for the delay** |

Five countries gave five states. Poland gives a sixth that is **not on the
done/not-done axis at all**: the instrument is now in force, but only after
the member state missed the 17 October 2024 deadline and was named among 23
states sent a letter of formal notice by the European Commission.

**This entity previously overstated that**, saying Poland "is in proceedings
before the Court of Justice of the European Union." Re-reading this pass —
the European Commission's own digital-strategy page, read directly — found
no such thing: a letter of formal notice is the *first* stage of the EU
infringement procedure, three steps short of a Court referral (formal
notice → reasoned opinion → referral to the CJEU → judgment). Nothing read
this pass places Poland even at the reasoned-opinion stage, let alone
referred. The comparison this entity previously drew — "Spain drew a
reasoned opinion, the stage before referral; Poland has been referred" — had
the two the wrong way round: on what could be confirmed this pass, Spain's
own file records a reasoned opinion, a *later* stage than the formal notice
found here for Poland.

`status: active` is correct either way, and the Atlas still has no field for
"transposed after a delay that drew Commission attention" — but the prose
should describe the delay accurately, which it previously did not.

## The amendment question, for the third time

Poland amends an existing act, as Germany did. The Atlas's handling differs
between them:

| | Germany | Poland |
|---|---|---|
| Amending instrument | [[DE-NIS2UMSUCG]] — has its own name and is its own entity | *nowelizacja* — no separate name found, **not an entity** |
| Amended act | [[DE-BSIG]] — separate entity, left `active` | **this entity**, which is the amended act |
| Edge | `supersedes`, `confidence: low` | none needed |

The Polish case needed no workaround because the amendment has no
independent identity in the sources — the same treatment [[FR-LIL]] and
[[ES-LEY-37-2007]] received. Germany's needed one because the amending act
is separately named.

Three countries, three amendment situations, and the Atlas has now handled
them three different ways. `progress/backlog.md` carries *"decide on an
amendment relationship type"*; this is the third data point for it.

## Not modelled

**Correction: two of three national CSIRTs are now modelled.** This
section previously said none of CSIRT NASK, CSIRT GOV and CSIRT MON had
been researched — stale as of this pass. [[PL-ABW]] `implements` this
entity for CSIRT GOV and [[PL-NASK]] `implements` it for CSIRT NASK, both
added in a later batch than this entity's own creation and never
cross-referenced back here until now. Only **CSIRT MON** remains
unmodelled, because Poland's Ministry of National Defence is not an
Atlas entity.

**No 2018 original as a separate entity.** This entity is the act as
amended, dated from the amendment's entry into force. Whether the 2018
original warrants its own entity is the same question [[NL-WBNI]] /
[[NL-CBW]] answered differently — there the predecessor is separate.

## Relationships

- `applies-in` [[PL]] — anchor edge, confirmed this pass.
- `implements-requirement-from` [[EU-NIS2]], valid from 3 April 2026.
- [[PL-ABW]] and [[PL-NASK]] both carry `implements` edges pointing here.

## Sources

Listed in frontmatter. Four of five read directly this pass, including
the European Commission's own page — the primary citation the CJEU claim
needed, which is what caught the error. `legalgeek.pl` was not read this
pass.
