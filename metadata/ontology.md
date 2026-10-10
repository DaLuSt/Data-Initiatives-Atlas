# Ontology

This document defines the entity model of the Data Initiatives Atlas: what
kinds of things the Atlas records, how each kind is identified, and where it
lives in the repository. It is the authoritative reference for Batch 0 and
every batch after it. If a later batch needs a concept this document does not
cover, extend this document first, then use the new concept.

The ontology is deliberately **country-neutral**: nothing here is defined in
terms of Dutch government structures. The Netherlands is the first dataset
loaded into a model designed to hold any country.

---

## 1. Entity types

Every entity in the Atlas has exactly one `type`, drawn from this controlled
vocabulary:

| Type | Meaning | Example |
|---|---|---|
| `initiative` | A named effort, project or programme-like activity that does not fit a more specific type below | `NL-COMMON-GROUND` |
| `organisation` | A body: ministry, agency, standards body, research institute, international organisation | `NL-FORUM-STANDAARDISATIE` |
| `country` | A national geographic/jurisdictional anchor node | `NL` |
| `region` | A regional geographic/jurisdictional anchor node (e.g. the EU) | `EU` |
| `policy` | A non-binding policy position or plan adopted by an organisation | |
| `soft-law` | A non-binding instrument adopted by an international or supranational body in a formal act: a recommendation, resolution, declaration, compact or set of principles. Not legislation, so it is filed under `soft-law/` | `UN-AI-ETHICS-RECOMMENDATION` |
| `act` | Primary legislation: a statute with the rank of law, whether passed by a parliament (including a regional parliament's decree or ordinance) or issued by a government under a constitutional power to make law-rank acts (decree-law). Includes bills and draft acts, with `status: proposed`/`planned` | `NL-WDO` |
| `regulation` | A binding EU regulation (directly applicable), or a national text that is itself a regulation carried over from one (the UK GDPR) | `EU-DATA-ACT` |
| `directive` | An EU directive (requires national transposition) | `EU-OPEN-DATA-DIRECTIVE` |
| `decision` | A binding decision of an EU or EEA body addressed to specific recipients: Commission adequacy decisions, EEA Joint Committee Decisions | `EU-CH-ADEQUACY` |
| `subordinate-legislation` | National legislation made under the authority of an act and ranking below it: statutory instruments, ministerial orders, executive decrees | `IE-PSI-REGULATIONS-2021` |
| `agreement` | A binding agreement between states, or between the governments of one federation: an international treaty, convention or protocol, or a Bund-Länder Verwaltungsvereinbarung | `UN-AARHUS` |
| `strategy` | A published strategic plan | `NL-IBDS` |
| `standard` | A technical or semantic standard | `EU-DCAT-AP` |
| `framework` | An architecture or governance framework that organises standards/policies | `NL-NORA` |
| `programme` | A funded, time-bound programme that delivers initiatives | |
| `data-space` | A federated data-sharing ecosystem for a sector | `EU-HEALTH-DATA-SPACE` |
| `platform` | A concrete technical platform or system | |
| `technology` | A named technology, protocol or technical building block referenced by other entities | |
| `domain` | A subject-matter domain used to classify other entities (Mobility, Health, ...) | `DOMAIN-MOBILITY` |
| `publication` | An independently significant document (report, study) that is not itself an initiative | |

The six legislation types (`act`, `regulation`, `directive`, `decision`,
`subordinate-legislation`, `agreement`) are all filed under `legislation/`
(see §3). They are kept as separate `type` values because they differ in
legal force and in how they relate to other instruments, and folding them
into a single `legislation` type would lose that. Use `country` + `region`
on the entity, and `implements` / `implements-requirement-from`
relationships (§ relationship-types.md), to express the EU → national
transposition chain — never a new `type` per country.

**How to choose among them.** Ask what kind of instrument it is, not how
important it is.

- An EU regulation or directive is `regulation` or `directive`; an EU or EEA
  body's decision to specific recipients is `decision`.
- An instrument between governments is an `agreement`.
- A national instrument made under the authority of a statute, such as a
  ministerial order or statutory instrument, is `subordinate-legislation`.
- Everything else national is an `act`. This includes Belgium's regional
  decrees and ordinances (adopted by regional parliaments), French
  *ordonnances* that Parliament has ratified, and the Spanish *Real
  Decreto-ley* and Portuguese *Decreto-Lei* (decree-laws with the rank of
  law).
- A bill or draft is typed as the instrument it would become, with
  `status: proposed` or `planned`; there is no `bill` type.

"Secondary legislation" in EU usage covers regulations, directives and
decisions; `subordinate-legislation` is named differently on purpose and
means only the national, ranks-below-a-statute sense.

**Rank within a type.** The type says what kind of instrument it is; an
optional `rank` field says where it sits in its legal order (§1.2), which is
how an organic law is told from an ordinary one. A code versus a single
statute (Italy's CAD) is a difference of form and is still not distinguished
(`discovery/unresolved.md` item #11).

**Soft law.** `soft-law` holds non-binding instruments of international or
supranational bodies (see its definition above). It is a separate type with
its own folder, not part of `legislation/`, because it is not legislation and
the `legislation` statistic should not count it. The test is whether the
instrument was adopted by a body in a formal act yet creates no obligation:
five entities qualify today ([[UN-AI-ETHICS-RECOMMENDATION]],
[[UN-2030-AGENDA]], [[UN-GDC]], [[UN-FPOS]] and [[EU-EIF]], a Commission
Communication). A national government's own
non-binding plan stays a `policy` or `strategy`, and a measurement
framework such as [[UN-SDG-INDICATORS]] stays a `framework`.

**Reference: the EU hierarchy of legal acts.** When a new instrument is hard
to classify, use the EU's own hierarchy as the model, and map it onto the
types like this:

| EU tier | Instruments | Atlas type |
|---|---|---|
| Primary law | The Treaties (TEU, TFEU), the Charter of Fundamental Rights, international agreements the EU concludes | `agreement` |
| Secondary law, binding | Regulation, directive, decision (TFEU Art. 288) | `regulation`, `directive`, `decision` |
| Secondary law, non-binding | Recommendations and opinions (TFEU Art. 288), and Commission communications and guidelines | `soft-law` |
| Tertiary law | Delegated and implementing acts adopted under a basic act | the form they take: `regulation`, `directive` or `decision` (for example [[EU-HVD-REGULATION]], an implementing regulation) |

National law has its own ladder, which the types only partly follow:
constitution, then organic law, then ordinary law and decree-law, then
regulations below a statute. `act` covers the middle rungs together and
`subordinate-legislation` the bottom one; the `rank` field (§1.2) records the
rung.

### 1.1 Organisation role (optional)

`type: organisation` is deliberately a big tent — a ministry, an executive
statistics office, a standards-mirror committee and a consultative council
all carry the same `type`. That conflated bodies whose function is to
*deliberate, select or coordinate* with bodies that *execute, publish or
operate*: e.g. [[FR-CNIS]] and [[BE-IIS]] each select a country's SDG
indicator set but publish neither the indicators nor anything else
themselves, and [[NL-NEC]] mirrors CENELEC/IEC standardisation rather than
running infrastructure — structurally different from an executive body like
[[BE-STATBEL]], though both are `type: organisation`.

Rather than splitting these into a new `type` (which would force a hard
line across what is really a spectrum, and relitigate every existing
`organisation` entity), an optional `organisation_role` field is available
on `type: organisation` entities only:

| Value | Meaning |
|---|---|
| `executive` | Runs, publishes or operates something directly |
| `consultative` | Deliberates, selects or advises without itself publishing/operating the result |
| `regulatory` | Sets or enforces binding rules for others |
| `standards-body` | Develops, mirrors or maintains technical/semantic standards |
| `advisory` | Provides non-binding expert input, distinct from `consultative` in that it does not select/decide anything |

The field is optional and additive — omitting it says nothing about an
entity's role, and existing `organisation` entities are not touched
retroactively. `validate_frontmatter.py` rejects it on any other `type` and
rejects any value outside this table. Decided 2026-09-26, closing the
ontology discussion opened by [[FR-CNIS]]/[[BE-IIS]]/[[NL-NEC]] (chose the
"non-breaking field on the existing type" option over a new `type` or
prose-only convention).

---


### 1.2 Legal rank (optional)

The legislation types say what kind of instrument something is. They do not
say how it ranks against other instruments in its own legal order, and that
rank can decide whether a provision binds at all: Title X of [[ES-LOPDGDD]]
binds only because it is an organic law, and an ordinary law such as
[[ES-LEY-37-2007]] cannot amend it. An optional `rank` field records this.

| Value | Meaning | EU analogue |
|---|---|---|
| `constitutional` | A constitution, or a law with constitutional force. No entity uses it yet | The Treaties and the Charter (primary law) |
| `organic` | A statute of higher rank than an ordinary one, usually passed or amended by a qualified majority and reserved for named subject matter (Spain's *Ley Orgánica*) | None |
| `ordinary` | An ordinary statute, including a decree-law that has the rank of law | A legislative act adopted under the ordinary legislative procedure |
| `delegated` | An instrument made under the authority of a statute and ranking below it | Delegated and implementing acts (TFEU Arts 290 and 291) |

Which types may carry which values is fixed in `metadata/schema.json`
(`rank_by_type`) and enforced by `validate_frontmatter.py`: an `act` may be
`constitutional`, `organic` or `ordinary`; `subordinate-legislation` is always
`delegated`; `regulation`, `directive` and `decision` may be `ordinary` or
`delegated`. No other type may carry a rank, and the field is rejected on
them.

Rules for using it:

- **Unset means not assessed.** It does not mean `ordinary`. Set a rank only
  when the entity's own file shows it, such as a title that says *Ley
  Orgánica* or *Orden*, or an instrument that calls itself an implementing
  regulation. Not every legal system has an organic rank, so leaving a
  statute unset is correct unless someone has checked.
- **Rank is not the same as type.** A Belgian "loi organique" is a body's
  founding statute (*organieke wet*), not a rank, and does not make an entity
  `organic`.
- **Rank is not bindingness.** A non-binding instrument is `soft-law`, which
  has no rank. A treaty is an `agreement`, whose place in a state's hierarchy
  differs by state, so it has no rank either.

- **A bill has no rank.** A `proposed` or `planned` instrument is left unset
  until it is enacted; validation rejects a rank on one.
- **Read the rank against the country.** `metadata/rank-basis.md` records, per
  country, which ranks the legal system has and how an instrument of the
  higher rank is recognised. Add a row there before setting a rank for a new
  country.

Added 2026-10-02, closing the organic-versus-ordinary half of
`discovery/unresolved.md` item #11. The national acts of every country in the
Atlas were then backfilled (115 `ordinary`, 2 `organic`), and the EU
instruments from their Official Journal records (30 `ordinary`, 3
`delegated`, with the implementing regulation set earlier). Proposals, the
EEA Joint Committee Decisions and the UK GDPR stay unset (see
`metadata/rank-basis.md`).

## 2. Identifiers

### 2.1 Format

```
<SCOPE>-<SLUG>
```

- `SCOPE` is one of:
  - `UN` — United Nations and UN-system bodies/initiatives
  - `EU` — European Union
  - `<ISO2>` — a national scope, using the ISO 3166-1 alpha-2 code (`NL`, `DE`, `BE`, ...).
    **One exception:** `XK` for Kosovo, which has no ISO 3166-1 code. `XK` is a
    *user-assigned* code — the range ISO reserves for this case — and is what the
    European Commission, the IMF and the World Bank use operationally. The
    exception is named here rather than left as an undocumented break in the rule;
    creating the entity records what the sources describe and takes no position on
    recognition. See `countries/README.md`.
  - `INTL` — international/global entities that are not UN-system (e.g. ISO, W3C, IETF, OECD)
  - `DOMAIN` — subject-matter domain entities (`metadata/taxonomy.md` §1),
    which are cross-cutting classification nodes rather than entities
    belonging to any one geography
- `SLUG` is an uppercase, hyphen-separated short form of the entity's name,
  stable once assigned.

Examples: `NL-IBDS`, `NL-FORUM-STANDAARDISATIE`, `EU-DATA-ACT`,
`UN-DATA-STRATEGY`, `INTL-ISO`.

The three geographic anchor entities are the exception: their `id` is just
the scope itself — `NL`, `EU`, `UN` — since they *are* the scope, not
something scoped within it.

### 2.2 Rules

1. **IDs are permanent.** Never reuse an ID, even after an entity is archived
   or superseded. A superseded entity keeps its ID and gets `status:
   superseded` plus a `successor` field pointing at the new entity's ID.
2. **One ID, one file.** No entity may be represented by more than one file.
3. **Country-neutral entities are never re-scoped per country.** `EU-DATA-ACT`
   is one entity. Do not create `NL-EU-DATA-ACT`. Applicability to a country
   is a relationship (`applies-in`), not a new entity (README §16, and see
   §5 below for the one legitimate exception: genuine national
   implementation legislation).
4. IDs are case-insensitive for comparison but written in upper case in
   frontmatter and prose. The filename is the lower-case form.

### 2.3 Filenames

A file's name is always `<id-lowercased>.md`, e.g. `id: NL-IBDS` →
`initiatives/nl-ibds.md`. This makes the mapping between a wikilink
`[[NL-IBDS]]` and its file mechanical, and lets `validation/validate_ids.py`
detect drift between an `id` field and its filename.

---

## 3. Directory structure and placement rule

```
data-initiatives-atlas/
├── initiatives/
├── legislation/        # act, regulation, directive, decision, subordinate-legislation, agreement
├── policies/
├── strategies/
├── standards/
├── frameworks/
├── programmes/
├── organisations/
├── data-spaces/
├── platforms/
├── publications/
├── domains/
├── countries/
│   └── nl/              # one sub-folder per participating country
├── regions/
│   └── eu/               # one sub-folder per participating region
├── international/
│   └── un/               # one sub-folder per international system/body treated as an anchor
├── metadata/
├── templates/
├── discovery/
├── validation/
└── progress/
```

**Placement is by `type`, not by geography.** An entity's home folder is
determined solely by its `type`, using this fixed map (also encoded
machine-readably in `metadata/schema.json` as `type_folder_map`):

| `type` | Folder |
|---|---|
| `initiative` | `initiatives/` |
| `act`, `regulation`, `directive`, `decision`, `subordinate-legislation`, `agreement` | `legislation/` |
| `soft-law` | `soft-law/` |
| `policy` | `policies/` |
| `strategy` | `strategies/` |
| `standard` | `standards/` |
| `framework` | `frameworks/` |
| `programme` | `programmes/` |
| `organisation` | `organisations/` |
| `data-space` | `data-spaces/` |
| `platform` | `platforms/` |
| `technology` | `platforms/` (technologies are filed alongside platforms; split out a `technology/` folder only if volume later justifies it) |
| `publication` | `publications/` |
| `domain` | `domains/` |
| `country` | `countries/<iso2>/` |
| `region` | `regions/<code>/` |

A Dutch initiative and a UN initiative both live in `initiatives/`, side by
side, distinguished by their `level`, `country` and `region` metadata — never
by a parallel folder tree. This is what keeps the ontology country-neutral
and lets a new country be added without restructuring anything (README
§"Country-Neutral Architecture").

### 3.1 What `countries/`, `regions/` and `international/` are for

These folders are **not** a second copy of the entity tree. They hold two
things only, per participating geography:

1. **The anchor entity itself** — the `country` or `region` node, e.g.
   `countries/nl/nl.md` (`id: NL`, `type: country`), `regions/eu/eu.md`
   (`id: EU`, `type: region`). `international/un/un.md` holds the UN as an
   `organisation` at `level: international`, anchoring the international
   layer the same way.
2. **A curated `index.md`** per geography — a human-maintained hub page of
   wikilinks into the flat type folders, e.g. `countries/nl/index.md` lists
   the key NL-scoped initiatives, legislation, organisations, etc. This
   exists because the canonical store is plain Markdown/YAML with no live
   query engine (README §"Source of Truth"), so a geography's "table of
   contents" has to be maintained as a real page to stay navigable in
   Obsidian and on GitHub.

Do not put entity files themselves inside `countries/nl/`,
`regions/eu/` or `international/un/` beyond the anchor + index described
above.

### 3.2 Domains

`domains/` holds `domain` entities (Mobility, Health, Government, ...) used
to classify other entities via the `domains:` frontmatter field. Only create
a domain when it is actually used to connect two or more other entities
(README Batch 5: "Only create domains where they provide useful graph
relationships").

---

## 4. Geographic model

`level` (controlled vocabulary): `international`, `regional`, `national`, `subnational`,
`local`.

- `international`: scope spans multiple countries by treaty, convention or
  membership, without being a single regional bloc's own instrument (UN
  bodies, ISO/IEC, other worldwide organisations).
- `regional`: scope is a supra-national regional bloc — used for both EU
  institutions and EU legislation directly applicable across member states.
- `national`: scope is one country as a whole. The default level for a
  country's own government bodies, legislation and platforms.
- `subnational`: scope is bounded to part of one country's territory — a
  German Land, a Spanish Comunidad Autónoma or province, a Belgian Region
  or Community — rather than the whole country. Added 2026-08-21 for
  Belgium's regional digital agencies; see `discovery/unresolved.md` item
  #5 for the cross-country modelling history.
- **`sectoral` (retired 2026-10-03).** Until then `level` had a `sectoral`
  value for entities "bounded to one industry or policy sector rather than by
  geography". It was documented on 2026-09-20 (item #10), but only 13
  entities ever used it, and none added afterwards did. It put a second axis
  (sector) into a field that is otherwise geographic, `domains` already
  carries sector, and the rule fitted 70 other entities that did not use it.
  It also took the 13 out of their country's band in the Global Atlas. All 13
  had a single `country` and became `national`: [[BE-KSZ]], [[NL-NICTIZ]],
  [[NL-ROSA]], [[NL-WILMA]], [[NL-DIGIGO]], [[NL-EDUSTANDAARD]], [[NL-DSGO]]
  and the six German data spaces ([[DE-CATENA-X]], [[DE-AEROSPACE-X]],
  [[DE-CONSTRUCT-X]], [[DE-FACTORY-X]], [[DE-HEALTHTRACK-X]], [[DE-MDS]]). Sector
  is expressed with `domains`. Three sectors had no domain to carry them, and
  two were created the same day: [[DOMAIN-SOCIAL-SECURITY]] ([[BE-KSZ]],
  [[BE-KSZ-WET]]) and [[DOMAIN-BUILT-ENVIRONMENT]] ([[NL-DIGIGO]],
  [[NL-DSGO]]). The third, [[NL-WILMA]]'s water authorities, is not covered by
  [[DOMAIN-WATER]] (drinking water and waste water only), so its sector still
  appears only in the entity's text. A `region: EU` tag on an entity does not
  change its level.
- `local`: scope is a municipality or other unit below `subnational`.

- `country`: ISO 3166-1 alpha-2 code, or `null` for EU/UN/international
  entities that are not scoped to one country.
- `region`: a region code such as `EU`, used to tag an entity's regional
  scope. Never used as a substitute for `country`.

## 5. National implementation entities

Per README §"Country-Neutral Architecture", a national implementation is its
own entity **only when a genuine national implementation act, decree or
programme exists** — not merely to mirror an EU entity. When it does exist,
it gets its own `<ISO2>-...` ID and is connected back with `implements` /
`implements-requirement-from` (target: the EU entity), never by embedding
the EU entity's slug into a national ID.

---

## 6. Design decisions recorded here (Batch 0)

- Added `platforms/` and `publications/` folders, not present in the
  original README diagram, to give the `platform`/`technology` and
  `publication` types (defined in README §"What is being mapped?") a home
  without overloading `domains/` or `data-spaces/`. README.md's structure
  diagram has been updated to match.
- The legislation types share the `legislation/` folder but remain distinct
  `type` values. Batch 0 had `law`, `regulation` and `directive`; `law` was
  split into `act`, `decision`, `subordinate-legislation` and `agreement` on
  2026-10-02 (§1).
- Relationship provenance is carried in a `relationships:` frontmatter list
  (see `metadata/relationship-types.md`), which adds an explicit `target`
  field to the block sketched in the brief — without a target, a relationship
  entry cannot be resolved to another entity.
- Country/region/UN anchor entities use their bare scope code as `id`
  (`NL`, `EU`, `UN`) rather than a `<SCOPE>-SLUG` form, since they are the
  scope.
- **Membership dates follow the Union's own list** (decided 2026-10-09, roadmap #533). An entity's
  date for when a country joined the EU is the date the Union's "EU countries" page gives: for
  Belgium, Germany, France, Italy, Luxembourg and the Netherlands that is 1 January 1958, the entry
  into force of the Treaty of Rome. The signature date (25 March 1957) is recorded in the entity's
  body where it matters. The same holds for later accessions: the date is the one the Union's list
  gives, not the signature or ratification date, and the evidence string cites that list.

### Records that fit two types (decided 2026-10-09, roadmap #499)

**Rule.** When a record fits two types, it is filed under the type its **own primary source** gives
it ("framework", "initiative", "programme", a register, an agency); if the source uses several
words, under the type of what it **does** (a system that runs is a `platform`, a body that decides
is an `organisation`, a set of agreements is a `framework`). The other fit is named in the entity's
prose, so a reader who searches by it is pointed to the record. A type is **not** changed for style,
and an existing record is retyped only when a filter or the folder gives a misleading answer. A new
type is added only under `metadata/relationship-types.md` §2.4's test (a clear semantic need, at
least one real example, a `schema_version` bump), never to settle one record.

| Record | Fits | Decision | Why |
|---|---|---|---|
| [[EU-SEMIC]], [[EU-DSSC]] | `organisation`, programme, "action" | stay `organisation` | the best available fit; the sources call SEMIC an action and give DSSC no clear legal form |
| [[UN-CES]] | `programme`, `organisation` | stays `programme` | convened by [[UN-UNECE]], the same reading as [[UN-GGIM]] |
| [[NL-HEALTH-RI]] | `data-space`, `organisation` | stays one `data-space` | the infrastructure has no name of its own, so a split would invent one |
| [[NL-NDW]] | `platform`, `organisation` | stays `platform` | typed by its primary function, though it is a partnership of 19 governments |
| [[NL-FDS]] | `framework`, `initiative`, `programme` | stays `framework` | its own sources call it an *afsprakenstelsel*, a system of agreements |
| [[NL-COMMON-GROUND]] | `initiative`, `framework`, `programme` | stays `initiative` | the sources use it as a vision first; the programme is a part of it |
| [[NL-GDI]] | `platform`, `framework` | stays `platform` | its own name is an infrastructure; the agreements inside it are described in prose |
| [[NL-BASISREGISTRATIES]] | `framework`, `platform` | stays `framework` | it is the *stelsel*, not a single register |
| the ten basisregistraties | `platform`, a missing `register` type | stay `platform` | no `register` or `dataset` type exists and one would touch ten files and the schema; the question moves to #458 (register typing), where authentic data is decided |
| [[NL-BIO]] | one entity or two | stays one with versions | BIO2 is a new version of a continuously named baseline, unlike Wob and Woo or Archiefwet 1995 and 2026, which are separate instruments with their own legal basis; split it if a re-verification contradicts this |
| ISO/IEC JTC 1 | an entity or none | not modelled | it sits between the two organisations and the standards; model it when a source ties a standard to it by name |

