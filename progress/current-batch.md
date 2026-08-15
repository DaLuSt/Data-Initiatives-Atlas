# Current Batch

**Status:** Batch 8 complete (search-only sourcing) and validated. No batch
currently in progress.

The Netherlands layer (Batches 1–5) and the EU layer (Batches 7–8) are
populated. **Batch 6 was skipped** — see below.

## Why Batch 6 was skipped, and when to do it

Batch 6 is "Netherlands Validation". It cannot be completed in substance
while the sourcing debt stands: 81 of the Atlas's 90 entities are
`verification: search-only`, compiled from search results with no cited page
actually read.

The automated suite already checks and passes everything checkable without
sources — IDs, links, relationship types, vocabularies, placement. What
Batch 6 *additionally* asks for — outdated information, incorrect statuses,
missing sources, unsupported relationships — requires reading primary
sources. Running it now would produce a report that reads like assurance
without being any.

**Do Batch 1b (re-verification) first**, then Batch 6.

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
EU-GDPR                → NL-UAVG → NL-AP
EU-OPEN-DATA-DIRECTIVE → NL-WHO
EU-ITS-DIRECTIVE       → NL-NTM  → (part-of) NL-NDW
EU-EIDAS  ──amended-by──→ EU-EIDAS2 → EU-EUDI-WALLET
EU-DIGITAL-DECADE ──applies-in──→ NL
EU-EIF ──applies-in──→ NL   (NORA link unconfirmed)
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

| Entity | Awaiting | Batch |
|---|---|---|
| [[EU-CYBERSECURITY-ACT]] | ENISA | 9 |
| [[EU-EIF]] | Interoperable Europe Board | 9 |
| [[NL-AP]] | EDPB, EDPS | 9 |
| [[NL-NEN]] | ISO, IEC, CEN | 9, 13 |
| [[NL-DCAT-AP-NL]] | EU DCAT-AP, W3C DCAT | 9, 14 |
| [[EU-CER]] | Wet weerbaarheid kritieke entiteiten (NL) | 9+ |
| [[EU-COMMON-DATA-SPACES]] | The 14 sectoral data spaces | 10 |
| [[NL-HEALTH-RI]] / [[NL-NICTIZ]] | European Health Data Space, HL7 | 10 |
| [[NL-ISHARE]] | Topsector Logistiek, DMI, IDSA | 10 |
| [[NL-DSGO]] | digiGO | 10 |
| [[NL-BIO]] | ISO/IEC 27001 & 27002 | 14 |
| [[EU-DIGITAL-OMNIBUS]] | Free Flow of Non-Personal Data Regulation | 9 |
| [[NL-GEMMA]] | VNG Realisatie | 9+ |
| [[NL-ROSA]] | Edustandaard | 9+ |
| [[NL-KVK]] | Handelsregisterwet | 9+ |
| [[EU-EUDI-WALLET]] | Dutch wallet implementation | 9+ |
