---
id: PL-AW
type: organisation
name: Agencja Wywiadu
alternative_names:
  - AW
  - Foreign Intelligence Agency
description: >
  Poland's civilian foreign intelligence agency, responsible for protecting
  the external security of the state. Its head reports directly to the Prime
  Minister. It operates under the Act of 24 May 2002 on the Internal
  Security Agency and the Foreign Intelligence Agency, the same act that
  constitutes the ABW.

level: national
country: PL
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2002-05-24
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - PL-UABWAW-2002
  - PL-ABW
  - PL-SWW
  - PL-KSS
relationships:
  - type: governed-by
    target: PL-UABWAW-2002
    source: fact
    evidence: "The Act of 24 May 2002 on the Agencja Bezpieczeństwa Wewnętrznego and the Agencja Wywiadu constitutes both agencies; the AW is responsible for protecting the external security of the state, and the Agencja Wywiadu publishes that act as its legal framework ('Ramy prawne') (aw.gov.pl 'Ramy prawne'; isap.sejm.gov.pl WDU20020740676; bip.abw.gov.pl). NOT READ — search-only."
    confidence: medium
    valid_from: 2002-05-24
    valid_until: null

sources:
  - title: "Ramy prawne"
    url: "https://aw.gov.pl/pl/o-nas/ramy-prawne/167,Ramy-prawne.html"
    publisher: "Agencja Wywiadu (AW)"
  - title: "Ustawa z dnia 24 maja 2002 r. o Agencji Bezpieczeństwa Wewnętrznego oraz Agencji Wywiadu"
    url: "https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=wdu20020740676"
    publisher: "Internetowy System Aktów Prawnych (ISAP), Sejm RP"
---

# Agencja Wywiadu (AW)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

The AW is Poland's civilian **foreign** intelligence agency, protecting the
external security of the state, with its head reporting directly to the
Prime Minister. Its internal counterpart is [[PL-ABW]].

## The act names itself after both agencies

[[PL-UABWAW-2002]] is titled *o Agencji Bezpieczeństwa Wewnętrznego oraz
Agencji Wywiadu* — the statute carries **both** agencies in its own title.

That is worth noticing next to the Dutch and Belgian acts, which are named
for the *function* ("on the intelligence and security services") rather than
for the bodies. It makes the Polish act harder to reuse and easier to read:
a reader of the title knows exactly which two agencies are inside.

## Relationships

- `governed-by` [[PL-UABWAW-2002]].

## Sources

Listed in frontmatter. The AW's own site publishes a *Ramy prawne* ("legal
framework") page, which is the primary citation here — one of the few
service-published legal-basis pages found in this batch, alongside
[[GB-GCHQ]]'s and [[FR-DGSI]]'s.
