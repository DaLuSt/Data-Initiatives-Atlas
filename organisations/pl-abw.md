---
id: PL-ABW
type: organisation
name: Agencja Bezpieczeństwa Wewnętrznego
alternative_names:
  - ABW
  - Internal Security Agency
description: >
  Poland's civilian internal security service, responsible for protecting
  the internal security of the state and its constitutional order. Its head
  reports directly to the Prime Minister. It operates under the Act of
  24 May 2002 on the Internal Security Agency and the Foreign Intelligence
  Agency, the same act that constitutes the AW.

level: national
country: PL
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2002-05-24
end_date: null
last_verified: "2026-09-06"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - PL-UABWAW-2002
  - PL-KSC
  - PL-AW
  - PL-SKW
  - PL-SWW
  - PL-KSS
relationships:
  - type: implements
    target: PL-KSC
    source: fact
    evidence: "CSIRT GOV is the Computer Security Incident Response Team operating at the national level, led by the Head of the Agencja Bezpieczeństwa Wewnętrznego; Poland has three CSIRT teams at the national level under the national cybersecurity system — CSIRT GOV, CSIRT MON and CSIRT NASK. nask.pl's own page on its Cybersecurity Centre, read directly (2026-08-26), corroborates the three-way split, describing CSIRT NASK's own remit as coordinating incidents from entities not covered by the other two national CSIRTs. CSIRT GOV's own citations (csirt.gov.pl, cyberpolicy.nask.pl, archiwum.rcb.gov.pl) were not read this pass."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: PL-UABWAW-2002
    source: fact
    evidence: "Confirmed by reading bip.abw.gov.pl's own pages directly (2026-08-26): its list of governing legislation names the Act of 24 May 2002 as ABW's principal legal act, and its College for Special Services page separately confirms ABW's head sits on that College alongside AW, CBA, SKW and SWW. aw.gov.pl's own 'Ramy prawne' page, also read directly, confirms the same Act as AW's basis. `isap.sejm.gov.pl`, which would carry the Act's own text, is genuinely CAPTCHA-blocked, confirmed on multiple attempts this pass."
    confidence: medium
    valid_from: 2002-05-24
    valid_until: null

sources:
  - title: "Ustawa z dnia 24 maja 2002 r. o Agencji Bezpieczeństwa Wewnętrznego oraz Agencji Wywiadu (currently CAPTCHA-blocked)"
    url: "https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=wdu20020740676"
    publisher: "Internetowy System Aktów Prawnych (ISAP), Sejm RP"
  - title: "Ustawa o Agencji Bezpieczeństwa Wewnętrznego oraz Agencji Wywiadu"
    url: "https://bip.abw.gov.pl/bip/akty-prawne/ustawy/36,Ustawa-o-Agencji-Bezpieczenstwa-Wewnetrznego-oraz-Agencji-Wywiadu.html"
    publisher: "Agencja Bezpieczeństwa Wewnętrznego (BIP)"
    accessed: "2026-08-26"
  - title: "Kolegium ds. służb specjalnych"
    url: "https://bip.abw.gov.pl/bip/nadzor-i-kontrola/kolegium-ds-sluzb-spec/18,Kolegium-ds-sluzb-specjalnych.html"
    publisher: "Agencja Bezpieczeństwa Wewnętrznego (BIP)"
    accessed: "2026-08-26"
---

# Agencja Bezpieczeństwa Wewnętrznego (ABW)

> **Verified 2026-08-26.** Two of three cited pages were read directly.
> `isap.sejm.gov.pl` remains genuinely CAPTCHA-blocked, confirmed on
> multiple attempts across this batch.
>
> **Updated 2026-09-06**: cross-references a documented negative added on
> [[PL-KSS]] — the ECHR found Poland's Anti-Terrorism Act gives ABW's
> secret-surveillance powers no independent-body review.

## Description

The ABW protects the **internal** security of the Polish state and its
constitutional order. Its head reports **directly to the Prime Minister** —
not through a line ministry, which distinguishes the Polish civilian
services from the German, Dutch and French arrangement.

## Poland's four services, two acts

Poland pairs its services and legislates them in pairs:

| Act | Services | Sphere |
|---|---|---|
| [[PL-UABWAW-2002]] | ABW, [[PL-AW]] | Civilian |
| [[PL-USKWSWW-2006]] | [[PL-SKW]], [[PL-SWW]] | Military |

Within each pair the split is **internal security vs. foreign intelligence**
— ABW/SKW inward, AW/SWW outward. It is the most symmetrical structure in
this batch: four services, two acts, one axis repeated twice.

## The ABW is also a national CSIRT

**CSIRT GOV is led by the Head of the ABW.** It is one of the three
national-level CSIRTs in Poland's national cybersecurity system — alongside
CSIRT MON and CSIRT NASK — established under [[PL-KSC]], which was already
an Atlas entity.

Its remit under that act is specific: incidents at entities critical to the
continuity of the state in the public finance sector, entities subordinate
to and supervised by the Prime Minister, the National Bank of Poland, Bank
Gospodarstwa Krajowego, and entities whose systems appear in the register of
critical infrastructure.

The edge is `implements`, not `governed-by`. [[PL-KSC]] does not constitute
the ABW — [[PL-UABWAW-2002]] does — but the ABW *operationalises* part of
the system that act establishes.

It is one of four edges in this batch connecting the national-security
cluster to the Atlas that already existed, and the only one running to a
cyber-security statute rather than to a data-protection act or a parent body.

## No independent review of its secret-surveillance powers, per the ECHR

**Added 2026-09-06.** [[PL-KSS]] records a documented negative closing a
long-open question: does Poland have an independent legality-review body
comparable to [[FR-CNCTR]] or [[NL-TIB]]? The European Court of Human
Rights's own Registrar press release (ECHR 135 (2024), *Pietrzak and
Bychawska-Siniarska and Others v. Poland*, 28 May 2024), read directly,
names the ABW specifically: under the Anti-Terrorism Act, "neither the
imposition of a secret-surveillance measure nor its application in the
initial three-month period was subject to any authorisation or review by
an independent body that did not include employees of the ABW conducting
the surveillance." See [[PL-KSS]] for the full finding.

## Not modelled

- **CBA** (Centralne Biuro Antykorupcyjne), named by the sources among the
  services under the College for Special Services. It is an anti-corruption
  bureau rather than an intelligence service, and its current status was not
  established.
- **SOP** (Służba Ochrony Państwa), the state protection service.
- The **Kolegium do Spraw Służb Specjalnych**, the government-side
  coordinating college, as distinct from the parliamentary [[PL-KSS]].

## Relationships

- `governed-by` [[PL-UABWAW-2002]].
- `implements` [[PL-KSC]].

## Sources

Listed in frontmatter, two of three read directly this pass.
