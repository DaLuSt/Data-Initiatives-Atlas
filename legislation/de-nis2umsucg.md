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
last_verified: "2026-09-20"
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
  - type: amends
    target: DE-BSIG
    source: fact
    evidence: "ONTOLOGY DECISION 2026-09-20, closing discovery/unresolved.md items #7 and #68. Confirmed by reading Deloitte's own page directly (2026-08-28): 'Dabei wurde kein eigenständiges NIS-2-Gesetz geschaffen, stattdessen erfolgte eine umfassende Revision des bestehenden BSI-Gesetzes' (no standalone NIS2 law was created; instead a comprehensive revision of the existing BSI-Gesetz was carried out), with adjustments to other sector-specific regulations. OpenKRITIS's page, also read directly, uses similar language ('Das bisherige BSI-Gesetz tritt in der alten Fassung dann außer Kraft') describing the same amendment mechanism — the ordinary German Änderungsgesetz/Neufassung pattern, where old wording lapses the instant new wording takes effect while the statute continues under its own name and citation. This was originally recorded `supersedes` at `confidence: low` because no better type existed at the time; `amends` (metadata/relationship-types.md §2.1, added in the third research-queue batch, defined as 'modifies the text of another instrument, which continues to exist under its own name and date') was added later for an analogous shape (three of five Open Data Directive transpositions turning out to be amendments to pre-existing acts) but was never checked against this older, already-flagged case. It fits cleanly: this instrument comprehensively revised the BSIG's text; the BSIG continues to exist under its own name and 2009 enactment date; and this instrument separately carries `implements-requirement-from` → [[EU-NIS2]], matching the type's own description of an amending act 'typically carr[ying] both.'"
    confidence: high
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
>
> **Ontology decision, 2026-09-20**, closing `discovery/unresolved.md`
> items #7 and #68: the relationship to [[DE-BSIG]] moves from `supersedes`
> (`confidence: low`) to `amends` (`confidence: high`). See "The relationship
> to DE-BSIG, resolved" below — the type this entity's own text called "the
> honest answer" in the German batch was added later for a different case
> and never checked against this one.

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

## The relationship to DE-BSIG, resolved — 2026-09-20

This was the weakest modelling decision in the German batch, flagged
rather than smoothed over, and re-checked without resolution in the
2026-08-28 re-verification pass.

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

At the time this entity was written, the candidates were:

- **`supersedes`** — overstates; the BSIG was not withdrawn.
- **`influences`** — badly understates a comprehensive rewrite.
- **omit** — loses the single most important fact about how Germany
  transposed the directive.
- **a new relationship type** for amending acts — the honest answer, not
  created in the German batch itself to avoid adding vocabulary on the
  strength of one case while re-verifying a whole country.

That type now exists, just not built for this case: `amends`
(metadata/relationship-types.md §2.1) was added in the third
research-queue batch for three Open Data Directive transpositions that
turned out to be amendments to pre-existing national re-use acts. Nobody
went back to check it against this older, already-flagged German
question — until this pass. It fits without qualification: "modifies the
text of another instrument, which continues to exist under its own name
and date" is exactly the BSIG's situation, and the type's own description
of an amending act "typically carr[ying] both" `amends` and
`implements-requirement-from` matches this entity precisely.

**Closed as an ontology decision, 2026-09-20**: the edge moves from
`supersedes` (`confidence: low`) to `amends` (`confidence: high`). The
tension the old edge created — [[DE-BSIG]] left `status: active` despite
something "superseding" it — dissolves along with it: `amends` carries no
implication that the target retires, so `DE-BSIG`'s `active` status is now
simply correct, not a deliberate inconsistency requiring a footnote.

Compare [[EU-EIDAS]] → [[EU-EIDAS2]], which the Atlas records as an
amendment lineage through `previous_version` / `successor` rather than
through a relationship edge. That mechanism still does not fit here: the
BSIG does not become a new entity under this pass's resolution either — it
is the same law, amended, which is exactly what `amends` is for.

## Relationships

- Implements requirements from [[EU-NIS2]] — confirmed directly this pass,
  `confidence: high`.
- `amends` [[DE-BSIG]] — `confidence: high`, closed 2026-09-20 (previously
  `supersedes` at `confidence: low`); see above.

## Sources

Listed in frontmatter. One government source (BSI, read directly this
pass) and two commercial/sectoral commentators read directly (Deloitte,
OpenKRITIS). `twobirds.com` (HTTP 402, paywalled) and `dnv.de` (HTTP 403,
retried once) are genuinely blocked, not silently dropped. **No
Bundesgesetzblatt or Gesetze-im-Internet URL** was found by search this
pass either.
