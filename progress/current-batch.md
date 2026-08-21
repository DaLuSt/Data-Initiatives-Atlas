# Current Batch

**Status:** No batch in progress. **Re-verification batch 1** completed on
2026-08-21 — the first pass where `tools/reverify.py` actually fetched and
read live pages. Full detail moved to `progress/completed.md`; summary below.
Batches 2+ remain: ~414 entities are still `verification: search-only` or
`unverified`, and `discovery/reverification-allowlist.md` ranks the next
targets. Skip entities citing only `eur-lex.europa.eu`, `www.iso.org`,
`www.coe.int` or `unece.org` — those hosts return a bot-defense challenge
page to every fetch in this environment, egress policy notwithstanding.

## Re-verification batch 1, in brief

**Date:** 2026-08-21. Twenty-one entities moved to `verification:
primary-source`: the seven Dutch base-registration statutes
(`NL-WET-BAG`, `NL-WET-BGT`, `NL-WET-BRO`, `NL-WET-WOZ`,
`NL-HANDELSREGISTERWET`, `NL-WEGENVERKEERSWET-1994`, `NL-KADASTERWET`) and
fourteen EU-scoped organisations (national statistics institutes and data
protection authorities citing `ec.europa.eu` / `edpb.europa.eu`).

Two substantive corrections: [[NL-WET-BGT]]'s third commencement date was
30 April 2018 in the entity and is 1 July 2018 on `wetten.overheid.nl` (30
April is when the commencement decree was *published*, not when it took
effect); [[NL-KADASTERWET]]'s "Kadasterwet 1989" alternative name is not
attested by the statute's own metadata and was removed. Three diacritic
typos fixed (`Datenschutzbehorde`, `Bundesanstalt Statistik Osterreich`,
`Dataombudsmannens byra`, each missing an umlaut or accent the authority's
own site uses).

`LU-STATEC` and `PT-INE` were attempted and not moved — see
`progress/completed.md` for why. Full write-up, counts and the egress
finding (open egress does not mean every host is readable — four
high-value hosts answer with a bot-defense challenge page instead of
content) are in `progress/completed.md` under "The re-verification pass,
batch 1" and in `docs/re-verification.md` §"A machine-corroborated pass".
