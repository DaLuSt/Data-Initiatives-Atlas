# Current Batch

**Status:** No batch in progress. **The fourth verification-gap push**
completed on 2026-08-22. Full detail moved to `progress/completed.md`;
summary below. 336 entities remain `verification: search-only`/`unverified`
(181 now `primary-source`); `discovery/reverification-allowlist.md` ranks
the next targets.

**Corrected guidance on what is actually blocked, found during the
fourth push:** `www.iso.org`, `www.coe.int`, `unece.org` and `efta.int`
return a bot-defense challenge (403, Cloudflare) to every fetch in this
environment and can be skipped or treated as unread. **`eur-lex.europa.eu`
and `europarl.europa.eu` are NOT blocked** — earlier guidance here said
otherwise and was wrong; both were read directly and successfully in the
fourth push (NO, NO-PERSONOPPLYSNINGSLOVEN, INTL-EEA-AGREEMENT,
INTL-EEA-JCD-154-2018), matching the same false-blocked finding earlier
pushes made for `legislation.gov.uk`.

## Fourth push — 2026-08-22

Closed out the **entire Norway cluster** (10 entities: [[NO]], seven
`country: NO` entities, and the two EEA connective entities
[[INTL-EEA-AGREEMENT]] and [[INTL-EEA-JCD-154-2018]]).

Highlights: a significant finding on [[NO-NSM]] — its own official
website states directly that NSM is one of Norway's three intelligence,
surveillance and security services, overturning the entity's previous
declined-to-classify stance, which had rested only on an encyclopaedia
entry; found and sourced `participates-in` [[UN-GGIM]] on [[NO-KARTVERKET]];
found new evidence (a site publisher footer) for who operates
[[NO-ALTINN]]; fixed a factual error on [[NO-DIGDIR]] (it claimed
[[GB-GDS]] carries `maintained-by` edges to identity platforms — GB-GDS
explicitly declines one) and corrected a confusing relationship-direction
rationale to match the established convention. Full write-up in
`progress/completed.md` under "The fourth verification-gap push".

## Earlier pushes

- **Third push** (2026-08-22): the entire Swiss cluster (9 entities plus
  CH) — closed the "no Fedlex citation" gap on CH-REVDSG/CH-EMBAG, found
  CH-OPENDATA-SWISS `governed-by` CH-EMBAG, corrected a wrong alternative
  name on CH-DVS. See "The third verification-gap push".
- **Second push** (2026-08-22): the entire UK cluster (17 entities),
  [[EU-UK-ADEQUACY]], and the entire Ireland cluster (7 entities) — 24
  entities moved. See "The second verification-gap push".
- **First push** (2026-08-22, merged as PR #54): 37 entities across four
  German and UK clusters. See "The verification-gap multi-batch push".
