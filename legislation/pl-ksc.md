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
  into force on 3 April 2026. Poland exceeded the 17 October 2024
  transposition deadline and is in proceedings before the Court of Justice
  of the European Union. The amendment expands the scope from roughly 400 to
  roughly 42,000 entities, replaces administrative designation with
  self-identification, introduces a distinction between critical and
  important entities, makes management personally responsible, and extends
  obligations across the supply chain to subcontractors. Entities have six
  months to register and twelve months to implement a full security
  management system, with self-assessment by 3 October 2026 and registration
  through the S46 system, and penalties up to ten million euro.

level: national
country: PL
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2026-04-03
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - EU-NIS2
  - NL-CBW
  - DE-NIS2UMSUCG
  - BE-NIS2-WET
  - FR-NIS2-LOI
  - ES-LCGC
relationships:
  - type: implements-requirement-from
    target: EU-NIS2
    source: fact
    evidence: "The amendment to the Act on the National Cybersecurity System (KSC), implementing the NIS2 directive, came into force on 3 April 2026; Poland exceeded the transposition deadline of 17 October 2024 and is in proceedings before the Court of Justice of the European Union. The amendment expands scope from about 400 to about 42,000 entities in Poland, replaces administrative decisions with self-identification, introduces the critical/important entity distinction, and cascades obligations across the supply chain (itwiz.pl 'Nowelizacja ustawy o KSC zaczyna obowiazywac'; gov.pl/web/baza-wiedzy 'Nowelizacja ustawy o krajowym systemie cyberbezpieczenstwa'; trecom.pl; legalgeek.pl). NOT READ — search-only."
    confidence: medium
    valid_from: 2026-04-03
    valid_until: null

sources:
  - title: "Nowelizacja ustawy o krajowym systemie cyberbezpieczeństwa — Baza wiedzy"
    url: "https://www.gov.pl/web/baza-wiedzy/nowelizacja-ustawy-o-krajowym-systemie-cyberbezpieczenstwa"
    publisher: "Portal Gov.pl"
  - title: "Nowelizacja ustawy o KSC zaczyna obowiązywać — rusza harmonogram wdrożenia NIS2 w Polsce"
    url: "https://itwiz.pl/nowelizacja-ustawy-o-ksc-zaczyna-obowiazywac-rusza-harmonogram-wdrozenia-nis2-w-polsce/"
    publisher: "ITwiz"
  - title: "Ustawa o KSC w 2026 roku: Jak polskie prawo wdraża NIS 2?"
    url: "https://www.trecom.pl/ustawa-o-ksc-w-2026-roku-jak-polskie-prawo-wdraza-nis-2/"
    publisher: "Trecom"
  - title: "Ustawa KSC 2026 — co zmienia nowelizacja NIS2"
    url: "https://legalgeek.pl/en/blog/nis2-ksc-2026-wprowadzenie/"
    publisher: "LegalGeek"
---

# KSC — Ustawa o krajowym systemie cyberbezpieczeństwa

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The KSC Act establishes Poland's national cybersecurity system. Originally
of 2018, it was **amended to implement [[EU-NIS2]]**, with the amendment in
force from **3 April 2026**.

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

## A sixth NIS2 state, and a kind the Atlas had not seen

| Country | Instrument | State |
|---|---|---|
| Belgium | [[BE-NIS2-WET]] | in force 18 Oct 2024 |
| Germany | [[DE-NIS2UMSUCG]] | in force 6 Dec 2025 — **amends** [[DE-BSIG]] |
| Netherlands | [[NL-CBW]] | in force 15 Aug 2026 |
| France | [[FR-NIS2-LOI]] | **`unknown`** — sources contradict each other |
| Spain | [[ES-LCGC]] | **`proposed`** — still a draft |
| **Poland** | **this act** | **in force 3 Apr 2026 — and before the CJEU for the delay** |

Five countries gave five states. Poland gives a sixth that is **not on the
done/not-done axis at all**: the instrument is in force *and* the member
state is in infringement proceedings over having been late.

`status: active` is correct and carries none of that. The Atlas has no field
for "in force, following infringement proceedings", and the CJEU case
appears only in the `evidence` string and this prose. It is a different
shape from Spain's — Spain drew a **reasoned opinion**, the stage *before*
referral; Poland has been **referred**.

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

**No Polish cybersecurity authority.** CSIRT NASK, CSIRT GOV and CSIRT MON
are the operational bodies of the national system and **none was
researched**. Poland therefore joins the Netherlands as a country whose
cybersecurity legislation is modelled and whose cyber authority is not —
see [[DOMAIN-CYBERSECURITY]], which now records two such countries out of
six rather than one.

**No 2018 original as a separate entity.** This entity is the act as
amended, dated from the amendment's entry into force. Whether the 2018
original warrants its own entity is the same question [[NL-WBNI]] /
[[NL-CBW]] answered differently — there the predecessor is separate.

## Relationships

- `implements-requirement-from` [[EU-NIS2]], valid from 3 April 2026.

## Sources

Listed in frontmatter. Only one is a government source; the other three are
industry and legal commentary, which is why `confidence` is medium and the
CJEU proceedings in particular need a primary citation.
