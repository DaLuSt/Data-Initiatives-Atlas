---
id: GB-BSI
type: organisation
name: British Standards Institution
alternative_names:
  - BSI
  - BSI Group
  - British Standards Institute
description: >
  The United Kingdom's National Standards Body, appointed by the UK
  government, and the world's first national standards body, formed in 1901.
  It represents UK interests at the International Organization for
  Standardization, the International Electrotechnical Commission and the
  European standards organisations CEN, CENELEC and ETSI, holding permanent
  seats on the ISO and IEC boards and managing over 175 international and
  European committees. It provides the infrastructure through which more
  than 13,000 UK experts participate in international standardisation.

level: national
country: GB
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - INTL-ISO
  - INTL-IEC
  - EU-CEN
  - EU-CENELEC
  - EU-ETSI
  - NL-NEN
  - DE-DIN
relationships:
  - type: participates-in
    target: INTL-ISO
    source: fact
    evidence: "BSI is appointed by the UK government as the national standards body and represents UK interests at the International Organization for Standardization (ISO); it is the UK national member of ISO and holds a permanent seat on the ISO board (bsigroup.com 'The UK's National Standards Body'; committees.parliament.uk written evidence 126888; trade.gov 'United Kingdom - Standards for Trade'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: INTL-IEC
    source: fact
    evidence: "BSI is the UK national member of the International Electrotechnical Commission (IEC) and holds a permanent seat on the IEC board (bsigroup.com 'The UK's National Standards Body'; committees.parliament.uk written evidence 126888). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-CEN
    source: fact
    evidence: "BSI is the UK national member of CEN and provides the infrastructure through which over 13,000 UK experts participate in CEN/CENELEC and ISO/IEC standardisation; BSI's membership of the European standards organisations was retained after the UK left the European Union (bsigroup.com; committees.parliament.uk written evidence 126888; linkedin.com 'How BSI works with CEN, CENELEC, ETSI, ISO, IEC and ITU (before and after Brexit)'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-CENELEC
    source: fact
    evidence: "BSI is the UK national member of CENELEC alongside CEN, and UK experts participate in CEN/CENELEC committees through BSI (bsigroup.com 'The UK's National Standards Body'; committees.parliament.uk written evidence 126888). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-ETSI
    source: fact
    evidence: "BSI represents UK interests at the European standards organisations CEN, CENELEC and ETSI (bsigroup.com 'The UK's National Standards Body'; linkedin.com 'How BSI works with CEN, CENELEC, ETSI, ISO, IEC and ITU'). NOT READ — search-only. CAVEAT: ETSI membership is direct and company-based rather than by national body in the way CEN and CENELEC are; the sources describe BSI as representing UK interests there without stating the mechanism."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "The UK's National Standards Body"
    url: "https://www.bsigroup.com/en-US/about-bsi/national-standards-body/"
    publisher: "British Standards Institution (BSI)"
  - title: "British Standards Institution (BSI) — written evidence"
    url: "https://committees.parliament.uk/writtenevidence/126888/html/"
    publisher: "UK Parliament Committees"
  - title: "United Kingdom — Standards for Trade"
    url: "https://www.trade.gov/knowledge-product/united-kingdom-trade-standards"
    publisher: "International Trade Administration (US Department of Commerce)"
  - title: "British Standards"
    url: "https://en.wikipedia.org/wiki/British_Standards"
    publisher: "Wikipedia"
  - title: "British Standards Institute (BSI) — Open Standards for Data Guidebook"
    url: "https://standards.theodi.org/community/who-can-i-work-with/bsi/"
    publisher: "Open Data Institute"
---

# British Standards Institution

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

BSI is the UK's **National Standards Body**, appointed by government, and —
formed in **1901** — the world's first. It carries UK representation into
five standards organisations at once: [[INTL-ISO]], [[INTL-IEC]],
[[EU-CEN]], [[EU-CENELEC]] and [[EU-ETSI]], with permanent seats on the ISO
and IEC boards and more than **175 committees** managed.

## The single most connective UK entity in the Atlas

Before this entity, the United Kingdom reached the rest of the Atlas by
**two** edges — [[GB-UK-GDPR]] `derived-from` [[EU-GDPR]] and
[[GB-NIS-REGULATIONS]] `implements-requirement-from` [[EU-NIS]] — plus
[[GB-ONS]] into [[UN-CES]]. BSI adds **five** on its own.

It also fits an existing shape rather than inventing one:

| Country | National standards body | Attaches to |
|---|---|---|
| Netherlands | [[NL-NEN]] | [[EU-CEN]] |
| Germany | [[DE-DIN]] | [[INTL-ISO]], [[EU-CEN]] |
| **United Kingdom** | **this entity** | **[[INTL-ISO]], [[INTL-IEC]], [[EU-CEN]], [[EU-CENELEC]], [[EU-ETSI]]** |

## The finding: leaving the EU did not remove the UK from European standards

This is the part worth reading twice. [[GB]] records that no EU *instrument*
applies in the United Kingdom, and that is correct. But **CEN and CENELEC
are not EU institutions** — they are European standards organisations whose
membership is national standards bodies, not member states — and BSI's
membership of them **survived the UK's departure**.

So the Atlas now holds a country that:

- takes **no** `applies-in` edge from any EU instrument, and
- sits inside **three** European standardisation bodies.

Those two facts are not in tension; they are what "left the European Union"
actually means in this domain, and neither is visible without the other.

⚠ The ETSI edge is `confidence: low` and deliberately so. ETSI membership is
direct and organisation-based rather than delegated through a national body
the way CEN and CENELEC membership is, and the sources found describe BSI as
*representing UK interests* at ETSI without stating the mechanism. The
evidence string says this.

## Not modelled

**No British Standard is an Atlas entity.** BSI publishes the BS series and
the UK adoptions of EN and ISO standards, and none is here — so this
organisation participates in five standards bodies while maintaining nothing
the Atlas holds. The same gap exists for [[NL-NEN]] and [[DE-DIN]].

**BSI's commercial certification arm** is out of scope: this entity is the
National Standards Body role, which is the part appointed by government.

## Relationships

- `participates-in` [[INTL-ISO]], [[INTL-IEC]], [[EU-CEN]], [[EU-CENELEC]]
  and [[EU-ETSI]] — the last at `confidence: low`.

## Sources

Listed in frontmatter.
