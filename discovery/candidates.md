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

**A third batch ran 2026-09-05**, in two parts. The first emptied the
entire carried-leads section except for one name (DESA): nine
new/re-verified entities — [[UN-CCL]], [[UN-GLOBAL-PLATFORM]],
[[UN-ITU-X509]], [[UN-WHO]] (+ [[UN-WHO-GHO]]), [[UN-UNDP]], [[UN-IMO]]
(+ [[UN-IMO-GISIS]]) newly created; [[UN-UNCTAD]] and [[UN-GDC]] promoted
to `primary-source` on the strength of `un.org`'s own official text. The
INSPIRE↔UN-GGIM edge (§1) was attempted again and remained genuinely
open at that point. The second part worked the ontology-gaps table
(§6): added the `supplements` relationship type, closed the "modelled
on" row as a deliberate decision rather than a new type, and created
[[EU-CJEU]] — narrowing, not closing, the enforcement-modelling gap. A
third, small part narrowed §4's `region` entities row: [[INTL-EFTA]] and
[[INTL-COE]] turn out to already exist, just as `type: organisation`
rather than `type: region` — the same shape the EEA already taught was
more useful.

**A fourth pass, later the same day, closed everything this page had
left.** The INSPIRE↔UN-GGIM edge (§1) got a fourth independent attempt —
still no source found it directly, and it is now retired from this page
as a candidate and left as a permanent record in
`discovery/unresolved.md` instead, where "a relationship that seems
plausible but isn't directly sourced" is the correct home for it. **UN
DESA** (§3's last carried lead) was checked once more and declined for
the same reason already on record: a broad Secretariat department, "the
think tank of the UN," already represented through [[UN-UNSD]] and
[[UN-UNCTAD]]'s CSTD work, with no source giving it a distinct enough
identity of its own. The **Nordic Council and Benelux** (§4) are
likewise finally declined — no identified data-governance role, the
same call already made for World Bank in `discovery/unresolved.md`. The
**`level: local`** question (§4) closes the same way: the Dutch
municipalities are the only thing it gates, and `discovery/unresolved.md`'s
Basisregistraties section already explains why no single entity for
"the municipalities" is the right answer — [[NL-VNG]] is their
association, which is a different thing, and there is no candidate left
to research. §6's two remaining ontology-gap rows — the
infringement-procedure type/relationship and the `type: law` taxonomy
flattening — are genuine, still-open design questions, but they were
never really *candidates* (unresearched entities) in this page's sense;
both are now consolidated into rows `discovery/unresolved.md` already
carried for the same underlying issue, rather than tracked twice.

**Nothing is left on this page to pick up.** Every row that started here
either became a real entity, was found already covered, or was declined
with its reasoning kept — on the entity itself, in this page's own
history above, or in `discovery/unresolved.md` where the finding was a
genuine open question rather than a closed one. §2's `measures` type
addition and §5's domain-coverage count stay below as historical
reference, not as work to do.

---

## 1. Retired 2026-09-05 — the INSPIRE ↔ UN-GGIM edge

[[EU-EUROGEOGRAPHICS]] exists and the geospatial cluster has its middle
layer: five national mapping and cadastral authorities attach to it by
`participates-in`, mirroring [[EU-ESS]] for statistics. **The edge from the
European instrument to the UN structure was never found**, across four
separate attempts (UN batch / 2026-08-16; re-checked 2026-08-21 and twice
on 2026-09-05).

**Creating the missing node did not close this one, and that is the useful
finding.** [[EU-ESS]] closed five refused edges because the missing node was
what every one of them had been pointing at. Here the missing node was also
genuinely missing — but it was never what this refusal turned on.

The nearest thing to a bridge that ever surfaced is incidental: [[GB-OS]]
carries `participates-in` to **both** [[UN-GGIM]] and
[[EU-EUROGEOGRAPHICS]]. A path through a shared member is not a relationship
between the instruments. The fourth attempt tried an academic-source lead
(an MDPI article's claim that a UN-GGIM: Europe working group selected
geospatial themes "from the list of the INSPIRE annexes"), the current
un-ggim-europe.org homepage and working-group pages, and its 2026-2030
work plan PDF — the article 403'd, none of the live pages mentions
INSPIRE, and the PDF's text was not extractable. Retired as a candidate
here; kept as a standing open question in `discovery/unresolved.md`'s UN
batch section, where a plausible-but-unsourced relationship belongs.

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
modelled, and the third is declined. [[UN-WHO]] (plus its [[UN-WHO-GHO]]
platform) and [[UN-UNDP]] were both confirmed via `who.int` and
`sdgs.un.org` (an official UN subdomain — `undp.org` itself 403'd) read
directly. **DESA declined, 2026-09-05**: a fresh check (un.org and
sdgs.un.org, read directly) confirms it is a broad Secretariat
department — "the think tank of the UN" — already represented in the
Atlas through several of its divisions ([[UN-UNSD]], and [[UN-UNCTAD]]'s
CSTD work), with no source giving DESA itself a distinct enough identity
to warrant its own entity separate from those. The same call Batch 13
already made for the World Bank.

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
| **`level: local`** | **0 uses**, against 385 `national`, 69 `regional`, 52 `international`, 6 `sectoral` and 4 `subnational` | **No longer the blocker it was.** What blocked Flanders, the Comunidades Autónomas and the German Länder was that `regional` means *supra*-national here and nothing meant *sub*-national; `level: subnational` was added 2026-08-21 and those three became ordinary research. `local` remains unused; it gated one thing — the Dutch municipalities — and that closes as **declined, 2026-09-05**: `discovery/unresolved.md`'s Basisregistraties section already explains why no single "the municipalities" entity is the right answer (hundreds of them; [[NL-VNG]] is their association, a different thing), so there is no candidate left to research here |
| **`level: sectoral`** | 6 uses | Barely exercised. Whether that reflects the subject matter or under-use is unexamined | Later |
| **`region` entities** | **1** — only [[EU]] | **Closed 2026-09-05.** Two of the four named absentees turned out to already exist, just not as `type: region` — [[INTL-EFTA]] and [[INTL-COE]] (Council of Europe) are both modelled as `type: organisation`, the same lesson the EEA already taught: [[INTL-EEA-AGREEMENT]] (`type: law`) turned out to be the more useful shape than a region, since [[INTL-EEA-JCD-154-2018]] `amends` it and an amendment to a region would be meaningless. The **Nordic Council** and **Benelux** are declined, not carried: neither has an identified data-governance role in this Atlas's scope, and creating either would be the thin, scope-free entity the taxonomy threshold exists to prevent |

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

Two of the four rows this table used to carry are closed, 2026-09-05:

- **`implements-requirement-from` cannot say "supplements"** → the
  `supplements` type was added to `metadata/relationship-types.md`, with
  [[LI-DSG]] as its motivating (and, for now, only) example, replacing
  the overstated `implements-requirement-from` edge that entity's own
  file had flagged as the closest available but wrong type.
- **No way to record "modelled on"** → deliberately **not** given a new
  type. `LI-DSG`'s "modelled on the German BDSG" characterisation comes
  from a law-firm commentary describing legislative style, not a sourced
  statement that the legislature adapted a specific text — exactly the
  kind of single, weakly-sourced instance this page's own §2 (now closed)
  warned against building a type around. Closed as a decision to keep it
  in prose, the same treatment given to other deliberately-not-created
  entities (e.g. StUF, searched for but never given an entity for want
  of a usable source).

Both remaining rows are consolidated into `discovery/unresolved.md`
rather than tracked here too, 2026-09-05 — they are genuine ongoing
ontology questions rather than unresearched candidates:

- **No way to model enforcement against a member state.** The missing
  node ([[EU-CJEU]]) was created 2026-08-21 — confirmed via
  `curia.europa.eu`'s own page — but creating the Court did not create
  the edge: the Atlas still has no entity type for an individual
  infringement procedure and no relationship type for "was referred to
  the Court over". Tracked in `discovery/unresolved.md`'s "Research-queue
  batch" section, updated 2026-09-05 to reflect the Court's creation.
- **`type: law` flattens primary and secondary legislation** — Irish
  statutory instrument vs. Act, Spanish *Ley Orgánica* vs. ordinary law,
  German *Gesetz* vs. *Verordnung*, and [[INTL-EEA-JCD-154-2018]] (a
  Joint Committee *decision* filed as a `law`). A taxonomy change
  touching every legislation entity, genuinely out of scope for a
  candidates-page pickup. Tracked in `discovery/unresolved.md`'s Spain
  and Ireland batch sections, folded together 2026-09-05.

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
