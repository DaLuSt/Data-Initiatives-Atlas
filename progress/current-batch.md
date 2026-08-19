# Current Batch

**Status:** No batch in progress. **The cheap structural fixes** was
completed on 2026-08-18, after the data spaces batch.

## The cheap structural fixes

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
