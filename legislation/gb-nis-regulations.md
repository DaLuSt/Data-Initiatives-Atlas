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
verification: primary-source
start_date: 2018-05-10
end_date: null
last_verified: "2026-08-22"
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
    evidence: "Confirmed by reading the statute text at legislation.gov.uk (2026-08-22): 'Made 19th April 2018. Laid before Parliament 20th April 2018. Coming into force 10th May 2018.' Schedule 1 designates competent authorities including 'Digital Infrastructure ... Office of Communications (United Kingdom)'."
    confidence: medium
    valid_from: 2018-05-10
    valid_until: null
  - type: implements-requirement-from
    target: EU-NIS
    source: fact
    evidence: "Confirmed by reading the statute text at legislation.gov.uk (2026-08-22): the Regulations cite 'Directive (EU) 2016/1148 of the European Parliament and of the Council' directly and came into force 10 May 2018, one day after the Directive's 9 May 2018 transposition deadline."
    confidence: medium
    valid_from: 2018-05-10
    valid_until: null

sources:
  - title: "The Network and Information Systems Regulations 2018"
    url: "https://www.legislation.gov.uk/uksi/2018/506"
    publisher: "legislation.gov.uk (The National Archives)"
    accessed: "2026-08-22"
  - title: "The NIS Regulations 2018"
    url: "https://www.gov.uk/government/collections/nis-directive-and-nis-regulations-2018"
    publisher: "GOV.UK"
    accessed: "2026-08-22"
  - title: "UK NIS Regulations 2018: scope, duties and enforcement"
    url: "https://www.lexisnexis.com/en-gb/legal/guidance/the-network-information-systems-regulations-2018"
    publisher: "LexisNexis UK"
    accessed: "2026-08-22"
  - title: "The Network and Information Systems Regulations 2018: how will they apply in practice?"
    url: "https://www.osborneclarke.com/insights/the-network-and-information-systems-regulations-2018-how-will-they-apply-in-practice"
    publisher: "Osborne Clarke"
    accessed: "2026-08-22"
---

# The NIS Regulations 2018

> **Verified 2026-08-22.** The statutory instrument's own text at
> legislation.gov.uk was read directly and confirmed the claims below,
> including Schedule 1's competent-authority list verbatim.

## Description

Confirmed directly on legislation.gov.uk (2026-08-22): "Made 19th April
2018. Laid before Parliament 20th April 2018. Coming into force 10th May
2018," citing "Directive (EU) 2016/1148 of the European Parliament and of
the Council" throughout. SI 2018/506 **gave effect in the UK to Directive (EU) 2016/1148** — see
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

Schedule 1, read directly (2026-08-22), lists competent authorities rather
than naming one: energy (electricity, oil, gas) to the Secretary of State
and sector regulators; transport (air, rail, water, road) to the Secretary
of State for Transport and devolved administrations; health and drinking
water similarly split by nation; and, in the row that matters for this
Atlas, **"Digital Infrastructure — Office of Communications (United
Kingdom)"** — Ofcom, named by its full statutory title. [[GB-ICO]] is named
for relevant digital service providers. [[GB-NCSC]] is **explicitly not a
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
