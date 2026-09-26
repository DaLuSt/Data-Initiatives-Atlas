---
id: INTL-OECD-CSSP
type: programme
name: OECD Committee on Statistics and Statistical Policy
alternative_names:
  - CSSP
  - OECD statistics committee
description: >
  The OECD's committee on statistics and statistical policy (CSSP),
  named by Eurostat as one of the key international forums in which it
  represents the European Union, alongside the United Nations
  Statistical Commission and the Conference of European Statisticians.
  Eurostat describes these international statistical agencies as
  cooperating to set up international standards for statistics, improve
  the comparability of statistical information, improve the
  coordination of international statistics-related activities, and
  support national statistical systems financially or technically.

level: international
country: null
region: null

status: active
confidence: high
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-26"
previous_version: null
successor: null

domains: []
organisations:
  - INTL-OECD
related_entities:
  - INTL-OECD
  - EU-EUROSTAT
relationships:
  - type: part-of
    target: INTL-OECD
    source: fact
    evidence: "CLOSES discovery/unresolved.md row #169. Confirmed by reading ec.europa.eu/eurostat's own 'Statistical cooperation – introduction' page directly (2026-09-26, both URL forms): 'Eurostat represents the EU in key international forums such as the United Nations Statistical Commission (UNSC), in the Conference of European Statisticians (CES) organised by the UNECE and in the OECD's committee on statistics and statistical policy (CSSP).' A direct read finds no 'CSTAT' anywhere on the page and no parallel passage describing Eurostat representing 'the European Commission' in any OECD body — the two-name, two-representation-claim premise this entity carried since creation rested on a search-engine summary marked 'NOT READ — search-only' and does not survive an actual read of the cited page. Independently, the OECD's own BodyID 7229 page, read directly 2026-09-05 and again 2026-09-18, names only 'CSSP' and labels participation '(EU)', not '(European Commission)' — both of this entity's own primary sources now agree on both points."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Statistical cooperation — introduction"
    url: "https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Statistical_cooperation_-_introduction"
    publisher: "Eurostat — European Commission"
    accessed: "2026-09-26"
  - title: "Statistical cooperation — introduction (alternate path)"
    url: "https://ec.europa.eu/eurostat/statistics-explained/index.php/Statistical_cooperation_-_introduction"
    publisher: "Eurostat — European Commission"
    accessed: "2026-09-26"
  - title: "Committee on Statistics and Statistical Policy — On-Line Guide to OECD Intergovernmental Activity"
    url: "https://oecdgroups.oecd.org/Bodies/ShowBodyView.aspx?BodyID=7229&Lang=en"
    publisher: "OECD"
    accessed: "2026-09-05"
---

# OECD Committee on Statistics and Statistical Policy

> **Verified 2026-08-21.** Every source this entity cites is on a domain the
> repository owner confirmed read and correct — `europa.eu`. `verification:
> primary-source`. See `docs/re-verification.md` §"The confirmed domains".
>
> **Updated 2026-09-05**: the previously-flagged gap — no OECD source cited
> — is closed. See below.
>
> **Partly closed 2026-09-18** (`discovery/unresolved.md` row #169): the
> "EU or Commission" half of the naming question is narrowed — the OECD's
> own page labels the participation "EU". See "The EU, not the
> Commission — on the OECD's own page" below.
>
> **Fully closed 2026-09-26**: Eurostat's own cooperation page, previously
> cited but never read directly (marked "search-only"), was read directly
> for the first time. It does not contain the "CSTAT"/"Commission"
> passage this entity had carried since creation — that premise came
> from an unread search summary and does not survive contact with the
> actual page. `alternative_names` no longer carries "CSTAT";
> `confidence` raised to `high`.

## Description

The CSSP is the OECD's committee on statistics and statistical policy. It is
recorded here because [[EU-EUROSTAT]]'s own cooperation page names it as one
of three forums in which Eurostat represents the European Union — with the
[[UN-UNSC]] and the [[UN-CES]].

## Why a non-UN body is in a UN-layer batch

`discovery/candidates.md` predicted this and it held:

> *The same Eurostat page reportedly names the CSSP alongside the UNSC and
> CES — so **one page read may close the OECD gap and the UN gap
> together**.*

[[INTL-OECD]] had sat in the Atlas since Batch 13 **with no instrument
beneath it and no relationship to anything**. It was as isolated as the UN
layer and attracted less attention because it is one node rather than nine.
The same sentence that connects Eurostat to the UN statistical system
connects it here.

## The name was never actually unsettled — that came from an unread summary

This entity was created carrying **two different names and acronyms** for
what was assumed to be the same body — "CSSP" and "CSTAT" — plus two
different claims about who is represented ("the EU" vs. "the European
Commission"), both attributed to "a parallel passage on the same Eurostat
page." That evidence was explicitly marked `NOT READ — search-only` at
the time.

**Reading the page directly, 2026-09-26, finds no such parallel
passage.** Eurostat's own page names only **CSSP** and states only that
Eurostat "represents the EU" in it — the same wording, the same forum,
no second name and no second representation claim anywhere on the page.
The "CSTAT"/"Commission" pairing was a search-engine-summary artifact
that this entity carried, honestly flagged as unread, for over a month
before anyone actually opened the source it was attributed to.

`coverage: low` remains: the committee's composition, meeting cadence and
outputs beyond its mandate statement are still unrecorded.

## An OECD source, found 2026-09-05

The gap flagged above — no OECD source cited at all, the committee
described only from the outside by a participant — is now closed. The
OECD's own "On-Line Guide to OECD Intergovernmental Activity" (
`oecdgroups.oecd.org`, BodyID 7229), read directly, confirms the official
name is exactly **"Committee on Statistics and Statistical Policy
(CSSP)"** and states its mandate: the Committee is *"responsible to
Council for the OECD's statistical policy, both within the Organisation
and vis-à-vis the rest of the world,"* supporting *"policy-making on the
basis of high quality, internationally comparable data and evidence-based
analysis."* It reports to the **OECD Council**, not directly to a body
called [[INTL-OECD]] as a whole, though `part-of` [[INTL-OECD]] remains
the closest available Atlas relationship for a body reporting to that
organisation's own governing Council.

**The CSSP/CSTAT naming question, resolved 2026-09-26.** The OECD's own
page never mentioned "CSTAT" either — only "CSSP" appears there too. Both
of this entity's primary sources, now both read directly, agree: the
body is CSSP, full stop. `confidence` moved from `low` to `medium` on
2026-09-05 for the OECD-side confirmation, and to `high` on 2026-09-26
once Eurostat's own page was read directly and found not to contain the
competing name at all.

## The EU, not the Commission — on the OECD's own page — 2026-09-18

The second half of row #169 asked which of Eurostat's two descriptions is
right: does the CSSP represent "the EU" or "the Commission"? Re-reading
the same OECD page already cited (BodyID 7229) in full, rather than only
its mandate statement, finds the answer on the OECD's own side rather than
Eurostat's: *"The European Union (EU) takes part in the work of the OECD,
in accordance with the Supplementary Protocol to the Convention on the
Organisation for Economic Co-operation and Development."* The page's own
Bureau listing names a member's affiliation as **"(EU)"**, not "(European
Commission)".

This corroborates the "EU" framing independently of Eurostat's page.
**Closed 2026-09-26**: the "parallel Eurostat passage describing
Commission representation" this section once hedged around does not
exist — see "The name was never actually unsettled" above. Both of this
entity's primary sources agree the participation is described as "the
EU," and row #169 is fully closed for this entity.

## Relationships

- `part-of` [[INTL-OECD]].

[[EU-EUROSTAT]] carries the `participates-in` edge pointing here.

## Sources

Three sources: two are the same Eurostat page under its two URL forms
(recorded honestly rather than padded out), both read directly for the
first time 2026-09-26 after being carried as unread search-only citations
since creation; and the OECD's own committee page, read directly
2026-09-05 and again in full 2026-09-18.
