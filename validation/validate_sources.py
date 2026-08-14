#!/usr/bin/env python3
"""Validate source metadata: well-formed entries, plausible URLs, and a
warning (not a hard failure) when a non-stub entity has no sources at all."""

from __future__ import annotations

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

    return report.print_and_exit_code()


if __name__ == "__main__":
    sys.exit(main())
