---
id: GB-NIS-REGULATIONS
type: regulation
name: The Network and Information Systems Regulations 2018
alternative_names:
  - NIS Regulations 2018
  - NIS Regulations
  - SI 2018/506
description: >
  United Kingdom statutory instrument, SI 2018/506, which gave effect in the
  United Kingdom to Directive (EU) 2016/1148 on security of network and
  information systems. It came into force on 10 May 2018, one day after the
  transposition deadline, and imposes security and notification obligations
  on operators of essential services in electricity, gas, water supply,
  transport and other sectors, and on relevant digital service providers
  being online search engines, online marketplaces and cloud computing
  services. Rather than appointing a single central competent authority, it
  takes a sector-by-sector approach, listing competent authorities in
  Schedule 1 including the responsible government departments, Ofcom for
  digital infrastructure and the Information Commissioner's Office for
  relevant digital service providers.

level: national
country: GB
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2018-05-10
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations:
  - GB-ICO
  - GB-NCSC
related_entities:
  - GB
  - EU-NIS
  - GB-CSRB
  - NL-WBNI
relationships:
  - type: applies-in
    target: GB
    source: fact
    evidence: "The Network and Information Systems Regulations 2018, SI 2018/506, gave effect in the United Kingdom to Directive (EU) 2016/1148 and came into force on 10 May 2018, imposing obligations on operators of essential services and relevant digital service providers in the UK (legislation.gov.uk SI 2018/506; gov.uk 'The NIS Regulations 2018'; lexisnexis.com). NOT READ — search-only."
    confidence: medium
    valid_from: 2018-05-10
    valid_until: null
  - type: implements-requirement-from
    target: EU-NIS
    source: fact
    evidence: "The Network and Information Systems Regulations 2018, SI 2018/506, gave effect in the UK to the Network and Information Systems Directive, Directive (EU) 2016/1148; EU member states, including at that time the UK, were required to transpose the directive by 9 May 2018, and the UK Regulations came into force on 10 May 2018 (lexisnexis.com legal guidance on the NIS Regulations 2018; legislation.gov.uk SI 2018/506; gov.uk 'The NIS Regulations 2018'; osborneclarke.com). NOT READ — search-only."
    confidence: medium
    valid_from: 2018-05-10
    valid_until: null

sources:
  - title: "The Network and Information Systems Regulations 2018"
    url: "https://www.legislation.gov.uk/uksi/2018/506"
    publisher: "legislation.gov.uk (The National Archives)"
  - title: "The NIS Regulations 2018"
    url: "https://www.gov.uk/government/collections/nis-directive-and-nis-regulations-2018"
    publisher: "GOV.UK"
  - title: "UK NIS Regulations 2018: scope, duties and enforcement"
    url: "https://www.lexisnexis.com/en-gb/legal/guidance/the-network-information-systems-regulations-2018"
    publisher: "LexisNexis UK"
  - title: "The Network and Information Systems Regulations 2018: how will they apply in practice?"
    url: "https://www.osborneclarke.com/insights/the-network-and-information-systems-regulations-2018-how-will-they-apply-in-practice"
    publisher: "Osborne Clarke"
---

# The NIS Regulations 2018

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

SI 2018/506 **gave effect in the UK to Directive (EU) 2016/1148** — see
[[EU-NIS]] — and came into force on **10 May 2018**, the day after the
transposition deadline. It is still in force, and [[GB-CSRB]] would amend
rather than replace it.

## The only EU transposition in the Atlas from a country that has left

This is the single strangest edge in the graph, and it is entirely
straightforward.

The UK was a member state in May 2018. It transposed the NIS Directive as
every other member state did. It then left the European Union, and **the
transposing instrument stayed in force** — as assimilated law, on the same
constitutional footing as [[GB-UK-GDPR]].

So `implements-requirement-from` [[EU-NIS]] is **a fact about 2018 that is
still true in 2026**, asserted from a country that is no longer bound by the
directive it implements. The edge needs no qualification and gets none. Its
`valid_from` is the commencement date and its `valid_until` is null, because
nothing has ended it.

**In the Compare view this puts the UK next to the Netherlands on the
[[EU-NIS]] row** — the only two countries with a modelled NIS Directive
implementation, and the row now spans a member state and a former one.

## The UK has no NIS2 position, and that is the point

Six batches built a NIS2 table. The seventh country **is not on it**:

| Country | NIS2 instrument | State |
|---|---|---|
| Belgium | [[BE-NIS2-WET]] | in force 18 Oct 2024 |
| Germany | [[DE-NIS2UMSUCG]] | in force 6 Dec 2025 |
| Netherlands | [[NL-CBW]] | in force 15 Aug 2026 |
| France | [[FR-NIS2-LOI]] | `unknown` |
| Spain | [[ES-LCGC]] | `proposed` |
| Poland | [[PL-KSC]] | in force 3 Apr 2026, before the CJEU |
| **United Kingdom** | **none, and none is due** | **[[GB-CSRB]] instead** |

[[EU-NIS2]] repealed [[EU-NIS]] for the member states. It did not repeal
**this** instrument, because the UK was outside its scope by then. The UK
therefore runs a **NIS1-era regime that the EU has superseded**, and is
replacing it on its own timetable with a domestic bill that is not a
transposition of anything.

That divergence — same starting point in 2016, different instruments eight
years later — is the clearest thing the Atlas can now show about what
leaving the EU did to a regulatory area.

## Sector-by-sector competent authorities

Schedule 1 lists competent authorities rather than naming one: the
departments responsible for **energy, transport, health and drinking
water**, **Ofcom** for digital infrastructure, and **[[GB-ICO]]** for
relevant digital service providers. [[GB-NCSC]] is **explicitly not a
competent authority**, and coordinates instead.

**[[GB-OFCOM]] is now modelled**, so two of the named competent authorities
are Atlas entities and both carry `applies-to` edges to this instrument.
**The sectoral departments — energy, transport, health, drinking water — are
still not**, so the statute names more authorities than the graph shows.

## Relationships

- `applies-in` [[GB]].
- `implements-requirement-from` [[EU-NIS]], valid from 10 May 2018.

[[GB-ICO]] and [[GB-OFCOM]] carry the `applies-to` edges pointing here.

## Sources

Listed in frontmatter, including the legislation.gov.uk entry for the
statutory instrument itself — which makes this the best-cited legislative
entity in the UK batch.
