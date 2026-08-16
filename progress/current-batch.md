# Current Batch

**Status:** No batch in progress. The **basisregistraties batch** was
completed on 2026-08-16, after the UN-connection and Spain batches the same
day.

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

**224 of 233 entities are `verification: search-only`**, and 227 of 233 are
unread in total. Page retrieval was blocked throughout the basisregistraties
batch as it was for every earlier one
(`EGRESS_BLOCKED`; 403 at the proxy tunnel, re-tested at the start of this
batch, and `WebFetch` re-tested and blocked too — the proxy reports
`connect_rejected`, an environment egress policy that cannot be changed
from inside the session).

Every entity added in these batches carries the sourcing caveat block. **No `accessed`
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

1. **Re-verification pass** (blocked on egress). 214 of 220 entities are
   unread; `discovery/reverification-allowlist.md` is the generated
   worklist. Still the single highest-value outstanding work.
2. **[[NL-CBW]] status check.** Its `start_date` is 2026-08-15. Its own body
   instructs a reader after that date to verify and, if confirmed, move it
   to `active` and [[NL-WBNI]] to `superseded`.
3. **Propose a relationship type for cooperation acts.** The UN batch found
   two real EU↔UN interactions the vocabulary cannot express — the
   UNESCO–Commission agreement and the 2023 EU voluntary review. Two
   examples is `metadata/relationship-types.md` §2.3's threshold. **This is
   the clearest live candidate for the next vocabulary change.**
4. **The eIDAS2 wallet deadline.** Roughly four months away, and **no
   country in the Atlas is linked to [[EU-EIDAS2]]** — five national
   identity systems, zero edges. A factual question now, not a modelling
   one.
5. **Finish the geospatial cluster.** [[UN-GGIM]] and [[UN-GGIM-EUROPE]]
   exist; no edge reaches [[EU-INSPIRE]]. The missing middle is probably
   **EuroGeographics**, playing [[EU-ESS]]'s role for geospatial.
6. **Connect the DPAs to the EDPB.** Five national data protection
   authorities, one sourced link. Five page reads fix four edges — still the
   cheapest high-value item.
7. **The national transpositions of
   [[EU-ENVIRONMENTAL-INFORMATION-DIRECTIVE]].** Five `applies-in` edges and
   not one transposing instrument named. ⚠ The trap is live: general
   open-government acts already in the Atlas ([[NL-WOO]],
   [[ES-LEY-37-2007]]) are **not** the environmental-information
   transpositions.
8. **[[EU-INSPIRE]] → [[NL]]**. The directive carries `applies-in` to `DE`,
   `BE`, `FR` and `ES` but **not** `NL`. Four countries have touched it
   without closing the Dutch gap.
9. **`UN-FPOS` → national statistical legislation.** The UN batch connected
   the statistical *offices*; the *legislation* ([[NL-WET-CBS]],
   [[DE-BSTATG]]) still has no UN link.
10. **Resolve [[FR-NIS2-LOI]]'s status.** The Atlas's only entity whose
    sources contradict each other about whether the instrument is in force.
11. **Resolve the federal modelling gap.** Three of five countries have an
    unrepresentable sub-national tier, in three constitutionally distinct
    forms, and the Atlas fails on all three identically.
12. **A cybersecurity domain entity**, and **a sixth country outside western
    Europe**. See `progress/backlog.md`.
