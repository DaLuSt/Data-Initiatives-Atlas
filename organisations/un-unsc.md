---
id: UN-UNSC
type: organisation
name: United Nations Statistical Commission
alternative_names:
  - UNSC
  - UN Statistical Commission
  - StatCom
description: >
  The highest body of the global statistical system, established in 1946 and
  a functional commission of the United Nations Economic and Social Council.
  It brings together the chief statisticians of member states from around
  the world and is the highest decision-making body for international
  statistical activities, responsible for setting statistical standards and
  developing concepts and methods, including their implementation at
  national and international level. It consists of 24 member states elected
  by ECOSOC for four-year terms on the basis of equitable geographical
  distribution, and it oversees the work of the United Nations Statistics
  Division, which acts as its secretariat.

level: international
country: null
region: null

status: active
confidence: high
coverage: medium
verification: primary-source
organisation_role: standards-body

start_date: 1946-02-16
end_date: null
last_verified: "2026-09-18"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - UN
  - UN-UNSD
  - EU-EUROSTAT
  - UN-SDG-INDICATORS
relationships:
  - type: part-of
    target: UN
    source: fact
    evidence: "un.org/en/desa's 'Shaping the future of global statistics' page was read directly (2026-08-28) and confirms the Commission as 'the apex body responsible for the development of global statistical standards', 24 member states elected by ECOSOC on geographic balance, and UNSD as its secretariat — though this page itself states the Commission was 'established in 1947', not 1946. unstats.un.org/UNSDWebsite/statcom/ was fetched but returned only a bare page-title shell ('UNSD - Welcome to UNSD') with no readable body content. ecosoc.un.org and the officialstatistics.org handbook both returned HTTP 403. Wikipedia's UN Statistical Commission article was fetched directly as a substitute and states 1946 (without a resolution number), matching this entity's original year but contradicting the DESA page's 1947. The 1946/1947 discrepancy is resolved (2026-09-18, see below): the UN Dag Hammarskjöld Library's own Functional Commissions research guide, read directly, names the founding resolutions (E/RES/8(I), 16 February 1946; E/RES/8(II), 21 June 1946), and UNSD's own session archive, read directly, labels 1947 as the Commission's '1st Session' — DESA's 1947 describes when the Commission first convened, not when ECOSOC created it."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "United Nations Statistical Commission"
    url: "https://unstats.un.org/UNSDWebsite/statcom/"
    publisher: "United Nations Statistics Division (UNSD)"
  - title: "Shaping the future of global statistics"
    url: "https://www.un.org/en/desa/shaping-future-global-statistics"
    publisher: "United Nations Department of Economic and Social Affairs"
    accessed: "2026-08-28"
  - title: "Statistical Commission | Economic and Social Council"
    url: "https://ecosoc.un.org/en/events/2026/statistical-commission"
    publisher: "United Nations Economic and Social Council (ECOSOC)"
  - title: "United Nations Statistical Commission"
    url: "https://en.wikipedia.org/wiki/United_Nations_Statistical_Commission"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
  - title: "Functional Commissions — UN Economic and Social Council Documentation"
    url: "https://research.un.org/en/docs/ecosoc/functionalcommissions"
    publisher: "United Nations Dag Hammarskjöld Library"
    accessed: "2026-09-18"
  - title: "United Nations Statistical Commission — 1st Session (1947)"
    url: "https://unstats.un.org/unsd/statcom/1st-session/documents/"
    publisher: "United Nations Statistics Division (UNSD)"
    accessed: "2026-09-18"
---

# UNSC — United Nations Statistical Commission

> **Verified 2026-08-28, with an open discrepancy flagged rather than
> hidden.** Two of the four sources in the revised list are read directly:
> un.org's own DESA page, and Wikipedia's UNSC article (substituted for the
> 403-blocked ECOSOC and Handbook pages). They **disagree on the founding
> year** — DESA says 1947, Wikipedia says 1946 — and neither cites a
> resolution number.
>
> **Resolved 2026-09-18.** The UN Dag Hammarskjöld Library's own
> "Functional Commissions" research guide, read directly, names the exact
> resolutions: the Commission "Established by E/RES/8(I) of 16 and 18
> February 1946 and E/RES/8(II) of 21 June 1946." Separately, UNSD's own
> session archive, read directly, labels 1947 as the Commission's "1st
> Session" — resolving DESA's "1947" as the year the Commission first
> convened, not the year it was created. `start_date` moves from the prior
> `1946-01-01` placeholder to `1946-02-16`, the earlier resolution's date;
> `confidence` rises to `high`. See "The founding-year discrepancy,
> resolved" below.

## Description

The Statistical Commission is the **highest body of the global statistical
system**, established by ECOSOC resolutions **E/RES/8(I) (16 February
1946) and E/RES/8(II) (21 June 1946)** — see "The founding-year
discrepancy, resolved" below — and a functional commission of ECOSOC. It
brings together the chief statisticians of member states worldwide and is
the highest decision-making body for international statistical activities —
setting statistical standards and developing concepts and methods, including
their implementation nationally and internationally.

It consists of **24 member states elected by ECOSOC** for four-year terms on
equitable geographical distribution.

## This resolves an open modelling question

`discovery/unresolved.md` has carried it since Batch 13:

> *Should UNSD and the UN Statistical Commission be separate entities? UNSD
> is the secretariat; the Commission is the intergovernmental body. Folded
> into one on a single sourced sentence.*

They are now separate, because a source distinguishes them: **the Commission
oversees the work of UNSD**, and the Statistics Division of DESA **acts as
the Commission's secretariat**. One is an intergovernmental decision-making
body of 24 elected states; the other is a division of a UN department.

The split is not cosmetic. It is what allows [[EU-EUROSTAT]] to attach:
Eurostat is described as representing the EU **in the Commission**, which is
a forum, not in the Division, which is a secretariat. Folding the two
together had made that edge unstatable — the Atlas had a node for the
secretariat and none for the body Eurostat actually sits in.

**That is the same shape as the `EU-ESS` problem**, and the two together are
most of why the UN layer stayed an island: in both cases the refused edge
was pointing at a node that did not exist.

## The founding-year discrepancy, resolved

Reading un.org's own DESA page directly ("Shaping the future of global
statistics") had surfaced a genuine conflict: it states the Commission
"was established in 1947," not 1946. Wikipedia's UN Statistical Commission
article, and a WebSearch cross-check for "created in 1946 by Resolution
8(I) of ECOSOC," both pointed at 1946 instead — but neither cited a
resolution number, so the 1946 figure rested on secondary corroboration
rather than a primary text.

**Resolved 2026-09-18** with two direct reads that confirm the plausible
reconciliation already guessed at here: the UN Dag Hammarskjöld Library's
own "Functional Commissions" research guide gives the exact resolutions —
*"Established by E/RES/8(I) of 16 and 18 February 1946 and E/RES/8(II) of
21 June 1946"* — and UNSD's own session-documents archive labels 1947 as
the Commission's **"1st Session"**. The two are not in conflict: ECOSOC
created the Commission by resolution in February and June 1946, but the
Commission itself did not convene until 1947, and DESA's "1947" describes
the latter. `start_date` is set to **1946-02-16**, the earlier of the two
founding resolutions.

## Relationships

- `part-of` [[UN]].

Edges pointing here, recorded on the other entity in each case:

- [[UN-UNSD]] `governed-by` this Commission — the Commission oversees the
  Division's work.
- [[EU-EUROSTAT]] `participates-in` this Commission — **the first edge from
  the European layer into the UN layer in the Atlas's history.**
- [[UN-SDG-INDICATORS]] `governed-by` this Commission — the global indicator
  framework was designed under its supervision.

## Sources

Listed in frontmatter. The original four: two read directly in the
2026-08-28 pass (the DESA overview and, substituting for the 403-blocked
ECOSOC session page and Handbook chapter, Wikipedia's UNSC article); the
UNSD-hosted statcom page loaded only a bare title shell with no body
content. Two more added 2026-09-18, both read directly: the UN Dag
Hammarskjöld Library's Functional Commissions research guide (the
resolution numbers) and UNSD's own 1st-session archive page (the 1947
session label).
