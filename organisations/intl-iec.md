---
id: INTL-IEC
type: organisation
name: International Electrotechnical Commission
alternative_names:
  - IEC
description: >
  International standards organisation for electrotechnical and related
  technologies, based on national delegation and **not** a UN body. With ISO
  it operates Joint Technical Committee 1 on information technology.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - INTL-ISO
relationships: []

sources:
  - title: "ISO/IEC 27001:2022 — Information security management systems"
    url: "https://www.iso.org/standard/27001"
    publisher: "International Organization for Standardization (ISO)"
  - title: "Information security, cybersecurity and privacy protection — JTC 1"
    url: "https://jtc1info.org/technology/subcommittees/information-security-cybersecurity-privacy-protection/"
    publisher: "ISO/IEC JTC 1"
    accessed: "2026-08-28"
  - title: "International Electrotechnical Commission"
    url: "https://en.wikipedia.org/wiki/International_Electrotechnical_Commission"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
---

# IEC (International Electrotechnical Commission)

> **Verified 2026-08-28, with a documented block.** `iso.org` is
> domain-wide 403-blocked for this pass's retrieval tool (confirmed
> across multiple paths; see [[INTL-ISO]] for the detail), so the
> `iso.org/standard/27001` source stays unread. jtc1info.org was read
> directly, and a Wikipedia article on the IEC was added as a substitute
> source and also read directly, bringing two of three cited sources to
> a genuine read. `verification` moves from `search-only` to
> `primary-source` on that basis.

## Description

The IEC is the international standards organisation for electrotechnical and
related technologies. With [[INTL-ISO]] it operates **ISO/IEC JTC 1**, the
joint technical committee on information technology, under which SC 27
publishes the information security standards this Atlas depends on.
Wikipedia's IEC article, read directly this pass, confirms the IEC
"prepares and publishes international standards for all electrical,
electronic and related technologies," organised through one national
committee per member country — **92 full members** plus 75 countries in an
affiliate programme — and headquartered in Geneva as a Swiss association.

`INTL` scope, not `UN` — the IEC is not a UN body; Wikipedia's article does
not describe it as one, consistent with its description as an independent
Swiss association.

`coverage: low`. **No IEC-only standard is modelled**; the IEC appears here
solely through the jointly published ISO/IEC standards. Its European
counterpart is [[EU-CENELEC]], and the Dutch electrotechnical committee NEC
— which has cooperated with [[NL-NEN]] under the shared NEN name since 2000
— is the national level of the same chain, still unmodelled.

**ISO/IEC JTC 1 itself is not modelled.** It is arguably the entity that
actually produces the 27000-family standards, sitting between the two
organisations and the standards. Whether it warrants its own entity is
queued.

## Relationships

- Operates JTC 1 jointly with [[INTL-ISO]].

## Sources

Listed in frontmatter. Two of three read directly this pass —
jtc1info.org and the Wikipedia IEC article. `iso.org/standard/27001`
stays unread, blocked domain-wide (see verification note above).
