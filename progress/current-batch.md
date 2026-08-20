# Current Batch

**Status:** No batch in progress. **Explorer depth** was completed on
2026-08-20.

## Explorer depth — 4 hops, and the counts to go with it

Two changes to the Entity Explorer's neighbourhood control, both driven by
measuring the graph rather than guessing at it. No entity content changed.

### Why 4, and not 6

The question was whether to raise the ceiling from 3 to 6. Measured across
all 450 entities, median entities reached from a seed:

| hops | relationships only (default) | all edges (wikilinks on) |
|---|---|---|
| 1 | 3 (1%) | 11 (2%) |
| 2 | 14 (3%) | 295 (**66%**) |
| 3 | 34 (8%) | 424 (**94%**) |
| 4 | 108 (24%) | 450 (**100%**) |
| 5 | 214 (47%) | 450 |
| 6 | **296 (66%)** | 450 |

Two conclusions fall straight out. **With wikilinks on the control is already
maxed at 3** — four hops reaches the entire graph from the median seed, so
options 4, 5 and 6 would be three ways to spell "everything". And **on the
default edge set 6 hops shows two-thirds of the Atlas**, which is not a
neighbourhood.

**4 is where the real chains finish.** Every signature descent in the Atlas
completes inside it:

| | hops |
|---|---|
| [[EU-GDPR]] → [[NL-AP]] | 1 |
| [[INTL-DCAT]] → [[NL-DCAT-AP-NL]] | 2 |
| [[INTL-W3C]] → [[NL-DCAT-AP-NL]] | 3 |
| [[UN-AARHUS]] → [[NL-AP]] | 3 |
| [[UY]] → [[NL]] | 3 |
| [[INTL-CONVENTION-108-PLUS]] → [[FR-CNIL]] | **4** |

So 4 buys the full treaty → protocol → regulation → authority descent at a
median of 108 entities, still a readable subset. Five and six buy scale and
nothing else.

### The counts matter more than the extra hop

Each option now states what it would show, recomputed against the current
focus **and the current filters**:

```
1 hop — direct links — 3 entities        [1% of the Atlas]
2 hops — 36 entities                     [8% of the Atlas]
3 hops — 105 entities                    [23% of the Atlas]
4 hops — the longest chains — 188 entities  [42% of the Atlas]
```

This graph is **hub-heavy**: almost every entity touches its country anchor,
[[EU]], [[UN]] or a domain node, so one extra hop through a hub can multiply
the result several times over. Depth is not a dial a reader can predict, and
the useful moment for a number is *before* the click, not in the status line
afterwards. A depth that would show more than half the Atlas says so beneath
the control.

### The lever is still the wrong one

Both changes work around the real problem rather than fixing it. The reason
two hops explodes to 66% with wikilinks on is that a path `A → EU → B` exists
between almost any pair — and that path means "both are European", not that
A and B are related.

**Not traversing *through* anchors and domain nodes** would make depth
meaningful instead of explosive, and would make wikilinks-on mode usable at
depth, which it currently is not. That is a genuine design change and is
queued rather than taken unilaterally.

### Verification

- `tools/test_ui.mjs` — 81 → **86 checks**, five of them new: the ceiling is
  4; every option carries a count; the counts are cumulative; **choosing a
  depth renders exactly the count its label promised**; and the counts move
  when filters do.
- `validation/run_all.py` 5/5 · `tools/test_build_graph.py` 41 OK ·
  `tools/test_reverify.py` 35 OK

The traversal was extracted into a shared `neighbourhood()` helper so the
control and the renderer cannot disagree about what a hop is.

## The re-verification runner — previous batch

`tools/reverify.py` — the missing half of a pass the repository has described
since Batch 1 and never had a way to run. **443 of 450 entities** have never
had a cited source read.

No entity content changed in this batch. 450 entities, 5,090 edges, unchanged.

### What it does

- fetches each `sources[].url`, honouring `HTTPS_PROXY` and the system CA
  bundle;
- extracts the entity's **checkable claims** and looks for each on the
  retrieved page;
- reports a verdict — `BLOCKED`, `UNREACHABLE`, `NEEDS REVIEW`,
  `CORROBORATED`, `NO SOURCES`;
- on `--write`, stamps `accessed:` on the sources that actually came back,
  sets `last_verified:`, and flips `verification:` to `primary-source`.

### The check exists because of one specific near-miss

A search returned **BWBR0007376** for the Kadasterwet. That identifier is the
**Archiefwet 1995**.

A wrong identifier in this field **does not 404** — it silently returns
another real act. Fetching the page succeeds and looks entirely convincing.
The only thing that catches it is checking the page for the identifier the
entity *claims*, which is what the tool does and what a human skim-reading a
plausible page would not.

That case is a test: `test_the_near_miss_this_tool_exists_for`.

### What it deliberately does not do

**Corroboration is not verification.** A `CORROBORATED` verdict means the
identifiers are on the pages. It says nothing about whether the entity's
dates, description, relationships or evidence strings are right — the part
that matters, and the part only a reader can do.

So: `--write` takes exactly one `--id`, refuses on `BLOCKED` and
`UNREACHABLE`, refuses when a claim went uncorroborated unless `--force`, and
never touches `confidence`. Raising confidence stays a hand judgment, gated by
the existing rule that `confidence: high` cannot sit on a `search-only`
entity.

### TLS is not negotiable

The tool has no switch to relax certificate verification, and
`test_source_has_no_verification_escape_hatch` asserts that against the
module's **syntax tree** — not its text.

That distinction was not academic. The first version of the test did a
substring search and failed on the module's own prose about never disabling
verification. A text search would also have passed happily on
`# verify=False` in a comment while missing `ctx.verify_mode = x` where
`x = ssl.CERT_NONE`. The AST version checks what the code does.

A `primary-source` claim made over an unverified connection is worth less than
the `search-only` claim it replaced.

### Run against the priority seven

The seven Dutch register statutes, flagged high-priority in
`discovery/unresolved.md` precisely because of the BWBR problem:

```
BLOCKED: 7
```

Every source, every statute. That is the correct output for this environment:
`curl "$HTTPS_PROXY/__agentproxy/status"` reports `403 to CONNECT` for every
host. The tool degrades to a truthful report rather than a crash or a false
pass, and it exits `1` so a sweep cannot be mistaken for success.

`discovery/reverification-allowlist.md` was regenerated and is the list of
hosts to request: **1,500 URLs across 486 hosts, 353 registrable domains**.
`europa.eu` alone unblocks 80 entities.



### Running it found three more bugs

The first full sweep is what tested this tool, not the unit suite. In order:

1. **`http.client.InvalidURL` crashed the run six minutes in.** A source URL
   on [[GB-OS]] contained a literal space. On Python 3.11 `InvalidURL`
   inherits from `HTTPException` and **not** from `ValueError`, so a tidy
   tuple of expected exception types missed it. One unfetchable source must
   never take down a sweep of four hundred entities, so the guard is now
   deliberately broad — and it names a malformed URL as the repository's
   fault rather than the network's.
2. **`Request()` construction sat outside the guard**, so a nonsense URL
   crashed before any handling could apply. Found by the test written for
   bug 1.
3. **Nine egress denials were misreported as origin failures.** A plain
   `http://` URL reaches the proxy as an ordinary forward request, so its
   refusal comes back as an HTTP **403 response** rather than a failed
   CONNECT. That is precisely the distinction this tool exists to keep
   straight. The proxy labels its own refusals with `x-deny-reason`, so that
   header is now the signal, and the response body is surfaced either way so
   a reader can check the classification rather than trust it.

The malformed URL also exposed a gap in `validation/validate_sources.py`,
which checked only that a URL starts with `http`. A URL containing raw
whitespace **cannot be fetched at all** — it is silently un-re-verifiable,
which is exactly the debt this repository is trying to pay down. It is now an
error, and the rule was confirmed to fire by reintroducing the bad URL.

31 → **35 tests**.

### The first full sweep

```
python tools/reverify.py --search-only --timeout 8
```

| | |
|---|---|
| Entities swept | **443** |
| Sources attempted | **1,500** |
| Retrieved | **0** |
| Refused by egress policy | **1,494** (99.6%) |
| Other | **6** |

Six minutes; not one page read. The six are three different things, and only
one is fixable by an allowlist:

- **5 × `github.com`**, refused by the **GitHub** proxy, which scopes a
  session to its configured repositories. Adding a host will not lift it.
- **1 × `catedrapsyd.unizar.es`** on [[ES-LO-2-2002]], which **did not
  resolve at all** while every other host tested resolved to the
  interceptor — pointing at a genuinely dead host. Recorded in
  `discovery/unresolved.md` as a citation to replace.
- **1 entity with no sources**, [[DOMAIN-NATIONAL-SECURITY]], correctly:
  domains carry no factual claims.

Six entities have **no checkable claims** — [[RO]], [[UA]], [[FR-ETALAB]],
[[NL-LOGIUS]], [[NL-NICTIZ]], [[NO-ALTINN]]. Short names, no legal
identifier. The tool reports that rather than passing them silently.

### ⚠ CI caught what local testing could not

The first push failed on GitHub Actions with `PermissionError: [Errno 13]
Permission denied: '/root/.ccr/ca-bundle.crt'`.

`Path.exists()` **raises** rather than returning `False` when a parent
directory is unreadable. The agent proxy's CA bundle lives under `/root/`,
which is readable in the container this repository is normally worked in and
**not** readable by the `runner` user in CI. Every local run passed; the
failure needed a machine that simply does not have the file.

Extra trust anchors are an optimisation for one environment, and the fix is
that they can no longer break the tool in another: `_readable()` returns
`False` on any `OSError` instead of propagating it.

Two regression tests were added, and the guard was confirmed load-bearing by
re-creating the old unguarded implementation and watching it reproduce the CI
failure under the same mocks that the new one survives. 29 → **31 tests**.

### Verification

- `tools/test_reverify.py` — **35 tests**, no network, added to both CI
  workflows
- `validation/run_all.py` — 5/5
- `tools/test_build_graph.py` — 41 OK
- `tools/test_ui.mjs` — 81/81
- The write path was exercised on a copy of a real entity: frontmatter
  stamped, sources and relationships preserved, **body byte-identical**, and
  the result re-parses.

`docs/re-verification.md` is the procedure, linked from the README.

## Convention 108 and 108+ — previous batch

The first item on the research queue after the European country batch, and
the one that came with a correction to how the Atlas presented European data
protection.

**11 new entities, 22 relationships.** 439 → **450 entities**, 728 → **750
relationships**. One new `status` value. 50 → **58 country scopes**.

| Entity | Instrument | Status |
|---|---|---|
| [[INTL-CONVENTION-108]] | ETS 108, opened 28 Jan 1981 | in force since 1 Oct 1985 |
| [[INTL-CONVENTION-108-PROTOCOL]] | ETS 181, opened 8 Nov 2001 | in force |
| [[INTL-CONVENTION-108-PLUS]] | CETS 223, opened 10 Oct 2018 | **`adopted` — not in force** |

Plus eight country anchors: [[AR]], [[CV]], [[MU]], [[MX]], [[MA]], [[SN]],
[[TN]] and [[UY]].

### What this corrects

The Atlas presented [[EU-GDPR]] as the origin of European data protection.
It is not. Convention 108 opened for signature on **28 January 1981** —
thirty-five years before the GDPR became applicable, and thirteen years
before the Directive the GDPR replaced. Fair and lawful processing, purpose
limitation, data minimisation, accuracy, storage limitation, security,
special protection for sensitive data, access and rectification: all of it is
in the 1981 text. **28 January is Data Protection Day** for that reason.

The GDPR now points back at it: **Recital 105** makes a third country's
accession to Convention 108 a factor in EU adequacy assessment. That edge is
asserted.

### The first entities outside Europe

Convention 108 is **the only instrument in the Atlas that is not regional**.
Every other binding instrument here is an EU act binding 27 states or a
national act binding one. This one is open to accession by any state, and
eight non-European states have acceded — five African, three Latin American.

They were created as base anchors because modelling the treaty without them
would have modelled it as the regional instrument it is expressly not. They
are **not the start of a global country layer**, and `countries/README.md`
and each anchor say so.

[[MU]] Mauritius has ratified **both** Convention 108 and the amending
protocol, putting it ahead of most European parties on the modernised
instrument.

### ⚠ Adopted, ratified by 34 states, binding nobody

[[INTL-CONVENTION-108-PLUS]] needs **38** ratifications. [[MD]] Moldova
became the **34th on 15 May 2026**. After nearly eight years it is four
short, and the Council of Europe has published a specific appeal to EU
member states to ratify.

That is a different kind of failure from the transposition delays the Atlas
already records. Belgium was twenty-nine months late on
[[EU-OPEN-DATA-DIRECTIVE]] and the Netherlands three years — but those
instruments were in force and being breached. This one has never come into
force at all.

### A `status` value had to be added

No existing value could say it.

- `proposed` would have called a treaty **34 sovereign states have ratified**
  a proposal.
- `active` would have called a treaty **not in force** operative law.

**`adopted`** was added to `metadata/schema.json`,
`metadata/controlled-vocabularies.md` and `metadata/metadata-schema.md`:
formally adopted, not yet in force. It is the third vocabulary addition in
three batches, after `proposes-to-supersede` and `amends`, and it meets the
same test — an existing value would have had to assert something untrue.

[[INTL-CONVENTION-108-PLUS]] also carries the **second use of `amends`**, and
the first outside a national transposition.

### ⚠ The verification debt blocked new modelling for the first time

Sources state that **all Council of Europe member states are parties** to
Convention 108 — roughly 46 more `applies-in` edges.

They were **not asserted**. The one source found for the rule gives a stale
member count (47, wrong since [[RU]]'s expulsion in 2022), and [[RU]]'s own
status as a party after expulsion is unaddressed by anything found. The
Council of Europe's chart of signatures and ratifications settles it, and
**`coe.int` is blocked by the egress proxy** — confirmed by probe, not
assumed.

Every previous batch's sourcing problem was *re-verification*: the facts were
recorded and unread. This is the first time the block has prevented the Atlas
from **recording a fact at all**. It is queued as `Blocked (egress)`.

### Verification

- **450 entities, 5,090 edges** (750 relationship, 1,653 association, 2,687
  wikilink), **58 country scopes**
- `validation/run_all.py` — 5/5
- `tools/test_build_graph.py` — 41 OK
- `tools/test_ui.mjs` — **81/81**
- `validation/audit.py` — no fully disconnected entities

All 11 new entities are `verification: search-only`; `coe.int`, `rm.coe.int`
and `eur-lex.europa.eu` are all blocked.

## The European country anchors — previous batch

Thirty-seven base country anchors, taking the Atlas from **13 country
scopes to 50**. **39 new entities, 65 relationships.** 400 → **439
entities**, 676 → **728 relationships**.

These are deliberately *base* entities: each carries its country's position
in the European legal and institutional frameworks, and nothing else. No
data protection authority, no portal, no statistics office, no legislation.
The purpose is that the next contributor to reach for Estonia or Italy finds
somewhere to attach rather than having to create the scope first.

### The scope rule is stated, not implied

There is no authoritative list of "European countries", so the batch wrote
its rule down in `countries/README.md` rather than drawing a line and hoping
nobody asked. A state gets an anchor if it satisfies **any** of: EU
membership; EFTA or EEA membership; Council of Europe membership; or a live
EU accession relationship. [[BY]] and [[VA]] are added on top, satisfying
none of the four.

The rule is a **union, not a geography**, and it admits four states the UN
M49 geoscheme places in Western Asia — [[AM]], [[AZ]], [[GE]] and [[TR]] —
on their Council of Europe membership. Each says so on its own page.

### Two new international organisations

Both were created because the country layer needed them, and both close gaps
the Atlas had already recorded:

- **[[INTL-COE]]** — the Council of Europe. EU member states can anchor on
  [[EU]]; the twenty European states that are not EU members had nowhere to
  anchor at all. It is also the home of **Convention 108 and 108+**, the only
  binding international treaty on data protection and the highest-value item
  this batch surfaced.
- **[[INTL-EFTA]]** — listed under "not modelled" on [[NO]] since the Norway
  batch. The gap became three countries wide when [[IS]] and [[LI]] arrived.

### A membership that ended, and one that never was

[[RU]] carries `part-of` [[INTL-COE]] with **`valid_from: 1996-02-28` and
`valid_until: 2022-03-16`** — the Atlas's first closed validity interval on a
membership edge. Russia's expulsion on 16 March 2022 was the first in the
organisation's history.

[[BY]] carries `related-to` [[INTL-COE]] instead. Belarus has never been a
member; its special guest status was suspended in 1997. A membership that
ended and a membership that never existed are different facts, and the two
edge types record the difference.

### ⚠ One anchor is not an ISO code

[[XK]] — Kosovo — has **no ISO 3166-1 alpha-2 code**. `XK` is a user-assigned
code, which is what the European Commission, the IMF and the World Bank use.

`metadata/ontology.md` §3.1 said the national scope segment *is* the ISO
code. Rather than quietly break that rule, §3.1 now names the exception. The
entity records what the sources describe and states explicitly that creating
an entity is not a position on recognition.

### The existing thirteen were normalised too

Before this batch, every country anchor had `relationships: []` and reached
the graph only through the national entities pointing at it. That works for a
country with a modelled layer and fails for one just created.

All fifty anchors now carry the same membership edge — `part-of` [[EU]] for
the 27 member states, `part-of` [[INTL-COE]] for the rest — and `region: EU`
is now set consistently on member states rather than on four of them.

### A layout test that was asserting the wrong thing

`tools/test_ui.mjs` failed at 80/81 once 50 country blocks existed:
*"country blocks are further apart than they are wide — min separation 295
vs max spread 464."*

The check compared the **single smallest** centroid gap anywhere in the band
against the **single largest** block radius anywhere in the band. That proxy
held while every country block was roughly the same size. With [[NL]] at 85
entities and [[AD]] at one, it demanded that two *one-entity* blocks sit 464
apart — not a legibility requirement, just wasted canvas.

The assertion was rewritten to the question it was always trying to ask:
**for each pair, is the separation greater than those two blocks' own
radii?** Bounding-box non-overlap is still checked separately, so small
blocks are still guaranteed not to collide.

It is not vacuous — the tightest pair is now **BE/NO at 585 against a
combined radius of 463**. The layout constants were not touched; the test
was wrong, not the layout.

### The five highest-value gaps this created

1. **[[EE]]** — X-Road and e-Residency, the most cited digital-government
   components in Europe, and the Atlas holds nothing about either.
2. **Convention 108 / 108+** — see above.
3. **[[BG]] and [[LV]]'s Open Data Directive transpositions** — two of the
   four member states referred to the Court of Justice in February 2023. The
   other two are modelled.
4. **`applies-in` to the 17 new member states** — every EU instrument the
   Atlas holds applies in all 27; it names 10.
5. **The EFTA Surveillance Authority, EFTA Court and EEA Joint Committee** —
   [[IS]], [[LI]] and [[NO]] are supervised by nobody in the graph.

### Verification

- **439 entities, 4,985 edges** (728 relationship, 1,627 association, 2,630
  wikilink), **50 countries**
- `validation/run_all.py` — 5/5
- `tools/test_build_graph.py` — 41 OK
- `tools/test_ui.mjs` — **81/81**
- `validation/audit.py` — no fully disconnected entities

All 39 new entities are `verification: search-only`. Accession **years** in
the framework tables come from general reference knowledge rather than from
the cited pages, and every anchor says so in a note under its own table.

## The Open Data Directive transpositions — previous batch

The largest remaining item on `discovery/research-queue.md`, carried since
the Belgium, France and Spain batches:

> *"**The Open Data Directive transpositions for Belgium, France and
> Spain.** All three amended existing law rather than passing a standalone
> act, and none of the three instruments was identified."*

**4 new entities, 10 relationships.** 396 → **400 entities**, 666 → **676
relationships**. One new relationship type.

The prediction was right for two of the three, and wrong in a way worth
having.

| Country | Instrument | Pattern |
|---|---|---|
| Belgium | [[BE-HERGEBRUIK-WET-2023]] — federal act of 25 Dec 2023 | `amends` [[BE-HERGEBRUIK-WET]] |
| Spain | [[ES-RDL-24-2021]] — decree-law of 2 Nov 2021, Book Three | `amends` [[ES-LEY-37-2007]] |
| France | **none** — [[FR-LOI-VALTER]] explains why | no ODD-era instrument exists |

### Belgium had not transposed yet when the Belgium batch ran

The Belgium batch could not have found this instrument. Belgium's federal
transposition was adopted on **21 December 2023** and published on **25
December 2023** — after the sources that batch searched were written.

The gap the queue recorded as a research failure was a **timing** fact.

Its lateness is the extreme of the Atlas's range. Against
[[IE-PSI-REGULATIONS-2021]] at five days late, Belgium is **twenty-nine
months** late, and was referred to the Court of Justice ten months before
the act passed.

### Belgium's regions beat its federal state

Belgium transposed four times, because the competence is shared:

| Level | Instrument | Date |
|---|---|---|
| Flanders | Decreet amending the Bestuursdecreet | 2 July 2021 — **inside the deadline** |
| Brussels-Capital | Ordonnance amending that of 27 Oct 2016 | 10 December 2021 |
| Wallonia | Two décrets on dissemination and re-use | 24 November 2022 |
| Federal | [[BE-HERGEBRUIK-WET-2023]] | 25 December 2023 |

Flanders met the deadline with a fortnight to spare. Belgium was referred to
the Court anyway, because a member state answers for its whole territory.

Only the federal act is modelled. `level: regional` in this Atlas means
*supra*-national — every EU instrument carries it — so there is no value for
a Belgian Region. That is the same blocker recorded against OSLO and
Digitaal Vlaanderen, and this batch did not resolve it; it recorded the
three instruments in prose and queued the design question.

### France's 2021 ordinance does not exist

The France batch recorded the transposition as *"understood to be a 2021
ordinance; not identified."*

There is no such ordinance. **Ordonnance n° 2021-1518 du 24 novembre 2021**
is real, is French, is from 2021, and "complète la transposition" of a 2019
directive — but that directive is **2019/790**, on copyright in the digital
single market, not **2019/1024**.

France's regime predates the Directive: [[FR-LOI-VALTER]] of 28 December
2015, codified into Title II of Book III of the Code des relations entre le
public et l'administration in March 2016. The confirming evidence is a
**documented negative**: France is absent from the nineteen member states
the Commission served with letters of formal notice on 30 September 2021.

So **no French entity asserts `implements-requirement-from` to the
Directive**, and the comparison matrix shows France with an empty implementer
cell. That is the finding rather than a gap, and it is the only deliberately
empty cell in the matrix.

This is the second near-miss of its kind in three batches. The register
batch caught a search returning the **Archiefwet's** BWBR identifier for the
Kadasterwet; this one caught **2019/790** standing in for **2019/1024**. In
both fields a wrong citation resolves to a real instrument about something
else, which is worse than resolving to nothing.

### Spain had the edge but not the instrument

[[ES-LEY-37-2007]] has carried `implements-requirement-from`
[[EU-OPEN-DATA-DIRECTIVE]] since the Spain batch, with RDL 24/2021 named in
the evidence text. The edge was right and the graph was wrong: it attributed
to a **2007** act the transposition of a **2019** directive.

[[ES-RDL-24-2021]] separates them. Spain issued it as a *decree-law* — the
urgent form — five weeks after receiving its letter of formal notice.

### New relationship type: `amends`

Four of the six modelled transpositions are amendments to statutes that
already existed. The vocabulary had no way to say so: `supersedes` would
have retired instruments that are still in force, and
`implements-requirement-from` records the EU obligation, not the domestic
edit.

`amends` was added to `metadata/relationship-types.md`,
`metadata/controlled-vocabularies.md` and `metadata/schema.json`, and is used
twice — 22 types in the vocabulary now.

Its inverse was **not** added. `implements`/`implemented-by` exist as a pair,
so the vocabulary is now inconsistent with itself; that is queued as a design
question rather than settled by reflex.

### Also closed

- **Red.es** → [[ES-RED-ES]]. The Spain batch judged it "too thinly sourced
  to create". The missing statement was on red.es itself, which lists
  *"Aporta - datos.gob.es"* among its own initiatives. [[ES-DATOS-GOB-ES]]
  now has a `maintained-by` edge, taking the portal-custodian gap from seven
  national portals to six.
- **A French DCAT application profile** — closed as a negative. None exists;
  the sources describe France being measured on conformity with **DCAT-AP
  itself**. Recorded on [[FR-DATA-GOUV]]. Spain's profile turned out to be
  already modelled, folded into [[ES-NTI-RISP]] rather than standing alone,
  so no duplicate was created.

### Verification

- **400 entities, 4,733 edges** (676 relationship, 1,571 association, 2,486
  wikilink), 13 countries
- `validation/run_all.py` — 5/5
- `tools/test_build_graph.py` — 41 OK
- `tools/test_ui.mjs` — **81/81**
- `validation/audit.py` — "no fully disconnected entities"

All four new entities are `verification: search-only`; the egress proxy
blocks eur-lex.europa.eu and legifrance.gouv.fr outright, so no primary text
was read.

## The Dutch register statutes — previous batch

The second of the two clusters the research-queue pass left open, and the one
the register batch itself had deferred with a reason:

> *"Creating six or seven Dutch statutes would be a legislation batch, not a
> registry batch, and doing half of it would leave the layer inconsistent."*

That legislation batch is now done. **7 new entities, 15 relationships.**
389 → **396 entities**, 651 → **666 relationships**.

**Nine of the ten basisregistraties now carry a `governed-by` edge**, against
one before.

| Register | Statute |
|---|---|
| [[NL-BAG]] | [[NL-WET-BAG]] |
| [[NL-BGT]] | [[NL-WET-BGT]] — in force 1 January 2016 |
| [[NL-BRO]] | [[NL-WET-BRO]] — in force 1 January 2018 |
| [[NL-WOZ]] | [[NL-WET-WOZ]] |
| [[NL-NHR]] | [[NL-HANDELSREGISTERWET]] |
| [[NL-BRV]] | [[NL-WEGENVERKEERSWET-1994]] |
| [[NL-BRK]] | [[NL-KADASTERWET]] |
| [[NL-BRT]] | [[NL-KADASTERWET]] — **the same act** |
| [[NL-BRP]] | [[NL-WET-BRP]] — from Batch 3 |
| [[NL-BRI]] | **still none** |

### The weakest of the ten, closed

`discovery/research-queue.md` recorded [[NL-BRT]] as *"the only one of the
ten where **no statute was found at all** … the weakest of the ten."*

It is the **[[NL-KADASTERWET]]** of 3 May 1989, and the reason it resisted
searching is that **there is no "Wet basisregistratie topografie"**. The
Kadasterwet's rules on the public registers and the cadastre carry *both* the
cadastral and the topographic base registration as authentic data.

A gap that looked like missing research was a wrong assumption about the
shape of the law.

### Seven statutes for nine registers

The stelsel's legal underpinning is **not one-to-one**, and that is what this
layer produces:

- **One act carries two registers** — [[NL-KADASTERWET]], for [[NL-BRK]] and
  [[NL-BRT]].
- **Three of the seven are general statutes** that happen to contain a
  registration: the Kadasterwet, [[NL-WET-WOZ]] (a *valuation* act) and
  [[NL-WEGENVERKEERSWET-1994]] (a *road traffic* act). Only four were written
  to constitute a registration.

Neither fact is visible from the register entities; both are visible from the
statutes. That is the argument for having created them, and it is why doing
half would genuinely have been worse than doing none.

### Two commencement patterns, both now held

[[NL-WET-BGT]] came into force in **three stages by provision** — the
register's content and the bronhouder obligations on 1 January 2016, articles
23–24 on 1 July 2017, articles 29–30 on 30 April 2018. That is the
[[GB-DUAA]] pattern. [[CH-EMBAG]] stages by *organisational scope* instead.
The Atlas now holds both and can tell them apart.

### A wrong identifier caught before it shipped

A search for the Kadasterwet's BWBR identifier returned **BWBR0007376** in a
plausible-looking context. That is the **Archiefwet 1995**, not the
Kadasterwet, which is **BWBR0004541**.

Every one of these seven entities is keyed on a BWBR identifier, and one
wrong digit would produce a citation that resolves to a real but unrelated
act — the kind of error that is invisible on review because the URL works.
Worth recording as the specific hazard of this batch.

### What is still open

- **[[NL-BRI]]** — Chapter IVA of the Algemene wet inzake rijksbelastingen is
  named in the sources as its basis, and no citable identifier for that
  chapter as a distinct instrument was found. One register of ten.
- **The Organisatiewet Kadaster** (BWBR0006463), which constitutes
  [[NL-KADASTER]] as a body where the Kadasterwet governs the registers. The
  cleanest body/registers statute pair in the Atlas, and only one half is
  modelled.
- **The implementing decrees and ministerial regulations** beneath all seven
  acts — Besluit and Regeling instruments. A consistent scoping decision, not
  an oversight.
- **Belgium, France and Spain's Open Data Directive transpositions** — the
  one remaining cluster from the first research-queue pass.

### A layout regression the browser tests caught

Adding seven Dutch entities pushed the national band's largest block past a
threshold, and `tools/test_ui.mjs` failed:

```
FAIL  country blocks are further apart than they are wide
      — min separation 463 vs max spread 464
```

**One pixel.** The assertion is that no two country-block centroids sit
closer than the largest block's own mean radius — the property that makes
blocks read as blocks rather than as one ribbon.

The first two fixes were aimed at the wrong axis. Widening `blockGapX` made
it *worse* (463 → 461, by changing which blocks wrap onto which line), and a
minimum horizontal footprint for small blocks helped the wrong pair.
Instrumenting the layout showed why: the binding pair was **PL/PT, stacked
vertically** at Δy 444, not two blocks side by side.

Blocks wrap onto new lines within a band, so it is the **vertical** distance
that a growing country eats into. `blockGapY` 70 → **190** fixes it with real
headroom — **579 vs 464** — and `docs/graph-development.md` now says to raise
that constant and not `blockGapX`, which does not move the binding pair.

Worth recording because the failure was one pixel and the two obvious fixes
were both wrong.

### Connectivity

Components unchanged at **20**, largest 354 → **361**, isolated unchanged at
**8**.

---

## Working the research queue — previous batch

**Status:** completed 2026-08-18.

`discovery/research-queue.md` had drifted: six items it still listed as open
had been closed by later batches and never marked. This batch **reconciled
the queue** and then worked its two highest-value remaining clusters.

**5 new entities, 10 relationships.** 384 → **389 entities**, 641 →
**651 relationships**.

### First, the queue was wrong

Marked done, with the closing entity named in place:

| Item | Closed by |
|---|---|
| IDSA and the IDS reference architecture | data spaces batch — [[INTL-IDSA]], [[INTL-IDS-RAM]] |
| INSEE | cheap structural fixes — [[FR-INSEE]] |
| European Statistical System | UN-connection batch — [[EU-ESS]], now 11 institutes |
| The Dutch NCSC | cheap structural fixes — [[NL-NCSC]] |
| CSIRT NASK / GOV / MON | **partly** — [[PL-NASK]] and [[PL-ABW]]; **CSIRT MON still open** |
| A cybersecurity domain entity | [[DOMAIN-CYBERSECURITY]] |

A queue that lists finished work as pending is worse than no queue: it hides
what is actually open. The reconciliation is the least interesting part of
this batch and probably the most useful.

### The e-invoicing chain — the queue's "highest-value German item"

Carried since the Germany batch, on the grounds that it *"would connect
[[DE-XRECHNUNG]] to [[EU-CEN]] and give the Atlas a standards-body EU→national
chain"*. It does exactly that:

```
EU-EINVOICING-DIRECTIVE  →  EU-EN-16931  →  DE-XRECHNUNG
   (Directive 2014/55/EU)   (CEN, 2017)     (German CIUS)
                                 ↑
                            maintained by
                               EU-CEN
```

[[EU-EINVOICING-DIRECTIVE]] is unusual among the Atlas's directives: it does
not tell member states to do something, it **commissions a standard**. CEN
established CEN/TC 434 in 2014 and produced [[EU-EN-16931]] in 2017 — a
**semantic data model of 176 business terms, not a file format**.

**[[EU-CEN]] now maintains something.** It has had national members pointing
at it since the Germany batch — eleven of them now — and never a standard.
The same note is recorded on [[GB-BSI]] ("maintaining nothing the repository
holds") and on the four bodies added in the structural-fixes batch. This is
CEN's first, and [[DE-DIN]] got its first in the data-spaces batch via DIN
SPEC 27070.

### The Open Data Directive gap, halved

Five countries were recorded as having an unidentified transposition. Two are
now identified, and the reason they were hard is that **they are not the same
kind of instrument**:

| Country | Instrument | Approach |
|---|---|---|
| **Ireland** | [[IE-PSI-REGULATIONS-2021]] — S.I. 376/2021, made 22 July 2021 | **standalone** |
| **Portugal** | [[PT-LEI-26-2016]], third amendment | **amend an existing act** |
| Netherlands | [[NL-WHO]], amended 2024 | amend |
| Belgium, France, Spain | **still unidentified** | amend |

Ireland transposed **five days late**. Portugal folded open data into the act
that already governed **access to administrative and environmental
information** — one Portuguese statute covering what takes three in Germany.

### A source conflict, resolved toward the specific one

A general European survey placed **Ireland and Portugal** as the two member
states with standalone open data legislation. The Portugal-specific sources
say Portugal amended [[PT-LEI-26-2016]] — the amendment pattern.

The Atlas follows the specific source and **records the conflict** on that
entity rather than picking a side silently. Ireland's standalone instrument
is independently confirmed from the Irish Statute Book, so the survey is
right about Ireland and appears wrong about Portugal.

### [[EU-PSI-DIRECTIVE]] — a repealed directive that two live acts needed

Queued from the Belgium batch with a precise reason: it would *"give
[[BE-HERGEBRUIK-WET]] and [[DE-IWG]] somewhere to point."*

Both are national instruments **still in force** that transpose the **2003**
directive, not the 2019 recast. Before this entity the Atlas could either
point them at [[EU-OPEN-DATA-DIRECTIVE]] — dating a 2016 Belgian act to a
2019 instrument — or leave them pointing at nothing. It left them pointing at
nothing.

`status: superseded`, `successor: EU-OPEN-DATA-DIRECTIVE`, and the recast
edge asserted from the successor.

### ⚠ Enforcement the Atlas cannot model

The Commission opened infringement proceedings against **nineteen member
states** over the Open Data Directive, and in **February 2023 referred
Belgium, Bulgaria, Latvia and the Netherlands to the Court of Justice**.

The Atlas has **no way to represent this**: no entity type for an
infringement procedure, no relationship type for "was referred to the Court
over", and no Court of Justice entity.

So a reader can see that [[NL-WHO]] was amended in 2024 — three years after
the deadline — and cannot see from the graph that the Netherlands was taken
to court in between. Recorded on [[EU-OPEN-DATA-DIRECTIVE]] and queued in
`discovery/candidates.md`.

### Connectivity

Components unchanged at **20**, largest 349 → **354**, isolated unchanged at
**8**. [[EU-CEN]] 10 → **11** incoming, and for the first time one of those
is a standard rather than a member.

### What is still open, honestly

The two largest remaining clusters, both left deliberately:

1. **Belgium, France and Spain's Open Data Directive transpositions.** All
   three amended existing law and none was identified. A three-country gap
   now rather than five.
2. **The Dutch basisregistraties statutory bases** — eight statutes. The
   queue's own note says six-plus Dutch statutes is a legislation batch and
   that doing half would leave the layer inconsistent. That judgement still
   holds, so none was done.

---

## Portugal, Luxembourg and Czechia — previous batch

**Status:** completed 2026-08-18.

**23 new entities** plus **54 `applies-in` edges**. 361 → **384 entities**,
555 → **641 relationships**. The Atlas goes from ten countries to
**thirteen**, and from eight EU member states to **eleven**.

The three hubs the previous batch thickened gained three each:

| Hub | Before | After |
|---|---:|---:|
| [[EU-EDPB]] | 8 | **11** |
| [[EU-ESS]] | 8 | **11** |
| [[EU-CEN]] | 7 | **10** |

Every EU member state in the Atlas now has a data protection authority on the
Board, a statistical institute in the ESS, and a standards body in CEN. The
pattern established by the structural-fixes batch held for three new
countries without needing new research into how it works — which is what a
good pattern is for.

### What each country brought

**Czechia — an act about how the state manages its own data.**
[[CZ-ZAKON-60-2026]], *zákon o správě dat a řízeném přístupu*, makes
[[CZ-DIA]] Czechia's **single information point** and the node connecting
Czech data sources to the European data portal.

The Atlas holds a great deal of law *about* data — protection acts, open data
transpositions, cyber acts. It had almost none about **how a state manages
its own data and lets others reach it**. The nearest comparators are Dutch
and are not statutes: [[NL-IBDS]] is a strategy, [[NL-FDS]] a system. **The
Netherlands built the arrangement; Czechia legislated it.**

**Luxembourg — the case against reading size into the graph.** The smallest
country here, and through [[LU-ILNAS]] one of only **two** whose standards
body belongs to all five standardisation organisations the Atlas holds. The
other is the United Kingdom, through [[GB-BSI]], recorded as "the most
connective UK entity". Luxembourg matches it and beats eight larger member
states.

It also shows **small-state concentration** twice: ILNAS is standards,
accreditation *and* product safety; [[LU-CTIE]] runs government IT *and*
implements the State's infrastructure security — functions the Netherlands
splits between [[NL-LOGIUS]] and [[NL-NCSC]].

**Portugal — a verb, and a mandate.** [[PT-LEI-58-2019]] *executes* the GDPR,
where the Dutch act implements it, the German supplements and concretises it,
the Irish gives it further effect and the British simply *is* it. All carry
the same relationship type; the varied language is how each tradition
describes one operation. And [[PT-AMA]]'s remit covers **regulatory**
simplification, which no comparable body in the Atlas records.

### Three name collisions in one batch

| Collision | Entities |
|---|---|
| **CNPD** | [[PT-CNPD]] (Comissão Nacional de Proteção de Dados) and [[LU-CNPD]] (Commission nationale pour la protection des données) |
| **INE** | [[PT-INE]] (Instituto Nacional de Estatística) and [[ES-INE]] (Instituto Nacional de Estadística) |
| **The exact same name** | [[LU-STATEC]]'s full name is *Institut national de la statistique et des études économiques* — **word for word** [[FR-INSEE]]'s |

All three are genuine ambiguities in the world, not Atlas artefacts, and all
three are why the repository keys on **scoped IDs rather than names**. Each
entity says so.

### The one that needed care rather than a template

Czechia splits standardisation between two bodies: **[[CZ-UNMZ]] holds the
formal membership** at ISO, IEC, CEN and CENELEC and the legal responsibility
on behalf of the state, while **ČAS** performs the operational work —
technical committees, drafting, publication.

No other country in the Atlas splits it. The `participates-in` edges are
asserted on ÚNMZ because that is what membership means. Getting it wrong
would have been easy: **ČAS is the more visible body** and publishes the
English-language standards pages, and an entity built from those would have
claimed a membership ČAS does not hold.

**ČAS is not modelled**, which understates Czech standardisation — the body
that actually produces ČSN standards is absent.

### Refusals

- **No relationship between [[LU]] and [[EU-PUBLICATIONS-OFFICE]]**, though
  the Publications Office is seated in Luxembourg. Hosting an institution is
  not participating in it, and modelling it as one would make every host
  state look like a participant in what it hosts.
- **No `maintained-by` on any of the three new portals.** [[LU-CTIE]] has a
  *publisher page* on data.public.lu — that proves publication, not
  custodianship. Seven national portals in the Atlas now lack a custodian and
  one has it.
- **[[CZ-NUKIB]]'s NCKB is not a separate entity.** The sources present it as
  a section of NÚKIB, and a node for an internal division would imply a
  standing it does not have.

### Known gaps, named

- **Luxembourg's GDPR implementation act** (1 August 2018) was not
  identified — the **only member state in the Atlas** without one.
- **NIS2 transpositions for Portugal and Czechia**, so [[PT-CNCS]] and
  [[CZ-NUKIB]] carry anchor edges rather than relationships to acts.
- **Luxembourg's NIS2 competent authority and CSIRT.**
- **Portugal's Open Data Directive transposition**, joining Belgium, France,
  Spain and Ireland on that list — five countries, comfortably a batch.

### Connectivity

Components unchanged at **20**, largest 326 → **349**, isolated entities
unchanged at **8** — still only the domains. Twenty-three new entities and
not one orphan, because the scope-anchor rule is now enforced at build time.

---

## The cheap structural fixes — previous batch

**Status:** completed 2026-08-18.

All four items on `discovery/candidates.md`'s "cheap structural fixes" list,
done. **7 new entities and 16 relationships.** 354 → **361 entities**,
539 → **555 relationships**.

The list was written on the premise that these cost one or a few entities and
connect many. They did.

| Hub | Incoming edges before | After |
|---|---:|---:|
| [[EU-EDPB]] | **3** | **8** |
| [[EU-CEN]] | 3 | **7** |
| [[EU-ESS]] | 7 | **8** |

### 1. The DPAs reach the Board — and a refusal was wrong for an instructive reason

[[EU-EDPB]] had **two** incoming edges when the review flagged it, against
[[EU-ESS]]'s six, in a repository holding **eight** data protection
authorities.

The blocker was recorded on [[DE-BFDI]]: the German federal and Land
authorities are certainly represented, **no source read said so**, and *which
authority represents a member state with seventeen of them* was "precisely
the kind of detail that should not be guessed at."

That refusal was correct in method and the answer was in the Regulation. **
[[EU-GDPR]] Article 68(3)** composes the Board of the head of one supervisory
authority per member state and the [[EU-EDPS]] — and adds:

> where in a Member State more than one supervisory authority is responsible
> …, **a joint representative shall be appointed in accordance with that
> Member State's law**.

The provision that creates the Board anticipates the exact case that had
blocked the edge. Five edges added — [[DE-BFDI]], [[BE-APD]], [[FR-CNIL]],
[[ES-AEPD]], [[PL-UODO]] — joining [[NL-AP]] and [[IE-DPC]]. **No new
entity.**

The three authorities that do **not** get the edge are now a clean set of
three different reasons: [[GB-ICO]] (not a member state), [[NO-DATATILSYNET]]
(EEA cooperation runs through EEA-specific channels), [[CH-EDOEB]] (outside
the Union and the EEA entirely).

### 2. [[FR-INSEE]] — the last missing statistical office

France was the **only Atlas country with no statistical office**, queued
since the France batch. [[EU-ESS]] now holds **every EU member state in the
Atlas**: [[NL-CBS]], [[DE-DESTATIS]], [[BE-STATBEL]], [[ES-INE]],
[[PL-GUS]], [[IE-CSO]] and INSEE.

The three non-member states remain outside it, each for its own reason —
[[GB-ONS]] via [[UN-CES]], [[NO-SSB]] and [[CH-BFS]] with no ESS edge at all.

### 3. Four standards bodies, and the same lesson twice

[[BE-NBN]], [[FR-AFNOR]], [[ES-UNE]] and [[PL-PKN]] created; [[EU-CEN]] and
[[EU-CENELEC]] each gain four members.

The [[IE-NSAI]] refusal — asserted last batch, that the CEN members page had
been *found but not read*, so membership could not be claimed — is also
closed, and **not by reading it**. CEN-CENELEC states the **rule**: its
national members are the standardization bodies of the 27 EU countries.
Ireland is a member state; NSAI is its standards body; the membership follows
from the rule rather than from a list.

Twice in one batch, a refusal for want of a source turned out to be a source
not yet found. **That is not the same as a fact being unknowable**, and both
entities now say so where the refusal used to stand.

**[[INTL-ISO]] is still not asserted** for any of the five. The CEN rule
covers the European organisations and says nothing about ISO;
[[GB-BSI]] and [[DE-DIN]] carry ISO edges because their own sources state it.

### 4. The Dutch and Polish cyber authorities

- **[[NL-NCSC]]** — the gap recorded since the Belgium batch, that
  [[NL-CBW]] was a NIS2 act with no authority attached. On **1 January 2026**
  the Digital Trust Center merged into the NCSC, creating a single
  strengthened body serving **2.4 million** Dutch organisations.
- **[[PL-NASK]]** — conducts **CSIRT NASK**, one of the three national CSIRTs
  under [[PL-KSC]]. [[PL-ABW]] already carried the CSIRT GOV role; **CSIRT
  MON remains unmodelled**, because the Polish defence ministry is not an
  entity.

### ⚠ The one weak edge, named

[[NL-NCSC]] `applies-to` [[NL-CBW]] is `source: interpretation`,
`confidence: low` — the only edge in the batch that is not a plain fact.

The sources establish that the NCSC is the national cyber security body and
that it is guiding organisations through the Cyberbeveiligingswet. **None
read states that it is the competent authority or CSIRT designated under
it**, and the Dutch act distributes competent-authority roles across sectoral
regulators. Compare [[BE-CCB]] (`governed-by` **and** `produces` its act),
[[DE-BSI]] (`governed-by`) and [[FR-ANSSI]] (`applies-to`) — all on firmer
ground.

### Connectivity

Components unchanged at **20**, largest 319 → **326**, isolated entities
unchanged at **8** — still only the domains.

The components number not moving is the point: these fixes did not rescue
islands, they **thickened the middle**. Three hub entities went from thin to
properly connected.

---

## Data spaces — completing the fourteen — previous batch

**Status:** completed 2026-08-18.

**13 new entities.** 341 → **354 entities**, 522 → **539 relationships**.
The data-space layer goes from **8 entities to 19**.

### All fourteen common European data spaces now exist

Batch 10 created four and deliberately left the other ten, because research
had returned only their names and creating shallow entities was the failure
its brief warned against. That was right at the time.

What changed: **six of the ten turned out to have real content** once
searched for individually rather than as a list — deployment programmes,
named operators, funding instruments, live infrastructure.

| Sector | Entity | What it turned out to have |
|---|---|---|
| Energy | [[EU-CEEDS]] | Digital Europe Programme deployment; INSIEME with 50+ partners and 15+ member-state pilots; anchored in the Commission's Strategic Roadmap of 3 June 2026 |
| Research and innovation | [[EU-EOSC]] | **Already running** — EU Node live since October 2024, federation of 13 candidate nodes demonstrated 2025, including CERN and EMBL |
| Cultural heritage | [[EU-CULTURAL-HERITAGE-DATA-SPACE]] | Built on **Europeana** — 60M+ digitised items, Europeana Foundation plus 18 partners selected to steward it |
| Industry | [[EU-MANUFACTURING-DATA-SPACE]] | UNDERPIN and SM4RTENANCE deployment actions |
| Finance | [[EU-FINANCIAL-DATA-SPACE]] | **FIDA** named as one of three components |
| Language | [[EU-LANGUAGE-DATA-SPACE]] | Publishing, language-technology and press participants; stated purpose includes **monetising** data |

The remaining four — [[EU-TOURISM-DATA-SPACE]], [[EU-MEDIA-DATA-SPACE]],
[[EU-SKILLS-DATA-SPACE]], [[EU-PUBLIC-ADMIN-DATA-SPACE]] — are `coverage:
low` and say so. They are created anyway because **holding thirteen of
fourteen would misrepresent the set**. Completeness is the claim;
depth is claimed only where `coverage` says so.

### Having all fourteen makes the differences visible

Four could not show this; fourteen can:

- **One has a Regulation** ([[EU-EHDS]]) and is the **only one carrying
  `applies-in` edges to countries.** The rest are programmes and initiatives,
  not instruments, and do not apply in a member state in the sense that
  relationship carries here. One has legislation in progress
  ([[EU-FINANCIAL-DATA-SPACE]], via FIDA).
- **One already runs** ([[EU-EOSC]]).
- **One inverts the usual order** ([[EU-CULTURAL-HERITAGE-DATA-SPACE]]) —
  designating a data space over infrastructure that had run for a decade.
- **Participants differ**: health systems, energy operators, public
  administrations — and publishers and the press, expected to *sell* into
  the language data space.

### The IDSA layer — a gap carried since Batch 5

`discovery/research-queue.md` has listed the IDSA and its reference
architecture since the Dutch platform batch, reinforced in the German one,
calling it the **best-evidenced gap in the international layer**: two
entities in two countries referred to it in prose with nothing to point at.

- [[INTL-IDSA]] — the association, formed 2016.
- [[INTL-IDS-RAM]] — the reference architecture model: five layers
  (business, functional, process, information, system), each addressed for
  security, certification and governance.

Both refusals are now closed: [[DE-CATENA-X]] `based-on` the IDS-RAM, and
[[NL-ISHARE]] `references` it — the latter deliberately not `based-on`,
because the direction the sources describe is the **IDSA incorporating
iSHARE**, not iSHARE deriving from the model.

**And an unexpected bridge.** DIN SPEC 27070, published 21 February 2020,
standardises the IDS security gateway. [[DE-DIN]] has been an Atlas entity
since the Germany batch and was recorded there as a standards body that
**maintained nothing the Atlas held**. This is the first specification to
connect to it from the standards side. The edge is `references`, not
`maintained-by`: DIN standardised one component, it does not own the model.

### A national lineage

[[DE-MANUFACTURING-X]] is the Atlas's first data space with an **ancestor**.
The sources state it plainly: the BMWK launched [[DE-CATENA-X]] for cars,
Manufacturing-X followed, and its goal is a data ecosystem for factory
equipment suppliers **on the basis of Catena-X**. `based-on`, not `part-of` —
it builds on Catena-X, it does not contain it.

Germany's family as the sources describe it: Catena-X for cars,
Manufacturing-X for factories, energy data-X for power, with Factory-X (2024)
and Aerospace-X as lighthouse projects. Only the first two are modelled.

### Refusals worth naming

- **No edge between [[DE-MANUFACTURING-X]] and
  [[EU-MANUFACTURING-DATA-SPACE]].** Same sector is not evidence of a
  relationship; the EU data space's own deployment projects are UNDERPIN and
  SM4RTENANCE, and no source connects either to the German initiative.
- **No edges from [[EU-PUBLIC-ADMIN-DATA-SPACE]]** to
  [[EU-INTEROPERABLE-EUROPE-ACT]], [[EU-EIF]] or [[EU-SDG]]. Every one would
  be plausible; none is sourced. This is the entity where the temptation was
  strongest, being closest to the Atlas's own subject matter.
- **No cultural-heritage ↔ media/tourism edges**, though the cultural
  heritage sources say it *will explore cooperation* with both. Intent is not
  connection.
- **No `DOMAIN-ENERGY`.** CEEDS would be its only member, below the
  two-entity threshold the domain entities record.

### Connectivity

Components 22 → **20**, largest component 302 → **319**, isolated entities
unchanged at **8** — still only the domains, as the scope-anchor rule
requires.

---

## Every entity reaches its scope anchor — previous batch

**Status:** completed 2026-08-18.

A rule, 24 edges, one new entity, and enforcement so it holds.

**The rule** — now `metadata/relationship-types.md` §2.3: *every entity
carries at least one provenanced relationship, in or out.* An entity that
connects to nothing is invisible in the graph, and the Atlas exists to be a
graph.

### The result

| | Before | After |
|---|---:|---:|
| Entities | 340 | **341** |
| Typed relationships | 498 | **522** |
| Components | 45 | **22** |
| Largest component | 283 | **302** |
| Entities with no typed relationship | 32 | **8 — all domains** |

### What an anchor edge is

Where an entity had no substantive relationship — its statutory basis
unidentified, its custodian unnamed, or the obvious edge resting on a page
found but not read — it now takes an **anchor edge** to the scope it belongs
to. This follows the two conventions the repository already had: country
anchors are reached by `applies-in`, [[EU]] and [[UN]] by `part-of`.

| Entity | Edge | Count |
|---|---|---|
| Instruments — `law`, `strategy`, `data-space` | `applies-in` its country | 7 |
| State bodies and public platforms | `part-of` its country | 14 |
| National bodies **not** part of the state | `related-to` its country | 2 |
| [[INTL-IETF]] | `part-of` [[INTL-ISOC]] | 1 |

Every anchor edge carries evidence, and every one ends with a sentence
naming itself as an anchor edge, so they can be found and revisited when the
substantive edge turns up. **An anchor edge asserts scope and nothing more**
— the missing substantive edges stay in `discovery/unresolved.md`.

### The distinction that mattered

[[NL-SURF]] is a cooperative **owned by its members** and [[NL-NICTIZ]] is a
foundation. Neither is part of the Dutch state, so `part-of` would have been
a false claim about ownership dressed up as a filing convention. Both take
**`related-to`** instead, and say so in their evidence.

That is the whole risk of a rule like this: it makes it cheap to blur a
type. Fourteen bodies took `part-of` because their own sources describe them
as federal offices, directorates, departments or government services; two
did not.

### [[INTL-IETF]] was the hard case

It belongs to no country, is not part of the EU or the UN, and the Atlas has
no `INTL` anchor to fall back on. Rather than attach it somewhere
convenient, this batch found its **actual** parent: the IETF Administration
LLC is the corporate home of the IETF, the IAB and the IRTF, and is a
*single-member disregarded entity* of the **Internet Society**.

[[INTL-ISOC]] was created for it — the batch's only new entity, and
deliberately a stub with a job. The IETF LLC itself is not modelled, so the
edge collapses `IETF → IETF LLC → ISOC` into one hop, which both entities
state rather than hide.

### Domains are exempt, and they earn it

The 8 `DOMAIN-*` entities carry no typed relationships and never will. They
are classification nodes: they carry no factual claims, are already exempt
from the source requirement, and are reached by **association** through
every entity's `domains:` list.

Calling them unconnected is an artefact of looking at one layer. In the
association layer they are the **three largest nodes in the Atlas**:

| Node | Association degree |
|---|---:|
| [[DOMAIN-GOVERNMENT]] | **232** — the most connected node in the repository |
| [[DOMAIN-NATIONAL-SECURITY]] | 47 |
| [[DOMAIN-CYBERSECURITY]] | 35 |

Giving them typed edges would mean inventing a hierarchy that does not
exist.

### Enforcement, so the rule is not just a paragraph

- **`validate_relationships.py`** fails the build on any entity with no
  provenanced relationship in either direction, naming §2.3 and the domain
  exemption. Verified against a deliberately broken entity before shipping.
- **`tools/test_build_graph.py`** gains two tests (39 → **41**): one
  asserting no orphans, and one asserting the domain exemption **earns
  itself** — if a domain stopped being referenced by any entity's `domains:`
  list it would be unreachable in *both* layers, and the exemption would be
  hiding it rather than explaining it.
- **`CONTRIBUTING.md`** step 6a tells a contributor what to do when they
  cannot source a substantive edge.

### A reversal, recorded

Two batches ago this repository argued that own-country `applies-in` should
be **reconsidered rather than extended**, and declined to add it to eighteen
national acts. This batch extends it deliberately, on the maintainer's
instruction, and makes it a documented rule rather than an inconsistency.

The earlier objection was that an edge asserting only "a national instrument
applies in its own country" gives `applies-in` a second meaning. That is
still true. What changed is the trade: a second, clearly documented meaning
is worth less than 24 entities being invisible in the graph. The backlog
note is updated to say so rather than left contradicting the ontology.

---

## Norway, Switzerland and Ireland — previous batch

**Status:** completed 2026-08-18.

**27 new entities** across three countries, plus 18 `applies-in` edges to
Ireland. 312 → **339 entities**, 466 → **495 relationships**. The Atlas goes
from seven countries to **ten**.

The three were chosen from a structural review recorded in
`discovery/candidates.md`, and chosen for what each **proves** rather than
for size.

### The Atlas now holds all four relationships to EU law

| Position | Country | How EU law reaches it |
|---|---|---|
| Member state | NL, DE, BE, FR, ES, PL, **IE** | Directly applicable, or transposed |
| Former member state | GB | Assimilated law, adequacy, extraterritorial scope |
| **EEA EFTA state** | **NO** | **Incorporation by EEA Joint Committee decision, then national implementation** |
| **Neither** | **CH** | **Autonomous law, plus adequacy and bilateral agreements** |

Before this batch the Atlas had two of the four.

### Norway — incorporation is not direct applicability

The batch's sharpest finding, and it is datable:

| Date | Event |
|---|---|
| 25 May 2018 | [[EU-GDPR]] applicable **in the member states** |
| 15 June 2018 | [[NO-PERSONOPPLYSNINGSLOVEN]] adopted |
| **6 July 2018** | **JCD No 154/2018 incorporates the GDPR into Annex XI of the EEA Agreement** |
| **20 July 2018** | The Act enters into force — the GDPR takes effect in Norway |

**Eight weeks** in which the Regulation was in force across the Union and
had no effect in Norway. That cannot happen in a member state, and it is why
**no `applies-in` edge points at [[NO]]**.

The incorporation carried an adaptation with a visible consequence: Norway
notifies its supervisory authority to the **EEA Joint Committee**, not the
Commission — which is why [[NO-DATATILSYNET]] carries no
`participates-in` [[EU-EDPB]] edge.

### Switzerland — a fourth relationship type for a national data act

[[CH-REVDSG]] carries **`aligned-with`** [[EU-GDPR]], not
`implements-requirement-from`. No requirement obliged Switzerland to pass
it; the Swiss legislature harmonised to preserve **adequacy** under Article
45 and to avoid competitive disadvantage. The Atlas now records four answers
to "how does a national data protection act relate to the GDPR":

`implements-requirement-from` (NL, DE, ES, PL, IE, **NO**) ·
`derived-from` (GB) · **`aligned-with` (CH)** · direct applicability (BE, FR).

[[CH-EMBAG]] is the Atlas's **first statutory open-source mandate** —
"Public Money – Public Code" written into a statute rather than a policy.

### Ireland — the one-stop-shop, finally in the graph

[[IE-DPC]] is lead supervisory authority under [[EU-GDPR]] Article 56 for
much of the technology sector established in the Union. Before this batch
the Atlas held **eight** national data protection authorities and modelled
no mechanism connecting any of them.

[[EU-EDPB]] had **two** incoming edges. It now has three. **The general fix
— connecting the remaining five member-state authorities — was not done**
and remains the highest-value item in `discovery/candidates.md`.

[[IE-NCS-BILL]] is `proposed`: Ireland missed the 17 October 2024 NIS2
deadline. It is the Atlas's second pending cyber instrument after
[[GB-CSRB]], and **not the same kind of thing** — one is a sovereign choice,
the other a member state overdue on an obligation.

### ⚠ `NO` parses as the boolean `false` in YAML

Found the hard way. YAML 1.1 — which PyYAML implements — resolves `NO`,
`YES`, `ON`, `OFF`, `Y` and `N` to booleans, so an unquoted `country: NO`
silently became `False` and every Norwegian entity failed validation.

Fixed by quoting (`id: "NO"`, `country: "NO"`), and then **guarded**:

- `validate_frontmatter.py` now reports the boolean coercion by name, for
  both `id` and `country`, instead of "missing or non-string field".
- `tools/test_build_graph.py` gains two tests — a general one asserting no
  entity's `id` or `country` is a bool, and one pinning Norway by name.

Norway is the only ISO 3166-1 alpha-2 code in the Atlas that collides. The
guard is there for the next contributor, not for this batch.

### What the batch deliberately did not do

- **No `applies-in` edge to [[NO]] or [[CH]].** Both are argued at length on
  the anchors rather than forced into a type that means member-state
  applicability.
- **[[UN-AARHUS]] carries no Irish edge.** It is a mixed agreement and
  Ireland's ratification was not researched; the other six member states
  carry the edge on evidence this batch did not gather.
- **[[IE-NSAI]] carries no `participates-in` edges.** The CEN-CENELEC
  members page was returned by search and, like everything else here, not
  read — so the Atlas has a URL that almost certainly lists NSAI and no
  confirmation that it does.
- **[[CH-OPENDATA-SWISS]] is not linked to [[CH-EMBAG]]**, though the act
  creates the legal basis for open government data and this is the federal
  OGD portal. No source read connects them by name.
- **[[NO-ALTINN]] gets no `maintained-by` edge** where [[NO-ID-PORTEN]]
  does — Digdir's own page lists the solutions it operates and Altinn is not
  among them.

### ⚠ Connectivity got worse, and that is the honest cost

| | Before | After |
|---|---:|---:|
| Entities | 312 | **340** |
| Typed relationships | 466 | **498** |
| Components | 31 | **45** |
| Largest component | 272 | **283** |
| Isolated entities | 21 | **32** |

**Eleven of the twenty-eight new entities carry no typed relationship at
all**: [[NO-NSM]], [[NO-SSB]], [[NO-KARTVERKET]], [[NO-ALTINN]],
[[CH-BACS]], [[CH-DVS]], [[CH-SWISSTOPO]], [[CH-EMBAG]], [[IE-TAILTE]],
[[IE-NSAI]] and [[IE-DATA-GOV-IE]].

Every one is a refusal, not an oversight — the statutory basis was not
identified, the custodian was not named, or the obvious edge rests on a page
that was returned by search and not read. Each is argued on its entity and
logged in `discovery/unresolved.md`.

This is the same debt the **loose nodes** batch of 2026-08-17 paid down, and
it is the natural follow-up: eleven entities, each needing one source.

Two anchors were rescued from isolation rather than left:

- **[[NO]]** by [[INTL-EEA-AGREEMENT]] `applies-in` [[NO]] — correct,
  because the EEA Agreement genuinely applies in Norway, and it turns the
  batch's central finding into a relationship.
- **[[CH]]** by [[CH-REVDSG]] `applies-in` [[CH]] — the [[GB-UK-GDPR]]
  precedent, an own-country edge, taken deliberately and flagged on the
  entity as an extension of a pattern `progress/backlog.md` says to
  reconsider. Switzerland has no supra-national instrument in the Atlas to
  reach it, because the bilateral agreements are unmodelled.

### Weakest entities, named

- [[IE-TAILTE]] — `confidence: low`. The merger of Ordnance Survey Ireland,
  the Property Registration Authority and the Valuation Office was not
  confirmed against a primary source; neither citation is a government legal
  source.
- [[CH-DVS]], [[NO-SSB]], [[NO-KARTVERKET]], [[CH-SWISSTOPO]],
  [[IE-NSAI]], [[IE-DATA-GOV-IE]] — all `coverage: low`.
- **No Fedlex citation appears anywhere in the Swiss set**, including on
  [[CH-REVDSG]], which carries the batch's most comparative weight.
- [[NO-DATATILSYNET]] rests on two commercial law-firm surveys; no
  Datatilsynet page describing its own mandate was returned.

### Best-sourced

[[IE-DPC]] — its claims rest on the Commission's own published decisions and
an EDPB news release, not on secondary description.

---

## The intelligence and security services — previous batch

**Status:** completed 2026-08-18.

**47 new entities** — 19 services, 9 oversight bodies, 18 acts and one new
domain — across all seven countries. 265 → **312 entities**;
390 → **465 relationships**.

The relationship layer stays at **31 components** and the largest grows from
**224 to 272 of 312**. Six of the seven country clusters joined the main
component on the day they were written; Spain needed one extra edge, below.

### What was added

| Country | Services | Oversight | Acts |
|---|---|---|---|
| NL | [[NL-AIVD]], [[NL-MIVD]] | [[NL-TIB]], [[NL-CTIVD]] | [[NL-WIV-2017]], [[NL-TWCO]] |
| DE | [[DE-BND]], [[DE-BFV]], [[DE-BAMAD]] | [[DE-PKGR]], [[DE-UKR]] | [[DE-BNDG]], [[DE-BVERFSCHG]], [[DE-MADG]], [[DE-G10]], [[DE-PKGRG]] |
| BE | [[BE-VSSE]], [[BE-ADIV]] | [[BE-COMITE-I]] | [[BE-WIV-1998]], [[BE-TOEZICHTSWET-1991]] |
| FR | [[FR-DGSE]], [[FR-DGSI]], [[FR-DRM]], [[FR-DRSD]] | [[FR-CNCTR]] | [[FR-LOI-RENSEIGNEMENT-2015]] |
| ES | [[ES-CNI]] | — | [[ES-LEY-11-2002]], [[ES-LO-2-2002]] |
| PL | [[PL-ABW]], [[PL-AW]], [[PL-SKW]], [[PL-SWW]] | [[PL-KSS]] | [[PL-UABWAW-2002]], [[PL-USKWSWW-2006]] |
| GB | [[GB-MI5]], [[GB-SIS]], [[GB-GCHQ]] | [[GB-IPCO]], [[GB-ISC]] | [[GB-SSA-1989]], [[GB-ISA-1994]], [[GB-IPA-2016]], [[GB-JSA-2013]] |

Plus [[DOMAIN-NATIONAL-SECURITY]].

### The bridges into the Atlas that already existed

A new cluster of 47 entities would have been an island. Six edges prevented
that, and each was researched rather than assumed:

| Edge | What it joins |
|---|---|
| [[GB-NCSC]] `part-of` [[GB-GCHQ]] | the UK cyber layer to signals intelligence |
| [[ES-CCN]] `part-of` [[ES-CNI]] | the Spanish cyber layer to the intelligence service |
| [[GB-MI5]]/[[GB-SIS]]/[[GB-GCHQ]] `governed-by` [[GB-DPA-2018]] | **Part 4** — the UK legislates its services *into* data protection law |
| [[BE-VSSE]]/[[BE-ADIV]] `governed-by` [[BE-GDPR-WET]] | Belgium's subtitle on intelligence processing |
| [[PL-ABW]] `implements` [[PL-KSC]] | CSIRT GOV is led by the Head of the ABW |
| [[FR-DGSI]] `governed-by` [[FR-LIL]] | ⚠ `confidence: low` — Title IV, state security and defence |
| [[DE-BFV]] `part-of` [[DE-BMI]], [[NL-AIVD]] `part-of` [[NL-BZK]] | the two services the Atlas can place in a ministry it holds |

One incidental fix: **[[ES-ENS]] `aligned-with` [[INTL-ISO-IEC-27001]]**.
[[ES-ENS]] and [[ES-CCN]] were a pre-existing two-node island; this batch
grew it to five and then closed it. The ENS follows the PDCA model inspired
by ISO 27001, and an ISO/IEC 27001-certified ISMS can satisfy ENS
requirements at the LOW level.

### The finding this batch exists to record

Article 4(2) TEU reserves national security to the member states, and
[[EU-GDPR]] Article 2(2)(a) excludes it from the Regulation's scope.
**No EU instrument carries `applies-in` to any entity in this batch, and
none should.** Each country builds its own review machinery instead. That is
why [[DOMAIN-NATIONAL-SECURITY]] exists as a domain and says so at length —
an empty EU column here is a finding, not a gap.

Two countries qualify it. The UK put its services **inside** its data
protection act ([[GB-DPA-2018]] Part 4) and Belgium gave them a dedicated
subtitle in [[BE-GDPR-WET]]. The Union does not regulate here; a state still
may.

### No own-country `applies-in` was added

The preceding batch recorded in `progress/backlog.md` that own-country
`applies-in` should be **reconsidered rather than extended**. Eighteen new
national acts were the obvious opportunity to extend it, and it was not
taken. The countries are reached through the services and their ministries
instead.

### Weakest entities, named

- [[DE-UKR]] — `confidence: low`. Its provisions were moved **out** of
  [[DE-BNDG]] after the Constitutional Court's decision of 28 September
  2022, and where they went could not be established. **The only oversight
  body in the batch with no `governed-by` edge.**
- [[DE-BVERFSCHG]], [[DE-MADG]] — no official statute URL found.
- [[PL-USKWSWW-2006]], [[PL-SKW]], [[PL-SWW]] — no Polish government URL,
  in contrast to the very well-sourced civilian pair.
- [[ES-LEY-11-2002]] — no BOE link, unlike [[ES-LO-2-2002]].
- [[FR-DRM]] — `coverage: low`; nothing from the service's own site.

### Known scope limits, recorded on the entities

- **France's délégation parlementaire au renseignement** is not modelled, so
  France shows independent control and no parliamentary control.
- **DNRED and TRACFIN** — two of the six *premier cercle* services — are
  absent, so [[FR-CNCTR]]'s remit is understated by two.
- **Germany's G10-Kommission** is not modelled.
- **UK Defence Intelligence** has no avowal act and was not researched.
- **Belgium's BIM-wet (2010)** and **OCAD** are not modelled.
- **Poland's CBA** is not modelled.
- The **sixteen German Landesämter für Verfassungsschutz** are out of scope:
  the Atlas has no sub-national level.

---

## Connecting the loose nodes — previous batch

**Status:** completed 2026-08-17.

**No new entities. 14 relationships added**, 376 → 390. The relationship
layer was fragmented into **39 components**; it is now **31**, and the
largest has grown from **184 to 224 of 265 entities**.

Every edge was researched and sourced. Where the Atlas had already looked
and refused for want of a source, **that refusal was left standing**.

| Edge | Nodes pulled into the main component |
|---|---|
| [[EU-EIDAS]] `applies-in` × 6 | **7** — the German identity/OZG cluster |
| [[NL-PDOK]] `aligned-with` [[EU-INSPIRE]] | **21** — the whole basisregistraties system |
| [[FR-RGI]] `based-on` [[EU-EIF]] | **5** — the French DINUM/Etalab cluster |
| [[NL-EAR]] `based-on` [[NL-NORA]] | 2, with [[NL-RORA]] |
| [[DE-BFDI]] `applies-to` [[DE-BDSG]] | 2, with [[DE-IFG]] |
| [[NL-ROSA]], [[NL-PETRA]] `based-on` [[NL-NORA]] | 2 isolated frameworks |
| [[EU-INSPIRE]] `applies-in` [[NL]] | completes INSPIRE 6/6 |
| [[ES-CLAVE]] → [[EU-EIDAS]] | 1 isolated platform |

**Two were open backlog items.** [[EU-EIDAS]] had **no `applies-in` edges at
all** despite being an active EU regulation — flagged by the
comparison-matrix batch — and fixing it reconnected seven German entities.
[[EU-INSPIRE]] applied in five countries and not the Netherlands; the Dutch
*Implementatiewet* of **1 September 2009** closed it.

**The most valuable edge was not obvious.** [[NL-PDOK]] `aligned-with`
[[EU-INSPIRE]] connected **21 entities** — every Dutch base registry, the
stelsel, [[NL-KADASTER]], [[NL-KVK]], [[NL-RDW]]. The whole system had been
a sealed island since the register batch. One sourced sentence about a
platform's standards conformance was the door into a fifth of the Atlas.

**The NORA family is sourced at last.** [[NL-ROSA]] said its NORA link was
*"likely… but was not sourced"*; [[NL-PETRA]] said the obvious edges were
*"precisely what could not be"* sourced. NORA's own wiki enumerates its
**dochters** — one page sourced three edges, and both entities' prose was
rewritten.

**What was left disconnected, deliberately:** [[ES-INCIBE]] ↔ [[ES-LCGC]]
(*"a contested draft allocation of competences is not a relationship"*),
[[NL-HEALTH-RI]] ↔ [[EU-EHDS]] (designation phase runs 2027–2029),
[[INTL-IETF]] ↔ [[INTL-W3C]] (a comparison, not a relationship), the seven
`DOMAIN-*` entities (isolated **by design**), and three organisation-only
pairs with no sourced edge to anything.

⚠ **A convention question answered by not acting.** 72 national instruments
lack `applies-in` to their own country, and 25 of them are the detached
ones — so the blanket pass would have connected most of what remains. It was
**not done**: `applies-in` is defined as the country-neutral applicability
mechanism, and using it for "this Dutch law applies in the Netherlands"
would make 72 of 181 such edges tautological. The backlog item is rewritten
to say the UK edges should probably be **reconsidered rather than
extended**.

**Verification:** `run_all.py` 5/5 · `test_build_graph.py` 37 tests ·
`test_ui.mjs` 81/81 · 265 entities, 2,825 edges, 390 relationships.

See `progress/completed.md` for the full entry.

## Connecting the United Kingdom

**258 → 265 entities, 354 → 376 relationships.** The UK batch left the
country technically correct and practically isolated; this closes that.

| | Before | After |
|---|---|---|
| Typed relationships touching a GB entity | **8** | **29** |
| GB relationship endpoints (rank of 7) | **13 — last** | **45 — third** |
| Edges leaving the UK | **3** | **13** |
| Non-wikilink edges into the [[GB]] anchor | **0** | **7** |
| `audit.py` | `⚠ 1 fully disconnected: ['GB']` | **none** |

**The orphaned anchor is fixed with an existing precedent, not a new
convention.** [[NL-BIO]] already carries `applies-in` to its own country, so
[[GB-UK-GDPR]], [[GB-DPA-2018]], [[GB-DUAA]], [[GB-NIS-REGULATIONS]] and
[[GB-CAF]] now do too. ⚠ Applied to the UK only; the same is true of the
other six countries' instruments and is a consistency pass still owed.

**Principal finding: leaving the EU did not remove the UK from European
standards.** [[GB-BSI]] alone adds five bridges — [[INTL-ISO]], [[INTL-IEC]],
[[EU-CEN]], [[EU-CENELEC]], [[EU-ETSI]] — more than the whole country had
before. **CEN and CENELEC are not EU institutions**; their members are
national standards bodies, so BSI's membership survived Brexit. No EU
instrument applies in the UK *and* the UK sits in three European
standardisation bodies. Both true, neither visible without the other.

**Also settled:** the [[DOMAIN-GEOSPATIAL]] gap ([[GB-OS]], which adds a
second UN-layer link via [[UN-GGIM]]); the cybersecurity chain, now complete
end to end on the UK side via [[GB-CAF]]; and the **adequacy decisions**
([[EU-UK-ADEQUACY]]), refused by the UK batch and now the only edge in the
Atlas running *from* the EU *to* a non-member state.

**Not settled:** [[GB-UKSA]] was created to resolve who holds the UK's
[[UN-CES]] seat and did not. Recorded on both bodies with the ambiguity in
both evidence strings.

**Prose corrected, not just added:** seven existing entities asserted things
this batch made false. Stale prose is a repeated defect here, and adding
entities without revisiting what they contradict is how it happens.

**Verification:** `run_all.py` 5/5 · `test_build_graph.py` 37 tests ·
`audit.py` no disconnected entities · 265 entities, 2,801 edges · 258 of 265
unread.

See `progress/completed.md` for the full entry.

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
