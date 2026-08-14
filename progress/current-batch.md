# Current Batch

**Status:** Batch 5 complete (search-only sourcing) and validated. No batch
currently in progress.

The Netherlands layer (Batches 1–5) is now populated. See
`progress/completed.md` for the batch reports and `progress/backlog.md` for
what remains.

## Read this before starting Batch 6

Batch 6 is "Netherlands Validation", and the brief says: *"Do not continue
until the Dutch layer is coherent."*

**Batch 6 cannot be completed properly under the current sourcing
constraint.** 63 of the Atlas's 72 entities are `verification: search-only`
— compiled from search results, with no cited page actually read. A
validation pass can check internal consistency (IDs, links, relationship
types, vocabularies — all of which the automated suite already checks and
all of which pass), but it **cannot** check what Batch 6 actually asks for:
outdated information, incorrect statuses, missing sources, unsupported
relationships. Those all require reading primary sources.

Running Batch 6 now would produce a validation report that certifies
internal tidiness while the underlying facts remain unverified — which is a
worse outcome than not running it, because it would look like assurance.

**Recommended order:**
1. **Batch 1b — re-verification** (needs network access to public
   government/EU domains). Every URL needed is already recorded in the
   entities' `sources:` lists.
2. **Batch 6 — validation**, which then becomes meaningful.

If network access cannot be restored, the honest alternative is to proceed
to Batches 7+ (EU layer) under the same declared constraint, and defer
Batch 6 until verification is possible.

## Time-critical item

[[NL-CBW]] (Cyberbeveiligingswet) is `status: planned` with
`start_date: 2026-08-15` — **the day after it was written**. If that date
held, `status` should now be `active` and [[NL-WBNI]] `superseded`.

## Re-verification priority order

Where a wrong value would propagate furthest:

| Entity | What to check first |
|---|---|
| [[NL-CBW]] / [[NL-WBNI]] | Did the 15 Aug 2026 commencement happen? |
| [[NL-PETRA]] | Does this entity survive contact with a real source at all? |
| [[NL-ISHARE]] | Is it Dutch or European now? Affects the country model |
| [[NL-WHO]] | Which entry-into-force date is correct (19 Jun vs 2 Aug 2024)? |
| [[NL-ARCHIEFWET-2026]] | The act's actual name |
| [[NL-RORA]] / [[NL-EAR]] | The 2024 succession and the site-naming oddity |
| [[NL-FDS]] | Was the afsprakenstelsel established Feb 2026? |
| [[NL-NDS]] / [[NL-DIGIBETER]] | Is NDS operative, and did it supersede DIGIbeter? |

## Open schema question

Four entities carry a `YYYY-01-01` `start_date` meaning "year known, day
unknown". That is indistinguishable from a real 1 January date. Either adopt
an explicit convention or add a `date_precision` field before the pattern
spreads further. See `discovery/unresolved.md`.

## Dangling relationships awaiting later batches

| Entity | Awaiting | Batch |
|---|---|---|
| [[NL-NTM]] | EU ITS instrument (national access point obligation) | 8 |
| [[NL-ISHARE]] | Topsector Logistiek; DMI; IDSA | 10 |
| [[NL-DSGO]] | digiGO | 10 |
| [[NL-HEALTH-RI]] | European Health Data Space | 10 |
| [[NL-NICTIZ]] | HL7, EHDS | 10 |
| [[NL-GEMMA]] | VNG Realisatie (currently points at [[NL-VNG]]) | 5+ |
| [[NL-ROSA]] | Edustandaard | 5+ |
| [[NL-PDOK]] | Ministerie van I&W, Rijkswaterstaat | 5+ |
| [[NL-BIO]] | ISO/IEC 27001 & 27002 | 14 |
| [[NL-DCAT-AP-NL]] | EU DCAT-AP, W3C DCAT | 9, 14 |
| [[NL-NEN]] | ISO, IEC, CEN | 9, 13 |
| [[NL-KVK]] | Handelsregisterwet (no source located) | 5+ |
| [[NL-WDO]] | eIDAS | 8 |
| [[NL-WBNI]] | Original NIS Directive | 8 |
| [[NL-AP]] | EDPB, EDPS | 9 |
