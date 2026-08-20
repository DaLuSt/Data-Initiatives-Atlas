#!/usr/bin/env python3
"""Validate source metadata: well-formed entries, plausible URLs, and a
warning (not a hard failure) when a non-stub entity has no sources at all."""

from __future__ import annotations

import re
import sys

import common

REQUIRED_SOURCE_FIELDS = ("title", "url", "publisher")


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

        for i, src in enumerate(sources):
            where = f"{e.rel_path}: sources[{i}]"
            if not isinstance(src, dict):
                report.error(f"{where} is not a mapping")
                continue
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
            # Plain HTTP is a warning, not an error: a handful of legacy
            # academic and government hosts genuinely do not serve https, and
            # that is outside this repository's control. But a government
            # citation over http is usually a stale URL rather than a real
            # constraint — all three espanadigital.gob.es citations were,
            # found when the repository owner manually checked the
            # highest-value hosts on 2026-08-20 and reported gob.es as the one
            # inaccurate domain.
            if url.startswith("http://"):
                report.warn(f"{where}: url is plain http, not https — check whether "
                            f"the citation is stale: {url}")
            if url and re.search(r"[\s\x00-\x1f]", url):
                report.error(f"{where}: url contains whitespace or a control "
                             f"character and cannot be fetched — percent-encode "
                             f"it: {url!r}")

    return report.print_and_exit_code()


if __name__ == "__main__":
    sys.exit(main())
