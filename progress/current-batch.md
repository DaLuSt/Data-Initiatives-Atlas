# Current Batch

**Status:** No batch in progress. **The candidates pickup** completed on
2026-08-22. Full detail moved to `progress/completed.md`;
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
research-queue pickup, researching [[PL-PESEL]]). `riigiteataja.ee`,
Estonia's official legal gazette, is likewise genuinely blocked — a
plain JavaScript single-page application with no static content at all
(found in the third research-queue pickup, researching
[[EE-STATISTIKAAMET]]). `www.iso.org`, `www.coe.int` and `unece.org`
remain untested against an honest User-Agent and are still treated as
blocked. `unece.org` was re-tested with an honest User-Agent in the
candidates pickup and remains genuinely blocked (403) — unlike
`efta.int`, this one really is closed. `eur-lex.europa.eu` and
`europarl.europa.eu` are confirmed **not** blocked — both were read
directly and successfully in the fourth verification-gap push (NO,
NO-PERSONOPPLYSNINGSLOVEN, INTL-EEA-AGREEMENT, INTL-EEA-JCD-154-2018),
matching the same false-blocked finding earlier pushes made for
`legislation.gov.uk`. `eur-lex.europa.eu` does occasionally return an
empty AWS WAF challenge response (`202`, `x-amzn-waf-action: challenge`)
on a given request — the candidates pickup hit this once and got the
real page on a bare retry, so treat a single `202` there as a flake to
retry, not a block.

## The candidates pickup — 2026-08-22

Picked up two items from `discovery/candidates.md` rather than
`discovery/research-queue.md`: the **High-level Political Forum** and
the **eFTI Regulation**, both carried since the candidate-clearing batch
of 2026-08-21.

[[UN-HLPF]] closes a gap [[EU-VOLUNTARY-REVIEW-2023]] named in its own
text: the review "was a key input to" the Forum, which "has no entity,
so nothing here says the review was *submitted to* it." `hlpf.un.org`,
the Forum's own domain already cited unread, is bot-walled (403) even
with an honest User-Agent; `sustainabledevelopment.un.org`, a sibling UN
DESA subdomain carrying the same institutional description, was not
blocked and is the entity's primary source instead.

[[EU-EFTI-REGULATION]] closes the other row with a **negative result**:
secondary sources described its data set as built on the UN/CEFACT
MMT-RDM model, sourced only to a UNECE presentation and a project
website, "not in the regulation." This pass reads the Regulation's full
text directly and searches it for "UN/CEFACT", "CEFACT", "MMT" and
"UNECE" — none appears anywhere. The claim is not merely unread, now
that the instrument itself has been read; the actual data set is
delegated to a future Commission act the Regulation does not identify,
which is where any real UN/CEFACT connection would have to live. No
such relationship is asserted. Full write-up in `progress/completed.md`
under "The candidates pickup".

## Earlier pushes

- **Fifth verification-gap push** (2026-08-22): the entire Iceland and
  Liechtenstein clusters (6 entities), added alongside Norway's to test
  whether the Norwegian EEA pattern generalises. Found a translation
  error on [[LI-DSG]]'s English-language source (two date typos its own
  German original didn't have) and confirmed `coe.int`/`iso.org`
  genuinely bot-walled. See "The fifth verification-gap push".
- **Third research-queue pickup** (2026-08-22): [[EE-STATISTIKAAMET]],
  Statistics Estonia, the twelfth national statistical office in the
  Atlas — an [[EU-ESS]] member on the same strong-evidence standard
  [[PL-GUS]] set. Found `riigiteataja.ee` genuinely bot-walled (see
  above). See "The third research-queue pickup".
- **Second research-queue pickup** (2026-08-22): [[PL-PESEL]] and
  [[PL-EWIDENCJA-LUDNOSCI]], Poland's population register and its 2010
  legal basis — closing a gap [[PL-COI]] had named as "in a list of
  systems and nothing more." Found `isap.sejm.gov.pl` genuinely
  bot-walled (see above). See "The second research-queue pickup".
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
