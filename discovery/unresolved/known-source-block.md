# Unresolved: Known source block (full detail)

The full text of the "Why it matters / status detail" column for the rows of
[`../unresolved.md`](../unresolved.md) that are too long to read in the table. The master table keeps the
row, its question, status and date and a short excerpt; **edit the long history here**, in the row's
section, and keep the excerpt in the table in step with it. Row numbers are never reused.

<a id="row-216"></a>
## Row 216 — `digitaleoverheid.nl`

*Area: Known source block.*

Confirmed across NL Batch 3 (~10 URLs, two dozen attempts) and the Wdo entity; three specific newer pages **did** load (`/nederlandse-digitaliseringsstrategie-nds/`, `/nieuws-nds/...`, `/overzicht-van-alle-onderwerpen/kabinetsbeleid-digitalisering/`) — not a domain-wide block, just very frequent on older paths. **Workaround found 2026-09-25**: the site's own WordPress REST API (`www.digitaleoverheid.nl/wp-json/wp/v2/pages?slug=<slug>`, or `?search=<term>`) is not blocked and returns the same page content the bot-walled rendered HTML hides — used to read [[NL-CBW]]'s previously-unread `digitaleoverheid.nl` citation directly, surfacing a new sourced link to [[NL-BIO]]. Worth trying on any other `digitaleoverheid.nl` citation this Atlas still records as blocked.

<a id="row-217"></a>
## Row 217 — `bmi.bund.de`, `digitale-verwaltung.de`

*Area: Known source block.*

Confirmed consistent, not transient, across the Germany cluster pass. **Workaround found 2026-09-30 for `bmi.bund.de`**: the HTTP 400 turns out to be a missing session cookie rather than a genuine block — the site's homepage issues a cookie via a redirect that a cookie-less request cannot follow; a cookie-jar-aware fetch reaches every page tried afterwards, including all five of [[DE-BMI]]'s own previously-unread citations. **Confirmed 2026-10-01 to cover `digitale-verwaltung.de` too** (the same Government-Site-Builder CMS issues the same `AL_CHK-S` session cookie via redirect): all four of its previously-unread citations are now read directly — [[DE-FITKO]], [[DE-FIM]], [[DE-BUNDID]] and [[DE-MODERNISIERUNGSAGENDA-FOEDERAL]] — plus [[DE-OZG]]'s FITKO source, `personalausweisportal.de` (same 400-without-cookie behaviour; read for [[DE-BUNDID]]), and the remaining `bmi.bund.de` citations on [[DE-DATENSTRATEGIE]] and [[DE-REGMOG]]. Worth trying on any other government site that answers 400 to a bare request but 200 to a browser. Not every `bmi.bund.de` URL is live: [[DE-IFG]]'s BMI page loads but is an empty stub, and the BMDV press release cited on [[DE-DATENSTRATEGIE]] is genuinely gone (301 then 404).

<a id="row-218"></a>
## Row 218 — `geant.org` family (`geant.org`, `about.geant.org`, `compendium.geant.org`), `dfn.de`, `eduroam.org`

*Area: Known source block.*

Wikipedia/CORDIS/archived-page alternates substituted; `geant.org` itself never read directly. **Corrected 2026-10-01**: `dfn.de` is not blocked — it returns a full page without any cookie, and [[DE-DFN]] already read it directly on 2026-08-28; this row had never been updated. `geant.org`'s subdomains and `eduroam.org` still return a bare 403 (103 bytes) with or without a cookie jar, so they are a genuine block, not a cookie gate.

<a id="row-219"></a>
## Row 219 — `coe.int`, `rm.coe.int`

*Area: Known source block.*

`assembly.coe.int` (a different subdomain) is reachable and closed the last Convention-108-family gap (2026-09-05). **A third subdomain, `edoc.coe.int`, found reachable 2026-09-26** — the Council's own document-publishing site, used to confirm the 46-member-states chart directly on [[INTL-COE]]. `www.coe.int`/`rm.coe.int` themselves remain unread throughout. **Per-country accession dates found 2026-09-30**: `coe.int` itself (including `edoc.coe.int`'s poster page, which only gives the 46-count, not individual countries) still cannot answer *which* country joined *when* — but Wikipedia's own dedicated "Member states of the Council of Europe" article, read directly, carries a sourced per-country accession table. Used to upgrade six country anchors' `part-of` [[INTL-COE]] edges from a retained-but-unconfirmed claim to a dated fact: [[GB]], [[NO]] and [[IT]] (founders, 5 May 1949), [[IS]] (7 March 1950), [[CH]] (6 May 1963) and [[LI]] (23 November 1978). Worth trying on any other country anchor whose CoE edge still lacks a date.

<a id="row-220"></a>
## Row 220 — `iso.org`

*Area: Known source block.*

**Workaround found 2026-09-25**: `iso.org` itself remains blocked, but `isotc.iso.org` and `standards.iteh.ai` (an authorized ISO/IEC standards reseller) are both reachable. `standards.iteh.ai`'s "redline" preview PDFs — free samples at `cdn.standards.iteh.ai/samples/<catalog-number>/.../<name>.pdf` — reproduce a genuine, substantial excerpt of the actual © ISO/IEC standard text (front matter, Foreword, Introduction, opening clauses), not just a catalogue listing. Used to close [[INTL-ISO-IEC-27002]], row #166. **Applied again 2026-09-27** to [[INTL-ISO-IEC-27001]] (catalog 82875) and to substitute for [[INTL-ISO]]'s bot-walled 27000-family landing page with a direct read of ISO/IEC 27000:2018 itself (catalog 73906) — see [[INTL-ISO]]'s own file for the family list this gave. **A second, different workaround found 2026-09-27**: `iso.org/member/<id>.html` (the ISO membership-directory pages cited on several national standards-body entities, e.g. [[PT-IPQ]], [[LU-ILNAS]], [[IE-NSAI]], [[DE-DIN]]) are also domain-wide 403-blocked, but `committee.iso.org/iso/home/about/iso_members.htm` — a different `iso.org` subdomain — is reachable and lists every ISO member body with its TC/PDC participation counts, confirming membership directly rather than requiring a Wikipedia/national-site substitute. **Applied 2026-09-27** to all four entities named above: PT-IPQ's edge restored from `interpretation`/`low` to `fact`/`high`; LU-ILNAS's and IE-NSAI's already-`fact` edges corroborated and raised to `high`; DE-DIN's current membership corroborated (though not its specific 1951 accession year, which the page does not give). This also surfaced and fixed a stale claim on DE-DIN's own file ("the Atlas has never been able to record NL-NEN's ISO membership") that a later 2026-08-27 pass on NL-NEN had already made untrue. **Applied once more 2026-09-30** to [[LU]]'s own country-anchor file, the last remaining `iso.org/member/<id>.html` citation in the Atlas: `committee.iso.org` corroborates ILNAS's "Member body" tier with the same 176 TC/3 PDC participation counts already confirmed on [[LU-ILNAS]]'s own file. Worth trying on any other ISO/IEC-family citation this Atlas still records as blocked. **Re-tested 2026-10-07 with the fetch tool**: `iso.org/standard/27001` still returns 403.

<a id="row-223"></a>
## Row 223 — `eur-lex.europa.eu`

*Area: Known source block.*

Later passes (2026-09-05 onward) found the **TXT/HTML URL form** (`legal-content/EN/TXT/HTML/?uri=...`) works where other forms fail, closing several previously-stuck dates (EU-VOLUNTARY-REVIEW-2023, EU-DIGITAL-OMNIBUS-AI). Plain-parameter forms and homepage-directory URLs still tend to redirect to a generic "today's Official Journal" listing rather than the requested document. **Refined 2026-09-06** (EU-HVD-REGULATION): even within the TXT/HTML form, the CELEX URI must use a **plain colon** (`uri=CELEX:32023R0138`) — the percent-encoded form (`uri=CELEX%3A32023R0138`) returned empty content on the same document, as did the PDF form. **Re-tested 2026-10-07 with the fetch tool (`WebFetch`; curl is still blocked)**: the national-implementation-measures form `legal-content/EN/NIM/?uri=CELEX:32019L1024` read in full for Belgium (11 measures with titles and publication dates) and, for France, up to item 51, where the tool's page limit (about 100,000 characters) cut it off: read on with the tool's `offset`. So a transposition question that was "not identified" can now be answered from the Commission's own list, one page-chunk at a time. Results differ by tool, URL form and day; a failure is not proof of a block.

**Resolver workaround found 2026-10-10**: `https://publications.europa.eu/resource/celex/<CELEX>` read with curl and the headers `Accept: application/xhtml+xml` and `Accept-Language: eng` returns the full Official Journal text of an act (tested on Regulation (EU) No 910/2014, 124,000 characters), where `eur-lex.europa.eu`'s `TXT/HTML` form is empty for it; `Accept: application/pdf` returns the PDF; plain `text/html` answers 404.

<a id="row-225"></a>
## Row 225 — `efta.int`, EEA Joint Committee Decision texts on EUR-Lex's EEA supplement

*Area: Known source block.*

Blocked the direct sourcing of Norway/EEA questions #105, #109 and #178, all now closed. **Workaround found 2026-09-19**: `efta.int`'s `eea-lex` viewer and homepage stay bot-walled, but its document-store path (`efta.int/sites/default/files/documents/legal-texts/eea/other-legal-documents/adopted-joint-committee-decisions/YYYY - English/NNN-YYYY.pdf`) serves adopted Joint Committee decisions' PDFs directly — used to close [[INTL-EEA-JCD-154-2018]] and create [[INTL-EEA-JCD-22-2018]]. Worth trying on any other JCD citation this Atlas still records as blocked. **Re-tested 2026-10-07 with the fetch tool**: the `efta.int` homepage is now readable ("Homepage \| European Free Trade Association"); the document-store path above is still the route for decision PDFs.

<a id="row-235"></a>
## Row 235 — Which blocked hosts a GitHub runner can read

*Area: Known source block.*

**Readable from a runner with the honest User-Agent, though not from the agent's environment**: `efta.int` (all four pages), `bosa.belgium.be`, `data.gov.be` and `financien.belgium.be` (Belgium), `legislation.gov.uk`, `web.archive.org`, `bizkaia.eus`, `edoc.coe.int`, `committee.iso.org`, `legalinstruments.oecd.org` and `oecdgroups.oecd.org`, three `digitaleoverheid.nl` paths, and the filestore subdomains `data.legilux.public.lu`, `files.dre.pt` and Fedlex's `filestore` (full documents). **A browser-like User-Agent was worse, not better**: it turned `efta.int` and all three Belgian federal hosts from readable into a challenge page, so the honest agent should stay the default. **Still blocked from a runner**: `unece.org` and `unctad.org`, `rm.coe.int` and the bare `coe.int`/`iso.org`/`oecd.org` roots (bot-defence challenge); `eur-lex.europa.eu` (HTTP 202 with nothing: a challenge in progress); `geant.org`, `eduroam.org`, `ccb.belgium.be`; `bmi.bund.de` and `digitale-verwaltung.de` (HTTP 400, the missing-session-cookie case of row #217; one probe also timed out); the JavaScript shells `fedlex.admin.ch` (its pages answer every address with the same 2,383 characters: the probe counted them readable until a same-text check was added), `diariodarepublica.pt` and the main `legilux.public.lu`. **What this does not do**: a runner's pages are read by the workflow, not by the agent; to use one, put its address in the workflow's host list and read the artifact, which this probe does not yet offer (a fetch-these-URLs input would). The UN CES seat question (#459) stays blocked because `unece.org` is. **Added 2026-10-10 (standards bodies, #501)**: from a runner `iso.org` (about-us, history, members), `unece.org/trade/uncefact` and `iec.ch/history` still answer 403, `committee.iso.org/home/jtc1` answers 400, `ilnas.public.lu` fails certificate verification (hostname mismatch), while `nen.nl/over-nen`, `bsigroup.com` history and `ipq.pt` read.
