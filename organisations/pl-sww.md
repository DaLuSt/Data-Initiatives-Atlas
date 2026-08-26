---
id: PL-SWW
type: organisation
name: Służba Wywiadu Wojskowego
alternative_names:
  - SWW
  - Military Intelligence Service
description: >
  Poland's military intelligence service, constituted together with the
  Military Counterintelligence Service by the Act of 9 June 2006 on the
  Military Counterintelligence Service and the Military Intelligence
  Service. It is one of the five Polish special services represented on the
  College for Special Services.

level: national
country: PL
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2006-06-09
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - PL-USKWSWW-2006
  - PL-SKW
  - PL-AW
  - PL-KSS
relationships:
  - type: governed-by
    target: PL-USKWSWW-2006
    source: fact
    evidence: "Confirmed by reading bip.abw.gov.pl's own College for Special Services page directly (2026-08-26): 'Szef ABW, Szef AW, Szef Centralnego Biura Antykorupcyjnego, Szef Służby Kontrwywiadu Wojskowego, Szef Służby Wywiadu Wojskowego' names SWW's head among the College's members. pl.wikipedia.org's article on the Sejm's oversight committee, also read directly, confirms this Act constitutes both SKW and SWW. Neither page carries the Act's own text or a Dz.U. citation."
    confidence: medium
    valid_from: 2006-06-09
    valid_until: null

sources:
  - title: "Kolegium ds. służb specjalnych"
    url: "https://bip.abw.gov.pl/bip/nadzor-i-kontrola/kolegium-ds-sluzb-spec/18,Kolegium-ds-sluzb-specjalnych.html"
    publisher: "Agencja Bezpieczeństwa Wewnętrznego (BIP)"
    accessed: "2026-08-26"
  - title: "Komisja do Spraw Służb Specjalnych"
    url: "https://pl.wikipedia.org/wiki/Komisja_do_Spraw_S%C5%82u%C5%BCb_Specjalnych"
    publisher: "Wikipedia"
    accessed: "2026-08-26"
---

# Służba Wywiadu Wojskowego (SWW)

> **Verified 2026-08-26.** Both cited pages were read directly. Both
> describe the service rather than being published by it — the weak
> sourcing this entity already flagged stands.

## Description

The SWW is Poland's **military intelligence** service — foreign collection
in the military sphere — paired with [[PL-SKW]] under
[[PL-USKWSWW-2006]].

It is the counterpart of France's [[FR-DRM]]. Germany has no separate body
in this role among its three federal services; the function sits with
[[DE-BND]].

## The 2006 pair completed a four-service structure

Poland's civilian services were created in 2002 and its military services in
2006, four years apart, on the same internal/external axis. The result is
the only fully symmetrical intelligence structure in the Atlas:

```
            civilian              military
internal    PL-ABW      2002      PL-SKW      2006
external    PL-AW       2002      PL-SWW      2006
```

## ⚠ `coverage: low`

The same limitation recorded on [[PL-SKW]] applies: no source published by
the service itself was found.

## Relationships

- `governed-by` [[PL-USKWSWW-2006]].

## Sources

Listed in frontmatter, both read directly this pass.
