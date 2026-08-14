# Current Batch

**Status:** Batch 2 complete (search-only sourcing) and validated. No batch
currently in progress.

See `progress/completed.md` for the Batch 1 and Batch 2 reports and
`progress/backlog.md` for the remaining plan.

## Outstanding debt carried forward

30 of the Atlas's 36 entities were compiled from search-engine results only
— page retrieval is blocked by the environment's network policy, and the
reduced evidence standard was accepted explicitly rather than silently. All
30 carry `verification: search-only`. (The six exceptions are the three
geographic anchors [[NL]], [[EU]] and [[UN]], sourced in Batch 0, and the
three domain taxonomy nodes, which make no factual claims.)

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

## Dangling relationships awaiting later batches

Several Batch 2 organisations have deliberately empty `relationships:`
lists because their defining links point at entities that do not exist yet.
These should be revisited as the relevant batches land:

| Entity | Awaiting | Batch |
|---|---|---|
| [[NL-AP]] | `EU-GDPR`, Dutch UAVG | 8, 3 |
| [[NL-NATIONAAL-ARCHIEF]] | Archiefwet | 3 |
| [[NL-CBS]] | Wet op het CBS; responsible ministry | 3 |
| [[NL-TNO]] | TNO-wet | 3 |
| [[NL-KVK]] | Handelsregisterwet | 3 |
| [[NL-NEN]] | ISO, IEC, CEN | 9, 13 |
| [[NL-NICTIZ]] | `DOMAIN-HEALTH`, HL7, European Health Data Space | 5, 10 |
| [[NL-SURF]] | `DOMAIN-EDUCATION`, EOSC, DANS, Health-RI | 5, 10 |
