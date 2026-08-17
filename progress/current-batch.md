# Current Batch

**Status:** No batch in progress. **A switchable force-directed layout** was
added on 2026-08-17, after the grouped-layout rework.

## Site — force-directed layout, weighted by evidence

**No entity changed.** Part two of the layout question, and still **no new
dependency** — `cose` is in the vendored build and `idealEdgeLength` takes a
per-edge callback.

**A switch, not a replacement.** The force layout trades away the one thing
the grouped layout exists to show: geographic level stops being positional
and survives only as colour. Global Atlas only. **Seeded** from the grouped
positions so it is reproducible, and **not persisted**, because
`SECURITY.md` says the page stores nothing between visits.

**Two mitigations the earlier measurements demanded:** `componentSpacing`
for the 44 components and 28 isolated nodes, and degree-scaled
`nodeRepulsion` so `DOMAIN-GOVERNMENT`'s 206 edges do not pull everything
into a ball.

**What the weighting actually achieves — the claim had to be narrowed
twice.** Typed relationships are the tightest class (72 px vs 132 px for
associations); low-confidence relationships sit **~22% further apart** than
medium (203 vs 166). But ⚠ **a slack spring is not a long one** — wikilinks
were given almost no elasticity so 1,392 of them could not reshape the
graph, and the cost is they float at ambient spacing (~82 px), *shorter*
than associations. And `confidence: high` gets **no claim at all**: only 2
of 354 relationships carry it.

**The size guard is not dead this time.** `LOD_LAYOUT` was removed last
batch because both sides of its branch were identical. `FORCE_MAX = 900`
declines the simulation and says why; a test proves it by padding the graph
to 1,258 nodes.

**Verification:** `run_all.py` 5/5 · `test_build_graph.py` 37 tests ·
`test_ui.mjs` 81/81 (was 72) · graph byte-identical. A switch costs ~2.8 s
at 258 nodes, which is why the guard exists.

See `progress/completed.md` for the full entry.

## Site — layout blocks by scope, ordered by connectivity

**No entity changed.** A rewrite of `layeredPositions()`; the first half of a
two-part answer to *"can strongly connected nodes be drawn closer?"*, and the
half that needs no layout engine.

**Why not just use a force layout:** measured first. On relationships only
the graph has **44 components and 28 isolated nodes** — a physics layout
scatters them. With associations on, `DOMAIN-GOVERNMENT` has **degree 206 of
258** and running `cose` collapses the bounding box from 1686 px to 426 px.
That is a hairball.

**The strongest signal in the data is one physics would not surface:** every
typed relationship between two country-attributed entities stays **inside one
country — 131 of 131**. So the layout draws that instead: bands by level
(unchanged — the hierarchy is the Atlas's core claim), **blocks by scope**
within a band, and **connectivity order** within a block. Seven country
clumps, non-overlapping, centroids 715 px apart against a max spread of 431.

Connectivity is counted over the **visible** edges, so toggling wikilinks
re-orders the blocks.

⚠ **`LOD_LAYOUT` was dead** — `runLayout()` branched on it and both branches
were byte-identical. Removed. ⚠ The first attempt stacked every block on its
own line because the packing budget was the viewport width; the budget now
scales with the band.

**Verification:** `run_all.py` 5/5 · `test_build_graph.py` 37 tests ·
`test_ui.mjs` 72/72 (was 67) · graph byte-identical.

See `progress/completed.md` for the full entry.

## Governance — Code of Conduct and security policy

**No entity changed.** `CODE_OF_CONDUCT.md` (Contributor Covenant 2.1, with a
project-specific section) and `SECURITY.md`, linked from `README.md` and
`CONTRIBUTING.md`.

**No email address is published anywhere.** The maintainer commits under
GitHub's `noreply` address; both files route through **GitHub private
vulnerability reporting** instead, with a GitHub DM as fallback. ⚠ That link
404s until private reporting is enabled in *Settings → Advanced Security*.

Both are adapted rather than boilerplate. The CoC separates **being wrong**
(normal — 251 of 258 entities are `search-only`) from **fabricating sources**
(a violation). `SECURITY.md` states the site's posture as verified — no
cookies, no storage, no analytics, no external requests, Cytoscape vendored —
and draws two lines no template provides: a vulnerability in a system the
Atlas *describes* is out of scope, and a citation that does not support its
claim is a **public issue**, not a security report.

See `progress/completed.md` for the full entry.

## United Kingdom — seventh country, first non-EU

**258 entities, 354 relationships, seven countries.** 14 entities added.
`applies-in` targets unchanged — `['BE', 'DE', 'ES', 'FR', 'NL', 'PL']` —
and **that is the result, not an omission**.

**Principal result: the first assumption finally broke, and nothing else
did.** Six batches produced six EU member states, so the country-neutral
claim had never been tested against a country with no regional parent. The
UK has none: `region: null` on every entity, no `applies-in` edge, and **no
schema, ontology, taxonomy, relationship-type, folder, validation or
generator change** — and no `GB-EU-*` entity.

**The ID is `GB`, not `UK`.** `metadata/schema.json` requires an ISO 3166-1
alpha-2 code and `GB` is the alpha-2 assignment. The README's folder tree
had carried a speculative `uk/` placeholder since batch 0; it is corrected.

**Two European edges, neither `applies-in`:**

- [[GB-UK-GDPR]] **`derived-from`** [[EU-GDPR]] — assimilated law: the
  Regulation's own text, domesticated and now diverging. Six batches have
  each added to a list of *connections the vocabulary cannot express*;
  **this is not a seventh**. `derived-from` already meant exactly this.
- [[GB-NIS-REGULATIONS]] **`implements-requirement-from`** [[EU-NIS]] — a
  2018 transposition made **while a member state**, still in force, never
  repealed by [[EU-NIS2]]. In the Compare view it puts the UK beside the
  Netherlands on the [[EU-NIS]] row, spanning a member state and a former
  one. The UK is correspondingly **absent from the NIS2 table**.

**The statistical office joins through the UN.** [[GB-ONS]]
`participates-in` [[UN-CES]] — the first office in the Atlas to reach the
international layer without [[EU-ESS]], and possible **only because the UN
batch created [[UN-CES]]**.

**What the UK exposed:** ⚠ **`country` is a field, not an edge.** `GB` is
the Atlas's first orphan anchor — `audit.py` reports
`1 fully disconnected: ['GB']`. The other six anchors are reachable through
frontmatter only because EU instruments point `applies-in` at them.
Deliberately **not fixed here**: it is a design change across all seven
countries, not a country addition. In `progress/backlog.md`.

**Three findings about time and institutions:** the Atlas's **first
abolition** ([[GB-DSIT]], 21 Jul 2026) and with it a **fan-out succession
that `successor` cannot express**; a **third kind of unverifiable status**
([[GB-ICO]] → Information Commission, completion date unknown); and the
**amendment question for the fourth time**, now with no workaround left
because [[GB-DUAA]] amends two instruments that both remain in force.

⚠ **[[GB-DCMS]] is the weakest entity in the batch** — `confidence: low`,
all three sources trade press, no machinery-of-government order found.

See `progress/completed.md` for the full entry.

## Site — the comparison matrix

**No entity changed, and `graph.json` is byte-identical.** A fourth view:
rows are supra-national instruments, columns are countries, cells say what
each country did. Derived in the browser from `applies-in` and
`implements-requirement-from` edges that were already there.

**Why:** the Atlas's most valuable content is cross-country comparison, and
it existed **only as prose tables hand-written inside entity bodies** — the
GDPR technique table, the NIS2 state table, the 2016-act trap. All of them
had to be re-edited by hand on every new country, and several went stale.

**20 instruments × 6 countries · 21 implemented · 88 applying with no
national instrument modelled.** Only **two** instruments are implemented in
all six countries — the GDPR and NIS2 — and those are the only two the prose
tables ever covered.

**Three findings, none visible from any single entity:**

1. **The GDPR supervisory authority is modelled inconsistently.** Six
   countries attach `implements-requirement-from EU-GDPR` to a national law;
   the Netherlands attaches it to a law *and* to [[NL-AP]], the authority
   itself. No other country's authority carries it.
2. **[[EU-EIDAS]] has no `applies-in` edges at all**, though it is `active`
   and [[DE-BUNDID]] implements it. [[EU-NIS]]'s empty row is correct by
   contrast — it is `superseded`.
3. **[[EU-INSPIRE]] applies in five countries and not the Netherlands** —
   the founding country, which has a geospatial domain and a geo-portal.

**Two traps recorded in `progress/completed.md`:** rows are instruments with
`country: null`, so the country filter had to move the *columns* rather than
filter the rows; and `.filter(passesNodeFilters)` passes the array index as
the new second argument, which would have silently disabled the country
filter in the List view.

**Verification:** `run_all.py` 5/5 · `test_build_graph.py` 37 tests
(unchanged) · `test_ui.mjs` 66/66 (was 55).

## Site — domain, provenance and confidence filters

**No entity changed.** Three facets added to `tools/build_graph.py`, three
filter groups added to the site. The graph regenerated to identical content:
244 entities, 2,420 edges.

Both axes were already in the data and neither was reachable from the UI.
`metadata/taxonomy.md` §1.1 calls domains "the cross-cutting axis of the
graph", [[DOMAIN-CYBERSECURITY]] was written the same day to make *"what
connects to cybersecurity?"* answerable — and **the site could not ask it**.
Provenance and confidence were visible per-edge in the detail panel and
nowhere in aggregate, so *"show me only the interpretations"* had no answer
short of grepping the repository.

**Two things the aggregate view revealed, both about the Atlas rather than
about Europe:** only **2 of 346** typed relationships are
`confidence: high`, and **317 are `medium`** — the field is close to a
constant and should not be read as a signal. Interpretations are **13**.

**Three decisions recorded in `progress/completed.md`:** a domain filter must
keep the domain entity itself (it carries no `domains:` of its own, and is
the hub the tagged entities point at); provenance and confidence narrow
typed relationships only, or selecting `interpretation` would silently drop
every association; and confidence is ordinal, so it is ordered high → low
rather than by count.

**Verification:** `run_all.py` 5/5 · `test_build_graph.py` 37 tests (was 32)
· `test_ui.mjs` 55/55 (was 47).

## Poland — sixth country

**244 entities, 346 relationships, six countries.** `applies-in` targets
`['BE', 'DE', 'ES', 'FR', 'NL', 'PL']`. No ontology, schema, folder,
validation or generator change; no `PL-EU-*` entity. 10 entities added.

**Principal result: both untested assumptions held.** Poland acceded in
**2004**, in a different enlargement from the five western European states
before it. `progress/backlog.md` asked whether the EU layer is the right
regional parent for such a state and whether `applies-in` is the right way
to attach it. Both are.

**Second result: the new questions are about *time*, not structure** — and
neither is expressible.

- [[PL-KSC]] is **in force (3 Apr 2026) while Poland is before the CJEU**
  for the delay that preceded it. `status: active` carries none of that, and
  [[ES-LCGC]] sits at the earlier stage of the same process.
- [[PL-MOBYWATEL]] is reported **architecturally incompatible with eIDAS
  2.0** and unable to serve as an EUDI Wallet. This is the Atlas's **first
  eIDAS2 link of any kind**, after four batches recorded that none existed —
  and it is negative. No relationship type expresses a requirement an entity
  *fails* to meet, so it is `related-to` at `confidence: low` with the
  substance in the evidence string. **A sixth sourced connection the
  vocabulary cannot express.**

**Also:** the first country batch to attach to a **UN** instrument as well
as EU ones ([[UN-AARHUS]]); the 2016-act trap now has a documented answer
([[PL-OTWARTE-DANE]] repeals Poland's 2016 act, so four of six countries are
closed); and the best-sourced [[EU-ESS]] membership yet ([[PL-GUS]]), leaving
France the only modelled country with no statistical office.

See `progress/completed.md` for the full entry.

## Cybersecurity domain

**234 entities.** [[DOMAIN-CYBERSECURITY]] connects **23 entities across
three layers and five countries** — a threshold `metadata/taxonomy.md` §1
had passed several batches ago. One entity added, 23 tagged, one taxonomy
row.

**What a domain view is for.** Three things became legible that no single
entity shows: **one directive with five different national states** (two of
which are unclear in *different* ways — `unknown` versus `proposed`); **the
national authority is not one institution** (Spain has two split by
audience, and the **Netherlands has none in the Atlas at all** — the NCSC is
unmodelled); and **two three-layer chains that do not meet**, since nothing
connects the ISO/EU standards layer to the national baselines.

The Dutch gap is the point: invisible looking at Dutch entities one at a
time, obvious the moment the domain is assembled.

**Boundary calls, both judgements rather than facts.** [[EU-CER]] is
**excluded** — it governs physical resilience, not network and information
security — even though [[FR-NIS2-LOI]] is a single French instrument
transposing NIS2, CER and DORA together, so the domain boundary cuts through
one national law. Data protection is excluded for the same kind of reason.

See `progress/completed.md` for the full entry.

## Basisregistraties — the ten registers modelled

**233 entities, 320 relationships.** All ten Dutch base registries are now
entities, with a description, a holder and a place in the stelsel. 13
entities added: the ten registers plus [[NL-RVIG]],
[[NL-WAARDERINGSKAMER]] and [[NL-BELASTINGDIENST]].

[[NL-BASISREGISTRATIES]] had been asking for this since Batch 2 — *"once the
individual registrations become entities, this link should move down to the
BRP entity"*. It has: `governed-by` [[NL-WET-BRP]] now sits on [[NL-BRP]].

**Principal finding — about the vocabulary, not the Netherlands.** Five
sourced connections could not be recorded, in three shapes: **authorised
use** (the Belastingdienst consumes the WOZ; the RDW receives BRP data),
**key-sharing couplings** (BRK products carry the KvK number; the BAG
couples to the BRP), and **`authentiek gegeven`**, the legal status that
makes a base registry authoritative and has no field.

**The Atlas models what entities *are* and what they *descend from*, and has
almost no vocabulary for how data moves between them.** For a system whose
entire purpose is data movement, that is the honest result. With the UN
batch's two, five sourced connections are now unmodelled for want of a type.

**Roles, not owners.** The stelsel describes four roles and says one
organisation can be several at once; the Atlas has one `maintained-by` per
register. Where they diverge the caveat is written into the relationship's
own `evidence` string, so it is visible in the graph data. For the BAG, BGT
and WOZ the party that actually creates the data — municipalities, seven
kinds of bronhouder — is **absent from the graph**. Unlike the federal
`level` gap this is not an ontology limit: `local` exists. There is simply
no obvious entity to create.

See `progress/completed.md` for the full entry.

## UN-connection batch — the island is connected

**220 entities, 300 relationships.** `UN → anything` was **0** through five
country batches; it is now **`EU → UN` = 4** and **`UN → national` = 5**.
14 entities added, 7 rewired, **no relationship type added and no sourcing
standard lowered**.

**Principal finding: the refusals were right, the target was missing.**
`UN-UNSD` → [[EU-EUROSTAT]] had been refused three times, correctly — UNSD
is a secretariat and Eurostat does not relate to it directly. Eurostat's own
page says it represents the EU **in forums**, and the Atlas had no node for
any of them. Once [[UN-UNSC]], [[UN-CES]] and [[EU-ESS]] existed, six
previously-refused edges became statable on evidence that was already
available.

**The chain that matters:** [[UN-AARHUS]] (UNECE convention, 1998) →
[[EU-ENVIRONMENTAL-INFORMATION-DIRECTIVE]] (2003/4/EC) → `applies-in` to all
five countries. The Atlas's **first complete UN → EU → national chain**, and
its first `applies-in` from a UN instrument. `implements-requirement-from`
covered the UN→EU step unchanged — its Batch 3 definition says *"an EU (or
other higher-level) legal instrument"*, and the parenthesis turned out to
have anticipated this exact case.

**Three of four clusters closed.** Geospatial was left incomplete on
purpose: [[UN-GGIM]] and [[UN-GGIM-EUROPE]] exist, and no edge reaches
[[EU-INSPIRE]], because a EuroGeographics presentation *about* UN-GGIM given
to an INSPIRE audience shows two communities talking, not two instruments
relating.

**Two failures worth keeping:** the UNESCO–Commission agreement and the 2023
EU voluntary review are real EU↔UN interactions that **no relationship type
can express**. Two examples is §2.3's threshold for proposing a new type;
deliberately not proposed by a batch that could not read sources.

**A record corrected:** the claim that *"no national statistical office
connects upward"* had been repeated for three batches and was wrong —
[[NL-CBS]] already had an edge. Cluster narratives in `discovery/` are
prose, and prose is not validated.

See `progress/completed.md` for the full entry.

## Spain — fifth country

**206 entities, 269 relationships, five countries.** `applies-in` targets
`['BE', 'DE', 'ES', 'FR', 'NL']`. No ontology, schema, folder, validation or
generator change; no `ES-EU-*` entity.

**Principal result: the model is not western-European-shaped.** Spain is the
first country outside the founding-six / Benelux-DACH group — southern
European, a later enlargement, a constitutional form none of the others use
— and it fitted unchanged. The standing objection that four neighbouring
states cannot demonstrate country-neutrality is answered.

**Second result: the federal `level` gap has a third shape.** Comunidades
Autónomas are neither Länder nor Regions, and the Atlas fails on all three
identically — which localises the defect in the vocabulary rather than in
any country's constitution. Three of five countries are affected. In Spain
it hides seventeen regional open data portals and half of a named axis of
the national digital strategy.

**Four things closed:** the first national link to [[EU-AI-ACT]]
([[ES-AESIA]], the EU's first AI supervisory agency, created *before* the
Regulation applied); the Open Data Directive transposition on the third
attempt ([[ES-LEY-37-2007]]); a fourth branch of the DCAT chain
([[ES-NTI-RISP]], the only legally mandatory one); and the first edge in the
statistics cluster ([[ES-INE]] → [[EU-EUROSTAT]], recorded honestly as an
interpretation).

**Also:** the Atlas's first *organisational* succession ([[ES-AEAD]]
supersedes [[ES-SGAD]]), and five countries now showing **five different
NIS2 states** — including `proposed` and `unknown` side by side.

See `progress/completed.md` for the full entry.

## France — fourth country

**189 entities, 242 relationships, four countries.** `applies-in` targets
`['BE', 'DE', 'FR', 'NL']`. No ontology, schema, folder, validation or
generator change; no `FR-EU-*` entity.

**The result is a negative, and that is what makes it useful.** France is
unitary and was added to test whether anything besides the federal `level`
gap was Netherlands-shaped. It raised **no new ontology question at all** —
the first country of which that is true. Combined with Germany and Belgium
this isolates the defect: the ontology is sound for unitary states and
lossy for federal ones, and the loss is confined to `level`.

Also found: a **third GDPR implementation technique** (France amended a
1978 act in place); a **fourth national DPA with still only one EDPB link**;
and the Atlas's **only entity whose sources contradict each other about
whether it is in force** ([[FR-NIS2-LOI]], recorded `status: unknown`).

See `progress/completed.md` for the full entry.

## Belgium — third country

Completed 2026-08-15, after Batch 16 (Interactive Knowledge Graph) and the
Germany second-country batch the same day.

**178 entities, 218 relationships, three countries** at the time.
`applies-in` targeted `['BE', 'DE', 'NL']`. Adding a third country again required no
ontology, schema, folder, validation or generator change, and produced no
`BE-EU-*` entity.

The published graph regenerates automatically on merge, so the Atlas at
https://dalust.github.io/Data-Initiatives-Atlas/ picks Belgium up without
any manual step.

**Principal finding: the federal modelling gap is general.** Germany showed
the `level` vocabulary has no term for a Land. Belgium shows the term that
would fit is already taken — `regional` means supra-national in this Atlas.
**OSLO**, a major Flemish semantic-interoperability programme, is therefore
unmodelled. After three countries this is the Atlas's best-evidenced
ontology defect, and no sub-national level has been invented to paper over
it.

**One link closed:** [[BE-BELGIF]] `based-on` [[EU-EIF]] — the first
EIF → national-framework descent, which Germany had to refuse.

See `progress/completed.md` for the full entry.

## Batch 16 — the Atlas is published as an interactive graph

The repository is rendered as an interactive knowledge graph at
**https://dalust.github.io/Data-Initiatives-Atlas/**, generated by
`tools/build_graph.py` and deployed by `.github/workflows/pages.yml`.

164 nodes and 1,307 edges (189 typed relationships, 473 associations, 645
wikilinks), all derived — nothing about the graph is hand-maintained, and no
entity file changed, so the repository still works as an Obsidian vault.

**The site is live and the deployment is verified.** GitHub Pages was
pointed at Actions (*Settings → Pages → Build and deployment → Source →
GitHub Actions*) and `pages.yml` run 31893120291 completed successfully on
2026-08-15: `configure-pages`, `upload-pages-artifact` and `deploy-pages`
all green.

The first attempt of that run failed at `configure-pages` — *"Get Pages
site failed… verify that the repository has Pages enabled"* — because the
setting had not yet been made. Every step before it passed, so the fix was
simply to re-run once the setting was in place. This is the one part of the
pipeline no workflow can perform for itself; it is documented in
`docs/github-pages.md` under one-time repository setup.

**The Atlas is structurally complete and evidentially unverified**, and it
now covers **five countries** (this section describes the state at the
time of Batch 16; see the Spain entry above for the current figures). See
`validation/germany-second-country-report.md` for the second-country result
and `validation/final-quality-gate.md` for the standing verdict.

## What was done on 2026-08-15 — Germany as a second country

Germany was added as the second national scope, which was the outstanding
item from the Final Quality Gate: *"a second country — the only real test
of the country-neutral model."*

**The model holds.** 125 → **164 entities**, 131 → **189 provenanced
relationships**, validation **5/5, 0 errors, 0 warnings**. 33 `applies-in`
relationships now target **both `NL` and `DE`**.

Adding a country required no change to `metadata/schema.json`,
`metadata/ontology.md`, `metadata/taxonomy.md`,
`metadata/relationship-types.md`, the folder structure or any validation
rule. **No `DE-EU-*` entity was created.**

39 entities added: 37 German (`countries/de/`, plus entries in the existing
flat type folders) and 2 supra-national reached through German research
([[EU-INSPIRE]], [[EU-GAIA-X]] — both `country: null`).

### Principal finding

**The model is lossy for federal states.** The `level` vocabulary has no
term between `national` and `local`, so Germany's sixteen Länder are not
representable — including the sixteen Land acts that jointly transpose
[[EU-INSPIRE]] with [[DE-GEOZG]], the sixteen Land data protection
authorities alongside [[DE-BFDI]], and [[DE-KOSIT]]'s hosting in the Bremen
administration. The Atlas cites Land governments as sources while unable to
model them.

No sub-national level was invented — doing so for one country would be the
country-specific ontology change the model exists to prevent. Logged in
`discovery/unresolved.md`; it will matter for any federal state added
later.

## The sourcing position is unchanged

**234 of 244 entities are `verification: search-only`**, and 237 of 244 are
unread in total (the seven domain entities are taxonomy nodes carrying no
factual claims, so they are `primary-source`). Page retrieval was blocked throughout the basisregistraties
batch as it was for every earlier one
(`EGRESS_BLOCKED`; 403 at the proxy tunnel, re-tested at the start of this
batch, and `WebFetch` re-tested and blocked too — the proxy reports
`connect_rejected`, an environment egress policy that cannot be changed
from inside the session).

Every Polish entity carries the sourcing caveat block. **No `accessed`
dates were written and `last_verified` is null throughout**, because
nothing was accessed or verified. The hosts that would need to be reachable
are enumerated in `discovery/reverification-allowlist.md`, which is
generated from the entities themselves by `tools/source_hosts.py`.

One improvement worth noting: the [[DE]] anchor is
`verification: search-only`, not `unverified`. [[NL]], [[EU]] and [[UN]]
are `unverified` because Batch 0 composed their URLs from background
knowledge. The [[DE]] anchor's single cited URL was returned by a search
index. The second country was written to the corrected standard from the
start rather than retro-fitted into it.

**The re-verification pass remains the single highest-value outstanding
piece of work**, and it is blocked on outbound HTTPS, not on effort. Every
URL is already recorded in the entities' `sources:` lists.

## Immediate next steps, in priority order

1. **Propose the missing relationship types.** **Six** sourced connections
   across three batches cannot be recorded, in four shapes: **authorised
   use** ([[NL-BELASTINGDIENST]] → [[NL-WOZ]], [[NL-RDW]] → [[NL-BRP]]),
   **key-sharing couplings** ([[NL-BRK]] ↔ [[NL-NHR]]), **cooperation acts**
   (the UNESCO–Commission agreement, the 2023 EU voluntary review), and now
   an **unmet obligation** ([[PL-MOBYWATEL]] ↛ [[EU-EIDAS2]]). §2.3's
   threshold is two. **This needs no page access at all** — the evidence is
   already in the repository.
2. **Re-verification pass** (blocked on egress). 237 of 244 entities are
   unread; `discovery/reverification-allowlist.md` is the generated worklist.
3. **The eIDAS2 deadline.** Now weeks away. Poland is the only country with
   an edge to [[EU-EIDAS2]], and it says the national system **cannot
   comply**. The other five have no edge — not because they comply, but
   because nothing has been read either way.
4. **[[NL-CBW]] status check.** Its `start_date` is 2026-08-15; its own body
   instructs a reader after that date to verify and, if confirmed, move
   [[NL-WBNI]] to `superseded`.
5. **Connect the DPAs to the EDPB.** **Six** national authorities, one
   sourced link. Six page reads fix five edges — still the cheapest
   high-value item, now survived four country batches.
6. **Model infringement status.** [[PL-KSC]] is in force with Poland before
   the CJEU; [[ES-LCGC]] is a draft with a reasoned opinion received. Two
   stages of one process, neither in the structured data.
7. **The cyber authorities of the Netherlands and Poland.** Two of six
   countries have cybersecurity legislation modelled and no authority — see
   [[DOMAIN-CYBERSECURITY]].
8. **Finish the geospatial cluster.** [[UN-GGIM]] and [[UN-GGIM-EUROPE]]
   exist; no edge reaches [[EU-INSPIRE]]. The missing middle is probably
   **EuroGeographics**.
9. **INSEE.** France is the only one of six countries with no statistical
   office in [[EU-ESS]].
10. **[[EU-INSPIRE]] → [[NL]]**, still the one country the directive does
    not reach; **[[FR-NIS2-LOI]]'s status**; and the **Belgian and French
    Open Data Directive transpositions**, whose shape is now known from
    Poland and Spain.
11. **Resolve the federal modelling gap.** Three of six countries have an
    unrepresentable sub-national tier in three constitutionally distinct
    forms.
12. **A seventh country outside the EU.** All six are EU member states, so
    `applies-in` has never been tested against a country the EU cannot bind.
    See `progress/backlog.md`.
