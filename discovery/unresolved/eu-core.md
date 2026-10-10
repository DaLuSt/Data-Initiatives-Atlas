# Unresolved: EU core (full detail)

The full text of the "Why it matters / status detail" column for the rows of
[`../unresolved.md`](../unresolved.md) that are too long to read in the table. The master table keeps the
row, its question, status and date and a short excerpt; **edit the long history here**, in the row's
section, and keep the excerpt in the table in step with it. Row numbers are never reused.

<a id="row-35"></a>
## Row 35 — [[EU-EIDAS]]

*Area: EU core.*

Created purely so the [[NL-WDO]] question is expressible; its only source is the amending regulation. **Narrowed 2026-09-19**: its enactment date (23 July 2014), OJ citation, and EEA-EFTA applicability (via [[INTL-EEA-JCD-22-2018]], read directly) are now sourced. The regulation's own structure and trust-services provisions remain unresearched. **Partly narrowed 2026-09-25**: trust-services categories (electronic signatures, seals, qualified certificates) are now recorded in prose, sourced from Wikipedia only — `eur-lex.europa.eu`'s TXT/HTML form, which has worked for other EU instruments, returned empty content for this specific regulation on every attempt. **Structurally narrowed 2026-09-26**: `eur-lex.europa.eu` still returns empty content, but `legislation.gov.uk`'s own mirror of the UK-retained text, read directly, gives the full six-chapter structure and article-level detail for each trust service (signatures Art. 25-26, seals Art. 35-36, time stamps Art. 41, registered delivery Art. 43, website authentication Art. 45) — treated as reliable for structure/numbering, not as authoritative for the EU's own current in-force text, since it is UK-retained law. `coverage` raised to medium.

<a id="row-43"></a>
## Row 43 — [[EU-EMDS]] ↔ [[NL-NTM]]

*Area: EU core.*

**Narrowed 2026-09-05**: the EU-level half is sourced — transport.ec.europa.eu's own page states the EMDS "will take account of" the ITS Directive's NAP mechanism, recorded as `references` → [[EU-ITS-DIRECTIVE]]. No source names NL-NTM or any specific national NAP; the country-level link stays association-only. **Strengthened to a documented negative, 2026-09-25**: deployEMDS's own site, read directly, names nine participating countries in its first deployment project, and the Netherlands is not among them — despite having one of Europe's best-documented national access points. Silence from a source that would plausibly mention NL-NTM if any connection existed.

<a id="row-44"></a>
## Row 44 — [[EU-OPEN-DATA-DIRECTIVE]]

*Area: EU core.*

Nineteen member states faced infringement proceedings; four (Belgium, Bulgaria, Latvia, the Netherlands) were referred to the CJEU in Feb 2023. **Narrowed 2026-09-05**: the missing node now exists ([[EU-CJEU]]). **Further narrowed 2026-09-20**: the missing relationship type now exists too — `referred-to-court-over` (metadata/relationship-types.md §2.1) — applied to [[BE-HERGEBRUIK-WET-2023]] and [[NL-WHO]], plus (for the same escalation over NIS2) [[IE-NCS-BILL]], [[ES-LCGC]], [[FR-NIS2-LOI]] and [[NL-CBW]]. This also caught and fixed a stale claim on [[EU-NIS2]] wrongly stating Poland was referred (it was not, per [[PL-KSC]]'s own corrected record). Bulgaria and Latvia still lack a modelled transposing instrument to carry the edge — a scoping gap, not a vocabulary one. **Closed 2026-09-25**: both are now modelled, [[BG-ZDOI]] (Bulgaria's Access to Public Information Act, whose own 2023-amendment §1a states in so many words that it introduces Directive (EU) 2019/1024) and [[LV-IAL]] (Latvia's Informācijas atklātības likums, which names the directive in its own EU-directive reference section) — both now carrying `implements-requirement-from` this directive and `referred-to-court-over` [[EU-CJEU]], completing the February 2023 referral quartet. Only the entity-type question (an individual infringement procedure as a first-class object with its own stages) remains open.
