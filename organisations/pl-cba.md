---
id: PL-CBA
type: organisation
name: Centralne Biuro Antykorupcyjne
alternative_names:
  - CBA
  - Central Anti-Corruption Bureau
description: >
  Polish special service for combating corruption in public and economic
  life, particularly in state and local-government institutions, and for
  combating activity harmful to the state's economic interests. Its Head
  is a central government administration body, appointed for a four-year
  term by and supervised by the Prime Minister, and is subject to Sejm
  oversight through the Committee for Special Services.

level: national
country: PL
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2006-06-09
end_date: null
last_verified: "2026-09-06"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - PL-USTAWA-CBA-2006
  - PL-KSS
  - PL-ABW
  - PL-AW
  - PL-SKW
  - PL-SWW
relationships:
  - type: governed-by
    target: PL-USTAWA-CBA-2006
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP (PL-ABW's and PL-KSS's own 'Not modelled' sections). Confirmed by reading cba.gov.pl's own 'O nas' page directly (2026-09-06): 'CBA operates under the ustawa z dnia 9 czerwca 2006 r. o Centralnym Biurze Antykorupcyjnym.' The Act's own consolidated text, read directly via its own hosted PDF, confirms this in Article 1."
    confidence: high
    valid_from: 2006-06-09
    valid_until: null
  - type: part-of
    target: PL
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. Confirmed by reading cba.gov.pl's own 'O nas' page directly (2026-09-06): 'Szef CBA jest centralnym organem administracji rządowej, nadzorowanym przez Prezesa Rady Ministrów' (the Head of CBA is a central government administration body, supervised by the Prime Minister)."
    confidence: high
    valid_from: 2006-06-09
    valid_until: null

sources:
  - title: "O nas"
    url: "https://www.cba.gov.pl/pl/o-nas"
    publisher: "Centralne Biuro Antykorupcyjne (CBA)"
    accessed: "2026-09-06"
  - title: "Dz.U.2012.621 — Ustawa z dnia 9 czerwca 2006 r. o Centralnym Biurze Antykorupcyjnym (tekst jednolity)"
    url: "https://bip.cba.gov.pl/ftp/prawo/Ustawa_o_CBA_-_tekst_jednolity.pdf"
    publisher: "Centralne Biuro Antykorupcyjne (BIP)"
    accessed: "2026-09-06"
---

# Centralne Biuro Antykorupcyjne (CBA)

> **Created 2026-09-06**, closing a gap flagged on both [[PL-ABW]] and
> [[PL-KSS]]: CBA was repeatedly named as one of Poland's five special
> services but never modelled. cba.gov.pl's own page and the Act's own
> consolidated text (read via its hosted PDF's page images) agree.

## Description

Confirmed by reading cba.gov.pl's own "O nas" page directly: CBA "jest
służbą specjalną powołaną do zwalczania korupcji w życiu publicznym i
gospodarczym" (is a special service established to combat corruption in
public and economic life), particularly in state and local-government
institutions, and to combat activity harmful to the state's economic
interests. The Act's own text, read directly, gives the same description
verbatim in Article 1(1) and reserves the CBA name exclusively to this
body.

**The Head of CBA is a central government administration body**,
confirmed verbatim on cba.gov.pl: "Szef CBA jest centralnym organem
administracji rządowej, nadzorowanym przez Prezesa Rady Ministrów" — a
central organ of government administration, supervised by the Prime
Minister. A WebSearch cross-check (not independently confirmed by a
directly-read page this pass) describes the appointment process: a
four-year term, appointed and dismissed by the Prime Minister after
seeking the opinions of the President, the College for Special Services
and the Sejm's Committee for Special Services — the same [[PL-KSS]]
already modelled.

CBA employs more than **1,300** officers and civilian staff across 23
organisational units, per cba.gov.pl's own page, and is financed from the
state budget (confirmed directly in the Act's own Article 4(1)).

## The fifth service, named twice before this pass

Both [[PL-ABW]] (2026-08-26) and [[PL-KSS]] (2026-08-26) named CBA as
missing while describing it correctly as one of Poland's services under
the College for Special Services and within KSS's parliamentary
oversight remit. Neither created it. This entity closes both findings at
once.

## Not modelled

- The **appointment procedure's exact statutory citation** — the
  four-year term and consultation requirement are corroborated only by
  WebSearch, not read directly in the Act's own appointment articles this
  pass.
- CBA's **substantive investigative powers and case history** — out of
  scope for a single-entity closure pass.

## Relationships

- `governed-by` [[PL-USTAWA-CBA-2006]].
- `part-of` [[PL]] — a scope anchor.

## Sources

Listed in frontmatter, both read directly 2026-09-06.
