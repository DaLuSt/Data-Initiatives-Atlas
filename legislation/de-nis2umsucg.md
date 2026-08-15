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
  administration. Published in the Bundesgesetzblatt on 5 December 2025 and
  in force from 6 December 2025 with no transition period. Rather than
  creating a separate statute it comprehensively revised the existing
  BSI-Gesetz, expanding the population supervised by the BSI from roughly
  4,500 to roughly 29,500 entities across 18 sectors.

level: national
country: DE
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2025-12-06
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
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
    evidence: "The Gesetz zur Umsetzung der NIS-2-Richtlinie und zur Regelung wesentlicher Grundzüge des Informationssicherheitsmanagements in der Bundesverwaltung implements the EU minimum cybersecurity standards of the NIS2 Directive into German law (bsi.bund.de press release 251205; deloitte.com; twobirds.com). NOT READ — search-only."
    confidence: medium
    valid_from: 2025-12-06
    valid_until: null
  - type: supersedes
    target: DE-BSIG
    source: fact
    evidence: "Rather than creating a separate NIS-2 law, a comprehensive revision (umfassende Novelle) of the existing BSI-Gesetz was undertaken, along with adjustments to other sector-specific regulations (openkritis.de; deloitte.com; twobirds.com). NOT READ — search-only. See the entity body: this is an amendment lineage, not a repeal."
    confidence: low
    valid_from: 2025-12-06
    valid_until: null

sources:
  - title: "Cybersicherheitsrecht: NIS-2-Umsetzungsgesetz ab morgen in Kraft"
    url: "https://www.bsi.bund.de/DE/Service-Navi/Presse/Pressemitteilungen/Presse2025/251205_NIS-2-Umsetzungsgesetz_in_Kraft.html"
    publisher: "Bundesamt für Sicherheit in der Informationstechnik (BSI)"
  - title: "Umsetzung der EU-Direktive NIS2 in Deutschland (NIS2-Umsetzungsgesetz)"
    url: "https://www.deloitte.com/de/de/services/consulting-risk/perspectives/umsetzung-eu-direktive-nis2-nis2umsucg.html"
    publisher: "Deloitte Deutschland"
  - title: "NIS2-Umsetzungsgesetz in Deutschland 2025"
    url: "https://www.openkritis.de/it-sicherheitsgesetz/nis2-umsetzung-gesetz-cybersicherheit.html"
    publisher: "OpenKRITIS"
  - title: "Bundestag verabschiedet NIS-2-Umsetzungsgesetz"
    url: "https://www.twobirds.com/de/insights/2025/germany/german-bundestag-passes-german-nis-2-implementation-act"
    publisher: "Bird & Bird"
  - title: "Umsetzungsgesetz der NIS-2-Richtlinie in Kraft getreten"
    url: "https://www.dnv.de/news/2025/nis-2-umsetzungsgesetz/"
    publisher: "DNV Deutschland"
---

# NIS-2-Umsetzungsgesetz (NIS2UmsuCG)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

Germany's implementation of [[EU-NIS2]] was **published in the
Bundesgesetzblatt on 5 December 2025 and entered into force on 6 December
2025**, with **no transition period**.

Its full title — *Gesetz zur Umsetzung der NIS-2-Richtlinie und zur
Regelung wesentlicher Grundzüge des Informationssicherheitsmanagements in
der Bundesverwaltung* — shows it doing two jobs: transposing the directive,
and regulating information security management within the federal
administration itself.

Rather than a standalone statute, Germany undertook a **comprehensive
revision of the existing [[DE-BSIG]]**, with consequential adjustments to
other sector-specific regulations. The regulated population grew from
roughly **4,500 to roughly 29,500 entities across 18 sectors**, all
supervised by [[DE-BSI]] and obliged to implement risk management, report
incidents and register with the BSI.

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
Atlas can now show that without either country's model distorting the other.

**No relationship between the two acts is asserted.** They are siblings
under [[EU-NIS2]], the same call made for [[DE-BDSG]] and [[NL-UAVG]].

## ⚠ `supersedes` → [[DE-BSIG]] is recorded at low confidence

This is the weakest modelling decision in the German batch and it is
flagged rather than smoothed over.

What the sources say is that the NIS2UmsuCG *comprehensively revised* the
BSIG — a Novelle, an amending act. In German legislative terms the BSIG
continues to exist under its own name with new content; it was not
repealed and replaced.

`supersedes` therefore overstates the case. The alternatives were:

- **`supersedes`** — overstates; the BSIG was not withdrawn.
- **`influences`** — badly understates a comprehensive rewrite.
- **omit** — loses the single most important fact about how Germany
  transposed the directive.
- **a new relationship type** for amending acts — the honest answer, and
  the one `metadata/relationship-types.md` §2.3 permits when a batch
  genuinely needs one. It was not created here because doing so on the
  strength of unread sources, in a batch already introducing a country,
  risks adding vocabulary the Atlas then has to live with.

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

- Implements requirements from [[EU-NIS2]].
- `supersedes` [[DE-BSIG]] — at low confidence, see above.

## Sources

Listed in frontmatter. One government source (BSI) and four commercial or
sectoral commentators. **No Bundesgesetzblatt or Gesetze-im-Internet URL**
— none was returned by search.
