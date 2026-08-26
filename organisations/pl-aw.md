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
verification: primary-source

start_date: 2002-05-24
end_date: null
last_verified: "2026-08-26"
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
    evidence: "Confirmed by reading aw.gov.pl's own 'Ramy prawne' page directly (2026-08-26): it names the Act of 24 May 2002 as AW's legal basis, quotes the Act's own Article 24 on requesting assistance from state institutions, and gives the agency's motto ('pozyskujemy informacje — służymy państwu — chronimy naród'). bip.abw.gov.pl's own page on the College for Special Services, also read directly, separately names AW's head among the College's members alongside ABW. `isap.sejm.gov.pl`, which would carry the Act's own text, is genuinely CAPTCHA-blocked."
    confidence: medium
    valid_from: 2002-05-24
    valid_until: null

sources:
  - title: "Ramy prawne"
    url: "https://aw.gov.pl/pl/o-nas/ramy-prawne/167,Ramy-prawne.html"
    publisher: "Agencja Wywiadu (AW)"
    accessed: "2026-08-26"
  - title: "Kolegium ds. służb specjalnych"
    url: "https://bip.abw.gov.pl/bip/nadzor-i-kontrola/kolegium-ds-sluzb-spec/18,Kolegium-ds-sluzb-specjalnych.html"
    publisher: "Agencja Bezpieczeństwa Wewnętrznego (BIP)"
    accessed: "2026-08-26"
  - title: "Ustawa z dnia 24 maja 2002 r. o Agencji Bezpieczeństwa Wewnętrznego oraz Agencji Wywiadu (currently CAPTCHA-blocked)"
    url: "https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=wdu20020740676"
    publisher: "Internetowy System Aktów Prawnych (ISAP), Sejm RP"
---

# Agencja Wywiadu (AW)

> **Verified 2026-08-26.** Two of three cited pages were read directly.
> AW's own "Ramy prawne" page gives a founding-era statutory detail
> (Article 24) and the agency's own motto, neither previously carried.

## Description

The AW is Poland's civilian **foreign** intelligence agency, protecting the
external security of the state, with its head reporting directly to the
Prime Minister. Its internal counterpart is [[PL-ABW]]. Confirmed by
reading aw.gov.pl directly: the agency's own motto is "pozyskujemy
informacje — służymy państwu — chronimy naród" (we obtain information —
we serve the state — we protect the nation), and Article 24 of its
constituting Act lets AW personnel "żądania niezbędnej pomocy od
instytucji państwowych" (request necessary assistance from state
institutions) while executing their lawful duties.

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

Listed in frontmatter, two of three read directly this pass. The AW's own
site publishes a *Ramy prawne* ("legal framework") page, which is the
primary citation here — one of the few service-published legal-basis
pages found in this batch, alongside [[GB-GCHQ]]'s and [[FR-DGSI]]'s.
`isap.sejm.gov.pl` remains genuinely CAPTCHA-blocked.
