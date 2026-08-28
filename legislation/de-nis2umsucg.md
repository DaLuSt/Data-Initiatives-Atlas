---
id: DE-NIS2UMSUCG
type: law
name: NIS-2-Umsetzungsgesetz
alternative_names:
  - NIS2UmsuCG
  - Gesetz zur Umsetzung der NIS-2-Richtlinie und zur Regelung wesentlicher Grundzüge des Informationssicherheitsmanagements in der Bundesverwaltung
  - German NIS2 Implementation Act
description: >
  German act implementing the EU NIS2 Directive and regulating the
  essentials of information security management in the federal
  administration. Announced in the Bundesgesetzblatt on 5 December 2025 and
  in force from 6 December 2025 with no transition period. Rather than
  creating a separate statute it comprehensively revised the existing
  BSI-Gesetz, expanding the population supervised by the BSI from roughly
  4,500 to roughly 29,500 entities across 18 sectors.

level: national
country: DE
region: EU

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: 2025-12-06
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations:
  - DE-BSI
related_entities:
  - EU-NIS2
  - DE-BSIG
  - NL-CBW
relationships:
  - type: implements-requirement-from
    target: EU-NIS2
    source: fact
    evidence: "Confirmed by reading the BSI's own press release directly (2026-08-28): 'Cybersicherheitsrecht: NIS-2-Umsetzungsgesetz ab morgen in Kraft' states the law was announced 5 December 2025 and takes effect the following day, expanding BSI oversight from roughly 4,500 to roughly 29,500 entities. OpenKRITIS's own page, read directly, gives the law's full title as implementing the NIS-2 Directive and regulating federal-administration information security management, and Deloitte's own page, read directly, confirms this is Germany's transposition of the EU NIS2 Directive."
    confidence: high
    valid_from: 2025-12-06
    valid_until: null
  - type: supersedes
    target: DE-BSIG
    source: fact
    evidence: "Confirmed by reading Deloitte's own page directly (2026-08-28): 'Dabei wurde kein eigenständiges NIS-2-Gesetz geschaffen, stattdessen erfolgte eine umfassende Revision des bestehenden BSI-Gesetzes' (no standalone NIS2 law was created; instead a comprehensive revision of the existing BSI-Gesetz was carried out), with adjustments to other sector-specific regulations. OpenKRITIS's page, also read directly, uses similar language ('Das bisherige BSI-Gesetz tritt in der alten Fassung dann außer Kraft') describing the same amendment mechanism. See the entity body: this is an amendment lineage, not a repeal, and `supersedes` is recorded at low confidence for exactly that reason."
    confidence: low
    valid_from: 2025-12-06
    valid_until: null

sources:
  - title: "Cybersicherheitsrecht: NIS-2-Umsetzungsgesetz ab morgen in Kraft"
    url: "https://www.bsi.bund.de/DE/Service-Navi/Presse/Pressemitteilungen/Presse2025/251205_NIS-2-Umsetzungsgesetz_in_Kraft.html"
    publisher: "Bundesamt für Sicherheit in der Informationstechnik (BSI)"
    accessed: "2026-08-28"
  - title: "Umsetzung der EU-Direktive NIS2 in Deutschland (NIS2-Umsetzungsgesetz)"
    url: "https://www.deloitte.com/de/de/services/consulting-risk/perspectives/umsetzung-eu-direktive-nis2-nis2umsucg.html"
    publisher: "Deloitte Deutschland"
    accessed: "2026-08-28"
  - title: "NIS2-Umsetzungsgesetz in Deutschland 2025"
    url: "https://www.openkritis.de/it-sicherheitsgesetz/nis2-umsetzung-gesetz-cybersicherheit.html"
    publisher: "OpenKRITIS"
    accessed: "2026-08-28"
  - title: "Bundestag verabschiedet NIS-2-Umsetzungsgesetz"
    url: "https://www.twobirds.com/de/insights/2025/germany/german-bundestag-passes-german-nis-2-implementation-act"
    publisher: "Bird & Bird"
  - title: "Umsetzungsgesetz der NIS-2-Richtlinie in Kraft getreten"
    url: "https://www.dnv.de/news/2025/nis-2-umsetzungsgesetz/"
    publisher: "DNV Deutschland"
---

# NIS-2-Umsetzungsgesetz (NIS2UmsuCG)

> **Re-verified 2026-08-28.** Three of five cited pages read directly,
> including the BSI's own press release. `twobirds.com` returned HTTP 402
> (paywalled) and `dnv.de` HTTP 403 on two attempts each — both treated as
> genuinely blocked rather than silently dropped. Three of five is a
> genuine majority. `verification: primary-source`; `confidence` raised to
> `high` on the `implements-requirement-from` edge.

## Description

Germany's implementation of [[EU-NIS2]] was, per the BSI's own press
release (read directly), **announced in the Bundesgesetzblatt on 5
December 2025 and entered into force on 6 December 2025**, with **no
transition period**.

Its full title — *Gesetz zur Umsetzung der NIS-2-Richtlinie und zur
Regelung wesentlicher Grundzüge des Informationssicherheitsmanagements in
der Bundesverwaltung* — shows it doing two jobs: transposing the directive,
and regulating information security management within the federal
administration itself, confirmed directly this pass on OpenKRITIS's page.

Rather than a standalone statute, Germany undertook a **comprehensive
revision of the existing [[DE-BSIG]]**, with consequential adjustments to
other sector-specific regulations — confirmed directly this pass on
Deloitte's own page in its own words ("kein eigenständiges NIS-2-Gesetz
geschaffen"). The regulated population grew from roughly **4,500 to
roughly 29,500 entities**, confirmed directly on the BSI's own press
release, which also confirms new registration and incident-reporting
obligations (registration via "Mein Unternehmenskonto" and a dedicated BSI
reporting portal launching 6 January 2026) not previously recorded on this
entity.

## Two transpositions of one directive, four months apart

This is the second national NIS2 implementation in the Atlas, and the pair
is more informative than either alone:

| | [[DE-NIS2UMSUCG]] | [[NL-CBW]] |
|---|---|---|
| In force | 6 December 2025 | 15 August 2026 |
| Legislative technique | revises the existing [[DE-BSIG]] | new act superseding [[NL-WBNI]] |
| Predecessor handling | amendment lineage | clean supersession |

The directive is one entity. The two national responses differ in timing
*and in kind* — one amends a standing law, the other replaces one — and the
Atlas can now show that without either country's model distorting the
other.

**No relationship between the two acts is asserted.** They are siblings
under [[EU-NIS2]], the same call made for [[DE-BDSG]] and [[NL-UAVG]].

## ⚠ `supersedes` → [[DE-BSIG]] is recorded at low confidence

This is the weakest modelling decision in the German batch and it is
flagged rather than smoothed over — and this pass's direct reading
reinforces rather than resolves the tension.

What the sources say is that the NIS2UmsuCG *comprehensively revised* the
BSIG — a Novelle, an amending act. Deloitte's own page, read directly, is
explicit that no standalone law was created. OpenKRITIS's page, also read
directly, states "[d]as bisherige BSI-Gesetz tritt in der alten Fassung
dann außer Kraft" — language that could be misread as a repeal but, read
alongside Deloitte's framing, describes the ordinary mechanism for a German
Änderungsgesetz that restates a law's text in full: the old wording lapses
the instant the new wording takes effect, while the statute itself
continues under the same name and citation. In German legislative terms the
BSIG continues to exist under its own name with new content; it was not
repealed and replaced with a differently-named instrument.

`supersedes` therefore overstates the case. The alternatives were:

- **`supersedes`** — overstates; the BSIG was not withdrawn.
- **`influences`** — badly understates a comprehensive rewrite.
- **omit** — loses the single most important fact about how Germany
  transposed the directive.
- **a new relationship type** for amending acts — the honest answer, and
  the one `metadata/relationship-types.md` §2.3 permits when a batch
  genuinely needs one. It was not created here because doing so on the
  strength of what remains an imperfectly-typed relationship, in a batch
  already re-verifying a whole country, risks adding vocabulary the Atlas
  then has to live with.

`supersedes` at `confidence: low` with the reasoning in the evidence field
was chosen as the least-bad option. **[[DE-BSIG]] is deliberately left at
`status: active`, not `superseded`** — which is inconsistent with the
relationship and is meant to be, because the law is in force. Logged in
`discovery/unresolved.md` as the German batch's principal open modelling
question.

Compare [[EU-EIDAS]] → [[EU-EIDAS2]], which the Atlas records as an
amendment lineage through `previous_version` / `successor` rather than
through `supersedes`. That mechanism was not used here because the BSIG
does not become a new entity — it is the same law, amended.

## Relationships

- Implements requirements from [[EU-NIS2]] — confirmed directly this pass,
  `confidence: high`.
- `supersedes` [[DE-BSIG]] — at low confidence, see above; reasoning
  reinforced by two directly-read sources this pass.

## Sources

Listed in frontmatter. One government source (BSI, read directly this
pass) and two commercial/sectoral commentators read directly (Deloitte,
OpenKRITIS). `twobirds.com` (HTTP 402, paywalled) and `dnv.de` (HTTP 403,
retried once) are genuinely blocked, not silently dropped. **No
Bundesgesetzblatt or Gesetze-im-Internet URL** was found by search this
pass either.
