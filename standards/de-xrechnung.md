---
id: DE-XRECHNUNG
type: standard
name: XRechnung
alternative_names:
  - Standard XRechnung
description: >
  German standard for electronic invoicing to public sector contracting
  authorities, developed within the XÖV framework and operated by the
  Koordinierungsstelle für IT-Standards since 1 January 2019. It is a Core
  Invoice Usage Specification (CIUS) of the European standard EN 16931,
  supporting both the UBL 2.1 and UN/CEFACT CII XML syntaxes and adding
  German-specific mandatory fields such as the Leitweg-ID routing
  identifier for public offices. It was phased in as mandatory between
  27 November 2018 (top federal agencies) and 27 November 2020 (all
  suppliers invoicing public contracting authorities).

level: national
country: DE
region: EU

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: 2019-01-01
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - DE-KOSIT
related_entities:
  - EU-EINVOICING-DIRECTIVE
  - EU-EN-16931
  - DE-XOEV
relationships:
  - type: based-on
    target: EU-EN-16931
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP. Confirmed by reading de.wikipedia.org's dedicated XRechnung article, cleartax.com's own EN 16931/Germany explainer, and the European Commission's own digital-building-blocks CIUS-compliance page directly (2026-08-28): Wikipedia states 'XRechnung implements the European standard EN 16931-1' as a 'Core Invoice Usage Specification (CIUS)' and that 'all invoices conforming to XRechnung are also conforming to EN 16931-1.' cleartax.com states plainly: 'EN 16931 is the European e-invoice recipe everyone must follow. XRechnung is the German version of that recipe, customised to meet local rules' — supporting both UBL 2.1 and UN/CEFACT CII syntaxes and adding German-specific mandatory fields (e.g. the Leitweg-ID routing identifier) while remaining 'automatically compliant with EN 16931.' The European Commission's own page, read directly, independently confirms the general CIUS/CORE compliance mechanism a national specification like XRechnung operates under. This was previously the sharpest documented refusal in the German batch ('a refusal that visibly costs something'); it is closed this pass by direct reading rather than by search snippets."
    confidence: high
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: DE-KOSIT
    source: fact
    evidence: "Confirmed by reading de.wikipedia.org's dedicated XRechnung article directly (2026-08-28): 'The Coordination Office for IT Standards (KoSIT) has managed XRechnung since January 1, 2019.' The originally-cited xoev.de operations/support page now returns HTTP 404 and was not readable this pass; Wikipedia's independent, dedicated article substitutes for it."
    confidence: high
    valid_from: 2019-01-01
    valid_until: null
  - type: based-on
    target: DE-XOEV
    source: fact
    evidence: "Confirmed by reading de.wikipedia.org's dedicated XRechnung article directly (2026-08-28): 'XRechnung was developed within XÖV (XML in Public Administration), Germany's framework for standardized electronic data exchange across government.'"
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "XRechnung"
    url: "https://de.wikipedia.org/wiki/XRechnung"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
  - title: "Koordinierungsstelle für IT-Standards — Betrieb und Support (XRechnung)"
    url: "https://www.xoev.de/xrechnung/betrieb_und_support-16853"
    publisher: "Koordinierungsstelle für IT-Standards (KoSIT)"
  - title: "Elektronische Rechnung für die öffentliche Verwaltung"
    url: "https://www.b3-it.de/erechnung_xrechnung_zugferd.html"
    publisher: "b3-it"
    accessed: "2026-08-28"
  - title: "EN 16931 Standard Germany: Format, Example and Specification"
    url: "https://www.cleartax.com/de/en/en-16931-standard-germany"
    publisher: "ClearTax"
    accessed: "2026-08-28"
  - title: "EN 16931 compliance"
    url: "https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/EN+16931+compliance"
    publisher: "European Commission — Digital Building Blocks"
    accessed: "2026-08-28"
---

# XRechnung

> **Re-verified 2026-08-28, gap closed.** Four of five cited/added sources
> read directly; the `xoev.de` operations page now returns HTTP 404. Two
> sources not in the original list — a European Commission page and a
> corrected ClearTax URL (the originally-cited one 404s) — were added and
> read directly to close the entity's previously flagged and most visible
> refusal: the EU→DE link via EN 16931. `verification: primary-source`;
> `confidence` raised to `high`.

## Description

XRechnung is the German standard for **electronic invoicing to public
sector contracting authorities**. It was developed within the
[[DE-XOEV]] framework, confirmed directly this pass on its dedicated
Wikipedia article, and has been **operated by [[DE-KOSIT]] since 1 January
2019**. Its mandate was phased in, more precisely than previously
recorded: **27 November 2018** for top federal agencies, **27 November
2019** for other federal bodies, **18 April 2020** for the Länder, and
**27 November 2020** for all suppliers invoicing public contracting
authorities.

## The EU link is now recorded — closing the batch's sharpest flagged gap

The entity previously stated, in its own words, that a sourced EU link
here "would give the Atlas a fifth EU→DE chain... structurally the same
shape as the DCAT chain," and flagged it as the sharpest instance of a
costly refusal in the whole German batch. This pass closes it.

Confirmed directly on three independently-read sources: Wikipedia's own
XRechnung article states "XRechnung implements the European standard EN
16931-1" as a **Core Invoice Usage Specification (CIUS)**, such that "all
invoices conforming to XRechnung are also conforming to EN 16931-1."
ClearTax's own explainer, read directly, puts it plainly: "EN 16931 is the
European e-invoice recipe everyone must follow. XRechnung is the German
version of that recipe, customised to meet local rules" — supporting both
the **UBL 2.1** and **UN/CEFACT CII** XML syntaxes defined by EN 16931,
and adding German-specific mandatory fields such as the **Leitweg-ID**
routing identifier for public offices. The European Commission's own
digital-building-blocks page, also read directly, independently confirms
the general CIUS/CORE compliance mechanism under which a national
specification like XRechnung operates, including the Commission's own
caution that a receiver restricted to one CIUS may not be able to process
invoices compliant with a different one — a genuine interoperability
trade-off, not just a technical footnote.

`EU-EN-16931` — [[EU-EN-16931]] in this Atlas — is CEN's own 2017 standard
under Directive 2014/55/EU ([[EU-EINVOICING-DIRECTIVE]]). This gives the
Atlas a fifth EU→DE chain, and the first running through a **standards**
body rather than a legislature: `EU-CEN → EU-EN-16931 → DE-XRECHNUNG`,
structurally the same shape as the DCAT chain (`INTL-DCAT → EU-DCAT-AP →
NL-DCAT-AP-NL` / `DE-DCAT-AP-DE`) that Batch 15 called the template the
Atlas needs more of.

## Relationships

- `based-on` [[EU-EN-16931]] — newly confirmed this pass, closing a
  previously flagged high-value gap, `confidence: high`.
- Maintained by [[DE-KOSIT]] — confirmed directly this pass, `confidence:
  high`.
- `based-on` [[DE-XOEV]] — confirmed directly this pass, `confidence:
  high`.

## Sources

Listed in frontmatter. Four of five read directly this pass, including two
sources added to close the EN 16931 gap (a corrected ClearTax URL and the
European Commission's own compliance page); the originally-cited `xoev.de`
operations page now 404s and Wikipedia's dedicated article substitutes for
the facts it supported. `b3-it.de`, also read directly, adds ZUGFeRD as a
related but distinct hybrid PDF/XML format also permitted under Directive
2014/55/EU.
