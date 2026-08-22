# Current Batch

**Status:** No batch in progress. **The verification-gap multi-batch push**
completed on 2026-08-22. Full detail moved to `progress/completed.md`;
summary below. ~378 entities remain `verification: search-only`/`unverified`
(138 now `primary-source`); `discovery/reverification-allowlist.md` ranks
the next targets. Skip entities citing only `eur-lex.europa.eu`,
`www.iso.org`, `www.coe.int` or `unece.org` — those hosts return a
bot-defense challenge page to every fetch in this environment, egress
policy notwithstanding.

## In brief

Worked four clusters end to end — read every cited page, corrected what
needed correcting, and ran `tools/reverify.py --write` per entity — rather
than spreading effort thin across unrelated files:

- **German intelligence oversight** (10 entities: DE-BFDI, DE-BVERFSCHG,
  DE-G10, DE-MADG, DE-BAMAD, DE-BFV, DE-BND, DE-PKGR, DE-PKGRG, DE-UKR).
  Confirmed the PKGrG's Constitutional Court dispute mechanism in the
  statute's own § 14, and traced DE-BND's "28 September 2022" UKR claim to
  a source that turned out to be about an unrelated ruling — the claim was
  right, the citation was wrong, now fixed and re-sourced.
- **German digital-government legislation and strategy** (14 entities:
  DE-BNDG, DE-BSTATG, DE-DNG, DE-EGOVG, DE-IFG, DE-DATENSTRATEGIE,
  DE-DIGITALSTRATEGIE, both Modernisierungsagenda entities, DE-BMDS,
  DE-DEUTSCHLAND-STACK, DE-BUNDID, DE-GDNG, DE-GEMATIK). Found a genuine
  date error (DE-EGOVG's in-force date was 1 August 2013, not 31 August),
  closed two "no date established" gaps with real dates, and closed a
  gap DE-BUNDID had explicitly flagged (its EUDI-Wallet connection, now
  sourced). DE-DIGITALSTRATEGIE was read and confirmed via a PDF report,
  but stays `search-only`: `tools/reverify.py` cannot text-extract a PDF,
  so it cannot corroborate a claim only that PDF states — documented
  rather than forced.
- **UK intelligence oversight** (10 entities: GB-ISA-1994, GB-SSA-1989,
  GB-JSA-2013, GB-IPA-2016, GB-DPA-2018, GB-GCHQ, GB-MI5, GB-SIS, GB-ISC,
  GB-IPCO). `legislation.gov.uk` was believed blocked by this
  environment's egress proxy; it is not, and every entity that carried
  that caveat was wrong. Replaced three placeholder dates
  (`YYYY-01-01`) with the acts' actual enactment/commencement dates.
- **UK data protection** (3 entities: GB-UK-GDPR, GB-DUAA, GB-ICO).
  GB-UK-GDPR's canonical name never appeared in any source read — every
  source calls it "UK GDPR" — so the entity was renamed to match actual
  usage. GB-ICO's open question (has the Information Commission replaced
  it yet?) got one weak, explicitly-labelled signal: Wikipedia's infobox
  currently shows the Information Commissioner as vacant.

37 entities moved from `search-only` to `primary-source` in total (one,
DE-DIGITALSTRATEGIE, stayed `search-only` for the PDF-extraction reason
above despite being fully read). Full write-up, evidence quotes and the
complete list of corrections are in `progress/completed.md` under "The
verification-gap multi-batch push".
