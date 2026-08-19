# Final Global Relationship Pass and Quality Gate

Brief §26 and §27, run 2026-08-14 against 125 entities. Reproduce with
`python validation/run_all.py` and `python validation/audit.py`.

---

## Part 1 — Final Global Relationship Pass (§26)

### What was added

12 relationships, all sourced, taking the graph from 119 to **131**
provenanced relationships and reducing entities with no relationship of
their own from 35 to 29.

**Institutional membership.** The UN layer modelled `part-of` and the EU
layer did not — an inconsistency Batch 11 caught for the three institutions
and this pass extended to the rest:

| Entity | Added |
|---|---|
| `EU-EUROSTAT` | `part-of` → `EU-COMMISSION` (sourced: "the Community statistical authority, which is the Commission (Eurostat)") |
| `EU-SEMIC` | `part-of` → `EU-COMMISSION` |
| `EU-ENISA`, `EU-EDPB`, `EU-EDPS`, `EU-PUBLICATIONS-OFFICE` | `part-of` → `EU` |
| `UN-2-0`, `UN-GDC`, `UN-DATA-COMMONS`, `UN-DATA-STRATEGY` | `part-of` → `UN` |

**Links stated in prose but missing from frontmatter:**

| Entity | Added |
|---|---|
| `EU-COMMISSION` | `produces` → `EU-CYBERSECURITY-STRATEGY` |
| `EU-DSSC-BLUEPRINT` | `applies-to` → `EU-COMMON-DATA-SPACES` |

`part-of` is now the most common relationship type in the Atlas (25),
ahead of `maintained-by` (20) and `applies-in` (17).

### The four relationship patterns §26 asks for

**Vertical (UN → EU → National → Sector):** ⚠ **incomplete.**

| Direction | Count |
|---|---|
| EU → NL | 15 |
| NL → EU | 10 |
| NL → INTL | 2 |
| EU → INTL | 1 |
| **UN → anything** | **0** |

Unchanged by this pass, and deliberately so. Two links would close most of
the gap — `UN-UNSD` → `EU-EUROSTAT` and `UN-FPOS` → `NL-WET-CBS` — and both
were examined again here and refused again: they are plainly true in
substance, and no source read states either. **Adding them would have made
this report look better and the Atlas less trustworthy.**

**Horizontal (country ↔ country):** not applicable. One country is
modelled. The mechanism exists but cannot be exercised until a second
country joins.

**Standards (international → EU → national):** ✅ **complete, twice.**

```
INTL-DCAT (W3C) → EU-DCAT-AP (SEMIC) → NL-DCAT-AP-NL (Geonovum)
INTL-ISO-IEC-27001 + -27002 (ISO/IEC) → NL-BIO / BIO2
```

**Legislative (EU regulation → national implementation → national policy):**
✅ **complete.**

```
EU-CYBERSECURITY-STRATEGY → EU-NIS2 → NL-CBW → (supersedes) NL-WBNI
                          ↘ EU-CER
EU-GDPR                → NL-UAVG → NL-AP → (participates-in) EU-EDPB
EU-OPEN-DATA-DIRECTIVE → NL-WHO
EU-ITS-DIRECTIVE       → NL-NTM → (part-of) NL-NDW
```

**Organisational (initiative → organisation → programme → data space):**
partial. Organisation and programme links are dense; the data-space end is
thin because 10 of the 14 EU data spaces were never created for want of
sources.

---

## Part 2 — Final Quality Gate (§27)

### Ontology

| Check | Result |
|---|---|
| Internally coherent model | ✅ 17 entity types, all defined in `metadata/ontology.md` |
| Entity types used consistently | ✅ no type used outside its documented folder |
| Relationships semantically meaningful | ✅ 22 types, each defined; `proposes-to-supersede` added when `supersedes` would have asserted an untruth, and `amends` when it would have retired an instrument still in force. `status` gained `adopted` on the same test: a treaty ratified by 34 states and not in force is neither `proposed` nor `active` |
| Domains justified | ✅ all 6 connect ≥2 entities; 7 more withheld below threshold |

### Metadata

| Check | Result |
|---|---|
| IDs unique | ✅ 125 IDs across 125 files |
| IDs never reused | ✅ 3 superseded entities retained with IDs intact |
| Statuses controlled | ✅ active 115, planned 4, superseded 3, unknown 2, proposed 1 |
| Confidence present | ✅ every entity; **none claims `high`** |
| Coverage present | ✅ every entity; **none claims `high`** |
| Dates used appropriately | ⚠ 37 of 125 carry dates; several are `YYYY-01-01` placeholders meaning "year known, day unknown" — an unresolved schema question |
| `last_verified` populated where possible | ✅ **6, all domain nodes** — see the defect below |

### Sources

| Check | Result |
|---|---|
| Important entities sourced | ✅ every non-domain entity has ≥1 source; 310 source entries |
| Sources authoritative | ⚠ mostly; **2 entities rely solely on weak sources** (`NL-PETRA`, `UN-DATA-COMMONS`) |
| URLs real | ❌ **unverified — no URL in this repository has been fetched** |
| Source dates recorded | ✅ **0 `accessed` dates, correctly** — see the defect below |

### Relationships

| Check | Result |
|---|---|
| Cross-level relationships represented | ⚠ EU↔NL and INTL→NL yes; **UN→anything no** |
| Supported by evidence | ✅ every provenanced relationship carries `evidence` |
| Interpretations distinguished | ✅ 120 `fact` / 11 `interpretation`, each labelled and explained |

### Geography

| Check | Result |
|---|---|
| Model country-neutral | ✅ **no country-scoped copies of supra-national entities** (README §16) |
| Another country addable immediately | ✅ structurally — 17 `applies-in` relationships all target `NL`; **untested with a second country** |

### Temporal integrity

| Check | Result |
|---|---|
| Historical states representable | ✅ 5 `successor` and 6 `previous_version` chains, **0 mismatches** |
| Superseded initiatives retained | ✅ `EU-NIS`, `NL-WOB`, `NL-EAR` all kept with IDs intact |

Chains: `EU-NIS`→`EU-NIS2`, `NL-WBNI`→`NL-CBW`, `NL-WOB`→`NL-WOO`,
`NL-EAR`→`NL-RORA`, `NL-ARCHIEFWET-1995`→`NL-ARCHIEFWET-2026`, plus
`EU-EIDAS`→`EU-EIDAS2` as an amendment lineage.

### Technical integrity

| Check | Result |
|---|---|
| YAML parses | ✅ all 125 |
| Internal links valid | ✅ 0 broken wikilinks |
| IDs unique | ✅ |
| Validation passes | ✅ 5/5, 0 errors, 0 warnings |

---

## Defects found and fixed by this gate

**1. Four sources claimed `accessed` dates.** The `NL`, `EU` and `UN`
anchors carried `accessed: "2026-08-14"` on their sources — **asserting
access that never happened.** Removed.

**2. The same three anchors claimed `last_verified`.** They are
`verification: unverified`; claiming a verification date was a direct
contradiction. Set to null.

Both were Batch 0 residue, written before the network block was known and
before the `verification` field existed. Together with the three defects
found in Batches 6/11, **every defect this project's validation has
surfaced originated in its own earliest work** — which is an argument for
running gates like this one earlier, not only at the end.

---

## Verdict

**Structurally: passes.** Ontology coherent, IDs unique and stable,
temporal chains complete and consistent, country-neutrality intact,
provenance labelled throughout, zero technical defects.

**Evidentially: does not pass, and cannot yet.** 119 of 125 entities rest
on sources nobody has read; **no URL in the repository has been fetched**.
The gate cannot certify that any description is accurate, any status
current, or any cited page real.

**Structurally incomplete in one respect:** the UN layer connects to
nothing outside itself. The brief's target architecture is
UN → EU → National → Sector; the Atlas delivers EU → National → Sector
with an unattached UN component.

### What would close the remaining gaps

1. **A re-verification pass** — needs outbound HTTPS. Every URL is already
   recorded in the entities' `sources:` lists.
2. **Two sourced links** — `UN-UNSD`→`EU-EUROSTAT` and
   `UN-FPOS`→`NL-WET-CBS` — would connect the international layer.
3. **A second country** — the only real test of the country-neutral model.

The Atlas is a sound, honestly-labelled skeleton with a working ontology and
tooling. It is not yet a verified reference, and it says so everywhere it
matters.
