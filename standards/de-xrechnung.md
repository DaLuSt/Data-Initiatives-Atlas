---
id: DE-XRECHNUNG
type: standard
name: XRechnung
alternative_names:
  - Standard XRechnung
description: >
  German standard for electronic invoicing to public sector contracting
  authorities, developed within the XÖV framework and operated by the
  Koordinierungsstelle für IT-Standards since 1 January 2019. It has been
  mandatory since November 2020 for suppliers submitting invoices to public
  contracting authorities in Germany.

level: national
country: DE
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2019-01-01
end_date: null
last_verified: null
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
    evidence: "XRechnung in Germany is a CIUS — a Core Invoice Usage Specification — of EN 16931 for business-to-government invoicing, and supports both the UBL and CII syntaxes; EN 16931 is the European standard for electronic invoices issued by CEN in 2017 under Directive 2014/55/EU and defines a semantic data model of 176 business terms (cleartax.com 'EN 16931 Standard Germany'; ec.europa.eu digital-building-blocks 'EN 16931 compliance'; xoev.de XRechnung). NOT READ — search-only. This closes the item carried in discovery/research-queue.md since the Germany batch as the highest-value German item."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: DE-KOSIT
    source: fact
    evidence: "The XRechnung standard has been operated by the Koordinierungsstelle für IT-Standards (KoSIT) since 1 January 2019 and is developed and maintained by KoSIT, which also offers support services for it as part of its operations (de.wikipedia.org 'XRechnung'; xoev.de/xrechnung/betrieb_und_support-16853). NOT READ — search-only."
    confidence: medium
    valid_from: 2019-01-01
    valid_until: null
  - type: based-on
    target: DE-XOEV
    source: fact
    evidence: "The XRechnung standard was developed within the framework of requirements for electronic data exchange in public administration — XML in der öffentlichen Verwaltung (XÖV) (de.wikipedia.org 'XRechnung'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "XRechnung"
    url: "https://de.wikipedia.org/wiki/XRechnung"
    publisher: "Wikipedia"
  - title: "Koordinierungsstelle für IT-Standards — Betrieb und Support (XRechnung)"
    url: "https://www.xoev.de/xrechnung/betrieb_und_support-16853"
    publisher: "Koordinierungsstelle für IT-Standards (KoSIT)"
  - title: "Elektronische Rechnung für die öffentliche Verwaltung"
    url: "https://www.b3-it.de/erechnung_xrechnung_zugferd.html"
    publisher: "b3-it"
---

# XRechnung

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

XRechnung is the German standard for **electronic invoicing to public
sector contracting authorities**. It was developed within the
[[DE-XOEV]] framework, has been **operated by [[DE-KOSIT]] since 1 January
2019**, and has been **mandatory since November 2020** for all suppliers
submitting invoices to public contracting authorities in Germany.

The KoSIT develops and maintains it and offers support services for it as
part of its operations.

## ⚠ The EU link this entity almost certainly has, and does not record

Electronic invoicing in EU public procurement is governed by **Directive
2014/55/EU** and the European standard on electronic invoicing **EN
16931**, developed by [[EU-CEN]]. XRechnung is, in the ordinary
understanding of the field, the German *CIUS* — a national specification
narrowing that European norm.

**None of that is recorded.** No source read states it, neither Directive
2014/55/EU nor EN 16931 is an Atlas entity, and the November 2020 mandate
date — which corresponds to the directive's transposition deadline for
sub-central authorities — is recorded as a plain fact without the inference
attached.

This is the sharpest instance in the German batch of a refusal that
visibly costs something. A sourced link here would give the Atlas a fifth
EU→DE chain and, unusually, one running through a **standards** body rather
than a legislature: `EU-CEN → EN 16931 → DE-XRECHNUNG`, structurally the
same shape as the DCAT chain (`INTL-DCAT → EU-DCAT-AP → NL-DCAT-AP-NL`)
that Batch 15 called the template the Atlas needs more of.

It is logged in `discovery/unresolved.md` as high-value and low-effort:
one page read would probably establish it.

## Relationships

- Maintained by [[DE-KOSIT]].
- `based-on` [[DE-XOEV]].

## Sources

Listed in frontmatter — only three, one of them an IT vendor page.
Wikipedia carries more of this entity than is comfortable, and the KoSIT's
own page cited is about operations and support rather than the standard's
substance.
