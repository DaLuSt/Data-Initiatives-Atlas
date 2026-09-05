# Candidates

Entities that appear potentially relevant but have not yet been researched
and sourced enough to add to the graph. Move a row here to a real entity
file once it has a `type`, an ID, at least one authoritative source, and a
clear enough relationship to the rest of the graph — then delete the row.

Do not add anything here without noting where it was seen.

> **Nothing on this page has been read.** Rows were compiled from
> search-engine results; the pages cited in *Where seen* were returned by a
> search index and confirmed to exist, but page retrieval is blocked
> (`EGRESS_BLOCKED`, 403 at the proxy tunnel). **These are leads, not
> findings.**

> **Proposed IDs are written in `backticks`, not `[[wikilinks]]`.** A
> wikilink to an entity that does not exist fails Obsidian navigation, and
> `validate_links` does **not** scan `discovery/` — so wikilinks here are
> unchecked by tooling and must be verified by hand.

> **Rows are removed when they close, not struck through.** The record of
> what closed and why lives in `progress/completed.md` and on the entities
> themselves.

---

## Status: worked through 2026-08-21 (twice), then 2026-09-05

Two batches ran on 2026-08-21.

The **candidate-clearing batch** acted on this page and closed **eleven**
rows, emptying three whole sections — the EEA and Switzerland section, the
EU↔UN vocabulary section, and the unused entity types. Sixteen entities.

The **follow-on batch** then closed the two largest things this page had left
open: the `measures` relationship type and the `level` vocabulary,
and acted on the domain coverage measured. Fourteen more entities.

**A third batch ran 2026-09-05**, emptying the entire carried-leads section
except for one name (DESA). Nine new/re-verified entities: [[UN-CCL]],
[[UN-GLOBAL-PLATFORM]], [[UN-ITU-X509]], [[UN-WHO]] (+ [[UN-WHO-GHO]]),
[[UN-UNDP]], [[UN-IMO]] (+ [[UN-IMO-GISIS]]) newly created; [[UN-UNCTAD]]
and [[UN-GDC]] promoted to `primary-source` on the strength of `un.org`'s
own official text. The INSPIRE↔UN-GGIM edge (§1) was attempted again and
remains genuinely open — the one item on this page that keeps resisting
closure across three separate passes.

What remains below is what is genuinely still open. **Section 6's
ontology-gap table is now the largest thing on this page**, and every row in
it is a modelling decision rather than research.

---

## 1. Still open — the INSPIRE ↔ UN-GGIM edge

[[EU-EUROGEOGRAPHICS]] now exists and the geospatial cluster has its middle
layer: five national mapping and cadastral authorities attach to it by
`participates-in`, mirroring [[EU-ESS]] for statistics. **The edge from the
European instrument to the UN structure still does not exist**, and creating
EuroGeographics did not create it.

| Name | Suspected type | Suspected scope | Why it might matter | Where seen | Noted by / date | Status |
|---|---|---|---|---|---|---|
| **[[EU-INSPIRE]] → the UN-GGIM structure** | relationship | — | The one edge that would finish the geospatial vertical. What exists is a 2016 EuroGeographics presentation *about* UN-GGIM delivered to an INSPIRE audience, and general discussion of INSPIRE harmonisation in UN-GGIM: Europe working groups. **That is evidence the communities talk, not that the instruments relate**, and no edge was asserted | un-ggim-europe.org working groups; eurogeographics.org INSPIRE KEN deck | UN batch / 2026-08-16; re-checked 2026-08-21, 2026-09-05 | **Open — needs a real source** |

**Creating the missing node did not close this one, and that is the useful
finding.** [[EU-ESS]] closed five refused edges because the missing node was
what every one of them had been pointing at. Here the missing node was also
genuinely missing — but it was never what this refusal turned on. The two
cases look identical on this page and are not.

The nearest thing to a bridge that now exists is incidental: [[GB-OS]]
carries `participates-in` to **both** [[UN-GGIM]] and
[[EU-EUROGEOGRAPHICS]]. A path through a shared member is not a relationship
between the instruments.

**2026-09-05 attempt, also inconclusive.** An academic source (an MDPI
article on cadastral mapping in Europe) surfaced a specific-sounding claim
— that a UN-GGIM: Europe core-data working group selected geospatial
themes "from the list of the INSPIRE annexes" — but the article itself
returned HTTP 403 on every attempt, so it was never actually read. Chasing
it to `un-ggim-europe.org`'s own current working-groups page found no
"core data" group by that name (the current three are Frameworks, Geodesy
Supply Chain, and Data for Global Agendas — the group structure may have
been renamed since whatever the article described), and the specific PDF
search turned up (`UN-GGIM-Europe_WGA_Recommandation_Content_SU_v1.0.pdf`)
404s. Still open.

## 2. Closed — `measures` was added the same day

[[EU-DESI]] and [[EU-EGOV-BENCHMARK]] carried no edge to any country they
measure, because no relationship type meant "measures". This section argued
for waiting: *"a type added in the same batch that creates its only users has
not been tested against anything."*

**`measures` was added on 2026-08-21**, in the follow-on batch, and the two
publications now carry **62 edges** — 27 from DESI and 35 from the benchmark.
`metadata/relationship-types.md` carries the definition; the edges rest on
each publication's sourced scope rule rather than on 62 individual sources,
which is the same basis [[NL-NEN]] attaches to [[EU-CEN]] on.

The one-batch separation cost nothing and is worth keeping as the pattern:
`cooperates-with` was added on a single example because it had one instance
and no scaling consequence; `measures` immediately wanted 62 edges and got a
batch of separation from the entities that would use it.

## 3. Closed 2026-09-05 — five of six carried leads

Five of the six rows this section used to carry are now closed, each with
a directly-read primary source rather than the WebSearch snippets or
unopened pages that had left them as "weak" or "carried" leads:

- **UN/CEFACT Core Component Library** → [[UN-CCL]]. `interoperable-europe.
  ec.europa.eu` (reached via a redirect from `joinup.ec.europa.eu`, since
  `unece.org` itself remains 403-blocked) supplied real substance where
  earlier searches had found only a name.
- **UN Global Platform / Committee of Experts on Big Data** →
  [[UN-GLOBAL-PLATFORM]]. `unstats.un.org`'s own Big Data page, read
  directly, named [[UN-UNSD]] as the manager and UN-CEBD as the governing
  committee (not separately modelled).
- **ITU standards** → [[UN-ITU-X509]], the PKI recommendation jointly
  published with [[INTL-ISO]] as ISO/IEC 9594-8, confirmed on `itu.int`'s
  own recommendation page.
- **UNCTAD data governance work** → resolved on [[UN-UNCTAD]]'s own file,
  promoted to `primary-source`: `un.org`'s own "Annex I: Global Digital
  Compact" page (UN General Assembly resolution A/RES/79/1) quotes
  paragraph 48 verbatim, requesting the CSTD establish the working group.
  [[UN-GDC]] was itself re-verified and enriched the same pass.
- **IMO, GISIS and the SafeSeaNet codes** → [[UN-IMO]] and
  [[UN-IMO-GISIS]]. `imo.org`'s own page confirmed IMO's substantive
  mandate as a full UN specialised agency — clearing the bar this section
  had explicitly said "one code list" would not clear — and
  `gisis.imo.org`'s own page confirmed GISIS itself.

**UN DESA, UNDP, WHO** was a three-name row; two of the three are now
modelled. [[UN-WHO]] (plus its [[UN-WHO-GHO]] platform) and [[UN-UNDP]]
were both confirmed via `who.int` and `sdgs.un.org` (an official UN
subdomain — `undp.org` itself 403'd) read directly. **DESA remains
unmodelled**: it is a broad UN Secretariat department already represented
in the Atlas through several of its divisions ([[UN-UNSD]], and
[[UN-UNCTAD]]'s CSTD work), and no source read this pass gave DESA itself
a distinct enough identity to warrant its own entity separate from those.

| Name | Suspected type | Suspected scope | Why it might matter | Where seen | Noted by / date | Status |
|---|---|---|---|---|---|---|
| **UN DESA** — no ID proposed | organisation | UN, `level: international` | Named in Batch 13's scope; WHO and UNDP (named alongside it) are now modelled, DESA itself is not | Batch 13 scope | Batch 13; carried; narrowed 2026-09-05 | Carried lead |

## 4. Entity types and levels (re-measured 2026-08-21)

`technology` and `publication` were both on this list and are both now in
use — [[INTL-X-ROAD]] for the first, [[EU-DESI]], [[EU-EGOV-BENCHMARK]] and
[[EU-VOLUNTARY-REVIEW-2023]] for the second. **All 17 entity types are now
in use.**

The **`level` vocabulary gained a sixth value on 2026-08-21**: `subnational`,
for the tier below the state and above the municipality. It has four uses —
the three Belgian sub-federal Open Data Directive instruments and the 2016
Brussels ordonnance one of them amends. See
`metadata/controlled-vocabularies.md` §`level` for why `local` would have been
the wrong answer.

| Item | Measurement | Why it matters | Status |
|---|---|---|---|
| **`level: local`** | **0 uses**, against 385 `national`, 69 `regional`, 52 `international`, 6 `sectoral` and 4 `subnational` | **No longer the blocker it was.** What blocked Flanders, the Comunidades Autónomas and the German Länder was that `regional` means *supra*-national here and nothing meant *sub*-national; `level: subnational` was added 2026-08-21 and those three became ordinary research. `local` remains unused and now gates one thing only — the Dutch municipalities — where the open question is **what entity to create**, not what to call it | Open (design), much narrower |
| **`level: sectoral`** | 6 uses | Barely exercised. Whether that reflects the subject matter or under-use is unexamined | Later |
| **`region` entities** | **1** — only [[EU]] | EFTA, the Nordic Council, the Council of Europe and Benelux are absent. The **EEA** is now modelled as [[INTL-EEA-AGREEMENT]] (`type: law`) rather than as a region, which turned out to be the more useful shape: [[INTL-EEA-JCD-154-2018]] `amends` it, and an amendment to a region would be meaningless | Later |

## 5. Domain coverage (re-measured 2026-08-21, after the health batch)

Counted as **distinct countries having at least one entity that lists the
domain**, across all 58 country anchors:

| Domain | Countries | Change this batch |
|---|---|---|
| [[DOMAIN-GOVERNMENT]] | 21 | — |
| [[DOMAIN-CYBERSECURITY]] | 13 | — |
| [[DOMAIN-NATIONAL-SECURITY]] | 8 | — |
| [[DOMAIN-GEOSPATIAL]] | 6 | — |
| [[DOMAIN-HEALTH]] | **5** | **from 1** |
| [[DOMAIN-MOBILITY]] | 2 | — |
| [[DOMAIN-RESEARCH]] | **2** | **from 1** |
| [[DOMAIN-EDUCATION]] | **2** | **from 1** |

The three domains that stood at **1 of 58** are the three that moved. Health
was called *"the single largest correction available"* and got four new
countries: [[DE]], [[FR]], [[FI]] and [[DK]], each with a materially
different national regime — pool, license, custody — which is recorded on
[[DOMAIN-HEALTH]].

**[[DOMAIN-MOBILITY]] is now the thinnest at 2**, and unlike health it has no
obvious set of national counterparts to add: [[EU-EMSWE]] and [[UN-LOCODE]]
are both supra-national, and the national mobility layer would be transport
ministries and traffic-data agencies that no batch has surveyed.

## 6. Ontology gaps

| Gap | Why it matters | Noted | Status |
|---|---|---|---|
| **No way to model enforcement against a member state.** | Nineteen member states faced infringement proceedings over [[EU-OPEN-DATA-DIRECTIVE]], and four were referred to the Court of Justice in February 2023. The Atlas has no entity type for an infringement procedure, no relationship type for it, and no **Court of Justice of the European Union** entity. Non-compliance is a large part of how EU data law actually operates and none of it is visible | 2026-08-18 | **Open — would need a type, a relationship and at least one new entity** |
| **`type: law` flattens primary and secondary legislation.** | [[IE-PSI-REGULATIONS-2021]] is a statutory instrument; [[IE-DPA-2018]] is an Act. Both are `law`. The same flattening applies to Portuguese decreto-lei versus lei, to German Gesetz versus Verordnung, and now to [[INTL-EEA-JCD-154-2018]], which is a Joint Committee *decision* filed as a `law` | 2026-08-18; extended 2026-08-21 | Open |
| **`implements-requirement-from` cannot say "supplements".** | [[LI-DSG]] does not transpose the GDPR — the GDPR is directly applicable in Liechtenstein — it exercises the regulation's national opening clauses. The edge asserted is the closest available type and slightly overstates, which is recorded on the entity. A `supplements` type would today have exactly one instance | 2026-08-21 | Open (vocabulary) |
| **No way to record "modelled on".** | [[LI-DSG]] is described by its sources as modelled on the German BDSG. `based-on` claims the legislature adapted a specific text, which is more than a law-firm commentary supports. Left in prose | 2026-08-21 | Open |

---

## What the cheap structural fixes taught, for the record

The four "cheap structural fixes" identified on 2026-08-18 — national DPAs to
[[EU-EDPB]], [[FR-INSEE]], the four missing national standards bodies, and
the Dutch and Polish cyber authorities — were all completed in the batch of
2026-08-18. Their rows are gone. **What they taught is kept**, because it has
since proved right twice more.

**What actually unlocked the DPA fix.** The edge had been refused on
[[DE-BFDI]] because the German representation arrangement — which authority
represents a member state with seventeen of them — "should not be guessed
at". The answer was in [[EU-GDPR]] **Article 68(3)** all along: the Board is
composed of the head of one supervisory authority per member state plus the
[[EU-EDPS]], *and where a member state has more than one authority, a joint
representative is appointed under that member state's law.* The provision
that creates the Board anticipates the exact case that had blocked the edge.

The [[IE-NSAI]] refusal closed the same way: not by reading the CEN member
list the Atlas cannot retrieve, but by finding CEN-CENELEC's **statement of
the rule** — its national members are the standardization bodies of the 27 EU
countries. Membership follows from the rule.

**Both are the same lesson: a refusal for want of a source is not the same as
a fact being unknowable**, and the source is sometimes in the instrument that
created the thing.

Two more instances, from 2026-08-21:

- **The 2030 Agenda** was refused as "nothing found beyond passing
  references". It had been searched for on Eurostat's SDG pages, where it
  appears only as context. Searching for the **resolution** — A/RES/70/1 —
  returns the resolution. It is now [[UN-2030-AGENDA]].
- **The EEA supervisory authorities' seat at the [[EU-EDPB]]** is asserted
  for [[IS-PERSONUVERND]] and [[LI-DATENSCHUTZSTELLE]] on the same kind of
  composition rule: [[INTL-EEA-JCD-154-2018]] states that the supervisory
  authorities of the EFTA States participate in the Board's activities.
