# Current Batch

**Status:** Batch 1 complete (search-only sourcing) and validated. No batch
currently in progress.

See `progress/completed.md` for the Batch 1 report and
`progress/backlog.md` for the remaining plan.

## Outstanding debt carried forward

15 of Batch 1's 16 entities were compiled from search-engine results only —
page retrieval was blocked by the environment's network policy, and the
reduced evidence standard was accepted explicitly rather than silently. All
15 carry `verification: search-only`. (The 16th, `DOMAIN-GOVERNMENT`, is a
taxonomy node making no factual claims.)

A **re-verification pass** is owed before the Netherlands layer can be
considered coherent, and should be treated as a precondition for Batch 6
(Netherlands Validation):

```
grep -rl "verification: search-only" .
```

For each entity: fetch the URLs already recorded in its `sources:` list,
confirm or correct every claim, then set `verification: primary-source`,
populate `last_verified`, add per-source `accessed:` dates, and resolve the
matching rows in `discovery/unresolved.md`.
