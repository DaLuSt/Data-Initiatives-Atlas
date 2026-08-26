# Current Batch

**Status:** No batch in progress. **The tenth verification-gap push**
completed on 2026-08-26 — the entire France cluster (22 entities), the
last country whose whole cluster was still untouched. Full detail moved
to `progress/completed.md`; summary below. `discovery/reverification-allowlist.md`
ranks the next re-verification targets, and `discovery/research-queue.md`
carries the rest of the research backlog.

**Tail pushes, not fresh clusters.** Countries whose anchor and most
entities are `primary-source` can still carry a handful of
`verification: search-only` stragglers — entities added or left behind
after the country's main re-verification pass. [[DK]] (4) and [[SE]]
(3) were closed by the eighth and ninth pushes; [[FR]]'s entire cluster
(22 entities, one straggler — [[FR-DGSI]]) was closed by the tenth.
`NL` (67), `DE` (27), `BE` (24), `ES` (22), `PL` (18), `PT` (8), `EE`
(7), `CZ` (7), `FI` (6) and `AT` (3) still carry some tail entities.
No country now has an entirely untouched cluster.

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
pickup, and reconfirmed dead in the eighth push. `consilium.europa.eu`
was tested for the first time this session in the seventh push and is
genuinely blocked (403) even with an honest User-Agent. `bosettiegatti.eu`,
an Italian legal-text mirror cited on the Italy cluster, is the
**first host found doing the reverse of `efta.int`**: it returns a
custom IIS "999" bot-defense error to the honest, identifying
User-Agent `tools/reverify.py` sends, but serves the page normally
(`200`) to a browser-spoofing one — found in the seventh
verification-gap push, researching [[IT-CAD]]. `legifrance.gouv.fr`
(specifically its JORF text pages), `interieur.gouv.fr` (including the
`dgsi.interieur.gouv.fr` subdomain), `economie.gouv.fr` and `lejdd.fr`
were all tested with both an honest and a browser-spoofing User-Agent
in the tenth push and are genuinely blocked (403) either way — note
that this contradicts an earlier note elsewhere in the repo that
Légifrance was confirmed readable on 2026-08-21; that confirmation
evidently no longer holds, or covered different pages.
`guides.etalab.gouv.fr` and `www.drsd.defense.gouv.fr` no longer
resolve at all (checked via direct DNS lookup) — dead domains,
superseded respectively by `guides.data.gouv.fr` and pages under
`www.defense.gouv.fr/drsd/`. `sante.gouv.fr`'s Health Data Hub PDF
returns HTTP 200 but the body is actually an HTML page carrying an
F5/TSPD JavaScript bot-defense challenge, not a real PDF — a genuine
block, not a parsing failure.

## The tenth verification-gap push — 2026-08-26

Re-verified the entire France cluster (22 entities), the last country
whose whole cluster was still untouched. 21 entities promoted to
`verification: primary-source`; [[FR-DGSI]] stays `search-only` — only
one of its four cited sources (`cnctr.fr`) could be read, the other
three being genuinely blocked `interieur.gouv.fr`/`dgsi.interieur.gouv.fr`
pages, and a single reachable source among several is not enough to
justify promotion (contrast the "one dead/unread source among many"
exception used elsewhere this session for `iso.org` and similar).

**[[FR-NIS2-LOI]]'s direct sourcing contradiction, resolved.** The
entity previously carried `status: unknown` because its sources gave
two directly contradictory accounts — one asserting the bill was
already law (n° 2025-90 of 26 February 2025), the other that it
remained a Senate-passed bill awaiting promulgation. Three independent
sources plus ANSSI's own official MonEspaceNIS2 page, all read this
pass, agree the bill was still unpromulgated as of 6 August 2026; only
one uncorroborated source asserted the "already law" account. Status
changed to `planned`, confidence to `medium`.

**A genuine pre-existing bug found and fixed on [[FR-RGI]].** Its
frontmatter asserted a `based-on` [[EU-EIF]] relationship that the
entity's own body text explicitly refused. The relationship has been
removed.

**Three founding-date/legal-citation gaps closed.** [[FR-DRM]]'s
founding decree (16 June 1992, Décret n° 92-523) and [[FR-DRSD]]'s
precise legal basis (Article D3126-5, Code de la Défense) plus its 2016
renaming from the DPSD, both found via an academic paper on
`afdsd.fr`. [[FR-ETALAB]]'s actual founding date (21 February 2011) was
found via fr.wikipedia.org, correcting a previously wrong date that
conflated founding with its later 2019 DINUM-department reorganisation.

**Two new entities created from the research queue, now populated
rather than queued.** [[FR-INSEE]], the last Atlas country left without
a national statistical office, closing the [[EU-ESS]] gap named since
the France batch; [[FR-AFNOR]], the national standards body, confirmed
by name on `standards.cencenelec.eu`'s own member list. An unsupported
claim on [[FR-INSEE]] ("French branch of Eurostat") was traced to a
login-gated, content-free European Commission shell page and dropped
rather than carried forward unverified.

## The ninth verification-gap push — 2026-08-25

Closed Sweden's tail: [[SE-DATAPORTAL]], [[SE-DIGG]] and [[SE-SCB]],
the three Swedish entities still `verification: search-only` after
Sweden's country anchor and [[SE-IMY]] had already been re-verified.
All three now carry `verification: primary-source`.

**[[SE-DIGG]]'s custodianship of [[SE-DATAPORTAL]], confirmed almost
word for word.** dataportal.se's own "Om oss" page states directly:
"(Digg) ansvarar för Sveriges dataportal" (DIGG is responsible for
Sweden's data portal), matching the `maintained-by` edge and the
"public and private organisations" framing this entity already
carried, unread, since creation.

**[[SE-SCB]]'s [[EU-ESS]] membership stays on the composition-rule
tier.** scb.se's own "About us" page confirms Statistics Sweden's
identity directly ("responsible for official statistics and for other
government statistics") but does not name Eurostat or the ESS — the
same honest call made on [[LU-STATEC]] and [[DK-DST]] in earlier
passes.

## The eighth verification-gap push — 2026-08-25

Closed Denmark's tail: [[DK-GRUNDDATA]], [[DK-DATATILSYNET]],
[[DK-SUNDHEDSDATASTYRELSEN]] and [[DK-DST]], the four Danish entities
still `verification: search-only` after Denmark's country anchor and
other entities had already been re-verified across earlier pushes. All
four now carry `verification: primary-source`.

**A 2012 origin for [[DK-GRUNDDATA]].** A European Commission ISA2
conference document, read directly, dates the Basic Data Programme
precisely: established in 2012 as part of an e-government strategy
agreed between the Danish state, Local Government Denmark and the
Danish regions — a fact this entity did not previously carry.
`grunddata.dk` remains dead, reconfirmed again this pass.

**[[DK-DST]]'s legal basis, named but not read.** Statistics Denmark's
own "role and mandate" page states directly it is "responsible for
official statistics in Denmark, as established by the Act on
Statistics Denmark" and has operated since 1850. The Act's own citation
was not read, so no legislation entity was created from the name
alone. Its [[EU-ESS]] membership, like [[LU-STATEC]]'s in an earlier
pass, stays on the composition-rule tier — no page read this pass has
Statistics Denmark describe ESS membership in its own words.

## Earlier pushes

- **Seventh verification-gap push** (2026-08-25): the entire Italy
  cluster (6 entities). Fixed a stale country anchor still claiming
  Italy had "no national entities"; closed [[IT-DATI-GOV-IT]]'s
  custodian gap ([[IT-AGID]] since 2015); upgraded [[IT-ISTAT]]'s
  [[EU-ESS]] membership to a direct statement; found `bosettiegatti.eu`
  blocks the honest User-Agent but not a browser-spoofing one, the
  mirror image of the `efta.int` finding. See "The seventh
  verification-gap push".
- **Sixth verification-gap push** (2026-08-25): the entire Luxembourg
  cluster (6 entities). Found [[LU-ILNAS]]'s sixth standardisation
  membership (the ITU), breaking its tie with [[GB-BSI]], and sourced
  Luxembourg's GDPR act date via an ELI URL without creating a law
  entity from it. See "The sixth verification-gap push".
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
