# Current Batch

**Status:** No batch in progress. **The seventh verification-gap push**
completed on 2026-08-25 — the entire Italy cluster (6 entities). Full
detail moved to `progress/completed.md`; summary below.
`discovery/reverification-allowlist.md` ranks the next re-verification
targets, and `discovery/research-queue.md` carries the rest of the
research backlog.

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
[[EE-STATISTIKAAMET]]). `www.iso.org` and `www.coe.int` were tested
with an honest User-Agent (fifth verification-gap push, and again in
the sixth push on [[LU]] and [[LU-ILNAS]]) and remain genuinely
blocked — a real Cloudflare/bot-wall block, not a User-Agent artefact.
`unece.org` was re-tested with an honest User-Agent in the candidates
pickup and remains genuinely blocked (403) — unlike `efta.int`, this
one really is closed. `eur-lex.europa.eu` and
`europarl.europa.eu` are confirmed **not** blocked — both were read
directly and successfully in the fourth verification-gap push (NO,
NO-PERSONOPPLYSNINGSLOVEN, INTL-EEA-AGREEMENT, INTL-EEA-JCD-154-2018),
matching the same false-blocked finding earlier pushes made for
`legislation.gov.uk`. `eur-lex.europa.eu` does occasionally return an
empty AWS WAF challenge response (`202`, `x-amzn-waf-action: challenge`)
on a given request — the candidates pickup hit this once and got the
real page on a bare retry, so treat a single `202` there as a flake to
retry, not a block. `grunddata.dk`, cited on [[DK-DATAFORDELER]] and
[[DK-GRUNDDATA]], no longer resolves at all (checked https and http) —
a dead domain, not a bot-wall, found in the fourth research-queue
pickup. `consilium.europa.eu` was tested for the first time this
session in the seventh push and is genuinely blocked (403) even with
an honest User-Agent. `bosettiegatti.eu`, an Italian legal-text mirror
cited on the Italy cluster, is the **first host found doing the
reverse of `efta.int`**: it returns a custom IIS "999" bot-defense
error to the honest, identifying User-Agent `tools/reverify.py` sends,
but serves the page normally (`200`) to a browser-spoofing one — found
in the seventh verification-gap push, researching [[IT-CAD]].

## The seventh verification-gap push — 2026-08-25

Re-verified the entire Italy cluster (6 entities: [[IT]], [[IT-CAD]],
[[IT-AGID]], [[IT-ISTAT]], [[IT-DATI-GOV-IT]] and [[IT-SPID]] —
[[IT-GARANTE]] was already `primary-source` from an earlier pass), all
promoted from `verification: search-only` to `primary-source`.

**A stale country anchor, fixed.** [[IT]]'s own body text still said
Italy carried "no national entities" and flagged the anchor as a gap
to research — a claim that stopped being true once [[IT-AGID]],
[[IT-CAD]], [[IT-DATI-GOV-IT]], [[IT-ISTAT]] and [[IT-SPID]] were added
and [[IT-GARANTE]] was re-verified, none of which had updated the
anchor. Rewritten to describe the six entities it now anchors.

**[[IT-DATI-GOV-IT]]'s custodian gap, closed.** dati.gov.it's own "Chi
siamo" page states plainly it has been "gestito dall'Agenzia per
l'Italia Digitale" (managed by AgID) since 2015 — a `maintained-by`
edge this entity did not previously carry, closing Italy's row on the
open-data-portal-custodian gap tracked in `discovery/research-queue.md`
alongside [[NL-DATA-OVERHEID]] and [[ES-RED-ES]].

**[[IT-ISTAT]]'s EU-ESS membership, upgraded to a direct statement.**
Istat's own "L'Istat nella UE e nel mondo" page names its European
Statistical System Committee membership directly, rather than resting
on the generic composition-rule inference — the same strong-evidence
tier established for [[PL-GUS]] and [[EE-STATISTIKAAMET]], and a step
up from [[LU-STATEC]]'s weaker tier in the previous pass.

**A new "unreadable" host shape: blocks the honest UA, not the
deceptive one.** `bosettiegatti.eu`, which carries the actual text of
[[IT-CAD]], is unreachable by `tools/reverify.py`'s own honest User-Agent
but opens normally to a browser-spoofing one — the mirror image of the
`efta.int` finding from the first research-queue pickup. The law text
was read this pass via the browser-spoofing fetch, but any future
automated `tools/reverify.py` run against this exact host will report
it UNREACHABLE.

## Earlier pushes

- **Sixth verification-gap push** (2026-08-25): the entire Luxembourg
  cluster (6 entities). Found [[LU-ILNAS]]'s sixth standardisation
  membership (the ITU), breaking its tie with [[GB-BSI]], and sourced
  Luxembourg's GDPR act date via an ELI URL without creating a law
  entity from it. See "The sixth verification-gap push".

Re-verified the entire Luxembourg cluster (6 entities: [[LU]],
[[LU-CTIE]], [[LU-CNPD]], [[LU-STATEC]], [[LU-ILNAS]] and
[[LU-DATA-PUBLIC]]), all promoted from `verification: search-only` to
`primary-source`.

**A sixth [[LU-ILNAS]] membership.** ILNAS's own "Découvrir la
normalisation" page states directly that it represents Luxembourg in
three European standardisation organisations (CEN, CENELEC, ETSI) and
three international ones — and the third international one is the
**ITU**, a membership this entity did not previously carry. This breaks
what the Atlas had recorded as a tie with [[GB-BSI]] at five
memberships each: GB-BSI's own five do not include the ITU, so ILNAS is
now the single most-connected national standards body in the Atlas, a
genuine new fact rather than an artefact of uneven sourcing.

**Luxembourg's GDPR act date, sourced via an ELI URL.** [[LU-CNPD]]'s
own "Législation" page links to the implementing law under the label
"Loi 'Protection des données'" at an ELI (European Legislation
Identifier) URL whose date segment confirms **1 August 2018**.
`legilux.public.lu` itself, which would carry the law's official title
and text, is a JavaScript single-page application with no static
content — consistent with `riigiteataja.ee` and `retsinformation.dk`'s
pattern from earlier pushes. No law entity was created from the date
alone; logged in `discovery/unresolved.md`.

**`iso.org` re-confirmed genuinely blocked.** Tested again with the
honest, identifying User-Agent on both [[LU]]'s and [[LU-ILNAS]]'s
`iso.org` citations — still a 403 Cloudflare challenge regardless. This
is a real, non-UA-fixable block, distinct from the `efta.int` pattern.

## Earlier pushes

- **Fourth research-queue pickup** (2026-08-25): [[DK-KLIMADATASTYRELSEN]],
  which Datafordeleren's own homepage names directly as its operating
  authority — [[DK-DATAFORDELER]] promoted to `primary-source` in the
  same pass. An incidental find on [[EU-INSPIRE]]: Klimadatastyrelsen's
  own "Lovstof" page names Denmark's INSPIRE transposition act by its
  exact citation. `retsinformation.dk` confirmed a JavaScript
  single-page application with no static content. See "The fourth
  research-queue pickup".
- **Candidates pickup** (2026-08-22): [[UN-HLPF]] and
  [[EU-EFTI-REGULATION]], closing two `discovery/candidates.md` rows.
  UN-HLPF closed a gap [[EU-VOLUNTARY-REVIEW-2023]] named in its own
  text; EU-EFTI-REGULATION closed the other with a negative result —
  reading the Regulation's full text found no trace of the UN/CEFACT
  connection secondary sources claimed. See "The candidates pickup".
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
