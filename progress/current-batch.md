# Current Batch

**Status:** Batch 10 complete (search-only sourcing) and validated. No batch
currently in progress.

The Netherlands layer (Batches 1–5) and the EU layer (Batches 7–10) are
populated. **Batches 6 and 11 — the two validation batches — are both
deferred** for the same reason; see below.

## Why the validation batches are deferred

Batch 6 (Netherlands Validation) and Batch 11 (EU Validation) cannot be
completed in substance while the sourcing debt stands: **101 of the Atlas's
110 entities** are `verification: search-only`, compiled from search results
with no cited page actually read.

The automated suite already checks and passes everything checkable without
sources — IDs, links, relationship types, vocabularies, placement. What
Batch 6 *additionally* asks for — outdated information, incorrect statuses,
missing sources, unsupported relationships — requires reading primary
sources. Running it now would produce a report that reads like assurance
without being any.

**Do the re-verification pass first**, then Batches 6 and 11.

## Priority fixes for the next verification pass

Ranked by how far a wrong value would propagate:

| Entity | What to check |
|---|---|
| [[EU-DIGITAL-OMNIBUS]] | **Current legislative status.** Three proposed repeals hang off it, and the record dates from Nov 2025 |
| [[NL-CBW]] / [[NL-WBNI]] | Did the 15 Aug 2026 commencement happen? |
| [[EU-AI-ACT]] | Which obligations the omnibus postponed; find a EUR-Lex citation |
| [[NL-PETRA]] | Does this entity survive contact with a real source at all? |
| [[EU-EIF]] ↔ [[EU-INTEROPERABLE-EUROPE-ACT]] | How do they relate? One root or two? |
| [[EU-EIF]] → [[NL-NORA]] | Is NORA formally the Dutch NIF? |
| [[NL-ISHARE]] | Dutch or European now? Affects the country model |
| [[NL-WHO]] | Which entry-into-force date (19 Jun vs 2 Aug 2024)? |
| [[NL-ARCHIEFWET-2026]] | The act's actual name |
| [[NL-RORA]] / [[NL-EAR]] | The 2024 succession and site-naming oddity |
| [[NL-FDS]] | Was the afsprakenstelsel established Feb 2026? |
| [[NL-NDS]] / [[NL-DIGIBETER]] | Is NDS operative, and did it supersede DIGIbeter? |

## Cross-level chains established so far

Cybersecurity — both generations, all three package elements:

```
EU-CYBERSECURITY-STRATEGY  (Dec 2020)
   │ influences                    ╲ influences
EU-NIS2  ◄──supersedes── EU-NIS     EU-CER
   │                        │
NL-CBW   ◄──supersedes── NL-WBNI
```

Others:

```
EU-GDPR                → NL-UAVG → NL-AP → (participates-in) EU-EDPB
EU-OPEN-DATA-DIRECTIVE → NL-WHO
EU-ITS-DIRECTIVE       → NL-NTM  → (part-of) NL-NDW
EU-EIDAS  ──amended-by──→ EU-EIDAS2 → EU-EUDI-WALLET
EU-DIGITAL-DECADE ──applies-in──→ NL
EU-EIF ──applies-in──→ NL   (NORA link unconfirmed)
```

Standards — the first end-to-end international → EU → national descent:

```
INTL-DCAT (W3C) → EU-DCAT-AP (SEMIC) → NL-DCAT-AP-NL (Geonovum)
```

Membership chains (each from a sourced composition rule, not a source naming
the Dutch body):

```
NL-AP → EU-EDPB    NL-NEN → EU-CEN    NL-CBS → EU-EUROSTAT
```

Pending (proposal, not adopted):

```
EU-DIGITAL-OMNIBUS ──proposes-to-supersede──→ EU-DGA
                   ──proposes-to-supersede──→ EU-OPEN-DATA-DIRECTIVE
```

## Open schema questions

1. **Date precision.** Several entities carry a `YYYY-01-01` `start_date`
   meaning "year known, day unknown", indistinguishable from a real
   1 January date. Adopt a convention or add a `date_precision` field.
2. **Office-holders.** Deliberately not modelled (see [[NL-MIDO]]). Confirm
   that is the intended long-term rule.

## Dangling relationships awaiting later batches

Batches 9–10 closed several of these. What remains:

| Entity | Awaiting | Batch |
|---|---|---|
| [[EU-EIF]] | Interoperable Europe Board | later |
| [[NL-NEN]] | ISO, IEC | 13 |
| [[INTL-DCAT]] | W3C (the organisation), and a W3C source | 13, 14 |
| [[NL-BIO]] | ISO/IEC 27001 & 27002 | 14 |
| [[EU-CER]] | Wet weerbaarheid kritieke entiteiten (NL) | later |
| [[EU-COMMON-DATA-SPACES]] | The 10 remaining sectoral data spaces | later |
| [[EU-EHDS]] | Dutch health data access body designation (2027–2029) | later |
| [[EU-EMDS]] | Whether it builds on the national access point network | later |
| [[EU-DSSC-BLUEPRINT]] | Whether Dutch afsprakenstelsels map to its rulebook model | later |
| [[NL-NICTIZ]] | HL7 | later |
| [[NL-ISHARE]] | Topsector Logistiek, DMI, IDSA | later |
| [[NL-DSGO]] | digiGO | later |
| [[EU-DIGITAL-OMNIBUS]] | Free Flow of Non-Personal Data Regulation | later |
| [[NL-GEMMA]] | VNG Realisatie | later |
| [[NL-ROSA]] | Edustandaard | later |
| [[NL-KVK]] | Handelsregisterwet | later |
| [[EU-EUDI-WALLET]] | Dutch wallet implementation | later |
| [[EU-ETSI]] | Any ETSI standard at all | later |

**Closed in Batches 9–10:** `EU-CYBERSECURITY-ACT` → ENISA; `NL-AP` → EDPB;
`NL-NEN` → CEN; `NL-CBS` → Eurostat; `NL-DCAT-AP-NL` → DCAT-AP → DCAT.
