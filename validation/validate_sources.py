#!/usr/bin/env python3
"""Validate source metadata: well-formed entries, plausible URLs, and a
warning (not a hard failure) when a non-stub entity has no sources at all."""

from __future__ import annotations

import re
import sys
from urllib.parse import urlparse

import common

REQUIRED_SOURCE_FIELDS = ("title", "url", "publisher")

# Domains whose pages the repository owner confirmed read and correct on
# 2026-08-21 (docs/re-verification.md, "The confirmed domains"). An entity all of
# whose sources are on these needs no per-page `accessed` date to be
# `primary-source`: the confirmation covers them.
CONFIRMED_DOMAINS = ("europa.eu", "iso.org", "coe.int", "bund.de", "legifrance.gouv.fr")


def on_confirmed_domain(url: str) -> bool:
    host = (urlparse(url).hostname or "").lower()
    return any(host == d or host.endswith("." + d) for d in CONFIRMED_DOMAINS)


def check_primary_source_basis(rel_path: str, sources: list, report: common.Report) -> None:
    """`verification: primary-source` means the cited pages were read. That has to
    be visible in the file: at least one source with an `accessed` date, or every
    source on a domain the owner confirmed (CONFIRMED_DOMAINS). An entity with no
    sources (a domain or anchor) has nothing to confirm and is not checked."""
    dicts = [s for s in sources if isinstance(s, dict)]
    if not dicts:
        return
    if any(s.get("accessed") for s in dicts):
        return
    if all(on_confirmed_domain(str(s.get("url") or "")) for s in dicts):
        return
    report.error(f"{rel_path}: verification is 'primary-source' but no source has an 'accessed' "
                 f"date and not every source is on a confirmed domain "
                 f"({', '.join(CONFIRMED_DOMAINS)}) — add the date the pages were read, or "
                 f"lower verification")


def main() -> int:
    entities = common.load_all_entities()
    report = common.Report("validate_sources")

    for e in entities:
        if e.parse_error:
            continue  # already reported by validate_frontmatter

        fm = e.frontmatter
        sources = fm.get("sources") or []

        if not isinstance(sources, list):
            report.error(f"{e.rel_path}: 'sources' must be a list")
            continue

        if not sources:
            # Domains are taxonomy/classification nodes rather than researched
            # entities: they carry no factual claims, so they need no sources.
            if fm.get("type") == "domain":
                continue
            if fm.get("status") not in ("unknown", "proposed") or fm.get("coverage") not in ("low",):
                report.warn(f"{e.rel_path}: no sources listed for an entity with status "
                            f"'{fm.get('status')}' / coverage '{fm.get('coverage')}'")
            continue

        if fm.get("verification") == "primary-source":
            check_primary_source_basis(e.rel_path, sources, report)

        seen_urls: dict[str, int] = {}
        for i, src in enumerate(sources):
            where = f"{e.rel_path}: sources[{i}]"
            if not isinstance(src, dict):
                report.error(f"{where} is not a mapping")
                continue
            if src.get("url"):
                if src["url"] in seen_urls:
                    report.warn(f"{where}: url already cited at sources[{seen_urls[src['url']]}]: {src['url']}")
                else:
                    seen_urls[src["url"]] = i
            if src.get("accessed") not in (None, ""):
                day = common.as_date(src["accessed"])
                if day is None:
                    report.error(f"{where}: accessed '{src['accessed']}' is not a YYYY-MM-DD date")
                elif common.is_in_the_future(day):
                    report.error(f"{where}: accessed {day} is in the future")
            for field_name in REQUIRED_SOURCE_FIELDS:
                if not src.get(field_name):
                    report.error(f"{where}: missing '{field_name}'")
            url = src.get("url", "")
            if url and not (url.startswith("http://") or url.startswith("https://")):
                report.error(f"{where}: url '{url}' does not look like a real http(s) URL")
            # A URL containing raw whitespace or a control character cannot be
            # fetched: http.client refuses to put it in a request line. Every
            # such URL is silently un-re-verifiable, which is exactly the debt
            # this repository is trying to pay down — so it is an error, not a
            # warning. Found by the first full run of tools/reverify.py, which
            # it crashed. Percent-encode the offending characters.
            # Plain HTTP is a warning, not an error, and it is about transport
            # rather than correctness: some hosts genuinely do not serve https
            # and that is outside this repository's control. A cited page
            # fetched over http cannot be trusted not to have been modified in
            # transit, which matters for a repository whose whole claim is
            # provenance.
            #
            # It is deliberately *not* evidence that a URL is stale. This check
            # was first written on that assumption, about three
            # espanadigital.gob.es citations, and the assumption was wrong —
            # they work. See progress/completed.md, 2026-08-20.
            if url.startswith("http://"):
                report.warn(f"{where}: cited over plain http, so the page cannot be "
                            f"fetched with integrity — prefer https if the host "
                            f"offers it: {url}")
            if url and re.search(r"[\s\x00-\x1f]", url):
                report.error(f"{where}: url contains whitespace or a control "
                             f"character and cannot be fetched — percent-encode "
                             f"it: {url!r}")

    return report.print_and_exit_code()


if __name__ == "__main__":
    sys.exit(main())
