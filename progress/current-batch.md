# Current Batch

**Status:** Batch 3 complete (search-only sourcing) and validated. No batch
currently in progress.

See `progress/completed.md` for the Batch 1–3 reports and
`progress/backlog.md` for the remaining plan.

## Time-critical item

[[NL-CBW]] (Cyberbeveiligingswet) is recorded `status: planned` with
`start_date: 2026-08-15` — **the day after this entry was written**. If that
date held, the entity is now stale: `status` should be `active`, and
[[NL-WBNI]] should move from `active` to `superseded`. Verify before relying
on either.

## Outstanding debt carried forward

45 of the Atlas's 51 entities were compiled from search-engine results only
— page retrieval is blocked by the environment's network policy, and the
reduced evidence standard was accepted explicitly rather than silently. All
45 carry `verification: search-only`. (The six exceptions are the three
geographic anchors [[NL]], [[EU]] and [[UN]], and the three domain taxonomy
nodes, which make no factual claims.)

A **re-verification pass** is owed before the Netherlands layer can be
considered coherent, and is a precondition for Batch 6 (Netherlands
Validation):

```
grep -rl "verification: search-only" .
```

For each entity: fetch the URLs already recorded in its `sources:` list,
confirm or correct every claim, then set `verification: primary-source`,
populate `last_verified`, add per-source `accessed:` dates, and resolve the
matching rows in `discovery/unresolved.md`.

Priority items for that pass, where a wrong value would propagate:

| Entity | What to check first |
|---|---|
| [[NL-CBW]] / [[NL-WBNI]] | Did the 15 Aug 2026 commencement happen? |
| [[NL-WHO]] | Which entry-into-force date is correct (19 Jun vs 2 Aug 2024)? |
| [[NL-ARCHIEFWET-2026]] | The act's actual name |
| [[NL-FDS]] | Was the afsprakenstelsel established Feb 2026? |
| [[NL-NDS]] / [[NL-DIGIBETER]] | Is NDS operative, and did it supersede DIGIbeter? |

## Dangling relationships awaiting later batches

Batch 3 closed five of the gaps Batch 2 left open. Remaining:

| Entity | Awaiting | Batch |
|---|---|---|
| [[NL-KVK]] | Handelsregisterwet (no source located) | 4+ |
| [[NL-NEN]] | ISO, IEC, CEN | 9, 13 |
| [[NL-NICTIZ]] | `DOMAIN-HEALTH`, HL7, European Health Data Space | 5, 10 |
| [[NL-SURF]] | `DOMAIN-EDUCATION`, EOSC, DANS, Health-RI | 5, 10 |
| [[NL-WDO]] | eIDAS — to settle whether it has an EU origin | 8 |
| [[NL-WBNI]] | Original NIS Directive | 8 |
| [[NL-AP]] | EDPB, EDPS | 9 |
