# Current Batch

**Status:** No batch in progress. **The second research-queue pickup**
completed on 2026-08-22. Full detail moved to `progress/completed.md`;
summary below. `discovery/reverification-allowlist.md` ranks the next
re-verification targets, and `discovery/research-queue.md` carries the
rest of the research backlog.

**Corrected/added guidance on what is actually blocked:** `efta.int` is
**not** bot-walled — it returns a 403 to a browser-spoofing User-Agent
but real content (200) to an honest, identifying one, the same kind
`tools/reverify.py` sends (found in the first research-queue pickup).
`isap.sejm.gov.pl` — the Sejm's legal-text database — **is** genuinely
blocked: an Incapsula JavaScript challenge page regardless of
User-Agent, browser-spoofing or honest alike (found in the second
research-queue pickup, researching [[PL-PESEL]]). `www.iso.org`,
`www.coe.int` and `unece.org` remain untested against an honest
User-Agent and are still treated as blocked. `eur-lex.europa.eu` and
`europarl.europa.eu` are confirmed **not** blocked — both were read
directly and successfully in the fourth verification-gap push (NO,
NO-PERSONOPPLYSNINGSLOVEN, INTL-EEA-AGREEMENT, INTL-EEA-JCD-154-2018),
matching the same false-blocked finding earlier pushes made for
`legislation.gov.uk`.

## Second research-queue pickup — 2026-08-22

Picked up **PESEL**, Poland's population register — the "Next"-priority
research-queue item carried since the Poland batch and named on
[[PL-COI]]'s own entity as "named in a list of systems and nothing
more." It is now two entities: [[PL-PESEL]] (the register and the
eleven-digit number itself) and [[PL-EWIDENCJA-LUDNOSCI]] (the 2010 act
that has been its legal basis since 1 March 2015), following the same
platform+law pairing [[NL-BRP]]/[[NL-WET-BRP]] uses.

[[PL-PESEL]] is `maintained-by` [[PL-COI]] with a specific date and
mechanism (the State Registers System, launched 1 March 2015) that
neither PL-COI's nor PESEL's own prior mentions carried on their own —
found by cross-reading gov.pl's own PESEL page against Polish Wikipedia.
`isap.sejm.gov.pl` proved genuinely unreadable (see above), so the Act's
original 2010 Dziennik Ustaw promulgation citation is not asserted —
only the consolidated-text citation gov.pl itself quotes. Full write-up
in `progress/completed.md` under "The second research-queue pickup".

## Earlier pushes

- **First research-queue pickup** (2026-08-22): the EFTA Surveillance
  Authority, the EFTA Court and the EEA Joint Committee — three EEA
  institutions [[NO]], [[INTL-EFTA]] and [[INTL-EEA-AGREEMENT]] had all
  separately named as "not modelled" — anchored to
  [[INTL-EEA-AGREEMENT]] rather than [[INTL-EFTA]] since their
  jurisdiction excludes Switzerland. Found that `efta.int` is not
  actually bot-walled (see above). See "The first research-queue
  pickup".
- **Fourth push** (2026-08-22): the entire Norway cluster (10 entities:
  [[NO]], seven `country: NO` entities, and the two EEA connective
  entities [[INTL-EEA-AGREEMENT]] and [[INTL-EEA-JCD-154-2018]]). A
  significant finding on [[NO-NSM]] — its own official website states
  directly that NSM is one of Norway's three intelligence, surveillance
  and security services; found `participates-in` [[UN-GGIM]] on
  [[NO-KARTVERKET]]; fixed a factual error on [[NO-DIGDIR]]. See "The
  fourth verification-gap push".
- **Third push** (2026-08-22): the entire Swiss cluster (9 entities plus
  CH) — closed the "no Fedlex citation" gap on CH-REVDSG/CH-EMBAG, found
  CH-OPENDATA-SWISS `governed-by` CH-EMBAG, corrected a wrong alternative
  name on CH-DVS. See "The third verification-gap push".
- **Second push** (2026-08-22): the entire UK cluster (17 entities),
  [[EU-UK-ADEQUACY]], and the entire Ireland cluster (7 entities) — 24
  entities moved. See "The second verification-gap push".
- **First push** (2026-08-22, merged as PR #54): 37 entities across four
  German and UK clusters. See "The verification-gap multi-batch push".
