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
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
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
    evidence: "Confirmed by reading bsigroup.com's own 'The UK's National Standards Body' page (2026-08-22): 'As the UK's NSB, BSI is the UK member of the international and European standards development organizations: ISO, IEC, CEN, CENELEC, and ETSI ... with permanent seats on the ISO and IEC Boards.'"
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: INTL-IEC
    source: fact
    evidence: "Confirmed by reading bsigroup.com's own page (2026-08-22): BSI 'is the UK member of the international and European standards development organizations: ISO, IEC, CEN, CENELEC, and ETSI,' with 'permanent seats on the ISO and IEC Boards.'"
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-CEN
    source: fact
    evidence: "Confirmed by reading bsigroup.com's own page (2026-08-22): BSI is the UK member of CEN alongside ISO, IEC, CENELEC and ETSI, and 'facilitate[s] expert participation in the technical work of these organizations, the outcomes of which form 95% of the UK's national catalogue of standards.' The specific figure of 13,000 UK experts was not found on this page and is not independently re-confirmed."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-CENELEC
    source: fact
    evidence: "Confirmed by reading bsigroup.com's own page (2026-08-22): BSI is the UK member of CENELEC alongside CEN, ISO, IEC and ETSI."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-ETSI
    source: fact
    evidence: "Confirmed by reading bsigroup.com's own page (2026-08-22): BSI names itself as the UK member of ETSI alongside ISO, IEC, CEN and CENELEC, without elaborating the membership mechanism. CAVEAT: ETSI membership is direct and company-based rather than by national body in the way CEN and CENELEC are; the source describes BSI as a member there without stating the mechanism."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "The UK's National Standards Body"
    url: "https://www.bsigroup.com/en-US/about-bsi/national-standards-body/"
    publisher: "British Standards Institution (BSI)"
    accessed: "2026-08-22"
  - title: "United Kingdom — Standards for Trade"
    url: "https://www.trade.gov/knowledge-product/united-kingdom-trade-standards"
    publisher: "International Trade Administration (US Department of Commerce)"
    accessed: "2026-08-22"
  - title: "British Standards"
    url: "https://en.wikipedia.org/wiki/British_Standards"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
  - title: "British Standards Institute (BSI) — Open Standards for Data Guidebook"
    url: "https://standards.theodi.org/community/who-can-i-work-with/bsi/"
    publisher: "Open Data Institute"
    accessed: "2026-08-22"
---

# British Standards Institution

> **Verified 2026-08-22.** bsigroup.com's own "National Standards Body"
> page was read directly and confirmed the claims below, verbatim in
> places. `committees.parliament.uk` returned a bot-defense challenge
> (403) and its citation was dropped rather than re-cited unread.

## Description

Confirmed verbatim on bsigroup.com (2026-08-22): "Formed in 1901, BSI was
the world's first national standards body ... As the UK's NSB, BSI is the
UK member of the international and European standards development
organizations: ISO, IEC, CEN, CENELEC, and ETSI ... with permanent seats on
the ISO and IEC Boards, and managing over 175 international and European
committees." BSI is the UK's **National Standards Body**, appointed by government, and —
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
