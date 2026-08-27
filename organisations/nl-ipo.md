---
id: NL-IPO
type: organisation
name: Interprovinciaal Overleg
alternative_names:
  - IPO
description: >
  Umbrella organisation of the twelve Dutch provinces. Within the
  data/digital ecosystem it coordinates inter-provincial cooperation on data
  sharing, information security and digital service delivery, and represents
  provinces in government-wide digital governance.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-VNG
  - NL-UVW
relationships:
  - type: participates-in
    target: NL-OBDO
    source: fact
    evidence: "Confirmed by reading ibestuur.nl's article on the OBDO directly (2026-08-27), quoting the OBDO's own governance description: 'In dit overleg zijn alle departementen, Interprovinciaal Overleg (IPO), Unie van Waterschappen (UvW), CIO-Rijk en de voorzitter van de Programmeringsraad Logius vertegenwoordigd' (all ministries, IPO, UvW, CIO-Rijk and the chair of the Logius Programming Council are represented in this consultation). digitaleoverheid.nl's own OBDO/MIDO governance pages, cited in the prior text, returned a bot-verification challenge page both times they were fetched this pass and could not be read directly — this is a genuine, repeated block on that domain, not a silent drop."
    confidence: high
    valid_from: null
    valid_until: null
  - type: participates-in
    target: NL-IBDS
    source: fact
    evidence: "Confirmed by reading noraonline.nl's IBDS wiki page directly (2026-08-27): the IBDS 'is tot stand gekomen door samenwerking tussen departementen, uitvoeringsorganisaties en koepels van gemeenten, provincies en waterschappen' (came about through cooperation between ministries, implementing bodies, and associations of municipalities, provinces and water authorities) — IPO is the named association for the provincial tier. ipo.nl's own digitalisation theme page, read directly, references 'interprovinciale en interbestuurlijke samenwerking' (inter-provincial and inter-governmental cooperation) without naming the IBDS specifically, so this edge rests on the noraonline.nl page's general statement rather than a source naming IPO."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Interprovinciale Digitale Agenda — Digitalisering"
    url: "https://www.ipo.nl/thema-s/digitalisering/"
    publisher: "Interprovinciaal Overleg (IPO)"
    accessed: "2026-08-27"
  - title: "Interprovinciaal Overleg (IPO) — Organisaties rondom digitalisering (confirmed genuinely bot-walled)"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/organisaties-rondom-digitalisering/interprovinciaal-overleg-ipo/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "OBDO stelt Architectuur Digitale Overheid 2030 vast"
    url: "https://ibestuur.nl/artikel/obdo-stelt-architectuur-digitale-overheid-2030-vast/"
    publisher: "iBestuur"
    accessed: "2026-08-27"
  - title: "Interbestuurlijke Datastrategie (IBDS)"
    url: "https://www.noraonline.nl/wiki/Interbestuurlijke_Datastrategie_(IBDS)"
    publisher: "NORA Online (ICTU)"
    accessed: "2026-08-27"
---

# Interprovinciaal Overleg (IPO)

> **Verified 2026-08-27.** ipo.nl's own page was read directly, and two new
> alternate sources (ibestuur.nl, noraonline.nl) were found and read to
> confirm the two relationships after digitaleoverheid.nl proved genuinely
> and repeatedly bot-walled — a verification-challenge page, not real
> content, on every fetch attempt this pass. `verification` moves from
> `search-only` to `primary-source`.

## Description

The IPO is the umbrella organisation of the twelve Dutch provinces.
Confirmed by reading ipo.nl directly: it stimulates cooperation on
"informatieversterking" (information strengthening — provincial data and
territorial knowledge), digital innovation, and the ethical dimensions of
technology and data use, working through a multi-year digital information
management plan (Meerjarenplan Digitale Informatiehuishouding).

Its relevance to the Atlas is that it makes the provincial tier a
participant in government-wide data governance. This pass confirms two
concrete channels directly: the [[NL-OBDO]], where iBestuur's own reporting
on the OBDO's governance names IPO explicitly as a represented body
alongside all ministries, [[NL-UVW]], and CIO-Rijk; and the [[NL-IBDS]],
where NORA's own wiki describes provincial associations as among the
strategy's founding cooperators.

Together with [[NL-VNG]] and [[NL-UVW]], the IPO forms the set of
koepelorganisaties representing the decentralised tiers of Dutch government.

## Relationships

- Participates in [[NL-OBDO]] — confirmed this pass, IPO named explicitly.
- Participates in [[NL-IBDS]] — confirmed this pass via NORA's general
  description of the strategy's founding cooperators; IPO is not named by
  name in the page read, so `confidence: medium` reflects that gap.
- [[NL-FDS]] and [[NL-NDS]] co-signatory claims in the prior text were not
  re-confirmed by any page read this pass and are left as unsourced
  associations rather than asserted relationships; see `discovery/unresolved.md`.

## Sources

Listed in frontmatter. ipo.nl, ibestuur.nl and noraonline.nl read directly
this pass; digitaleoverheid.nl's IPO page is confirmed genuinely bot-walled
(a JavaScript verification challenge, not static content) on every attempt.
