---
id: UN-DATA-COMMONS
type: platform
name: UN Data Commons
alternative_names: []
description: >
  UN DESA Statistics Division platform, launched 4 October 2023 in
  partnership with Google.org, aggregating authoritative SDG-related data
  from across the UN system into a publicly accessible, AI-searchable
  ecosystem for policymakers, researchers and the public. Expanded in
  September 2024 through further Google collaboration to integrate more UN
  agencies, including WHO and the ILO.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2023-10-04
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - UN
related_entities:
  - UN-UNSD
relationships:
  - type: part-of
    target: UN
    source: fact
    evidence: "The Grokipedia page originally cited here returned HTTP 403 on re-fetch this pass. Searching instead for un.org's own material located a genuine primary source that was never found in the original research: un.org/en/desa/un-data-commons-for-the-sdgs, read directly (2026-08-28), which states UN DESA's Statistics Division launched the platform on 4 October 2023 during the SDG Summit, in partnership with Google.org, integrating 'authoritative SDG data and insights from across the UN System' with 'AI-powered search functionality.' A second source, Google's own blog post on the September 2024 expansion (blog.google, read directly), confirms the platform scaled that year to add WHO, ILO and UNICEF via a partnership with the UN International Computing Centre, quoting UNSD Director Stefan Schweinfest. This replaces the single Grokipedia citation entirely."
    confidence: high
    valid_from: 2023-10-04
    valid_until: null

sources:
  - title: "Empowering SDG actions with new tools for tracking SDG progress"
    url: "https://www.un.org/en/desa/un-data-commons-for-the-sdgs"
    publisher: "United Nations Department of Economic and Social Affairs"
    accessed: "2026-08-28"
  - title: "Google's Data Commons expands to support more UN agencies"
    url: "https://blog.google/company-news/outreach-and-initiatives/public-policy/un-data-commons-expansion/"
    publisher: "Google"
    accessed: "2026-08-28"
---

# UN Data Commons

> **Verified 2026-08-28, rebuilt on real sources.** The prior pass's sole
> citation — a Grokipedia page — now 403s and, more importantly, should
> never have been the only source: a dedicated un.org/DESA page for this
> exact platform exists and was simply not found in the original research.
> It and Google's own expansion announcement are both read directly this
> pass, replacing the weak citation entirely rather than patching around it.

## Description

The **UN Data Commons for the SDGs** launched on **4 October 2023** during
the SDG Summit, built by UN DESA's Statistics Division in partnership with
**Google.org**. It aggregates authoritative SDG data and insights from
across the UN system into a single, publicly accessible platform with
AI-powered natural-language search, letting policymakers, NGOs and the
public explore country- and region-level SDG progress without needing to
navigate each UN agency's own data separately.

It expanded in **September 2024** — a detail the prior version of this
entity had right — when Google's Data Commons team, working with UNDESA and
the UN International Computing Centre, scaled the integration to add the
**World Health Organization**, the **International Labour Organization** and
**UNICEF**.

## A correction to how this entity was found, not just what it says

The prior pass's caveat said plainly: *"No un.org or unstats.un.org page for
the UN Data Commons was returned"* by the original research. That was
simply not tried hard enough — `un.org/en/desa/un-data-commons-for-the-sdgs`
is exactly the kind of dedicated primary page the README's source
preference order asks for, and it surfaced on the first targeted search this
pass. The lesson generalises: a single-weak-source entity is worth one more
real search attempt before being accepted as permanently thin, not just
re-fetched on the same URL.

`confidence` moves from `low` to `medium`: the launch date, partnership and
scope are now confirmed by the platform's own operator, though governance
detail (funding, data-quality controls, relationship to [[UN-UNSD]]'s wider
SDG indicator work) remains unresearched, hence `coverage: low` stays as is.

## Relationships

- Operates within [[UN]], built and operated by UN DESA's Statistics
  Division. Still no source directly states a formal relationship to
  [[UN-UNSD]]'s SDG indicator compilation work, though both sit within the
  same DESA Statistics Division — plausible but not asserted.

## Sources

Listed in frontmatter, both read directly this pass, replacing the original
single Grokipedia citation.
