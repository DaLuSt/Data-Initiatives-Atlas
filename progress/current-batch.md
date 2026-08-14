# Current Batch

**Status:** Batch 4 complete (search-only sourcing) and validated. No batch
currently in progress.

See `progress/completed.md` for the Batch 1–4 reports and
`progress/backlog.md` for the remaining plan.

## Time-critical item

[[NL-CBW]] (Cyberbeveiligingswet) is recorded `status: planned` with
`start_date: 2026-08-15` — **the day after it was written**. If that date
held, `status` should now be `active` and [[NL-WBNI]] `superseded`. Verify
before relying on either.

## Outstanding debt carried forward

56 of the Atlas's 62 entities were compiled from search-engine results only
— page retrieval is blocked by the environment's network policy, and the
reduced evidence standard was accepted explicitly rather than silently. All
56 carry `verification: search-only`. (The six exceptions are the three
geographic anchors [[NL]], [[EU]] and [[UN]], and the three domain taxonomy
nodes, which make no factual claims.)

A **re-verification pass** is owed before the Netherlands layer can be
considered coherent, and is a precondition for Batch 6:

```
grep -rl "verification: search-only" .
```

For each entity: fetch the URLs already in its `sources:` list, confirm or
correct every claim, then set `verification: primary-source`, populate
`last_verified`, add per-source `accessed:` dates, and resolve the matching
rows in `discovery/unresolved.md`.

Priority order, where a wrong value would propagate furthest:

| Entity | What to check first |
|---|---|
| [[NL-CBW]] / [[NL-WBNI]] | Did the 15 Aug 2026 commencement happen? |
| [[NL-PETRA]] | Does this entity survive contact with a real source at all? |
| [[NL-WHO]] | Which entry-into-force date is correct (19 Jun vs 2 Aug 2024)? |
| [[NL-ARCHIEFWET-2026]] | The act's actual name |
| [[NL-RORA]] / [[NL-EAR]] | The 2024 succession and the site-naming oddity |
| [[NL-FDS]] | Was the afsprakenstelsel established Feb 2026? |
| [[NL-NDS]] / [[NL-DIGIBETER]] | Is NDS operative, and did it supersede DIGIbeter? |

## Dangling relationships awaiting later batches

| Entity | Awaiting | Batch |
|---|---|---|
| [[NL-GEMMA]] | VNG Realisatie (currently points at [[NL-VNG]]) | 5+ |
| [[NL-ROSA]] | Edustandaard; `DOMAIN-EDUCATION` | 5 |
| [[NL-SURF]] | `DOMAIN-EDUCATION` (threshold now met) | 5 |
| [[NL-NICTIZ]] | `DOMAIN-HEALTH`, HL7, EHDS | 5, 10 |
| [[NL-BIO]] | ISO/IEC 27001 & 27002 | 14 |
| [[NL-DCAT-AP-NL]] | EU DCAT-AP, W3C DCAT | 9, 14 |
| [[NL-NEN]] | ISO, IEC, CEN | 9, 13 |
| [[NL-KVK]] | Handelsregisterwet (no source located) | 5+ |
| [[NL-WDO]] | eIDAS | 8 |
| [[NL-WBNI]] | Original NIS Directive | 8 |
| [[NL-AP]] | EDPB, EDPS | 9 |
