# Current Batch

**Status:** Batch 7 complete (search-only sourcing) and validated. No batch
currently in progress.

The Netherlands layer (Batches 1–5) and the EU core layer (Batch 7) are
populated. **Batch 6 was skipped** — see below.

## Why Batch 6 was skipped, and when to do it

Batch 6 is "Netherlands Validation". It cannot be completed in substance
while the sourcing debt stands: 70 of the Atlas's 79 entities are
`verification: search-only`, compiled from search results with no cited page
actually read.

The automated suite already checks and passes everything checkable without
sources — IDs, links, relationship types, vocabularies, placement. What
Batch 6 *additionally* asks for — outdated information, incorrect statuses,
missing sources, unsupported relationships — requires reading primary
sources. Running it now would produce a report that reads like assurance
without being any.

**Do Batch 1b (re-verification) first**, then Batch 6. Every URL needed is
already recorded in the entities' `sources:` lists.

## Priority fixes for the next verification pass

Ranked by how far a wrong value would propagate:

| Entity | What to check |
|---|---|
| [[EU-EIDAS2]] / [[EU-EUDI-WALLET]] | **Rebuild entirely** — both rest only on secondary sources |
| [[NL-CBW]] / [[NL-WBNI]] | Did the 15 Aug 2026 commencement happen? |
| [[NL-PETRA]] | Does this entity survive contact with a real source at all? |
| [[EU-EIF]] → [[NL-NORA]] | Is NORA formally the Dutch NIF? High-value link |
| [[EU-EIF]] | Has the post-2017 EIF revision been adopted? |
| [[NL-ISHARE]] | Dutch or European now? Affects the country model |
| [[NL-WHO]] | Which entry-into-force date (19 Jun vs 2 Aug 2024)? |
| [[NL-ARCHIEFWET-2026]] | The act's actual name |
| [[NL-RORA]] / [[NL-EAR]] | The 2024 succession and site-naming oddity |
| [[NL-FDS]] | Was the afsprakenstelsel established Feb 2026? |
| [[NL-NDS]] / [[NL-DIGIBETER]] | Is NDS operative, and did it supersede DIGIbeter? |

## Cross-level chains established so far

```
EU-CYBERSECURITY-STRATEGY → EU-NIS2 → NL-CBW → (supersedes) NL-WBNI
EU-GDPR → NL-UAVG → NL-AP
EU-OPEN-DATA-DIRECTIVE → NL-WHO
EU-DIGITAL-DECADE ──applies-in──→ NL
EU-EIF ──applies-in──→ NL   (NORA link unconfirmed)
```

## Open schema question

Four entities carry a `YYYY-01-01` `start_date` meaning "year known, day
unknown", indistinguishable from a real 1 January date. Adopt a convention
or add a `date_precision` field before it spreads further.

## Dangling relationships awaiting later batches

| Entity | Awaiting | Batch |
|---|---|---|
| [[EU-COMMON-DATA-SPACES]] | The 14 sectoral data spaces | 10 |
| [[EU-CYBERSECURITY-STRATEGY]] | CER Directive | 8 |
| [[EU-EIF]] | Interoperable Europe Act & Board | 8, 9 |
| [[EU-DATA-STRATEGY]] | Data Governance Act, Data Act | 8 |
| [[NL-WDO]] | Original eIDAS (910/2014) | 8 |
| [[NL-NTM]] | EU ITS instrument | 8 |
| [[NL-WBNI]] | Original NIS Directive | 8 |
| [[NL-AP]] | EDPB, EDPS | 9 |
| [[NL-NEN]] | ISO, IEC, CEN | 9, 13 |
| [[NL-DCAT-AP-NL]] | EU DCAT-AP, W3C DCAT | 9, 14 |
| [[NL-BIO]] | ISO/IEC 27001 & 27002 | 14 |
| [[NL-HEALTH-RI]] / [[NL-NICTIZ]] | European Health Data Space, HL7 | 10 |
| [[NL-ISHARE]] | Topsector Logistiek, DMI, IDSA | 10 |
| [[NL-DSGO]] | digiGO | 10 |
| [[NL-GEMMA]] | VNG Realisatie | 5+ |
| [[NL-ROSA]] | Edustandaard | 5+ |
| [[NL-KVK]] | Handelsregisterwet | 5+ |
