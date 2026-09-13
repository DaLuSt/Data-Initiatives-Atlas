---
id: NL-WBP
type: law
name: Wet bescherming persoonsgegevens
alternative_names:
  - Wbp
  - Dutch Data Protection Act
description: >
  The Netherlands' general data protection act, in force from 1 September
  2001 to 25 May 2018, implementing the EU's 1995 Data Protection Directive
  (95/46/EC) and replacing the earlier Wet persoonsregistraties (1989). It
  designated the College Bescherming Persoonsgegevens (renamed the
  Autoriteit Persoonsgegevens from 1 January 2016) as supervisory authority.
  Repealed and replaced by the Uitvoeringswet Algemene verordening
  gegevensbescherming (UAVG) when the GDPR took direct effect.

level: national
country: NL
region: EU

status: superseded
confidence: high
coverage: low
verification: primary-source

start_date: "2001-09-01"
end_date: "2018-05-25"
last_verified: "2026-09-13"
previous_version: null
successor: NL-UAVG

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-AP
related_entities:
  - NL-UAVG
  - EU-GDPR
relationships: []

sources:
  - title: "Wet bescherming persoonsgegevens — BWBR0011468 (informatie)"
    url: "https://wetten.overheid.nl/BWBR0011468/2016-01-01/0/informatie"
    publisher: "Overheid.nl (wetten.overheid.nl)"
    accessed: "2026-09-13"
  - title: "Wet bescherming persoonsgegevens (Wbp)"
    url: "https://nl.wikipedia.org/wiki/Wet_bescherming_persoonsgegevens_(Nederland)"
    publisher: "Wikipedia (NL)"
    accessed: "2026-09-13"
---

# Wet bescherming persoonsgegevens (Wbp)

> **Created 2026-09-13.** Named on [[NL-UAVG]]'s own file as the act it
> repealed but left unmodelled ("queued for temporal completeness"), no
> tracked row in `discovery/unresolved.md` or `discovery/research-queue.md`
> — found instead via a routine grep for lingering "not yet an Atlas
> entity" language. Two independent sources read directly: wetten.overheid.nl's
> own "informatie" page for BWBR0011468 (the official record of enactment,
> entry-into-force and repeal dates) and Dutch Wikipedia's dedicated article,
> corroborating without contradiction.

## Description

The Wbp was the Netherlands' general data protection act before the GDPR.
Confirmed directly via wetten.overheid.nl's own record for BWBR0011468: it
was **enacted 6 July 2000** (Stb. 2000, 302), entered into force **1
September 2001** (Stb. 2001, 337), and was **repealed 25 May 2018** (Stb.
2018, 298) — the same day [[NL-UAVG]] and the GDPR took effect.

Dutch Wikipedia's own article, read directly and independently, corroborates
the 1 September 2001 entry-into-force date, adds that the Wbp was "for a
large part based on" the EU's 1995 Data Protection Directive (95/46/EC —
not itself an Atlas entity, a documented gap), and that it replaced an
earlier act, the **Wet persoonsregistraties** of 1989 — not modelled here,
one predecessor step removed from what this entity closes.

The supervisory authority was the **College Bescherming Persoonsgegevens**,
renamed the **Autoriteit Persoonsgegevens** ([[NL-AP]]) from 1 January
2016 — confirmed by the same Wikipedia article — carrying the name change
through to the body [[NL-UAVG]] itself designates.

## Relationships

- **This entity asserts no relationship of its own.** It is reached from
  [[NL-UAVG]], which carries `supersedes` → this entity, matching the
  Atlas's convention of recording succession on the successor (see
  [[NL-ARCHIEFWET-2026]] → [[NL-ARCHIEFWET-1995]] for the same pattern).
- No edge to the EU's Data Protection Directive (95/46/EC) is asserted —
  it is not an Atlas entity. Creating it was out of scope for this pass;
  left as a documented, named gap rather than silently dropped.
- No edge to the Wet persoonsregistraties (1989) is asserted, for the same
  reason.

## Sources

Two of two read directly: wetten.overheid.nl's own official record and
Dutch Wikipedia's dedicated article, agreeing on every date checked.
