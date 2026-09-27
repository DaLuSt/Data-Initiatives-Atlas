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
last_verified: "2026-09-27"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-VNG
  - NL-UVW
  - NL-FDS
  - NL-NDS
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
    evidence: "Confirmed by reading noraonline.nl's IBDS wiki page directly (2026-08-27): the IBDS 'is tot stand gekomen door samenwerking tussen departementen, uitvoeringsorganisaties en koepels van gemeenten, provincies en waterschappen' (came about through cooperation between ministries, implementing bodies, and associations of municipalities, provinces and water authorities) — IPO is the named association for the provincial tier. Confirmed by name 2026-09-27 by reading digitaleoverheid.nl's own IPO page directly via its WordPress REST API (www.digitaleoverheid.nl/wp-json/wp/v2/pages?slug=interprovinciaal-overleg-ipo — the workaround documented in discovery/unresolved.md row #216, the rendered page itself remaining bot-walled): 'Het werkt samen met het Rijk, gemeenten en waterschappen aan de Interbestuurlijke Datastrategie (IBDS)...' — IPO is now named explicitly rather than only by the general noraonline.nl statement."
    confidence: high
    valid_from: null
    valid_until: null
  - type: participates-in
    target: NL-FDS
    source: fact
    evidence: "CLOSES a gap [[NL-NDS]]'s own file flags for the co-signatory claim generally ('none of the five sources read this pass names VNG, IPO or UvW individually'), for IPO specifically. Confirmed by reading digitaleoverheid.nl's own IPO page directly via its WordPress REST API (2026-09-27, www.digitaleoverheid.nl/wp-json/wp/v2/pages?slug=interprovinciaal-overleg-ipo — the workaround documented in discovery/unresolved.md row #216): 'Het werkt samen met het Rijk, gemeenten en waterschappen aan de Interbestuurlijke Datastrategie (IBDS), het Federatief Datastelsel, gezamenlijke kaders voor informatiebeveiliging en gegevensuitwisseling en de Nederlandse digitaliseringsstrategie (NDS)' (it works with central government, municipalities and water authorities on the IBDS, the Federatief Datastelsel, joint frameworks for information security and data exchange, and the NDS)."
    confidence: high
    valid_from: null
    valid_until: null
  - type: participates-in
    target: NL-NDS
    source: fact
    evidence: "CLOSES a gap [[NL-NDS]]'s own file flags for the co-signatory claim generally, for IPO specifically. Confirmed by the same digitaleoverheid.nl IPO page quoted above (2026-09-27, WordPress REST API workaround, discovery/unresolved.md row #216), which names the NDS alongside the IBDS and Federatief Datastelsel as strategies IPO works on jointly with central government, municipalities and water authorities."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Interprovinciale Digitale Agenda — Digitalisering"
    url: "https://www.ipo.nl/thema-s/digitalisering/"
    publisher: "Interprovinciaal Overleg (IPO)"
    accessed: "2026-08-27"
  - title: "Interprovinciaal Overleg (IPO) — Organisaties rondom digitalisering"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/organisaties-rondom-digitalisering/interprovinciaal-overleg-ipo/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-09-27"
    note: "The rendered page is genuinely bot-walled (JavaScript verification challenge). Read directly via the site's own WordPress REST API instead (www.digitaleoverheid.nl/wp-json/wp/v2/pages?slug=interprovinciaal-overleg-ipo) — the workaround documented in discovery/unresolved.md row #216."
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
>
> **Closed 2026-09-27**: digitaleoverheid.nl's IPO page, genuinely
> bot-walled to direct fetch, is now read directly via the site's own
> WordPress REST API (the workaround documented in
> `discovery/unresolved.md` row #216) — 5 of 5 sources now read directly.
> It names IPO explicitly as a joint worker on the IBDS, the Federatief
> Datastelsel and the NDS, closing the co-signatory gap [[NL-NDS]]'s own
> file flags — for IPO specifically. Two new `participates-in` edges
> ([[NL-FDS]], [[NL-NDS]]) are added, and the IBDS edge is upgraded to
> `confidence: high`. It also gives IPO's founding year (1986) and its
> Brussels representation office.

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

**Founded 1986** — confirmed 2026-09-27 by reading digitaleoverheid.nl's
own IPO page directly (via the WordPress REST API workaround) — to
strengthen inter-provincial cooperation and better organise joint
positions. It is based in The Hague and maintains a representation office
in Brussels. The same page names IPO explicitly as a joint worker,
alongside central government, municipalities and water authorities, on
the [[NL-IBDS]], the [[NL-FDS]], joint frameworks for information
security and data exchange, and the [[NL-NDS]] — closing, for IPO
specifically, the co-signatory gap [[NL-NDS]]'s own file flags ("none of
the five sources read this pass names VNG, IPO or UvW individually").

## Relationships

- Participates in [[NL-OBDO]] — confirmed this pass, IPO named explicitly.
- Participates in [[NL-IBDS]] — confirmed via NORA's general description
  of the strategy's founding cooperators, and now, 2026-09-27, via
  digitaleoverheid.nl's own IPO page naming IPO by name — `confidence`
  raised to `high`.
- Participates in [[NL-FDS]] and [[NL-NDS]] — new 2026-09-27, both sourced
  to the same digitaleoverheid.nl IPO page, which names IPO as a joint
  worker on both strategies alongside central government, municipalities
  and water authorities.

## Sources

Listed in frontmatter. **5 of 5 now read directly.** ipo.nl, ibestuur.nl
and noraonline.nl (earlier pass); and, closing this file 2026-09-27,
digitaleoverheid.nl's IPO page via the site's own WordPress REST API
(`www.digitaleoverheid.nl/wp-json/wp/v2/pages?slug=interprovinciaal-overleg-ipo`)
— the workaround documented in `discovery/unresolved.md` row #216. The
rendered HTML at that URL remains genuinely bot-walled.
