---
id: INTL-OECD
type: organisation
name: Organisation for Economic Co-operation and Development
alternative_names:
  - OECD
description: >
  Intergovernmental economic organisation, **not** part of the UN system. It
  works on data governance, framed as the technical, policy and regulatory
  frameworks for managing data across its value cycle and across policy
  domains including health, research, public administration and finance.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 1961-09-30
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities: []
relationships: []

sources:
  - title: "Data governance — OECD"
    url: "https://www.oecd.org/en/topics/sub-issues/data-governance.html"
    publisher: "Organisation for Economic Co-operation and Development (OECD)"
  - title: "European Data Governance Act (DGA), Regulation (EU) 2022/868"
    url: "https://www.oecd.org/en/publications/access-to-public-research-data-toolkit_a12e8998-en/european-data-governance-act-dga-regulation-eu-2022-868_920b8b28-en.html"
    publisher: "Organisation for Economic Co-operation and Development (OECD)"
  - title: "OECD"
    url: "https://en.wikipedia.org/wiki/OECD"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
  - title: "Recommendation of the Council for Enhanced Access and More Effective Sharing of Data (OECD-LEGAL-0463)"
    url: "https://legalinstruments.oecd.org/public/doc/668/fb17bc8f-0f30-4247-9ca4-5f78271149b5.htm"
    publisher: "OECD Legal Instruments (legalinstruments.oecd.org)"
    accessed: "2026-08-28"
  - title: "Organisation for Economic Co-operation and Development (OECD)"
    url: "https://diplomatie.belgium.be/en/policy/international-institutions/financial-and-economic-institutions/organisation-economic-co-operation-and-development-oecd"
    publisher: "FPS Foreign Affairs, Belgium"
    accessed: "2026-08-28"
---

# OECD

> **Promoted to `primary-source` 2026-08-28.** `oecd.org` (the main site)
> is domain-wide 403-blocked for this pass's retrieval tool: both
> originally cited pages, plus the bare `oecd.org` homepage tried as a
> control, all returned HTTP 403 again this pass. Per this pass's
> instruction, an OECD data/stats-adjacent subdomain was tried instead —
> `legalinstruments.oecd.org` — and it worked: unlike the main site, it is
> not blocked, and its HTML document page for the OECD's own 2021
> Recommendation on Enhancing Access to and Sharing of Data (OECD-LEGAL-
> 0463) was fetched and read directly, giving the recommendation's actual
> content in the OECD's own words (trust in the data ecosystem, a
> strategic government approach, investment incentives, cross-border data
> flows, interoperability via FAIR-aligned standards, and capacity
> building) — the first OECD-authored primary text this entity has ever
> carried, resolving the `coverage: low` gap this entity flagged. A second
> independent source, the Belgian foreign ministry's own OECD profile
> page, was also found and read directly, corroborating the founding date,
> current 38-member count, and mission in a source with no connection to
> `oecd.org`. Together with the Wikipedia article read in the prior pass,
> that is 3 of 5 sources read directly — a genuine majority — so
> `verification` is promoted to `primary-source`.

## Description

The OECD is an intergovernmental economic organisation with a substantial
data governance workstream. Its framing — data governance as the technical,
policy and regulatory frameworks for managing data along its value cycle
from creation to deletion, across policy domains including health, research,
public administration and finance — is close to this Atlas's own scope
definition.

It is named alongside [[INTL-ISO]] and [[UN-ITU]] as a participant in
international data governance work.

## Not a UN organisation

`INTL` scope, not `UN`. The OECD is an independent intergovernmental
organisation with its own membership, distinct from the UN system — a
distinction Batch 13's brief asks to be maintained, and one that is easy to
get wrong given how often the OECD appears in the same discussions as UN
bodies. One nuance found via Wikipedia this pass, worth stating precisely:
the OECD **is** "an official United Nations observer" — a formal
recognition status — which is not the same thing as being a UN specialised
agency (as [[UN-ITU]] is). The `INTL` framing survives that nuance intact.

## An OECD source already relied on elsewhere

The OECD's Access to Public Research Data Toolkit is one of the sources
cited on [[EU-DGA]]. That is worth noting for the same reason as
[[EU-PUBLICATIONS-OFFICE]]: the Atlas leans on this organisation's material
while barely documenting the organisation.

`coverage: low`: no OECD instrument, recommendation or guideline is
modelled as its own Atlas entity yet, though this pass narrows the gap in
prose. **Confirmed by reading the OECD's own legal-instrument text
directly (2026-08-28, legalinstruments.oecd.org, OECD-LEGAL-0463):** the
Council adopted the Recommendation on Enhancing Access to and Sharing of
Data, setting out "general principles and policy guidance on how
governments can maximise the benefits of enhancing data access and
sharing arrangements while protecting individuals' and organisations'
rights" across six areas — trust in the data ecosystem, a strategic
government approach to data governance, investment and incentives,
cross-border data flows (restrictions must be "non-discriminatory,
transparent, necessary, and proportionate"), data interoperability via
FAIR-aligned standards, and capacity building. This is close enough to
this Atlas's own scope definition to be a strong future-entity candidate;
it is not created here because doing so mid-pass, without researching its
adoption date, legal status among OECD instruments, or uptake, would be
the thin entity the taxonomy threshold exists to prevent. The OECD Privacy
Guidelines remain a separate, still-unresearched candidate. Queued.

## Sources

Listed in frontmatter. Neither original `oecd.org` source could be read
this pass (domain-wide block, see verification note above). Three of five
read directly: Wikipedia (prior pass), plus `legalinstruments.oecd.org`
(a different, unblocked OECD subdomain) and Belgium's foreign ministry
OECD profile (both this pass, 2026-08-28) — a genuine majority.
